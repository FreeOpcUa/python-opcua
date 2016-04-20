import logging
from datetime import timedelta
from datetime import datetime
from threading import Lock
from opcua import ua
from opcua.common.utils import Buffer
from opcua.common.event import Event
from opcua.server.history import HistoryStorageInterface
import sqlite3


class HistorySQLite(HistoryStorageInterface):
    """
    very minimal history backend storing data in SQLite database
    """

    def __init__(self, path="history.db"):
        self.logger = logging.getLogger(__name__)
        self._datachanges_period = {}
        self._events = {}
        self._db_file = path
        self._lock = Lock()

        self._conn = sqlite3.connect(self._db_file, detect_types=sqlite3.PARSE_DECLTYPES, check_same_thread=False)

    def new_historized_node(self, node_id, period, count=0):
        with self._lock:
            _c_new = self._conn.cursor()

            table = self._get_table_name(node_id)

            self._datachanges_period[node_id] = period, count

            # create a table for the node which will store attributes of the DataValue object
            # note: Value/VariantType TEXT is only for human reading, the actual data is stored in VariantBinary column
            try:
                _c_new.execute('CREATE TABLE "{tn}" (Id INTEGER PRIMARY KEY NOT NULL,'
                               ' ServerTimestamp TIMESTAMP,'
                               ' SourceTimestamp TIMESTAMP,'
                               ' StatusCode INTEGER,'
                               ' Value TEXT,'
                               ' VariantType TEXT,'
                               ' VariantBinary BLOB)'.format(tn=table))

            except sqlite3.Error as e:
                self.logger.info('Historizing SQL Table Creation Error for %s: %s', node_id, e)

            self._conn.commit()

    def save_node_value(self, node_id, datavalue):
        with self._lock:
            _c_sub = self._conn.cursor()

            table = self._get_table_name(node_id)

            # insert the data change into the database
            try:
                _c_sub.execute('INSERT INTO "{tn}" VALUES (NULL, ?, ?, ?, ?, ?, ?)'.format(tn=table),
                               (
                                   datavalue.ServerTimestamp,
                                   datavalue.SourceTimestamp,
                                   datavalue.StatusCode.value,
                                   str(datavalue.Value.Value),
                                   datavalue.Value.VariantType.name,
                                   datavalue.Value.to_binary()
                               )
                               )
            except sqlite3.Error as e:
                self.logger.error('Historizing SQL Insert Error for %s: %s', node_id, e)

            self._conn.commit()

            # get this node's period from the period dict and calculate the limit
            period, count = self._datachanges_period[node_id]

            if period:
                # after the insert, if a period was specified delete all records older than period
                date_limit = datetime.now() - period

                try:
                    _c_sub.execute('DELETE FROM "{tn}" WHERE ServerTimestamp < ?'.format(tn=table),
                                   (date_limit.isoformat(' '),))
                except sqlite3.Error as e:
                    self.logger.error('Historizing SQL Delete Old Data Error for %s: %s', node_id, e)

                self._conn.commit()

    def read_node_history(self, node_id, start, end, nb_values):
        with self._lock:
            _c_read = self._conn.cursor()

            order = "ASC"

            if start is None or start == ua.DateTimeMinValue:
                order = "DESC"
                start = ua.DateTimeMinValue

            if end is None or end == ua.DateTimeMinValue:
                end = datetime.utcnow() + timedelta(days=1)

            if start < end:
                start_time = start.isoformat(' ')
                end_time = end.isoformat(' ')
            else:
                order = "DESC"
                start_time = end.isoformat(' ')
                end_time = start.isoformat(' ')

            if nb_values:
                limit = nb_values + 1  # add 1 to the number of values for retrieving a continuation point
            else:
                limit = -1  # in SQLite a LIMIT of -1 returns all results

            table = self._get_table_name(node_id)

            cont = None
            results = []

            # select values from the database; recreate UA Variant from binary
            try:
                for row in _c_read.execute('SELECT * FROM "{tn}" WHERE "ServerTimestamp" BETWEEN ? AND ? '
                                           'ORDER BY "Id" {dir} LIMIT ?'.format(tn=table, dir=order), (start_time, end_time, limit,)):
                    dv = ua.DataValue(ua.Variant.from_binary(Buffer(row[6])))
                    dv.ServerTimestamp = row[1]
                    dv.SourceTimestamp = row[2]
                    dv.StatusCode = ua.StatusCode(row[3])

                    results.append(dv)

            except sqlite3.Error as e:
                self.logger.error('Historizing SQL Read Error for %s: %s', node_id, e)

            if nb_values:
                if start > ua.DateTimeMinValue and len(results) > nb_values:
                    cont = results[nb_values].ServerTimestamp

                results = results[:nb_values]

            return results, cont

    def new_historized_event(self, obj_id, period):
        with self._lock:
            _c_new = self._conn.cursor()

            table = self._get_table_name(obj_id)

            self._datachanges_period[obj_id] = period

            # create a table for the event which will store attributes of the Event object
            # note: Value/VariantType TEXT is only for human reading, the actual data is stored in VariantBinary column
            try:
                _c_new.execute('CREATE TABLE "{tn}" (Id INTEGER PRIMARY KEY NOT NULL,'
                               ' Time TIMESTAMP,'
                               ' ReceiveTime TIMESTAMP,'
                               ' EventIdBinary BLOB,'
                               ' EventTypeBinary BLOB,'
                               ' Severity INTEGER,'
                               ' Message TEXT,'
                               ' MessageBinary BLOB,'
                               ' SourceName TEXT,'
                               ' SourceNodeBinary BLOB,'
                               ' ServerHandle INTEGER)'.format(tn=table))

            except sqlite3.Error as e:
                self.logger.info('Historizing SQL Table Creation Error for events from %s: %s', obj_id, e)

            self._conn.commit()

    def save_event(self, event):
        with self._lock:
            _c_sub = self._conn.cursor()

            table = self._get_table_name(event.SourceNode)

            # insert the event into the database
            try:
                _c_sub.execute('INSERT INTO "{tn}" VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'.format(tn=table),
                               (
                                   event.Time,
                                   event.ReceiveTime,
                                   event.EventId,
                                   event.EventType.to_binary(),
                                   event.Severity,
                                   event.Message.Text,
                                   event.Message.to_binary(),
                                   event.SourceName,
                                   event.SourceNode.to_binary(),
                                   event.server_handle,
                               )
                               )
            except sqlite3.Error as e:
                self.logger.error('Historizing SQL Insert Error for events from %s: %s', event.SourceNode, e)

            self._conn.commit()

            # get this node's period from the period dict and calculate the limit
            period = self._datachanges_period[event.SourceNode]

            if period:
                # after the insert, if a period was specified delete all records older than period
                date_limit = datetime.now() - period

                try:
                    _c_sub.execute('DELETE FROM "{tn}" WHERE Time < ?'.format(tn=table),
                                   (date_limit.isoformat(' '),))
                except sqlite3.Error as e:
                    self.logger.error('Historizing SQL Delete Old Data Error for events from %s: %s', event.SourceNode, e)

                self._conn.commit()

    def read_event_history(self, obj_id, start, end, nb_values, evfilter):
        with self._lock:
            _c_read = self._conn.cursor()

            order = "ASC"

            if start is None or start == ua.DateTimeMinValue:
                order = "DESC"
                start = ua.DateTimeMinValue

            if end is None or end == ua.DateTimeMinValue:
                end = datetime.utcnow() + timedelta(days=1)

            if start < end:
                start_time = start.isoformat(' ')
                end_time = end.isoformat(' ')
            else:
                order = "DESC"
                start_time = end.isoformat(' ')
                end_time = start.isoformat(' ')

            if nb_values:
                limit = nb_values + 1  # add 1 to the number of values for retrieving a continuation point
            else:
                limit = -1  # in SQLite a LIMIT of -1 returns all results

            table = self._get_table_name(obj_id)

            results = []

            # select events from the database
            # FIXME use EventFilter to customize SQL clause
            try:
                for row in _c_read.execute('SELECT * FROM "{tn}" WHERE "ServerTimestamp" BETWEEN ? AND ? '
                                           'ORDER BY "Id" {dir} LIMIT ?'.format(tn=table, dir=order), (start_time, end_time, limit,)):
                    ev = Event()
                    ev.Time = row[1]
                    # FIXME finish rebuilding event from SQL data

                    results.append(ev)

            except sqlite3.Error as e:
                self.logger.error('Historizing SQL Read Error events for node %s: %s', obj_id, e)

            if nb_values:
                if start > ua.DateTimeMinValue and len(results) > nb_values:
                    cont = results[nb_values].Time

                results = results[:nb_values]

            return results

    def _get_table_name(self, node_id):
        return str(node_id.NamespaceIndex) + '_' + str(node_id.Identifier)

    def stop(self):
        with self._lock:
            self._conn.close()

