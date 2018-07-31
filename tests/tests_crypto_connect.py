import pytest

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

pytestmark = pytest.mark.asyncio

port_num1 = 48515
port_num2 = 48512
uri_crypto = 'opc.tcp://127.0.0.1:{0:d}'.format(port_num1)
uri_no_crypto = 'opc.tcp://127.0.0.1:{0:d}'.format(port_num2)


@pytest.fixture()
async def srv_crypto():
    # start our own server
    srv = Server()
    await srv.init()
    srv.set_endpoint(uri_crypto)
    await srv.load_certificate("examples/certificate-example.der")
    await srv.load_private_key("examples/private-key-example.pem")
    await srv.start()
    yield srv
    # stop the server
    await srv.stop()


@pytest.fixture()
async def srv_no_crypto():
    # start our own server
    srv = Server()
    await srv.init()
    srv.set_endpoint(uri_no_crypto)
    await srv.start()
    yield srv
    # stop the server
    await srv.stop()


async def test_nocrypto(srv_no_crypto):
    clt = Client(uri_no_crypto)
    async with clt:
        await clt.get_objects_node().get_children()


async def test_nocrypto_fail():
    clt = Client(uri_no_crypto)
    with pytest.raises(ua.UaError):
        await clt.set_security_string("Basic256,Sign,examples/certificate-example.der,examples/private-key-example.pem")


async def test_basic256(srv_crypto):
    clt = Client(uri_crypto)
    await clt.set_security_string("Basic256,Sign,examples/certificate-example.der,examples/private-key-example.pem")
    async with clt:
        assert await clt.get_objects_node().get_children()


async def test_basic256_encrypt():
    clt = Client(uri_crypto)
    await clt.set_security_string(
            "Basic256,SignAndEncrypt,examples/certificate-example.der,examples/private-key-example.pem")
    async with clt:
        assert await clt.get_objects_node().get_children()


async def test_basic128Rsa15():
    clt = Client(uri_crypto)
    await clt.set_security_string("Basic128Rsa15,Sign,examples/certificate-example.der,examples/private-key-example.pem")
    async with clt:
        assert await clt.get_objects_node().get_children()


async def test_basic128Rsa15_encrypt():
    clt = Client(uri_crypto)
    await clt.set_security_string(
        "Basic128Rsa15,SignAndEncrypt,examples/certificate-example.der,examples/private-key-example.pem"
    )
    async with clt:
        assert await clt.get_objects_node().get_children()


async def test_basic256_encrypt_success():
    clt = Client(uri_crypto)
    await clt.set_security(
            security_policies.SecurityPolicyBasic256,
            'examples/certificate-example.der',
            'examples/private-key-example.pem',
            None,
            ua.MessageSecurityMode.SignAndEncrypt
        )
    async with clt:
        assert await clt.get_objects_node().get_children()


async def test_basic256_encrypt_feil():
    # FIXME: how to make it feil???
    clt = Client(uri_crypto)
    with pytest.raises(ua.UaError):
        await clt.set_security(
            security_policies.SecurityPolicyBasic256,
            'examples/certificate-example.der',
            'examples/private-key-example.pem',
            None,
            ua.MessageSecurityMode.None_
        )


"""
@unittest.skipIf(disable_crypto_tests, "crypto not available")
class TestCryptoConnect(unittest.TestCase):

    '''
    Test connectino with a server supporting crypto 

    '''
    @classmethod
    def setUpClass(cls):
        # start our own server
        cls.srv_crypto = Server()
        cls.uri_crypto = 'opc.tcp://127.0.0.1:{0:d}'.format(port_num1)
        cls.srv_crypto.set_endpoint(cls.uri_crypto)
        # load server certificate and private key. This enables endpoints
        # with signing and encryption.
        cls.srv_crypto.load_certificate("examples/certificate-example.der")
        cls.srv_crypto.load_private_key("examples/private-key-example.pem")
        cls.srv_crypto.start()

        # start a server without crypto
        cls.srv_no_crypto = Server()
        cls.uri_no_crypto = 'opc.tcp://127.0.0.1:{0:d}'.format(port_num2)
        cls.srv_no_crypto.set_endpoint(cls.uri_no_crypto)
        cls.srv_no_crypto.start()

    @classmethod
    def tearDownClass(cls):
        # stop the server 
        cls.srv_no_crypto.stop()
        cls.srv_crypto.stop()


    def test_basic256_encrypt(self):
        clt = Client(self.uri_crypto)
        try:
            clt.set_security_string("Basic256,SignAndEncrypt,examples/certificate-example.der,examples/private-key-example.pem")
            clt.connect()
            self.assertTrue(clt.get_objects_node().get_children())
        finally:
            clt.disconnect()

    def test_basic128Rsa15(self):
        clt = Client(self.uri_crypto)
        try:
            clt.set_security_string("Basic128Rsa15,Sign,examples/certificate-example.der,examples/private-key-example.pem")
            clt.connect()
            self.assertTrue(clt.get_objects_node().get_children())
        finally:
            clt.disconnect()

    def test_basic128Rsa15_encrypt(self):
        clt = Client(self.uri_crypto)
        try:
            clt.set_security_string("Basic128Rsa15,SignAndEncrypt,examples/certificate-example.der,examples/private-key-example.pem")
            clt.connect()
            self.assertTrue(clt.get_objects_node().get_children())
        finally:
            clt.disconnect()

    def test_basic256_encrypt_success(self):
        clt = Client(self.uri_crypto)
        try:
            clt.set_security(security_policies.SecurityPolicyBasic256,
                             'examples/certificate-example.der',
                             'examples/private-key-example.pem',
                             None,
                             ua.MessageSecurityMode.SignAndEncrypt
                             )
            clt.connect()
            self.assertTrue(clt.get_objects_node().get_children())
        finally:
            clt.disconnect()

    def test_basic256_encrypt_feil(self):
        # FIXME: how to make it feil???
        clt = Client(self.uri_crypto)
        with self.assertRaises(ua.UaError):
            clt.set_security(security_policies.SecurityPolicyBasic256,
                             'examples/certificate-example.der',
                             'examples/private-key-example.pem',
                             None,
                             ua.MessageSecurityMode.None_
                             )
"""
