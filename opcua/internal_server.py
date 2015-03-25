"""
Internal server to be used on server side
"""
import asyncio
from datetime import datetime
import uuid
import logging
from threading import RLock, Timer, Thread, Condition

from opcua import ua
from opcua import utils
from opcua import Node
from opcua.address_space import AddressSpace
from opcua.standard_address_space_part3 import create_standard_address_space_Part3
from opcua.standard_address_space_part4 import create_standard_address_space_Part4
from opcua.standard_address_space_part5 import create_standard_address_space_Part5
from opcua.standard_address_space_part8 import create_standard_address_space_Part8
from opcua.standard_address_space_part9 import create_standard_address_space_Part9
from opcua.standard_address_space_part10 import create_standard_address_space_Part10
from opcua.standard_address_space_part11 import create_standard_address_space_Part11
from opcua.standard_address_space_part13 import create_standard_address_space_Part13

class Session(object):
    _counter = 10
    _auth_counter = 1000
    def __init__(self):
        self.session_id = ua.NodeId(self._counter)
        Session._counter += 1
        self.authentication_token = ua.NodeId(self._auth_counter)
        Session._auth_counter += 1
        self.nonce = utils.create_nonce() 

    def __str__(self):
        return "InternalSession(id:{}, auth_token:{})".format(self.session_id, self.authentication_token)

class SubscriptionManager(Thread):
    def __init__(self, aspace):
        Thread.__init__(self)
        self.logger = logging.getLogger(__name__)
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

    def add_task(self, coroutine):
        return self.loop.create_task(coroutine)

    def stop(self):
        self.loop.call_soon_threadsafe(self.loop.stop)

    def create_subscription(self, params, callback):
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
        res = []
        for i in ids:
            sub = self.subscriptions.pop(i)
            sub.stop()
            res.append(ua.StatusCode())
        return res

    def publish(self, acks):
        self.logger.warn("publish request with acks %s", acks)

    def create_monitored_items(self, params):
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
        self.logger = logging.getLogger(__name__)
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




  



class InternalServer(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.endpoints = []
        self.sessions = {}
        self._channel_id_counter = 5
        self.aspace = AddressSpace()
        create_standard_address_space_Part3(self.aspace)
        create_standard_address_space_Part4(self.aspace)
        create_standard_address_space_Part5(self.aspace)
        create_standard_address_space_Part8(self.aspace)
        create_standard_address_space_Part9(self.aspace)
        create_standard_address_space_Part10(self.aspace)
        create_standard_address_space_Part11(self.aspace)
        create_standard_address_space_Part13(self.aspace)
        self.channels = {}
        self._lock = RLock()
        #set some node values expected by some clients
        self.current_time_node = Node(self, ua.NodeId(ua.ObjectIds.Server_ServerStatus_CurrentTime))
        self._stopev = False
        self.submanager = SubscriptionManager(self.aspace)
        self._timer = None

    def start(self): 
        Node(self, ua.NodeId(ua.ObjectIds.Server_ServerStatus_State)).set_value(0)
        Node(self, ua.NodeId(ua.ObjectIds.Server_ServerStatus_StartTime)).set_value(datetime.now())
        # set time every seconds, maybe we should disable it for performance reason??
        self._set_current_time()
        self.submanager.start()

    def stop(self):
        self.submanager.stop()
        self._stopev = True

    def _set_current_time(self):
        if self._stopev:
            return
        self.current_time_node.set_value(datetime.now())
        self._timer = Timer(1, self._set_current_time)
        self._timer.start()

    def open_secure_channel(self, params, currentchannel=None):
        self.logger.info("open secure channel")
        with self._lock:
            if params.RequestType == ua.SecurityTokenRequestType.Issue:
                channel = ua.OpenSecureChannelResult()
                channel.SecurityToken.TokenId = 13 #random value
                channel.SecurityToken.ChannelId = self._channel_id_counter
                channel.SecurityToken.RevisedLifetime = params.RequestedLifetime 
                self._channel_id_counter += 1
            else:
                channel = self.channels[currentchannel.SecurityToken.ChannelId]
            channel.SecurityToken.TokenId += 1
            channel.SecurityToken.CreatedAt = datetime.now()
            channel.SecurityToken.RevisedLifetime = params.RequestedLifetime
            channel.ServerNonce = uuid.uuid4().bytes + uuid.uuid4().bytes
            self.channels[channel.SecurityToken.ChannelId] = channel
            return channel

    def add_endpoint(self, endpoint):
        with self._lock:
            self.endpoints.append(endpoint)

    def get_endpoints(self, params=None):
        #FIXME check params
        with self._lock:
            return self.endpoints[:]

    def create_session(self, params):
        self.logger.info("create session")
        with self._lock:
            session = Session()
            self.sessions[session.session_id] = session
            self.logger.info("Create session request, created session: %s", session)

            result = ua.CreateSessionResult()
            result.SessionId = session.session_id
            result.AuthenticationToken = session.authentication_token 
            result.RevisedSessionTimeout = params.RequestedSessionTimeout
            result.MaxRequestMessageSize = 65536
            result.ServerNonce = session.nonce
            result.ServerEndpoints = self.endpoints[:]

            return result

    def close_session(self, session, delete_subs):
        self.logger.info("close session")
        with self._lock:
            if not session.SessionId in self.sessions:
                self.logger.warn("session id %s is invalid: available sessions are %s", session.SessionId, self.sessions)
                return
            self.sessions.pop(session.SessionId)

    def activate_session(self, session, params):
        self.logger.info("activate session")
        with self._lock:
            result = ua.ActivateSessionResult()
            if not session:
                result.Results = [ua.StatusCode(ua.StatusCodes.BadSessionIdInvalid)]
                return result
            result.ServerNonce = self.sessions[session.SessionId].nonce
            for _ in params.ClientSoftwareCertificates:
                result.Results.append(ua.StatusCode())
            return result

    def read(self, params):
        return self.aspace.read(params)

    def write(self, params):
        return self.aspace.write(params)

    def browse(self, params):
        return self.aspace.browse(params)

    def translate_browsepaths_to_nodeids(self, params):
        return self.aspace.translate_browsepaths_to_nodeids(params)

    def add_nodes(self, params):
        return self.aspace.add_nodes(params)

    def create_subscription(self, params, callback):
        return self.submanager.create_subscription(params, callback)

    def create_monitored_items(self, params):
        return self.submanager.create_monitored_items(params)

    def publish(self, acks=None):
        if acks is None:
            acks = []
        return self.submanager.publish(acks)


