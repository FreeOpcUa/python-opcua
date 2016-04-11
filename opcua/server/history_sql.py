from datetime import timedelta
from datetime import datetime

from opcua import ua, Node
from opcua.server.history import HistoryStorageInterface

import struct
import sqlite3


class HistorySQLite(HistoryStorageInterface):
    """
    very minimal history backend storing data in SQLite database
    """
    # FIXME: need to check on if sql_conn.commit() should be inside try block; and if .rollback() needs to be except

    def __init__(self):
        self._datachanges_period = {}
        self._events = {}
        self._db_file = "history.db"

        self._conn = sqlite3.connect(self._db_file, detect_types=sqlite3.PARSE_DECLTYPES, check_same_thread=False)

    def new_historized_node(self, node, period, count=0):
        _c_new = self._conn.cursor()

        node_id = self._get_table_name(node)

        self._datachanges_period[node_id] = period

        # create a table for the node which will store attributes of the DataValue object
        try:
            _c_new.execute('CREATE TABLE "{tn}" (ServerTimestamp TIMESTAMP,'
                           ' SourceTimestamp TIMESTAMP,'
                           ' StatusCode INTEGER,'
                           ' Value TEXT,'
                           ' VariantType INTEGER,'
                           ' ValueBinary BLOB)'.format(tn=node_id))

        except sqlite3.Error as e:
            print(node_id, 'Historizing SQL Table Creation Error:', e)

        self._conn.commit()

    def save_node_value(self, node, datavalue):
        _c_sub = self._conn.cursor()

        node_id = self._get_table_name(node)

        value_blob = self._pack_value(datavalue)

        # insert the data change into the database
        try:
            _c_sub.execute('INSERT INTO "{tn}" VALUES (?, ?, ?, ?, ?, ?)'.format(tn=node_id), (datavalue.ServerTimestamp,
                                                                                               datavalue.SourceTimestamp,
                                                                                               datavalue.StatusCode.value,
                                                                                               str(datavalue.Value.Value),
                                                                                               datavalue.Value.VariantType.value,
                                                                                               value_blob))
        except sqlite3.Error as e:
            print(node_id, 'Historizing SQL Insert Error:', e)

        # get this node's period from the period dict and calculate the limit
        period = self._datachanges_period[node_id]
        date_limit = datetime.now() - period

        # after the insert, delete all values older than period
        try:
            _c_sub.execute('DELETE FROM "{tn}" WHERE ServerTimestamp < ?'.format(tn=node_id),
                                                                                (date_limit.isoformat(' '),))
        except sqlite3.Error as e:
            print(node_id, 'Historizing SQL Delete Old Data Error:', e)

        self._conn.commit()

    def read_node_history(self, node, start, end, nb_values):
        _c_read = self._conn.cursor()

        if end is None:
            end = datetime.now() + timedelta(days=1)
        if start is None:
            start = ua.DateTimeMinValue

        node_id = self._get_table_name(node)

        cont = None
        results = []

        start_time = start.isoformat(' ')
        end_time = end.isoformat(' ')

        # select values from the database
        try:
            for row in _c_read.execute('SELECT * FROM "{tn}" WHERE "ServerTimestamp" BETWEEN ? AND ? '
                                       'LIMIT ?'.format(tn=node_id), (start_time, end_time, nb_values,)):

                value = self._unpack_value(row[4], row[5])

                dv = ua.DataValue(ua.Variant(value, ua.VariantType(row[4])))
                dv.ServerTimestamp = row[0]
                dv.SourceTimestamp = row[1]
                dv.StatusCode = ua.StatusCode(row[2])

                results.append(dv)

        except sqlite3.Error as e:
            print(node_id, 'Historizing SQL Read Error:', e)

        return results, cont

    def new_historized_event(self, event, period):
        raise NotImplementedError

    def save_event(self, event):
        raise NotImplementedError

    def read_event_history(self, start, end, evfilter):
        raise NotImplementedError

    def _pack_value(self, datavalue):
        variant_code = datavalue.Value.VariantType.value
        return struct.pack(self._get_pack_type(variant_code), datavalue.Value.Value)

    def _unpack_value(self, variant_code, binary,):
        return struct.unpack(self._get_pack_type(variant_code), binary)

    def _get_pack_type(self, variant_code):
        # see object_ids.py
        if variant_code is 1:  # Bool
            return '?'
        elif variant_code is 2:  # Char (string with length of one in python)
            return 'c'
        elif variant_code is 3:  # Byte (Signed Char in python)
            return 'b'
        if variant_code is 4:  # Int16
            return 'h'
        elif variant_code is 5:  # UInt16
            return 'H'
        elif variant_code is 6:  # Int32
            return 'i'
        elif variant_code is 7:  # UInt32
            return 'I'
        elif variant_code is 8:  # Int64
            return 'q'
        elif variant_code is 9:  # UInt64
            return 'Q'
        elif variant_code is 10:  # Float
            return 'f'
        elif variant_code is 11:  # Double
            return 'd'
        elif variant_code in (12,):  # String
            return "s"
        else:
            # FIXME: Should raise exception here that historizing of node type isn't supported in SQL storage interface
            return None

    def _get_table_name(self, node):
        if type(node) is Node:
            return str(node.nodeid.NamespaceIndex) + '_' + str(node.nodeid.Identifier)
        if type(node) is ua.HistoryReadValueId:
            return str(node.NodeId.NamespaceIndex) + '_' + str(node.NodeId.Identifier)

    # close connections to the history database when the server stops
    def stop(self):
        pass
        self._conn.close()
        # FIXME: Should close the database connections when the server stops, but because server.stop() is called
        # FIXME: on a different thread than the SQL conn object, no idea how to do this at the moment
