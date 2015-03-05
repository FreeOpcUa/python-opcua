"""
high level interface to subscriptions
"""
import logging

import opcua.uaprotocol as ua

class Subscription(object):
    def __init__(self, server, params, handler):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.server = server
        self._client_handle = 200
        self.parameters = params #move to data class
        response = self.server.create_subscription(params, handler)
        self.subscription_id = response.SubscriptionId #move to data class
        self.server.publish(ua.PublishRequest())
        self.server.publish(ua.PublishRequest())

    def delete(self):
        results = self.server.delete_subscriptions([self.subscription_id])
        results[0].check()

    def publish_callback(self, publishresult):
        self.logger.info("Publish callback called with result: %s", publishresult)

    def subscribe_data_change(self, node, attr=ua.AttributeIds.Value):
        rv = ua.ReadValueId()
        rv.NodeId = node.nodeid
        rv.AttributeId = attr
        #rv.IndexRange //We leave it null, then the entire array is returned
        mparams = ua.MonitoringParameters()
        self._client_handle += 1
        mparams.ClientHandle = self._client_handle
        mparams.SamplingInterval = self.parameters.RequestedPublishingInterval

        mir = ua.MonitoredItemCreateRequest() 
        mir.ItemToMonitor = rv
        mir.RequestedParameters = mparams

        params = ua.CreateMonitoredItemsParameters()
        params.SubscriptionId = self.subscription_id
        params.ItemsToCreate.append(mir)

        results = self.server.create_monitored_items(params)
        result = results[0]
        result.StatusCode.check()

        return result.MonitoredItemId
        

