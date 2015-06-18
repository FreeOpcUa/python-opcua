"""
Internal server implementing opcu-ua interface. can be used on server side or to implement binary/https opc-ua servers
"""

from datetime import datetime
from copy import copy
import logging
from threading import Lock
from enum import Enum
try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse


from opcua import ua
from opcua import utils
from opcua import Node
from opcua.address_space import AddressSpace
from opcua.address_space import AttributeService
from opcua.address_space import ViewService
from opcua.address_space import NodeManagementService
from opcua.address_space import MethodService
from opcua.subscription_service import SubscriptionService
from opcua import standard_address_space

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
        self.attribute_service = AttributeService(self.aspace)
        self.view_service = ViewService(self.aspace)
        self.method_service = MethodService(self.aspace)
        self.node_mgt_service = NodeManagementService(self.aspace)
        standard_address_space.fill_address_space(self.node_mgt_service)
        #standard_address_space.fill_address_space_from_disk(self.aspace)

        self.loop = utils.ThreadLoop()
        self.subcsription_service = SubscriptionService(self.loop, self.aspace)

        # create a session to use on server side
        self.isession = InternalSession(self, self.aspace, self.subcsription_service, "Internal")
        self._timer = None
        self.current_time_node = Node(self.isession, ua.NodeId(ua.ObjectIds.Server_ServerStatus_CurrentTime))
        uries = ["http://opcfoundation.org/UA/"]
        ns_node = Node(self.isession, ua.NodeId(ua.ObjectIds.Server_NamespaceArray))
        ns_node.set_value(uries)

    def load_address_space(self, path):
        self.aspace.load(path)

    def dump_address_space(self, path):
        self.aspace.dump(path)

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

    def get_endpoints(self, params=None, sockname=None):
        self.logger.info("get endpoint")
        if sockname:
            #return to client the ip address it has access to
            edps = []
            for edp in self.endpoints:
                edp1 = copy(edp)
                url = urlparse(edp1.EndpointUrl)
                url = url._replace(netloc=sockname[0] + ":" + str(sockname[1]))
                edp1.EndpointUrl = url.geturl()
                edps.append(edp1)
                return edps
        return self.endpoints[:]

    def find_servers(self, params):
        #FIXME: implement correctly
        servers = []
        for edp in self.endpoints:
            servers.append(edp.Server)
        return servers
        

    def create_session(self, name):
        return InternalSession(self, self.aspace, self.subcsription_service, name)


class InternalSession(object):
    _counter = 10
    _auth_counter = 1000

    def __init__(self, internal_server, aspace, submgr, name):
        self.logger = logging.getLogger(__name__)
        self.iserver = internal_server
        self.aspace = aspace
        self.subscription_service = submgr
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

    def get_endpoints(self, params=None, sockname=None):
        return self.iserver.get_endpoints(params, sockname)

    def create_session(self, params, sockname=None):
        self.logger.info("Create session request")

        result = ua.CreateSessionResult()
        result.SessionId = self.session_id
        result.AuthenticationToken = self.authentication_token
        result.RevisedSessionTimeout = params.RequestedSessionTimeout
        result.MaxRequestMessageSize = 65536
        result.ServerNonce = self.nonce
        result.ServerEndpoints = self.get_endpoints(sockname=sockname)

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
        return self.iserver.attribute_service.read(params)

    def write(self, params):
        return self.iserver.attribute_service.write(params)

    def browse(self, params):
        return self.iserver.view_service.browse(params)

    def translate_browsepaths_to_nodeids(self, params):
        return self.iserver.view_service.translate_browsepaths_to_nodeids(params)

    def add_nodes(self, params):
        return self.iserver.node_mgt_service.add_nodes(params)

    def add_method_callback(self, methodid, callback):
        return self.aspace.add_method_callback(methodid, callback)

    def call(self, params):
        return self.iserver.method_service.call(params)

    def create_subscription(self, params, callback):
        result = self.subscription_service.create_subscription(params, callback)
        with self._lock:
            self.subscriptions.append(result.SubscriptionId)
        return result

    def create_monitored_items(self, params):
        return self.subscription_service.create_monitored_items(params)

    def modify_monitored_items(self, params):
        return self.subscription_service.modify_monitored_items(params)

    def republish(self, params):
        return self.subscription_service.republish(params)

    def delete_subscriptions(self, ids):
        for i in ids:
            with self._lock:
                if i in self.subscriptions:
                    self.subscriptions.remove(i)
        return self.subscription_service.delete_subscriptions(ids)

    def delete_monitored_items(self, params):
        return self.subscription_service.delete_monitored_items(params)

    def publish(self, acks=None):
        if acks is None:
            acks = []
        return self.subscription_service.publish(acks)
