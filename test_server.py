"""
Test an OPC-UA server with freeopcua python client
"""
import logging
import sys
import unittest

from opcua import ua
from opcua import Client


class MySubHandler(object):
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

if __name__ == "__main__":

    logging.basicConfig(level=logging.WARN)
    # FIXME add better arguments parsing with possibility to specify username and password
    if len(sys.argv) < 2:
        print("Usage: test_server.py url")
        sys.exit(1)
    else:
        URL = sys.argv[1]

    unittest.main(verbosity=30, argv=sys.argv[:1])

if __name__ == "__main__":

    logging.basicConfig(level=logging.WARN)
    # FIXME add better arguments parsing with possibility to specify username and password
    if len(sys.argv) < 2:
        print("Usage: test_server.py url")
        sys.exit(1)
    else:
        URL = sys.argv[1]

    unittest.main(verbosity=30, argv=sys.argv[:1])

