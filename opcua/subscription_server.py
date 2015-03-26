"""
server side implementation of subscriptions
"""
from threading import RLock, Timer, Thread, Condition
import logging
import asyncio
import functools

from opcua import ua


class SubscriptionManager(Thread):
    def __init__(self, aspace):
        Thread.__init__(self)
        self.logger = logging.getLogger(self.__class__.__name__)
        self.loop = None
        self.aspace = aspace
        self.subscriptions = {}
        self._sub_id_counter = 77
        self._cond = Condition()

    def start(self):
        print("start internal")
        Thread.start(self)
        with self._cond:
            self._cond.wait()
        print("start internal finished")

    def run(self):
        self.logger.warn("Starting subscription thread")
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        with self._cond:
            self._cond.notify_all()
        self.loop.run_forever()
        print("LOOP", self.loop)

    def add_task(self, coro):
        """
        execute a coroutine in subscription loop
        threadsafe method
        """
        f = functools.partial(self.loop.create_task, coro)
        return self.loop.call_soon_threadsafe(f)

    def stop(self):
        """
        stop subscription loop, thus the subscription thread
        """
        self.loop.call_soon_threadsafe(self.loop.stop)

    def create_subscription(self, params, callback):
        self.logger.info("create subscription")
        result = ua.CreateSubscriptionResult()
        self._sub_id_counter += 1
        result.SubscriptionId = self._sub_id_counter
        result.RevisedPublishingInterval = params.RequestedPublishingInterval
        result.RevisedLifetimeCount = params.RequestedLifetimeCount
        result.RevisedMaxKeepAliveCount = params.RequestedMaxKeepAliveCount

        sub = Subscription(self, result, self.aspace, callback)
        sub.start()
        self.subscriptions[result.SubscriptionId] = sub

        return result

    def delete_subscriptions(self, ids):
        self.logger.info("delete subscription")
        res = []
        for i in ids:
            sub = self.subscriptions.pop(i)
            sub.stop()
            res.append(ua.StatusCode())
        return res

    def publish(self, acks):
        self.logger.warn("publish request with acks %s", acks)

    def create_monitored_items(self, params):
        self.logger.info("create monitored items")
        if not params.SubscriptionId in self.subscriptions:
            res = []
            for _ in params.ItemsToCreate:
                response = ua.MonitoredItemCreateResult()
                response.StatusCode = ua.StatusCode(ua.StatusCodes.BadSubscriptionIdInvalid)
                res.append(response)
            return res
        return self.subscriptions[params.SubscriptionId].create_monitored_items(params)


class MonitoredItemData(object):
    def __init__(self):
        self.client_handle = None
        self.callback_handle = None
        self.monitored_item_id = None
        self.parameters = None
        self.mode = None
            

class Subscription(object):
    def __init__(self, manager, data, addressspace, callback):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.aspace = addressspace
        self.manager = manager
        self.data = data
        self.callback = callback
        self.task = None
        self._monitored_item_counter = 111
        self._monitored_events = {}
        self._monitored_datachange = {}

    def start(self):
        self.task = self.manager.add_task(self.loop())
    
    def stop(self):
        self.task.cancel()

    @asyncio.coroutine
    def loop(self):
        self.logger.debug("starting subscription %s", self.data.SubscriptionId)
        while True:
            self.publish_results()
            yield from asyncio.sleep(1)

    def publish_results(self): 
        print("looking for results and publishing")

    def create_monitored_items(self, params):
        results = []
        for item in params.ItemsToCreate:
            results.append(self._create_monitored_item(item))
        return results

    def _create_monitored_item(self, params):
        result = ua.MonitoredItemCreateResult()
        result.RevisedSamplingInterval = self.data.RevisedPublishingInterval
        result.RevisedQueueSize = params.RequestedParameters.QueueSize #FIXME check and use value
        result.FilterResult = params.RequestedParameters.Filter
        self._monitored_item_counter += 1
        result.MonitoredItemId = self._monitored_item_counter
        if params.ItemToMonitor.AttributeId == ua.AttributeIds.EventNotifier:
            self.logger.info("request to subscribe to events")
            self._monitored_events[params.ItemToMonitor.NodeId] = result.MonitoredItemId
        else:
            self.logger.info("request to subscribe to datachange")
            result.StatusCode, handle = self.aspace.add_datachange_callback(params.ItemToMonitor.NodeId, params.ItemToMonitor.AttributeId, self.datachange_callback)

        mdata = MonitoredItemData()
        mdata.parameters = result
        mdata.Mode = params.MonitoringMode
        mdata.client_handle = params.RequestedParameters.ClientHandle
        mdata.callback_handle = handle
        mdata.monitored_item_id = result.MonitoredItemId 
        self._monitored_datachange[result.MonitoredItemId] = mdata

        #FIXME force event generation

        return result

    def datachange_callback(self, handle, value):
        self.logger.warn("subscription %s: datachange callback called with %s, %s", self, handle, value)





