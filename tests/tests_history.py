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


    def test_history_read(self):
        o = self.srv.get_objects_node()
        vals = [i for i in range(20)]
        var = o.add_variable(3, "history_var", 0)
        self.srv.iserver.enable_history(var, period=None, count=10)
        for i in vals:
            var.set_value(i)
        time.sleep(1)

        now = datetime.now()
        old = now - timedelta(days=6)

        res = var.read_raw_history(None, now, 2)
        self.assertEqual(len(res), 2)
        self.assertEqual(res[-1].Value.Value, vals[-1])

        res = var.read_raw_history(old, now, 0)
        self.assertEqual(len(res), 20)
        self.assertEqual(res[-1].Value.Value, vals[-1])
        self.assertEqual(res[0].Value.Value, vals[0])

        res = var.read_raw_history(old, now, 5)
        self.assertEqual(len(res), 5)
        self.assertEqual(res[-1].Value.Value, vals[4])
        self.assertEqual(res[0].Value.Value, vals[0])



class TestHistory(unittest.TestCase, HistoryCommon):

    '''
    '''
    @classmethod
    def setUpClass(self):
        # start our own server
        self.srv = Server()
        self.srv.set_endpoint('opc.tcp://localhost:%d' % port_num1)
        self.srv.start()

        # start anonymous client
        self.clt = Client('opc.tcp://localhost:%d' % port_num1)
        self.clt.connect()

    @classmethod
    def tearDownClass(self):
        self.clt.disconnect()
        self.srv.stop()


class TestHistorySQL(unittest.TestCase, HistoryCommon):

    '''
    '''
    @classmethod
    def setUpClass(self):
        # start our own server
        self.srv = Server()
        self.srv.set_endpoint('opc.tcp://localhost:%d' % port_num1)
        self.srv.iserver.history_manager.set_storage(HistorySQLite())
        self.srv.start()

        # start anonymous client
        self.clt = Client('opc.tcp://localhost:%d' % port_num1)
        self.clt.connect()

    @classmethod
    def tearDownClass(self):
        self.clt.disconnect()
        self.srv.stop()








