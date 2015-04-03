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
        with self._cond:
            Thread.start(self)
            self._cond.wait()

    def run(self):
        self.logger.debug("Starting subscription thread")
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        with self._cond:
            self._cond.notify_all()
        self.loop.run_forever()
        self.logger.debug("subscription thread ended")

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
        self.logger.info("create subscription with callback: %s", callback)
        result = ua.CreateSubscriptionResult()
        result.RevisedPublishingInterval = params.RequestedPublishingInterval
        result.RevisedLifetimeCount = params.RequestedLifetimeCount
        result.RevisedMaxKeepAliveCount = params.RequestedMaxKeepAliveCount
        with self._lock:
            self._sub_id_counter += 1
            result.SubscriptionId = self._sub_id_counter

            sub = InternalSubscription(self, result, self.aspace, callback)
            sub.start()
            self.subscriptions[result.SubscriptionId] = sub

            return result

    def delete_subscriptions(self, ids):
        self.logger.info("delete subscriptions: %s", ids)
        res = []
        for i in ids:
            with self._lock:
                if not i in self.subscriptions:
                    res.append(ua.StatusCode(ua.StatusCodes.BadSubscriptionIdInvalid))
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

    def modify_monitored_items(self, params):
        self.logger.info("modify monitored items")
        with self._lock:
            if not params.SubscriptionId in self.subscriptions:
                res = []
                for _ in params.ItemsToModify:
                    result = ua.MonitoredItemModifyResult()
                    result.StatusCode = ua.StatusCode(ua.StatusCodes.BadSubscriptionIdInvalid)
                    res.append(result)
                return res
            return self.subscriptions[params.SubscriptionId].modify_monitored_items(params)

    def delete_monitored_items(self, params):
        self.logger.info("delete monitored items")
        with self._lock:
            if not params.SubscriptionId in self.subscriptions:
                res = []
                for _ in params.MonitoredItemIds:
                    res.append(ua.StatusCode(ua.StatusCodes.BadSubscriptionIdInvalid))
                return res
            return self.subscriptions[params.SubscriptionId].delete_monitored_items(params.MonitoredItemIds)



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
        self._triggered_datachanges = []
        self._triggered_events = []
        self._notification_seq = 1
        self._not_acknowledged_results = []
        self._startup = True 
        self._keep_alive_count = 0

    def __str__(self):
        return "Subscription(id:{})".format(self.data.SubscriptionId)

    def start(self):
        self.logger.debug("starting subscription %s", self.data.SubscriptionId)
        self.task = self.manager.add_task(self._subscription_loop())
    
    def stop(self):
        self.logger.debug("stopping subscription %s", self.data.SubscriptionId)
        self.manager.cancel_task(self.task)
        self.delete_all_monitored_items()

    def delete_all_monitored_items(self):
        self.delete_monitored_items([mdata.monitored_item_id for mdata in self._monitored_datachange.values()])

    @asyncio.coroutine
    def _subscription_loop(self):
        self.logger.debug("%s loop running", self)
        while True:
            yield from asyncio.sleep(self.data.RevisedPublishingInterval/1000)
            #test disabled we do not check that one since we do not care about not received results
            #if self._keep_alive_count > self.data.RevisedLifetimeCount:
                #self.logger.warn("Subscription %s has expired, keep alive count(%s) > lifetime count (%s)", self.data.SubscriptionId, self._keep_alive_count, self.data.RevisedLifetimeCount)
                #return
            try:
                self.publish_results()
            except Exception as ex: #we catch everythin since it seems exceptions are lost in loop
                self.logger.exception("Exception in %s loop", self)

    def has_published_results(self):
        with self._lock:
            if self._startup or self._triggered_datachanges or self._triggered_events:
                return True
            if self._keep_alive_count > self.data.RevisedMaxKeepAliveCount:
                self.logger.debug("keep alive count %s is > than max keep alive count %s, sending publish event", self._keep_alive_count, self.data.RevisedMaxKeepAliveCount)
                return True
            self._keep_alive_count += 1
            return False

    def publish_results(self): 
        #self.logger.debug("looking for results and publishing")
        with self._lock:
            if self.has_published_results(): #FIXME: should I pop a publish request here? or I do not care?
                result = self._pop_publish_result()
                self.callback(result)

    def _pop_publish_result(self):
        result = ua.PublishResult()
        result.SubscriptionId = self.data.SubscriptionId
        if self._triggered_datachanges:
            notif = ua.DataChangeNotification()
            notif.MonitoredItems = self._triggered_datachanges[:]
            self._triggered_datachanges.clear() 
            self.logger.debug("sending datachanges nontification with %s events", len(notif.MonitoredItems))
            result.NotificationMessage.NotificationData.append(notif)
        if self._triggered_events:
            notif = ua.EventNotificationList()
            notif.Events = self._triggered_events[:]
            self._triggered_events.clear()
            result.NotificationMessage.NotificationData.append(notif)
        #FIXME: add statuschaneg events
        self._keep_alive_count = 0
        self._startup = False
        result.NotificationMessage.SequenceNumber = self._notification_seq
        self._notification_seq += 1
        result.MoreNotifications = False
        result.AvailableSequenceNumbers = [res.NotificationMessage.SequenceNumber for res in self._not_acknowledged_results]
        self._not_acknowledged_results.append(result)
        return result

    def create_monitored_items(self, params):
        results = []
        for item in params.ItemsToCreate:
            results.append(self._create_monitored_item(item))
        return results

    def modify_monitored_items(self, params):
        results = []
        for item in params.ItemsToModify:
            results.append(self._modify_monitored_item(item))
        return results


    def trigger_datachange(self, handle, nodeid, attr):
        self.logger.debug("triggering datachange for handle %s, nodeid %s, and attribute %s", handle, nodeid, attr)
        variant = self.aspace.get_attribute_value(nodeid, attr)
        self.datachange_callback(handle, variant)

    def _modify_monitored_item(self, params):
        with self._lock:
            for _, mdata in self._monitored_datachange.items():
                result = ua.MonitoredItemCreateResult()
                if mdata.monitored_item_id == params.MonitoredItemId:
                    result.RevisedSamplingInterval = self.data.RevisedPublishingInterval
                    result.RevisedQueueSize = params.RequestedParameters.QueueSize #FIXME check and use value
                    result.FilterResult = params.RequestedParameters.Filter
                    mdata.parameters = result
                    return result
            #FIXME modify event subscriptions
            result = ua.MonitoredItemCreateResult()
            result.StatusCode(ua.StatusCodes.BadMonitoredItemIdInvalid)
            return result

    def _create_monitored_item(self, params):
        with self._lock:
            result = ua.MonitoredItemCreateResult()
            result.RevisedSamplingInterval = self.data.RevisedPublishingInterval
            result.RevisedQueueSize = params.RequestedParameters.QueueSize #FIXME check and use value
            result.FilterResult = params.RequestedParameters.Filter
            self._monitored_item_counter += 1
            result.MonitoredItemId = self._monitored_item_counter
            if params.ItemToMonitor.AttributeId == ua.AttributeIds.EventNotifier:
                self.logger.info("request to subscribe to events for node %s and attribute %s", params.ItemToMonitor.NodeId, params.ItemToMonitor.AttributeId)
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
            self._monitored_datachange[handle] = mdata

            #force event generation
            self.trigger_datachange(handle, params.ItemToMonitor.NodeId, params.ItemToMonitor.AttributeId)

            return result

    def delete_monitored_items(self, ids):
        self.logger.debug("delete monitored items %s", ids)
        with self._lock:
            results = []
            for mid in ids:
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
            for k, v in self._monitored_datachange.items():
                if v.monitored_item_id == mid:
                    self._monitored_datachange.pop(k)
                return True
            return False

    def datachange_callback(self, handle, value):
        self.logger.info("subscription %s: datachange callback called with %s, %s", self, handle, value.Value)
        event = ua.MonitoredItemNotification()
        with self._lock:
            mdata = self._monitored_datachange[handle]
            #event.monitored_item_id = mdata.monitored_item_id
            #event.monitored_item_notification.ClientHandle = mdata.client_handle
            event.ClientHandle = mdata.client_handle
            event.Value = value
            self._triggered_datachanges.append(event)





