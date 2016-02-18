import unittest

from opcua import Client
from opcua import Server
from opcua import ua

port_num1 = 48515
port_num2 = 48512


class TestCryptoConnect(unittest.TestCase):

    '''
    Test connectino with a server supporting crypto 

    '''
    @classmethod
    def setUpClass(self):
        # start our own server
        self.srv_crypto = Server()
        self.uri_crypto = 'opc.tcp://localhost:%d' % port_num1
        self.srv_crypto.set_endpoint(self.uri_crypto)
        # load server certificate and private key. This enables endpoints
        # with signing and encryption.
        self.srv_crypto.load_certificate("examples/example-certificate.der")
        self.srv_crypto.load_private_key("examples/example-private-key.pem")
        self.srv_crypto.start()

        # start a server without crypto
        self.srv_no_crypto = Server()
        self.uri_no_crypto = 'opc.tcp://localhost:%d' % port_num2
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

    def test_nocrypto_feil(self):
        clt = Client(self.uri_no_crypto)
        with self.assertRaises(ua.UaError):
            clt.set_security_string("Basic256,Sign,examples/example-certificate.der,examples/example-private-key.pem")

    def test_basic256(self):
        clt = Client(self.uri_crypto)
        try:
            clt.set_security_string("Basic256,Sign,examples/example-certificate.der,examples/example-private-key.pem")
            clt.connect()
            self.assertTrue(clt.get_objects_node().get_children())
        finally:
            clt.disconnect()



