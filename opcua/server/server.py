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
from opcua.server.binary_server_asyncio import BinaryServer
from opcua.server.internal_server import InternalServer
from opcua.common.node import Node
from opcua.common.event import Event
from opcua.common.subscription import Subscription
from opcua.common import xmlimporter
from opcua.common.manage_nodes import delete_nodes
from opcua.client.client import Client
from opcua.crypto import security_policies
use_crypto = True
try:
    from opcua.crypto import uacrypto
except ImportError:
    print("cryptography is not installed, use of crypto disabled")
    use_crypto = False


class Server(object):

    """
    High level Server class

    This class creates an opcua server with default values

    Create your own namespace and then populate your server address space
    using use the get_root() or get_objects() to get Node objects.
    and get_event_object() to fire events.
    Then start server. See example_server.py
    All methods are threadsafe

    If you need more flexibility you call directly the Ua Service methods
    on the iserver  or iserver.isesssion object members.


    :ivar application_uri:
    :vartype application_uri: uri
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
        self.endpoint = urlparse("opc.tcp://0.0.0.0:4840/freeopcua/server/")
        self.application_uri = "urn:freeopcua:python:server"
        self.product_uri = "urn:freeopcua.github.no:python:server"
        self.name = "FreeOpcUa Python Server"
        self.application_type = ua.ApplicationType.ClientAndServer
        self.default_timeout = 3600000
        self.iserver = InternalServer()
        self.bserver = None
        self._discovery_clients = {}
        self._discovery_period = 60
        self.certificate = None
        self.private_key = None
        self._policies = []

        # setup some expected values
        self.register_namespace(self.application_uri)
        sa_node = self.get_node(ua.NodeId(ua.ObjectIds.Server_ServerArray))
        sa_node.set_value([self.application_uri])

    def load_certificate(self, path):
        """
        load server certificate from file, either pem or der
        """
        self.certificate = uacrypto.load_certificate(path)

    def load_private_key(self, path):
        self.private_key = uacrypto.load_private_key(path)

    def disable_clock(self, val=True):
        """
        for debugging you may want to disable clock that write every second
        to address space
        """
        self.iserver.disabled_clock = val

    def set_application_uri(self, uri):
        """
        Set application/server URI.
        This uri is supposed to be unique. If you intent to register
        your server to a discovery server, it really should be unique in
        your system!
        default is : "urn:freeopcua:python:server"
        """
        self.application_uri = uri

    def find_servers(self, uris=None):
        """
        find_servers. mainly implemented for simmetry with client
        """
        if uris is None:
            uris = []
        params = ua.FindServersParameters()
        params.EndpointUrl = self.endpoint.geturl()
        params.ServerUris = uris
        return self.iserver.find_servers(params)

    def register_to_discovery(self, url="opc.tcp://localhost:4840", period=60):
        """
        Register to an OPC-UA Discovery server. Registering must be renewed at
        least every 10 minutes, so this method will use our asyncio thread to
        re-register every period seconds
        if period is 0 registration is not automatically renewed
        """
        # FIXME: habe a period per discovery
        if url in self._discovery_clients:
            self._discovery_clients[url].disconnect()
        self._discovery_clients[url] = Client(url)
        self._discovery_clients[url].connect()
        self._discovery_clients[url].register_server(self)
        self._discovery_period = period
        if period:
            self.iserver.loop.call_soon(self._renew_registration)

    def unregister_to_discovery(self, url="opc.tcp://localhost:4840"):
        """
        stop registration thread
        """
        # FIXME: is there really no way to deregister?
        self._discovery_clients[url].disconnect()

    def _renew_registration(self):
        for client in self._discovery_clients.values():
            client.register_server(self)
            self.iserver.loop.call_later(self._discovery_period, self._renew_registration)

    def get_client_to_discovery(self, url="opc.tcp://localhost:4840"):
        """
        Create a client to discovery server and return it
        """
        client = Client(url)
        client.connect()
        return client

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
        self._policies = [ua.SecurityPolicyFactory()]
        if self.certificate and self.private_key:
            self._set_endpoints(security_policies.SecurityPolicyBasic128Rsa15,
                                ua.MessageSecurityMode.SignAndEncrypt)
            self._policies.append(ua.SecurityPolicyFactory(security_policies.SecurityPolicyBasic128Rsa15,
                                                           ua.MessageSecurityMode.SignAndEncrypt,
                                                           self.certificate,
                                                           self.private_key)
                                 )
            self._set_endpoints(security_policies.SecurityPolicyBasic128Rsa15,
                                ua.MessageSecurityMode.Sign)
            self._policies.append(ua.SecurityPolicyFactory(security_policies.SecurityPolicyBasic128Rsa15,
                                                           ua.MessageSecurityMode.Sign,
                                                           self.certificate,
                                                           self.private_key)
                                 )
            self._set_endpoints(security_policies.SecurityPolicyBasic256,
                                ua.MessageSecurityMode.SignAndEncrypt)
            self._policies.append(ua.SecurityPolicyFactory(security_policies.SecurityPolicyBasic256,
                                                           ua.MessageSecurityMode.SignAndEncrypt,
                                                           self.certificate,
                                                           self.private_key)
                                 )
            self._set_endpoints(security_policies.SecurityPolicyBasic256,
                                ua.MessageSecurityMode.Sign)
            self._policies.append(ua.SecurityPolicyFactory(security_policies.SecurityPolicyBasic256,
                                                           ua.MessageSecurityMode.Sign,
                                                           self.certificate,
                                                           self.private_key)
                                 )

    def _set_endpoints(self, policy=ua.SecurityPolicy, mode=ua.MessageSecurityMode.None_):
        idtoken = ua.UserTokenPolicy()
        idtoken.PolicyId = 'anonymous'
        idtoken.TokenType = ua.UserTokenType.Anonymous

        idtoken2 = ua.UserTokenPolicy()
        idtoken2.PolicyId = 'certificate_basic256'
        idtoken2.TokenType = ua.UserTokenType.Certificate

        idtoken3 = ua.UserTokenPolicy()
        idtoken3.PolicyId = 'certificate_basic128'
        idtoken3.TokenType = ua.UserTokenType.Certificate

        idtoken4 = ua.UserTokenPolicy()
        idtoken4.PolicyId = 'username'
        idtoken4.TokenType = ua.UserTokenType.UserName

        appdesc = ua.ApplicationDescription()
        appdesc.ApplicationName = ua.LocalizedText(self.name)
        appdesc.ApplicationUri = self.application_uri
        appdesc.ApplicationType = self.application_type
        appdesc.ProductUri = self.product_uri
        appdesc.DiscoveryUrls.append(self.endpoint.geturl())

        edp = ua.EndpointDescription()
        edp.EndpointUrl = self.endpoint.geturl()
        edp.Server = appdesc
        if self.certificate:
            edp.ServerCertificate = uacrypto.der_from_x509(self.certificate)
        edp.SecurityMode = mode
        edp.SecurityPolicyUri = policy.URI
        edp.UserIdentityTokens = [idtoken, idtoken2, idtoken3, idtoken4]
        edp.TransportProfileUri = 'http://opcfoundation.org/UA-Profile/Transport/uatcp-uasc-uabinary'
        edp.SecurityLevel = 0
        self.iserver.add_endpoint(edp)

    def set_server_name(self, name):
        self.name = name

    def start(self):
        """
        Start to listen on network
        """
        self._setup_server_nodes()
        self.iserver.start()
        self.bserver = BinaryServer(self.iserver, self.endpoint.hostname, self.endpoint.port)
        self.bserver.set_policies(self._policies)
        self.bserver.start()

    def stop(self):
        """
        Stop server
        """
        for client in self._discovery_clients.values():
            client.disconnect()
        self.bserver.stop()
        self.iserver.stop()

    def get_root_node(self):
        """
        Get Root node of server. Returns a Node object.
        """
        return self.get_node(ua.TwoByteNodeId(ua.ObjectIds.RootFolder))

    def get_objects_node(self):
        """
        Get Objects node of server. Returns a Node object.
        """
        return self.get_node(ua.TwoByteNodeId(ua.ObjectIds.ObjectsFolder))

    def get_server_node(self):
        """
        Get Server node of server. Returns a Node object.
        """
        return self.get_node(ua.TwoByteNodeId(ua.ObjectIds.Server))

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
        return len(uries) - 1

    def get_namespace_index(self, uri):
        """
        get index of a namespace using its uri
        """
        uries = self.get_namespace_array()
        return uries.index(uri)

    def get_event_object(self, etype=ua.ObjectIds.BaseEventType, source=ua.ObjectIds.Server):
        """
        Returns an event object using an event type from address space.
        Use this object to fire events
        """
        return Event(self.iserver.isession, etype, source)

    def import_xml(self, path):
        """
        import nodes defined in xml
        """
        importer = xmlimporter.XmlImporter(self.iserver.node_mgt_service)
        importer.import_xml(path)

    def delete_nodes(self, nodes, recursive=False):
        return delete_nodes(self.iserver.isession, nodes, recursive)
