"""
implement ua datatypes
"""
import logging
from enum import Enum, IntEnum, EnumMeta
from datetime import datetime, timedelta, tzinfo, MAXYEAR
from calendar import timegm
import sys
import os
import uuid
import struct
import re
import itertools
if sys.version_info.major > 2:
    unicode = str

from opcua.ua import status_codes
from opcua.common.uaerrors import UaError
from opcua.common.uaerrors import UaStatusCodeError
from opcua.common.uaerrors import UaStringParsingError


logger = logging.getLogger('opcua.uaprotocol')


# types that will packed and unpacked directly using struct (string, bytes and datetime are handles as special cases
UaTypes = ("Boolean", "SByte", "Byte", "Int8", "UInt8", "Int16", "UInt16", "Int32", "UInt32", "Int64", "UInt64", "Float", "Double")


EPOCH_AS_FILETIME = 116444736000000000  # January 1, 1970 as MS file time
HUNDREDS_OF_NANOSECONDS = 10000000
FILETIME_EPOCH_AS_DATETIME = datetime(1601, 1, 1)


class UTC(tzinfo):

    """UTC"""

    def utcoffset(self, dt):
        return timedelta(0)

    def tzname(self, dt):
        return "UTC"

    def dst(self, dt):
        return timedelta(0)


# method copied from David Buxton <david@gasmark6.com> sample code
def datetime_to_win_epoch(dt):
    if (dt.tzinfo is None) or (dt.tzinfo.utcoffset(dt) is None):
        dt = dt.replace(tzinfo=UTC())
    ft = EPOCH_AS_FILETIME + (timegm(dt.timetuple()) * HUNDREDS_OF_NANOSECONDS)
    return ft + (dt.microsecond * 10)


def win_epoch_to_datetime(epch):
    try:
        return FILETIME_EPOCH_AS_DATETIME + timedelta(microseconds=epch // 10)
    except OverflowError:
        # FILETIMEs after 31 Dec 9999 can't be converted to datetime
        logger.warning("datetime overflow: {}".format(epch))
        return datetime(MAXYEAR, 12, 31, 23, 59, 59, 999999)


#  minimum datetime as in ua spec, used for history
DateTimeMinValue = datetime(1606, 1, 1, 12, 0, 0)


def build_array_format_py2(prefix, length, fmtchar):
    return prefix + str(length) + fmtchar


def build_array_format_py3(prefix, length, fmtchar):
    return prefix + str(length) + chr(fmtchar)


if sys.version_info.major < 3:
    build_array_format = build_array_format_py2
else:
    build_array_format = build_array_format_py3


def pack_uatype_array_primitive(st, value, length):
    if length == 1:
        return b'\x01\x00\x00\x00' + st.pack(value[0])
    else:
        return struct.pack(build_array_format("<i", length, st.format[1]), length, *value)


def pack_uatype_array(uatype, value):
    if value is None:
        return b'\xff\xff\xff\xff'
    length = len(value)
    if length == 0:
        return b'\x00\x00\x00\x00'
    if uatype in uatype2struct:
        return pack_uatype_array_primitive(uatype2struct[uatype], value, length)
    b = []
    b.append(uatype_Int32.pack(length))
    for val in value:
        b.append(pack_uatype(uatype, val))
    return b"".join(b)


def pack_uatype(uatype, value):
    if uatype in uatype2struct:
        if value is None:
            value = 0
        return uatype2struct[uatype].pack(value)
    elif uatype == "Null":
        return b''
    elif uatype == "String":
        return pack_string(value)
    elif uatype in ("CharArray", "ByteString", "Custom"):
        return pack_bytes(value)
    elif uatype == "DateTime":
        return pack_datetime(value)
    elif uatype == "LocalizedText":
        if isinstance(value, LocalizedText):
            return value.to_binary()
        else:
            return LocalizedText(value).to_binary()
    elif uatype == "ExtensionObject":
        # dependency loop: classes in uaprotocol_auto use Variant defined in this file,
        # but Variant can contain any object from uaprotocol_auto as ExtensionObject.
        # Using local import to avoid import loop
        from opcua.ua.uaprotocol_auto import extensionobject_to_binary
        return extensionobject_to_binary(value)
    else:
        return value.to_binary()

uatype_Int8 = struct.Struct("<b")
uatype_SByte = uatype_Int8
uatype_Int16 = struct.Struct("<h")
uatype_Int32 = struct.Struct("<i")
uatype_Int64 = struct.Struct("<q")
uatype_UInt8 = struct.Struct("<B")
uatype_Char = uatype_UInt8
uatype_Byte = uatype_UInt8
uatype_UInt16 = struct.Struct("<H")
uatype_UInt32 = struct.Struct("<I")
uatype_UInt64 = struct.Struct("<Q")
uatype_Boolean = struct.Struct("<?")
uatype_Double = struct.Struct("<d")
uatype_Float = struct.Struct("<f")

uatype2struct = {
    "Int8": uatype_Int8,
    "SByte": uatype_SByte,
    "Int16": uatype_Int16,
    "Int32": uatype_Int32,
    "Int64": uatype_Int64,
    "UInt8": uatype_UInt8,
    "Char": uatype_Char,
    "Byte": uatype_Byte,
    "UInt16": uatype_UInt16,
    "UInt32": uatype_UInt32,
    "UInt64": uatype_UInt64,
    "Boolean": uatype_Boolean,
    "Double": uatype_Double,
    "Float": uatype_Float,
}


def unpack_uatype(uatype, data):
    if uatype in uatype2struct:
        st = uatype2struct[uatype]
        return st.unpack(data.read(st.size))[0]
    elif uatype == "String":
        return unpack_string(data)
    elif uatype in ("CharArray", "ByteString", "Custom"):
        return unpack_bytes(data)
    elif uatype == "DateTime":
        return unpack_datetime(data)
    elif uatype == "ExtensionObject":
        # dependency loop: classes in uaprotocol_auto use Variant defined in this file,
        # but Variant can contain any object from uaprotocol_auto as ExtensionObject.
        # Using local import to avoid import loop
        from opcua.ua.uaprotocol_auto import extensionobject_from_binary
        return extensionobject_from_binary(data)
    else:
        glbs = globals()
        if uatype in glbs:
            klass = glbs[uatype]
            if hasattr(klass, 'from_binary'):
                return klass.from_binary(data)
        raise UaError("can not unpack unknown uatype %s" % uatype)


def unpack_uatype_array(uatype, data):
    length = uatype_Int32.unpack(data.read(4))[0]
    if length == -1:
        return None
    elif length == 0:
        return []
    elif uatype in uatype2struct:
        st = uatype2struct[uatype]
        if length == 1:
            return list(st.unpack(data.read(st.size)))
        else:
            arrst = struct.Struct(build_array_format("<", length, st.format[1]))
            return list(arrst.unpack(data.read(arrst.size)))
    else:
        result = []
        for _ in range(0, length):
            result.append(unpack_uatype(uatype, data))
        return result


def pack_datetime(value):
    epch = datetime_to_win_epoch(value)
    return uatype_Int64.pack(epch)


def unpack_datetime(data):
    epch = uatype_Int64.unpack(data.read(8))[0]
    return win_epoch_to_datetime(epch)


def pack_string(string):
    if string is None:
        return uatype_Int32.pack(-1)
    if isinstance(string, unicode):
        string = string.encode('utf-8')
    length = len(string)
    return uatype_Int32.pack(length) + string

pack_bytes = pack_string


def unpack_bytes(data):
    length = uatype_Int32.unpack(data.read(4))[0]
    if length == -1:
        return None
    return data.read(length)


def py3_unpack_string(data):
    b = unpack_bytes(data)
    if b is None:
        return b
    return b.decode("utf-8")


if sys.version_info.major < 3:
    unpack_string = unpack_bytes
else:
    unpack_string = py3_unpack_string


def test_bit(data, offset):
    mask = 1 << offset
    return data & mask


def set_bit(data, offset):
    mask = 1 << offset
    return data | mask


def unset_bit(data, offset):
    mask = 1 << offset
    return data & ~mask


class _FrozenClass(object):

    """
    make it impossible to add members to a class.
    This is a hack since I found out that most bugs are due to misspelling a variable in protocol
    """
    _freeze = False

    def __setattr__(self, key, value):
        if self._freeze and not hasattr(self, key):
            raise TypeError("Error adding member '{}' to class '{}', class is frozen, members are {}".format(
                key, self.__class__.__name__, self.__dict__.keys()))
        object.__setattr__(self, key, value)

if "PYOPCUA_NO_TYPO_CHECK" in os.environ:
    # typo check is cpu consuming, but it will make debug easy.
    # if typo check is not need (in production), please set env PYOPCUA_NO_TYPO_CHECK.
    # this will make all uatype class inherit from object intead of _FrozenClass
    # and skip the typo check.
    FrozenClass = object
else:
    FrozenClass = _FrozenClass


class ValueRank(IntEnum):
    """
    Defines dimensions of a variable.
    This enum does not support all cases since ValueRank support any n>0
    but since it is an IntEnum it can be replace by a normal int
    """
    ScalarOrOneDimension = -3
    Any = -2
    Scalar = -1
    OneOrMoreDimensions = 0
    OneDimension = 1
    # the next names are not in spec but so common we express them here
    TwoDimensions = 2
    ThreeDimensions = 3
    FourDimensions = 4


class _MaskEnum(IntEnum):

    @classmethod
    def parse_bitfield(cls, the_int):
        """ Take an integer and interpret it as a set of enum values. """
        assert isinstance(the_int, int)

        return {cls(b) for b in cls._bits(the_int)}

    @classmethod
    def to_bitfield(cls, collection):
        """ Takes some enum values and creates an integer from them. """
        # make sure all elements are of the correct type (use itertools.tee in case we get passed an
        # iterator)
        iter1, iter2 = itertools.tee(iter(collection))
        assert all(isinstance(x, cls) for x in iter1)

        return sum(x.mask for x in iter2)

    @property
    def mask(self):
        return 1 << self.value

    @staticmethod
    def _bits(n):
        """ Iterate over the bits in n.

            e.g. bits(44) yields at 2, 3, 5
        """
        assert n >= 0 # avoid infinite recursion

        pos = 0
        while n:
            if n & 0x1:
                yield pos
            n = n // 2
            pos += 1

class AccessLevel(_MaskEnum):
    """
    Bit index to indicate what the access level is.

    Spec Part 3, appears multiple times, e.g. paragraph 5.6.2 Variable NodeClass
    """
    CurrentRead    = 0
    CurrentWrite   = 1
    HistoryRead    = 2
    HistoryWrite   = 3
    SemanticChange = 4
    StatusWrite    = 5
    TimestampWrite = 6

class WriteMask(_MaskEnum):
    """
    Bit index to indicate which attribute of a node is writable

    Spec Part 3, Paragraph 5.2.7 WriteMask
    """
    AccessLevel             = 0
    ArrayDimensions         = 1
    BrowseName              = 2
    ContainsNoLoops         = 3
    DataType                = 4
    Description             = 5
    DisplayName             = 6
    EventNotifier           = 7
    Executable              = 8
    Historizing             = 9
    InverseName             = 10
    IsAbstract              = 11
    MinimumSamplingInterval = 12
    NodeClass               = 13
    NodeId                  = 14
    Symmetric               = 15
    UserAccessLevel         = 16
    UserExecutable          = 17
    UserWriteMask           = 18
    ValueRank               = 19
    WriteMask               = 20
    ValueForVariableType    = 21


class EventNotifier(_MaskEnum):
    """
    Bit index to indicate how a node can be used for events.

    Spec Part 3, appears multiple times, e.g. Paragraph 5.4 View NodeClass
    """
    SubscribeToEvents = 0
    # Reserved        = 1
    HistoryRead       = 2
    HistoryWrite      = 3


class Guid(FrozenClass):

    def __init__(self):
        self.uuid = uuid.uuid4()
        self._freeze = True

    def to_binary(self):
        return self.uuid.bytes

    def __hash__(self):
        return hash(self.uuid.bytes)

    @staticmethod
    def from_binary(data):
        g = Guid()
        g.uuid = uuid.UUID(bytes=data.read(16))
        return g

    def __eq__(self, other):
        return isinstance(other, Guid) and self.uuid == other.uuid


class StatusCode(FrozenClass):

    """
    :ivar value:
    :vartype value: int
    :ivar name:
    :vartype name: string
    :ivar doc:
    :vartype doc: string
    """

    def __init__(self, value=0):
        if isinstance(value, str):
            self.name = value
            self.value = getattr(status_codes.StatusCodes, value)
        else:
            self.value = value
            self.name, self.doc = status_codes.get_name_and_doc(value)
        self._freeze = True

    def to_binary(self):
        return uatype_UInt32.pack(self.value)

    @staticmethod
    def from_binary(data):
        val = uatype_UInt32.unpack(data.read(4))[0]
        sc = StatusCode(val)
        return sc

    def check(self):
        """
        Raises an exception if the status code is anything else than 0 (good).

        Use the is_good() method if you do not want an exception.
        """
        if self.value != 0:
            raise UaStatusCodeError(self.value)

    def is_good(self):
        """
        return True if status is Good.
        """
        if self.value == 0:
            return True
        return False

    def __str__(self):
        return 'StatusCode({})'.format(self.name)
    __repr__ = __str__

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return not self.__eq__(other)


class NodeIdType(Enum):
    TwoByte = 0
    FourByte = 1
    Numeric = 2
    String = 3
    Guid = 4
    ByteString = 5


class NodeId(FrozenClass):

    """
    NodeId Object

    Args:
        identifier: The identifier might be an int, a string, bytes or a Guid
        namespaceidx(int): The index of the namespace
        nodeidtype(NodeIdType): The type of the nodeid if it cannor be guess or you want something special like twobyte nodeid or fourbytenodeid


    :ivar Identifier:
    :vartype Identifier: NodeId
    :ivar NamespaceIndex:
    :vartype NamespaceIndex: Int
    :ivar NamespaceUri:
    :vartype NamespaceUri: String
    :ivar ServerIndex:
    :vartype ServerIndex: Int
    """

    def __init__(self, identifier=None, namespaceidx=0, nodeidtype=None):
        self.Identifier = identifier
        self.NamespaceIndex = namespaceidx
        self.NodeIdType = nodeidtype
        self.NamespaceUri = ""
        self.ServerIndex = 0
        self._freeze = True
        if not isinstance(self.NamespaceIndex, int):
            raise UaError("NamespaceIndex must be an int")
        if self.Identifier is None:
            self.Identifier = 0
            self.NodeIdType = NodeIdType.TwoByte
            return
        if self.NodeIdType is None:
            if isinstance(self.Identifier, int):
                self.NodeIdType = NodeIdType.Numeric
            elif isinstance(self.Identifier, str):
                self.NodeIdType = NodeIdType.String
            elif isinstance(self.Identifier, bytes):
                self.NodeIdType = NodeIdType.ByteString
            else:
                raise UaError("NodeId: Could not guess type of NodeId, set NodeIdType")

    def __key(self):
        if self.NodeIdType in (NodeIdType.TwoByte, NodeIdType.FourByte, NodeIdType.Numeric):  # twobyte, fourbyte and numeric may represent the same node
            return self.NamespaceIndex, self.Identifier
        else:
            return self.NodeIdType, self.NamespaceIndex, self.Identifier

    def __eq__(self, node):
        return isinstance(node, NodeId) and self.__key() == node.__key()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.__key())

    def is_null(self):
        if self.NamespaceIndex != 0:
            return False
        return self.has_null_identifier()

    def has_null_identifier(self):
        if not self.Identifier:
            return True
        if self.NodeIdType == NodeIdType.Guid and re.match(b'0.', self.Identifier):
            return True
        return False

    @staticmethod
    def from_string(string):
        try:
            return NodeId._from_string(string)
        except ValueError as ex:
            raise UaStringParsingError("Error parsing string {}".format(string), ex)

    @staticmethod
    def _from_string(string):
        l = string.split(";")
        identifier = None
        namespace = 0
        ntype = None
        srv = None
        nsu = None
        for el in l:
            if not el:
                continue
            k, v = el.split("=", 1)
            k = k.strip()
            v = v.strip()
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
            raise UaStringParsingError("Could not find identifier in string: " + string)
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
        return "{}NodeId({})".format(self.NodeIdType.name, self.to_string())
    __repr__ = __str__

    def to_binary(self):
        if self.NodeIdType == NodeIdType.TwoByte:
            return struct.pack("<BB", self.NodeIdType.value, self.Identifier)
        elif self.NodeIdType == NodeIdType.FourByte:
            return struct.pack("<BBH", self.NodeIdType.value, self.NamespaceIndex, self.Identifier)
        elif self.NodeIdType == NodeIdType.Numeric:
            return struct.pack("<BHI", self.NodeIdType.value, self.NamespaceIndex, self.Identifier)
        elif self.NodeIdType == NodeIdType.String:
            return struct.pack("<BH", self.NodeIdType.value, self.NamespaceIndex) + \
                pack_string(self.Identifier)
        elif self.NodeIdType == NodeIdType.ByteString:
            return struct.pack("<BH", self.NodeIdType.value, self.NamespaceIndex) + \
                pack_bytes(self.Identifier)
        else:
            return struct.pack("<BH", self.NodeIdType.value, self.NamespaceIndex) + \
                self.Identifier.to_binary()
        #FIXME: Missing NNamespaceURI and ServerIndex

    @staticmethod
    def from_binary(data):
        nid = NodeId()
        encoding = ord(data.read(1))
        nid.NodeIdType = NodeIdType(encoding & 0b00111111)

        if nid.NodeIdType == NodeIdType.TwoByte:
            nid.Identifier = ord(data.read(1))
        elif nid.NodeIdType == NodeIdType.FourByte:
            nid.NamespaceIndex, nid.Identifier = struct.unpack("<BH", data.read(3))
        elif nid.NodeIdType == NodeIdType.Numeric:
            nid.NamespaceIndex, nid.Identifier = struct.unpack("<HI", data.read(6))
        elif nid.NodeIdType == NodeIdType.String:
            nid.NamespaceIndex = uatype_UInt16.unpack(data.read(2))[0]
            nid.Identifier = unpack_string(data)
        elif nid.NodeIdType == NodeIdType.ByteString:
            nid.NamespaceIndex = uatype_UInt16.unpack(data.read(2))[0]
            nid.Identifier = unpack_bytes(data)
        elif nid.NodeIdType == NodeIdType.Guid:
            nid.NamespaceIndex = uatype_UInt16.unpack(data.read(2))[0]
            nid.Identifier = Guid.from_binary(data)
        else:
            raise UaError("Unknown NodeId encoding: " + str(nid.NodeIdType))

        if test_bit(encoding, 7):
            nid.NamespaceUri = unpack_string(data)
        if test_bit(encoding, 6):
            nid.ServerIndex = uatype_UInt32.unpack(data.read(4))[0]

        return nid


class TwoByteNodeId(NodeId):

    def __init__(self, identifier):
        NodeId.__init__(self, identifier, 0, NodeIdType.TwoByte)


class FourByteNodeId(NodeId):

    def __init__(self, identifier, namespace=0):
        NodeId.__init__(self, identifier, namespace, NodeIdType.FourByte)


class NumericNodeId(NodeId):

    def __init__(self, identifier, namespace=0):
        NodeId.__init__(self, identifier, namespace, NodeIdType.Numeric)


class ByteStringNodeId(NodeId):

    def __init__(self, identifier, namespace=0):
        NodeId.__init__(self, identifier, namespace, NodeIdType.ByteString)


class GuidNodeId(NodeId):

    def __init__(self, identifier, namespace=0):
        NodeId.__init__(self, identifier, namespace, NodeIdType.Guid)


class StringNodeId(NodeId):

    def __init__(self, identifier, namespace=0):
        NodeId.__init__(self, identifier, namespace, NodeIdType.String)


ExpandedNodeId = NodeId


class QualifiedName(FrozenClass):

    '''
    A string qualified with a namespace index.
    '''

    def __init__(self, name=None, namespaceidx=0):
        if not isinstance(namespaceidx, int):
            raise UaError("namespaceidx must be an int")
        self.NamespaceIndex = namespaceidx
        self.Name = name
        self._freeze = True

    def to_string(self):
        return "{}:{}".format(self.NamespaceIndex, self.Name)

    @staticmethod
    def from_string(string):
        if ":" in string:
            try:
                idx, name = string.split(":", 1)
                idx = int(idx)
            except (TypeError, ValueError) as ex:
                raise UaStringParsingError("Error parsing string {}".format(string), ex)
        else:
            idx = 0
            name = string
        return QualifiedName(name, idx)

    def to_binary(self):
        packet = []
        packet.append(uatype_UInt16.pack(self.NamespaceIndex))
        packet.append(pack_string(self.Name))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = QualifiedName()
        obj.NamespaceIndex = uatype_UInt16.unpack(data.read(2))[0]
        obj.Name = unpack_string(data)
        return obj

    def __eq__(self, bname):
        return isinstance(bname, QualifiedName) and self.Name == bname.Name and self.NamespaceIndex == bname.NamespaceIndex

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if not isinstance(other, QualifiedName):
            raise TypeError("Cannot compare QualifiedName and {}".format(other))
        if self.NamespaceIndex == other.NamespaceIndex:
            return self.Name < other.Name
        else:
            return self.NamespaceIndex < other.NamespaceIndex

    def __str__(self):
        return 'QualifiedName({}:{})'.format(self.NamespaceIndex, self.Name)

    __repr__ = __str__


class LocalizedText(FrozenClass):

    '''
    A string qualified with a namespace index.
    '''

    def __init__(self, text=None):
        self.Encoding = 0
        self.Text = text
        if isinstance(self.Text, unicode):
            self.Text = self.Text.encode('utf-8')
        if self.Text:
            self.Encoding |= (1 << 1)
        self.Locale = None 
        self._freeze = True

    def to_binary(self):
        packet = []
        if self.Locale:
            self.Encoding |= (1 << 0)
        if self.Text:
            self.Encoding |= (1 << 1)
        packet.append(uatype_UInt8.pack(self.Encoding))
        if self.Locale:
            packet.append(pack_bytes(self.Locale))
        if self.Text:
            packet.append(pack_bytes(self.Text))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = LocalizedText()
        obj.Encoding = ord(data.read(1))
        if obj.Encoding & (1 << 0):
            obj.Locale = unpack_bytes(data)
        if obj.Encoding & (1 << 1):
            obj.Text = unpack_bytes(data)
        return obj

    def to_string(self):
        # FIXME: use local
        if self.Text is None:
            return ""
        return self.Text.decode('utf-8')

    def __str__(self):
        return 'LocalizedText(' + 'Encoding:' + str(self.Encoding) + ', ' + \
            'Locale:' + str(self.Locale) + ', ' + \
            'Text:' + str(self.Text) + ')'
    __repr__ = __str__

    def __eq__(self, other):
        if isinstance(other, LocalizedText) and self.Locale == other.Locale and self.Text == other.Text:
            return True
        return False

    def __ne__(self, other):
        return not self.__eq__(other)


class ExtensionObject(FrozenClass):

    '''

    Any UA object packed as an ExtensionObject


    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar Body:
    :vartype Body: bytes

    '''

    def __init__(self):
        self.TypeId = NodeId()
        self.Encoding = 0
        self.Body = b''
        self._freeze = True

    def to_binary(self):
        packet = []
        if self.Body:
            self.Encoding |= (1 << 0)
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        if self.Body:
            packet.append(pack_uatype('ByteString', self.Body))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = ExtensionObject()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        if obj.Encoding & (1 << 0):
            obj.Body = unpack_uatype('ByteString', data)
        return obj

    @staticmethod
    def from_object(obj):
        ext = ExtensionObject()
        oid = getattr(ObjectIds, "{}_Encoding_DefaultBinary".format(obj.__class__.__name__))
        ext.TypeId = FourByteNodeId(oid)
        ext.Body = obj.to_binary()
        return ext

    def __str__(self):
        return 'ExtensionObject(' + 'TypeId:' + str(self.TypeId) + ', ' + \
            'Encoding:' + str(self.Encoding) + ', ' + str(len(self.Body)) + ' bytes)'

    __repr__ = __str__


class VariantType(Enum):

    '''
    The possible types of a variant.

    :ivar Null:
    :ivar Boolean:
    :ivar SByte:
    :ivar Byte:
    :ivar Int16:
    :ivar UInt16:
    :ivar Int32:
    :ivar UInt32:
    :ivar Int64:
    :ivar UInt64:
    :ivar Float:
    :ivar Double:
    :ivar String:
    :ivar DateTime:
    :ivar Guid:
    :ivar ByteString:
    :ivar XmlElement:
    :ivar NodeId:
    :ivar ExpandedNodeId:
    :ivar StatusCode:
    :ivar QualifiedName:
    :ivar LocalizedText:
    :ivar ExtensionObject:
    :ivar DataValue:
    :ivar Variant:
    :ivar DiagnosticInfo:



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


class VariantTypeCustom(object):
    def __init__(self, val):
        self.name = "Custom"
        self.value = val
        if self.value > 0b00111111:
            raise UaError("Cannot create VariantType. VariantType must be {} > x > {}, received {}".format(0b111111, 25, val))

    def __str__(self):
        return "VariantType.Custom:{}".format(self.value)
    __repr__ = __str__

    def __eq__(self, other):
        return self.value == other.value


class Variant(FrozenClass):

    """
    Create an OPC-UA Variant object.
    if no argument a Null Variant is created.
    if not variant type is given, attemps to guess type from python type
    if a variant is given as value, the new objects becomes a copy of the argument

    :ivar Value:
    :vartype Value: Any supported type
    :ivar VariantType:
    :vartype VariantType: VariantType
    """

    def __init__(self, value=None, varianttype=None, dimensions=None):
        self.Value = value
        self.VariantType = varianttype
        self.Dimensions = dimensions
        self._freeze = True
        if isinstance(value, Variant):
            self.Value = value.Value
            self.VariantType = value.VariantType
        if self.VariantType is None:
            self.VariantType = self._guess_type(self.Value)
        if self.Dimensions is None and type(self.Value) in (list, tuple):
            dims = get_shape(self.Value)
            if len(dims) > 1:
                self.Dimensions = dims

    def __eq__(self, other):
        if isinstance(other, Variant) and self.VariantType == other.VariantType and self.Value == other.Value:
            return True
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def _guess_type(self, val):
        if isinstance(val, (list, tuple)):
            error_val = val
        while isinstance(val, (list, tuple)):
            if len(val) == 0:
                raise UaError("could not guess UA type of variable {}".format(error_val))
            val = val[0]
        if val is None:
            return VariantType.Null
        elif isinstance(val, bool):
            return VariantType.Boolean
        elif isinstance(val, float):
            return VariantType.Double
        elif isinstance(val, int):
            return VariantType.Int64
        elif type(val) in (str, unicode):
            return VariantType.String
        elif isinstance(val, bytes):
            return VariantType.ByteString
        elif isinstance(val, datetime):
            return VariantType.DateTime
        else:
            if isinstance(val, object):
                try:
                    return getattr(VariantType, val.__class__.__name__)
                except AttributeError:
                    return VariantType.ExtensionObject
            else:
                raise UaError("Could not guess UA type of {} with type {}, specify UA type".format(val, type(val)))

    def __str__(self):
        return "Variant(val:{!s},type:{})".format(self.Value, self.VariantType)
    __repr__ = __str__

    def to_binary(self):
        b = []
        encoding = self.VariantType.value & 0b111111
        if type(self.Value) in (list, tuple):
            if self.Dimensions is not None:
                encoding = set_bit(encoding, 6)
            encoding = set_bit(encoding, 7)
            b.append(uatype_UInt8.pack(encoding))
            b.append(pack_uatype_array(self.VariantType.name, flatten(self.Value)))
            if self.Dimensions is not None:
                b.append(pack_uatype_array("Int32", self.Dimensions))
        else:
            b.append(uatype_UInt8.pack(encoding))
            b.append(pack_uatype(self.VariantType.name, self.Value))

        return b"".join(b)

    @staticmethod
    def from_binary(data):
        dimensions = None
        encoding = ord(data.read(1))
        int_type = encoding & 0b00111111
        vtype = DataType_to_VariantType(int_type)
        if vtype == VariantType.Null:
            return Variant(None, vtype, encoding)
        if test_bit(encoding, 7):
            value = unpack_uatype_array(vtype.name, data)
        else:
            value = unpack_uatype(vtype.name, data)
        if test_bit(encoding, 6):
            dimensions = unpack_uatype_array("Int32", data)
            value = reshape(value, dimensions)

        return Variant(value, vtype, dimensions)


def reshape(flat, dims):
    subdims = dims[1:]
    subsize = 1
    for i in subdims:
        if i == 0:
            i = 1
        subsize *= i
    while dims[0] * subsize > len(flat):
        flat.append([])
    if not subdims or subdims == [0]:
        return flat
    return [reshape(flat[i: i + subsize], subdims) for i in range(0, len(flat), subsize)]


def _split_list(l, n):
    n = max(1, n)
    return [l[i:i + n] for i in range(0, len(l), n)]


def flatten_and_get_shape(mylist):
    dims = []
    dims.append(len(mylist))
    while isinstance(mylist[0], (list, tuple)):
        dims.append(len(mylist[0]))
        mylist = [item for sublist in mylist for item in sublist]
        if len(mylist) == 0:
            break
    return mylist, dims


def flatten(mylist):
    if len(mylist) == 0:
        return mylist
    while isinstance(mylist[0], (list, tuple)):
        mylist = [item for sublist in mylist for item in sublist]
        if len(mylist) == 0:
            break
    return mylist


def get_shape(mylist):
    dims = []
    while isinstance(mylist, (list, tuple)):
        dims.append(len(mylist))
        if len(mylist) == 0:
            break
        mylist = mylist[0]
    return dims


class XmlElement(FrozenClass):
    '''
    An XML element encoded as an UTF-8 string.
    '''
    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            self._freeze = True
            return
        self.Value = []
        self._freeze = True

    def to_binary(self):
        return pack_string(self.Value)

    @staticmethod
    def from_binary(data):
        return XmlElement(data)

    def _binary_init(self, data):
        self.Value = unpack_string(data)

    def __str__(self):
        return 'XmlElement(Value:' + str(self.Value) + ')'

    __repr__ = __str__


class DataValue(FrozenClass):

    '''
    A value with an associated timestamp, and quality.
    Automatically generated from xml , copied and modified here to fix errors in xml spec

    :ivar Value:
    :vartype Value: Variant
    :ivar StatusCode:
    :vartype StatusCode: StatusCode
    :ivar SourceTimestamp:
    :vartype SourceTimestamp: datetime
    :ivar SourcePicoSeconds:
    :vartype SourcePicoSeconds: int
    :ivar ServerTimestamp:
    :vartype ServerTimestamp: datetime
    :ivar ServerPicoseconds:
    :vartype ServerPicoseconds: int

    '''

    def __init__(self, variant=None, status=None):
        self.Encoding = 0
        if not isinstance(variant, Variant):
            variant = Variant(variant)
        self.Value = variant
        if status is None:
            self.StatusCode = StatusCode()
        else:
            self.StatusCode = status
        self.SourceTimestamp = None  # DateTime()
        self.SourcePicoseconds = None
        self.ServerTimestamp = None  # DateTime()
        self.ServerPicoseconds = None
        self._freeze = True

    def to_binary(self):
        packet = []
        if self.Value:
            self.Encoding |= (1 << 0)
        if self.StatusCode:
            self.Encoding |= (1 << 1)
        if self.SourceTimestamp:
            self.Encoding |= (1 << 2)
        if self.ServerTimestamp:
            self.Encoding |= (1 << 3)
        if self.SourcePicoseconds:
            self.Encoding |= (1 << 4)
        if self.ServerPicoseconds:
            self.Encoding |= (1 << 5)
        packet.append(uatype_UInt8.pack(self.Encoding))
        if self.Value:
            packet.append(self.Value.to_binary())
        if self.StatusCode:
            packet.append(self.StatusCode.to_binary())
        if self.SourceTimestamp:
            packet.append(pack_datetime(self.SourceTimestamp))  # self.SourceTimestamp.to_binary())
        if self.ServerTimestamp:
            packet.append(pack_datetime(self.ServerTimestamp))  # self.ServerTimestamp.to_binary())
        if self.SourcePicoseconds:
            packet.append(uatype_UInt16.pack(self.SourcePicoseconds))
        if self.ServerPicoseconds:
            packet.append(uatype_UInt16.pack(self.ServerPicoseconds))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        encoding = ord(data.read(1))
        if encoding & (1 << 0):
            value = Variant.from_binary(data)
        else:
            value = None
        if encoding & (1 << 1):
            status = StatusCode.from_binary(data)
        else:
            status = None
        obj = DataValue(value, status)
        obj.Encoding = encoding
        if obj.Encoding & (1 << 2):
            obj.SourceTimestamp = unpack_datetime(data)  # DateTime.from_binary(data)
        if obj.Encoding & (1 << 3):
            obj.ServerTimestamp = unpack_datetime(data)  # DateTime.from_binary(data)
        if obj.Encoding & (1 << 4):
            obj.SourcePicoseconds = uatype_UInt16.unpack(data.read(2))[0]
        if obj.Encoding & (1 << 5):
            obj.ServerPicoseconds = uatype_UInt16.unpack(data.read(2))[0]
        return obj

    def __str__(self):
        s = 'DataValue(Value:{}'.format(self.Value)
        if self.StatusCode is not None:
            s += ', StatusCode:{}'.format(self.StatusCode)
        if self.SourceTimestamp is not None:
            s += ', SourceTimestamp:{}'.format(self.SourceTimestamp)
        if self.ServerTimestamp is not None:
            s += ', ServerTimestamp:{}'.format(self.ServerTimestamp)
        if self.SourcePicoseconds is not None:
            s += ', SourcePicoseconds:{}'.format(self.SourcePicoseconds)
        if self.ServerPicoseconds is not None:
            s += ', ServerPicoseconds:{}'.format(self.ServerPicoseconds)
        s += ')'
        return s

    __repr__ = __str__


def DataType_to_VariantType(int_type):
    """
    Takes a NodeId or int and return a VariantType
    This is only supported if int_type < 63 due to VariantType encoding
    """
    if isinstance(int_type, NodeId):
        int_type = int_type.Identifier

    if int_type <= 25:
        return VariantType(int_type)
    else:
        return VariantTypeCustom(int_type)
