
import logging
import sqlite3

import opcua
from opcua import ua
from opcua.common.utils import Buffer
from .address_space import AddressSpace

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
        self._conn = sqlite3.connect(self._sqlFile, detect_types=sqlite3.PARSE_DECLTYPES, check_same_thread=False)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self._conn:
            self._conn.close()
            self._conn = None
        super(AddressSpaceSQLite, self).__exit__(exc_type, exc_value, traceback)

    def __getitem__(self, nodeid):
        with self._lock:
            if nodeid not in self._cache:
                # For now only the standard address space is loaded from sql
                if nodeid.NamespaceIndex != 0:
                    raise KeyError
                nodeData = AddressSpaceSQLite._read_nodedata(self._conn, nodeid) # throws KeyError
                self._cache[nodeid] = nodeData
            return self._cache[nodeid]

    def get(self, nodeid, value=None):
        try:
            return self[nodeid]
        except KeyError:
            return value

    def __setitem__(self, key, value):
        # TODO the item in the database it is not updated
        super(AddressSpaceSQLite, self).__setitem__(key, value)
    
    def __contains__(self, nodeid):
        try:
            self.__getitem__(nodeid)
        except:
            return False
        return True
        
    def __delitem__(self, key):
        # TODO only deleting items from the cache is implemented.
        super(AddressSpaceSQLite, self).__delitem__(key)
    
    def __iter__(self):
        # TODO only the cache can be iterated over.
        return super(AddressSpaceSQLite, self).__iter__()
    
    def __len__(self):
        # TODO only returns the length of items in the cache.
        return super(AddressSpaceSQLite, self).__len__()

    def dump(self, path):
        """
        Dump address space into an sqlite database; note that server must be stopped for this method to work
        Note 1: DO NOT DUMP AN ADDRESS SPACE RESTORED FROM DATABASE, ONLY CACHED NODES WILL GET DUMPED!
        Note 2: If a NodeData instance holds a reference to a method call, it is not preserved.
        """
        # 1. Create tables.
        AddressSpaceSQLite._create_attr_table(self._conn)
        AddressSpaceSQLite._create_refs_table(self._conn)

        # 2. Populate.
        # IMPORTANT: numeric node id's are required for database searches!
        for nodeid, ndata in self._cache.items():
            assert(isinstance(nodeid, opcua.ua.uatypes.NumericNodeId))
            assert(isinstance(ndata, opcua.server.address_space.NodeData))
            assert(isinstance(ndata.nodeid, opcua.ua.uatypes.NumericNodeId))
            assert(nodeid == ndata.nodeid)
            AddressSpaceSQLite._write_nodedata(self._conn, ndata)

        self._conn.commit()

        # 3. Integrity checks.
        for nodeid, ndata in self._cache.items():
            ndata2 = AddressSpaceSQLite._read_nodedata(self._conn, nodeid)
            if str(ndata) != str(ndata2):
                raise Exception(
                    'NodeData integrity check failed:\n'
                    'EXPECTED:\n{:s}\n\nIMPORTED:\n{:s}'.format(str(ndata), str(ndata2))
                )

    # Write NodeData to database
    @staticmethod
    def _write_nodedata(conn, ndata):
        # Attributes to database
        assert(isinstance(ndata.attributes, dict))
        for attrId, attr in ndata.attributes.items():
            AddressSpaceSQLite._insert_attribute(conn, ndata.nodeid, attrId, attr)

        # References to database
        assert(isinstance(ndata.references, list))
        for ref in ndata.references:
            AddressSpaceSQLite._insert_reference(conn, ndata.nodeid, ref)

    # Read NodeData from database
    @staticmethod
    def _read_nodedata(conn, nodeid, attrTable=ATTR_TABLE_NAME, refsTable=REFS_TABLE_NAME):
        # Numeric nodeid's must be used for database searches.
        if not isinstance(nodeid, opcua.ua.uatypes.NumericNodeId):
            nodeid = opcua.ua.uatypes.NumericNodeId(nodeid.Identifier, nodeid.NamespaceIndex)

        _c_read = conn.cursor()
        hex_id = opcua.ua.ua_binary.nodeid_to_binary(nodeid).hex()
        nodeData = opcua.server.address_space.NodeData(nodeid)

        cmd1 = 'SELECT * FROM "{tn}" WHERE NodeId = x\'{h}\''.format(tn=attrTable, h=hex_id)
        for row in _c_read.execute(cmd1):
            (attrId, attr) = AddressSpaceSQLite._read_attribute_row(row)
            nodeData.attributes[attrId] = attr

        if len(nodeData.attributes) is 0:
            raise KeyError('Nodeid {:s}, ns={:d} does not exist in database'.format(str(nodeid), nodeid.NamespaceIndex))

        cmd2 = 'SELECT * FROM "{tn}" WHERE NodeId = x\'{h}\''.format(tn=refsTable, h=hex_id)
        for row in _c_read.execute(cmd2):
            ref = AddressSpaceSQLite._read_reference_row(row)
            nodeData.references.append(ref)

        return nodeData

    # Read and write from attribute table
    @staticmethod
    def _create_attr_table(conn, table=ATTR_TABLE_NAME):
        ATTR_TABLE_COLS = [
            '_Id INTEGER PRIMARY KEY NOT NULL', # 0
            'NodeId BLOB',                      # 1
            'AttributeId INTEGER',              # 2
            'ServerTimestamp TIMESTAMP',        # 3
            'SourceTimestamp TIMESTAMP',        # 4
            'StatusCode INTEGER',               # 5
            'Variant BLOB',                     # 6
        ]
        _c_new = conn.cursor()
        _c_new.execute('DROP TABLE IF EXISTS "{tn}"'.format(tn=table))
        _c_new.execute('CREATE TABLE "{tn}" ({c})'.format(tn=table, c=', '.join(ATTR_TABLE_COLS)))

    @staticmethod
    def _insert_attribute(conn, nodeid, attrId, attr, table=ATTR_TABLE_NAME):
        assert(isinstance(nodeid, opcua.ua.uatypes.NumericNodeId))
        assert(isinstance(attrId, opcua.ua.AttributeIds))
        assert(isinstance(attr, opcua.server.address_space.AttributeValue))
        # Callback methods are not supported.
        assert(attr.value_callback is None) 
        # Datachange callbacks not supported.
        assert(isinstance(attr.datachange_callbacks, dict))
        assert(len(attr.datachange_callbacks) == 0)
        # DataValue has no opc-ua to_binary: flatten object.
        assert(isinstance(attr.value, opcua.ua.uatypes.DataValue))
        assert(attr.value.SourceTimestamp is None)
        assert(attr.value.SourcePicoseconds is None)
        assert(attr.value.ServerTimestamp is None)
        assert(attr.value.ServerPicoseconds is None)
        assert(isinstance(attr.value.StatusCode, opcua.ua.uatypes.StatusCode))
        assert(isinstance(attr.value.Value, opcua.ua.uatypes.Variant))

        _c_sub = conn.cursor()
        _c_sub.execute('INSERT INTO "{tn}" VALUES (NULL{q})'.format(tn=table, q=', ?'*6),
            ( sqlite3.Binary(opcua.ua.ua_binary.nodeid_to_binary(nodeid)),
              int(attrId),
              attr.value.ServerTimestamp,
              attr.value.SourceTimestamp,
              int(attr.value.StatusCode.value),
              sqlite3.Binary(opcua.ua.ua_binary.variant_to_binary(attr.value.Value))
            )
        )

    @staticmethod
    def _read_attribute_row(row):
        attrId = ua.AttributeIds(row[2])
        # Rebuild DataValue instance from flattened.
        dv = ua.DataValue(opcua.ua.ua_binary.variant_from_binary(Buffer(row[6])))
        if attrId == ua.AttributeIds.NodeClass:
            dv.Value.Value = ua.NodeClass(dv.Value.Value)
        assert(row[3] is None and row[4] is None)
        dv.ServerTimestamp = row[3]
        dv.SourceTimestamp = row[4]
        dv.StatusCode = ua.StatusCode(row[5])
        attr = opcua.server.address_space.AttributeValue(dv)
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
        assert isinstance(ref, opcua.ua.uaprotocol_auto.ReferenceDescription)
        assert(isinstance(ref.ReferenceTypeId, opcua.ua.uatypes.NodeId))
        assert(isinstance(ref.IsForward, bool))
        assert(isinstance(ref.NodeId, opcua.ua.uatypes.NumericNodeId))
        # BrowseName
        assert(isinstance(ref.BrowseName, opcua.ua.uatypes.QualifiedName))
        assert(isinstance(ref.BrowseName.NamespaceIndex, int))
        try:
            assert(isinstance(ref.BrowseName.Name, str))
        except:
            assert(ref.BrowseName.Name is None)
        # DisplayName
        assert(isinstance(ref.DisplayName, opcua.ua.uatypes.LocalizedText))
        try:
            assert(isinstance(ref.DisplayName.Text, str))
        except:
            assert(ref.DisplayName.Text is None)
        assert(ref.DisplayName.Locale is None)
        assert(isinstance(ref.DisplayName.Encoding, int))
        # NodeClass is enum, stored as INTEGER
        assert(isinstance(ref.NodeClass, opcua.ua.uaprotocol_auto.NodeClass))
        assert(isinstance(ref.TypeDefinition, opcua.ua.uatypes.NodeId))

        _c_sub = conn.cursor()
        _c_sub.execute('INSERT INTO "{tn}" VALUES (NULL{q})'.format(tn=table, q=', ?'*11),
            ( sqlite3.Binary(opcua.ua.ua_binary.nodeid_to_binary(nodeid)),
              sqlite3.Binary(opcua.ua.ua_binary.nodeid_to_binary(ref.ReferenceTypeId)),
              int(bool(ref.IsForward)),
              sqlite3.Binary(opcua.ua.ua_binary.nodeid_to_binary(ref.NodeId)),
              int(ref.BrowseName.NamespaceIndex),
              str(ref.BrowseName.Name or ''),
              str(ref.DisplayName.Text or ''),
              str(ref.DisplayName.Locale or ''),
              int(ref.DisplayName.Encoding),
              int(ref.NodeClass),
              sqlite3.Binary(opcua.ua.ua_binary.nodeid_to_binary(ref.TypeDefinition)),
            )
        )

    @staticmethod
    def _read_reference_row(row):
        ref = opcua.ua.uaprotocol_auto.ReferenceDescription()
        ref.ReferenceTypeId = opcua.ua.ua_binary.nodeid_from_binary(Buffer(row[2]))
        ref.IsForward = bool(int(row[3]))
        ref.NodeId = opcua.ua.ua_binary.nodeid_from_binary(Buffer(row[4]))
        ref.BrowseName = opcua.ua.QualifiedName(str(row[6]) or None, int(row[5]))
        ref.DisplayName = opcua.ua.LocalizedText(str(row[7]) or None)
        ref.NodeClass = opcua.ua.NodeClass(int(row[10]))
        ref.TypeDefinition = opcua.ua.ua_binary.nodeid_from_binary(Buffer(row[11]))
        return ref
