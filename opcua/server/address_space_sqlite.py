
import sqlite3
import datetime

from opcua import ua
from opcua.ua.uatypes import NumericNodeId, NodeIdType
from opcua.common.utils import Buffer
from opcua.server.address_space import NodeData, AddressSpace, AttributeValue

class AddressSpaceSQLite(AddressSpace):
    """
    Load the standard address space nodes from a SQLite database.
    Intended for slow devices, such as Raspberry Pi, to greatly improve start up time
    """
    ATTR_TABLE_NAME = 'Attributes'
    REFS_TABLE_NAME = 'ReferenceDescription'

    def __init__(self, cache=None, sqlFile=None):
        super(AddressSpaceSQLite, self).__init__(cache)
        assert(isinstance(sqlFile, str))
        self._sqlFile = sqlFile
        self._conn = None

    def __enter__(self):
        super(AddressSpaceSQLite, self).__enter__()
        assert(self._conn is None)
        self._conn = sqlite3.connect(self._sqlFile, \
          detect_types=sqlite3.PARSE_DECLTYPES, check_same_thread=False)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self._conn:
            self._conn.close()
            self._conn = None
        super(AddressSpaceSQLite, self).__exit__(exc_type, exc_value, traceback)

    def __getitem__(self, nodeid):
        with self._lock:
            (nodeData, fromDisk) = self._getitem_sqlite(nodeid)
            return nodeData

    def _getitem_sqlite(self, nodeid):
        try:
            if not hasattr(self._cache, '_getitem_sqlite'):
                (nodeData, fromDisk) = (self._cache.__getitem__(nodeid), False)
            else:
                (nodeData, fromDisk) = self._cache._getitem_sqlite(nodeid)
                if fromDisk:
                    self._read_nodedata(self._conn, nodeid, nodeData)
        except KeyError:
            (nodeData, fromDisk) = (NodeData(nodeid), True)
            AddressSpaceSQLite._read_nodedata(self._conn, nodeid, nodeData)
            if len(nodeData.attributes) is 0:
                raise
            self._cache[nodeid] = nodeData
        return (nodeData, fromDisk)

    def get(self, nodeid, value=None):
        try:
            return self[nodeid]
        except KeyError:
            return value

    def __contains__(self, nodeid):
        return self.get(nodeid) is not None

    def __setitem__(self, key, value):
        # TODO the item in the database it is not updated
        super(AddressSpaceSQLite, self).__setitem__(key, value)
    

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
        Dump address space into an sqlite database; note that server must be stopped for this method to work
        Note 1: DO NOT DUMP AN ADDRESS SPACE RESTORED FROM DATABASE, ONLY CACHED NODES WILL GET DUMPED!
        Note 2: If a NodeData instance holds a reference to a method call, it is not preserved.
        Note 3: numeric nodeid's are required for database searches.
        """
        # 1. Create tables.
        AddressSpaceSQLite._create_attr_table(self._conn)
        AddressSpaceSQLite._create_refs_table(self._conn)

        with self._lock:
            # 2. Populate.
            for nodeid, ndata in self._cache.items():
                if nodeid.NamespaceIndex != namespaceidx:
                    for ref in ndata.references:
                        if ref.NodeId.NamespaceIndex == namespaceidx:
                            keyNodeId = AddressSpaceSQLite._nodeid_to_key(ndata.nodeid)
                            AddressSpaceSQLite._insert_reference(self._conn, keyNodeId, ref)
                            print('INTER_NAMESPACE REF {:s}/{:d}->{:d}'.format(str(nodeid.Identifier), nodeid.NamespaceIndex, ref.NodeId.NamespaceIndex))
                    continue
                assert(nodeid == ndata.nodeid)
                assert(isinstance(ndata, NodeData))
                AddressSpaceSQLite._write_nodedata(self._conn, ndata)

            # 3. Integrity checks.
            for nodeid, ndata in self._cache.items():
                if nodeid.NamespaceIndex != namespaceidx:
                    continue
                ndata2 = NodeData(nodeid)
                AddressSpaceSQLite._read_nodedata(self._conn, nodeid, ndata2)
                AddressSpaceSQLite._cmp_nodedata(ndata, ndata2)

            self._conn.commit()
        print("Export to {:s} completed".format(self._sqlFile))

    # Write NodeData to database
    @staticmethod
    def _write_nodedata(conn, ndata):
        assert(isinstance(ndata.nodeid, ua.uatypes.NodeId))
        keyNodeId = AddressSpaceSQLite._nodeid_to_key(ndata.nodeid)

        # Add attributes to database
        assert(isinstance(ndata.attributes, dict))
        for attrId, attr in ndata.attributes.items():
            AddressSpaceSQLite._insert_attribute(conn, keyNodeId, attrId, attr)

        # Add references to database
        assert(isinstance(ndata.references, list))
        for ref in ndata.references:
            AddressSpaceSQLite._insert_reference(conn, keyNodeId, ref)

    @staticmethod
    def _nodeid_to_key(nodeid):
        # For database lookups, map TwoByte and FourByte onto NumericNodeId.
        if nodeid.NodeIdType in (NodeIdType.TwoByte, NodeIdType.FourByte):
            return NumericNodeId(nodeid.Identifier, nodeid.NamespaceIndex)
        return nodeid

    # Read NodeData from database
    @staticmethod
    def _read_nodedata(conn, nodeid, nodeData, attrTable=ATTR_TABLE_NAME, refsTable=REFS_TABLE_NAME):

        _c_read = conn.cursor()

        # Search key = numeric nodeid in opc-ua binary format
        keyNodeId = AddressSpaceSQLite._nodeid_to_key(nodeid)
        hexNodeId = ua.ua_binary.nodeid_to_binary(keyNodeId).hex()

        cmd1 = 'SELECT * FROM "{tn}" WHERE NodeId = x\'{h}\''.format(tn=attrTable, h=hexNodeId)
        for row in _c_read.execute(cmd1):
            (attrId, attr) = AddressSpaceSQLite._read_attribute_row(row)
            nodeData.attributes[attrId] = attr

        cmd2 = 'SELECT * FROM "{tn}" WHERE NodeId = x\'{h}\''.format(tn=refsTable, h=hexNodeId)
        referred_nodeids = [r.NodeId for r in nodeData.references]
        for row in _c_read.execute(cmd2):
            ref = AddressSpaceSQLite._read_reference_row(row)
            #try:
            #    idx = referred_nodeids.index(ref.NodeId)
            #    print('DUPLICATE {:s}'.format(str(ref.NodeId)))
            #    nodeData.references[idx] = ref
            #except ValueError:
            nodeData.references.append(ref)

    # Read and write from attribute table
    @staticmethod
    def _create_attr_table(conn, table=ATTR_TABLE_NAME):
        ATTR_TABLE_COLS = [
            '_Id INTEGER PRIMARY KEY NOT NULL', # 0
            'NodeId BLOB',                      # 1
            'AttributeId INTEGER',              # 2
            'ServerTimestamp TIMESTAMP',        # 3
            'ServerPicoseconds INTEGER',        # 4
            'SourceTimestamp TIMESTAMP',        # 5
            'SourcePicoseconds INTEGER',        # 6
            'StatusCode INTEGER',               # 7
            'Variant BLOB',                     # 8
        ]
        _c_new = conn.cursor()
        _c_new.execute('DROP TABLE IF EXISTS "{tn}"'.format(tn=table))
        _c_new.execute('CREATE TABLE "{tn}" ({c})'.format(tn=table, c=', '.join(ATTR_TABLE_COLS)))

    @staticmethod
    def _insert_attribute(conn, nodeid, attrId, attr, table=ATTR_TABLE_NAME):
        assert(isinstance(nodeid, ua.uatypes.NodeId))
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

        _c_sub = conn.cursor()
        _c_sub.execute('INSERT INTO "{tn}" VALUES (NULL{q})'.format(tn=table, q=', ?'*8),
            ( sqlite3.Binary(ua.ua_binary.nodeid_to_binary(nodeid)),
              int(attrId),
              attr.value.ServerTimestamp,
              None if attr.value.ServerPicoseconds is None else int(attr.value.ServerPicoseconds),
              attr.value.SourceTimestamp,
              None if attr.value.SourcePicoseconds is None else int(attr.value.SourcePicoseconds),
              int(attr.value.StatusCode.value),
              sqlite3.Binary(ua.ua_binary.variant_to_binary(attr.value.Value))
            )
        )

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
    def _create_refs_table(conn, table='ReferenceDescription'):
        REFS_TABLE_COLS = [
            '_Id INTEGER PRIMARY KEY NOT NULL',  # 0
            'NodeId BLOB',                       # 1 = the nodeid of this ReferenceDescription
            'ReferenceTypeId BLOB',              # 2
            'IsForward INTEGER',                 # 3
            'ReferenceNodeId BLOB',              # 4 = referred nodeid of ReferenceDescription
            'BrowseName_NamespaceIndex INTEGER', # 5
            'BrowseName_Name TEXT',              # 6
            'DisplayName_Text TEXT',             # 7
            'DisplayName_Locale TEXT',           # 8
            'DisplayName_Encoding INTEGER',      # 9
            'NodeClass INTEGER',                 # 10
            'TypeDefinition BLOB',               # 11
        ]
        _c_new = conn.cursor()
        _c_new.execute('DROP TABLE IF EXISTS "{tn}"'.format(tn=table))
        _c_new.execute('CREATE TABLE "{tn}" ({c})'.format(tn=table, c=', '.join(REFS_TABLE_COLS)))

    @staticmethod
    def _insert_reference(conn, nodeid, ref, table=REFS_TABLE_NAME):
        assert(isinstance(nodeid, ua.uatypes.NodeId))
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

        _c_sub = conn.cursor()
        _c_sub.execute('INSERT INTO "{tn}" VALUES (NULL{q})'.format(tn=table, q=', ?'*11),
            ( sqlite3.Binary(ua.ua_binary.nodeid_to_binary(nodeid)),
              sqlite3.Binary(ua.ua_binary.nodeid_to_binary(ref.ReferenceTypeId)),
              int(bool(ref.IsForward)),
              sqlite3.Binary(ua.ua_binary.nodeid_to_binary(ref.NodeId)),
              int(ref.BrowseName.NamespaceIndex),
              None if ref.BrowseName.Name is None else str(ref.BrowseName.Name),
              None if ref.DisplayName.Text is None else str(ref.DisplayName.Text),
              None if ref.DisplayName.Locale is None else str(ref.DisplayName.Locale),
              int(ref.DisplayName.Encoding),
              int(ref.NodeClass),
              sqlite3.Binary(ua.ua_binary.nodeid_to_binary(ref.TypeDefinition)),
            )
        )

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
