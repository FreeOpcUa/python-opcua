"""
Test an OPC-UA server with freeopcua python client
"""
import logging
import sys
import unittest
from concurrent.futures import Future
from datetime import datetime
from datetime import timedelta
import time

from opcua import ua
from opcua import Client


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


class MySubHandler2(object):
    def __init__(self):
        self.results = [] 

    def datachange_notification(self, node, val, data):
        self.results.append((node, val))

    def event_notification(self, event):
        self.results.append(event)


def connect(func):
    def wrapper(self):
        try:
            client = Client(URL)
            client.connect()
            func(self, client)
        finally:
            client.disconnect()
    return wrapper


class Tests(unittest.TestCase):

    def test_connect_anonymous(self):
        c = Client(URL)
        c.connect()
        c.disconnect()

    def FINISH_test_connect_basic256(self):
        c = Client(URL)
        c.set_security_string("basic256,sign,XXXX")
        c.connect()
        c.disconnect()

    def test_find_servers(self):
        c = Client(URL)
        res = c.connect_and_find_servers()
        self.assertTrue(len(res) > 0)

    def test_find_endpoints(self):
        c = Client(URL)
        res = c.connect_and_get_server_endpoints()
        self.assertTrue(len(res) > 0)

    @connect
    def test_get_root(self, client):
        root = client.get_root_node()
        self.assertEqual(root.get_browse_name(), ua.QualifiedName("Root", 0))

    @connect
    def test_get_root_children(self, client):
        root = client.get_root_node()
        childs = root.get_children()
        self.assertTrue(len(childs) > 2)

    @connect
    def test_get_namespace_array(self, client):
        array = client.get_namespace_array()
        self.assertTrue(len(array) > 0)

    @connect
    def test_get_server_node(self, client):
        srv = client.get_server_node()
        self.assertEqual(srv.get_browse_name(), ua.QualifiedName("Server", 0))
        #childs = srv.get_children()
        #self.assertTrue(len(childs) > 4)

    @connect
    def test_browsepathtonodeid(self, client):
        root = client.get_root_node()
        node = root.get_child(["0:Objects", "0:Server" , "0:ServerArray"])
        self.assertEqual(node.get_browse_name(), ua.QualifiedName("ServerArray", 0))

    @connect
    def test_subscribe_server_time(self, client):
        msclt = MySubHandler()

        server_time_node = client.get_node(ua.NodeId(ua.ObjectIds.Server_ServerStatus_CurrentTime))
        sub = client.create_subscription(200, msclt)
        handle = sub.subscribe_data_change(server_time_node)

        node, val, data = msclt.future.result()
        self.assertEqual(node, server_time_node)
        delta = datetime.utcnow() - val
        print("Timedelta is ", delta)
        #self.assertTrue(delta < timedelta(seconds=2))

        sub.unsubscribe(handle)
        sub.delete()


if __name__ == "__main__":

    logging.basicConfig(level=logging.WARN)
    # FIXME add better arguments parsing with possibility to specify
    # username and password and encryption
    if len(sys.argv) < 2:
        print("This script is meant to test compatibilty to a server with freeopcua python client library")
        print("Usage: test_server.py url")
        sys.exit(1)
    else:
        URL = sys.argv[1]

    unittest.main(verbosity=30, argv=sys.argv[:1])

