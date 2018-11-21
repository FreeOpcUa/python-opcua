from __future__ import division  # support for python2
from threading import Thread, Condition
import concurrent.futures
import logging
try:
    from urllib.parse import urlparse
except ImportError:  # support for python2
    from urlparse import urlparse

from opcua import ua
from opcua.client.ua_client import UaClient
from opcua.common.xmlimporter import XmlImporter
from opcua.common.xmlexporter import XmlExporter
from opcua.common.node import Node
from opcua.common.manage_nodes import delete_nodes
from opcua.common.subscription import Subscription
from opcua.common import utils
from opcua.crypto import security_policies
from opcua.common.shortcuts import Shortcuts
from opcua.common.structures import load_type_definitions, load_enums
use_crypto = True
try:
    from opcua.crypto import uacrypto
except ImportError:
    logging.getLogger(__name__).warning("cryptography is not installed, use of crypto disabled")
    use_crypto = False


class KeepAlive(Thread):

    """
    Used by Client to keep the session open.
    OPCUA defines timeout both for sessions and secure channel
    """

    def __init__(self, client, timeout):
        """
        :param session_timeout: Timeout to re-new the session
            in milliseconds.
        """
        Thread.__init__(self)
        self.logger = logging.getLogger(__name__)

        self.client = client
        self._dostop = False
        self._cond = Condition()
        self.timeout = timeout

        # some server support no timeout, but we do not trust them
        if self.timeout == 0:
            self.timeout = 3600000  # 1 hour

    def run(self):
        self.logger.debug("starting keepalive thread with period of %s milliseconds", self.timeout)
        server_state = self.client.get_node(ua.FourByteNodeId(ua.ObjectIds.Server_ServerStatus_State))
        while not self._dostop:
            with self._cond:
                self._cond.wait(self.timeout / 1000)
            if self._dostop:
                break
            self.logger.debug("renewing channel")
            try:
                self.client.open_secure_channel(renew=True)
            except concurrent.futures.TimeoutError:
                self.logger.debug("keepalive failed: timeout on open_secure_channel()")
                break
            val = server_state.get_value()
            self.logger.debug("server state is: %s ", val)
        self.logger.debug("keepalive thread has stopped")

    def stop(self):
        self.logger.debug("stoping keepalive thread")
        self._dostop = True
        with self._cond:
            self._cond.notify_all()


class Client(object):

    """
    High level client to connect to an OPC-UA server.

    This class makes it easy to connect and browse address space.
    It attemps to expose as much functionality as possible
    but if you want more flexibility it is possible and adviced to
    use UaClient object, available as self.uaclient
    which offers the raw OPC-UA services interface.
    """

    def __init__(self, url, timeout=4):
        """

        :param url: url of the server.
            if you are unsure of url, write at least hostname
            and port and call get_endpoints

        :param timeout:
            Each request sent to the server expects an answer within this
            time. The timeout is specified in seconds.
        """
        self.logger = logging.getLogger(__name__)
        self.server_url = urlparse(url)
        # take initial username and password from the url
        self._username = self.server_url.username
        self._password = self.server_url.password
        self.name = "Pure Python Client"
        self.description = self.name
        self.application_uri = "urn:freeopcua:client"
        self.product_uri = "urn:freeopcua.github.io:client"
        self.security_policy = ua.SecurityPolicy()
        self.secure_channel_id = None
        self.secure_channel_timeout = 3600000  # 1 hour
        self.session_timeout = 3600000  # 1 hour
        self._policy_ids = []
        self.uaclient = UaClient(timeout)
        self.user_certificate = None
        self.user_private_key = None
        self._server_nonce = None
        self._session_counter = 1
        self.keepalive = None
        self.nodes = Shortcuts(self.uaclient)
        self.max_messagesize = 0  # No limits
        self.max_chunkcount = 0  # No limits

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.disconnect()

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
        raise ua.UaError("No matching endpoints: {0}, {1}".format(security_mode, policy_uri))

    def set_user(self, username):
        """
        Set user name for the connection.
        initial user from the URL will be overwritten
        """
        self._username = username

    def set_password(self, pwd):
        """
        Set user password for the connection.
        initial password from the URL will be overwritten
        """
        self._password = pwd

    def set_security_string(self, string):
        """
        Set SecureConnection mode. String format:
        Policy,Mode,certificate,private_key[,server_private_key]
        where Policy is Basic128Rsa15, Basic256 or Basic256Sha256,
            Mode is Sign or SignAndEncrypt
            certificate, private_key and server_private_key are
                paths to .pem or .der files
        Call this before connect()
        """
        if not string:
            return
        parts = string.split(',')
        if len(parts) < 4:
            raise ua.UaError('Wrong format: `{0}`, expected at least 4 comma-separated values'.format(string))
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
        self.uaclient.set_security(self.security_policy)

    def load_client_certificate(self, path):
        """
        load our certificate from file, either pem or der
        """
        self.user_certificate = uacrypto.load_certificate(path)

    def load_private_key(self, path):
        """
        Load user private key. This is used for authenticating using certificate
        """
        self.user_private_key = uacrypto.load_private_key(path)

    def connect_and_get_server_endpoints(self):
        """
        Connect, ask server for endpoints, and disconnect
        """
        self.connect_socket()
        try:
            self.send_hello()
            self.open_secure_channel()
            endpoints = self.get_endpoints()
            self.close_secure_channel()
        finally:
            self.disconnect_socket()
        return endpoints

    def connect_and_find_servers(self):
        """
        Connect, ask server for a list of known servers, and disconnect
        """
        self.connect_socket()
        try:
            self.send_hello()
            self.open_secure_channel()  # spec says it should not be necessary to open channel
            servers = self.find_servers()
            self.close_secure_channel()
        finally:
            self.disconnect_socket()
        return servers

    def connect_and_find_servers_on_network(self):
        """
        Connect, ask server for a list of known servers on network, and disconnect
        """
        self.connect_socket()
        try:
            self.send_hello()
            self.open_secure_channel()
            servers = self.find_servers_on_network()
            self.close_secure_channel()
        finally:
            self.disconnect_socket()
        return servers

    def connect(self):
        """
        High level method
        Connect, create and activate session
        """
        self.connect_socket()
        try:
            self.send_hello()
            self.open_secure_channel()
            self.create_session()
        except Exception:
            self.disconnect_socket()  # clean up open socket
            raise
        self.activate_session(username=self._username, password=self._password, certificate=self.user_certificate)

    def disconnect(self):
        """
        High level method
        Close session, secure channel and socket
        """
        try:
            self.close_session()
            self.close_secure_channel()
        finally:
            self.disconnect_socket()

    def connect_socket(self):
        """
        connect to socket defined in url
        """
        self.uaclient.connect_socket(self.server_url.hostname, self.server_url.port)

    def disconnect_socket(self):
        self.uaclient.disconnect_socket()

    def send_hello(self):
        """
        Send OPC-UA hello to server
        """
        ack = self.uaclient.send_hello(self.server_url.geturl(), self.max_messagesize, self.max_chunkcount)
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
        # length should be equal to the length of key of symmetric encryption
        nonce = utils.create_nonce(self.security_policy.symmetric_key_size)
        params.ClientNonce = nonce  # this nonce is used to create a symmetric key
        result = self.uaclient.open_secure_channel(params)
        self.security_policy.make_symmetric_key(nonce, result.ServerNonce)
        self.secure_channel_timeout = result.SecurityToken.RevisedLifetime

    def close_secure_channel(self):
        return self.uaclient.close_secure_channel()

    def get_endpoints(self):
        params = ua.GetEndpointsParameters()
        params.EndpointUrl = self.server_url.geturl()
        return self.uaclient.get_endpoints(params)

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
        return self.uaclient.find_servers(params)

    def find_servers_on_network(self):
        params = ua.FindServersOnNetworkParameters()
        return self.uaclient.find_servers_on_network(params)

    def create_session(self):
        """
        send a CreateSessionRequest to server with reasonable parameters.
        If you want o modify settings look at code of this methods
        and make your own
        """
        desc = ua.ApplicationDescription()
        desc.ApplicationUri = self.application_uri
        desc.ProductUri = self.product_uri
        desc.ApplicationName = ua.LocalizedText(self.name)
        desc.ApplicationType = ua.ApplicationType.Client

        params = ua.CreateSessionParameters()
        # at least 32 random bytes for server to prove possession of private key (specs part 4, 5.6.2.2)
        nonce = utils.create_nonce(32)
        params.ClientNonce = nonce
        params.ClientCertificate = self.security_policy.client_certificate
        params.ClientDescription = desc
        params.EndpointUrl = self.server_url.geturl()
        params.SessionName = self.description + " Session" + str(self._session_counter)
        params.RequestedSessionTimeout = 3600000
        params.MaxResponseMessageSize = 0  # means no max size
        response = self.uaclient.create_session(params)
        if self.security_policy.client_certificate is None:
            data = nonce
        else:
            data = self.security_policy.client_certificate + nonce
        self.security_policy.asymmetric_cryptography.verify(data, response.ServerSignature.Signature)
        self._server_nonce = response.ServerNonce
        if not self.security_policy.server_certificate:
            self.security_policy.server_certificate = response.ServerCertificate
        elif self.security_policy.server_certificate != response.ServerCertificate:
            raise ua.UaError("Server certificate mismatch")
        # remember PolicyId's: we will use them in activate_session()
        ep = Client.find_endpoint(response.ServerEndpoints, self.security_policy.Mode, self.security_policy.URI)
        self._policy_ids = ep.UserIdentityTokens
        self.session_timeout = response.RevisedSessionTimeout
        self.keepalive = KeepAlive(
            self, min(self.session_timeout, self.secure_channel_timeout) * 0.7)  # 0.7 is from spec
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

    def server_policy_uri(self, token_type):
        """
        Find SecurityPolicyUri of server's UserTokenPolicy by token_type.
        If SecurityPolicyUri is empty, use default SecurityPolicyUri
        of the endpoint
        """
        for policy in self._policy_ids:
            if policy.TokenType == token_type:
                if policy.SecurityPolicyUri:
                    return policy.SecurityPolicyUri
                else:   # empty URI means "use this endpoint's policy URI"
                    return self.security_policy.URI
        return self.security_policy.URI

    def activate_session(self, username=None, password=None, certificate=None):
        """
        Activate session using either username and password or private_key
        """
        params = ua.ActivateSessionParameters()
        challenge = b""
        if self.security_policy.server_certificate is not None:
            challenge += self.security_policy.server_certificate
        if self._server_nonce is not None:
            challenge += self._server_nonce
        params.ClientSignature.Algorithm = "http://www.w3.org/2000/09/xmldsig#rsa-sha1"
        params.ClientSignature.Signature = self.security_policy.asymmetric_cryptography.signature(challenge)
        params.LocaleIds.append("en")
        if not username and not certificate:
            self._add_anonymous_auth(params)
        elif certificate:
            self._add_certificate_auth(params, certificate, challenge)
        else:
            self._add_user_auth(params, username, password)
        return self.uaclient.activate_session(params)

    def _add_anonymous_auth(self, params):
        params.UserIdentityToken = ua.AnonymousIdentityToken()
        params.UserIdentityToken.PolicyId = self.server_policy_id(ua.UserTokenType.Anonymous, "anonymous")

    def _add_certificate_auth(self, params, certificate, challenge):
        params.UserIdentityToken = ua.X509IdentityToken()
        params.UserIdentityToken.PolicyId = self.server_policy_id(ua.UserTokenType.Certificate, "certificate_basic256")
        params.UserIdentityToken.CertificateData = uacrypto.der_from_x509(certificate)
        # specs part 4, 5.6.3.1: the data to sign is created by appending
        # the last serverNonce to the serverCertificate
        sig = uacrypto.sign_sha1(self.user_private_key, challenge)
        params.UserTokenSignature = ua.SignatureData()
        params.UserTokenSignature.Algorithm = "http://www.w3.org/2000/09/xmldsig#rsa-sha1"
        params.UserTokenSignature.Signature = sig

    def _add_user_auth(self, params, username, password):
        params.UserIdentityToken = ua.UserNameIdentityToken()
        params.UserIdentityToken.UserName = username
        policy_uri = self.server_policy_uri(ua.UserTokenType.UserName)
        if not policy_uri or policy_uri == security_policies.POLICY_NONE_URI:
            # see specs part 4, 7.36.3: if the token is NOT encrypted,
            # then the password only contains UTF-8 encoded password
            # and EncryptionAlgorithm is null
            if self._password:
                self.logger.warning("Sending plain-text password")
                params.UserIdentityToken.Password = password.encode('utf8')
            params.UserIdentityToken.EncryptionAlgorithm = None
        elif self._password:
            data, uri = self._encrypt_password(password, policy_uri)
            params.UserIdentityToken.Password = data
            params.UserIdentityToken.EncryptionAlgorithm = uri
        params.UserIdentityToken.PolicyId = self.server_policy_id(ua.UserTokenType.UserName, "username_basic256")

    def _encrypt_password(self, password, policy_uri):
        pubkey = uacrypto.x509_from_der(self.security_policy.server_certificate).public_key()
        # see specs part 4, 7.36.3: if the token is encrypted, password
        # shall be converted to UTF-8 and serialized with server nonce
        passwd = password.encode("utf8")
        if self._server_nonce is not None:
            passwd += self._server_nonce
        etoken = ua.ua_binary.Primitives.Bytes.pack(passwd)
        data, uri = security_policies.encrypt_asymmetric(pubkey, etoken, policy_uri)
        return data, uri

    def close_session(self):
        """
        Close session
        """
        if self.keepalive and self.keepalive.is_alive():
            self.keepalive.stop()
            self.keepalive.join()
        return self.uaclient.close_session(True)

    def get_root_node(self):
        return self.get_node(ua.TwoByteNodeId(ua.ObjectIds.RootFolder))

    def get_objects_node(self):
        return self.get_node(ua.TwoByteNodeId(ua.ObjectIds.ObjectsFolder))

    def get_server_node(self):
        return self.get_node(ua.FourByteNodeId(ua.ObjectIds.Server))

    def get_node(self, nodeid):
        """
        Get node using NodeId object or a string representing a NodeId
        """
        return Node(self.uaclient, nodeid)

    def create_subscription(self, period, handler):
        """
        Create a subscription.
        returns a Subscription object which allow
        to subscribe to events or data on server
        handler argument is a class with data_change and/or event methods.
        period argument is either a publishing interval in milliseconds or a
        CreateSubscriptionParameters instance. The second option should be used,
        if the opcua-server has problems with the default options.
        These methods will be called when notfication from server are received.
        See example-client.py.
        Do not do expensive/slow or network operation from these methods
        since they are called directly from receiving thread. This is a design choice,
        start another thread if you need to do such a thing.
        """

        if isinstance(period, ua.CreateSubscriptionParameters):
            return Subscription(self.uaclient, period, handler)
        params = ua.CreateSubscriptionParameters()
        params.RequestedPublishingInterval = period
        params.RequestedLifetimeCount = 10000
        params.RequestedMaxKeepAliveCount = 3000
        params.MaxNotificationsPerPublish = 10000
        params.PublishingEnabled = True
        params.Priority = 0
        return Subscription(self.uaclient, params, handler)

    def get_namespace_array(self):
        ns_node = self.get_node(ua.NodeId(ua.ObjectIds.Server_NamespaceArray))
        return ns_node.get_value()

    def get_namespace_index(self, uri):
        uries = self.get_namespace_array()
        return uries.index(uri)

    def delete_nodes(self, nodes, recursive=False):
        return delete_nodes(self.uaclient, nodes, recursive)

    def import_xml(self, path=None, xmlstring=None):
        """
        Import nodes defined in xml
        """
        importer = XmlImporter(self)
        return importer.import_xml(path, xmlstring)

    def export_xml(self, nodes, path):
        """
        Export defined nodes to xml
        """
        exp = XmlExporter(self)
        exp.build_etree(nodes)
        return exp.write_xml(path)

    def register_namespace(self, uri):
        """
        Register a new namespace. Nodes should in custom namespace, not 0.
        This method is mainly implemented for symetry with server
        """
        ns_node = self.get_node(ua.NodeId(ua.ObjectIds.Server_NamespaceArray))
        uries = ns_node.get_value()
        if uri in uries:
            return uries.index(uri)
        uries.append(uri)
        ns_node.set_value(uries)
        return len(uries) - 1

    def load_type_definitions(self, nodes=None):
        """
        Load custom types (custom structures/extension objects) definition from server
        Generate Python classes for custom structures/extension objects defined in server
        These classes will available in ua module
        """
        return load_type_definitions(self, nodes)

    def load_enums(self):
        """
        generate Python enums for custom enums on server.
        This enums will be available in ua module
        """
        return load_enums(self)
