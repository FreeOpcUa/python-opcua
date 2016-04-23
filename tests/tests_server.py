import unittest
from tests_common import CommonTests, add_server_methods
import time
from datetime import timedelta

from opcua import Server
from opcua import Client
from opcua import ua
from opcua import uamethod


port_num = 485140
port_discovery = 48550


class TestServer(unittest.TestCase, CommonTests):

    '''
    Run common tests on server side
    Tests that can only be run on server side must be defined here
    '''
    @classmethod
    def setUpClass(self):
        self.srv = Server()
        self.srv.set_endpoint('opc.tcp://localhost:%d' % port_num)
        add_server_methods(self.srv)
        self.srv.start()
        self.opc = self.srv
        self.discovery = Server()
        self.discovery.set_application_uri("urn:freeopcua:python:discovery")
        self.discovery.set_endpoint('opc.tcp://localhost:%d' % port_discovery)
        self.discovery.start()

    @classmethod
    def tearDownClass(self):
        self.srv.stop()
        self.discovery.stop()

    def test_discovery(self):
        client = Client(self.discovery.endpoint.geturl())
        client.connect()
        try:
            servers = client.find_servers()
            new_app_uri = "urn:freeopcua:python:server:test_discovery"
            self.srv.application_uri = new_app_uri
            self.srv.register_to_discovery(self.discovery.endpoint.geturl(), 0)
            time.sleep(0.1) # let server register registration
            new_servers = client.find_servers()
            self.assertEqual(len(new_servers) - len(servers) , 1)
            self.assertFalse(new_app_uri in [s.ApplicationUri for s in servers])
            self.assertTrue(new_app_uri in [s.ApplicationUri for s in new_servers])
        finally:
            client.disconnect()

    def test_find_servers2(self):
        client = Client(self.discovery.endpoint.geturl())
        client.connect()
        try:
            servers = client.find_servers()
            new_app_uri1 = "urn:freeopcua:python:server:test_discovery1"
            self.srv.application_uri = new_app_uri1
            self.srv.register_to_discovery(self.discovery.endpoint.geturl(), period=0)
            new_app_uri2 = "urn:freeopcua:python:test_discovery2"
            self.srv.application_uri = new_app_uri2
            self.srv.register_to_discovery(self.discovery.endpoint.geturl(), period=0)
            time.sleep(0.1) # let server register registration
            new_servers = client.find_servers()
            self.assertEqual(len(new_servers) - len(servers) , 2)
            self.assertFalse(new_app_uri1 in [s.ApplicationUri for s in servers])
            self.assertFalse(new_app_uri2 in [s.ApplicationUri for s in servers])
            self.assertTrue(new_app_uri1 in [s.ApplicationUri for s in new_servers])
            self.assertTrue(new_app_uri2 in [s.ApplicationUri for s in new_servers])
            # now do a query with filer
            new_servers = client.find_servers(["urn:freeopcua:python:server"])
            self.assertEqual(len(new_servers) - len(servers) , 0)
            self.assertTrue(new_app_uri1 in [s.ApplicationUri for s in new_servers])
            self.assertFalse(new_app_uri2 in [s.ApplicationUri for s in new_servers])
            # now do a query with filer
            new_servers = client.find_servers(["urn:freeopcua:python"])
            self.assertEqual(len(new_servers) - len(servers) , 2)
            self.assertTrue(new_app_uri1 in [s.ApplicationUri for s in new_servers])
            self.assertTrue(new_app_uri2 in [s.ApplicationUri for s in new_servers])
        finally:
            client.disconnect()


    """
    # not sure if this test is necessary, and there is a lot repetition with previous test
    def test_discovery_server_side(self):
        servers = self.discovery.find_servers()
        self.assertEqual(len(servers), 1)
        self.srv.register_to_discovery(self.discovery.endpoint.geturl(), 1)
        time.sleep(1) # let server register registration
        servers = self.discovery.find_servers()
        print("SERVERS 2", servers)
        self.assertEqual(len(servers), 2)
    """
    #def test_register_server2(self):
        #servers = self.opc.register_server()

    def test_register_namespace(self):
        uri = 'http://mycustom.Namespace.com'
        idx1 = self.opc.register_namespace(uri)
        idx2 = self.opc.get_namespace_index(uri)
        self.assertEqual(idx1, idx2)

    def test_register_use_namespace(self):
        uri = 'http://my_very_custom.Namespace.com'
        idx = self.opc.register_namespace(uri)
        root = self.opc.get_root_node()
        myvar = root.add_variable(idx, 'var_in_custom_namespace', [5])
        myid = myvar.nodeid
        self.assertEqual(idx, myid.NamespaceIndex)

    def test_server_method(self):
        def func(parent, variant):
            variant.Value *= 2
            return [variant]
        o = self.opc.get_objects_node()
        v = o.add_method(3, 'Method1', func, [ua.VariantType.Int64], [ua.VariantType.Int64])
        result = o.call_method(v, ua.Variant(2.1))
        self.assertEqual(result, 4.2)

    def test_xml_import(self):
        self.srv.import_xml("tests/custom_nodes.xml")
        o = self.opc.get_objects_node()
        v = o.get_child(["MyXMLFolder", "MyXMLObject", "MyXMLVariable"])
        val = v.get_value()
        self.assertEqual(val, "StringValue")

    def test_historize(self):
        o = self.opc.get_objects_node()
        var = o.add_variable(3, "test_hist", 1.0)
        self.srv.iserver.enable_history(var, timedelta(days=1))
        time.sleep(1)
        var.set_value(2.0)
        var.set_value(3.0)
        self.srv.iserver.disable_history(var)

    def test_references_for_added_nodes_method(self):
        objects = self.opc.get_objects_node()
        o = objects.add_object(3, 'MyObject')
        nodes = objects.get_referenced_nodes(refs=ua.ObjectIds.Organizes, direction=ua.BrowseDirection.Forward, includesubtypes=False)
        self.assertTrue(o in nodes)
        nodes = o.get_referenced_nodes(refs=ua.ObjectIds.Organizes, direction=ua.BrowseDirection.Inverse, includesubtypes=False)
        self.assertTrue(objects in nodes)
        self.assertEqual(o.get_parent(), objects)
        self.assertEqual(o.get_type_definition(), ua.ObjectIds.BaseObjectType)

        @uamethod
        def callback(parent):
            return

        m = o.add_method(3, 'MyMethod', callback)
        nodes = o.get_referenced_nodes(refs=ua.ObjectIds.HasComponent, direction=ua.BrowseDirection.Forward, includesubtypes=False)
        self.assertTrue(m in nodes)
        nodes = m.get_referenced_nodes(refs=ua.ObjectIds.HasComponent, direction=ua.BrowseDirection.Inverse, includesubtypes=False)
        self.assertTrue(o in nodes)
        self.assertEqual(m.get_parent(), o)
