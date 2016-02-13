import unittest
import subprocess

from opcua import Server


port_num = 48530


class TestCmdLines(unittest.TestCase):

    '''
    Test command lines
    '''
    @classmethod
    def setUpClass(self):
        self.srv = Server()
        self.srv_url = 'opc.tcp://localhost:%d' % port_num
        self.srv.set_endpoint(self.srv_url)
        objects = self.srv.get_objects_node()
        obj = objects.add_object(4, "directory")
        var = obj.add_variable(4, "variable", 1.999)
        var2 = obj.add_variable(4, "variable2", 1.777)
        var2.set_writable()
        self.srv.start()

    def test_uals(self):
        s = subprocess.check_output(["python", "tools/uals", "--url", self.srv_url])
        self.assertIn(b"i=85", s)
        self.assertNotIn(b"i=89", s)
        self.assertNotIn(b"1.999", s)
        s = subprocess.check_output(["python", "tools/uals", "--url", self.srv_url, "-d", "3"])
        self.assertIn(b"1.999", s)

    def test_uaread(self):
        s = subprocess.check_output(["python", "tools/uaread", "--url", self.srv_url, "--path", "0:Objects,4:directory,4:variable"])
        self.assertIn(b"1.999", s)

    def test_uawrite(self):
        s = subprocess.check_output(["python", "tools/uawrite", "--url", self.srv_url, "--path", "0:Objects,4:directory,4:variable2", "1.789"])
        s = subprocess.check_output(["python", "tools/uaread", "--url", self.srv_url, "--path", "0:Objects,4:directory,4:variable2"])
        self.assertIn(b"1.789", s)
        self.assertNotIn(b"1.999", s)

    def test_uadiscover(self):
        s = subprocess.check_output(["python", "tools/uadiscover", "--url", self.srv_url])
        self.assertIn(b"opc.tcp://localhost", s)
        self.assertIn(b"FreeOpcUa", s)
        self.assertIn(b"urn:freeopcua:python:server", s)

    @classmethod
    def tearDownClass(self):
        self.srv.stop()


