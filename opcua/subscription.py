"""
high level interface to subscriptions
"""
import io
import time
import logging
from threading import RLock

import opcua.uaprotocol as ua


class SubscriptionItemData():
    def __init__(self):
        self.node = None
        self.client_handle = None
        self.server_handle = None
        self.attribute = None

class Subscription(object):
    def __init__(self, server, params, handler):
        self.logger = logging.getLogger(__name__)
        self.server = server
        self._client_handle = 200
        self._handler = handler
        self.parameters = params #move to data class
        self._monitoreditems_map = {}
        self._lock = RLock()
        self.subscription_id = None
        response = self.server.create_subscription(params, self.publish_callback)
        self.subscription_id = response.SubscriptionId #move to data class
        self.server.publish()
        self.server.publish()

    def delete(self):
        results = self.server.delete_subscriptions([self.subscription_id])
        results[0].check()

    def publish_callback(self, publishresult):
        self.logger.info("Publish callback called with result: %s", publishresult)
        while self.subscription_id is None:
            time.sleep(0.01)

        for notif in publishresult.NotificationMessage.NotificationData:
            if notif.TypeId == ua.FourByteNodeId(ua.ObjectIds.DataChangeNotification_Encoding_DefaultBinary):
                datachange = ua.DataChangeNotification.from_binary(io.BytesIO(notif.to_binary()))
                self._call_datachange(datachange)
            elif notif.TypeId == ua.FourByteNodeId(ua.ObjectIds.EventNotificationList_Encoding_DefaultBinary):
                eventlist = ua.EventNotificationList.from_binary(io.BytesIO(notif.to_binary()))
                self._call_event(eventlist)
            elif notif.TypeId == ua.FourByteNodeId(ua.ObjectIds.StatusChangeNotification_Encoding_DefaultBinary):
                statuschange = ua.StatusChangeNotification.from_binary(io.BytesIO(notif.to_binary()))
                self._call_status(statuschange)
            else:
                self.logger.warn("Notification type not supported yet for notification %s", notif)
        
        ack = ua.SubscriptionAcknowledgement()
        ack.SubscriptionId = self.subscription_id
        ack.SequenceNumber = publishresult.NotificationMessage.SequenceNumber
        self.server.publish([ack])

    def _call_datachange(self, datachange):
        for item in datachange.MonitoredItems:
            data = self._monitoreditems_map[item.ClientHandle]
            self._handler.data_change(data.server_handle, data.node, item.Value.Value.Value, data.attribute)

    def _call_event(self, eventlist):
        print(eventlist)
        self.logger.warn("Not implemented")

    def _call_status(self, status):
        print(status)
        self.logger.warn("Not implemented")


    def subscribe_data_change(self, node, attr=ua.AttributeIds.Value):
        rv = ua.ReadValueId()
        rv.NodeId = node.nodeid
        rv.AttributeId = attr
        #rv.IndexRange //We leave it null, then the entire array is returned
        mparams = ua.MonitoringParameters()
        self._client_handle += 1
        mparams.ClientHandle = self._client_handle
        mparams.SamplingInterval = self.parameters.RequestedPublishingInterval
        mparams.QueueSize = 1
        mparams.DiscardOldest = True

        mir = ua.MonitoredItemCreateRequest() 
        mir.ItemToMonitor = rv
        mir.MonitoringMode = ua.MonitoringMode.Reporting
        mir.RequestedParameters = mparams

        params = ua.CreateMonitoredItemsParameters()
        params.SubscriptionId = self.subscription_id
        params.ItemsToCreate.append(mir)
        params.TimestampsToReturn = ua.TimestampsToReturn.Neither

        results = self.server.create_monitored_items(params)
        result = results[0]
        result.StatusCode.check()
        
        data = SubscriptionItemData()
        data.client_handle = mparams.ClientHandle
        data.node = node
        data.attribute = attr
        data.server_handle = result.MonitoredItemId
        self._monitoreditems_map[mparams.ClientHandle] = data

        return result.MonitoredItemId

    def unsubscribe(self, handle):
        params = ua.DeleteMonitoredItemsParameters()
        params.SubscriptionId = self.subscription_id
        params.MonitoredItemIds = [handle]
        results = self.server.delete_monitored_items(params)
        results[0].check()
        

