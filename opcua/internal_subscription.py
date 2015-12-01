"""
server side implementation of a subscription object
"""

from threading import RLock
import logging
import copy

from opcua import ua


class MonitoredItemData(object):

    def __init__(self):
        self.client_handle = None
        self.callback_handle = None
        self.monitored_item_id = None
        self.parameters = None
        self.mode = None


class MonitoredItemService(object):

    """
    implement monitoreditem service for 1 subscription
    """

    def __init__(self, isub, aspace):
        self.logger = logging.getLogger(__name__ + str(isub.data.SubscriptionId))
        self.isub = isub
        self.aspace = aspace
        self._lock = RLock()
        self._monitored_items = {}
        self._monitored_events = {}
        self._monitored_datachange = {}
        self._monitored_item_counter = 111

    def delete_all_monitored_items(self):
        self.delete_monitored_items([mdata.monitored_item_id for mdata in self._monitored_items.values()])

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
            for mdata in self._monitored_items.values():
                result = ua.MonitoredItemCreateResult()
                if mdata.monitored_item_id == params.MonitoredItemId:
                    result.RevisedSamplingInterval = self.isub.data.RevisedPublishingInterval
                    result.RevisedQueueSize = params.RequestedParameters.QueueSize
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
            result.RevisedSamplingInterval = self.isub.data.RevisedPublishingInterval
            result.RevisedQueueSize = params.RequestedParameters.QueueSize
            result.FilterResult = params.RequestedParameters.Filter
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
                if result.StatusCode.is_good():
                    # force data change event generation
                    self.trigger_datachange(handle, params.ItemToMonitor.NodeId, params.ItemToMonitor.AttributeId)
            
            if not result.StatusCode.is_good():
                del(self._monitored_items[result.MonitoredItemId])
                self._monitored_item_counter -= 1

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
            self.isub.enqueue_datachange_event(mid, event, mdata.parameters.RevisedQueueSize)

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
            mdata = self._monitored_items[mid]
            fieldlist = ua.EventFieldList()
            fieldlist.ClientHandle = mdata.client_handle
            fieldlist.EventFields = self._get_event_fields(mdata.parameters.FilterResult, event)
            self.isub.enqueue_event(mid, fieldlist, mdata.parameters.RevisedQueueSize)
            return True

    def _get_event_fields(self, evfilter, event):
        fields = []
        for sattr in evfilter.SelectClauses:
            try:
                if not sattr.BrowsePath:
                    val = getattr(event, ua.AttributeIdsInv[sattr.Attribute])
                    val = copy.deepcopy(val)
                    fields.append(ua.Variant(val))
                else:
                    name = sattr.BrowsePath[0].Name
                    val = getattr(event, name)
                    val = copy.deepcopy(val)
                    fields.append(ua.Variant(val))
            except AttributeError:
                fields.append(ua.Variant())
        return fields

    def trigger_statuschange(self, code):
        self.isub.enqueue_statuschange(code)


class InternalSubscription(object):

    def __init__(self, subservice, data, addressspace, callback):
        self.logger = logging.getLogger(__name__ + str(data.SubscriptionId))
        self.aspace = addressspace
        self.subservice = subservice
        self.data = data
        self.callback = callback
        self.monitored_item_srv = MonitoredItemService(self, addressspace)
        self.task = None
        self._lock = RLock()
        self._triggered_datachanges = {}
        self._triggered_events = {}
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
        self.monitored_item_srv.delete_all_monitored_items()

    def _subscription_loop(self):
        #self.logger.debug("%s loop", self)
        if not self._stopev:
            self.subservice.loop.call_later(self.data.RevisedPublishingInterval / 1000.0, self._sub_loop)

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
            self.monitored_item_srv.trigger_statuschange(ua.StatusCode(ua.StatusCodes.BadTimeout))
            self._stopev = True
        with self._lock:
            if self.has_published_results():  # FIXME: should we pop a publish request here? or we do not care?
                self._publish_cycles_count += 1
                result = self._pop_publish_result()
                self.callback(result)

    def _pop_publish_result(self):
        result = ua.PublishResult()
        result.SubscriptionId = self.data.SubscriptionId
        self._pop_triggered_datachanges(result)
        self._pop_triggered_events(result)
        self._pop_triggered_statuschanges(result)
        self._keep_alive_count = 0
        self._startup = False
        result.NotificationMessage.SequenceNumber = self._notification_seq
        self._notification_seq += 1
        result.MoreNotifications = False
        result.AvailableSequenceNumbers = list(self._not_acknowledged_results.keys())
        self._not_acknowledged_results[result.NotificationMessage.SequenceNumber] = result
        return result

    def _pop_triggered_datachanges(self, result):
        if self._triggered_datachanges:
            notif = ua.DataChangeNotification()
            notif.MonitoredItems = [item for sublist in self._triggered_datachanges.values() for item in sublist]
            self._triggered_datachanges = {}
            self.logger.debug("sending datachanges notification with %s events", len(notif.MonitoredItems))
            result.NotificationMessage.NotificationData.append(notif)

    def _pop_triggered_events(self, result):
        if self._triggered_events:
            notif = ua.EventNotificationList()
            notif.Events = [item for sublist in self._triggered_events.values() for item in sublist]
            self._triggered_events = {}
            result.NotificationMessage.NotificationData.append(notif)
            self.logger.debug("sending event notification with %s events", len(notif.Events))

    def _pop_triggered_statuschanges(self, result):
        if self._triggered_statuschanges:
            notif = ua.StatusChangeNotification()
            notif.Status = self._triggered_statuschanges.pop(0)
            result.NotificationMessage.NotificationData.append(notif)
            self.logger.debug("sending event notification %s", len(notif.Status))

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

    def enqueue_datachange_event(self, mid, eventdata, maxsize):
        self._enqueue_event(mid, eventdata, maxsize, self._triggered_datachanges)

    def enqueue_event(self, mid, eventdata, maxsize):
        self._enqueue_event(mid, eventdata, maxsize, self._triggered_events)

    def enqueue_statuschange(self, code):
        self._triggered_statuschanges.append(code)

    def _enqueue_event(self, mid, eventdata, size, queue):
        if mid not in queue:
            queue[mid] = [eventdata]
            return
        if size != 0:
            if len(queue[mid]) >= size:
                queue[mid].pop(0)
        queue[mid].append(eventdata)
