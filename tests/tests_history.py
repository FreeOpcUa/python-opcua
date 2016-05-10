import time
from datetime import datetime, timedelta
import unittest

from opcua import Client
from opcua import Server
from opcua import ua

from opcua.server.history_sql import HistorySQLite

from tests_common import CommonTests, add_server_methods

from opcua.common.subscription import get_event_properties_from_type_node as get_props

port_num1 = 48530
port_num2 = 48530



class HistoryCommon(object):
    srv = Server
    clt = Client

    @classmethod
    def start_server_and_client(cls):
        cls.srv = Server()
        cls.srv.set_endpoint('opc.tcp://localhost:%d' % port_num1)
        cls.srv.start()

        cls.clt = Client('opc.tcp://localhost:%d' % port_num1)
        cls.clt.connect()

    @classmethod
    def stop_server_and_client(cls):
        cls.clt.disconnect()
        cls.srv.stop()

    @classmethod
    def create_var(cls):
        o = cls.srv.get_objects_node()
        cls.values = [i for i in range(20)]
        cls.var = o.add_variable(3, "history_var", 0)
        cls.srv.iserver.enable_history_data_change(cls.var, period=None, count=10)
        for i in cls.values:
            cls.var.set_value(i)
        time.sleep(1)

    @classmethod
    def create_srv_events(cls):
        cls.ev_values = [i for i in range(20)]
        cls.srvevgen = cls.srv.get_event_generator()

        # for now we need to build our own filter explicitly because node class can't do it
        cls.evfilter = ua.EventFilter()
        ev_type_node = cls.srv.get_node(cls.srvevgen.event.EventType)
        for ev_property in get_props(ev_type_node):
            op = ua.SimpleAttributeOperand()
            op.TypeDefinitionId = ev_type_node.nodeid
            op.AttributeId = ua.AttributeIds.Value
            op.BrowsePath = [ev_property.get_browse_name()]
            cls.evfilter.SelectClauses.append(op)

        cls.revevfilter = ua.EventFilter()
        for ev_property in reversed(get_props(ev_type_node)):
            op = ua.SimpleAttributeOperand()
            op.TypeDefinitionId = ev_type_node.nodeid
            op.AttributeId = ua.AttributeIds.Value
            op.BrowsePath = [ev_property.get_browse_name()]
            cls.revevfilter.SelectClauses.append(op)

        cls.srv_node = cls.srv.get_node(ua.ObjectIds.Server)
        cls.srv.iserver.enable_history_event(cls.srv_node, period=None)

        for i in cls.ev_values:
            cls.srvevgen.event.Severity = cls.ev_values[i]
            cls.srvevgen.trigger(message="test message")
            time.sleep(.1)
        time.sleep(2)

    # no start and no end is not defined by spec, return reverse order
    def test_history_var_read_one(self):
        # Spec says that at least two parameters should be provided, so
        # this one is out of spec
        res = self.var.read_raw_history(None, None, 1)
        self.assertEqual(len(res), 1)
        self.assertEqual(res[0].Value.Value, self.values[-1])

    # no start and no end is not defined by spec, return reverse order
    def test_history_var_read_none(self):
        res = self.var.read_raw_history(None, None, 0)
        self.assertEqual(len(res), 20)
        self.assertEqual(res[0].Value.Value, self.values[-1])
        self.assertEqual(res[-1].Value.Value, self.values[0])

    # no start and no end is not defined by spec, return reverse order
    def test_history_var_read_last_3(self):
        res = self.var.read_raw_history(None, None, 3)
        self.assertEqual(len(res), 3)
        self.assertEqual(res[-1].Value.Value, self.values[-3])
        self.assertEqual(res[0].Value.Value, self.values[-1])

    # no start and no end is not defined by spec, return reverse order
    def test_history_var_read_all2(self):
        res = self.var.read_raw_history(None, None, 9999)
        self.assertEqual(len(res), 20)
        self.assertEqual(res[-1].Value.Value, self.values[0])
        self.assertEqual(res[0].Value.Value, self.values[-1])

    # only has end time, should return reverse order
    def test_history_var_read_2_with_end(self):
        now = datetime.utcnow()
        old = now - timedelta(days=6)

        res = self.var.read_raw_history(None, now, 2)
        self.assertEqual(len(res), 2)
        self.assertEqual(res[-1].Value.Value, self.values[-2])
    
    # both start and endtime, return from start to end
    def test_history_var_read_all(self):
        now = datetime.utcnow()
        old = now - timedelta(days=6)

        res = self.var.read_raw_history(old, now, 0)
        self.assertEqual(len(res), 20)
        self.assertEqual(res[-1].Value.Value, self.values[-1])
        self.assertEqual(res[0].Value.Value, self.values[0])

    def test_history_var_read_5_in_timeframe(self):
        now = datetime.utcnow()
        old = now - timedelta(days=6)

        res = self.var.read_raw_history(old, now, 5)
        self.assertEqual(len(res), 5)
        self.assertEqual(res[-1].Value.Value, self.values[4])
        self.assertEqual(res[0].Value.Value, self.values[0])

    # start time greater than end time, should return reverse order
    def test_history_var_read_5_in_timeframe_start_greater_than_end(self):
        now = datetime.utcnow()
        old = now - timedelta(days=6)

        res = self.var.read_raw_history(now, old, 5)
        self.assertEqual(len(res), 5)
        self.assertEqual(res[-1].Value.Value, self.values[-5])
        self.assertEqual(res[0].Value.Value, self.values[-1])
    
    # only start return original order
    def test_history_var_read_6_with_start(self):
        now = datetime.utcnow()
        old = now - timedelta(days=6)
        res = self.var.read_raw_history(old, None, 6)
        self.assertEqual(len(res), 6)
        self.assertEqual(res[-1].Value.Value, self.values[5])
        self.assertEqual(res[0].Value.Value, self.values[0])

    # only start return original order
    def test_history_var_read_all_with_start(self):
        now = datetime.utcnow()
        old = now - timedelta(days=6)
        res = self.var.read_raw_history(old, None, 0)
        self.assertEqual(len(res), 20)
        self.assertEqual(res[-1].Value.Value, self.values[-1])
        self.assertEqual(res[0].Value.Value, self.values[0])

    # only end return reversed order
    def test_history_var_read_all_with_end(self):
        end = datetime.utcnow() + timedelta(days=6)
        res = self.var.read_raw_history(None, end, 0)
        self.assertEqual(len(res), 20)
        self.assertEqual(res[-1].Value.Value, self.values[0])
        self.assertEqual(res[0].Value.Value, self.values[-1])

    # only end return reversed order
    def test_history_var_read_3_with_end(self):
        end = datetime.utcnow() + timedelta(days=6)
        res = self.var.read_raw_history(None, end, 3)
        self.assertEqual(len(res), 3)
        self.assertEqual(res[2].Value.Value, self.values[-3])
        self.assertEqual(res[0].Value.Value, self.values[-1])


class TestHistory(unittest.TestCase, HistoryCommon):

    @classmethod
    def setUpClass(cls):
        cls.start_server_and_client()
        cls.create_var()

    @classmethod
    def tearDownClass(cls):
        cls.stop_server_and_client()


class TestHistorySQL(unittest.TestCase, HistoryCommon):
    @classmethod
    def setUpClass(cls):
        cls.start_server_and_client()
        cls.srv.iserver.history_manager.set_storage(HistorySQLite(":memory:"))
        cls.create_var()
        cls.create_srv_events()

    # ~~~~~~~~~~~~~~~~~~~~~~~ events ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # only has end time, should return reverse order
    def test_history_ev_read_2_with_end(self):
        now = datetime.utcnow()
        old = now - timedelta(days=6)

        res = self.srv_node.read_event_history(self.evfilter, None, now, 2)
        self.assertEqual(len(res), 2)
        self.assertEqual(res[-1].EventFields[8].Value, self.ev_values[-2])

    # both start and end time, return from start to end
    def test_history_ev_read_all(self):
        now = datetime.utcnow()
        old = now - timedelta(days=6)

        res = self.srv_node.read_event_history(self.evfilter, old, now, 0)
        self.assertEqual(len(res), 20)
        self.assertEqual(res[-1].EventFields[8].Value, self.ev_values[-1])
        self.assertEqual(res[0].EventFields[8].Value, self.ev_values[0])

    def test_history_ev_read_5_in_timeframe(self):
        now = datetime.utcnow()
        old = now - timedelta(days=6)

        res = self.srv_node.read_event_history(self.evfilter, old, now, 5)
        self.assertEqual(len(res), 5)
        self.assertEqual(res[-1].EventFields[8].Value, self.ev_values[4])
        self.assertEqual(res[0].EventFields[8].Value, self.ev_values[0])

    # start time greater than end time, should return reverse order
    def test_history_ev_read_5_in_timeframe_start_greater_than_end(self):
        now = datetime.utcnow()
        old = now - timedelta(days=6)

        res = self.srv_node.read_event_history(self.evfilter, now, old, 5)
        self.assertEqual(len(res), 5)
        self.assertEqual(res[-1].EventFields[8].Value, self.ev_values[-5])
        self.assertEqual(res[0].EventFields[8].Value, self.ev_values[-1])

    # only start return original order
    def test_history_ev_read_6_with_start(self):
        now = datetime.utcnow()
        old = now - timedelta(days=6)
        res = self.srv_node.read_event_history(self.evfilter, old, None, 6)
        self.assertEqual(len(res), 6)
        self.assertEqual(res[-1].EventFields[8].Value, self.ev_values[5])
        self.assertEqual(res[0].EventFields[8].Value, self.ev_values[0])

    # only start return original order
    def test_history_ev_read_all_with_start(self):
        now = datetime.utcnow()
        old = now - timedelta(days=6)
        res = self.srv_node.read_event_history(self.evfilter, old, None, 0)
        self.assertEqual(len(res), 20)
        self.assertEqual(res[-1].EventFields[8].Value, self.ev_values[-1])
        self.assertEqual(res[0].EventFields[8].Value, self.ev_values[0])

    # only end return reversed order
    def test_history_ev_read_all_with_end(self):
        end = datetime.utcnow() + timedelta(days=6)
        res = self.srv_node.read_event_history(self.evfilter, None, end, 0)
        self.assertEqual(len(res), 20)
        self.assertEqual(res[-1].EventFields[8].Value, self.ev_values[0])
        self.assertEqual(res[0].EventFields[8].Value, self.ev_values[-1])

    # only end return reversed order
    def test_history_ev_read_3_with_end(self):
        end = datetime.utcnow() + timedelta(days=6)
        res = self.srv_node.read_event_history(self.evfilter, None, end, 3)
        self.assertEqual(len(res), 3)
        self.assertEqual(res[2].EventFields[8].Value, self.ev_values[-3])
        self.assertEqual(res[0].EventFields[8].Value, self.ev_values[-1])

    # reverse event filter select clauses and test that results match the filter order
    def test_history_ev_read_all_filter_order_reversed(self):
        now = datetime.utcnow()
        old = now - timedelta(days=6)
        res = self.srv_node.read_event_history(self.revevfilter, old, None, 0)
        self.assertEqual(len(res), 20)
        self.assertEqual(res[-1].EventFields[0].Value, self.ev_values[-1])
        self.assertEqual(res[0].EventFields[0].Value, self.ev_values[0])

    @classmethod
    def tearDownClass(cls):
        cls.stop_server_and_client()










