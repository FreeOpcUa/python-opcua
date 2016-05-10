import logging
from datetime import timedelta
from datetime import datetime
from threading import Lock
from opcua import ua
from opcua.common.utils import Buffer
from opcua.server.history import HistoryStorageInterface
import sqlite3


class HistorySQLite(HistoryStorageInterface):
    """
    very minimal history backend storing data in SQLite database
    """

    def __init__(self, path="history.db"):
        self.logger = logging.getLogger(__name__)
        self._datachanges_period = {}
        self._db_file = path
        self._lock = Lock()
        self._event_fields = {}

        self._conn = sqlite3.connect(self._db_file, detect_types=sqlite3.PARSE_DECLTYPES, check_same_thread=False)

    def new_historized_node(self, node_id, period, count=0):
        with self._lock:
            _c_new = self._conn.cursor()

            table = self._get_table_name(node_id)

            self._datachanges_period[node_id] = period, count

            # create a table for the node which will store attributes of the DataValue object
            # note: Value/VariantType TEXT is only for human reading, the actual data is stored in VariantBinary column
            try:
                _c_new.execute('CREATE TABLE "{tn}" (_Id INTEGER PRIMARY KEY NOT NULL,'
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
                                           'ORDER BY "_Id" {dir} LIMIT ?'.format(tn=table, dir=order), (start_time, end_time, limit,)):

                    # rebuild the data value object
                    dv = ua.DataValue(ua.Variant.from_binary(Buffer(row[6])))
                    dv.ServerTimestamp = row[1]
                    dv.SourceTimestamp = row[2]
                    dv.StatusCode = ua.StatusCode(row[3])

                    results.append(dv)

            except sqlite3.Error as e:
                self.logger.error('Historizing SQL Read Error for %s: %s', node_id, e)

            if nb_values:
                if len(results) > nb_values:
                    cont = results[nb_values].ServerTimestamp

                results = results[:nb_values]

            return results, cont

    def new_historized_event(self, source_id, ev_fields, period):
        with self._lock:
            _c_new = self._conn.cursor()

            self._datachanges_period[source_id] = period
            self._event_fields[source_id] = ev_fields

            table = self._get_table_name(source_id)
            columns = self._get_event_columns(ev_fields)

            # create a table for the event which will store fields generated by the source object's events
            # note that _Timestamp is for SQL query, _EventTypeName is for debugging, be careful not to create event
            # properties with these names
            try:
                _c_new.execute('CREATE TABLE "{tn}" (_Id INTEGER PRIMARY KEY NOT NULL, '
                               '_Timestamp TIMESTAMP, '
                               '_EventTypeName TEXT, '
                               '{co})'.format(tn=table, co=columns))

            except sqlite3.Error as e:
                self.logger.info('Historizing SQL Table Creation Error for events from %s: %s', source_id, e)

            self._conn.commit()

    def save_event(self, event):
        with self._lock:
            _c_sub = self._conn.cursor()

            table = self._get_table_name(event.SourceNode)
            columns, placeholders, evtup = self._format_event(event)
            event_type = event.EventType  # useful for troubleshooting database

            # insert the event into the database
            try:
                _c_sub.execute('INSERT INTO "{tn}" ("_Id", "_Timestamp", "_EventTypeName", {co}) '
                               'VALUES (NULL, "{ts}", "{et}", {pl})'.format(tn=table, co=columns, ts=event.Time, et=event_type, pl=placeholders), evtup)

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

    def read_event_history(self, source_id, start, end, nb_values, evfilter):
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

            table = self._get_table_name(source_id)
            clauses = self._get_select_clauses(source_id, evfilter)

            cont = None
            cont_timestamps = []
            results = []

            # select events from the database; SQL select clause is built from EventFilter and available fields
            try:
                for row in _c_read.execute('SELECT "_Timestamp", {cl} FROM "{tn}" WHERE "_Timestamp" BETWEEN ? AND ? '
                                           'ORDER BY "_Id" {dir} LIMIT ?'.format(cl=clauses, tn=table, dir=order),
                                           (start_time, end_time, limit,)):

                    # place all the variants in the event field list object
                    hist_ev_field_list = ua.HistoryEventFieldList()
                    i = 0
                    for field in row:
                        # if the field is the _Timestamp column store it in a list used for getting the continuation
                        if i == 0:
                            cont_timestamps.append(field)
                        else:
                            if field is not None:
                                hist_ev_field_list.EventFields.append(ua.Variant.from_binary(Buffer(field)))
                            else:
                                hist_ev_field_list.EventFields.append(ua.Variant(None))
                        i += 1

                    results.append(hist_ev_field_list)

            except sqlite3.Error as e:
                self.logger.error('Historizing SQL Read Error events for node %s: %s', source_id, e)

            if nb_values:
                if len(results) > nb_values:  # start > ua.DateTimeMinValue and
                    cont = cont_timestamps[nb_values]

                results = results[:nb_values]

            return results, cont

    def _get_table_name(self, node_id):
        return str(node_id.NamespaceIndex) + '_' + str(node_id.Identifier)

    def _format_event(self, event_result):
        placeholders = []
        ev_fields = []
        ev_variant_binaries = []

        ev_variant_dict = event_result.get_event_props_as_field_dict()

        # split dict into two synchronized lists which will be converted to SQL strings
        # note that the variants are converted to binary objects for storing in SQL BLOB format
        for field, variant in ev_variant_dict.items():
            placeholders.append('?')
            ev_fields.append(field)
            ev_variant_binaries.append(variant.to_binary())

        return self._list_to_sql_str(ev_fields), self._list_to_sql_str(placeholders, False), tuple(ev_variant_binaries)

    def _get_event_columns(self, ev_fields):
        fields = []
        for field in ev_fields:
                fields.append(field + ' BLOB')
        return self._list_to_sql_str(fields, False)

    def _get_select_clauses(self, source_id, evfilter):
        s_clauses = []
        for select_clause in evfilter.SelectClauses:
            try:
                if not select_clause.BrowsePath:
                    s_clauses.append(select_clause.Attribute.name)
                else:
                    name = select_clause.BrowsePath[0].Name
                    s_clauses.append(name)
            except AttributeError:
                self.logger.error('Historizing SQL OPC UA Select Clauses Error for node %s', source_id)

        # remove select clauses that the event type doesn't have; SQL will error because the column doesn't exist
        clauses = [x for x in s_clauses if self._check(source_id, x)]

        return self._list_to_sql_str(clauses)

    def _check(self, source_id, s_clause):
        if s_clause in self._event_fields[source_id]:
            return True
        else:
            return False

    def _list_to_sql_str(self, ls, quotes=True):
        sql_str = ''
        for item in ls:
            if quotes:
                sql_str += '"' + item + '", '
            else:
                sql_str += item + ', '
        return sql_str[:-2]  # remove trailing space and comma for SQL syntax

    def stop(self):
        with self._lock:
            self._conn.close()
            self.logger.info('Historizing SQL connection closed')
