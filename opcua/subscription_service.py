"""
server side implementation of subscriptions
"""
import time
import sys
from threading import RLock
import logging

from opcua import ua


class SubscriptionService(object):

    def __init__(self, loop, aspace):
        self.logger = logging.getLogger(__name__)
        self.loop = loop
        self.aspace = aspace
        self.subscriptions = {}
        self._sub_id_counter = 77
        self._lock = RLock()

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
        for ack in acks:
            with self._lock:
                if ack.SubscriptionId in self.subscriptions:
                    self.subscriptions[ack.SubscriptionId].publish(ack.SequenceNumber)
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

    def republish(self, params):
        with self._lock:
            if not params.SubscriptionId in self.subscriptions:
                # what should I do?
                return ua.NotificationMessage()
            return self.subscriptions[params.SubscriptionId].republish(params.RetransmitSequenceNumber)

    def trigger_event(self, event):
        with self._lock:
            for sub in self.subscriptions.values():
                sub.trigger_event(event)


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
        self._monitored_items = {}
        self._lock = RLock()
        self._triggered_datachanges = []
        self._triggered_events = []
        self._triggered_statuschanges = []
        self._notification_seq = 1
        self._not_acknowledged_results = {}
        self._startup = True
        self._keep_alive_count = 0
        self._publish_cycles_count = 0
        self._stopev = False

    def __str__(self):
        return "Subscription(id:{})".format(self.data.SubscriptionId)

    def start(self):
        self.logger.debug("starting subscription %s", self.data.SubscriptionId)
        self._subscription_loop()

    def stop(self):
        self.logger.debug("stopping subscription %s", self.data.SubscriptionId)
        self._stopev = True
        self.delete_all_monitored_items()

    def delete_all_monitored_items(self):
        self.delete_monitored_items([mdata.monitored_item_id for mdata in self._monitored_items.values()])

    def _subscription_loop(self):
        #self.logger.debug("%s loop", self)
        if not self._stopev:
            self.manager.loop.call_later(self.data.RevisedPublishingInterval / 1000.0, self._sub_loop)

    def _sub_loop(self):
        self.publish_results()
        self._subscription_loop()

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
        if self._publish_cycles_count > self.data.RevisedLifetimeCount:
            self.logger.warning("Subscription %s has expired, publish cycle count(%s) > lifetime count (%s)", self, self._publish_cycles_count, self.data.RevisedLifetimeCount)
            # FIXME this will never be send since we do not have publish request anyway
            self.trigger_statuschange(ua.StatusCode(ua.StatusCodes.BadTimeout))
            self._stopev = True
        with self._lock:
            if self.has_published_results():  # FIXME: should we pop a publish request here? or we do not care?
                self._publish_cycles_count += 1
                result = self._pop_publish_result()
                self.callback(result)

    def _pop_publish_result(self):
        result = ua.PublishResult()
        result.SubscriptionId = self.data.SubscriptionId
        if self._triggered_datachanges:
            notif = ua.DataChangeNotification()
            notif.MonitoredItems = self._triggered_datachanges[:]
            self._triggered_datachanges = []
            self.logger.debug("sending datachanges nontification with %s events", len(notif.MonitoredItems))
            result.NotificationMessage.NotificationData.append(notif)
        if self._triggered_events:
            notif = ua.EventNotificationList()
            notif.Events = self._triggered_events[:]
            self._triggered_events = []
            result.NotificationMessage.NotificationData.append(notif)
        if self._triggered_statuschanges:
            notif = ua.StatusChangeNotification()
            notif.Status = self._triggered_statuschanges.pop(0)
            result.NotificationMessage.NotificationData.append(notif)
        self._keep_alive_count = 0
        self._startup = False
        result.NotificationMessage.SequenceNumber = self._notification_seq
        self._notification_seq += 1
        result.MoreNotifications = False
        result.AvailableSequenceNumbers = list(self._not_acknowledged_results.keys())
        self._not_acknowledged_results[result.NotificationMessage.SequenceNumber] = result
        return result

    def trigger_statuschange(self, code):
        self._triggered_statuschanges.append(code)

    def publish(self, nb):
        with self._lock:
            self._publish_cycles_count = 0
            if nb in self._not_acknowledged_results:
                self._not_acknowledged_results.pop(nb)

    def republish(self, nb):
        self.logger.info("re-publish request for ack %s in subscription %s", nb, self)
        with self._lock:
            if nb in self._not_acknowledged_results:
                self.logger.info("re-publishing ack %s in subscription %s", nb, self)
                return self._not_acknowledged_results[nb].NotificationMessage
            else:
                self.logger.info("Error request to re-published non existing ack %s in subscription %s", nb, self)
                return ua.NotificationMessage()

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
            for _, mdata in self._monitored_items.items():
                result = ua.MonitoredItemCreateResult()
                if mdata.monitored_item_id == params.MonitoredItemId:
                    result.RevisedSamplingInterval = self.data.RevisedPublishingInterval
                    result.RevisedQueueSize = ua.downcast_extobject(params.RequestedParameters.QueueSize)  # FIXME check and use value
                    result.FilterResult = params.RequestedParameters.Filter
                    mdata.parameters = result
                    return result
            # FIXME modify event subscriptions
            result = ua.MonitoredItemCreateResult()
            result.StatusCode(ua.StatusCodes.BadMonitoredItemIdInvalid)
            return result

    def _create_monitored_item(self, params):
        with self._lock:
            result = ua.MonitoredItemCreateResult()
            result.RevisedSamplingInterval = self.data.RevisedPublishingInterval
            result.RevisedQueueSize = params.RequestedParameters.QueueSize  # FIXME check and use value
            result.FilterResult = ua.downcast_extobject(params.RequestedParameters.Filter)
            self._monitored_item_counter += 1
            result.MonitoredItemId = self._monitored_item_counter
            self.logger.debug("Creating MonitoredItem with id %s", result.MonitoredItemId)

            mdata = MonitoredItemData()
            mdata.parameters = result
            mdata.mode = params.MonitoringMode
            mdata.client_handle = params.RequestedParameters.ClientHandle
            mdata.monitored_item_id = result.MonitoredItemId

            self._monitored_items[result.MonitoredItemId] = mdata

            if params.ItemToMonitor.AttributeId == ua.AttributeIds.EventNotifier:
                self.logger.info("request to subscribe to events for node %s and attribute %s", params.ItemToMonitor.NodeId, params.ItemToMonitor.AttributeId)
                self._monitored_events[params.ItemToMonitor.NodeId] = result.MonitoredItemId
            else:
                self.logger.info("request to subscribe to datachange for node %s and attribute %s", params.ItemToMonitor.NodeId, params.ItemToMonitor.AttributeId)
                result.StatusCode, handle = self.aspace.add_datachange_callback(params.ItemToMonitor.NodeId, params.ItemToMonitor.AttributeId, self.datachange_callback)
                self.logger.debug("adding callback return status %s and handle %s", result.StatusCode, handle)
                mdata.callback_handle = handle
                self._monitored_datachange[handle] = result.MonitoredItemId
                # force data change event generation
                self.trigger_datachange(handle, params.ItemToMonitor.NodeId, params.ItemToMonitor.AttributeId)

            return result

    def delete_monitored_items(self, ids):
        self.logger.debug("delete monitored items %s", ids)
        with self._lock:
            results = []
            for mid in ids:
                results.append(self._delete_monitored_items(mid))
            return results

    def _delete_monitored_items(self, mid):
        if not mid in self._monitored_items:
            return ua.StatusCode(ua.StatusCodes.BadMonitoredItemIdInvalid)
        for k, v in self._monitored_events.items():
            if v == mid:
                self._monitored_events.pop(k)
                break
        for k, v in self._monitored_datachange.items():
            if v == mid:
                self.aspace.delete_datachange_callback(k)
                self._monitored_datachange.pop(k)
                break
        self._monitored_items.pop(mid)
        return ua.StatusCode()

    def datachange_callback(self, handle, value):
        self.logger.info("subscription %s: datachange callback called with handle '%s' and value '%s'", self, handle, value.Value)
        event = ua.MonitoredItemNotification()
        with self._lock:
            mid = self._monitored_datachange[handle]
            mdata = self._monitored_items[mid]
            event.ClientHandle = mdata.client_handle
            event.Value = value
            self._triggered_datachanges.append(event)

    def trigger_event(self, event):
        with self._lock:
            if not event.SourceNode in self._monitored_events:
                self.logger.debug("%s has no subscription for events %s from node: %s", self, event, event.SourceNode)
                return False
            self.logger.debug("%s has subscription for events %s from node: %s", self, event, event.SourceNode)
            mid = self._monitored_events[event.SourceNode]
            if not mid in self._monitored_items:
                self.logger.debug("Could not find monitored items for id %s for event %s in subscription %s", mid, event, self)
                return False
            item = self._monitored_items[mid]
            fieldlist = ua.EventFieldList()
            fieldlist.ClientHandle = item.client_handle
            fieldlist.EventFields = self._get_event_fields(item.parameters.FilterResult, event)
            self._triggered_events.append(fieldlist)
            return True

    def _get_event_fields(self, evfilter, event):
        fields = []
        for sattr in evfilter.SelectClauses:
            try:
                if not sattr.BrowsePath:
                    val = getattr(event, ua.AttributeIdsInv[sattr.Attribute])
                    fields.append(ua.Variant(val))
                else:
                    name = sattr.BrowsePath[0].Name
                    val = getattr(event, name)
                    fields.append(ua.Variant(val))
            except AttributeError:
                fields.append(ua.Variant())
        return fields
