import logging
from datetime import timedelta
from datetime import datetime

from opcua import ua
from opcua.server.history import HistoryStorageInterface

import struct
import sqlite3


class HistorySQLite(HistoryStorageInterface):
    """
    very minimal history backend storing data in SQLite database
    """

    def __init__(self):
        self.logger = logging.getLogger('historySQL')
        self._datachanges_period = {}
        self._events = {}
        self._db_file = "history.db"

        self._conn = sqlite3.connect(self._db_file, detect_types=sqlite3.PARSE_DECLTYPES, check_same_thread=False)

    def new_historized_node(self, node_id, period, count=0):
        _c_new = self._conn.cursor()

        table = self._get_table_name(node_id)

        self._datachanges_period[node_id] = period

        # create a table for the node which will store attributes of the DataValue object
        try:
            _c_new.execute('CREATE TABLE "{tn}" (ServerTimestamp TIMESTAMP,'
                           ' SourceTimestamp TIMESTAMP,'
                           ' StatusCode INTEGER,'
                           ' Value TEXT,'
                           ' VariantType INTEGER,'
                           ' ValueBinary BLOB)'.format(tn=table))

        except sqlite3.Error as e:
            self.logger.info('Historizing SQL Table Creation Error for %s: %s', node_id, e)

        self._conn.commit()

    def save_node_value(self, node_id, datavalue):
        _c_sub = self._conn.cursor()

        table = self._get_table_name(node_id)

        value_blob = self._pack_value(datavalue)

        # insert the data change into the database
        try:
            _c_sub.execute('INSERT INTO "{tn}" VALUES (?, ?, ?, ?, ?, ?)'.format(tn=table), (datavalue.ServerTimestamp,
                                                                                             datavalue.SourceTimestamp,
                                                                                             datavalue.StatusCode.value,
                                                                                             str(datavalue.Value.Value),
                                                                                             datavalue.Value.VariantType.value,
                                                                                             value_blob))
        except sqlite3.Error as e:
            self.logger.error('Historizing SQL Insert Error for %s: %s', node_id, e)

        self._conn.commit()

        # get this node's period from the period dict and calculate the limit
        period = self._datachanges_period[node_id]
        date_limit = datetime.now() - period

        # after the insert, delete all values older than period
        try:
            _c_sub.execute('DELETE FROM "{tn}" WHERE ServerTimestamp < ?'.format(tn=table),
                                                                                (date_limit.isoformat(' '),))
        except sqlite3.Error as e:
            self.logger.error('Historizing SQL Delete Old Data Error for %s: %s', node_id, e)

        self._conn.commit()

    def read_node_history(self, node_id, start, end, nb_values):
        _c_read = self._conn.cursor()

        if end is None:
            end = datetime.now() + timedelta(days=1)
        if start is None:
            start = ua.DateTimeMinValue

        table = self._get_table_name(node_id)

        cont = None
        results = []

        start_time = start.isoformat(' ')
        end_time = end.isoformat(' ')

        # select values from the database
        try:
            for row in _c_read.execute('SELECT * FROM "{tn}" WHERE "ServerTimestamp" BETWEEN ? AND ? '
                                       'LIMIT ?'.format(tn=table), (start_time, end_time, nb_values,)):

                variant_type = ua.VariantType(row[4])
                value = self._unpack_value(variant_type, row[5])

                dv = ua.DataValue(ua.Variant(value, variant_type))
                dv.ServerTimestamp = row[0]
                dv.SourceTimestamp = row[1]
                dv.StatusCode = ua.StatusCode(row[2])

                results.append(dv)

        except sqlite3.Error as e:
            self.logger.error('Historizing SQL Read Error for %s: %s', node_id, e)

        return results, cont

    def new_historized_event(self, event, period):
        raise NotImplementedError

    def save_event(self, event):
        raise NotImplementedError

    def read_event_history(self, start, end, evfilter):
        raise NotImplementedError

    def _pack_value(self, datavalue):
        return struct.pack(self._get_pack_type(datavalue.Value.VariantType), datavalue.Value.Value)

    def _unpack_value(self, variant_type, binary,):
        values_tuple = struct.unpack(self._get_pack_type(variant_type), binary)
        return values_tuple[0]

    def _get_pack_type(self, variant_type):
        # see object_ids.py
        if variant_type is ua.VariantType.Boolean:
            return '?'
        elif variant_type is ua.VariantType.SByte:  # Char (string with length of one in python)
            return 'c'
        elif variant_type is ua.VariantType.Byte:  # Byte (Signed Char in python)
            return 'b'
        if variant_type is ua.VariantType.Int16:
            return 'h'
        elif variant_type is ua.VariantType.UInt16:
            return 'H'
        elif variant_type is ua.VariantType.Int32:
            return 'i'
        elif variant_type is ua.VariantType.UInt32:
            return 'I'
        elif variant_type is ua.VariantType.Int64:
            return 'q'
        elif variant_type is ua.VariantType.UInt64:
            return 'Q'
        elif variant_type is ua.VariantType.Float:
            return 'f'
        elif variant_type is ua.VariantType.Double:
            return 'd'
        elif variant_type is ua.VariantType.String:
            return "s"
        else:
            # FIXME: Should raise exception here that historizing of node type isn't supported in SQL storage interface
            return None

    def _get_table_name(self, node_id):
        return str(node_id.NamespaceIndex) + '_' + str(node_id.Identifier)

    # close connections to the history database when the server stops
    def stop(self):
        self._conn.close()
