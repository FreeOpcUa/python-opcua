import unittest

from opcua import Client
from opcua import Server
from opcua import ua

from tests_subscriptions import SubscriptionTests
from tests_common import CommonTests, add_server_methods
from tests_xml import XmlTests 

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
        cls.srv.set_endpoint('opc.tcp://localhost:{0:d}'.format(port_num1))
        add_server_methods(cls.srv)
        cls.srv.start()

        # start admin client
        # long timeout since travis (automated testing) can be really slow
        cls.clt = Client('opc.tcp://admin@localhost:{0:d}'.format(port_num1), timeout=10)
        cls.clt.connect()
        cls.opc = cls.clt

        # start anonymous client
        cls.ro_clt = Client('opc.tcp://localhost:{0:d}'.format(port_num1))
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
        v.set_value(4) #this should work
        v_ro = self.ro_clt.get_node(v.nodeid)
        with self.assertRaises(ua.UaStatusCodeError):
            v_ro.set_value(2)
        self.assertEqual(v_ro.get_value(), 4)
        v.set_writable(True)
        v_ro.set_value(2) #now it should work
        self.assertEqual(v_ro.get_value(), 2)
        v.set_writable(False)
        with self.assertRaises(ua.UaStatusCodeError):
            v_ro.set_value(9)
        self.assertEqual(v_ro.get_value(), 2)

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
