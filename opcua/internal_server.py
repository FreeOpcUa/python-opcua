"""
Internal server implementing opcu-ua interface. can be used on server side or to implement binary/https opc-ua servers
"""

from datetime import datetime
import logging
from threading import Timer, Lock
from threading import Condition
from threading import Thread
from enum import Enum
import functools
try:
    #we prefer to use bundles asyncio version, otherwise fallback to trollius
    import asyncio
except ImportError:
    import trollius as asyncio
    from trollius import From


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
from opcua.subscription_server import SubscriptionManager


class ThreadLoop(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.logger = logging.getLogger(__name__)
        self.loop = None
        self._cond = Condition()

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

    def stop(self):
        """
        stop subscription loop, thus the subscription thread
        """
        self.loop.call_soon_threadsafe(self.loop.stop)

    def call_soon(self, callback):
        self.loop.call_soon_threadsafe(callback)

    def call_later(self, delay, callback):
        p = functools.partial(self.loop.call_later, delay, callback)
        self.loop.call_soon_threadsafe(p)


class SessionState(Enum):
    Created = 0
    Activated = 1
    Closed = 2

class InternalServer(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.endpoints = []
        self._channel_id_counter = 5
        self.aspace = AddressSpace()
        self.load_standard_address_space()
        self.loop = ThreadLoop()
        self.submanager = SubscriptionManager(self.loop, self.aspace)
        # create a session to use on server side
        self.isession = InternalSession(self, self.aspace, self.submanager, "Internal") 
        self._timer = None
        self.current_time_node = Node(self.isession, ua.NodeId(ua.ObjectIds.Server_ServerStatus_CurrentTime))
        uries = ["http://opcfoundation.org/UA/"]
        ns_node = Node(self.isession, ua.NodeId(ua.ObjectIds.Server_NamespaceArray))
        ns_node.set_value(uries)

    def load_address_space(self, path):
        self.aspace.load(path)

    def dump_address_space(self, path):
        self.aspace.dump(path)

    def load_standard_address_space(self):
        create_standard_address_space_Part3(self.aspace)
        create_standard_address_space_Part4(self.aspace)
        create_standard_address_space_Part5(self.aspace)
        create_standard_address_space_Part8(self.aspace)
        create_standard_address_space_Part9(self.aspace)
        create_standard_address_space_Part10(self.aspace)
        create_standard_address_space_Part11(self.aspace)
        create_standard_address_space_Part13(self.aspace)

    def start(self): 
        self.logger.info("starting internal server")
        self.loop.start()
        Node(self.isession, ua.NodeId(ua.ObjectIds.Server_ServerStatus_State)).set_value(0)
        Node(self.isession, ua.NodeId(ua.ObjectIds.Server_ServerStatus_StartTime)).set_value(datetime.now())
        self._set_current_time()

    def stop(self):
        self.logger.info("stopping internal server")
        self.loop.stop()

    def _set_current_time(self):
        self.current_time_node.set_value(datetime.now())
        self.loop.call_later(1, self._set_current_time)

    def get_new_channel_id(self):
        self._channel_id_counter += 1
        return self._channel_id_counter

    def add_endpoint(self, endpoint):
        self.endpoints.append(endpoint)

    def get_endpoints(self, params=None):
        self.logger.info("get endpoint")
        #FIXME check params
        return self.endpoints[:]
    
    def create_session(self, name):
        return InternalSession(self, self.aspace, self.submanager, name)

class InternalSession(object):
    _counter = 10
    _auth_counter = 1000
    def __init__(self, internal_server, aspace, submgr, name):
        self.logger = logging.getLogger(__name__)
        self.iserver = internal_server
        self.aspace = aspace
        self.submgr = submgr
        self.name = name
        self.state = SessionState.Created
        self.session_id = ua.NodeId(self._counter)
        InternalSession._counter += 1
        self.authentication_token = ua.NodeId(self._auth_counter)
        InternalSession._auth_counter += 1
        self.nonce = utils.create_nonce() 
        self.subscriptions = []
        self.logger.warning("Created internal session %s", self.name)
        self._lock = Lock()

    def __str__(self):
        return "InternalSession(name:{}, id:{}, auth_token:{})".format(self.name, self.session_id, self.authentication_token)
 
    def get_endpoints(self, params=None):
        return self.iserver.get_endpoints(params)

    def create_session(self, params):
        self.logger.info("Create session request")

        result = ua.CreateSessionResult()
        result.SessionId = self.session_id
        result.AuthenticationToken = self.authentication_token 
        result.RevisedSessionTimeout = params.RequestedSessionTimeout
        result.MaxRequestMessageSize = 65536
        result.ServerNonce = self.nonce
        result.ServerEndpoints = self.get_endpoints()

        return result

    def close_session(self, delete_subs):
        self.logger.info("close session %s with subscriptions %s", self, self.subscriptions)
        self.state = SessionState.Closed
        self.delete_subscriptions(self.subscriptions[:])

    def activate_session(self, params):
        self.logger.info("activate session")
        result = ua.ActivateSessionResult()
        if not self.state == SessionState.Created:
            result.Results = [ua.StatusCode(ua.StatusCodes.BadSessionIdInvalid)]
            return result
        result.ServerNonce = self.nonce
        for _ in params.ClientSoftwareCertificates:
            result.Results.append(ua.StatusCode())
        self.state = SessionState.Activated
        return result

    def read(self, params):
        return self.aspace.read(params)

    def write_user_writable(self, params):
        return self.aspace.write_user_writable(params)

    def write(self, params):
        return self.aspace.write(params)

    def browse(self, params):
        return self.aspace.browse(params)

    def translate_browsepaths_to_nodeids(self, params):
        return self.aspace.translate_browsepaths_to_nodeids(params)

    def add_nodes(self, params):
        return self.aspace.add_nodes(params)

    def add_method_callback(self, methodid, callback):
        return self.aspace.add_method_callback(methodid, callback)

    def call(self, params):
        return self.aspace.call(params)

    def create_subscription(self, params, callback):
        result = self.submgr.create_subscription(params, callback)
        with self._lock:
            self.subscriptions.append(result.SubscriptionId)
        return result

    def create_monitored_items(self, params):
        return self.submgr.create_monitored_items(params)

    def modify_monitored_items(self, params):
        return self.submgr.modify_monitored_items(params)

    def republish(self, params):
        return self.submgr.republish(params)

    def delete_subscriptions(self, ids):
        for i in ids:
            with self._lock:
                if i in self.subscriptions:
                    self.subscriptions.remove(i)
        return self.submgr.delete_subscriptions(ids)

    def delete_monitored_items(self, params):
        return self.submgr.delete_monitored_items(params)
 
    def publish(self, acks=None):
        if acks is None:
            acks = []
        return self.submgr.publish(acks)


