#! /usr/bin/env python
# coding: utf-8
import sys
sys.path.insert(0, "..")
sys.path.insert(0, ".")
import time
import logging
import math
import io
from datetime import datetime, timedelta
import unittest
from concurrent.futures import Future
from threading import Lock

from opcua import ua
from opcua import Client
from opcua import Server
from opcua import uamethod
from opcua import Event
from opcua import ObjectIds
from opcua import AttributeIds

port_num1 = 48510
port_num2 = 48530


class SubHandler():

    '''
        Dummy subscription client
    '''

    def data_change(self, handle, node, val, attr):
        pass

    def event(self, handle, event):
        pass


class MySubHandler():

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


class MySubHandler2():
    def __init__(self):
        self.results = [] 

    def data_change(self, handle, node, val, attr):
        self.results.append((node, val))

    def event(self, handle, event):
        self.results.append((node, val))


class Unit(unittest.TestCase):

    '''
    Simple unit test that do not need to setup a server or a client
    '''

    def test_guid(self):
        g = ua.Guid()
        sc = ua.StatusCode()

    def test_nodeid(self):
        nid = ua.NodeId()
        self.assertEqual(nid.NodeIdType, ua.NodeIdType.TwoByte)
        nid = ua.NodeId(446, 3, ua.NodeIdType.FourByte)
        self.assertEqual(nid.NodeIdType, ua.NodeIdType.FourByte)
        d = nid.to_binary()
        new_nid = nid.from_binary(io.BytesIO(d))
        self.assertEqual(new_nid, nid)
        self.assertEqual(new_nid.NodeIdType, ua.NodeIdType.FourByte)
        self.assertEqual(new_nid.Identifier, 446)
        self.assertEqual(new_nid.NamespaceIndex, 3)

        tb = ua.TwoByteNodeId(53)
        fb = ua.FourByteNodeId(53)
        n = ua.NumericNodeId(53)
        n1 = ua.NumericNodeId(53, 0)
        s = ua.StringNodeId(53, 0)  # should we raise an exception???
        s1 = ua.StringNodeId("53", 0)
        bs = ua.ByteStringNodeId(b"53", 0)
        gid = ua.Guid()
        g = ua.ByteStringNodeId(gid, 0)
        guid = ua.GuidNodeId(gid)
        self.assertEqual(tb, fb)
        self.assertEqual(tb, n)
        self.assertEqual(tb, n1)
        self.assertEqual(n1, fb)
        self.assertNotEqual(n1, s)
        self.assertNotEqual(s, bs)
        self.assertNotEqual(s, g)
        self.assertNotEqual(g, guid)
        self.assertEqual(tb, ua.NodeId.from_binary(ua.utils.Buffer(tb.to_binary())))
        self.assertEqual(fb, ua.NodeId.from_binary(ua.utils.Buffer(fb.to_binary())))
        self.assertEqual(n, ua.NodeId.from_binary(ua.utils.Buffer(n.to_binary())))
        self.assertEqual(s1, ua.NodeId.from_binary(ua.utils.Buffer(s1.to_binary())))
        self.assertEqual(bs, ua.NodeId.from_binary(ua.utils.Buffer(bs.to_binary())))
        self.assertEqual(guid, ua.NodeId.from_binary(ua.utils.Buffer(guid.to_binary())))

    def test_nodeid_string(self):
        nid0 = ua.NodeId(45)
        self.assertEqual(nid0, ua.NodeId.from_string("i=45"))
        self.assertEqual(nid0, ua.NodeId.from_string("ns=0;i=45"))
        nid = ua.NodeId(45, 10)
        self.assertEqual(nid, ua.NodeId.from_string("i=45; ns=10"))
        self.assertNotEqual(nid, ua.NodeId.from_string("i=45; ns=11"))
        self.assertNotEqual(nid, ua.NodeId.from_string("i=5; ns=10"))
        # not sure the next one is correct...
        self.assertEqual(nid, ua.NodeId.from_string("i=45; ns=10; srv=serverid"))

    def test_expandednodeid(self):
        nid = ua.ExpandedNodeId()
        self.assertEqual(nid.NodeIdType, ua.NodeIdType.TwoByte)
        nid2 = ua.ExpandedNodeId.from_binary(ua.utils.Buffer(nid.to_binary()))
        self.assertEqual(nid, nid2)

    def test_extension_object(self):
        obj = ua.ExtensionObject()
        obj2 = ua.ExtensionObject.from_binary(ua.utils.Buffer(obj.to_binary()))
        self.assertEqual(obj2.TypeId, obj2.TypeId)
        self.assertEqual(obj2.Body, obj2.Body)

    def test_datetime(self):
        now = datetime.now()
        epch = ua.datetime_to_win_epoch(now)
        dt = ua.win_epoch_to_datetime(epch)
        self.assertEqual(now, dt)

        epch = 128930364000001000
        dt = ua.win_epoch_to_datetime(epch)
        epch2 = ua.datetime_to_win_epoch(dt)
        self.assertEqual(epch, epch2)

    def test_equal_nodeid(self):
        nid1 = ua.NodeId(999, 2)
        nid2 = ua.NodeId(999, 2)
        self.assertTrue(nid1 == nid2)
        self.assertTrue(id(nid1) != id(nid2))

    def test_zero_nodeid(self):
        self.assertEqual(ua.NodeId(), ua.NodeId(0, 0))
        self.assertEqual(ua.NodeId(), ua.NodeId.from_string('ns=0;i=0;'))

    def test_string_nodeid(self):
        nid = ua.NodeId('titi', 1)
        self.assertEqual(nid.NamespaceIndex, 1)
        self.assertEqual(nid.Identifier, 'titi')
        self.assertEqual(nid.NodeIdType, ua.NodeIdType.String)

    def test_unicode_string_nodeid(self):
        nid = ua.NodeId('hëllò', 1)
        self.assertEqual(nid.NamespaceIndex, 1)
        self.assertEqual(nid.Identifier, 'hëllò')
        self.assertEqual(nid.NodeIdType, ua.NodeIdType.String)
        d = nid.to_binary()
        new_nid = nid.from_binary(io.BytesIO(d))
        self.assertEqual(new_nid, nid)
        self.assertEqual(new_nid.Identifier, 'hëllò')
        self.assertEqual(new_nid.NodeIdType, ua.NodeIdType.String)

    def test_numeric_nodeid(self):
        nid = ua.NodeId(999, 2)
        self.assertEqual(nid.NamespaceIndex, 2)
        self.assertEqual(nid.Identifier, 999)
        self.assertEqual(nid.NodeIdType, ua.NodeIdType.Numeric)

    def test_qualifiedstring_nodeid(self):
        nid = ua.NodeId.from_string('ns=2;s=PLC1.Manufacturer;')
        self.assertEqual(nid.NamespaceIndex, 2)
        self.assertEqual(nid.Identifier, 'PLC1.Manufacturer')

    def test_strrepr_nodeid(self):
        nid = ua.NodeId.from_string('ns=2;s=PLC1.Manufacturer;')
        self.assertEqual(nid.to_string(), 'ns=2;s=PLC1.Manufacturer')
        #self.assertEqual(repr(nid), 'ns=2;s=PLC1.Manufacturer;')

    def test_qualified_name(self):
        qn = ua.QualifiedName('qname', 2)
        self.assertEqual(qn.NamespaceIndex, 2)
        self.assertEqual(qn.Name, 'qname')
        self.assertEqual(qn.to_string(), '2:qname')

    def test_datavalue(self):
        dv = ua.DataValue(123)
        self.assertEqual(dv.Value, ua.Variant(123))
        self.assertEqual(type(dv.Value), ua.Variant)
        dv = ua.DataValue('abc')
        self.assertEqual(dv.Value, ua.Variant('abc'))
        now = datetime.now()
        dv.source_timestamp = now

    def test_variant(self):
        dv = ua.Variant(True, ua.VariantType.Boolean)
        self.assertEqual(dv.Value, True)
        self.assertEqual(type(dv.Value), bool)
        now = datetime.now()
        v = ua.Variant(now)
        self.assertEqual(v.Value, now)
        self.assertEqual(v.VariantType, ua.VariantType.DateTime)
        v2 = ua.Variant.from_binary(ua.utils.Buffer(v.to_binary()))
        self.assertEqual(v.Value, v2.Value)
        self.assertEqual(v.VariantType, v2.VariantType)
        # commonity method:
        self.assertEqual(v, ua.Variant(v))

    def test_variant_array(self):
        v = ua.Variant([1, 2, 3, 4, 5])
        self.assertEqual(v.Value[1], 2)
        # self.assertEqual(v.VarianType, ua.VariantType.Int64) # we do not care, we should aonly test for sutff that matter
        v2 = ua.Variant.from_binary(ua.utils.Buffer(v.to_binary()))
        self.assertEqual(v.Value, v2.Value)
        self.assertEqual(v.VariantType, v2.VariantType)

        now = datetime.now()
        v = ua.Variant([now])
        self.assertEqual(v.Value[0], now)
        self.assertEqual(v.VariantType, ua.VariantType.DateTime)
        v2 = ua.Variant.from_binary(ua.utils.Buffer(v.to_binary()))
        self.assertEqual(v.Value, v2.Value)
        self.assertEqual(v.VariantType, v2.VariantType)

    def test_text(self):
        t1 = ua.LocalizedText('Root')
        t2 = ua.LocalizedText('Root')
        t3 = ua.LocalizedText('root')
        self.assertEqual(t1, t2)
        self.assertNotEqual(t1, t3)
        t4 = ua.LocalizedText.from_binary(ua.utils.Buffer(t1.to_binary()))
        self.assertEqual(t1, t4)


class CommonTests(object):

    '''
    Tests that will be run twice. Once on server side and once on
    client side since we have been carefull to have the exact
    same api on server and client side
    '''

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
        props = obj.get_children(refs=ObjectIds.HasProperty)
        self.assertTrue(prop in props)
        self.assertTrue(prop2 in props)
        self.assertFalse(var in props)
        self.assertFalse(folder in props)
        all_vars = obj.get_children(nodeclassmask=ua.NodeClass.Variable)
        self.assertTrue(prop in all_vars)
        self.assertTrue(var in all_vars)
        all_objs = obj.get_children(nodeclassmask=ua.NodeClass.Object)
        self.assertTrue(folder in all_objs)
        self.assertTrue(obj2 in all_objs)
        self.assertFalse(var in all_objs)

    def test_create_delete_subscription(self):
        o = self.opc.get_objects_node()
        v = o.add_variable(3, 'SubscriptionVariable', [1, 2, 3])
        sub = self.opc.create_subscription(100, sclt)
        handle = sub.subscribe_data_change(v)
        time.sleep(0.1)
        sub.unsubscribe(handle)
        sub.delete()

    def test_subscribe_events(self):
        sub = self.opc.create_subscription(100, sclt)
        handle = sub.subscribe_events()
        time.sleep(0.1)
        sub.unsubscribe(handle)
        sub.delete()

    def test_events(self):
        msclt = MySubHandler()
        #cond = msclt.setup()
        sub = self.opc.create_subscription(100, msclt)
        handle = sub.subscribe_events()

        ev = Event(self.srv.iserver.isession)
        msg = b"this is my msg "
        ev.Message.Text = msg
        tid = datetime.now()
        ev.Time = tid
        #ev.source_node = self.opc.get_server_node().nodeid
        #ev.source_name = "our server node"
        ev.Severity = 500
        ev.trigger()

        clthandle, ev = msclt.future.result()
        # with cond:
        #ret = cond.wait(50000)
        # if sys.version_info.major>2: self.assertEqual(ret, True) # we went into timeout waiting for subcsription callback
        # else: pass # python2
        self.assertIsNot(ev, None)  # we did not receive event
        self.assertEqual(ev.Message.Text, msg)
        #self.assertEqual(msclt.ev.Time, tid)
        self.assertEqual(ev.Severity, 500)
        self.assertEqual(ev.SourceNode, self.opc.get_server_node().nodeid)

        # time.sleep(0.1)
        sub.unsubscribe(handle)
        sub.delete()

    def test_non_existing_path(self):
        root = self.opc.get_root_node()
        with self.assertRaises(Exception):
            server_time_node = root.get_child(['0:Objects', '0:Server', '0:nonexistingnode'])

    def test_bad_attribute(self):
        root = self.opc.get_root_node()
        with self.assertRaises(Exception):
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
        now = datetime.now()
        objects = self.opc.get_objects_node()
        v1 = objects.add_variable(4, "test_datetime", now)
        tid = v1.get_value()
        self.assertEqual(now, tid)

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
        with self.assertRaises(Exception):
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
        with self.assertRaises(Exception):
            bad.get_browse_name()
        with self.assertRaises(Exception):
            bad.set_value(89)
        with self.assertRaises(Exception):
            bad.add_object(0, "myobj")
        with self.assertRaises(Exception):
            bad.get_child(0, "myobj")

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
        with self.assertRaises(Exception):
            handle1 = sub.subscribe_data_change(o) # we can only subscribe to variables so this should fail
        sub.delete()

    def test_subscription_overload(self):
        msclt = MySubHandler()
        o = self.opc.get_objects_node()
        v = o.add_variable(3, 'SubscriptionVariableOverload', 0)
        sub = self.opc.create_subscription(1, msclt)
        handle1 = sub.subscribe_data_change(v)
        for i in range(10):
            v.set_value(i)
        sub2 = self.opc.create_subscription(1, msclt)
        sub.subscribe_data_change(v)
        sub.subscribe_data_change(v)
        for i in range(10):
            v.set_value(i)
        time.sleep(1)
        sub.delete()
        sub2.delete()

    def test_subscription_data_change(self):
        '''
        test subscriptions. This is far too complicated for
        a unittest but, setting up subscriptions requires a lot
        of code, so when we first set it up, it is best
        to test as many things as possible
        '''
        msclt = MySubHandler()
        #cond = msclt.setup()

        o = self.opc.get_objects_node()

        # subscribe to a variable
        startv1 = [1, 2, 3]
        v1 = o.add_variable(3, 'SubscriptionVariableV1', startv1)
        sub = self.opc.create_subscription(100, msclt)
        handle1 = sub.subscribe_data_change(v1)

        # Now check we get the start value
        clthandle, node, val, attr = msclt.future.result()
        # with cond:
        #ret = cond.wait(0.5)
        # if sys.version_info.major>2: self.assertEqual(ret, True) # we went into timeout waiting for subcsription callback
        # else: pass # XXX
        self.assertEqual(val, startv1)
        self.assertEqual(node, v1)

        msclt.reset()  # reset future object

        # modify v1 and check we get value
        v1.set_value([5])
        clthandle, node, val, attr = msclt.future.result()
        # with cond:
        #ret = cond.wait(0.5)
        # if sys.version_info.major>2: self.assertEqual(ret, True) # we went into timeout waiting for subcsription callback
        # else: pass # XXX
        self.assertEqual(node, v1)
        self.assertEqual(val, [5])

        with self.assertRaises(Exception):
            sub.unsubscribe(999)  # non existing handle
        sub.unsubscribe(handle1)
        with self.assertRaises(Exception):
            sub.unsubscribe(handle1)  # second try should fail
        sub.delete()
        with self.assertRaises(Exception):
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
        clthandle, node, val, attr = msclt.future.result()
        self.assertEqual(val, startv1)
        self.assertEqual(node, v1)

        msclt.reset()  # reset future object

        # modify v1 and check we get value
        v1.set_value(False)
        clthandle, node, val, attr = msclt.future.result()
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

        clthandle, node, val, attr = msclt.future.result()
        self.assertEqual(node, server_time_node)
        delta = datetime.now() - val
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
        with self.assertRaises(Exception):
            # FIXME: we should raise a more precise exception
            result = o.call_method("2:ServerMethod", 2.1, 89, 9)
        with self.assertRaises(Exception):
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
        v = f.add_variable(3, 'MyVariable', 6)
        p = f.add_property(3, 'MyProperty', 10)
        childs = f.get_children()
        self.assertTrue(v in childs)
        self.assertTrue(p in childs)

    def test_get_endpoints(self):
        endpoints = self.opc.get_endpoints()
        self.assertTrue(len(endpoints) > 0)
        self.assertTrue(endpoints[0].EndpointUrl.startswith("opc.tcp://"))


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

class AdminTestClient(unittest.TestCase, CommonTests):

    '''
    Run common tests on client side
    Of course we need a server so we start a server in another
    process using python Process module
    Tests that can only be run on client side must be defined here
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
        with self.assertRaises(Exception):
            self.clt.bclient._send_request(request)

    def test_objects_anonymous(self):
        objects = self.ro_clt.get_objects_node()
        with self.assertRaises(Exception):
            objects.set_attribute(ua.AttributeIds.WriteMask, ua.DataValue(999))
        with self.assertRaises(Exception):
            f = objects.add_folder(3, 'MyFolder')

    def test_folder_anonymous(self):
        objects = self.clt.get_objects_node()
        f = objects.add_folder(3, 'MyFolderRO')
        f_ro = self.ro_clt.get_node(f.nodeid)
        self.assertEqual(f, f_ro)
        with self.assertRaises(Exception):
            f2 = f_ro.add_folder(3, 'MyFolder2')

    def test_variable_anonymous(self):
        objects = self.clt.get_objects_node()
        v = objects.add_variable(3, 'MyROVariable', 6)
        v.set_value(4) #this should work
        v_ro = self.ro_clt.get_node(v.nodeid)
        with self.assertRaises(Exception):
            v_ro.set_value(2)
        self.assertEqual(v_ro.get_value(), 4)
        v.set_writable(True)
        v_ro.set_value(2) #now it should work
        self.assertEqual(v_ro.get_value(), 2)
        v.set_writable(False)
        with self.assertRaises(Exception):
            v_ro.set_value(9)
        self.assertEqual(v_ro.get_value(), 2)



class TestServer(unittest.TestCase, CommonTests):

    '''
    Run common tests on server side
    Tests that can only be run on server side must be defined here
    '''
    @classmethod
    def setUpClass(self):
        self.srv = Server()
        self.srv.set_endpoint('opc.tcp://localhost:%d' % port_num2)
        add_server_methods(self.srv)
        self.srv.start()
        self.opc = self.srv

    @classmethod
    def tearDownClass(self):
        self.srv.stop()

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



if __name__ == '__main__':
    logging.basicConfig(level=logging.WARN)

    sclt = SubHandler()
    unittest.main(verbosity=3)
