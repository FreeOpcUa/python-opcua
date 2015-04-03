"""
High level interface to pure python OPC-UA server
"""

import logging
try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse


from opcua import ua
from opcua.binary_server import BinaryServer
from opcua.internal_server import InternalServer
from opcua import Node, Subscription


class Server(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.endpoint = None
        self.name = None
        self.server_uri = "urn:freeopcua:python:server"
        self.product_uri = "urn:freeopcua.github.no:python:server"
        self.name = "FreeOpcUa Python Server"
        self.default_timeout = 3600000
        self.iserver = InternalServer()
        self.bserver = None

    def set_endpoint(self, url):
        self.endpoint = urlparse(url)

    def _setup_server_nodes(self):
        #to be called just before starting server since it needs all parameters to be setup
        self._set_endpoints()
        self.register_namespace(self.server_uri)
        sa_node = self.get_node(ua.NodeId(ua.ObjectIds.Server_ServerArray))
        sa_node.set_value([self.server_uri])

    def _set_endpoints(self):
        idtoken = ua.UserTokenPolicy()
        idtoken.PolicyId = 'anonymous'
        idtoken.TokenType = ua.UserTokenType.Anonymous

        appdesc = ua.ApplicationDescription()
        appdesc.ApplicationName = ua.LocalizedText(self.name)
        appdesc.ApplicationUri = self.server_uri 
        appdesc.ApplicationType = ua.ApplicationType.Server
        appdesc.ProductUri = self.product_uri 

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
        self.iserver.start()
        self._setup_server_nodes()
        self.bserver = BinaryServer(self.iserver, self.endpoint.hostname, self.endpoint.port)
        self.bserver.start()

    def stop(self):
        self.iserver.stop()
        self.bserver.stop()


    def get_root_node(self):
        return self.get_node(ua.TwoByteNodeId(ua.ObjectIds.RootFolder))

    def get_objects_node(self):
        return self.get_node(ua.TwoByteNodeId(ua.ObjectIds.ObjectsFolder))

    def get_node(self, nodeid):
        """
        Get node using NodeId object or a string representing a NodeId
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
        ns_node = self.get_node(ua.NodeId(ua.ObjectIds.Server_NamespaceArray))
        return ns_node.get_value()

    def register_namespace(self, uri):
        ns_node = self.get_node(ua.NodeId(ua.ObjectIds.Server_NamespaceArray))
        uries = ns_node.get_value()
        uries.append(uri)
        ns_node.set_value(uries)
        return (len(uries)-1)

    def get_namespace_index(self, uri):
        uries = self.get_namespace_array()
        return uries.index(uri)





