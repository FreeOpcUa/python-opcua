import time
from datetime import datetime, timedelta
import unittest

from opcua import Client
from opcua import Server
from opcua import ua
from opcua.server.history_sql import HistorySQLite

from tests_common import CommonTests, add_server_methods

port_num1 = 48530
port_num2 = 48530



class HistoryCommon(object):
    srv = Server
    clt = Client

    def start_server_and_client(self):
        self.srv = Server()
        self.srv.set_endpoint('opc.tcp://localhost:%d' % port_num1)
        self.srv.start()

        self.clt = Client('opc.tcp://localhost:%d' % port_num1)
        self.clt.connect()

    def stop_server_and_client(self):
        self.clt.disconnect()
        self.srv.stop()

    def create_var(self):
        o = self.srv.get_objects_node()
        self.values = [i for i in range(20)]
        self.var = o.add_variable(3, "history_var", 0)
        self.srv.iserver.enable_history(self.var, period=None, count=10)
        for i in self.values:
            self.var.set_value(i)
        time.sleep(1)

    def test_history_read_one(self):
        res = self.var.read_raw_history(None, None, 1)
        self.assertEqual(len(res), 1)
        self.assertEqual(res[0].Value.Value, self.values[-1])

    def test_history_read_none(self):
        # FIXME not sure this once is supported by spec
        res = self.var.read_raw_history(None, None, 0)
        self.assertEqual(len(res), 20)
        self.assertEqual(res[0].Value.Value, self.values[0])
        self.assertEqual(res[-1].Value.Value, self.values[-1])

    def test_history_read_last_3(self):
        res = self.var.read_raw_history(None, None, 3)
        self.assertEqual(len(res), 3)
        self.assertEqual(res[-1].Value.Value, self.values[-1])
        self.assertEqual(res[0].Value.Value, self.values[-3])

    def test_history_read_all2(self):
        res = self.var.read_raw_history(None, None, 9999)
        self.assertEqual(len(res), 20)
        self.assertEqual(res[-1].Value.Value, self.values[-1])
        self.assertEqual(res[0].Value.Value, self.values[0])
 
    def test_history_read_2_with_end(self):
        now = datetime.utcnow()
        old = now - timedelta(days=6)

        res = self.var.read_raw_history(None, now, 2)
        self.assertEqual(len(res), 2)
        self.assertEqual(res[-1].Value.Value, self.values[-1])
    
    def test_history_read_all(self):
        now = datetime.utcnow()
        old = now - timedelta(days=6)

        res = self.var.read_raw_history(old, now, 0)
        self.assertEqual(len(res), 20)
        self.assertEqual(res[-1].Value.Value, self.values[-1])
        self.assertEqual(res[0].Value.Value, self.values[0])

    def test_history_read_5_in_timeframe(self):
        now = datetime.utcnow()
        old = now - timedelta(days=6)

        res = self.var.read_raw_history(old, now, 5)
        self.assertEqual(len(res), 5)
        self.assertEqual(res[-1].Value.Value, self.values[4])
        self.assertEqual(res[0].Value.Value, self.values[0])



class TestHistory(unittest.TestCase, HistoryCommon):

    @classmethod
    def setUpClass(self):
        self.start_server_and_client(self)
        self.create_var(self)

    @classmethod
    def tearDownClass(self):
        self.stop_server_and_client(self)


class TestHistorySQL(unittest.TestCase, HistoryCommon):
    @classmethod
    def setUpClass(self):
        self.start_server_and_client(self)
        self.srv.iserver.history_manager.set_storage(HistorySQLite(":memory:"))
        self.create_var(self)

    @classmethod
    def tearDownClass(self):
        self.stop_server_and_client(self)










