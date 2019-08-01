import unittest

from opcua import Client
from opcua import Server
from opcua import ua
from opcua.client.ua_client import UASocketClient
from opcua.common.utils import SocketWrapper

from tests_subscriptions import SubscriptionTests
from tests_common import CommonTests, add_server_methods
from tests_xml import XmlTests

from tests_enum_struct import add_server_custom_enum_struct

port_num1 = 48510


class TestClient(unittest.TestCase, CommonTests, SubscriptionTests, XmlTests):

    '''
    Run common tests on client side
    Of course we need a server so we start also start a server
    Tests that can only be run on client side must be defined  in this class
    '''
    @classmethod
    def setUpClass(cls):
        # start our own server
        cls.srv = Server()
        cls.srv.set_endpoint('opc.tcp://127.0.0.1:{0:d}'.format(port_num1))
        add_server_methods(cls.srv)
        add_server_custom_enum_struct(cls.srv)
        cls.srv.start()

        # start admin client
        # long timeout since travis (automated testing) can be really slow
        cls.clt = Client('opc.tcp://admin@127.0.0.1:{0:d}'.format(port_num1), timeout=10)
        cls.clt.connect()
        cls.opc = cls.clt

        # start anonymous client
        cls.ro_clt = Client('opc.tcp://127.0.0.1:{0:d}'.format(port_num1))
        cls.ro_clt.connect()

    @classmethod
    def tearDownClass(cls):
        #stop our clients
        cls.ro_clt.disconnect()
        cls.clt.disconnect()
        # stop the server
        cls.srv.stop()

    def test_service_fault(self):
        request = ua.ReadRequest()
        request.TypeId = ua.FourByteNodeId(999)  # bad type!
        with self.assertRaises(ua.UaStatusCodeError):
            self.clt.uaclient._uasocket.send_request(request)

    def test_objects_anonymous(self):
        objects = self.ro_clt.get_objects_node()
        with self.assertRaises(ua.UaStatusCodeError):
            objects.set_attribute(ua.AttributeIds.WriteMask, ua.DataValue(999))
        with self.assertRaises(ua.UaStatusCodeError):
            f = objects.add_folder(3, 'MyFolder')

    def test_folder_anonymous(self):
        objects = self.clt.get_objects_node()
        f = objects.add_folder(3, 'MyFolderRO')
        f_ro = self.ro_clt.get_node(f.nodeid)
        self.assertEqual(f, f_ro)
        with self.assertRaises(ua.UaStatusCodeError):
            f2 = f_ro.add_folder(3, 'MyFolder2')

    def test_variable_anonymous(self):
        objects = self.clt.get_objects_node()
        v = objects.add_variable(3, 'MyROVariable', 6)
        v.set_value(4)  # this should work
        v_ro = self.ro_clt.get_node(v.nodeid)
        with self.assertRaises(ua.UaStatusCodeError):
            v_ro.set_value(2)
        self.assertEqual(v_ro.get_value(), 4)
        v.set_writable(True)
        v_ro.set_value(2)  # now it should work
        self.assertEqual(v_ro.get_value(), 2)
        v.set_writable(False)
        with self.assertRaises(ua.UaStatusCodeError):
            v_ro.set_value(9)
        self.assertEqual(v_ro.get_value(), 2)

    def test_multiple_read_and_write(self):
        objects = self.srv.get_objects_node()
        f = objects.add_folder(3, 'Multiple_read_write_test')
        v1 = f.add_variable(3, "a", 1)
        v1.set_writable()
        v2 = f.add_variable(3, "b", 2)
        v2.set_writable()
        v3 = f.add_variable(3, "c", 3)
        v3.set_writable()
        v_ro = f.add_variable(3, "ro", 3)

        vals = self.ro_clt.get_values([v1, v2, v3])
        self.assertEqual(vals, [1, 2, 3])
        self.ro_clt.set_values([v1, v2, v3], [4, 5, 6])
        vals = self.ro_clt.get_values([v1, v2, v3])
        self.assertEqual(vals, [4, 5, 6])
        with self.assertRaises(ua.uaerrors.BadUserAccessDenied):
            self.ro_clt.set_values([v1, v2, v_ro], [4, 5, 6])

    def test_context_manager(self):
        """ Context manager calls connect() and disconnect()
        """
        state = [0]
        def increment_state(self, *args, **kwargs):
            state[0] += 1

        # create client and replace instance methods with dummy methods
        client = Client('opc.tcp://dummy_address:10000')
        client.connect    = increment_state.__get__(client)
        client.disconnect = increment_state.__get__(client)

        assert state[0] == 0
        with client:
            # test if client connected
            self.assertEqual(state[0], 1)
        # test if client disconnected
        self.assertEqual(state[0], 2)

    def test_enumstrings_getvalue(self):
        ''' The real exception is server side, but is detected by using a client.
            Alldue the server trace is also visible on the console.
            The client only 'sees' an TimeoutError
        '''
        nenumstrings = self.clt.get_node(ua.ObjectIds.AxisScaleEnumeration_EnumStrings)
        with self.assertNotRaises(Exception):
            value = ua.Variant(nenumstrings.get_value())

    def test_uasocketclient_connect_disconnect(self):
        """Initialize, connect, and disconnect a UaSocketClient
        """
        uaclt = UASocketClient()
        uaclt.connect_socket('127.0.0.1', port_num1)
        self.assertTrue(uaclt._thread.is_alive())
        self.assertIsInstance(uaclt._socket, SocketWrapper)

        # disconnect_socket() should shut down the receiving thread
        uaclt.disconnect_socket()
        self.assertFalse(uaclt._thread.is_alive())

    def test_custom_enum_struct(self):
        self.ro_clt.load_type_definitions()
        ns = self.ro_clt.get_namespace_index('http://yourorganisation.org/struct_enum_example/')
        myvar = self.ro_clt.get_node(ua.NodeId(6009, ns))
        val = myvar.get_value()
        self.assertEqual(val.IntVal1, 242)
        self.assertEqual(val.EnumVal, ua.ExampleEnum.EnumVal2)
