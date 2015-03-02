"""
implement ua datatypes
"""
from enum import Enum
from datetime import datetime, timedelta
import uuid
import struct 

def uatype_to_fmt(uatype):
    if uatype == "String":
        return "s"
    elif uatype == "CharArray":
        return "s"
    elif uatype == "Char":
        return "s"
    elif uatype == "SByte":
        return "B"
    elif uatype == "Int6":
        return "b"
    elif uatype == "Int8":
        return "b"
    elif uatype == "Int16":
        return "h"
    elif uatype == "Int32":
        return "i"
    elif uatype == "Int64":
        return "q"
    elif uatype == "UInt8":
        return "B"
    elif uatype == "UInt16":
        return "H"
    elif uatype == "UInt32":
        return "I"
    elif uatype == "UInt64":
        return "Q"
    elif uatype == "Boolean":
        return "?"
    elif uatype == "Double":
        return "d"
    elif uatype == "Float":
        return "f"
    elif uatype == "Byte":
        return "B"
    else:
        #field = self.model.get_enum(obj.uatype)
        #return self.to_fmt(field)
        #print("Error unknown uatype: ", obj.uatype)
        raise Exception("Error unknown uatype: "+ uatype)

def pack_uatype_array(uatype, value):
    if value is None:
        return struct.pack("<i", -1)
    b = []
    b.append(struct.pack("<i", len(value)))
    for val in value:
        b.append(pack_uatype(uatype, val))

def pack_uatype(uatype, value):
    if uatype == "String":
        return pack_string(value)
    elif uatype in ("CharArray", "ByteString"):
        return pack_bytes(value)
    else:
        fmt = uatype_to_fmt(uatype)
        return struct.pack(fmt, value)

def unpack_uatype(uatype, data):
    if uatype == "String":
        return unpack_string(data)
    elif uatype in ("CharArray", "ByteString"):
        return unpack_bytes(data)
    else:
        fmt = uatype_to_fmt(uatype)
        size = struct.calcsize(fmt)
        return struct.unpack(fmt, data.read(size))[0]

def unpack_uatype_array(uatype, data):
    length = struct.unpack('<i', data.read(4))[0]
    if length == -1:
        return None
    else:
        result = []
        for i in range(0, length):
            result.append(unpack_uatype(uatype, data))
        return result




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
    def __init__(self, identifier=None, namespaceidx=0, nodeidtype=None):
        if identifier is None:
            self.Identifier = 0
            self.NamespaceIndex = 0
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

class TwoByteNodeId(NodeId):
    def __init__(self, identifier):
        NodeId.__init__(self, identifier, 0, NodeIdType.TwoByte)

class FourByteNodeId(NodeId):
    def __init__(self, identifier, namespace=0):
        NodeId.__init__(self, identifier, namespace, NodeIdType.FourByte)

ExpandedNodeId = NodeId

class QualifiedName(object):
    '''
    A string qualified with a namespace index.
    '''
    def __init__(self, name="", namespaceidx=0):
        self.NamespaceIndex = namespaceidx
        self.Name = name
    
    def to_binary(self):
        packet = []
        fmt = '<H'
        packet.append(struct.pack(fmt, self.NamespaceIndex))
        packet.append(pack_string(self.Name))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = QualifiedName()
        fmt = '<H'
        obj.NamespaceIndex = struct.unpack(fmt, data.read(2))[0]
        obj.Name = unpack_string(data)
        return obj
    
    def __str__(self):
        return 'QualifiedName({}:{})'.format(self.NamespaceIndex, self.Name)
    
    __repr__ = __str__
 
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
class VariantType(Enum):
    '''
    The possible types of a variant.
    '''
    Null = 0
    Boolean = 1
    SByte = 2
    Byte = 3
    Int16 = 5
    UInt16 = 5
    Int32 = 6
    UInt32 = 7
    Int64 = 8
    UInt64 = 9
    Float = 10
    Double = 11
    String = 12
    DateTime = 13
    Guid = 14
    ByteString = 15
    XmlElement = 16
    NodeId = 17
    ExpandedNodeId = 18
    StatusCode = 19
    DiagnosticInfo = 20
    QualifiedName = 21
    LocalizedText = 22
    ExtensionObject = 23
    DataValue = 24
    Variant = 25

class Variant(object):
    def __init__(self, value=None, varianttype=None):
        self.Encoding = 0
        self.Value = value
        if varianttype is None:
            if self.Value is None:
                self.VariantType = VariantType.Null
            elif type(self.Value) == float:
                self.VariantType = VariantType.Double
            elif type(self.Value) == int:
                self.VariantType = VariantType.UInt64
            elif type(self.Value) == str:
                self.VariantType = VariantType.String
            elif type(self.Value) == bytes:
                self.VariantType = VariantType.ByteString
            else:
                raise Exception("Could not guess variant type, specify type")
        self.VariantType = varianttype

    def __str__(self):
        return "Variant(val:{},type:{})".format(self.Value, self.VariantType)
    __repr__ = __str__

    def to_binary(self):
        b = []
        mask = self.Encoding & 0b01111111
        self.Encoding = (self.VariantType.value | mask)
        if self.Value is None:
            return
        if type(self.Value) in (list, tuple):
            self.Encoding |= (1 << 7)
            b.append(pack_uatype_array(self.VariantType.name, self.Value))
        else:
            b.append(pack_uatype(self.VariantType.name, self.Value))
        b.insert(0, struct.pack("<B", self.Encoding))
        return b"".join(b)

    @staticmethod
    def from_binary(data):
        obj = Variant()
        obj.Encoding = unpack_uatype('UInt8', data)
        val = obj.Encoding & 0b01111111
        self.VariantType = VariantType(val)
        if obj.Encoding & (1 << 7):
            obj.Value = unpack_uatype_array(self.VariantType.name, data)
        else:
            obj.Value = unpack_uatype(self.VariantType.name, data)
        return obj

        

