"""
Binary protocol specific functions and constants
"""

import sys
import struct
import logging
from datetime import datetime, timedelta, tzinfo, MAXYEAR
from calendar import timegm
import uuid

from opcua.ua.uaerrors import UaError


if sys.version_info.major > 2:
    unicode = str

logger = logging.getLogger('__name__')

EPOCH_AS_FILETIME = 116444736000000000  # January 1, 1970 as MS file time
HUNDREDS_OF_NANOSECONDS = 10000000
FILETIME_EPOCH_AS_DATETIME = datetime(1601, 1, 1)


def test_bit(data, offset):
    mask = 1 << offset
    return data & mask


def set_bit(data, offset):
    mask = 1 << offset
    return data | mask


def unset_bit(data, offset):
    mask = 1 << offset
    return data & ~mask


class UTC(tzinfo):
    """
    UTC
    """

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
        logger.warning("datetime overflow: %s", epch)
        return datetime(MAXYEAR, 12, 31, 23, 59, 59, 999999)


def build_array_format_py2(prefix, length, fmtchar):
    return prefix + str(length) + fmtchar


def build_array_format_py3(prefix, length, fmtchar):
    return prefix + str(length) + chr(fmtchar)


if sys.version_info.major < 3:
    build_array_format = build_array_format_py2
else:
    build_array_format = build_array_format_py3


class _Primitive(object):

    def pack_array(self, array):
        if array is None:
            return b'\xff\xff\xff\xff'
        length = len(array)
        b = [self.pack(val) for val in array]
        b.insert(0, Primitives.Int32.pack(length))

    def unpack_array(self, data):
        length = Primitives.Int32.unpack(data)
        if length == -1:
            return None
        elif length == 0:
            return []
        else:
            return [self.unpack(data) for _ in range(length)]


class _DateTime(_Primitive):

    @staticmethod
    def pack(dt):
        epch = datetime_to_win_epoch(dt)
        return Primitives.Int64.pack(epch)

    @staticmethod
    def unpack(data):
        epch = Primitives.Int64.unpack(data)
        return win_epoch_to_datetime(epch)


class _String(_Primitive):

    @staticmethod
    def pack(string):
        if string is None:
            return Primitives.Int32.pack(-1)
        if isinstance(string, unicode):
            string = string.encode('utf-8')
        length = len(string)
        return Primitives.Int32.pack(length) + string

    @staticmethod
    def unpack(data):
        b = _Bytes.unpack(data)
        if sys.version_info.major < 3:
            return b
        else:
            if b is None:
                return b
            return b.decode("utf-8")


class _Bytes(_Primitive):

    @staticmethod
    def pack(data):
        return _String.pack(data)

    @staticmethod
    def unpack(data):
        length = Primitives.Int32.unpack(data)
        if length == -1:
            return None
        return data.read(length)


class _Null(_Primitive):

    @staticmethod
    def pack(data):
        return b""

    @staticmethod
    def unpack(data):
        return None


class _Guid(_Primitive):

    @staticmethod
    def pack(guid):
        # convert python UUID 6 field format to OPC UA 4 field format
        f1 = Primitives.UInt32.pack(guid.time_low)
        f2 = Primitives.UInt16.pack(guid.time_mid)
        f3 = Primitives.UInt16.pack(guid.time_hi_version)
        f4a = Primitives.Byte.pack(guid.clock_seq_hi_variant)
        f4b = Primitives.Byte.pack(guid.clock_seq_low)
        f4c = struct.pack('>Q', guid.node)[2:8]  # no primitive .pack available for 6 byte int
        f4 = f4a+f4b+f4c
        # concat byte fields
        b = f1+f2+f3+f4

        return b

    @staticmethod
    def unpack(data):
        # convert OPC UA 4 field format to python UUID bytes
        f1 = struct.pack('>I', Primitives.UInt32.unpack(data))
        f2 = struct.pack('>H', Primitives.UInt16.unpack(data))
        f3 = struct.pack('>H', Primitives.UInt16.unpack(data))
        f4 = data.read(8)
        # concat byte fields
        b = f1 + f2 + f3 + f4

        return uuid.UUID(bytes=b)


class _Primitive1(_Primitive):
    def __init__(self, fmt):
        self.struct = struct.Struct(fmt)
        self.size = self.struct.size
        self.format = self.struct.format

    def pack(self, data):
        return struct.pack(self.format, data)

    def unpack(self, data):
        return struct.unpack(self.format, data.read(self.size))[0]
    
    #def pack_array(self, array):
        #"""
        #Basically the same as the method in _Primitive but MAYBE a bit more efficient....
        #"""
        #if array is None:
            #return b'\xff\xff\xff\xff'
        #length = len(array)
        #if length == 0:
            #return b'\x00\x00\x00\x00'
        #if length == 1:
            #return b'\x01\x00\x00\x00' + self.pack(array[0])
        #return struct.pack(build_array_format("<i", length, self.format[1]), length, *array)


class Primitives1(object):
    Int8 = _Primitive1("<b")
    SByte = Int8
    Int16 = _Primitive1("<h")
    Int32 = _Primitive1("<i")
    Int64 = _Primitive1("<q")
    UInt8 = _Primitive1("<B")
    Char = UInt8
    Byte = UInt8
    UInt16 = _Primitive1("<H")
    UInt32 = _Primitive1("<I")
    UInt64 = _Primitive1("<Q")
    Boolean = _Primitive1("<?")
    Double = _Primitive1("<d")
    Float = _Primitive1("<f")


class Primitives(Primitives1):
    Null = _Null()
    String = _String()
    Bytes = _Bytes()
    ByteString = _Bytes()
    CharArray = _Bytes()
    DateTime = _DateTime()
    Guid = _Guid()


def pack_uatype_array(vtype, array):
    if array is None:
        return b'\xff\xff\xff\xff'
    length = len(array)
    b = [pack_uatype(vtype, val) for val in array]
    b.insert(0, Primitives.Int32.pack(length))
    return b"".join(b)


def pack_uatype(vtype, value):
    if hasattr(Primitives, vtype.name):
        return getattr(Primitives, vtype.name).pack(value)
    elif vtype.value > 25:
        return Primitives.Bytes.pack(value)
    elif vtype.name == "ExtensionObject":
        # dependency loop: classes in uaprotocol_auto use Variant defined in this file,
        # but Variant can contain any object from uaprotocol_auto as ExtensionObject.
        # Using local import to avoid import loop
        from opcua.ua.uaprotocol_auto import extensionobject_to_binary
        return extensionobject_to_binary(value)
    else:
        try:
            return value.to_binary()
        except AttributeError:
            raise UaError("{0} could not be packed with value {1}".format(vtype, value))


def unpack_uatype(vtype, data):
    if hasattr(Primitives, vtype.name):
        st = getattr(Primitives, vtype.name)
        return st.unpack(data)
    elif vtype.value > 25:
        return Primitives.Bytes.unpack(data)
    elif vtype.name == "ExtensionObject":
        # dependency loop: classes in uaprotocol_auto use Variant defined in this file,
        # but Variant can contain any object from uaprotocol_auto as ExtensionObject.
        # Using local import to avoid import loop
        from opcua.ua.uaprotocol_auto import extensionobject_from_binary
        return extensionobject_from_binary(data)
    else:
        from opcua.ua import uatypes
        if hasattr(uatypes, vtype.name):
            klass = getattr(uatypes, vtype.name)
            return klass.from_binary(data)
        else:
            raise UaError("can not unpack unknown vtype {0!s}".format(vtype))


def unpack_uatype_array(vtype, data):
    if hasattr(Primitives, vtype.name):
        st = getattr(Primitives, vtype.name)
        return st.unpack_array(data)
    else:
        length = Primitives.Int32.unpack(data)
        if length == -1:
            return None
        else:
            return [unpack_uatype(vtype, data) for _ in range(length)]


