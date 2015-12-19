import struct
import logging

import opcua.uaprotocol_auto as auto
import opcua.uatypes as uatypes
from opcua.uatypes import uatype_UInt32
import opcua.utils as utils
from opcua.object_ids import ObjectIds
from opcua.attribute_ids import AttributeIds

logger = logging.getLogger('opcua.uaprotocol')

OPC_TCP_SCHEME = 'opc.tcp'

class AccessLevelMask(object):
    """
    used by AccessLevel and UserAccessLevel
    """
    CurrentRead = 0
    CurrentWrite = 1
    HistoryRead = 2
    HistoryWrite = 3
    SemanticChange = 4


class Hello(object):

    __slots__ = [
        "ProtocolVersion",
        "ReceiveBufferSize",
        "SendBufferSize",
        "MaxMessageSize",
        "MaxChunkCount",
        "EndpointUrl",
    ]

    def __init__(self):
        self.ProtocolVersion = 0
        self.ReceiveBufferSize = 65536
        self.SendBufferSize = 65536
        self.MaxMessageSize = 0
        self.MaxChunkCount = 0
        self.EndpointUrl = ""

    def to_binary(self):
        b = []
        b.append(uatype_UInt32.pack(self.ProtocolVersion))
        b.append(uatype_UInt32.pack(self.ReceiveBufferSize))
        b.append(uatype_UInt32.pack(self.SendBufferSize))
        b.append(uatype_UInt32.pack(self.MaxMessageSize))
        b.append(uatype_UInt32.pack(self.MaxChunkCount))
        b.append(uatypes.pack_string(self.EndpointUrl))
        return b"".join(b)

    @staticmethod
    def from_binary(data):
        hello = Hello()
        hello.ProtocolVersion = uatype_UInt32.unpack(data.read(4))[0]
        hello.ReceiveBufferSize = uatype_UInt32.unpack(data.read(4))[0]
        hello.SendBufferSize = uatype_UInt32.unpack(data.read(4))[0]
        hello.MaxMessageSize = uatype_UInt32.unpack(data.read(4))[0]
        hello.MaxChunkCount = uatype_UInt32.unpack(data.read(4))[0]
        hello.EndpointUrl = uatypes.unpack_string(data)
        return hello


class MessageType(object):
    Invalid = b"INV"  # FIXME: check value
    Hello = b"HEL"
    Acknowledge = b"ACK"
    Error = b"ERR"
    SecureOpen = b"OPN"
    SecureClose = b"CLO"
    SecureMessage = b"MSG"


class ChunkType(object):
    Invalid = b"0"  # FIXME check
    Single = b"F"
    Intermediate = b"C"
    Final = b"A"


class Header(object):
    __slots__ = [
        "MessageType",
        "ChunkType",
        "ChannelId",
        "body_size",
        "packet_size",
    ]

    def __init__(self, msgType=None, chunkType=None, channelid=0):
        self.MessageType = msgType
        self.ChunkType = chunkType
        self.ChannelId = channelid
        self.body_size = 0
        self.packet_size = 0

    def add_size(self, size):
        self.body_size += size

    def to_binary(self):
        b = []
        b.append(struct.pack("<3ss", self.MessageType, self.ChunkType))
        size = self.body_size + 8
        if self.MessageType in (MessageType.SecureOpen, MessageType.SecureClose, MessageType.SecureMessage):
            size += 4
        b.append(uatype_UInt32.pack(size))
        if self.MessageType in (MessageType.SecureOpen, MessageType.SecureClose, MessageType.SecureMessage):
            b.append(uatype_UInt32.pack(self.ChannelId))
        return b"".join(b)

    @staticmethod
    def from_string(data):
        hdr = Header()
        hdr.MessageType, hdr.ChunkType, hdr.packet_size = struct.unpack("<3scI", data.read(8))
        hdr.body_size = hdr.packet_size - 8
        if hdr.MessageType in (MessageType.SecureOpen, MessageType.SecureClose, MessageType.SecureMessage):
            hdr.body_size -= 4
            hdr.ChannelId = uatype_UInt32.unpack(data.read(4))[0]
        return hdr

    def __str__(self):
        return "Header(type:{}, chunk_type:{}, body_size:{}, channel:{})".format(self.MessageType, self.ChunkType, self.body_size, self.ChannelId)
    __repr__ = __str__


class ErrorMessage(object):
    __slots__ = [
        "Error",
        "Reason",
    ]

    def __init__(self):
        self.Error = uatypes.StatusCode()
        self.Reason = ""

    def to_binary(self):
        b = []
        b.append(self.Error.to_binary())
        b.append(uatypes.pack_string(self.Reason))
        return b"".join(b)

    @staticmethod
    def from_binary(data):
        ack = ErrorMessage()
        ack.Error = uatypes.StatusCode.from_binary(data)
        ack.Reason = uatypes.unpack_string(data)
        return ack

    def __str__(self):
        return "MessageAbort(error:{}, reason:{})".format(self.Error, self.Reason)
    __repr__ = __str__


class Acknowledge(object):
    __slots__ = [
        "ProtocolVersion",
        "ReceiveBufferSize",
        "SendBufferSize",
        "MaxMessageSize",
        "MaxChunkCount",
    ]

    def __init__(self):
        self.ProtocolVersion = 0
        self.ReceiveBufferSize = 65536
        self.SendBufferSize = 65536
        self.MaxMessageSize = 0  # No limits
        self.MaxChunkCount = 0  # No limits

    def to_binary(self):
        return struct.pack(
            "<5I",
            self.ProtocolVersion,
            self.ReceiveBufferSize,
            self.SendBufferSize,
            self.MaxMessageSize,
            self.MaxChunkCount)

    @staticmethod
    def from_binary(data):
        ack = Acknowledge()
        ack.ProtocolVersion, ack.ReceiveBufferSize, ack.SendBufferSize, ack.MaxMessageSize, ack.MaxChunkCount \
            = struct.unpack("<5I", data.read(20))
        return ack


class AsymmetricAlgorithmHeader(object):
    __slots__ = [
        "SecurityPolicyURI",
        "SenderCertificate",
        "ReceiverCertificateThumbPrint",
    ]

    def __init__(self):
        self.SecurityPolicyURI = "http://opcfoundation.org/UA/SecurityPolicy#None"
        self.SenderCertificate = b""
        self.ReceiverCertificateThumbPrint = b""

    def to_binary(self):
        b = []
        b.append(uatypes.pack_string(self.SecurityPolicyURI))
        b.append(uatypes.pack_string(self.SenderCertificate))
        b.append(uatypes.pack_string(self.ReceiverCertificateThumbPrint))
        return b"".join(b)

    @staticmethod
    def from_binary(data):
        hdr = AsymmetricAlgorithmHeader()
        hdr.SecurityPolicyURI = uatypes.unpack_bytes(data)
        hdr.SenderCertificate = uatypes.unpack_bytes(data)
        hdr.ReceiverCertificateThumbPrint = uatypes.unpack_bytes(data)
        return hdr

    def __str__(self):
        return "{}(SecurytyPolicy:{}, certificatesize:{}, receiverCertificatesize:{} )".format(self.__class__.__name__, self.SecurityPolicyURI, len(self.SenderCertificate), len(self.ReceiverCertificateThumbPrint))
    __repr__ = __str__


class SymmetricAlgorithmHeader(object):
    __slots__ = [
        "TokenId",
    ]

    def __init__(self):
        self.TokenId = 0

    @staticmethod
    def from_binary(data):
        obj = SymmetricAlgorithmHeader()
        obj.TokenId = uatype_UInt32.unpack(data.read(4))[0]
        return obj

    def to_binary(self):
        return uatype_UInt32.pack(self.TokenId)

    def __str__(self):
        return "{}(TokenId:{} )".format(self.__class__.__name__, self.TokenId)
    __repr__ = __str__


class SequenceHeader(object):
    __slots__ = [
        "SequenceNumber",
        "RequestId",
    ]

    def __init__(self):
        self.SequenceNumber = None
        self.RequestId = None

    @staticmethod
    def from_binary(data):
        obj = SequenceHeader()
        obj.SequenceNumber = uatype_UInt32.unpack(data.read(4))[0]
        obj.RequestId = uatype_UInt32.unpack(data.read(4))[0]
        return obj

    def to_binary(self):
        b = []
        b.append(uatype_UInt32.pack(self.SequenceNumber))
        b.append(uatype_UInt32.pack(self.RequestId))
        return b"".join(b)

    def __str__(self):
        return "{}(SequenceNumber:{}, RequestId:{} )".format(self.__class__.__name__, self.SequenceNumber, self.RequestId)
    __repr__ = __str__

# FIXES for missing switchfield in NodeAttributes classes
ana = auto.NodeAttributesMask


class ObjectAttributes(auto.ObjectAttributes):
    __slots__ = [
    ]

    def __init__(self):
        auto.ObjectAttributes.__init__(self)
        self.SpecifiedAttributes = ana.DisplayName | ana.Description | ana.WriteMask | ana.UserWriteMask | ana.EventNotifier


class ObjectTypeAttributes(auto.ObjectTypeAttributes):
    __slots__ = [
    ]

    def __init__(self):
        auto.ObjectTypeAttributes.__init__(self)
        self.SpecifiedAttributes = ana.DisplayName | ana.Description | ana.WriteMask | ana.UserWriteMask | ana.IsAbstract


class VariableAttributes(auto.VariableAttributes):
    __slots__ = [
    ]

    def __init__(self):
        auto.VariableAttributes.__init__(self)
        self.SpecifiedAttributes = ana.DisplayName | ana.Description | ana.WriteMask | ana.UserWriteMask | ana.Value | ana.DataType | ana.ValueRank | ana.ArrayDimensions | ana.AccessLevel | ana.UserAccessLevel | ana.MinimumSamplingInterval | ana.Historizing
        self.Historizing = False


class VariableTypeAttributes(auto.VariableTypeAttributes):
    __slots__ = [
    ]

    def __init__(self):
        auto.VariableTypeAttributes.__init__(self)
        self.SpecifiedAttributes = ana.DisplayName | ana.Description | ana.WriteMask | ana.UserWriteMask | ana.Value | ana.DataType | ana.ValueRank | ana.ArrayDimensions | ana.IsAbstract


class MethodAttributes(auto.MethodAttributes):
    __slots__ = [
    ]

    def __init__(self):
        auto.MethodAttributes.__init__(self)
        self.SpecifiedAttributes = ana.DisplayName | ana.Description | ana.WriteMask | ana.UserWriteMask | ana.Executable | ana.UserExecutable


class ReferenceTypeAttributes(auto.ReferenceTypeAttributes):
    __slots__ = [
    ]

    def __init__(self):
        auto.ReferenceTypeAttributes.__init__(self)
        self.SpecifiedAttributes = ana.DisplayName | ana.Description | ana.WriteMask | ana.UserWriteMask | ana.IsAbstract | ana.Symmetric | ana.InverseName


class DataTypeAttributes(auto.DataTypeAttributes):
    __slots__ = [
    ]

    def __init__(self):
        auto.DataTypeAttributes.__init__(self)
        self.SpecifiedAttributes = ana.DisplayName | ana.Description | ana.WriteMask | ana.UserWriteMask | ana.IsAbstract


class ViewAttributes(auto.ViewAttributes):
    __slots__ = [
    ]

    def __init__(self):
        auto.ViewAttributes.__init__(self)
        self.SpecifiedAttributes = ana.DisplayName | ana.Description | ana.WriteMask | ana.UserWriteMask | ana.ContainsNoLoops | ana.EventNotifier


class Argument(auto.Argument):
    __slots__ = [
    ]

    def __init__(self):
        auto.Argument.__init__(self)
        self.ValueRank = -2


AttributeIdsInv = {v: k for k, v in AttributeIds.__dict__.items()}
