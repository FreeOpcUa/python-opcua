"""
implement ua datatypes
"""
import logging
from enum import Enum
from datetime import datetime, timedelta, tzinfo
from calendar import timegm

import uuid
import struct 

import opcua.status_code as status_code

logger = logging.getLogger('opcua.uaprotocol')

#types that will packed and unpacked directly using struct (string, bytes and datetime are handles as special cases
UaTypes = ("Boolean", "SByte", "Byte", "Int8", "UInt8", "Int16", "UInt16", "Int32", "UInt32", "Int64", "UInt64", "Float", "Double")


EPOCH_AS_FILETIME = 116444736000000000  # January 1, 1970 as MS file time
HUNDREDS_OF_NANOSECONDS = 10000000

class UTC(tzinfo):
    """UTC"""
    def utcoffset(self, dt):
        return timedelta(0)

    def tzname(self, dt):
        return "UTC"

    def dst(self, dt):
        return timedelta(0)


#methods copied from  David Buxton <david@gasmark6.com> sample code
def datetime_to_win_epoch(dt):
    if (dt.tzinfo is None) or (dt.tzinfo.utcoffset(dt) is None):
        dt = dt.replace(tzinfo=UTC())
    ft = EPOCH_AS_FILETIME + (timegm(dt.timetuple()) * HUNDREDS_OF_NANOSECONDS)
    return ft + (dt.microsecond * 10)

def win_epoch_to_datetime(epch):
    (s, ns100) = divmod(epch - EPOCH_AS_FILETIME, HUNDREDS_OF_NANOSECONDS)
    dt = datetime.utcfromtimestamp(s)
    dt = dt.replace(microsecond=(ns100 // 10))
    return dt



def uatype_to_fmt(uatype):
    if uatype == "Char":
        return "B"
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
        raise Exception("Error unknown uatype: " + uatype)

def pack_uatype_array(uatype, value):
    if value is None:
        return struct.pack("<i", -1)
    b = []
    b.append(struct.pack("<i", len(value)))
    for val in value:
        b.append(pack_uatype(uatype, val))
    return b"".join(b)

def pack_uatype(uatype, value):
    if uatype == "Null":
        return b''
    elif uatype == "String":
        return pack_string(value)
    elif uatype in ("CharArray", "ByteString"):
        return pack_bytes(value)
    elif uatype == "DateTime":
        epch = datetime_to_win_epoch(value)
        return struct.pack('<q', epch)
    elif uatype in UaTypes:
        fmt = '<' + uatype_to_fmt(uatype)
        return struct.pack(fmt, value)
    else:
        return value.to_binary()

def unpack_uatype(uatype, data):
    if uatype == "String":
        return unpack_string(data)
    elif uatype in ("CharArray", "ByteString"):
        return unpack_bytes(data)
    elif uatype == "DateTime":
        epch = struct.unpack('<q', data.read(8))[0]
        return win_epoch_to_datetime(epch)
    elif uatype in UaTypes:
        fmt = '<' + uatype_to_fmt(uatype)
        size = struct.calcsize(fmt)
        return struct.unpack(fmt, data.read(size))[0]
    else:
        code = "{}.from_binary(data)".format(uatype)
        tmp = eval(code)
        return tmp

def unpack_uatype_array(uatype, data):
    length = struct.unpack('<i', data.read(4))[0]
    if length == -1:
        return None
    else:
        result = []
        for _ in range(0, length):
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
    #return str(b)
    return b.decode("utf-8")

def unpack_array(uatype, data):
    length = struct.unpack('<i', data.read(4))[0]
    array = []
    if length != -1:
        for _ in range(0, length):
            array.append(unpack_uatype(uatype, data))
    return array

def unpack_object_array(objclass, data):
    print("DEPRECATED, unpack_objects_array is deprecated, use unpack_array")
    length = struct.unpack('<i', data.read(4))[0]
    array = []
    if length != -1:
        for _ in range(0, length):
            array.append(objclass.from_binary(data))
    return array
 
def test_bit(data, offset):
    mask = 1 << offset
    return data & mask

def set_bit(data, offset):
    mask = 1 << offset
    return data | mask


class FrozenClass(object):
    """
    make it impossible to add members to a class.
    This is a hack since I found out that most bugs are due to misspelling a variable in protocol
    """
    __isfrozen = False
    def __setattr__(self, key, value):
        if self.__isfrozen and not hasattr(self, key):
            raise TypeError("Error adding member '{}' to class '{}', class is frozen, members are {}".format(key, self.__class__.__name__, self.__dict__.keys()))
        object.__setattr__(self, key, value)

    def _freeze(self):
        self.__isfrozen = True


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
    def __init__(self, value=0):
        self.value = value
        self.name, self.doc = status_code.get_name_and_doc(value)

    def to_binary(self):
        return struct.pack("<I", self.value)

    @staticmethod 
    def from_binary(data):
        val = struct.unpack("<I", data.read(4))[0]
        sc = StatusCode(val)
        return sc

    def check(self):
        if self.value != 0:
            raise Exception("{}({})".format(self.doc, self.name))

    def __str__(self):
        return 'StatusCode({})'.format(self.name)
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
        self.Identifier = identifier
        self.NamespaceIndex = namespaceidx
        self.NodeIdType = nodeidtype
        self.NamespaceUri = ""
        self.ServerIndex = 0
        if self.Identifier is None:
            self.Identifier = 0
            self.NodeIdType = NodeIdType.TwoByte
            return
        if self.NodeIdType is None:
            if type(self.Identifier) == int:
                self.NodeIdType = NodeIdType.Numeric
            elif type(self.Identifier) == str:
                self.NodeIdType = NodeIdType.String
            elif type(self.Identifier) == bytes:
                self.NodeIdType = NodeIdType.ByteString
            else:
                raise Exception("NodeId: Could not guess type of NodeId, set NodeIdType")

    def __key(self):
        if self.NodeIdType in (NodeIdType.TwoByte, NodeIdType.FourByte, NodeIdType.Numeric):#twobyte, fourbyte and numeric may represent the same node
            return self.NamespaceIndex, self.Identifier
        else:
            return self.NodeIdType, self.NamespaceIndex, self.Identifier

    def __eq__(self, node):
        return isinstance(node, NodeId) and self.__key() == node.__key()

    def __hash__(self):
        return hash(self.__key())

    @staticmethod
    def from_string(string):
        l = string.split(";")
        identifier = None
        namespace = 0
        ntype = None
        srv = None
        nsu = None
        for el in l:
            if not el:
                continue
            k, v = el.split("=")
            if k == "ns":
                namespace = int(v)
            elif k == "i":
                ntype = NodeIdType.Numeric
                identifier = int(v)
            elif k == "s":
                ntype = NodeIdType.String
                identifier = v
            elif k == "g":
                ntype = NodeIdType.Guid
                identifier = v
            elif k == "b":
                ntype = NodeIdType.ByteString
                identifier = v
            elif k == "srv":
                srv = v
            elif k == "nsu":
                nsu = v
        if identifier is None:
            raise Exception("Could not parse nodeid string: " + string)
        nodeid = NodeId(identifier, namespace, ntype)
        nodeid.NamespaceUri = nsu
        nodeid.ServerIndex = srv
        return nodeid


    def to_string(self):
        string = ""
        if self.NamespaceIndex != 0:
            string += "ns={};".format(self.NamespaceIndex)
        ntype = None
        if self.NodeIdType == NodeIdType.Numeric:
            ntype = "i"
        elif self.NodeIdType == NodeIdType.String:
            ntype = "s"
        elif self.NodeIdType == NodeIdType.TwoByte:
            ntype = "i" 
        elif self.NodeIdType == NodeIdType.FourByte:
            ntype = "i" 
        elif self.NodeIdType == NodeIdType.Guid:
            ntype = "g"
        elif self.NodeIdType == NodeIdType.ByteString:
            ntype = "b"
        string += "{}={}".format(ntype, self.Identifier)
        if self.ServerIndex:
            string = "srv=" + str(self.ServerIndex) + string
        if self.NamespaceUri:
            string += "nsu={}".format(self.NamespaceUri)
        return string 

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
            nid.NamespaceIndex = struct.unpack("<H", data.read(2))[0]
            nid.Identifier = unpack_string(data)
        elif nid.NodeIdType == NodeIdType.ByteString:
            nid.NamespaceIndex = struct.unpack("<H", data.read(2))[0]
            nid.Identifier = unpack_bytes(data)
        elif nid.NodeIdType == NodeIdType.Guid:
            nid.NamespaceIndex = struct.unpack("<H", data.read(2))[0]
            nid.Identifier = Guid.from_binary(data)
        else:
            raise Exception("Unknown NodeId encoding: " + str(nid.NodeIdType))

        if test_bit(encoding, 6):
            nid.NamespaceUri = unpack_string(data)
        if test_bit(encoding, 7):
            nid.ServerIndex = struct.unpack("<I", data.read(4))[0]

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

    def to_string(self):
        return "{}:{}".format(self.NamespaceIndex, self.Name)

    @staticmethod
    def from_string(string):
        if ":" in string:
            idx, name = string.split(":")
        else:
            idx = 0
            name = string
        return QualifiedName(name, int(idx))
    
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
    
    def __eq__(self, bname):
        return isinstance(bname, QualifiedName) and self.Name == bname.Name and self.NamespaceIndex == bname.NamespaceIndex

    def __str__(self):
        return 'QualifiedName({}:{})'.format(self.NamespaceIndex, self.Name)
    
    __repr__ = __str__

'''
class DateTime(object):
    def __init__(self, data=None):
        if data is None:
            self.data = datetime_to_win_epoch(datetime.now()) 
        else:
            self.data = data

    @staticmethod
    def now():
        return DateTime.from_datetime(datetime.now())

    @staticmethod
    def from_datetime(pydt):
        dt = DateTime()
        dt.data = datetime_to_win_epoch(pydt) 
        return dt

    def to_binary(self):
        return struct.pack("<d", self.data)
    
    @staticmethod
    def from_binary(data):
        #print("Generating DateTime from {}", data)
        d = DateTime()
        d.data = struct.unpack("<d", data.read(8))[0]
        return d

    @staticmethod
    def from_time_t(data):
        return DateTime.from_datetime(datetime.fromtimestamp(data))
    
    def to_time_t(self):
        epoch = datetime.utcfromtimestamp(0)
        delta = self.win_epoch_to_datetime(self.data)() - epoch
        return delta.total_seconds()

    def __str__(self):
        return "Datetime({})".format(win_epoch_to_datetime(self.data).isoformat())
    __repr__ = __str__
'''


class VariantType(Enum):
    '''
    The possible types of a variant.
    '''
    Null = 0
    Boolean = 1
    SByte = 2
    Byte = 3
    Int16 = 4
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
    QualifiedName = 20
    LocalizedText = 21
    ExtensionObject = 22
    DataValue = 23
    Variant = 24
    DiagnosticInfo = 25

class Variant(object):
    def __init__(self, value=None, varianttype=None):
        self.Encoding = 0
        self.Value = value
        if varianttype is None:
            if type(self.Value) in (list, tuple):
                if len(self.Value) == 0:
                    raise Exception("could not guess UA variable type")
                self.VariantType = self._guess_type(self.Value[0])
            else:
                self.VariantType = self._guess_type(self.Value)
        else:
            self.VariantType = varianttype

    def __eq__(self, other):
        if isinstance(other, Variant) and self.VariantType == other.VariantType and self.Value == other.Value:
            return True
        return False

    def _guess_type(self, val):
        if val is None:
            return VariantType.Null
        elif type(val) == float:
            return VariantType.Double
        elif type(val) == int:
            return VariantType.Int64
        elif type(val) == str:
            return VariantType.String
        elif type(val) == bytes:
            return VariantType.ByteString
        elif type(val) == datetime:
            return VariantType.DateTime
        else:
            raise Exception("Could not guess UA type of {} with type {}, specify UA type".format(val, type(val)))

    def __str__(self):
        return "Variant(val:{},type:{})".format(self.Value, self.VariantType)
    __repr__ = __str__

    def to_binary(self):
        b = []
        mask = self.Encoding & 0b01111111
        self.Encoding = (self.VariantType.value | mask)
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
        obj.VariantType = VariantType(val)
        if obj.VariantType == VariantType.Null:
            return obj
        if obj.Encoding & (1 << 7):
            obj.Value = unpack_uatype_array(obj.VariantType.name, data)
        else:
            obj.Value = unpack_uatype(obj.VariantType.name, data)
        return obj


class DataValue(object):
    '''
    A value with an associated timestamp, and quality.
    Automatically generated from xml , copied and modified here to fix errors in xml spec
    '''
    def __init__(self, variant=None):
        self.Encoding = 0
        if not type(variant) is Variant:
            variant = Variant(variant)
        self.Value = variant
        self.StatusCode = StatusCode()
        self.SourceTimestamp = datetime.now()#DateTime()
        self.SourcePicoseconds = 0
        self.ServerTimestamp = datetime.now()#DateTime()
        self.ServerPicoseconds = 0
    
    def to_binary(self):
        packet = []
        if self.Value: self.Encoding |= (1 << 0)
        if self.StatusCode: self.Encoding |= (1 << 1)
        if self.SourceTimestamp: self.Encoding |= (1 << 2)
        if self.ServerTimestamp: self.Encoding |= (1 << 3)
        if self.SourcePicoseconds: self.Encoding |= (1 << 4)
        if self.ServerPicoseconds: self.Encoding |= (1 << 5)
        packet.append(pack_uatype('UInt8', self.Encoding))
        if self.Value: 
            packet.append(self.Value.to_binary())
        if self.StatusCode: 
            packet.append(self.StatusCode.to_binary())
        if self.SourceTimestamp: 
            packet.append(pack_uatype('DateTime', self.SourceTimestamp))#self.SourceTimestamp.to_binary())
        if self.ServerTimestamp: 
            packet.append(pack_uatype('DateTime', self.ServerTimestamp))#self.ServerTimestamp.to_binary())
        if self.SourcePicoseconds: 
            packet.append(pack_uatype('UInt16', self.SourcePicoseconds))
        if self.ServerPicoseconds: 
            packet.append(pack_uatype('UInt16', self.ServerPicoseconds))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = DataValue()
        obj.Encoding = unpack_uatype('UInt8', data)
        if obj.Encoding & (1 << 0):
            obj.Value = Variant.from_binary(data)
        if obj.Encoding & (1 << 1):
            obj.StatusCode = StatusCode.from_binary(data)
        if obj.Encoding & (1 << 2):
            obj.SourceTimestamp = unpack_uatype('DateTime', data)#DateTime.from_binary(data)
        if obj.Encoding & (1 << 3):
            obj.ServerTimestamp = unpack_uatype('DateTime', data)#DateTime.from_binary(data)
        if obj.Encoding & (1 << 4):
            obj.SourcePicoseconds = unpack_uatype('UInt16', data)
        if obj.Encoding & (1 << 5):
            obj.ServerPicoseconds = unpack_uatype('UInt16', data)
        return obj
    
    def __str__(self):
        return 'DataValue(' + 'Encoding:' + str(self.Encoding) + ', ' + \
             'Value:' + str(self.Value) + ', ' + \
             'StatusCode:' + str(self.StatusCode) + ', '  + \
             'SourceTimestamp:' + str(self.SourceTimestamp) + ', ' + \
             'ServerTimestamp:' + str(self.ServerTimestamp) + ', ' + \
             'SourcePicoseconds:' + str(self.SourcePicoseconds) + ', ' + \
             'ServerPicoseconds:' + str(self.ServerPicoseconds) + ')'
    
    __repr__ = __str__



        

