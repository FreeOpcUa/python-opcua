
import os.path
import time
import datetime
from struct import pack

from opcua import ua
from opcua.ua.uatypes import NumericNodeId, NodeIdType
from opcua.common.utils import Buffer
from opcua.common.sqlite3_backend import SQLite3Backend
from opcua.server.address_space import NodeData, AddressSpace, AttributeValue

class ReadOnlyException(Exception):
    pass


class MonitoredAttribute(AttributeValue):

    def __init__(self, attr, onchange_cb):
        self._value = attr.value
        self.value_callback = attr.value_callback
        self.datachange_callbacks = attr.datachange_callbacks
        self.onchange_cb = onchange_cb

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, newVal):
        self._value = newVal
        self.onchange_cb()

class MonitoredNode(object):

    def __init__(self, aspace, ndata):
        self._aspace = aspace
        self._nodeid = AddressSpaceSQLite._nodeid_to_numeric(ndata.nodeid)

    @property
    def aspace(self):
        return self._aspace

    @property
    def nodeid(self):
        return self._nodeid


class MonitoredAttributeDict(MonitoredNode, dict):

    def __init__(self, aspace, ndata):
        MonitoredNode.__init__(self, aspace, ndata)
        for attrId, attr in ndata.attributes.items():
            self[attrId] = attr

    def __setitem__(self, attrId, attr):
        def onchange_cb():
            self.aspace._insert_attribute_threadsafe(self.nodeid, attrId, self[attrId])
        mAttr = MonitoredAttribute(attr, onchange_cb)
        dict.__setitem__(self, attrId, mAttr)
        mAttr.onchange_cb()

    def __delitem__(self, attrId):
        raise NotImplementedError


class MonitoredReferenceList(MonitoredNode, list):

    def __init__(self, aspace, ndata):
        MonitoredNode.__init__(self, aspace, ndata)
        list.__init__(self, ndata.references)

    def append(self, ref):
        list.append(self, ref)
        self._aspace._insert_reference_threadsafe(self.nodeid, ref)

    def remove(self, ref):
        raise NotImplementedError


class AddressSpaceSQLite(AddressSpace):
    """
    Load the standard address space nodes from a SQLite database.
    Intended for slow devices, such as Raspberry Pi, to greatly improve start up time
    """
    ATTR_TABLE_NAME = 'Attributes'
    REFS_TABLE_NAME = 'References'
    CUR_TIME_NODEID = NumericNodeId(ua.ObjectIds.Server_ServerStatus_CurrentTime, 0)

    def __init__(self, backend, cache=None):
        super(AddressSpaceSQLite, self).__init__(cache)
        self._backend = backend

    def __enter__(self):
        super(AddressSpaceSQLite, self).__enter__()
        AddressSpaceSQLite._create_attr_table(self.backend)
        AddressSpaceSQLite._create_refs_table(self.backend)
        return self

    def __str__(self):
        return str(self.backend)

    @property
    def backend(self):
        return self._backend

    @property
    def readonly(self):
        return self.backend.readonly

    def __getitem__(self, nodeid):
        with self._lock:
            (nodeData, fromDisk) = self._getitem_backend(nodeid)
            return nodeData

    def _getitem_backend(self, nodeid):
        try:
            if not hasattr(self._cache, '_getitem_backend'):
                (nodeData, fromDisk) = (self._cache.__getitem__(nodeid), False)
            else:
                (nodeData, fromDisk) = self._cache._getitem_backend(nodeid)
                if fromDisk:
                    AddressSpaceSQLite._read_nodedata(self.backend, nodeid, nodeData)
                    if not (self.readonly is True or hasattr(nodeData.attributes, 'aspace')):
                        self._monitor_nodedata(nodeData)
        except KeyError:
            (nodeData, fromDisk) = (NodeData(nodeid), True)
            AddressSpaceSQLite._read_nodedata(self.backend, nodeid, nodeData)
            if len(nodeData.attributes) is 0:
                raise
            elif self.readonly is False:
                self._monitor_nodedata(nodeData)
            self._cache[nodeid] = nodeData
        return (nodeData, fromDisk)

    def _monitor_nodedata(self, ndata):
        if self.readonly is True:
            raise ReadOnlyException(ndata.nodeid)
        elif hasattr(ndata.attributes, 'aspace') and ndata.attributes.aspace is not self:
            other = str(ndata.attributes.aspace)
            raise Exception('Node {:s} is monitored by {:s}'.format(str(ndata.nodeid), other))
        elif hasattr(ndata.references, 'aspace') and ndata.references.aspace is not self:
            other = str(ndata.attributes.aspace)
            raise Exception('Node {:s} is monitored by {:s}'.format(str(ndata.nodeid), other))
        else:
            ndata.attributes = MonitoredAttributeDict(self, ndata)
            ndata.references = MonitoredReferenceList(self, ndata)

    def get(self, nodeid, value=None):
        try:
            return self[nodeid]
        except KeyError:
            return value

    def __contains__(self, nodeid):
        return self.get(nodeid) is not None

    def __setitem__(self, nodeid, ndata):
        self._cache.__setitem__(nodeid, ndata)
        if self.readonly is True:
            return
        with self._lock:
            self._setitem_backend(nodeid, ndata)

    def _setitem_backend(self, nodeid, ndata):
        if not hasattr(ndata.attributes, 'aspace'):
            self._monitor_nodedata(ndata)

        if ndata.attributes.aspace is self:
            self._write_nodedata(ndata)
            self.backend.commit()

    @staticmethod
    def _nodeid_to_numeric(nodeid):
        assert(isinstance(nodeid, ua.uatypes.NodeId))
        # For database lookups, map TwoByte and FourByte onto NumericNodeId.
        if nodeid.NodeIdType == NodeIdType.Numeric:
            return nodeid
        if nodeid.NodeIdType in (NodeIdType.TwoByte, NodeIdType.FourByte):
            return NumericNodeId(nodeid.Identifier, nodeid.NamespaceIndex)
        else:
            raise Exception('NodeIdType {:d} is not supported for backend lookups.'.format(nodeid.NodeIdType))

    def keys(self):
        raise Exception("dict.keys() is not supported for performance. Use iterator.")
        
    def __delitem__(self, key):
        # TODO only deleting items from the cache is implemented.
        super(AddressSpaceSQLite, self).__delitem__(key)
    
    def __iter__(self):
        # TODO only the cache can be iterated over.
        return super(AddressSpaceSQLite, self).__iter__()
    
    def __len__(self):
        # TODO only returns the length of items in the cache.
        return super(AddressSpaceSQLite, self).__len__()

    def dump(self, namespaceidx=AddressSpace.DEFAULT_USER_NAMESPACE_INDEX):
        """
        Dump address space into a database; note that server must be stopped for this method to work
        Note 1: DO NOT DUMP AN ADDRESS SPACE RESTORED FROM DATABASE, ONLY CACHED NODES WILL GET DUMPED!
        Note 2: If a NodeData instance holds a reference to a method call, it is not preserved.
        Note 3: numeric nodeid's are required for database searches.
        """
        with self._lock:
            self._dump(namespaceidx)
            self.backend.commit()
        print("Export to {:s} completed".format(str(self.backend)))

    def _dump(self, namespaceidx=AddressSpace.DEFAULT_USER_NAMESPACE_INDEX):
        # 1. Create tables.
        AddressSpaceSQLite._create_attr_table(self.backend, drop=True)
        AddressSpaceSQLite._create_refs_table(self.backend, drop=True)

        # 2. Populate.
        for nodeid, ndata in self._cache.items():
            assert(nodeid == ndata.nodeid)
            assert(isinstance(ndata, NodeData))
            if nodeid.NamespaceIndex == namespaceidx:
                self._write_nodedata(ndata)
                continue
            # inter-namespace references.
            for ref in ndata.references:
                if ref.NodeId.NamespaceIndex != namespaceidx:
                    continue
                numNodeId = AddressSpaceSQLite._nodeid_to_numeric(ndata.nodeid)
                self._insert_reference(numNodeId, ref)

        # 3. Integrity checks.
        for nodeid, ndata in self._cache.items():
            if nodeid.NamespaceIndex != namespaceidx:
                continue
            ndata2 = NodeData(nodeid)
            AddressSpaceSQLite._read_nodedata(self.backend, nodeid, ndata2)
            AddressSpaceSQLite._cmp_nodedata(ndata, ndata2)

    # Write NodeData to database
    def _write_nodedata(self, ndata):
        numNodeId = AddressSpaceSQLite._nodeid_to_numeric(ndata.nodeid)
        self._write_attributes(numNodeId, ndata)
        self._write_references(numNodeId, ndata)

    def _write_attributes(self, nodeid, ndata):
        assert(nodeid.NodeIdType == NodeIdType.Numeric)
        assert(isinstance(ndata.attributes, dict))
        for attrId, attr in ndata.attributes.items():
            AddressSpaceSQLite._insert_attribute(self.backend, nodeid, attrId, attr)

    def _write_references(self, nodeid, ndata):
        assert(nodeid.NodeIdType == NodeIdType.Numeric)
        assert(isinstance(ndata.references, list))
        for ref in ndata.references:
            AddressSpaceSQLite._insert_reference(self.backend, nodeid, ref)

    # Read NodeData from database
    @staticmethod
    def _read_nodedata(backend, nodeid, ndata):
        # Search key = numeric nodeid in opc-ua binary format
        numNodeId = AddressSpaceSQLite._nodeid_to_numeric(nodeid)
        hexNodeId = ua.ua_binary.nodeid_to_binary(numNodeId).hex()

        AddressSpaceSQLite._read_attributes(backend, hexNodeId, ndata)
        AddressSpaceSQLite._read_references(backend, hexNodeId, ndata)

    @staticmethod
    def _read_attributes(backend, hexNodeId, ndata, attrTable=ATTR_TABLE_NAME):
        cmd = 'SELECT * FROM "{tn}" WHERE NodeId = x\'{h}\''.format(tn=attrTable, h=hexNodeId)
        def CB(row):
            (attrId, attr) = AddressSpaceSQLite._read_attribute_row(row)
            ndata.attributes[attrId] = attr
        backend.execute_read(cmd, CB=CB)

    @staticmethod
    def _read_references(backend, hexNodeId, ndata, refsTable=REFS_TABLE_NAME):
        cmd = 'SELECT * FROM "{tn}" WHERE NodeId = x\'{h}\''.format(tn=refsTable, h=hexNodeId)
        def CB(row):
            ref = AddressSpaceSQLite._read_reference_row(row)
            ndata.references.append(ref)
        backend.execute_read(cmd, CB=CB)

    # Read and write from attribute table
    @staticmethod
    def _create_attr_table(backend, table=ATTR_TABLE_NAME, drop=False):
        ATTR_TABLE_COLS = [
            '_Id BLOB PRIMARY KEY NOT NULL', # 0
            'NodeId BLOB',                   # 1
            'AttributeId INTEGER',           # 2
            'ServerTimestamp TIMESTAMP',     # 3
            'ServerPicoseconds INTEGER',     # 4
            'SourceTimestamp TIMESTAMP',     # 5
            'SourcePicoseconds INTEGER',     # 6
            'StatusCode INTEGER',            # 7
            'Variant BLOB',                  # 8
            'Description STRING',            # 9
        ]
        if drop is True:
            dropCmd = 'DROP TABLE IF EXISTS "{tn}"'.format(tn=table)
            backend.execute_write(dropCmd)
        cmd = 'CREATE TABLE IF NOT EXISTS "{tn}" ({c})'.format(tn=table, c=', '.join(ATTR_TABLE_COLS))
        backend.execute_write(cmd)

    def _insert_attribute_threadsafe(self, nodeid, attrId, attr, table=ATTR_TABLE_NAME):
        with self._lock:
            if nodeid == AddressSpaceSQLite.CUR_TIME_NODEID:
                pass # Prevents SD-card wear: don't write the time.
            else:
                AddressSpaceSQLite._insert_attribute(self.backend, nodeid, attrId, attr, table)
            # CurrentTime-node updates result in commits at COMMIT_INTERVAL sec.
            # Commits without previous actual transactions don't touch the file.
            self.backend.commit()

    @staticmethod
    def _insert_attribute(backend, nodeid, attrId, attr, table=ATTR_TABLE_NAME):
        assert(nodeid.NodeIdType == NodeIdType.Numeric)
        assert(isinstance(attrId, ua.AttributeIds))
        assert(isinstance(attr, AttributeValue))
        # Callback methods are not supported.
        assert(attr.value_callback is None) 
        # Datachange callbacks not supported and are ignored.
        assert(isinstance(attr.datachange_callbacks, dict))
        # DataValue has no opc-ua to_binary: flatten object.
        assert(isinstance(attr.value, ua.uatypes.DataValue))
        # Server timestamp
        assert(attr.value.ServerTimestamp is None or \
          isinstance(attr.value.ServerTimestamp, datetime.datetime))
        assert(attr.value.ServerPicoseconds is None or \
          isinstance(attr.value.ServerTimestamp, int))
        # Source timestamp
        assert(attr.value.SourceTimestamp is None or \
          isinstance(attr.value.SourceTimestamp, datetime.datetime))
        assert(attr.value.SourcePicoseconds is None or \
          isinstance(attr.value.ServerTimestamp, int))
        assert(isinstance(attr.value.StatusCode, ua.uatypes.StatusCode))
        assert(isinstance(attr.value.Value, ua.uatypes.Variant))

        binNodeId = ua.ua_binary.nodeid_to_binary(nodeid)
        primaryKey = binNodeId + pack(">B", int(attrId))

        cmd = 'INSERT OR REPLACE INTO "{tn}" VALUES ({q})'.format(tn=table, q=', '.join('?'*10))
        params = (
          memoryview(primaryKey),
          memoryview(binNodeId),
          int(attrId),
          attr.value.ServerTimestamp,
          None if attr.value.ServerPicoseconds is None else int(attr.value.ServerPicoseconds),
          attr.value.SourceTimestamp,
          None if attr.value.SourcePicoseconds is None else int(attr.value.SourcePicoseconds),
          int(attr.value.StatusCode.value),
          memoryview(ua.ua_binary.variant_to_binary(attr.value.Value)),
          str(nodeid)
        )
        backend.execute_write(cmd, params=params)

    @staticmethod
    def _read_attribute_row(row):
        attrId = ua.AttributeIds(row[2])
        # Rebuild DataValue instance from flattened.
        assert(row[3] is None or isinstance(row[3], datetime.datetime))
        assert(row[4] is None or isinstance(row[4], int))
        assert(row[5] is None or isinstance(row[5], datetime.datetime))
        assert(row[6] is None or isinstance(row[6], int))
        dv = ua.DataValue(ua.ua_binary.variant_from_binary(Buffer(row[8])))
        dv.ServerTimestamp = row[3]
        dv.ServerPicoseconds = row[4]
        dv.SourceTimestamp = row[5]
        dv.SourcePicoseconds = row[6]
        dv.StatusCode = ua.StatusCode(row[7])
        attr = AttributeValue(dv)
        return (attrId, attr)

    # Read and write from references table
    @staticmethod
    def _create_refs_table(backend, table=REFS_TABLE_NAME, drop=False):
        REFS_TABLE_COLS = [
            '_Id BLOB PRIMARY KEY NOT NULL',     # 0
            'NodeId BLOB',                       # 1 = the nodeid of this ReferenceDescription
            'ReferenceTypeId BLOB',              # 2
            'IsForward INTEGER',                 # 3
            'ReferredNodeId BLOB',               # 4 = referred nodeid of ReferenceDescription
            'BrowseName_NamespaceIndex INTEGER', # 5
            'BrowseName_Name TEXT',              # 6
            'DisplayName_Text TEXT',             # 7
            'DisplayName_Locale TEXT',           # 8
            'DisplayName_Encoding INTEGER',      # 9
            'NodeClass INTEGER',                 # 10
            'TypeDefinition BLOB',               # 11
            'Description STRING'                 # 12
        ]
        if drop is True:
            dropCmd = 'DROP TABLE IF EXISTS "{tn}"'.format(tn=table)
            backend.execute_write(dropCmd)
        cmd = 'CREATE TABLE IF NOT EXISTS "{tn}" ({c})'.format(tn=table, c=', '.join(REFS_TABLE_COLS))
        backend.execute_write(cmd)

    def _insert_reference_threadsafe(self, nodeid, ref, table=REFS_TABLE_NAME):
        with self._lock:
            AddressSpaceSQLite._insert_reference(self.backend, nodeid, ref, table)
            self.backend.commit()

    @staticmethod
    def _insert_reference(backend, nodeid, ref, table=REFS_TABLE_NAME):
        # NumericNodeId is required for searching.
        assert(nodeid.NodeIdType == NodeIdType.Numeric)
        assert(isinstance(ref, ua.uaprotocol_auto.ReferenceDescription))
        assert(isinstance(ref.ReferenceTypeId, ua.uatypes.NodeId))
        assert(isinstance(ref.IsForward, bool))
        assert(isinstance(ref.NodeId, ua.uatypes.NodeId))
        # BrowseName
        assert(isinstance(ref.BrowseName, ua.uatypes.QualifiedName))
        assert(isinstance(ref.BrowseName.NamespaceIndex, int))
        assert(ref.BrowseName.Name is None or isinstance(ref.BrowseName.Name, str))
        # DisplayName
        assert(isinstance(ref.DisplayName, ua.uatypes.LocalizedText))
        assert(ref.DisplayName.Text is None or isinstance(ref.DisplayName.Text, str))
        assert(ref.DisplayName.Locale is None)
        assert(isinstance(ref.DisplayName.Encoding, int))
        # NodeClass is enum, stored as INTEGER
        assert(isinstance(ref.NodeClass, (int, ua.uaprotocol_auto.NodeClass)))
        assert(isinstance(ref.TypeDefinition, ua.uatypes.NodeId))

        binNodeId = ua.ua_binary.nodeid_to_binary(nodeid)     # Our own nodeid
        refNodeId = ua.ua_binary.nodeid_to_binary(ref.NodeId) # Referred nodeid
        primaryKey = binNodeId + refNodeId + pack(">B", int(ref.IsForward))

        cmd = 'INSERT OR REPLACE INTO "{tn}" VALUES ({q})'.format(tn=table, q=', '.join('?'*13))
        params = (
          memoryview(primaryKey),
          memoryview(binNodeId),
          memoryview(ua.ua_binary.nodeid_to_binary(ref.ReferenceTypeId)),
          int(bool(ref.IsForward)),
          memoryview(refNodeId),
          int(ref.BrowseName.NamespaceIndex),
          None if ref.BrowseName.Name is None else str(ref.BrowseName.Name),
          None if ref.DisplayName.Text is None else str(ref.DisplayName.Text),
          None if ref.DisplayName.Locale is None else str(ref.DisplayName.Locale),
          int(ref.DisplayName.Encoding),
          int(ref.NodeClass),
          memoryview(ua.ua_binary.nodeid_to_binary(ref.TypeDefinition)),
          str(nodeid)
        )
        backend.execute_write(cmd, params=params)

    @staticmethod
    def _read_reference_row(row):
        ref = ua.uaprotocol_auto.ReferenceDescription()
        ref.ReferenceTypeId = ua.ua_binary.nodeid_from_binary(Buffer(row[2]))
        ref.IsForward = bool(int(row[3]))
        ref.NodeId = ua.ua_binary.nodeid_from_binary(Buffer(row[4]))
        ref.BrowseName = ua.QualifiedName(str(row[6]) if row[6] else None, int(row[5]))
        ref.DisplayName = ua.LocalizedText(str(row[7]) if row[7] else None)
        # row[8] ignored: DisplayName.Locale is automatically set.
        # row[9] ignored: DisplayName.Encoding is automatically set.
        ref.NodeClass = ua.NodeClass(int(row[10]))
        ref.TypeDefinition = ua.ua_binary.nodeid_from_binary(Buffer(row[11]))
        return ref

    # Compare NodeData instances.
    @staticmethod
    def _cmp_nodedata(ndata, ndata2):
        assert(isinstance(ndata2, NodeData))
        assert(ndata.nodeid == ndata2.nodeid)
        for attrId, attr in ndata.attributes.items():
            attr2 = ndata2.attributes[attrId]
            AddressSpaceSQLite._cmp_attr(attr, attr2)
        for idx, ref in enumerate(ndata.references):
            ref2 = ndata2.references[idx]
            AddressSpaceSQLite._cmp_refs(ref, ref2)

    @staticmethod
    def _cmp_attr(attr, attr2):
        assert(attr.value.ServerTimestamp == attr2.value.ServerTimestamp)
        assert(attr.value.SourceTimestamp == attr2.value.SourceTimestamp)
        assert(attr.value.StatusCode.value == attr2.value.StatusCode.value)
        try:
            assert(str(attr.value.Value.Value) == str(attr2.value.Value.Value))
        except:
            assert(int(attr.value.Value.Value) == int(attr2.value.Value.Value))
        assert(attr.value.Value.VariantType == attr2.value.Value.VariantType)

    @staticmethod
    def _cmp_refs(ref, ref2):
        assert(isinstance(ref2, ua.uaprotocol_auto.ReferenceDescription))
        assert(ref.ReferenceTypeId == ref2.ReferenceTypeId)
        assert(ref.IsForward == ref2.IsForward)
        assert(ref.NodeId == ref2.NodeId)
        assert(ref.BrowseName == ref2.BrowseName)
        assert(ref.DisplayName == ref2.DisplayName)
        assert(int(ref.NodeClass) == int(ref2.NodeClass))
        assert(ref.TypeDefinition == ref2.TypeDefinition)


class StandardAddressSpaceSQLite(AddressSpaceSQLite):

    def __init__(self, cache=None):
        path = os.path.join(os.path.dirname(__file__), "standard_address_space", "standard_address_space.sql")
        backend = SQLite3Backend(sqlFile=path, readonly=True) 
        super(StandardAddressSpaceSQLite, self).__init__(backend, cache)

    def __enter__(self):
        self.backend.__enter__()
        return super(StandardAddressSpaceSQLite, self).__enter__()

    def __exit__(self, exc_type, exc_value, traceback):
        super(StandardAddressSpaceSQLite, self).__exit__(exc_type, exc_value, traceback)
        self.backend.__exit__(exc_type, exc_value, traceback)
