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
from opcua.users import User
from opcua import xmlimporter


class SessionState(Enum):
    Created = 0
    Activated = 1
    Closed = 2


class ServerDesc(object):
    def __init__(self, serv, cap=None):
        self.Server = serv
        self.Capabilities = cap


class InternalServer(object):

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.endpoints = []
        self._channel_id_counter = 5
        self.allow_remote_admin = True
        self.disabled_clock = False  # for debugging we may want to disable clock that writes too much in log
        self._known_servers = {}  # used if we are a discovery server

        self.aspace = AddressSpace()
        self.attribute_service = AttributeService(self.aspace)
        self.view_service = ViewService(self.aspace)
        self.method_service = MethodService(self.aspace)
        self.node_mgt_service = NodeManagementService(self.aspace)
        # import address space from code generated from xml
        standard_address_space.fill_address_space(self.node_mgt_service)  
        # import address space from save db to disc
        #standard_address_space.fill_address_space_from_disk(self.aspace)  

        # import address space directly from xml, this has preformance impact so disabled
        #importer = xmlimporter.XmlImporter(self.node_mgt_service)
        #importer.import_xml("/home/olivier/python-opcua/schemas/Opc.Ua.NodeSet2.xml")

        self.loop = utils.ThreadLoop()
        self.subscription_service = SubscriptionService(self.loop, self.aspace)

        # create a session to use on server side
        self.isession = InternalSession(self, self.aspace, self.subscription_service, "Internal", user=User.Admin)
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
        if not self.disabled_clock:
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
        #FIXME: implement filtering from parmams.uri 
        servers = []
        for edp in self.endpoints:
            servers.append(edp.Server)
        return servers + [desc.Server for desc in self._known_servers.values()]

    def register_server(self, server, conf=None):
        appdesc = ua.ApplicationDescription()
        appdesc.ApplicationUri = server.ServerUri
        appdesc.ProductUri = server.ProductUri
        appdesc.ApplicationName = server.ServerNames[0]  # FIXME: select name from client locale
        appdesc.ApplicationType = server.ServerType
        appdesc.GatewayServerUri = server.GatewayServerUri
        appdesc.DiscoveryUrls = server.DiscoveryUrls  # FIXME: select discovery uri using reachability from client network
        self._known_servers[server.ServerUri] = ServerDesc(appdesc, conf)

    def register_server2(self, params):
        return self.register_server(params.Server, params.DiscoveryConfiguration)

    def create_session(self, name, user=User.Anonymous):
        return InternalSession(self, self.aspace, self.subscription_service, name, user=user)


class InternalSession(object):
    _counter = 10
    _auth_counter = 1000

    def __init__(self, internal_server, aspace, submgr, name, user=User.Anonymous):
        self.logger = logging.getLogger(__name__)
        self.iserver = internal_server
        self.aspace = aspace
        self.subscription_service = submgr
        self.name = name
        self.user = user
        self.state = SessionState.Created
        self.session_id = ua.NodeId(self._counter)
        InternalSession._counter += 1
        self.authentication_token = ua.NodeId(self._auth_counter)
        InternalSession._auth_counter += 1
        self.nonce = utils.create_nonce()
        self.subscriptions = []
        #self.logger.debug("Created internal session %s for user %s", self.name, self.user)
        print("Created internal session {} for user {}".format(self.name, self.user))
        self._lock = Lock()

    def __str__(self):
        return "InternalSession(name:{}, user:{}, id:{}, auth_token:{})".format(self.name, self.user, self.session_id, self.authentication_token)

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
            raise utils.ServiceError(ua.StatusCodes.BadSessionIdInvalid)
        result.ServerNonce = self.nonce
        for _ in params.ClientSoftwareCertificates:
            result.Results.append(ua.StatusCode())
        self.state = SessionState.Activated
        id_token = params.UserIdentityToken
        if isinstance(id_token, ua.UserNameIdentityToken):
            if self.iserver.allow_remote_admin and id_token.UserName in ("admin", "Admin"):
                self.user = User.Admin
        return result

    def read(self, params):
        return self.iserver.attribute_service.read(params)

    def write(self, params):
        return self.iserver.attribute_service.write(params, self.user)

    def browse(self, params):
        return self.iserver.view_service.browse(params)

    def translate_browsepaths_to_nodeids(self, params):
        return self.iserver.view_service.translate_browsepaths_to_nodeids(params)

    def add_nodes(self, params):
        return self.iserver.node_mgt_service.add_nodes(params, self.user)

    def add_references(self, params):
        return self.iserver.node_mgt_service.add_references(params, self.user)

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
