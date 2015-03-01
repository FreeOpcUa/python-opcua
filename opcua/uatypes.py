"""
implement ua datatypes
"""
from datetime import datetime, timedelta
import uuid
import struct 

def pack_string(string):
    length = len(string)
    if length == 0:
        return struct.pack("<i", -1) 
    if not type(string) is bytes:
        string = string.encode()
    return struct.pack("<i", length) + string

pack_bytes = pack_string

def unpack_bytes(data):
    length = struct.unpack("<i", data.read(4))[0]
    if length == -1:
        return b''
    return data.read(length)

def unpack_string(data):
    b = unpack_bytes(data)
    return str(b)
    #return b.decode("utf-8")

def unpack_array(data, uatype):
    pass


def test_bit(data, offset):
    mask = 1 << offset
    return(data & mask)

def set_bit(data, offset):
    mask = 1 << offset
    return(data | mask)

class Guid(object):
    def __init__(self):
        self.uuid = uuid.uuid4()

    def to_binary(self):
        return self.uuid.bytes 

    @staticmethod
    def from_binary(data):
        g = Guid()
        g.uuid = uuid.UUID(bytes=data.read(16))
        return g


class StatusCode(object):
    def __init__(self):
        self.data = b""

    def to_binary(self):
        return struct.pack("!I", self.data)

    @staticmethod 
    def from_binary(data):
        sc = StatusCode()
        sc.data = struct.unpack("!I", data.read(4))[0]
        return sc

    def __str__(self):
        return 'StatusCode({})'.format(self.data)

    __repr__ = __str__

class NodeIdType(object):
    TwoByte = 0
    FourByte = 1
    Numeric = 2
    String = 3
    Guid = 4
    ByteString = 5


class NodeId(object):
    def __init__(self, namespaceidx=None, identifier=None, nodeidtype=None):
        if namespaceidx is None:
            self.NamespaceIndex = 0
            self.Identifier = 0
            self.NodeIdType = NodeIdType.TwoByte
            return
        self.NamespaceIndex = namespaceidx
        self.Identifier = identifier
        if nodeidtype is None:
            if type(self.Identifier) == int:
                self.NodeIdType = NodeIdType.Numeric
            elif type(self.Identifier) == str:
                self.NodeIdType = NodeIdType.String
            elif type(self.Identifier) == bytes:
                self.NodeIdType = NodeIdType.ByteString
            else:
                raise Exception("NodeId: Could not guess type of NodeId, set NodeIdType")
        else:
            self.NodeIdType = nodeidtype
        self.NamespaceUri = ""
        self.ServerIndex = 0

    def to_string(self):
        #FIXME:
        types = "ERROR"
        if self.NodeIdType == NodeIdType.Numeric:
            types = "i"
        elif self.NodeIdType == NodeIdType.String:
            types = "s"
        elif self.NodeIdType == NodeIdType.TwoByte:
            types = "twobyte"
        elif self.NodeIdType == NodeIdType.FourByte:
            types = "foubyte"
        elif self.NodeIdType == NodeIdType.Guid:
            types = "g"
        elif self.NodeIdType == NodeIdType.ByteString:
            types = "bytestring"
        return "ns={}; {}={}".format(self.NamespaceIndex, types, self.Identifier)

    def __str__(self):
        return "NodeId({})".format(self.to_string())
    __repr__ = __str__

    def to_binary(self):
        b = []
        b.append(struct.pack("<B", self.NodeIdType))
        if self.NodeIdType == NodeIdType.TwoByte:
            b.append(struct.pack("<B", self.Identifier))
        elif self.NodeIdType == NodeIdType.FourByte:
            b.append(struct.pack("<BH", self.NamespaceIndex, self.Identifier))
        elif self.NodeIdType == NodeIdType.Numeric:
            b.append(struct.pack("<HI", self.NamespaceIndex, self.Identifier))
        elif self.NodeIdType == NodeIdType.String:
            b.append(struct.pack("<H", self.NamespaceIndex))
            b.append(pack_string(self.Identifier))
        else:
            b.append(struct.pack("<H", self.NamespaceIndex))
            b.append(self.Identifier.to_binary())
        return b"".join(b)

    @staticmethod
    def from_binary(data):
        nid = NodeId()
        encoding = struct.unpack("<B", data.read(1))[0]
        nid.NodeIdType = encoding & 0b00111111

        if nid.NodeIdType == NodeIdType.TwoByte:
            nid.Identifier = struct.unpack("<B", data.read(1))[0]
        elif nid.NodeIdType == NodeIdType.FourByte:
            nid.NamespaceIndex, nid.Identifier = struct.unpack("<BH", data.read(3))
        elif nid.NodeIdType == NodeIdType.Numeric:
            nid.NamespaceIndex, nid.Identifier = struct.unpack("<HI", data.read(6))
        elif nid.NodeIdType == NodeIdType.String:
            nid.NamespaceIndex = struct.unpack("<H", data.read(2))
            nid.Identifier = unpack_string(data)
        elif nid.NodeIdType == NodeIdType.ByteString:
            nid.NamespaceIndex = struct.unpack("<H", data.read(2))
            nid.Identifier = unpack_bytes(data)
        elif nid.NodeIdType == NodeIdType.Guid:
            nid.NamespaceIndex = struct.unpack("<H", data.read(2))
            nid.Identifier = Guid.from_binary(data)
        else:
            raise Exception("Unknown NodeId encoding: " + str(nid.NodeIdType))

        if test_bit(encoding, 6):
            nid.NamespaceUri = unpack_string(data)
        if test_bit(encoding, 7):
            nid.ServerIndex = struct.unpack("<I", data.read(1))[0]

        return nid

ExpandedNodeId = NodeId

class DateTime(object):
    def __init__(self, data=None):
        if data is None:
            self.data = self._to1601(datetime.now()) 
        else:
            self.data = data

    def _to1601(self, dt):
        return (dt - datetime(1601,1,1,0,0)).total_seconds() * 10**7

    def to_datetime(self):
        us = self.data / 10.0
        print(us)
        print(timedelta(microseconds=us))
        return datetime(1601,1,1) + timedelta(microseconds=us)

    @staticmethod
    def now():
        return DateTime.from_datetime(datetime.now())

    @staticmethod
    def from_datetime(pydt):
        dt = DateTime()
        dt.data = dt._to1601(pydt) 
        return dt

    def to_binary(self):
        return struct.pack("<d", self.data)
    
    @staticmethod
    def from_binary(data):
        d = DateTime()
        d.data = struct.unpack("<d", data.read(8))[0]
        return d

    @staticmethod
    def from_ctime(data):
        return DateTime.from_datetime(datetime.fromtimestamp(data))

    def __str__(self):
        return "Datetime({})".format(self.to_datetime().isoformat())
    __repr__ = __str__

"""
class ExtensionObject(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.Encoding = 0
        self.Body = b''
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        if self.Body:
            set_bit(self.Encoding, 0)
        packet.append(struct.pack('<B', self.Encoding))
        if self.Body:
            pack_bytes(self.Body)
        
        @staticmethod
        def from_binary(self, data):
            obj = ExtensionObject()
            obj.TypeId = ExpandedNodeId.from_binary(data)
            obj.Encoding = struct.unpack('<B', data.read(1))[0]
            if test_but(obj.Encoding, 0):
                obj.Body = unpack_string(data)
            return obj
"""

