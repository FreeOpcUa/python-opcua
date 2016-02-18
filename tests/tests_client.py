import unittest

from opcua import Client
from opcua import Server
from opcua import ua

from tests_common import CommonTests, add_server_methods

port_num1 = 48510


class TestClient(unittest.TestCase, CommonTests):

    '''
    Run common tests on client side
    Of course we need a server so we start also start a server
    Tests that can only be run on client side must be defined  in this class
    '''
    @classmethod
    def setUpClass(self):
        # start our own server
        self.srv = Server()
        self.srv.set_endpoint('opc.tcp://localhost:%d' % port_num1)
        add_server_methods(self.srv)
        self.srv.start()

        # start admin client
        self.clt = Client('opc.tcp://admin@localhost:%d' % port_num1)
        self.clt.connect()
        self.opc = self.clt

        # start anonymous client
        self.ro_clt = Client('opc.tcp://localhost:%d' % port_num1)
        self.ro_clt.connect()



    @classmethod
    def tearDownClass(self):
        #stop our clients
        self.ro_clt.disconnect()
        self.clt.disconnect()
        # stop the server 
        self.srv.stop()

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


