"""
implement ua datatypes
"""

import uuid
import struct 

def pack_string(string):
    length = len(string)
    if not type(string) is bytes:
        string = string.encode()
    b.append(struct.pack("<i{}s".format(length), length, string))

def unpack_bytes(data):
    length = struct.unpack("<i", data.read(4))[0]
    return struct.unpack("<{}s", data.read(length))[0]

def unpack_string(data):
    b = unpack_bytes(data)
    return b.encode("utf-8")

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

    def from_binary(self, data):
        self.uuid = uuid.UUID(bytes=data.read(16))

class ByteString(object):
    def __init__(self):
        self.data = b""

    def to_binary(self):
        if not self.data:
            return struct.pack("!i", -1)
        size = len(self.data)
        data = struct.pack("!i", size)
        data += struct.pack("!{}B".format(size), *self.data)
        return data

    def from_binary(self, data):
        size = struct.unpack("!i", data.read(4))[0]
        self.data = struct.unpack("!{}c".format(size), data.read(size))
        self.data = b"".join(self.data)

class StatusCode(object):
    def __init__(self):
        self.data = b""

    def to_binary(self):
        return struct.pack("!I", self.data)
    
    def from_binary(self, data):
        self.data = struct.unpack("!I", data.read(4))[0]

class NodeIdType(object):
    TwoByte = 0
    FourByte = 1
    Numeric = 2
    String = 3
    Guid = 4
    ByteString = 5


class NodeId(object):
    def __init__(self, namespaceidx=0, identifier=0, nodeidtype=None):
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
        b.append(struct.pack("<BH", self.NodeIdType, self.NamespaceIndex))
        if self.NodeIdType == NodeIdType.TwoByte:
            b.append(struct.pack("<B", self.Identifier))
        elif self.NodeIdType == NodeIdType.FourByte:
            b.append(struct.pack("<H", self.Identifier))
        elif self.NodeIdType == NodeIdType.Numeric:
            b.append(struct.pack("<I", self.Identifier))
        elif self.NodeIdType == NodeIdType.String:
            b.append(pack_string(self._identifier))
        else:
            b.append(self.Indentifier.to_binary())
        return b"".join(b)

    def from_binary(self, data):
        encoding, self.NamespaceIndex = struct.unpack("<BH", data.read(3))
        self.NodeIdType = encoding & 0b00111111

        if self.NodeIdType == NodeIdType.TwoByte:
            self.Identifier = struct.unpack("<B", data.read(1))[0]
        elif self.NodeIdType == NodeIdType.FourByte:
            self.Identifier = struct.unpack("<B", data.read(1))[0]
        elif self.NodeIdType == NodeIdType.Numeric:
            self.Identifier = struct.unpack("<B", data.read(1))[0]
        elif self.NodeIdType == NodeIdType.String:
            self.Identifier = unpack_string(data)
        elif self.NodeIdType == NodeIdType.ByteString:
            self.Identifier = ByteString.from_binary(data)
        elif self.NodeIdType == NodeIdType.Guid:
            self.Identifier = Guid.from_binary(data)
        else:
            raise Exception("Unknown NodeId encoding: " + str(self.NodeIdType))

        if test_bit(encoding, 6):
            self.NamespaceURI = unpack_string(data)
        if test_bit(encoding, 7):
            self.ServerIndex = struct.unpack("<I", data.read(1))[0]

ExpandedNodeId = NodeId

if __name__ == "__main__":
    import io
    from IPython import embed
    bs = ByteString()
    g = Guid()
    sc = StatusCode()
    s = b"this is a test string"
    stream = io.BytesIO(s)
    bs.data = s
    d=bs.to_binary()
    print(d)
    bs.from_binary(io.BytesIO(d))
    nid = NodeId()
    print(nid)
    nid.to_binary()
    nid = NodeId(1, 4, NodeIdType.FourByte)
    print(nid)
    d = nid.to_binary()
    print(nid.from_binary(io.BytesIO(d)))

    embed()
