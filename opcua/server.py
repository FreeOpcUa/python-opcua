"""
High level interface to pure python OPC-UA server
"""

import logging
from urllib.parse import urlparse

from opcua import ua
from opcua.binary_server import BinaryServer
from opcua.internal_server import InternalServer

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

    def _set_endpoints(self):
        #to be called just before starting server since it needs all parameters to be setup
        idtoken = ua.UserTokenPolicy()
        idtoken.PolicyId = 'anonymous'
        idtoken.IssuedTokenType = ua.UserTokenType.Anonymous

        appdesc = ua.ApplicationDescription
        appdesc.ApplicationName = ua.LocalizedText(self.name)
        appdesc.ApplicationUri = self.server_uri 
        appdesc.ApplicationType = ua.ApplicationType.Server
        appdesc.ProductUri = self.product_uri 

        edp = ua.EndpointDescription()
        edp.Server = appdesc()
        edp.SecurityMode = ua.MessageSecurityMode.None_
        edp.SecurityPolicyUri = 'http://opcfoundation.org/UA/SecurityPolicy#None'
        edp.UserIdentityTokens = [idtoken]
        edp.TransportProfileUri = 'http://opcfoundation.org/UA-Profile/Transport/uatcp-uasc-uabinary'
        edp.SecurityLevel = 0

        self.iserver.add_endpoint(edp)

    def set_server_name(self, name):
        self.name = name

    def start(self):
        self._set_endpoints()
        self.bserver = BinaryServer(self.iserver, self.endpoint.hostname, self.endpoint.port)
        self.bserver.start()

    def stop(self):
        self.bserver.stop()



