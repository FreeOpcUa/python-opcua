import unittest

from opcua import Client
from opcua import Server
from opcua import ua

try:
    from opcua.crypto import uacrypto
    from opcua.crypto import security_policies
except ImportError:
    print("WARNING: CRYPTO NOT AVAILABLE, CRYPTO TESTS DISABLED!!")
    disable_crypto_tests = True
else:
    disable_crypto_tests = False


port_num1 = 48515
port_num2 = 48512

@unittest.skipIf(disable_crypto_tests, "crypto not available")
class TestCryptoConnect(unittest.TestCase):

    '''
    Test connectino with a server supporting crypto 

    '''
    @classmethod
    def setUpClass(self):
        # start our own server
        self.srv_crypto = Server()
        self.uri_crypto = 'opc.tcp://127.0.0.1:{0:d}'.format(port_num1)
        self.srv_crypto.set_endpoint(self.uri_crypto)
        # load server certificate and private key. This enables endpoints
        # with signing and encryption.
        self.srv_crypto.load_certificate("examples/certificate-example.der")
        self.srv_crypto.load_private_key("examples/private-key-example.pem")
        self.srv_crypto.start()

        # start a server without crypto
        self.srv_no_crypto = Server()
        self.uri_no_crypto = 'opc.tcp://127.0.0.1:{0:d}'.format(port_num2)
        self.srv_no_crypto.set_endpoint(self.uri_no_crypto)
        self.srv_no_crypto.start()

    @classmethod
    def tearDownClass(self):
        # stop the server 
        self.srv_no_crypto.stop()
        self.srv_crypto.stop()

    def test_nocrypto(self):
        clt = Client(self.uri_no_crypto)
        clt.connect()
        try:
            clt.get_objects_node().get_children()
        finally:
            clt.disconnect()

    def test_nocrypto_fail(self):
        clt = Client(self.uri_no_crypto)
        with self.assertRaises(ua.UaError):
            clt.set_security_string("Basic256Sha256,Sign,examples/certificate-example.der,examples/private-key-example.pem")

    def test_basic256sha256(self):
        clt = Client(self.uri_crypto)
        try:
            clt.set_security_string("Basic256Sha256,Sign,examples/certificate-example.der,examples/private-key-example.pem")
            clt.connect()
            self.assertTrue(clt.get_objects_node().get_children())
        finally:
            clt.disconnect()

    def test_basic256sha256_encrypt(self):
        clt = Client(self.uri_crypto)
        try:
            clt.set_security_string("Basic256Sha256,SignAndEncrypt,examples/certificate-example.der,examples/private-key-example.pem")
            clt.connect()
            self.assertTrue(clt.get_objects_node().get_children())
        finally:
            clt.disconnect()

    def test_basic256sha56_encrypt_success(self):
        clt = Client(self.uri_crypto)
        try:
            clt.set_security(security_policies.SecurityPolicyBasic256Sha256,
                             'examples/certificate-example.der',
                             'examples/private-key-example.pem',
                             None,
                             ua.MessageSecurityMode.SignAndEncrypt
                             )
            clt.connect()
            self.assertTrue(clt.get_objects_node().get_children())
        finally:
            clt.disconnect()

    def test_basic256sha56_encrypt_fail(self):
        # FIXME: how to make it fail???
        clt = Client(self.uri_crypto)
        with self.assertRaises(ua.UaError):
            clt.set_security(security_policies.SecurityPolicyBasic256Sha256,
                             'examples/certificate-example.der',
                             'examples/private-key-example.pem',
                             None,
                             ua.MessageSecurityMode.None_
                             )
