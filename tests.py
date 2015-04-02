#! /usr/bin/env python
import logging
import io
import sys
from datetime import datetime, timedelta
import unittest
from threading import Thread, Event
try:
    from queue import Queue
except ImportError:
    from Queue import Queue
import time
from threading import Condition

from opcua import ua
from opcua import Client
from opcua import Server

port_num1 = 48410
port_num2 = 48430

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
    More advanced subscription client using conditions, so we can wait for events in tests 
    '''
    def setup(self):
        self.cond = Condition()
        self.node = None
        self.handle = None
        self.attribute = None
        self.value = None
        self.ev = None
        return self.cond

    def data_change(self, handle, node, val, attr):
        self.handle = handle
        self.node = node
        self.value = val
        self.attribute = attr
        with self.cond:
            self.cond.notify_all()

    def event(self, handle, event):
        self.ev = event
        with self.cond:
            self.cond.notify_all()

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
        self.assertTrue(nid1==nid2)
        self.assertTrue(id(nid1)!=id(nid2))
    
    def test_zero_nodeid(self):
        self.assertEqual(ua.NodeId(), ua.NodeId(0,0))
        self.assertEqual(ua.NodeId(), ua.NodeId.from_string('ns=0;i=0;'))

    def test_string_nodeid(self):
        nid = ua.NodeId('titi', 1)
        self.assertEqual(nid.NamespaceIndex, 1)
        self.assertEqual(nid.Identifier, 'titi')
        self.assertEqual(nid.NodeIdType, ua.NodeIdType.String)

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

    def test_variant_array(self):
        v = ua.Variant([1,2,3,4,5])
        self.assertEqual(v.Value[1], 2)
        #self.assertEqual(v.VarianType, ua.VariantType.Int64) # we do not care, we should aonly test for sutff that matter
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


class CommonTests(object):
    '''
    Tests that will be run twice. Once on server side and once on 
    client side since we have been carefull to have the exact 
    same api on server and client side
    '''

    def test_root(self):
        root = self.opc.get_root_node()
        self.assertEqual(ua.QualifiedName('Root', 0), root.get_name())
        nid = ua.NodeId(84, 0) 
        self.assertEqual(nid, root.nodeid)

    def test_objects(self):
        objects = self.opc.get_objects_node()
        self.assertEqual(ua.QualifiedName('Objects', 0), objects.get_name())
        nid = ua.NodeId(85, 0) 
        self.assertEqual(nid, objects.nodeid)
    
    def test_create_delete_subscription(self):
        o = self.opc.get_objects_node()
        v = o.add_variable(3, 'SubscriptionVariable', [1, 2, 3])
        sub = self.opc.create_subscription(100, sclt)
        handle = sub.subscribe_data_change(v)
        time.sleep(0.1)
        sub.unsubscribe(handle)
        sub.delete()
    
    #def test_subscribe_events(self):
        #sub = self.opc.create_subscription(100, sclt)
        #handle = sub.subscribe_events()
        ##time.sleep(0.1)
        #sub.unsubscribe(handle)
        #sub.delete()

    #def test_events(self):
        #msclt = MySubHandler()
        #cond = msclt.setup()
        #sub = self.opc.create_subscription(100, msclt)
        #handle = sub.subscribe_events()
        
        #ev = ua.Event()
        #msg = "this is my msg " 
        #ev.message = msg
        #tid = datetime.datetime.now()
        #ev.time = tid
        #ev.source_node = self.opc.get_server_node().nodeid
        #ev.source_name = "our server node"
        #ev.severity = 500
        #self.srv.trigger_event(ev)
        
        #with cond:
            #ret = cond.wait(50000)
        #if sys.version_info.major>2: self.assertEqual(ret, True) # we went into timeout waiting for subcsription callback
        #else: pass # XXX
        #self.assertIsNot(msclt.ev, None)# we did not receive event
        #self.assertEqual(msclt.ev.message, msg)
        #self.assertEqual(msclt.ev.time.to_datetime(), tid)
        #self.assertEqual(msclt.ev.severity, 500)
        #self.assertEqual(msclt.ev.source_node, self.opc.get_server_node().nodeid)

        #time.sleep(0.1)
        #sub.unsubscribe(handle)
        #sub.delete()


    #def test_get_NamespaceIndex(self):
        #idx = self.opc.get_NamespaceIndex('http://freeua.github.io')
        #self.assertEqual(idx, 1) 

    #def test_use_namespace(self):
        #root = self.opc.get_root_node()
        #idx = self.opc.get_NamespaceIndex('http://freeua.github.io')
        #o = root.add_object(idx, 'test_namespace')
        #self.assertEqual(idx, o.nodeid.NamespaceIndex) 
        #o2 = root.get_child('{}:test_namespace'.format(idx))
        #self.assertEqual(o, o2) 

    def test_non_existing_node(self):
        root = self.opc.get_root_node()
        with self.assertRaises(Exception):
            server_time_node = root.get_child(['0:Objects', '0:Server', '0:nonexistingnode'])

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
        self.assertEqual(qn, v.get_name())

    def test_add_string_variable(self):
        objects = self.opc.get_objects_node()
        v = objects.add_variable('ns=3;s=stringid;', '3:stringnodefromstring', [68])
        nid = ua.NodeId('stringid', 3) 
        qn = ua.QualifiedName('stringnodefromstring', 3) 
        self.assertEqual(nid, v.nodeid)
        self.assertEqual(qn, v.get_name())

    def test_add_string_array_variable(self):
        objects = self.opc.get_objects_node()
        v = objects.add_variable('ns=3;s=stringarrayid;', '9:stringarray', ['l', 'b'])
        nid = ua.NodeId('stringarrayid', 3) 
        qn = ua.QualifiedName('stringarray', 9) 
        self.assertEqual(nid, v.nodeid)
        self.assertEqual(qn, v.get_name())
        val = v.get_value()
        self.assertEqual(['l', 'b'], val)

    def test_add_numeric_node(self):
        objects = self.opc.get_objects_node()
        nid = ua.NodeId(9999, 3)
        qn = ua.QualifiedName('AddNodeVar1', 3)
        v1 = objects.add_variable(nid, qn, 0)
        self.assertEqual(nid, v1.nodeid)
        self.assertEqual(qn, v1.get_name())

    def test_add_string_node(self):
        objects = self.opc.get_objects_node()
        qn = ua.QualifiedName('AddNodeVar2', 3)
        nid = ua.NodeId('AddNodeVar2Id', 3)
        v2 = objects.add_variable(nid, qn, 0)
        self.assertEqual(nid, v2.nodeid)
        self.assertEqual(qn, v2.get_name())

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
        self.assertEqual(o.get_name(), qn)

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

    def test_array_value(self):
        o = self.opc.get_objects_node()
        v = o.add_variable(3, 'VariableArrayValue', [1, 2, 3])
        val = v.get_value()
        self.assertEqual([1, 2, 3], val)

    def test_array_size_one_value(self):
        o = self.opc.get_objects_node()
        v = o.add_variable(3, 'VariableArrayValue', [1, 2, 3])
        v.set_value([1])
        val = v.get_value()
        self.assertEqual([1], val) 

    def test_subscription_data_change(self):
        '''
        test subscriptions. This is far too complicated for
        a unittest but, setting up subscriptions requires a lot
        of code, so when we first set it up, it is best 
        to test as many things as possible
        '''
        msclt = MySubHandler()
        cond = msclt.setup()

        o = self.opc.get_objects_node()

        # subscribe to a variable
        startv1 = [1, 2, 3]
        v1 = o.add_variable(3, 'SubscriptionVariableV1', startv1)
        sub = self.opc.create_subscription(100, msclt)
        handle1 = sub.subscribe_data_change(v1)

        # Now check we get the start value
        with cond:
            ret = cond.wait(0.5)
        if sys.version_info.major>2: self.assertEqual(ret, True) # we went into timeout waiting for subcsription callback
        else: pass # XXX
        self.assertEqual(msclt.value, startv1)
        self.assertEqual(msclt.node, v1)

        # modify v1 and check we get value 
        v1.set_value([5])
        with cond:
            ret = cond.wait(0.5)
        if sys.version_info.major>2: self.assertEqual(ret, True) # we went into timeout waiting for subcsription callback
        else: pass # XXX
        self.assertEqual(msclt.node, v1)
        self.assertEqual(msclt.value, [5])

        sub.unsubscribe(handle1)
        sub.delete()

    def test_subscribe_server_time(self):
        msclt = MySubHandler()
        cond = msclt.setup()

        server_time_node = self.opc.get_node(ua.NodeId(ua.ObjectIds.Server_ServerStatus_CurrentTime))

        sub = self.opc.create_subscription(200, msclt)
        handle = sub.subscribe_data_change(server_time_node)

        with cond:
            ret = cond.wait(0.5)
        if sys.version_info.major>2: self.assertEqual(ret, True) # we went into timeout waiting for subcsription callback
        else: pass # XXX
        self.assertEqual(msclt.node, server_time_node)
        delta = datetime.now() - msclt.value 
        self.assertTrue(delta < timedelta(seconds=0.5))

        sub.unsubscribe(handle)
        sub.delete()






class ServerProcess(Thread):
    '''
    Start a server in another process
    '''
    def __init__(self):
        Thread.__init__(self)
        self._exit = Event()
        self.started = Event()
        self._queue = Queue()

    def run(self):
        self.srv = Server()
        self.srv.set_endpoint('opc.tcp://localhost:%d' % port_num1)
        self.srv.start()
        self.started.set()
        while not self._exit.is_set():
            time.sleep(0.1)
            if not self._queue.empty():
                ev = self._queue.get()
                self.srv.trigger_event(ev)
        self.srv.stop()

    def stop(self):
        self._exit.set()

    def trigger_event(self, ev):
        self._queue.put(ev)


class TestClient(unittest.TestCase, CommonTests):
    '''
    Run common tests on client side
    Of course we need a server so we start a server in another 
    process using python Process module
    Tests that can only be run on client side must be defined here
    '''
    @classmethod
    def setUpClass(self):
        # start server in its own process
        global globalserver
        self.srv = globalserver 
        self.srv.start()
        self.srv.started.wait() # let it initialize

        # start client
        self.clt = Client('opc.tcp://localhost:%d' % port_num1)
        self.clt.connect()
        self.opc = self.clt

    @classmethod
    def tearDownClass(self):
        self.clt.disconnect()
        # stop the server in its own process
        self.srv.stop()
        # wait for server to stop, otherwise we may try to start a 
        # new one before this one is really stopped
        self.srv.join()

"""

class TestServer(unittest.TestCase, CommonTests):
    '''
    Run common tests on server side
    Tests that can only be run on server side must be defined here
    '''
    @classmethod
    def setUpClass(self):
        self.srv = Server()
        self.srv.set_endpoint('opc.tcp://localhost:%d' % port_num2)
        self.srv.start()
        self.opc = self.srv 

    @classmethod
    def tearDownClass(self):
        self.srv.stop()
    def test_add_nodes(self):
        objects = self.opc.get_objects_node()
        f = objects.add_folder(3, 'MyFolder')
        v = f.add_variable(3, 'MyVariable', 6)
        p = f.add_property(3, 'MyProperty', 10)
        childs = f.get_children()
        self.assertTrue(v in childs)
        self.assertTrue(p in childs)

'''
    def test_register_namespace(self):
        uri = 'http://mycustom.Namespace.com'
        idx1 = self.opc.register_namespace(uri)
        idx2 = self.opc.get_NamespaceIndex(uri)
        self.assertEqual(idx1, idx2) 

    def test_register_use_namespace(self):
        uri = 'http://my_very_custom.Namespace.com'
        idx = self.opc.register_namespace(uri)
        root = self.opc.get_root_node()
        myvar = root.add_variable(idx, 'var_in_custom_namespace', [5])
        myid = myvar.nodeid
        self.assertEqual(idx, myid.NamespaceIndex) 
        #self.assertEqual(uri, myid.Namespace_uri) #FIXME: should return uri!!!
'''
"""



if __name__ == '__main__':
    logging.basicConfig(level=logging.WARN)
    globalserver = ServerProcess() #server process will be started by client tests
    try:
        sclt = SubHandler()
        unittest.main(verbosity=3)
    finally:
        globalserver.stop()

