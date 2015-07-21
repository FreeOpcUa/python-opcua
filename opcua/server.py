"""
High level interface to pure python OPC-UA server
"""

import logging
try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse


from opcua import ua
#from opcua.binary_server import BinaryServer
from opcua.binary_server_asyncio import BinaryServer
from opcua.internal_server import InternalServer
from opcua import Node, Subscription, ObjectIds, Event


class Server(object):

    """
    High level Server class
    Create an opcua server with default values
    The class is very short. Users are adviced to read the code.
    Create your own namespace and then populate your server address space 
    using use the get_root() or get_objects() to get Node objects.
    and get_event_object() to fire events.
    Then start server. See example_server.py
    All methods are threadsafe


    :ivar server_uri: 
    :vartype server_uri: uri 
    :ivar product_uri: 
    :vartype product_uri: uri 
    :ivar name: 
    :vartype name: string 
    :ivar default_timeout: timout in milliseconds for sessions and secure channel
    :vartype default_timeout: int 
    :ivar iserver: internal server object 
    :vartype default_timeout: InternalServer 
    :ivar bserver: binary protocol server 
    :vartype bserver: BinaryServer 

    """

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.endpoint = "opc.tcp://localhost:4841/freeopcua/server/"
        self.server_uri = "urn:freeopcua:python:server"
        self.product_uri = "urn:freeopcua.github.no:python:server"
        self.name = "FreeOpcUa Python Server"
        self.default_timeout = 3600000
        self.iserver = InternalServer()
        self.bserver = None

        # setup some expected values
        self.register_namespace(self.server_uri)
        sa_node = self.get_node(ua.NodeId(ua.ObjectIds.Server_ServerArray))
        sa_node.set_value([self.server_uri])

    def allow_remote_admin(self, allow):
        """
        Enable or disable the builtin Admin user from network clients
        """
        self.iserver.allow_remote_admin = allow

    def set_endpoint(self, url):
        self.endpoint = urlparse(url)

    def get_endpoints(self):
        return self.iserver.get_endpoints()

    def _setup_server_nodes(self):
        # to be called just before starting server since it needs all parameters to be setup
        self._set_endpoints()

    def _set_endpoints(self):
        idtoken = ua.UserTokenPolicy()
        idtoken.PolicyId = 'anonymous'
        idtoken.TokenType = ua.UserTokenType.Anonymous

        appdesc = ua.ApplicationDescription()
        appdesc.ApplicationName = ua.LocalizedText(self.name)
        appdesc.ApplicationUri = self.server_uri
        appdesc.ApplicationType = ua.ApplicationType.Server
        appdesc.ProductUri = self.product_uri
        appdesc.DiscoveryUrls.append(self.endpoint.geturl())

        edp = ua.EndpointDescription()
        edp.EndpointUrl = self.endpoint.geturl()
        edp.Server = appdesc
        edp.SecurityMode = ua.MessageSecurityMode.None_
        edp.SecurityPolicyUri = 'http://opcfoundation.org/UA/SecurityPolicy#None'
        edp.UserIdentityTokens = [idtoken]
        edp.TransportProfileUri = 'http://opcfoundation.org/UA-Profile/Transport/uatcp-uasc-uabinary'
        edp.SecurityLevel = 0

        self.iserver.add_endpoint(edp)

    def set_server_name(self, name):
        self.name = name

    def start(self):
        """
        Start to listen on network 
        """
        self.iserver.start()
        self._setup_server_nodes()
        self.bserver = BinaryServer(self.iserver, self.endpoint.hostname, self.endpoint.port)
        self.bserver.start()

    def stop(self):
        """
        Stop server  
        """
        self.bserver.stop()
        self.iserver.stop()

    def get_root_node(self):
        """
        Get Root node of server. Returns a Node object.
        """
        return self.get_node(ua.TwoByteNodeId(ObjectIds.RootFolder))

    def get_objects_node(self):
        """
        Get Objects node of server. Returns a Node object.
        """
        return self.get_node(ua.TwoByteNodeId(ObjectIds.ObjectsFolder))

    def get_server_node(self):
        """
        Get Server node of server. Returns a Node object.
        """
        return self.get_node(ua.TwoByteNodeId(ObjectIds.Server))

    def get_node(self, nodeid):
        """
        Get a specific node using NodeId object or a string representing a NodeId
        """
        return Node(self.iserver.isession, nodeid)

    def create_subscription(self, period, handler):
        """
        Create a subscription.
        returns a Subscription object which allow
        to subscribe to events or data on server
        """
        params = ua.CreateSubscriptionParameters()
        params.RequestedPublishingInterval = period
        params.RequestedLifetimeCount = 3000
        params.RequestedMaxKeepAliveCount = 10000
        params.MaxNotificationsPerPublish = 0
        params.PublishingEnabled = True
        params.Priority = 0
        return Subscription(self.iserver.isession, params, handler)

    def get_namespace_array(self):
        """
        get all namespace defined in server
        """
        ns_node = self.get_node(ua.NodeId(ua.ObjectIds.Server_NamespaceArray))
        return ns_node.get_value()

    def register_namespace(self, uri):
        """
        Register a new namespace. Nodes should in custom namespace, not 0.
        """
        ns_node = self.get_node(ua.NodeId(ua.ObjectIds.Server_NamespaceArray))
        uries = ns_node.get_value()
        uries.append(uri)
        ns_node.set_value(uries)
        return (len(uries) - 1)

    def get_namespace_index(self, uri):
        """
        get index of a namespace using its uri
        """
        uries = self.get_namespace_array()
        return uries.index(uri)

    def get_event_object(self, etype=ObjectIds.BaseEventType, source=ObjectIds.Server):
        """
        Returns an event object using an event type from address space.
        Use this object to fire events
        """
        return Event(self.iserver.isession, etype, source)
