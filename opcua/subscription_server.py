"""
server side implementation of subscriptions
"""
from threading import RLock, Thread, Condition
from concurrent.futures import Future
import logging
import asyncio
import functools

from opcua import ua


class SubscriptionManager(Thread):
    def __init__(self, aspace):
        Thread.__init__(self)
        self.logger = logging.getLogger(__name__)
        self.loop = None
        self.aspace = aspace
        self.subscriptions = {}
        self._sub_id_counter = 77
        self._cond = Condition()
        self._lock = RLock()

    def start(self):
        Thread.start(self)
        with self._cond:
            self._cond.wait()

    def run(self):
        self.logger.debug("Starting subscription thread")
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        with self._cond:
            self._cond.notify_all()
        self.loop.run_forever()
        self.logger.debug("subsription thread ended")

    def _add_task(self, future, coro):
        task = self.loop.create_task(coro)
        future.set_result(task)

    def add_task(self, coro):
        """
        execute a coroutine in subscription loop
        threadsafe method
        """
        future = Future() #from concurrent, NOT asyncio
        p = functools.partial(self._add_task, future, coro)
        self.loop.call_soon_threadsafe(p)
        return future.result() #wait until result is available

    def cancel_task(self, task):
        """
        threadsafe stop task
        """
        self.loop.call_soon_threadsafe(task.cancel)

    def stop(self):
        """
        stop subscription loop, thus the subscription thread
        """
        self.loop.call_soon_threadsafe(self.loop.stop)

    def create_subscription(self, params, callback):
        self.logger.info("create subscription")
        print(self.loop, self)
        with self._lock:
            result = ua.CreateSubscriptionResult()
            self._sub_id_counter += 1
            result.SubscriptionId = self._sub_id_counter
            result.RevisedPublishingInterval = params.RequestedPublishingInterval
            result.RevisedLifetimeCount = params.RequestedLifetimeCount
            result.RevisedMaxKeepAliveCount = params.RequestedMaxKeepAliveCount

            sub = InternalSubscription(self, result, self.aspace, callback)
            sub.start()
            self.subscriptions[result.SubscriptionId] = sub

            return result

    def delete_subscriptions(self, ids):
        self.logger.info("delete subscription")
        with self._lock:
            res = []
            for i in ids:
                if not i in self.subscriptions:
                    res.append(ua.StatusCode(ua.StatusCodes.BadSubscriptionsIdInvalid))
                else:
                    sub = self.subscriptions.pop(i)
                    sub.stop()
                    res.append(ua.StatusCode())
            return res

    def publish(self, acks):
        self.logger.info("publish request with acks %s", acks)

    def create_monitored_items(self, params):
        self.logger.info("create monitored items")
        with self._lock:
            if not params.SubscriptionId in self.subscriptions:
                res = []
                for _ in params.ItemsToCreate:
                    response = ua.MonitoredItemCreateResult()
                    response.StatusCode = ua.StatusCode(ua.StatusCodes.BadSubscriptionIdInvalid)
                    res.append(response)
                return res
            return self.subscriptions[params.SubscriptionId].create_monitored_items(params)

    def delete_monitored_items(self, params):
        self.logger.info("delete monitored items")
        with self._lock:
            if not params.SubscriptionId in self.subscriptions:
                res = []
                for _ in params.MonitoredItemIds:
                    res.append(ua.StatusCode(ua.StatusCodes.BadSubscriptionIdInvalid))
                return res
            return self.subscriptions[params.SubscriptionId].delete_monitored_items(params)



class MonitoredItemData(object):
    def __init__(self):
        self.client_handle = None
        self.callback_handle = None
        self.monitored_item_id = None
        self.parameters = None
        self.mode = None
            

class InternalSubscription(object):
    def __init__(self, manager, data, addressspace, callback):
        self.logger = logging.getLogger(__name__)
        self.aspace = addressspace
        self.manager = manager
        self.data = data
        self.callback = callback
        self.task = None
        self._monitored_item_counter = 111
        self._monitored_events = {}
        self._monitored_datachange = {}
        self._lock = RLock()

    def start(self):
        self.logger.debug("starting subscription %s", self.data.SubscriptionId)
        self.task = self.manager.add_task(self.subscription_loop())
    
    def stop(self):
        self.logger.debug("stopping subscription %s", self.data.SubscriptionId)
        self.manager.cancel_task(self.task)

    @asyncio.coroutine
    def subscription_loop(self):
        while True:
            self.publish_results()
            yield from asyncio.sleep(1)

    def publish_results(self): 
        self.logger.debug("looking for results and publishing")

    def create_monitored_items(self, params):
        results = []
        for item in params.ItemsToCreate:
            results.append(self._create_monitored_item(item))
        return results

    def _create_monitored_item(self, params):
        with self._lock:
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
            mdata.mode = params.MonitoringMode
            mdata.client_handle = params.RequestedParameters.ClientHandle
            mdata.callback_handle = handle
            mdata.monitored_item_id = result.MonitoredItemId 
            self._monitored_datachange[result.MonitoredItemId] = mdata

            #FIXME force event generation

            return result

    def delete_monitored_items(self, params):
        with self._lock:
            results = []
            for mid in params.MonitoredItemIds:
                if self._delete_monitored_event(mid):
                    results.append(ua.StatusCode())
                elif self._delete_monitored_datachange(mid):
                    results.append(ua.StatusCode())
                    #FIXME add statuschange
                else:
                    results.append(ua.StatusCode(ua.StatusCodes.BadMonitoredItemIdInvalid))
            return results

    def _delete_monitored_event(self, mid):
        with self._lock:
            for k, v in self._monitored_events:
                if v == mid:
                    self._monitored_events.pop(k)
                    #FIXME we may need to remove events in queue, or we do not care ?
                    return True
            return False

    def _delete_monitored_datachange(self, mid):
        with self._lock:
            if mid in self._monitored_datachange:
                self._monitored_datachange.pop(mid)
                return True
            return False

    def datachange_callback(self, handle, value):
        self.logger.info("subscription %s: datachange callback called with %s, %s", self, handle, value)





