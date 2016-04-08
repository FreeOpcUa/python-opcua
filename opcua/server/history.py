from datetime import timedelta
from datetime import datetime

from opcua import Subscription
from opcua import ua

import sqlite3


class HistoryStorageInterface(object):

    """
    Interface of a history backend.
    Must be implemented by backends
    """

    def new_historized_node(self, node, period, count=0):
        """
        Called when a new node is to be historized
        Returns None
        """
        raise NotImplementedError

    def save_node_value(self, node, datavalue):
        """
        Called when the value of a historized node has changed and should be saved in history
        Returns None
        """
        raise NotImplementedError

    def read_node_history(self, node, start, end, nb_values):
        """
        Called when a client make a history read request for a node
        if start or end is missing then nb_values is used to limit query
        nb_values is the max number of values to read. Ignored if 0
        Start time and end time are inclusive
        Returns a list of DataValues and a continuation point which
        is None if all nodes are read or the ServerTimeStamp of the last rejected DataValue
        """
        raise NotImplementedError

    def new_historized_event(self, event, period):
        """
        Called when historization of events is enabled on server side
        FIXME: we may need to store events per nodes in future...
        Returns None
        """
        raise NotImplementedError

    def save_event(self, event):
        """
        Called when a new event has been generated ans should be saved in history
        Returns None
        """
        raise NotImplementedError

    def read_event_history(self, start, end, evfilter):
        """
        Called when a client make a history read request for events
        Start time and end time are inclusive
        Returns a list of Events and a continuation point which
        is None if all events are read or the ServerTimeStamp of the last rejected event
        """
        raise NotImplementedError

    def stop(self):
        """
        Called when the server shuts down
        Can be used to close database connections etc.
        """
        raise NotImplementedError


class HistoryDict(HistoryStorageInterface):
    """
    very minimal history backend storing data in memory using a Python dictionnary
    """
    def __init__(self):
        self._datachanges = {}
        self._datachanges_period = {}
        self._events = {}

    def new_historized_node(self, node, period, count=0):
        node_id = node.nodeid
        self._datachanges[node_id] = []
        self._datachanges_period[node_id] = period, count

    def save_node_value(self, node, datavalue):
        node_id = node.nodeid
        data = self._datachanges[node_id]
        period, count = self._datachanges_period[node_id]
        data.append(datavalue)
        now = datetime.now()
        if period:
            while now - data[0].ServerTimestamp > period:
                data.pop(0)
        if count and len(data) > count:
            data = data[-count:]

    def read_node_history(self, node, start, end, nb_values):
        node_id = node.NodeId
        cont = None
        if node_id not in self._datachanges:
            print("Error attempt to read history for a node which is not historized")
            return [], cont
        else:
            if end is None:
                end = datetime.now() + timedelta(days=1)
            if start is None:
                start = ua.DateTimeMinValue
            results = [dv for dv in self._datachanges[node_id] if start <= dv.ServerTimestamp <= end]
            if nb_values:
                if start > ua.DateTimeMinValue and len(results) > nb_values:
                    cont = results[nb_values + 1].ServerTimestamp
                    results = results[:nb_values]
                else:
                    results = results[-nb_values:]
            return results, cont

    def new_historized_event(self, event, period):
        self._events = []

    def save_event(self, event):
        raise NotImplementedError

    def read_event_history(self, start, end, evfilter):
        raise NotImplementedError

    def stop(self):
        pass


class HistorySQLite(HistoryStorageInterface):
    """
    very minimal history backend storing data in SQLite database
    """
    # FIXME: need to check on if sql_conn.commit() should be inside try block; and if .rollback() needs to be except

    def __init__(self):
        self._datachanges_period = {}
        self._events = {}
        self._db_file = "history.db"

        # SQL objects must be accessed in a single thread
        # adding a new node to be historized probably happens on the main thread
        self._conn_new = None
        self._c_new = None

        # subscriptions are in another thread so it needs it's own sqlite connection object
        self._conn_sub = None
        self._c_sub = None

        # FIXME: no idea what thread the read values happen in, just make a new conn object for now
        self._conn_read = None
        self._c_read = None

    def new_historized_node(self, node, period, count=0):
        if self._conn_new is None:
            self._conn_new = sqlite3.connect(self._db_file)
            self._c_new = self._conn_new.cursor()

        node_id = str(node.nodeid.NamespaceIndex) + '_' + str(node.nodeid.Identifier)
        self._datachanges_period[node_id] = period

        self._conn_new = sqlite3.connect(self._db_file)
        self._c_new = self._conn_new.cursor()

        sql_type = self._get_sql_type(node)

        # create a table for the node which will store attributes of the DataValue object
        try:
            self._c_new.execute('CREATE TABLE "{tn}" (ServerTimestamp TIMESTAMP,'
                               ' SourceTimestamp TIMESTAMP,'
                               ' StatusCode INTEGER,'
                               ' Value {type},'
                               ' VariantType INTEGER)'.format(tn=node_id, type=sql_type))

        except sqlite3.Error as e:
            print(node_id, 'Historizing SQL Table Creation Error:', e)

        self._conn_new.commit()
        self._conn_new.close()

    def save_node_value(self, node, datavalue):
        if self._conn_sub is None:
            self._conn_sub = sqlite3.connect(self._db_file, detect_types=sqlite3.PARSE_DECLTYPES)
            self._c_sub = self._conn_sub.cursor()

        node_id = str(node.nodeid.NamespaceIndex) + '_' + str(node.nodeid.Identifier)

        # insert the data change into the database
        try:
            self._c_sub.execute('INSERT INTO "{tn}" VALUES (?, ?, ?, ?, ?)'.format(tn=node_id), (datavalue.ServerTimestamp,
                                                                                                 datavalue.SourceTimestamp,
                                                                                                 datavalue.StatusCode.value,
                                                                                                 datavalue.Value.Value,
                                                                                                 datavalue.Value.VariantType.value))
        except sqlite3.Error as e:
            print(node_id, 'Historizing SQL Insert Error:', e)

        # get this node's period from the period dict and calculate the limit
        period = self._datachanges_period[node_id]
        date_limit = datetime.now() - period

        # after the insert, delete all values older than period
        try:
            self._c_sub.execute('DELETE FROM "{tn}" WHERE ServerTimestamp < ?'.format(tn=node_id), (date_limit.isoformat(' '),))
        except sqlite3.Error as e:
            print(node_id, 'Historizing SQL Delete Old Data Error:', e)

        self._conn_sub.commit()

    def read_node_history(self, node, start, end, nb_values):
        if self._conn_read is None:
            self._conn_read = sqlite3.connect(self._db_file, detect_types=sqlite3.PARSE_DECLTYPES)
            self._c_read = self._conn_read.cursor()

        if end is None:
            end = datetime.now() + timedelta(days=1)
        if start is None:
            start = ua.DateTimeMinValue

        node_id = str(node.NodeId.NamespaceIndex) + '_' + str(node.NodeId.Identifier)
        cont = None
        results = []

        start_time = start.isoformat(' ')
        end_time = end.isoformat(' ')

        # select values from the database
        try:
            for row in self._c_read.execute('SELECT * FROM "{tn}" WHERE "ServerTimestamp" BETWEEN ? AND ? '
                                           'LIMIT ?'.format(tn=node_id), (start_time, end_time, nb_values,)):

                dv = ua.DataValue(ua.Variant(row[3], self._get_variant_type(row[4])))
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

    # convert the node UA Variant type to an SQL supported type
    # FIXME: this could lead to lost precision! Better way to store the data? Add custom types to SQL?
    def _get_sql_type(self, node):
        node_type = node.get_data_type()
        # see object_ids.py
        if node_type.Identifier in (10, 11,):  # Float, Double
            return 'REAL'
        elif node_type.Identifier in (4, 5, 6, 7, 8, 9,):  # Ints
            return "INT"
        elif node_type.Identifier in (12,):  # String
            return "TEXT"
        else:
            return "NULL"

    # convert the OPC UA variant identifier stored in SQL back to a UA Variant
    # FIXME: is there a util method someplace for getting this?
    def _get_variant_type(self, identifier):
        if identifier is 10:
            return ua.VariantType.Float
        elif identifier is 11:
            return ua.VariantType.Double
        elif identifier is 4:
            return ua.VariantType.Int16
        elif identifier is 5:
            return ua.VariantType.UInt16
        elif identifier is 6:
            return ua.VariantType.Int32
        elif identifier is 7:
            return ua.VariantType.UInt32
        elif identifier is 8:
            return ua.VariantType.Int64
        elif identifier is 9:
            return ua.VariantType.UInt64
        elif identifier is 12:
            return ua.VariantType.String

    # close connections to the history database when the server stops
    def stop(self):
        pass
        # FIXME: Should close the database connections when the server stops, but because server.stop() is called
        # FIXME: on a different thread than the SQL conn object, no idea how to do this at the moment


class SubHandler(object):
    def __init__(self, storage):
        self.storage = storage

    def datachange_notification(self, node, val, data):
        self.storage.save_node_value(node, data.monitored_item.Value)  # SHOULD NOT GET NODE ID HERE

    def event_notification(self, event):
        self.storage.save_event(event)


class HistoryManager(object):
    def __init__(self, iserver):
        self.iserver = iserver
        self.storage = HistorySQLite()  # HistoryDict() HistorySQLite()
        self._sub = None
        self._handlers = {}

    def set_storage(self, storage):
        self.storage = storage

    def _create_subscription(self, handler):
        params = ua.CreateSubscriptionParameters()
        params.RequestedPublishingInterval = 10
        params.RequestedLifetimeCount = 3000
        params.RequestedMaxKeepAliveCount = 10000
        params.MaxNotificationsPerPublish = 0
        params.PublishingEnabled = True
        params.Priority = 0
        return Subscription(self.iserver.isession, params, handler)

    def historize(self, node, period=timedelta(days=7), count=0):
        if not self._sub:
            self._sub = self._create_subscription(SubHandler(self.storage))
        if node in self._handlers:
            raise ua.UaError("Node {} is allready historized".format(node))
        self.storage.new_historized_node(node, period, count)  # SHOULD NOT GET NODE ID HERE
        handler = self._sub.subscribe_data_change(node)
        self._handlers[node] = handler

    def dehistorize(self, node):
        self._sub.unsubscribe(self._handlers[node])
        del(self._handlers[node])

    def read_history(self, params):
        """
        Read history for a node
        This is the part AttributeService, but implemented as its own service
        since it requires more logic than other attribute service methods
        """
        results = []
        
        for rv in params.NodesToRead:
            res = self._read_history(params.HistoryReadDetails, rv)
            results.append(res)
        return results
        
    def _read_history(self, details, rv):
        """
        read history for a node
        """
        result = ua.HistoryReadResult()
        if isinstance(details, ua.ReadRawModifiedDetails):
            if details.IsReadModified:
                result.HistoryData = ua.HistoryModifiedData()
                # we do not support modified history by design so we return what we have
            else:
                result.HistoryData = ua.HistoryData()
            dv, cont = self._read_datavalue_history(rv, details)
            result.HistoryData.DataValues = dv
            result.ContinuationPoint = cont

        elif isinstance(details, ua.ReadEventDetails):
            result.HistoryData = ua.HistoryEvent()
            # FIXME: filter is a cumbersome type, maybe transform it something easier
            # to handle for storage
            result.HistoryData.Events = self.storage.read_event_history(details.StartTime,
                                                                        details.EndTime,
                                                                        details.Filter)
        else:
            # we do not currently support the other types, clients can process data themselves
            result.StatusCode = ua.StatusCode(ua.StatusCodes.BadNotImplemented)
        return result

    def _read_datavalue_history(self, rv, details):
        starttime = details.StartTime
        if rv.ContinuationPoint:
            # Spec says we should ignore details if cont point is present
            # but they also say we can use cont point as timestamp to enable stateless
            # implementation. This is contradictory, so we assume details is
            # send correctly with continuation point
            # starttime = bytes_to_datetime(rv.ContinuationPoint)
            starttime = ua.unpack_datetime(rv.ContinuationPoint)

        dv, cont = self.storage.read_node_history(rv,  # SHOULD NOT GET NODE ID HERE!
                                                  starttime,
                                                  details.EndTime,
                                                  details.NumValuesPerNode)
        if cont:
            # cont = datetime_to_bytes(dv[-1].ServerTimestamp)
            cont = ua.pack_datetime(dv[-1].ServerTimestamp)
        # FIXME, parse index range and filter out if necessary
        # rv.IndexRange
        # rv.DataEncoding # xml or binary, seems spec say we can ignore that one
        return dv, cont

    def update_history(self, params):
        """
        Update history for a node
        This is the part AttributeService, but implemented as its own service
        since it requires more logic than other attribute service methods
        """
        results = []
        for _ in params.HistoryUpdateDetails:
            result = ua.HistoryUpdateResult()
            # we do not accept to rewrite history
            result.StatusCode = ua.StatusCode(ua.StatusCodes.BadNotWritable)
            results.append(results)
        return results

    def stop(self):
        self.storage.stop()
