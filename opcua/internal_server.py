"""
Internal server implementing opcu-ua interface. can be used on server side or to implement binary/https opc-ua servers
"""

from datetime import datetime
import uuid
import logging
from threading import Timer
from enum import Enum

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
 
class SessionState(Enum):
    Init = 0
    Created = 1
    Activated = 2
    Closed = 3

class InternalServer(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.endpoints = []
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
        self.submanager = SubscriptionManager(self.aspace)
        self.isession = InternalSession(self, self.aspace, self.submanager, "Internal") #used internaly
        self._stopev = False
        self._timer = None
        self.current_time_node = Node(self.isession, ua.NodeId(ua.ObjectIds.Server_ServerStatus_CurrentTime))

    def start(self): 
        self.logger.info("starting internal server")
        Node(self.isession, ua.NodeId(ua.ObjectIds.Server_ServerStatus_State)).set_value(0)
        Node(self.isession, ua.NodeId(ua.ObjectIds.Server_ServerStatus_StartTime)).set_value(datetime.now())
        # set time every seconds, seems to be expected by some clients, maybe we should disable it for performance reason??
        self._set_current_time()
        self.submanager.start()

    def stop(self):
        self.logger.info("stopping internal server")
        self.submanager.stop()
        self._stopev = True

    def _set_current_time(self):
        if self._stopev:
            return
        self.current_time_node.set_value(datetime.now())
        self._timer = Timer(1, self._set_current_time)
        self._timer.start()

    def create_session(self, name):
        return InternalSession(self, self.aspace, self.submanager, name)
    
    def get_new_channel_id(self):
        self._channel_id_counter += 1
        return self._channel_id_counter

    def add_endpoint(self, endpoint):
        self.endpoints.append(endpoint)

    def get_endpoints(self, params=None):
        self.logger.info("get endpoint")
        #FIXME check params
        return self.endpoints[:]


class InternalSession(object):
    _counter = 10
    _auth_counter = 1000
    def __init__(self, internal_server, aspace, submgr, name):
        self.logger = logging.getLogger(__name__)
        self.iserver = internal_server
        self.aspace = aspace
        self.submgr = submgr
        self.name = name
        self.state = SessionState.Init
        self.session_id = ua.NodeId(self._counter)
        InternalSession._counter += 1
        self.authentication_token = ua.NodeId(self._auth_counter)
        InternalSession._auth_counter += 1
        self.nonce = utils.create_nonce() 
        self.subscriptions = []
        self.channel = None
        self.logger.warning("Created internal session %s", self.name)

    def __str__(self):
        return "InternalSession(name:{}, id:{}, auth_token:{})".format(self.name, self.session_id, self.authentication_token)
 
    def open_secure_channel(self, params):
        self.logger.info("open secure channel")
        if params.RequestType == ua.SecurityTokenRequestType.Issue:
            self.channel = ua.OpenSecureChannelResult()
            self.channel.SecurityToken.TokenId = 13 #random value
            self.channel.SecurityToken.ChannelId = self.iserver.get_new_channel_id()
            self.channel.SecurityToken.RevisedLifetime = params.RequestedLifetime 
        self.channel.SecurityToken.TokenId += 1
        self.channel.SecurityToken.CreatedAt = datetime.now()
        self.channel.SecurityToken.RevisedLifetime = params.RequestedLifetime
        self.channel.ServerNonce = uuid.uuid4().bytes + uuid.uuid4().bytes
        return self.channel

    def get_endpoints(self, params=None):
        return self.iserver.get_endpoints(params)

    def create_session(self, params):
        self.logger.info("create session")
        self.logger.info("Create session request, created session: %s", self.session_id)

        result = ua.CreateSessionResult()
        result.SessionId = self.session_id
        result.AuthenticationToken = self.authentication_token 
        result.RevisedSessionTimeout = params.RequestedSessionTimeout
        result.MaxRequestMessageSize = 65536
        result.ServerNonce = self.nonce
        result.ServerEndpoints = self.get_endpoints()

        self.state = SessionState.Created

        return result

    def close_session(self, delete_subs):
        self.logger.info("close session")
        self.state = SessionState.Closed
        self.delete_subscriptions(self.subscriptions)

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

    def write(self, params):
        return self.aspace.write(params)

    def browse(self, params):
        return self.aspace.browse(params)

    def translate_browsepaths_to_nodeids(self, params):
        return self.aspace.translate_browsepaths_to_nodeids(params)

    def add_nodes(self, params):
        return self.aspace.add_nodes(params)

    def create_subscription(self, params, callback):
        result = self.submgr.create_subscription(params, callback)
        self.subscriptions.append(result.SubscriptionId)
        return result

    def create_monitored_items(self, params):
        return self.submgr.create_monitored_items(params)

    def delete_subscriptions(self, ids):
        for i in ids:
            self.subscriptions.remove(i)
        return self.submgr.delete_subscriptions(ids)

    def delete_monitored_items(self, params):
        return self.submgr.delete_monitored_items(params)
 
    def publish(self, acks=None):
        if acks is None:
            acks = []
        return self.submgr.publish(acks)


