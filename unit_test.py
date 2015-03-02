import io
import unittest
import opcua.uaprotocol as ua

class Unit(unittest.TestCase):

    def test_bytestring(self):
        bs = ua.ByteString()
        if bs:
            raise AssertionError()
        s = b"this is a test string"
        bs.data = s
        if not bs:
            raise AssertionError()

        stream = io.BytesIO(s)
        d = bs.to_binary()
        nbs = ua.ByteString.from_binary(io.BytesIO(d))
        self.assertEqual(bs.data, nbs.data)
 
    def test_guid(self):
        g = ua.Guid()
        sc = ua.StatusCode()
  

    def test_nodeid(self):
        nid = ua.NodeId()
        self.assertEqual(nid.NodeIdType, ua.NodeIdType.TwoByte) 
        nid = ua.NodeId(0, 446, ua.NodeIdType.FourByte)
        self.assertEqual(nid.NodeIdType, ua.NodeIdType.FourByte) 
        d = nid.to_binary()
        new_nid = nid.from_binary(io.BytesIO(d))
        self.assertEqual(new_nid.NodeIdType, ua.NodeIdType.FourByte) 
        self.assertEqual(new_nid.Identifier, 446) 

    def test_expandednodeid(self):
        nid = ua.ExpandedNodeId()
        self.assertEqual(nid.NodeIdType, ua.NodeIdType.TwoByte) 
        print(nid.to_binary())

    def test_extension_object(self):
        obj = ua.ExtensionObject()
        d = obj.to_binary()
        print(d)
    
    def test_datetime(self):
        dt = ua.DateTime()
        print(dt)
        n = ua.DateTime.now()
        print(n)
        d = n.to_binary()
        self.assertEqual(len(d), 8)

    def test_qualified_name(self):
        qn = ua.QualifiedName("Root", 0)
        print(qn)
        qn.to_binary()

    def test_variant(self):
        qn = ua.QualifiedName("Root", 0)
        v = Variant



if __name__ == '__main__':
    unittest.main(verbosity=3)




