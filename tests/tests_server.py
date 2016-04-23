import unittest
from tests_common import CommonTests, add_server_methods, MySubHandler
import time
from datetime import timedelta

import opcua
from opcua import Server
from opcua import Client
from opcua import ua


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

    # This should work for following BaseEvent tests to work (maybe to write it a bit differentlly since they are not independent)
    def test_get_event_from_node_BaseEvent(self):
        ev = opcua.common.event.get_event_from_node(opcua.Node(self.opc.iserver.isession, ua.NodeId(ua.ObjectIds.BaseEventType)))
        check_base_event(self, ev)

    def test_get_event_from_node_CustomEvent(self):
        ev = opcua.common.event.get_event_from_node(opcua.Node(self.opc.iserver.isession, ua.NodeId(ua.ObjectIds.AuditEventType)))
        check_base_event(self, ev)

    #def test_get_event_from_node_InheritanceEvent(self):
        #ev = opcua.common.event.get_event_from_node(opcua.Node(self.opc.iserver.isession, ua.NodeId(ua.ObjectIds.AuditEventType)))
        #self.assertIsNot(ev, None)  # we did not receive event
        #self.assertIsInstance(ev, ua.BaseEvent)
        #self.assertIsInstance(ev, ua.AuditEventType)
        #self.assertEqual(ev.EventType, ua.NodeId(ua.ObjectIds.AuditEventType))
        #self.assertEqual(ev.SourceNode, ua.NodeId(ua.ObjectIds.Server))
        #self.assertEqual(ev.Severity, ua.Variant(1, ua.VariantType.UInt16))
        #self.assertEqual(ev._freeze, True)

    def test_eventgenerator_default(self):
        evgen = self.opc.get_event_generator()
        check_eventgenerator_BaseEvent(self, evgen)

    def test_eventgenerator_BaseEvent_object(self):
        evgen = self.opc.get_event_generator(ua.BaseEvent())
        check_eventgenerator_BaseEvent(self, evgen)

    def test_eventgenerator_BaseEvent_Node(self):
        evgen = self.opc.get_event_generator(opcua.Node(self.opc.iserver.isession, ua.NodeId(ua.ObjectIds.BaseEventType)))
        check_eventgenerator_BaseEvent(self, evgen)

    def test_eventgenerator_BaseEvent_NodeId(self):
        evgen = self.opc.get_event_generator(ua.NodeId(ua.ObjectIds.BaseEventType))
        check_eventgenerator_BaseEvent(self, evgen)

    def test_eventgenerator_BaseEvent_ObjectIds(self):
        evgen = self.opc.get_event_generator(ua.ObjectIds.BaseEventType)
        check_eventgenerator_BaseEvent(self, evgen)

    def test_eventgenerator_BaseEvent_Identifier(self):
        evgen = self.opc.get_event_generator(2041)
        check_eventgenerator_BaseEvent(self, evgen)

    def test_eventgenerator_sourceServer_Node(self):
        pass

    def test_eventgenerator_sourceServer_NodeId(self):
        pass

    def test_eventgenerator_sourceServer_ObjectIds(self):
        pass

    def test_eventgenerator_CustomEvent_object(self):
        pass

    def test_eventgenerator_CustomEvent_Node(self):
        pass

    def test_eventgenerator_CustomEvent_NodeId(self):
        pass

    def test_eventgenerator_CustomEvent_ObjectIds(self):
        pass

    #def test_eventgenerator_InheritedEvent(self):
        #pass



    #def test_events_default(self):
        #msclt = MySubHandler()
        #sub = self.opc.create_subscription(100, msclt)
        #handle = sub.subscribe_events()

        #ev = EventGenerator(self.srv.iserver.isession)
        #msg = b"this is my msg "
        #ev.Message.Text = msg
        #tid = datetime.utcnow()
        #ev.Time = tid
        #ev.Severity = 500
        #ev.trigger()

        #ev = msclt.future.result()
        #self.assertIsNot(ev, None)  # we did not receive event
        #self.assertEqual(ev.SourceNode, self.opc.get_server_node().nodeid)
        #self.assertEqual(ev.Message.Text, msg)
        ##self.assertEqual(msclt.ev.Time, tid)
        #self.assertEqual(ev.Severity, 500)

        ## time.sleep(0.1)
        #sub.unsubscribe(handle)
        #sub.delete()


def check_eventgenerator_BaseEvent(test, evgen):
    test.assertIsNot(evgen, None)  # we did not receive event generator
    test.assertIs(evgen.isession, test.opc.iserver.isession)
    check_base_event(test, evgen.event)
    test.assertEqual(evgen.event.SourceName, test.opc.get_server_node().get_display_name().Text)
    test.assertEqual(test.opc.get_server_node().get_attribute(ua.AttributeIds.EventNotifier).Value, ua.Variant(1, ua.VariantType.Byte))


def check_base_event(test, ev):
    test.assertIsNot(ev, None)  # we did not receive event
    test.assertIsInstance(ev, ua.BaseEvent)
    test.assertEqual(ev.EventType, ua.NodeId(ua.ObjectIds.BaseEventType))
    test.assertEqual(ev.SourceNode, ua.NodeId(ua.ObjectIds.Server))
    test.assertEqual(ev.Severity, ua.Variant(1, ua.VariantType.UInt16))
    test.assertEqual(ev._freeze, True)
