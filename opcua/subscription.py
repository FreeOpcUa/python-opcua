"""
high level interface to subscriptions
"""
import logging

import opcua.uaprotocol as ua

class Subscription(object):
    def __init__(self, server, params, handler):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.server = server
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
        

