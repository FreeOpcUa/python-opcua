# encoding: utf-8
from concurrent.futures import Future, TimeoutError
import time
from datetime import datetime
from datetime import timedelta
import math

import opcua
from opcua import ua
from opcua import uamethod


def add_server_methods(srv):
    @uamethod
    def func(parent, value):
        return value * 2

    o = srv.get_objects_node()
    v = o.add_method(ua.NodeId("ServerMethod", 2), ua.QualifiedName('ServerMethod', 2), func, [ua.VariantType.Int64], [ua.VariantType.Int64])

    @uamethod
    def func2(parent, methodname, value):
        return math.sin(value)

    o = srv.get_objects_node()
    v = o.add_method(ua.NodeId("ServerMethodArray", 2), ua.QualifiedName('ServerMethodArray', 2), func2, [ua.VariantType.String, ua.VariantType.Int64], [ua.VariantType.Int64])

    @uamethod
    def func3(parent, mylist):
        return [i * 2 for i in mylist]

    o = srv.get_objects_node()
    v = o.add_method(ua.NodeId("ServerMethodArray2", 2), ua.QualifiedName('ServerMethodArray2', 2), func3, [ua.VariantType.Int64], [ua.VariantType.Int64])


class SubHandler():

    '''
        Dummy subscription client
    '''

    def datachange_notification(self, node, val, data):
        pass

    def event_notification(self, event):
        pass


class MySubHandlerDeprecated():

    '''
    More advanced subscription client using Future, so we can wait for events in tests
    '''

    def __init__(self):
        self.future = Future()

    def reset(self):
        self.future = Future()

    def data_change(self, handle, node, val, attr):
        self.future.set_result((handle, node, val, attr))

    def event(self, handle, event):
        self.future.set_result((handle, event))

class MySubHandler():

    '''
    More advanced subscription client using Future, so we can wait for events in tests
    '''

    def __init__(self):
        self.future = Future()

    def reset(self):
        self.future = Future()

    def datachange_notification(self, node, val, data):
        self.future.set_result((node, val, data))

    def event_notification(self, event):
        self.future.set_result(event)


class MySubHandler2():
    def __init__(self):
        self.results = []

    def datachange_notification(self, node, val, data):
        self.results.append((node, val))

    def event_notification(self, event):
        self.results.append(event)


class MySubHandlerCounter():
    def __init__(self):
        self.datachange_count = 0
        self.event_count = 0

    def datachange_notification(self, node, val, data):
        self.datachange_count += 1

    def event_notification(self, event):
        self.event_count += 1


class CommonTests(object):

    '''
    Tests that will be run twice. Once on server side and once on
    client side since we have been carefull to have the exact
    same api on server and client side
    '''
    # jyst to avoid editor warnings
    opc = None
    assertEqual = lambda x, y: True
    assertIn = lambda x, y: True

    def test_find_servers(self):
        servers = self.opc.find_servers()
        # FIXME : finish

    def test_add_node_bad_args(self):
        obj = self.opc.get_objects_node()

        with self.assertRaises(TypeError):
            fold = obj.add_folder(1.2, "kk")

        with self.assertRaises(TypeError):
            fold = obj.add_folder(ua.UaError, "khjh")

        with self.assertRaises(ua.UaError):
            fold = obj.add_folder("kjk", 1.2)

        with self.assertRaises(TypeError):
            fold = obj.add_folder("i=0;s='oooo'", 1.2)

        with self.assertRaises(ua.UaError):
            fold = obj.add_folder("i=0;s='oooo'", "tt:oioi")

    def test_delete_nodes(self):
        obj = self.opc.get_objects_node()
        fold = obj.add_folder(2, "FolderToDelete")
        var = fold.add_variable(2, "VarToDelete", 9.1)
        childs = fold.get_children()
        self.assertIn(var, childs)
        self.opc.delete_nodes([var])
        with self.assertRaises(ua.UaStatusCodeError):
            var.set_value(7.8)
        with self.assertRaises(ua.UaStatusCodeError):
            obj.get_child(["2:FolderToDelete", "2:VarToDelete"])
        childs = fold.get_children()
        self.assertNotIn(var, childs)

    def test_delete_nodes_recursive(self):
        obj = self.opc.get_objects_node()
        fold = obj.add_folder(2, "FolderToDeleteR")
        var = fold.add_variable(2, "VarToDeleteR", 9.1)
        self.opc.delete_nodes([fold, var])
        with self.assertRaises(ua.UaStatusCodeError):
            var.set_value(7.8)
        with self.assertRaises(ua.UaStatusCodeError):
            obj.get_child(["2:FolderToDelete", "2:VarToDelete"])

    def test_delete_nodes_recursive2(self):
        obj = self.opc.get_objects_node()
        fold = obj.add_folder(2, "FolderToDeleteRoot")
        nfold = fold
        mynodes = []
        for i in range(7):
            nfold = fold.add_folder(2, "FolderToDeleteRoot")
            var = fold.add_variable(2, "VarToDeleteR", 9.1)
            var = fold.add_property(2, "ProToDeleteR", 9.1)
            prop = fold.add_property(2, "ProToDeleteR", 9.1)
            o = fold.add_object(3, "ObjToDeleteR")
            mynodes.append(nfold)
            mynodes.append(var)
            mynodes.append(prop)
            mynodes.append(o)
        self.opc.delete_nodes([fold], recursive=True)
        for node in mynodes:
            with self.assertRaises(ua.UaStatusCodeError):
                node.get_browse_name()

    def test_server_node(self):
        node = self.opc.get_server_node()
        self.assertEqual(ua.QualifiedName('Server', 0), node.get_browse_name())

    def test_root(self):
        root = self.opc.get_root_node()
        self.assertEqual(ua.QualifiedName('Root', 0), root.get_browse_name())
        self.assertEqual(ua.LocalizedText('Root'), root.get_display_name())
        nid = ua.NodeId(84, 0)
        self.assertEqual(nid, root.nodeid)

    def test_objects(self):
        objects = self.opc.get_objects_node()
        self.assertEqual(ua.QualifiedName('Objects', 0), objects.get_browse_name())
        nid = ua.NodeId(85, 0)
        self.assertEqual(nid, objects.nodeid)

    def test_browse(self):
        objects = self.opc.get_objects_node()
        obj = objects.add_object(4, "browsetest")
        folder = obj.add_folder(4, "folder")
        prop = obj.add_property(4, "property", 1)
        prop2 = obj.add_property(4, "property2", 2)
        var = obj.add_variable(4, "variable", 3)
        obj2 = obj.add_object(4, "obj")
        alle = obj.get_children()
        self.assertTrue(prop in alle)
        self.assertTrue(prop2 in alle)
        self.assertTrue(var in alle)
        self.assertTrue(folder in alle)
        self.assertFalse(obj in alle)
        props = obj.get_children(refs=ua.ObjectIds.HasProperty)
        self.assertTrue(prop in props)
        self.assertTrue(prop2 in props)
        self.assertFalse(var in props)
        self.assertFalse(folder in props)
        self.assertFalse(obj2 in props)
        all_vars = obj.get_children(nodeclassmask=ua.NodeClass.Variable)
        self.assertTrue(prop in all_vars)
        self.assertTrue(var in all_vars)
        self.assertFalse(folder in props)
        self.assertFalse(obj2 in props)
        all_objs = obj.get_children(nodeclassmask=ua.NodeClass.Object)
        self.assertTrue(folder in all_objs)
        self.assertTrue(obj2 in all_objs)
        self.assertFalse(var in all_objs)

    def test_browse_references(self):
        objects = self.opc.get_objects_node()
        folder = objects.add_folder(4, "folder")

        childs = objects.get_referenced_nodes(refs=ua.ObjectIds.Organizes, direction=ua.BrowseDirection.Forward, includesubtypes=False)
        self.assertTrue(folder in childs)

        childs = objects.get_referenced_nodes(refs=ua.ObjectIds.Organizes, direction=ua.BrowseDirection.Both, includesubtypes=False)
        self.assertTrue(folder in childs)

        childs = objects.get_referenced_nodes(refs=ua.ObjectIds.Organizes, direction=ua.BrowseDirection.Inverse, includesubtypes=False)
        self.assertFalse(folder in childs)

        parents = folder.get_referenced_nodes(refs=ua.ObjectIds.Organizes, direction=ua.BrowseDirection.Inverse, includesubtypes=False)
        self.assertTrue(objects in parents)

        parents = folder.get_referenced_nodes(refs=ua.ObjectIds.HierarchicalReferences, direction=ua.BrowseDirection.Inverse, includesubtypes=False)
        self.assertFalse(objects in parents)

        parents = folder.get_referenced_nodes(refs=ua.ObjectIds.HierarchicalReferences, direction=ua.BrowseDirection.Inverse, includesubtypes=True)
        self.assertTrue(objects in parents)

        parent = folder.get_parent()
        self.assertEqual(parent, objects)

    def test_browsename_with_spaces(self):
        o = self.opc.get_objects_node()
        v = o.add_variable(3, 'BNVariable with spaces and %&+?/', 1.3)
        v2 = o.get_child("3:BNVariable with spaces and %&+?/")
        self.assertEqual(v, v2)

    def test_create_delete_subscription(self):
        o = self.opc.get_objects_node()
        v = o.add_variable(3, 'SubscriptionVariable', [1, 2, 3])
        sub = self.opc.create_subscription(100, MySubHandler())
        handle = sub.subscribe_data_change(v)
        time.sleep(0.1)
        sub.unsubscribe(handle)
        sub.delete()

    def test_subscribe_events(self):
        sub = self.opc.create_subscription(100, MySubHandler())
        handle = sub.subscribe_events()
        time.sleep(0.1)
        sub.unsubscribe(handle)
        sub.delete()

    def test_subscribe_events_to_wrong_node(self):
        sub = self.opc.create_subscription(100, MySubHandler())
        with self.assertRaises(ua.UaStatusCodeError):
            handle = sub.subscribe_events(self.opc.get_node("i=85"))
        o = self.opc.get_objects_node()
        v = o.add_variable(3, 'VariableNoEventNofierAttribute', 4)
        with self.assertRaises(ua.UaStatusCodeError):
            handle = sub.subscribe_events(v)
        sub.delete()

    def test_get_event_from_type_node_BaseEvent(self):
        etype = self.opc.get_node(ua.ObjectIds.BaseEventType)
        properties = opcua.common.event.get_event_properties_from_type_node(etype)
        for child in etype.get_properties():
            self.assertTrue(child in properties)

    def test_get_event_from_type_node_CustomEvent(self):
        etype = self.srv.create_custom_event_type(2, 'MyEvent', ua.ObjectIds.AuditEventType, [('PropertyNum', ua.VariantType.Float), ('PropertyString', ua.VariantType.String)])

        properties = opcua.common.event.get_event_properties_from_type_node(etype)

        for child in self.opc.get_node(ua.ObjectIds.BaseEventType).get_properties():
            self.assertTrue(child in properties)
        for child in self.opc.get_node(ua.ObjectIds.AuditEventType).get_properties():
            self.assertTrue(child in properties)
        for child in self.opc.get_node(etype.nodeid).get_properties():
                self.assertTrue(child in properties)

        self.assertTrue(etype.get_child("2:PropertyNum") in properties)
        self.assertTrue(etype.get_child("2:PropertyString") in properties)

    def test_events_default(self):
        evgen = self.srv.get_event_generator()

        msclt = MySubHandler()
        sub = self.opc.create_subscription(100, msclt)
        handle = sub.subscribe_events()

        tid = datetime.utcnow()
        msg = b"this is my msg "
        evgen.trigger(tid, msg)

        ev = msclt.future.result()
        self.assertIsNot(ev, None)  # we did not receive event
        self.assertEqual(ev.EventType, ua.NodeId(ua.ObjectIds.BaseEventType))
        self.assertEqual(ev.Severity, 1)
        self.assertEqual(ev.SourceName, self.opc.get_server_node().get_display_name().Text)
        self.assertEqual(ev.SourceNode, self.opc.get_server_node().nodeid)
        self.assertEqual(ev.Message.Text, msg)
        self.assertEqual(ev.Time, tid)

        # time.sleep(0.1)
        sub.unsubscribe(handle)
        sub.delete()

    def test_events_MyObject(self):
        objects = self.srv.get_objects_node()
        o = objects.add_object(3, 'MyObject')
        evgen = self.srv.get_event_generator(source=o)

        msclt = MySubHandler()
        sub = self.opc.create_subscription(100, msclt)
        handle = sub.subscribe_events(o)

        tid = datetime.utcnow()
        msg = b"this is my msg "
        evgen.trigger(tid, msg)

        ev = msclt.future.result(10)
        self.assertIsNot(ev, None)  # we did not receive event
        self.assertEqual(ev.EventType, ua.NodeId(ua.ObjectIds.BaseEventType))
        self.assertEqual(ev.Severity, 1)
        self.assertEqual(ev.SourceName, b'MyObject')
        self.assertEqual(ev.SourceNode, o.nodeid)
        self.assertEqual(ev.Message.Text, msg)
        self.assertEqual(ev.Time, tid)

        # time.sleep(0.1)
        sub.unsubscribe(handle)
        sub.delete()

    def test_events_wrong_source(self):
        objects = self.srv.get_objects_node()
        o = objects.add_object(3, 'MyObject')
        evgen = self.srv.get_event_generator(source=o)

        msclt = MySubHandler()
        sub = self.opc.create_subscription(100, msclt)
        handle = sub.subscribe_events()

        tid = datetime.utcnow()
        msg = b"this is my msg "
        evgen.trigger(tid, msg)

        with self.assertRaises(TimeoutError):  # we should not receive event
            ev = msclt.future.result(10)

        # time.sleep(0.1)
        sub.unsubscribe(handle)
        sub.delete()

    def test_events_CustomEvent(self):
        etype = self.srv.create_custom_event_type(2, 'MyEvent', ua.ObjectIds.BaseEventType, [('PropertyNum', ua.VariantType.Float), ('PropertyString', ua.VariantType.String)])
        evgen = self.srv.get_event_generator(etype)

        msclt = MySubHandler()
        sub = self.opc.create_subscription(100, msclt)
        handle = sub.subscribe_events(evtype=etype)

        propertynum = 2
        propertystring = "This is my test"
        evgen.event.PropertyNum = propertynum
        evgen.event.PropertyString = propertystring
        serverity = 500
        evgen.event.Severity = serverity
        tid = datetime.utcnow()
        msg = b"this is my msg "
        evgen.trigger(tid, msg)

        ev = msclt.future.result(10)
        self.assertIsNot(ev, None)  # we did not receive event
        self.assertEqual(ev.EventType, etype.nodeid)
        self.assertEqual(ev.Severity, serverity)
        self.assertEqual(ev.SourceName, self.opc.get_server_node().get_display_name().Text)
        self.assertEqual(ev.SourceNode, self.opc.get_server_node().nodeid)
        self.assertEqual(ev.Message.Text, msg)
        self.assertEqual(ev.Time, tid)
        self.assertEqual(ev.PropertyNum, propertynum)
        self.assertEqual(ev.PropertyString, propertystring)

        # time.sleep(0.1)
        sub.unsubscribe(handle)
        sub.delete()

    def test_events_CustomEvent_MyObject(self):
        objects = self.srv.get_objects_node()
        o = objects.add_object(3, 'MyObject')
        etype = self.srv.create_custom_event_type(2, 'MyEvent', ua.ObjectIds.BaseEventType, [('PropertyNum', ua.VariantType.Float), ('PropertyString', ua.VariantType.String)])
        evgen = self.srv.get_event_generator(etype, o)

        msclt = MySubHandler()
        sub = self.opc.create_subscription(100, msclt)
        handle = sub.subscribe_events(o, etype)

        propertynum = 2
        propertystring = "This is my test"
        evgen.event.PropertyNum = propertynum
        evgen.event.PropertyString = propertystring
        tid = datetime.utcnow()
        msg = b"this is my msg "
        evgen.trigger(tid, msg)

        ev = msclt.future.result(10)
        self.assertIsNot(ev, None)  # we did not receive event
        self.assertEqual(ev.EventType, etype.nodeid)
        self.assertEqual(ev.Severity, 1)
        self.assertEqual(ev.SourceName, b'MyObject')
        self.assertEqual(ev.SourceNode, o.nodeid)
        self.assertEqual(ev.Message.Text, msg)
        self.assertEqual(ev.Time, tid)
        self.assertEqual(ev.PropertyNum, propertynum)
        self.assertEqual(ev.PropertyString, propertystring)

        # time.sleep(0.1)
        sub.unsubscribe(handle)
        sub.delete()

    def test_non_existing_path(self):
        root = self.opc.get_root_node()
        with self.assertRaises(ua.UaStatusCodeError):
            server_time_node = root.get_child(['0:Objects', '0:Server', '0:nonexistingnode'])

    def test_bad_attribute(self):
        root = self.opc.get_root_node()
        with self.assertRaises(ua.UaStatusCodeError):
            root.set_value(99)

    def test_get_node_by_nodeid(self):
        root = self.opc.get_root_node()
        server_time_node = root.get_child(['0:Objects', '0:Server', '0:ServerStatus', '0:CurrentTime'])
        correct = self.opc.get_node(ua.NodeId(ua.ObjectIds.Server_ServerStatus_CurrentTime))
        self.assertEqual(server_time_node, correct)

    def test_datetime_read(self):
        time_node = self.opc.get_node(ua.NodeId(ua.ObjectIds.Server_ServerStatus_CurrentTime))
        dt = time_node.get_value()
        utcnow = datetime.utcnow()
        delta = utcnow - dt
        self.assertTrue(delta < timedelta(seconds=1))

    def test_datetime_write(self):
        time_node = self.opc.get_node(ua.NodeId(ua.ObjectIds.Server_ServerStatus_CurrentTime))
        now = datetime.utcnow()
        objects = self.opc.get_objects_node()
        v1 = objects.add_variable(4, "test_datetime", now)
        tid = v1.get_value()
        self.assertEqual(now, tid)

    def test_variant_array_dim(self):
        objects = self.opc.get_objects_node()
        l = [[[1.0, 1.0, 1.0, 1.0], [2.0, 2.0, 2.0, 2.0], [3.0, 3.0, 3.0, 3.0]],[[5.0, 5.0, 5.0, 5.0], [7.0, 8.0, 9.0, 01.0], [1.0, 1.0, 1.0, 1.0]]]
        v = objects.add_variable(3, 'variableWithDims', l)

        v.set_array_dimensions([0, 0, 0])
        dim = v.get_array_dimensions()
        self.assertEqual(dim, [0, 0, 0])

        v.set_value_rank(0)
        rank = v.get_value_rank()
        self.assertEqual(rank, 0)

        v2 = v.get_value()
        self.assertEqual(v2, l)
        dv = v.get_data_value()
        self.assertEqual(dv.Value.Dimensions, [2,3,4])

        l = [[[], [], []], [[], [], []]]
        variant = ua.Variant(l, ua.VariantType.UInt32)
        v = objects.add_variable(3, 'variableWithDimsEmpty', variant)
        v2 = v.get_value()
        self.assertEqual(v2, l)
        dv = v.get_data_value()
        self.assertEqual(dv.Value.Dimensions, [2,3,0])

    def test_add_numeric_variable(self):
        objects = self.opc.get_objects_node()
        v = objects.add_variable('ns=3;i=888;', '3:numericnodefromstring', 99)
        nid = ua.NodeId(888, 3)
        qn = ua.QualifiedName('numericnodefromstring', 3)
        self.assertEqual(nid, v.nodeid)
        self.assertEqual(qn, v.get_browse_name())

    def test_add_string_variable(self):
        objects = self.opc.get_objects_node()
        v = objects.add_variable('ns=3;s=stringid;', '3:stringnodefromstring', [68])
        nid = ua.NodeId('stringid', 3)
        qn = ua.QualifiedName('stringnodefromstring', 3)
        self.assertEqual(nid, v.nodeid)
        self.assertEqual(qn, v.get_browse_name())

    def test_utf8(self):
        objects = self.opc.get_objects_node()
        utf_string = "æøå@%&"
        bn = ua.QualifiedName(utf_string, 3)
        nid = ua.NodeId("æølå", 3)
        val = "æøå"
        v = objects.add_variable(nid, bn, val)
        self.assertEqual(nid, v.nodeid)
        val2 = v.get_value()
        self.assertEqual(val, val2)
        bn2 = v.get_browse_name()
        self.assertEqual(bn, bn2)

    def test_null_variable(self):
        objects = self.opc.get_objects_node()
        var = objects.add_variable(3, 'nullstring', "a string")
        var.set_value(None)
        val = var.get_value()
        self.assertEqual(val, None)
        var.set_value("")
        val = var.get_value()
        self.assertNotEqual(val, None)
        self.assertEqual(val, "")

    def test_variable_data_type(self):
        objects = self.opc.get_objects_node()
        var = objects.add_variable(3, 'stringfordatatype', "a string")
        val = var.get_data_type()
        self.assertEqual(val, ua.NodeId(ua.ObjectIds.String))
        var = objects.add_variable(3, 'stringarrayfordatatype', ["a", "b"])
        val = var.get_data_type()
        self.assertEqual(val, ua.NodeId(ua.ObjectIds.String))

    def test_add_string_array_variable(self):
        objects = self.opc.get_objects_node()
        v = objects.add_variable('ns=3;s=stringarrayid;', '9:stringarray', ['l', 'b'])
        nid = ua.NodeId('stringarrayid', 3)
        qn = ua.QualifiedName('stringarray', 9)
        self.assertEqual(nid, v.nodeid)
        self.assertEqual(qn, v.get_browse_name())
        val = v.get_value()
        self.assertEqual(['l', 'b'], val)

    def test_add_numeric_node(self):
        objects = self.opc.get_objects_node()
        nid = ua.NodeId(9999, 3)
        qn = ua.QualifiedName('AddNodeVar1', 3)
        v1 = objects.add_variable(nid, qn, 0)
        self.assertEqual(nid, v1.nodeid)
        self.assertEqual(qn, v1.get_browse_name())

    def test_add_string_node(self):
        objects = self.opc.get_objects_node()
        qn = ua.QualifiedName('AddNodeVar2', 3)
        nid = ua.NodeId('AddNodeVar2Id', 3)
        v2 = objects.add_variable(nid, qn, 0)
        self.assertEqual(nid, v2.nodeid)
        self.assertEqual(qn, v2.get_browse_name())

    def test_add_find_node_(self):
        objects = self.opc.get_objects_node()
        o = objects.add_object('ns=2;i=101;', '2:AddFindObject')
        o2 = objects.get_child('2:AddFindObject')
        self.assertEqual(o, o2)

    def test_node_path(self):
        objects = self.opc.get_objects_node()
        o = objects.add_object('ns=2;i=105;', '2:NodePathObject')
        root = self.opc.get_root_node()
        o2 = root.get_child(['0:Objects', '2:NodePathObject'])
        self.assertEqual(o, o2)

    def test_add_read_node(self):
        objects = self.opc.get_objects_node()
        o = objects.add_object('ns=2;i=102;', '2:AddReadObject')
        nid = ua.NodeId(102, 2)
        self.assertEqual(o.nodeid, nid)
        qn = ua.QualifiedName('AddReadObject', 2)
        self.assertEqual(o.get_browse_name(), qn)

    def test_simple_value(self):
        o = self.opc.get_objects_node()
        v = o.add_variable(3, 'VariableTestValue', 4.32)
        val = v.get_value()
        self.assertEqual(4.32, val)

    def test_add_exception(self):
        objects = self.opc.get_objects_node()
        o = objects.add_object('ns=2;i=103;', '2:AddReadObject')
        with self.assertRaises(ua.UaStatusCodeError):
            o2 = objects.add_object('ns=2;i=103;', '2:AddReadObject')

    def test_negative_value(self):
        o = self.opc.get_objects_node()
        v = o.add_variable(3, 'VariableNegativeValue', 4)
        v.set_value(-4.54)
        val = v.get_value()
        self.assertEqual(-4.54, val)

    def test_read_server_state(self):
        statenode = self.opc.get_node(ua.NodeId(ua.ObjectIds.Server_ServerStatus_State))
        state = statenode.get_value()
        self.assertEqual(state, 0)

    def test_bad_node(self):
        bad = self.opc.get_node(ua.NodeId(999, 999))
        with self.assertRaises(ua.UaStatusCodeError):
            bad.get_browse_name()
        with self.assertRaises(ua.UaStatusCodeError):
            bad.set_value(89)
        with self.assertRaises(ua.UaStatusCodeError):
            bad.add_object(0, "0:myobj")
        with self.assertRaises(ua.UaStatusCodeError):
            bad.get_child("0:myobj")

    def test_value(self):
        o = self.opc.get_objects_node()
        var = ua.Variant(1.98, ua.VariantType.Double)
        v = o.add_variable(3, 'VariableValue', var)
        val = v.get_value()
        self.assertEqual(1.98, val)

        dvar = ua.DataValue(var)
        dv = v.get_data_value()
        self.assertEqual(ua.DataValue, type(dv))
        self.assertEqual(dvar.Value, dv.Value)
        self.assertEqual(dvar.Value, var)

    def test_set_value(self):
        o = self.opc.get_objects_node()
        var = ua.Variant(1.98, ua.VariantType.Double)
        dvar = ua.DataValue(var)
        v = o.add_variable(3, 'VariableValue', var)
        v.set_value(var.Value)
        v1 = v.get_value()
        self.assertEqual(v1, var.Value)
        v.set_value(var)
        v2 = v.get_value()
        self.assertEqual(v2, var.Value)
        v.set_data_value(dvar)
        v3 = v.get_data_value()
        self.assertEqual(v3.Value, dvar.Value)

    def test_array_value(self):
        o = self.opc.get_objects_node()
        v = o.add_variable(3, 'VariableArrayValue', [1, 2, 3])
        val = v.get_value()
        self.assertEqual([1, 2, 3], val)

    def test_bool_variable(self):
        o = self.opc.get_objects_node()
        v = o.add_variable(3, 'BoolVariable', True)
        dt = v.get_data_type()
        self.assertEqual(dt, ua.TwoByteNodeId(ua.ObjectIds.Boolean))
        val = v.get_value()
        self.assertEqual(True, val)
        v.set_value(False)
        val = v.get_value()
        self.assertEqual(False, val)

    def test_array_size_one_value(self):
        o = self.opc.get_objects_node()
        v = o.add_variable(3, 'VariableArrayValue', [1, 2, 3])
        v.set_value([1])
        val = v.get_value()
        self.assertEqual([1], val)

    def test_subscription_failure(self):
        msclt = MySubHandler()
        o = self.opc.get_objects_node()
        sub = self.opc.create_subscription(100, msclt)
        with self.assertRaises(ua.UaStatusCodeError):
            handle1 = sub.subscribe_data_change(o) # we can only subscribe to variables so this should fail
        sub.delete()

    def test_subscription_overload(self):
        nb = 10
        msclt = MySubHandler()
        o = self.opc.get_objects_node()
        sub = self.opc.create_subscription(1, msclt)
        variables = []
        subs = []
        for i in range(nb):
            v = o.add_variable(3, 'SubscriptionVariableOverload' + str(i), 99)
            variables.append(v)
        for i in range(nb):
            sub.subscribe_data_change(variables)
        for i in range(nb):
            for j in range(nb):
                variables[i].set_value(j)
            s = self.opc.create_subscription(1, msclt)
            s.subscribe_data_change(variables)
            subs.append(s)
            sub.subscribe_data_change(variables[i])
        for i in range(nb):
            for j in range(nb):
                variables[i].set_value(j)
        sub.delete()
        for s in subs:
            s.delete()

    def test_subscription_count(self):
        msclt = MySubHandlerCounter()
        sub = self.opc.create_subscription(1, msclt)
        o = self.opc.get_objects_node()
        var = o.add_variable(3, 'SubVarCounter', 0.1)
        sub.subscribe_data_change(var)
        nb = 12
        for i in range(nb):
            val = var.get_value()
            var.set_value(val +1)
        time.sleep(0.2)  # let last event arrive
        self.assertEqual(msclt.datachange_count, nb + 1)
        sub.delete()

    def test_subscription_count_list(self):
        msclt = MySubHandlerCounter()
        sub = self.opc.create_subscription(1, msclt)
        o = self.opc.get_objects_node()
        var = o.add_variable(3, 'SubVarCounter', [0.1, 0.2])
        sub.subscribe_data_change(var)
        nb = 12
        for i in range(nb):
            val = var.get_value()
            val.append(i)
            var.set_value(val)
        time.sleep(0.2)  # let last event arrive
        self.assertEqual(msclt.datachange_count, nb + 1)
        sub.delete()

    def test_subscription_count_no_change(self):
        msclt = MySubHandlerCounter()
        sub = self.opc.create_subscription(1, msclt)
        o = self.opc.get_objects_node()
        var = o.add_variable(3, 'SubVarCounter', [0.1, 0.2])
        sub.subscribe_data_change(var)
        nb = 12
        for i in range(nb):
            val = var.get_value()
            var.set_value(val)
        time.sleep(0.2)  # let last event arrive
        self.assertEqual(msclt.datachange_count, 1)
        sub.delete()

    def test_subscription_count_empty(self):
        msclt = MySubHandlerCounter()
        sub = self.opc.create_subscription(1, msclt)
        o = self.opc.get_objects_node()
        var = o.add_variable(3, 'SubVarCounter', [0.1, 0.2, 0.3])
        sub.subscribe_data_change(var)
        while True:
            val = var.get_value()
            val.pop()
            var.set_value(val, ua.VariantType.Double)
            if not val:
                break
        time.sleep(0.2)  # let last event arrive
        self.assertEqual(msclt.datachange_count, 4)
        sub.delete()

    def test_subscription_overload_simple(self):
        nb = 10
        msclt = MySubHandler()
        o = self.opc.get_objects_node()
        sub = self.opc.create_subscription(1, msclt)
        variables = [o.add_variable(3, 'SubVarOverload' + str(i), i) for i in range(nb)]
        for i in range(nb):
            sub.subscribe_data_change(variables)
        sub.delete()

    def test_subscription_data_change_depcrecated(self):
        '''
        test subscriptions. This is far too complicated for
        a unittest but, setting up subscriptions requires a lot
        of code, so when we first set it up, it is best
        to test as many things as possible
        '''
        msclt = MySubHandlerDeprecated()

        o = self.opc.get_objects_node()

        # subscribe to a variable
        startv1 = [1, 2, 3]
        v1 = o.add_variable(3, 'SubscriptionVariableDeprecatedV1', startv1)
        sub = self.opc.create_subscription(100, msclt)
        handle1 = sub.subscribe_data_change(v1)

        # Now check we get the start value
        clthandle, node, val, attr = msclt.future.result()
        self.assertEqual(val, startv1)
        self.assertEqual(node, v1)

        msclt.reset()  # reset future object

        # modify v1 and check we get value
        v1.set_value([5])
        clthandle, node, val, attr = msclt.future.result()

        self.assertEqual(node, v1)
        self.assertEqual(val, [5])

        with self.assertRaises(ua.UaStatusCodeError):
            sub.unsubscribe(999)  # non existing handle
        sub.unsubscribe(handle1)
        with self.assertRaises(ua.UaStatusCodeError):
            sub.unsubscribe(handle1)  # second try should fail
        sub.delete()
        with self.assertRaises(ua.UaStatusCodeError):
            sub.unsubscribe(handle1)  # sub does not exist anymore

    def test_subscription_data_change(self):
        '''
        test subscriptions. This is far too complicated for
        a unittest but, setting up subscriptions requires a lot
        of code, so when we first set it up, it is best
        to test as many things as possible
        '''
        msclt = MySubHandler()

        o = self.opc.get_objects_node()

        # subscribe to a variable
        startv1 = [1, 2, 3]
        v1 = o.add_variable(3, 'SubscriptionVariableV1', startv1)
        sub = self.opc.create_subscription(100, msclt)
        handle1 = sub.subscribe_data_change(v1)

        # Now check we get the start value
        node, val, data = msclt.future.result()
        self.assertEqual(val, startv1)
        self.assertEqual(node, v1)

        msclt.reset()  # reset future object

        # modify v1 and check we get value
        v1.set_value([5])
        node, val, data = msclt.future.result()

        self.assertEqual(node, v1)
        self.assertEqual(val, [5])

        with self.assertRaises(ua.UaStatusCodeError):
            sub.unsubscribe(999)  # non existing handle
        sub.unsubscribe(handle1)
        with self.assertRaises(ua.UaStatusCodeError):
            sub.unsubscribe(handle1)  # second try should fail
        sub.delete()
        with self.assertRaises(ua.UaStatusCodeError):
            sub.unsubscribe(handle1)  # sub does not exist anymore


    def test_subscription_data_change_bool(self):
        '''
        test subscriptions. This is far too complicated for
        a unittest but, setting up subscriptions requires a lot
        of code, so when we first set it up, it is best
        to test as many things as possible
        '''
        msclt = MySubHandler()

        o = self.opc.get_objects_node()

        # subscribe to a variable
        startv1 = True
        v1 = o.add_variable(3, 'SubscriptionVariableBool', startv1)
        sub = self.opc.create_subscription(100, msclt)
        handle1 = sub.subscribe_data_change(v1)

        # Now check we get the start value
        node, val, data = msclt.future.result()
        self.assertEqual(val, startv1)
        self.assertEqual(node, v1)

        msclt.reset()  # reset future object

        # modify v1 and check we get value
        v1.set_value(False)
        node, val, data = msclt.future.result()
        self.assertEqual(node, v1)
        self.assertEqual(val, False)

        sub.delete() # should delete our monitoreditem too

    def test_subscription_data_change_many(self):
        '''
        test subscriptions. This is far too complicated for
        a unittest but, setting up subscriptions requires a lot
        of code, so when we first set it up, it is best
        to test as many things as possible
        '''
        msclt = MySubHandler2()
        o = self.opc.get_objects_node()

        startv1 = True
        v1 = o.add_variable(3, 'SubscriptionVariableMany1', startv1)
        startv2 = [1.22, 1.65]
        v2 = o.add_variable(3, 'SubscriptionVariableMany2', startv2)

        sub = self.opc.create_subscription(100, msclt)
        handle1, handle2 = sub.subscribe_data_change([v1, v2])

        # Now check we get the start values
        nodes = [v1, v2]

        count = 0
        while not len(msclt.results) > 1:
            count += 1
            time.sleep(0.1)
            if count > 100:
                self.fail("Did not get result from subscription")
        for node, val in msclt.results:
            self.assertIn(node, nodes)
            nodes.remove(node)
            if node == v1:
                self.assertEqual(startv1, val)
            elif node == v2:
                self.assertEqual(startv2, val)
            else:
                self.fail("Error node {} is neither {} nor {}".format(node, v1, v2))

        sub.delete()

    def test_subscribe_server_time(self):
        msclt = MySubHandler()

        server_time_node = self.opc.get_node(ua.NodeId(ua.ObjectIds.Server_ServerStatus_CurrentTime))

        sub = self.opc.create_subscription(200, msclt)
        handle = sub.subscribe_data_change(server_time_node)

        node, val, data = msclt.future.result()
        self.assertEqual(node, server_time_node)
        delta = datetime.utcnow() - val
        self.assertTrue(delta < timedelta(seconds=2))

        sub.unsubscribe(handle)
        sub.delete()

    def test_use_namespace(self):
        idx = self.opc.get_namespace_index("urn:freeopcua:python:server")
        self.assertEqual(idx, 1)
        root = self.opc.get_root_node()
        myvar = root.add_variable(idx, 'var_in_custom_namespace', [5])
        myid = myvar.nodeid
        self.assertEqual(idx, myid.NamespaceIndex)

    def test_method(self):
        o = self.opc.get_objects_node()
        m = o.get_child("2:ServerMethod")
        result = o.call_method("2:ServerMethod", 2.1)
        self.assertEqual(result, 4.2)
        with self.assertRaises(ua.UaStatusCodeError):
            # FIXME: we should raise a more precise exception
            result = o.call_method("2:ServerMethod", 2.1, 89, 9)
        with self.assertRaises(ua.UaStatusCodeError):
            result = o.call_method(ua.NodeId(999), 2.1)  # non existing method

    def test_method_array(self):
        o = self.opc.get_objects_node()
        m = o.get_child("2:ServerMethodArray")
        result = o.call_method(m, "sin", ua.Variant(math.pi))
        self.assertTrue(result < 0.01)

    def test_method_array2(self):
        o = self.opc.get_objects_node()
        m = o.get_child("2:ServerMethodArray2")
        result = o.call_method(m, [1.1, 3.4, 9])
        self.assertEqual(result, [2.2, 6.8, 18])

    def test_add_nodes(self):
        objects = self.opc.get_objects_node()
        f = objects.add_folder(3, 'MyFolder')
        child = objects.get_child("3:MyFolder")
        self.assertEqual(child, f)
        o = f.add_object(3, 'MyObject')
        child = f.get_child("3:MyObject")
        self.assertEqual(child, o)
        v = f.add_variable(3, 'MyVariable', 6)
        child = f.get_child("3:MyVariable")
        self.assertEqual(child, v)
        p = f.add_property(3, 'MyProperty', 10)
        child = f.get_child("3:MyProperty")
        self.assertEqual(child, p)
        childs = f.get_children()
        self.assertTrue(o in childs)
        self.assertTrue(v in childs)
        self.assertTrue(p in childs)

    def test_references_for_added_nodes(self):
        objects = self.opc.get_objects_node()
        o = objects.add_object(3, 'MyObject')
        nodes = objects.get_referenced_nodes(refs=ua.ObjectIds.Organizes, direction=ua.BrowseDirection.Forward, includesubtypes=False)
        self.assertTrue(o in nodes)
        nodes = o.get_referenced_nodes(refs=ua.ObjectIds.Organizes, direction=ua.BrowseDirection.Inverse, includesubtypes=False)
        self.assertTrue(objects in nodes)
        self.assertEqual(o.get_parent(), objects)
        self.assertEqual(o.get_type_definition(), ua.ObjectIds.BaseObjectType)

        o2 = o.add_object(3, 'MySecondObject')
        nodes = o.get_referenced_nodes(refs=ua.ObjectIds.HasComponent, direction=ua.BrowseDirection.Forward, includesubtypes=False)
        self.assertTrue(o2 in nodes)
        nodes = o2.get_referenced_nodes(refs=ua.ObjectIds.HasComponent, direction=ua.BrowseDirection.Inverse, includesubtypes=False)
        self.assertTrue(o in nodes)
        self.assertEqual(o2.get_parent(), o)
        self.assertEqual(o2.get_type_definition(), ua.ObjectIds.BaseObjectType)

        v = o.add_variable(3, 'MyVariable', 6)
        nodes = o.get_referenced_nodes(refs=ua.ObjectIds.HasComponent, direction=ua.BrowseDirection.Forward, includesubtypes=False)
        self.assertTrue(v in nodes)
        nodes = v.get_referenced_nodes(refs=ua.ObjectIds.HasComponent, direction=ua.BrowseDirection.Inverse, includesubtypes=False)
        self.assertTrue(o in nodes)
        self.assertEqual(v.get_parent(), o)
        self.assertEqual(v.get_type_definition(), ua.ObjectIds.BaseDataVariableType)

        p = o.add_property(3, 'MyProperty', 2)
        nodes = o.get_referenced_nodes(refs=ua.ObjectIds.HasProperty, direction=ua.BrowseDirection.Forward, includesubtypes=False)
        self.assertTrue(p in nodes)
        nodes = p.get_referenced_nodes(refs=ua.ObjectIds.HasProperty, direction=ua.BrowseDirection.Inverse, includesubtypes=False)
        self.assertTrue(o in nodes)
        self.assertEqual(p.get_parent(), o)
        self.assertEqual(p.get_type_definition(), ua.ObjectIds.PropertyType)

    def test_get_endpoints(self):
        endpoints = self.opc.get_endpoints()
        self.assertTrue(len(endpoints) > 0)
        self.assertTrue(endpoints[0].EndpointUrl.startswith("opc.tcp://"))
