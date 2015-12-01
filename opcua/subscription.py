"""
high level interface to subscriptions
"""
import io
import time
import logging
from threading import Lock

from opcua import ua
from opcua import Node
from opcua import ObjectIds
from opcua import AttributeIds
#from opcua import Event


class EventResult():

    def __str__(self):
        return "EventResult({})".format([str(k) + ":" + str(v) for k, v in self.__dict__.items()])
    __repr__ = __str__


class SubscriptionItemData():

    def __init__(self):
        self.node = None
        self.client_handle = None
        self.server_handle = None
        self.attribute = None
        self.mfilter = None


class Subscription(object):
    """
    Subscription object returned by Server or Client objects.
    The object represent a subscription to an opc-ua server.
    This is a high level class, especially subscribe_data_change 
    and subscribe_events methods. If more control is necessary look at
    code and/or use create_monitored_items method.
    """

    def __init__(self, server, params, handler):
        self.logger = logging.getLogger(__name__)
        self.server = server
        self._client_handle = 200
        self._handler = handler
        self.parameters = params  # move to data class
        self._monitoreditems_map = {}
        self._lock = Lock()
        self.subscription_id = None
        response = self.server.create_subscription(params, self.publish_callback)
        self.subscription_id = response.SubscriptionId  # move to data class
        self.server.publish()
        self.server.publish()

    def delete(self):
        """
        Delete subscription on server. This is automatically done by Client and Server classes on exit
        """
        results = self.server.delete_subscriptions([self.subscription_id])
        results[0].check()

    def publish_callback(self, publishresult):
        self.logger.info("Publish callback called with result: %s", publishresult)
        while self.subscription_id is None:
            time.sleep(0.01)

        for notif in publishresult.NotificationMessage.NotificationData:
            if isinstance(notif, ua.DataChangeNotification):
                self._call_datachange(notif)
            elif isinstance(notif, ua.EventNotificationList):
                self._call_event(notif)
            elif isinstance(notif, ua.StatusChangeNotification):
                self._call_status(notif)
            else:
                self.logger.warning("Notification type not supported yet for notification %s", notif)

        ack = ua.SubscriptionAcknowledgement()
        ack.SubscriptionId = self.subscription_id
        ack.SequenceNumber = publishresult.NotificationMessage.SequenceNumber
        self.server.publish([ack])

    def _call_datachange(self, datachange):
        for item in datachange.MonitoredItems:
            with self._lock:
                if item.ClientHandle not in self._monitoreditems_map:
                    self.logger.warning("Received a notification for unknown handle: %s", item.ClientHandle)
                    continue
                data = self._monitoreditems_map[item.ClientHandle]
            try:
                self._handler.data_change(data.server_handle, data.node, item.Value.Value.Value, data.attribute)
            except Exception:
                self.logger.exception("Exception calling data change handler")

    def _call_event(self, eventlist):
        for event in eventlist.Events:
            with self._lock:
                data = self._monitoreditems_map[event.ClientHandle]
            try:
                #fields = {}
                result = EventResult()
                for idx, sattr in enumerate(data.mfilter.SelectClauses):

                    if len(sattr.BrowsePath) == 0:
                        #fields[ua.AttributeIdsInv[sattr.AttributeId]] = event.EventFields[idx].Value
                        setattr(result, ua.AttributeIdsInv[sattr.AttributeId], event.EventFields[idx].Value)
                    else:
                        setattr(result, sattr.BrowsePath[0].Name, event.EventFields[idx].Value)
                #self._handler.event(data.server_handle, fields)
                self._handler.event(data.server_handle, result)
            except Exception:
                self.logger.exception("Exception calling event handler")

    def _call_status(self, status):
        try:
            self._handler.status_change(status.Status)
        except Exception:
            self.logger.exception("Exception calling status change handler")

    def subscribe_data_change(self, nodes, attr=ua.AttributeIds.Value):
        """
        Subscribe for data change events for a node or list of nodes.
        default attribute is Value.
        Return a handle which can be used to unsubscribe
        If more control is necessary use create_monitored_items method
        """
        return self._subscribe(nodes, attr, queuesize=1)

    def _get_node(self, nodeid):
        if isinstance(nodeid, ua.NodeId):
            node = Node(self.server, nodeid)
        elif isinstance(nodeid, Node):
            node = nodeid
        else:
            node = Node(self.server, ua.NodeId(nodeid))
        return node

    def _get_filter_from_event_type(self, eventtype):
        eventtype = self._get_node(eventtype)
        evfilter = ua.EventFilter()
        for desc in eventtype.get_children_descriptions(refs=ua.ObjectIds.HasProperty, nodeclassmask=ua.NodeClass.Variable):
            op = ua.SimpleAttributeOperand()
            op.TypeDefinitionId = eventtype.nodeid
            op.AttributeId = AttributeIds.Value
            op.BrowsePath = [desc.BrowseName]
            evfilter.SelectClauses.append(op)
        return evfilter

    def subscribe_events(self, sourcenode=ObjectIds.Server, evtype=ObjectIds.BaseEventType):
        """
        Subscribe to events from a node. Default node is Server node. 
        In most servers the server node is the only one you can subscribe to.
        Return a handle which can be used to unsubscribe
        """
        sourcenode = self._get_node(sourcenode)
        evfilter = self._get_filter_from_event_type(evtype)
        return self._subscribe(sourcenode, AttributeIds.EventNotifier, evfilter)

    def _subscribe(self, nodes, attr, mfilter=None, queuesize=0):
        is_list = True
        if not type(nodes) in (list, tuple):
            is_list = False
            nodes = [nodes]
        mirs = []
        for node in nodes:
            mir = self._make_monitored_item_request(node, attr, mfilter, queuesize)
            mirs.append(mir)

        mids = self.create_monitored_items(mirs)
        if is_list:
            return mids
        if type(mids[0]) == ua.StatusCode:
            mids[0].check()
        return mids[0]

    def _make_monitored_item_request(self, node, attr, mfilter, queuesize):
        rv = ua.ReadValueId()
        rv.NodeId = node.nodeid
        rv.AttributeId = attr
        # rv.IndexRange //We leave it null, then the entire array is returned
        mparams = ua.MonitoringParameters()
        with self._lock:
            self._client_handle += 1
            mparams.ClientHandle = self._client_handle
        mparams.SamplingInterval = self.parameters.RequestedPublishingInterval
        mparams.QueueSize = queuesize
        mparams.DiscardOldest = True
        if mfilter:
            mparams.Filter = mfilter
        mir = ua.MonitoredItemCreateRequest()
        mir.ItemToMonitor = rv
        mir.MonitoringMode = ua.MonitoringMode.Reporting
        mir.RequestedParameters = mparams
        return mir

    def create_monitored_items(self, monitored_items):
        """
        low level method to have full control over subscription parameters
        Client handle must be unique since it will be used as key for internal registration of data
        """
        params = ua.CreateMonitoredItemsParameters()
        params.SubscriptionId = self.subscription_id
        params.ItemsToCreate = monitored_items
        params.TimestampsToReturn = ua.TimestampsToReturn.Neither
        
        mids = []
        results = self.server.create_monitored_items(params)
        # FIXME: Race condition here
        # We lock as early as possible. But in some situation, a notification may arrives before
        # locking and we will not be able to prosess it. To avoid issues, users should subscribe 
        # to all nodes at once
        with self._lock:  
            for idx, result in enumerate(results):
                mi = params.ItemsToCreate[idx]
                if not result.StatusCode.is_good():
                    mids.append(result.StatusCode)
                    continue
                data = SubscriptionItemData()
                data.client_handle = mi.RequestedParameters.ClientHandle
                data.node = Node(self.server, mi.ItemToMonitor.NodeId)
                data.attribute = mi.ItemToMonitor.AttributeId
                data.server_handle = result.MonitoredItemId
                data.mfilter = result.FilterResult
                self._monitoreditems_map[mi.RequestedParameters.ClientHandle] = data

                mids.append(result.MonitoredItemId)
        return mids

    def unsubscribe(self, handle):
        """
        unsubscribe to datachange or events using the handle returned while subscribing
        if you delete subscription, you do not need to unsubscribe
        """
        params = ua.DeleteMonitoredItemsParameters()
        params.SubscriptionId = self.subscription_id
        params.MonitoredItemIds = [handle]
        results = self.server.delete_monitored_items(params)
        results[0].check()
        with self._lock:
            for k, v in self._monitoreditems_map.items():
                if v.server_handle == handle:
                    del(self._monitoreditems_map[k])
                    return

