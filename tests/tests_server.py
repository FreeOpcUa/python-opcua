import unittest
import os
import shelve
import time

from tests_common import CommonTests, add_server_methods
from tests_subscriptions import SubscriptionTests
from datetime import timedelta, datetime
from tempfile import NamedTemporaryFile

import opcua
from opcua import Server
from opcua import Client
from opcua import ua
from opcua import uamethod
from opcua.common.event_objects import BaseEvent, AuditEvent


port_num = 485140
port_discovery = 48550


class TestServer(unittest.TestCase, CommonTests, SubscriptionTests):

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

    def test_historize_variable(self):
        o = self.opc.get_objects_node()
        var = o.add_variable(3, "test_hist", 1.0)
        self.srv.iserver.enable_history_data_change(var, timedelta(days=1))
        time.sleep(1)
        var.set_value(2.0)
        var.set_value(3.0)
        self.srv.iserver.disable_history_data_change(var)

    def test_historize_events(self):
        srv_node = self.srv.get_node(ua.ObjectIds.Server)
        srvevgen = self.srv.get_event_generator()
        self.srv.iserver.enable_history_event(srv_node, period=None)
        srvevgen.trigger(message="Message")
        self.srv.iserver.disable_history_event(srv_node)

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

    # This should work for following BaseEvent tests to work (maybe to write it a bit differentlly since they are not independent)
    def test_get_event_from_type_node_BaseEvent(self):
        ev = opcua.common.events.get_event_obj_from_type_node(opcua.Node(self.opc.iserver.isession, ua.NodeId(ua.ObjectIds.BaseEventType)))
        check_base_event(self, ev)

    def test_get_event_from_type_node_Inhereted_AuditEvent(self):
        ev = opcua.common.events.get_event_obj_from_type_node(opcua.Node(self.opc.iserver.isession, ua.NodeId(ua.ObjectIds.AuditEventType)))
        self.assertIsNot(ev, None)  # we did not receive event
        self.assertIsInstance(ev, BaseEvent)
        self.assertIsInstance(ev, AuditEvent)
        self.assertEqual(ev.EventType, ua.NodeId(ua.ObjectIds.AuditEventType))
        self.assertEqual(ev.Severity, 1)
        self.assertEqual(ev.ActionTimeStamp, None)
        self.assertEqual(ev.Status, False)
        self.assertEqual(ev.ServerId, None)
        self.assertEqual(ev.ClientAuditEntryId, None)
        self.assertEqual(ev.ClientUserId, None)

    def test_eventgenerator_default(self):
        evgen = self.opc.get_event_generator()
        check_eventgenerator_BaseEvent(self, evgen)
        check_eventgenerator_SourceServer(self, evgen)

    def test_eventgenerator_BaseEvent_object(self):
        evgen = self.opc.get_event_generator(BaseEvent())
        check_eventgenerator_BaseEvent(self, evgen)
        check_eventgenerator_SourceServer(self, evgen)

    def test_eventgenerator_BaseEvent_Node(self):
        evgen = self.opc.get_event_generator(opcua.Node(self.opc.iserver.isession, ua.NodeId(ua.ObjectIds.BaseEventType)))
        check_eventgenerator_BaseEvent(self, evgen)
        check_eventgenerator_SourceServer(self, evgen)

    def test_eventgenerator_BaseEvent_NodeId(self):
        evgen = self.opc.get_event_generator(ua.NodeId(ua.ObjectIds.BaseEventType))
        check_eventgenerator_BaseEvent(self, evgen)
        check_eventgenerator_SourceServer(self, evgen)

    def test_eventgenerator_BaseEvent_ObjectIds(self):
        evgen = self.opc.get_event_generator(ua.ObjectIds.BaseEventType)
        check_eventgenerator_BaseEvent(self, evgen)
        check_eventgenerator_SourceServer(self, evgen)

    def test_eventgenerator_BaseEvent_Identifier(self):
        evgen = self.opc.get_event_generator(2041)
        check_eventgenerator_BaseEvent(self, evgen)
        check_eventgenerator_SourceServer(self, evgen)

    def test_eventgenerator_sourceServer_Node(self):
        evgen = self.opc.get_event_generator(source=opcua.Node(self.opc.iserver.isession, ua.NodeId(ua.ObjectIds.Server)))
        check_eventgenerator_BaseEvent(self, evgen)
        check_eventgenerator_SourceServer(self, evgen)

    def test_eventgenerator_sourceServer_NodeId(self):
        evgen = self.opc.get_event_generator(source=ua.NodeId(ua.ObjectIds.Server))
        check_eventgenerator_BaseEvent(self, evgen)
        check_eventgenerator_SourceServer(self, evgen)

    def test_eventgenerator_sourceServer_ObjectIds(self):
        evgen = self.opc.get_event_generator(source=ua.ObjectIds.Server)
        check_eventgenerator_BaseEvent(self, evgen)
        check_eventgenerator_SourceServer(self, evgen)

    def test_eventgenerator_sourceMyObject(self):
        objects = self.opc.get_objects_node()
        o = objects.add_object(3, 'MyObject')
        evgen = self.opc.get_event_generator(source=o)
        check_eventgenerator_BaseEvent(self, evgen)
        check_event_generator_object(self, evgen, o)

    def test_eventgenerator_source_collision(self):
        objects = self.opc.get_objects_node()
        o = objects.add_object(3, 'MyObject')
        event = BaseEvent(sourcenode=o.nodeid)
        evgen = self.opc.get_event_generator(event, ua.ObjectIds.Server)
        check_eventgenerator_BaseEvent(self, evgen)
        check_event_generator_object(self, evgen, o)

    def test_eventgenerator_InheritedEvent(self):
        evgen = self.opc.get_event_generator(ua.ObjectIds.AuditEventType)
        check_eventgenerator_SourceServer(self, evgen)

        ev = evgen.event
        self.assertIsNot(ev, None)  # we did not receive event
        self.assertIsInstance(ev, BaseEvent)
        self.assertIsInstance(ev, AuditEvent)
        self.assertEqual(ev.EventType, ua.NodeId(ua.ObjectIds.AuditEventType))
        self.assertEqual(ev.Severity, 1)
        self.assertEqual(ev.ActionTimeStamp, None)
        self.assertEqual(ev.Status, False)
        self.assertEqual(ev.ServerId, None)
        self.assertEqual(ev.ClientAuditEntryId, None)
        self.assertEqual(ev.ClientUserId, None)

    def test_create_custom_event_type_ObjectId(self):
        etype = self.opc.create_custom_event_type(2, 'MyEvent', ua.ObjectIds.BaseEventType, [('PropertyNum', ua.VariantType.Float), ('PropertyString', ua.VariantType.String)])
        check_custom_event_type(self, etype)

    def test_create_custom_event_type_NodeId(self):
        etype = self.opc.create_custom_event_type(2, 'MyEvent', ua.NodeId(ua.ObjectIds.BaseEventType), [('PropertyNum', ua.VariantType.Float), ('PropertyString', ua.VariantType.String)])
        check_custom_event_type(self, etype)

    def test_create_custom_event_type_Node(self):
        etype = self.opc.create_custom_event_type(2, 'MyEvent', opcua.Node(self.opc.iserver.isession, ua.NodeId(ua.ObjectIds.BaseEventType)), [('PropertyNum', ua.VariantType.Float), ('PropertyString', ua.VariantType.String)])
        check_custom_event_type(self, etype)

    def test_get_event_from_type_node_CustomEvent(self):
        etype = self.opc.create_custom_event_type(2, 'MyEvent', ua.ObjectIds.BaseEventType, [('PropertyNum', ua.VariantType.Float), ('PropertyString', ua.VariantType.String)])

        ev = opcua.common.events.get_event_obj_from_type_node(etype)
        check_custom_event(self, ev, etype)
        self.assertEqual(ev.PropertyNum, None)
        self.assertEqual(ev.PropertyString, None)

    def test_eventgenerator_customEvent(self):
        etype = self.opc.create_custom_event_type(2, 'MyEvent', ua.ObjectIds.BaseEventType, [('PropertyNum', ua.VariantType.Float), ('PropertyString', ua.VariantType.String)])

        evgen = self.opc.get_event_generator(etype, ua.ObjectIds.Server)
        check_eventgenerator_CustomEvent(self, evgen, etype)
        check_eventgenerator_SourceServer(self, evgen)

        self.assertEqual(evgen.event.PropertyNum, None)
        self.assertEqual(evgen.event.PropertyString, None)

    def test_eventgenerator_double_customEvent(self):
        event1 = self.opc.create_custom_event_type(3, 'MyEvent1', ua.ObjectIds.BaseEventType, [('PropertyNum', ua.VariantType.Float), ('PropertyString', ua.VariantType.String)])

        event2 = self.opc.create_custom_event_type(4, 'MyEvent2', event1, [('PropertyBool', ua.VariantType.Boolean), ('PropertyInt', ua.VariantType.Int32)])

        evgen = self.opc.get_event_generator(event2, ua.ObjectIds.Server)
        check_eventgenerator_CustomEvent(self, evgen, event2)
        check_eventgenerator_SourceServer(self, evgen)

        # Properties from MyEvent1
        self.assertEqual(evgen.event.PropertyNum, None)
        self.assertEqual(evgen.event.PropertyString, None)

         # Properties from MyEvent2
        self.assertEqual(evgen.event.PropertyBool, None)
        self.assertEqual(evgen.event.PropertyInt, None)

    def test_eventgenerator_customEvent_MyObject(self):
        objects = self.opc.get_objects_node()
        o = objects.add_object(3, 'MyObject')
        etype = self.opc.create_custom_event_type(2, 'MyEvent', ua.ObjectIds.BaseEventType, [('PropertyNum', ua.VariantType.Float), ('PropertyString', ua.VariantType.String)])

        evgen = self.opc.get_event_generator(etype, o)
        check_eventgenerator_CustomEvent(self, evgen, etype)
        check_event_generator_object(self, evgen, o)

        self.assertEqual(evgen.event.PropertyNum, None)
        self.assertEqual(evgen.event.PropertyString, None)


def check_eventgenerator_SourceServer(test, evgen):
    server = test.opc.get_server_node()
    test.assertEqual(evgen.event.SourceName, server.get_browse_name().Name)
    test.assertEqual(evgen.event.SourceNode, ua.NodeId(ua.ObjectIds.Server))
    test.assertEqual(server.get_attribute(ua.AttributeIds.EventNotifier).Value, ua.Variant(1, ua.VariantType.Byte))
    refs = server.get_referenced_nodes(ua.ObjectIds.GeneratesEvent, ua.BrowseDirection.Forward, ua.NodeClass.ObjectType, False)
    test.assertGreaterEqual(len(refs), 1)


def check_event_generator_object(test, evgen, obj):
    test.assertEqual(evgen.event.SourceName, obj.get_browse_name().Name)
    test.assertEqual(evgen.event.SourceNode, obj.nodeid)
    test.assertEqual(obj.get_attribute(ua.AttributeIds.EventNotifier).Value, ua.Variant(1, ua.VariantType.Byte))
    refs = obj.get_referenced_nodes(ua.ObjectIds.GeneratesEvent, ua.BrowseDirection.Forward, ua.NodeClass.ObjectType, False)
    test.assertEqual(len(refs), 1)
    test.assertEqual(refs[0].nodeid, evgen.event.EventType)


def check_eventgenerator_BaseEvent(test, evgen):
    test.assertIsNot(evgen, None)  # we did not receive event generator
    test.assertIs(evgen.isession, test.opc.iserver.isession)
    check_base_event(test, evgen.event)


def check_base_event(test, ev):
    test.assertIsNot(ev, None)  # we did not receive event
    test.assertIsInstance(ev, BaseEvent)
    test.assertEqual(ev.EventType, ua.NodeId(ua.ObjectIds.BaseEventType))
    test.assertEqual(ev.Severity, 1)


def check_eventgenerator_CustomEvent(test, evgen, etype):
    test.assertIsNot(evgen, None)  # we did not receive event generator
    test.assertIs(evgen.isession, test.opc.iserver.isession)
    check_custom_event(test, evgen.event, etype)


def check_custom_event(test, ev, etype):
    test.assertIsNot(ev, None)  # we did not receive event
    test.assertIsInstance(ev, BaseEvent)
    test.assertEqual(ev.EventType, etype.nodeid)
    test.assertEqual(ev.Severity, 1)


def check_custom_event_type(test, ev):
    base = opcua.Node(test.opc.iserver.isession, ua.NodeId(ua.ObjectIds.BaseEventType))
    test.assertTrue(ev in base.get_children())
    nodes = ev.get_referenced_nodes(refs=ua.ObjectIds.HasSubtype, direction=ua.BrowseDirection.Inverse, includesubtypes=False)
    test.assertEqual(base, nodes[0])
    properties = ev.get_properties()
    test.assertIsNot(properties, None)
    test.assertEqual(len(properties), 2)
    test.assertTrue(ev.get_child("2:PropertyNum") in properties)
    test.assertEqual(ev.get_child("2:PropertyNum").get_data_value().Value.VariantType, ua.VariantType.Float)
    test.assertTrue(ev.get_child("2:PropertyString") in properties)
    test.assertEqual(ev.get_child("2:PropertyString").get_data_value().Value.VariantType, ua.VariantType.String)


class TestServerCaching(unittest.TestCase):
    def runTest(self):
        tmpfile = NamedTemporaryFile()
        path = tmpfile.name
        tmpfile.close()

        # create cache file
        server = Server(cacheFile=path)

        # modify cache content
        id = ua.NodeId(ua.ObjectIds.Server_ServerStatus_SecondsTillShutdown)
        s = shelve.open(path, "w", writeback=True)
        s[id.to_string()].attributes[ua.AttributeIds.Value].value = ua.DataValue(123)
        s.close()

        # ensure that we are actually loading from the cache
        server = Server(cacheFile=path)
        self.assertEqual(server.get_node(id).get_value(), 123)

        os.remove(path)
