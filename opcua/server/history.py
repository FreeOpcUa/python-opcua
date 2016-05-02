from datetime import timedelta
from datetime import datetime

from opcua import Subscription
from opcua import ua
from opcua.common import utils
from opcua.common import event

import itertools


class HistoryStorageInterface(object):

    """
    Interface of a history backend.
    Must be implemented by backends
    """

    def new_historized_node(self, node_id, period, count=0):
        """
        Called when a new node is to be historized
        Returns None
        """
        raise NotImplementedError

    def save_node_value(self, node_id, datavalue):
        """
        Called when the value of a historized node has changed and should be saved in history
        Returns None
        """
        raise NotImplementedError

    def read_node_history(self, node_id, start, end, nb_values):
        """
        Called when a client make a history read request for a node
        if start or end is missing then nb_values is used to limit query
        nb_values is the max number of values to read. Ignored if 0
        Start time and end time are inclusive
        Returns a list of DataValues and a continuation point which
        is None if all nodes are read or the ServerTimeStamp of the last rejected DataValue
        """
        raise NotImplementedError

    def new_historized_event(self, source_id, etype, period):
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

    def read_event_history(self, source_id, start, end, nb_values, evfilter):
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
    very minimal history backend storing data in memory using a Python dictionary
    """
    def __init__(self):
        self._datachanges = {}
        self._datachanges_period = {}
        self._events = {}

    def new_historized_node(self, node_id, period, count=0):
        self._datachanges[node_id] = []
        self._datachanges_period[node_id] = period, count

    def save_node_value(self, node_id, datavalue):
        data = self._datachanges[node_id]
        period, count = self._datachanges_period[node_id]
        data.append(datavalue)
        now = datetime.utcnow()
        if period:
            while now - data[0].ServerTimestamp > period:
                data.pop(0)
        if count and len(data) > count:
            data = data[-count:]

    def read_node_history(self, node_id, start, end, nb_values):
        cont = None
        if node_id not in self._datachanges:
            print("Error attempt to read history for a node which is not historized")
            return [], cont
        else:
            if start is None:
                start = ua.DateTimeMinValue
            if end is None:
                end = ua.DateTimeMinValue
            if start == ua.DateTimeMinValue:
                results = [dv for dv in reversed(self._datachanges[node_id]) if start <= dv.ServerTimestamp]
            elif end == ua.DateTimeMinValue:
                results = [dv for dv in self._datachanges[node_id] if start <= dv.ServerTimestamp]
            elif start > end:
                results = [dv for dv in reversed(self._datachanges[node_id]) if end <= dv.ServerTimestamp <= start]

            else:
                results = [dv for dv in self._datachanges[node_id] if start <= dv.ServerTimestamp <= end]
            if nb_values and len(results) > nb_values:
                cont = results[nb_values + 1].ServerTimestamp
                results = results[:nb_values]
            return results, cont

    def new_historized_event(self, source_id, etype, period):
        self._events = []

    def save_event(self, event):
        raise NotImplementedError

    def read_event_history(self, source_id, start, end, nb_values, evfilter):
        raise NotImplementedError

    def stop(self):
        pass


class SubHandler(object):
    def __init__(self, storage):
        self.storage = storage

    def datachange_notification(self, node, val, data):
        self.storage.save_node_value(node.nodeid, data.monitored_item.Value)

    def event_notification(self, event):
        self.storage.save_event(event)


class HistoryManager(object):
    def __init__(self, iserver):
        self.iserver = iserver
        self.storage = HistoryDict()
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
            raise ua.UaError("Node {} is already historized".format(node))
        self.storage.new_historized_node(node.nodeid, period, count)
        handler = self._sub.subscribe_data_change(node)
        self._handlers[node] = handler

    def historize_event(self, source, period=timedelta(days=7)):
        if not self._sub:
            self._sub = self._create_subscription(SubHandler(self.storage))
        if source in self._handlers:  # FIXME a single source might have many event has a handlers, how to check?
            raise ua.UaError("Events from {} are already historized".format(source))

        # get the event types the source node generates and a list of all possible event fields
        event_types, ev_fields = self._get_source_event_data(source)

        self.storage.new_historized_event(source.nodeid, ev_fields, period)

        ev_handlers = []
        for event_type in event_types:
            handler = self._sub.subscribe_events(source, event_type)
            ev_handlers.append(handler)
        self._handlers[source] = ev_handlers  # FIXME no way to dehistorize because of this at the moment

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
            ev, cont = self._read_event_history(rv, details)
            result.HistoryData.Events = ev
            result.ContinuationPoint = cont

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
            #starttime = bytes_to_datetime(rv.ContinuationPoint)
            starttime = ua.unpack_datetime(utils.Buffer(rv.ContinuationPoint))

        dv, cont = self.storage.read_node_history(rv.NodeId,
                                                  starttime,
                                                  details.EndTime,
                                                  details.NumValuesPerNode)
        if cont:
            # cont = datetime_to_bytes(dv[-1].ServerTimestamp)
            cont = ua.pack_datetime(dv[-1].ServerTimestamp)  # FIXME pretty sure this isn't correct; should just pack cont itself, not dv[-1]
        # FIXME, parse index range and filter out if necessary
        # rv.IndexRange
        # rv.DataEncoding # xml or binary, seems spec say we can ignore that one
        return dv, cont

    def _read_event_history(self, rv, details):
        starttime = details.StartTime
        if rv.ContinuationPoint:
            # Spec says we should ignore details if cont point is present
            # but they also say we can use cont point as timestamp to enable stateless
            # implementation. This is contradictory, so we assume details is
            # send correctly with continuation point
            #starttime = bytes_to_datetime(rv.ContinuationPoint)
            starttime = ua.unpack_datetime(utils.Buffer(rv.ContinuationPoint))

        ev, cont = self.storage.read_event_history(rv.NodeId,
                                                   starttime,
                                                   details.EndTime,
                                                   details.NumValuesPerNode,
                                                   details.Filter)
        if cont:
            # cont = datetime_to_bytes(dv[-1].ServerTimestamp)
            cont = ua.pack_datetime(ev[-1].Time)  # FIXME pretty sure this isn't correct; should just pack cont itself, not ev[-1]
        return ev, cont

    def _get_source_event_data(self, source):
        # get all event types which the source node can generate; get the fields of those event types
        event_types = source.get_referenced_nodes(ua.ObjectIds.GeneratesEvent)

        ev_aggregate_fields = []
        for event_type in event_types:
            ev_aggregate_fields.extend((event.get_event_properties_from_type_node(event_type)))

        ev_fields = []
        for field in set(ev_aggregate_fields):
            ev_fields.append(field.get_display_name().Text.decode(encoding='utf-8'))
        return event_types, ev_fields

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
