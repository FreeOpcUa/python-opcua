from datetime import timedelta
from datetime import datetime

from opcua import Subscription
from opcua import ua


class HistoryStorageInterface(object):
    """
    Interface of a history backend
    """
    def save_node_value(self, node, timestamp, datavalue):
        raise NotImplementedError

    def read_node_value(self, node, start, end):
        raise NotImplementedError

    def save_event(self, timestamp, event):
        raise NotImplementedError

    def read_event(self, event, start, end):
        raise NotImplementedError


class HistoryDict(HistoryStorageInterface):
    """
    very minimal history backend storing data in memory using a Python dictionnary
    """
    def __init__(self):
        self._datachanges = {}
        self._datachanges_period = {}
        self._events = {}

    def new_node(self, node, period):
        self._datachanges[node] = []
        self._datachanges_period[node] = period

    def new_event(self, period):
        self._events = []

    def save_node_value(self, node, datavalue):
        data = self._datachanges[node]
        period = self._datachanges_period[node]
        data.append(datavalue)
        now = datetime.now()
        while now - data[0].ServerTimestamp > period:
            data.pop(0)

    def read_node_value(self, node, start, end):
        if node not in self._datachanges:
            return []
        else:
            # FIME: improve algo
            return [dv for dv in self._datachanges[node] if start <= dv.ServerTimestamp <= end]

    def save_event(self, timestamp, event):
        raise NotImplementedError

    def read_event(self, event, start, end):
        raise NotImplementedError


class SubHandler(object):
    def __init__(self, storage):
        self.storage = storage

    def datachange_notification(self, node, val, data):
        print("Python: New data change event", node, val, data)
        self.storage.save_node_value(node, data.monitored_item.Value)

    def event_notification(self, event):
        print("Python: New event", event)
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

    def historize(self, node, period=timedelta(days=7)):
        if not self._sub:
            self._sub = self._create_subscription(SubHandler(self.storage))
        if node in self._handlers:
            raise ua.UaError("Node {} is allready historized".format(node))
        self.storage.new_node(node, period)
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
        if type(details) is ua.ReadRawModifiedDetails:
            pass
            
        self.storage.read_data()

    def update_history(self, params):
        """
        Update history for a node
        This is the part AttributeService, but implemented as its own service
        since it requires more logic than other attribute service methods
        """
        pass




