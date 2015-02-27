import logging

from opcua import uaprotocol as ua
from opcua import BinaryClient 


class Client(object):
    def __init__(self, uri):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.server_uri = uri
        self.session_name = "Pure Python Client"
        self.application_uri = "urn:freeopcua:client"
        self.product_uri = "urn:freeopcua.github.no:client"
        self.security_policy_uri = "http://opcfoundation.org/UA/SecurityPolicy#None"
        self.secure_channel_id = None
        self.default_timeout = 3600000
        self.bclient = BinaryClient()

    def connect(self):
        self.bclient.connect()
        ack = self.bclient.send_hello(self.server_uri)
        self.bclient.start()

    def disconnect(self):
        #self.bclient.disconnect()
        self.bclient.stop()


    def open_secure_channel(self):

        params = ua.OpenSecureChannelParameters()
        params.ClientProtocolVersion = 0
        params.RequestType = ua.SecurityTokenRequestType.Issue
        params.SecurityMode = ua.MessageSecurityMode.None_
        params.RequestedLifetime = 300000
        params.ClientNonce = ua.ByteString('\x00')
        self.bclient.open_secure_channel(params)


