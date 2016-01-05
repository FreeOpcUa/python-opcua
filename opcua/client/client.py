from __future__ import division  # support for python2
from threading import Thread, Condition
import logging
try:
    from urllib.parse import urlparse
except ImportError:  # support for python2
    from urlparse import urlparse

from opcua import ua
from opcua.client.binary_client import BinaryClient
from opcua.common.node import Node
from opcua.common.subscription import Subscription
from opcua.common import utils
from opcua.crypto import security_policies
use_crypto = True
try:
    from opcua.crypto import uacrypto
except ImportError:
    print("cryptography is not installed, use of crypto disabled")
    use_crypto = False


class KeepAlive(Thread):

    """
    Used by Client to keep session opened.
    OPCUA defines timeout both for sessions and secure channel
    """

    def __init__(self, client, timeout):
        Thread.__init__(self)
        self.logger = logging.getLogger(__name__)
        if timeout == 0:  # means no timeout bu we do not trust such servers
            timeout = 360000
        self.timeout = timeout
        self.client = client
        self._dostop = False
        self._cond = Condition()

    def run(self):
        self.logger.debug("starting keepalive thread with period of %s milliseconds", self.timeout)
        server_state = self.client.get_node(ua.FourByteNodeId(ua.ObjectIds.Server_ServerStatus_State))
        while not self._dostop:
            with self._cond:
                self._cond.wait(self.timeout / 1000)
            if self._dostop:
                break
            self.logger.debug("renewing channel")
            self.client.open_secure_channel(renew=True)
            val = server_state.get_value()
            self.logger.debug("server state is: %s ", val)
        self.logger.debug("keepalive thread has stopped")

    def stop(self):
        self.logger.debug("stoping keepalive thread")
        with self._cond:
            self._cond.notify_all()
        self._dostop = True


class Client(object):

    """
    High level client to connect to an OPC-UA server.
    This class makes it easy to connect and browse address space.
    It attemps to expose as much functionality as possible
    but if you want to do to special things you will probably need
    to work with the BinaryClient object, available as self.bclient
    which offers a raw OPC-UA interface.
    """

    def __init__(self, url, timeout=1):
        """
        used url argument to connect to server.
        if you are unsure of url, write at least hostname and port
        and call get_endpoints
        timeout is the timeout to get an answer for requests to server
        public member of this call are available to be set by API users

        """
        self.logger = logging.getLogger(__name__)
        self.server_url = urlparse(url)
        self.name = "Pure Python Client"
        self.description = self.name
        self.application_uri = "urn:freeopcua:client"
        self.product_uri = "urn:freeopcua.github.no:client"
        self.security_policy = ua.SecurityPolicy()
        self.secure_channel_id = None
        self.default_timeout = 3600000
        self.secure_channel_timeout = self.default_timeout
        self.session_timeout = self.default_timeout
        self._policy_ids = []
        self.bclient = BinaryClient(timeout)
        self.user_certificate = None
        self.user_private_key = None
        self._session_counter = 1
        self.keepalive = None

    @staticmethod
    def find_endpoint(endpoints, security_mode, policy_uri):
        """
        Find endpoint with required security mode and policy URI
        """
        for ep in endpoints:
            if (ep.EndpointUrl.startswith(ua.OPC_TCP_SCHEME) and
                    ep.SecurityMode == security_mode and
                    ep.SecurityPolicyUri == policy_uri):
                return ep
        raise ValueError("No matching endpoints: {}, {}".format(
                         security_mode, policy_uri))

    def set_security_string(self, string):
        """
        Set SecureConnection mode. String format:
        Policy,Mode,certificate,private_key[,server_private_key]
        where Policy is Basic128Rsa15 or Basic256,
            Mode is Sign or SignAndEncrypt
            certificate, private_key and server_private_key are
                paths to .pem or .der files
        Call this before connect()
        """
        if not string:
            return
        parts = string.split(',')
        if len(parts) < 4:
            raise Exception('Wrong format: `{}`, expected at least 4 '
                    'comma-separated values'.format(string))
        policy_class = getattr(security_policies, 'SecurityPolicy' + parts[0])
        mode = getattr(ua.MessageSecurityMode, parts[1])
        return self.set_security(policy_class, parts[2], parts[3],
                                 parts[4] if len(parts) >= 5 else None, mode)

    def set_security(self, policy, certificate_path, private_key_path,
                     server_certificate_path=None,
                     mode=ua.MessageSecurityMode.SignAndEncrypt):
        """
        Set SecureConnection mode.
        Call this before connect()
        """
        if server_certificate_path is None:
            # load certificate from server's list of endpoints
            endpoints = self.connect_and_get_server_endpoints()
            endpoint = Client.find_endpoint(endpoints, mode, policy.URI)
            server_cert = uacrypto.x509_from_der(endpoint.ServerCertificate)
        else:
            server_cert = uacrypto.load_certificate(server_certificate_path)
        cert = uacrypto.load_certificate(certificate_path)
        pk = uacrypto.load_private_key(private_key_path)
        self.security_policy = policy(server_cert, cert, pk, mode)
        self.bclient.set_security(self.security_policy)

    def load_client_certificate(self, path):
        """
        load our certificate from file, either pem or der
        """
        self.user_certificate = uacrypto.load_certificate(path)

    def load_private_key(self, path):
        self.user_private_key = uacrypto.load_private_key(path)

    def connect_and_get_server_endpoints(self):
        """
        Connect, ask server for endpoints, and disconnect
        """
        self.connect_socket()
        self.send_hello()
        self.open_secure_channel()
        endpoints = self.get_endpoints()
        self.close_secure_channel()
        self.disconnect_socket()
        return endpoints

    def connect_and_find_servers(self):
        """
        Connect, ask server for a list of known servers, and disconnect
        """
        self.connect_socket()
        self.send_hello()
        self.open_secure_channel()  # spec says it should not be necessary to open channel
        servers = self.find_servers()
        self.close_secure_channel()
        self.disconnect_socket()
        return servers

    def connect_and_find_servers_on_network(self):
        """
        Connect, ask server for a list of known servers on network, and disconnect
        """
        self.connect_socket()
        self.send_hello()
        self.open_secure_channel()
        servers = self.find_servers_on_network()
        self.close_secure_channel()
        self.disconnect_socket()
        return servers

    def connect(self):
        """
        High level method
        Connect, create and activate session
        """
        self.connect_socket()
        self.send_hello()
        self.open_secure_channel()
        self.create_session()
        self.activate_session(username=self.server_url.username, password=self.server_url.password, certificate=self.user_certificate)

    def disconnect(self):
        """
        High level method
        Close session, secure channel and socket
        """
        self.close_session()
        self.close_secure_channel()
        self.disconnect_socket()

    def connect_socket(self):
        """
        connect to socket defined in url
        """
        self.bclient.connect_socket(self.server_url.hostname, self.server_url.port)

    def disconnect_socket(self):
        self.bclient.disconnect_socket()

    def send_hello(self):
        """
        Send OPC-UA hello to server
        """
        ack = self.bclient.send_hello(self.server_url.geturl())
        # FIXME check ack

    def open_secure_channel(self, renew=False):
        """
        Open secure channel, if renew is True, renew channel
        """
        params = ua.OpenSecureChannelParameters()
        params.ClientProtocolVersion = 0
        params.RequestType = ua.SecurityTokenRequestType.Issue
        if renew:
            params.RequestType = ua.SecurityTokenRequestType.Renew
        params.SecurityMode = self.security_policy.Mode
        params.RequestedLifetime = self.secure_channel_timeout
        nonce = utils.create_nonce(self.security_policy.symmetric_key_size)   # length should be equal to the length of key of symmetric encryption
        params.ClientNonce = nonce	# this nonce is used to create a symmetric key
        result = self.bclient.open_secure_channel(params)
        self.security_policy.make_symmetric_key(nonce, result.ServerNonce)
        self.secure_channel_timeout = result.SecurityToken.RevisedLifetime

    def close_secure_channel(self):
        return self.bclient.close_secure_channel()

    def get_endpoints(self):
        params = ua.GetEndpointsParameters()
        params.EndpointUrl = self.server_url.geturl()
        return self.bclient.get_endpoints(params)

    def register_server(self, server, discovery_configuration=None):
        """
        register a server to discovery server
        if discovery_configuration is provided, the newer register_server2 service call is used
        """
        serv = ua.RegisteredServer()
        serv.ServerUri = server.application_uri
        serv.ProductUri = server.product_uri
        serv.DiscoveryUrls = [server.endpoint.geturl()]
        serv.ServerType = server.application_type
        serv.ServerNames = [ua.LocalizedText(server.name)]
        serv.IsOnline = True
        if discovery_configuration:
            params = ua.RegisterServer2Parameters()
            params.Server = serv
            params.DiscoveryConfiguration = discovery_configuration
            return self.bclient.register_server2(params)
        else:
            return self.bclient.register_server(serv)

    def find_servers(self, uris=None):
        """
        send a FindServer request to the server. The answer should be a list of
        servers the server knows about
        A list of uris can be provided, only server having matching uris will be returned
        """
        if uris is None:
            uris = []
        params = ua.FindServersParameters()
        params.EndpointUrl = self.server_url.geturl()
        params.ServerUris = uris 
        return self.bclient.find_servers(params)

    def find_servers_on_network(self):
        params = ua.FindServersOnNetworkParameters()
        return self.bclient.find_servers_on_network(params)

    def create_session(self):
        desc = ua.ApplicationDescription()
        desc.ApplicationUri = self.application_uri
        desc.ProductUri = self.product_uri
        desc.ApplicationName = ua.LocalizedText(self.name)
        desc.ApplicationType = ua.ApplicationType.Client

        params = ua.CreateSessionParameters()
        nonce = utils.create_nonce(32)  # at least 32 random bytes for server to prove possession of private key (specs part 4, 5.6.2.2)
        params.ClientNonce = nonce
        params.ClientCertificate = self.security_policy.client_certificate
        params.ClientDescription = desc
        params.EndpointUrl = self.server_url.geturl()
        params.SessionName = self.description + " Session" + str(self._session_counter)
        params.RequestedSessionTimeout = 3600000
        params.MaxResponseMessageSize = 0  # means no max size
        response = self.bclient.create_session(params)
        self.security_policy.asymmetric_cryptography.verify(self.security_policy.client_certificate + nonce, response.ServerSignature.Signature)
        self._server_nonce = response.ServerNonce
        if not self.security_policy.server_certificate:
            self.security_policy.server_certificate = response.ServerCertificate
        elif self.security_policy.server_certificate != response.ServerCertificate:
            raise Exception("Server certificate mismatch")
        # remember PolicyId's: we will use them in activate_session()
        ep = Client.find_endpoint(response.ServerEndpoints, self.security_policy.Mode, self.security_policy.URI)
        self._policy_ids = ep.UserIdentityTokens
        self.session_timeout = response.RevisedSessionTimeout
        self.keepalive = KeepAlive(self, min(self.session_timeout, self.secure_channel_timeout) * 0.7)  # 0.7 is from spec
        self.keepalive.start()
        return response

    def server_policy_id(self, token_type, default):
        """
        Find PolicyId of server's UserTokenPolicy by token_type.
        Return default if there's no matching UserTokenPolicy.
        """
        for policy in self._policy_ids:
            if policy.TokenType == token_type:
                return policy.PolicyId
        return default

    def activate_session(self, username=None, password=None, certificate=None):
        """
        Activate session using either username and password or private_key
        """
        params = ua.ActivateSessionParameters()
        challenge = self.security_policy.server_certificate + self._server_nonce
        params.ClientSignature.Algorithm = b"http://www.w3.org/2000/09/xmldsig#rsa-sha1"
        params.ClientSignature.Signature = self.security_policy.asymmetric_cryptography.signature(challenge)
        params.LocaleIds.append("en")
        if not username and not certificate:
            params.UserIdentityToken = ua.AnonymousIdentityToken()
            params.UserIdentityToken.PolicyId = self.server_policy_id(ua.UserTokenType.Anonymous, b"anonymous")
        elif certificate:
            params.UserIdentityToken = ua.X509IdentityToken()
            params.UserIdentityToken.PolicyId = self.server_policy_id(ua.UserTokenType.Certificate, b"certificate_basic256")
            params.UserIdentityToken.CertificateData = uacrypto.der_from_x509(certificate)
            # specs part 4, 5.6.3.1: the data to sign is created by appending
            # the last serverNonce to the serverCertificate
            sig = uacrypto.sign_sha1(self.user_private_key, challenge)
            params.UserTokenSignature = ua.SignatureData()
            params.UserTokenSignature.Algorithm = b"http://www.w3.org/2000/09/xmldsig#rsa-sha1"
            params.UserTokenSignature.Signature = sig
        else:
            params.UserIdentityToken = ua.UserNameIdentityToken()
            params.UserIdentityToken.UserName = username 
            if self.server_url.password:
                pubkey = uacrypto.x509_from_der(self.security_policy.server_certificate).public_key()
                # see specs part 4, 7.36.3: if the token is encrypted, password
                # shall be converted to UTF-8 and serialized with server nonce
                etoken = ua.pack_bytes(bytes(password, "utf8") + self._server_nonce)
                #data = uacrypto.encrypt_basic256(pubkey, etoken)
                data = uacrypto.encrypt_rsa_oaep(pubkey, etoken)
                params.UserIdentityToken.Password = data
            params.UserIdentityToken.PolicyId = self.server_policy_id(ua.UserTokenType.UserName, b"username_basic256")
            params.UserIdentityToken.EncryptionAlgorithm = 'http://www.w3.org/2001/04/xmlenc#rsa-oaep'
        return self.bclient.activate_session(params)

    def close_session(self):
        """
        Close session
        """
        if self.keepalive:
            self.keepalive.stop()
        return self.bclient.close_session(True)

    def get_root_node(self):
        return self.get_node(ua.TwoByteNodeId(ua.ObjectIds.RootFolder))

    def get_objects_node(self):
        return self.get_node(ua.TwoByteNodeId(ua.ObjectIds.ObjectsFolder))

    def get_server_node(self):
        return self.get_node(ua.TwoByteNodeId(ua.ObjectIds.Server))

    def get_node(self, nodeid):
        """
        Get node using NodeId object or a string representing a NodeId
        """
        return Node(self.bclient, nodeid)

    def create_subscription(self, period, handler):
        """
        Create a subscription.
        returns a Subscription object which allow
        to subscribe to events or data on server
        handler argument is a class with data_change and/or event methods.
        These methods will be called when notfication from server are received.
        See example-client.py.
        Do not do expensive/slow or network operation from these methods 
        since they are called directly from receiving thread. This is a design choice,
        start another thread if you need to do such a thing.
        """
        params = ua.CreateSubscriptionParameters()
        params.RequestedPublishingInterval = period
        params.RequestedLifetimeCount = 3000
        params.RequestedMaxKeepAliveCount = 10000
        params.MaxNotificationsPerPublish = 10000
        params.PublishingEnabled = True
        params.Priority = 0
        return Subscription(self.bclient, params, handler)

    def get_namespace_array(self):
        ns_node = self.get_node(ua.NodeId(ua.ObjectIds.Server_NamespaceArray))
        return ns_node.get_value()

    def get_namespace_index(self, uri):
        uries = self.get_namespace_array()
        return uries.index(uri)
