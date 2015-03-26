import io
import struct 
import logging

import opcua.uaprotocol_auto as auto
import opcua.uatypes as uatypes 
import opcua.utils as utils
from opcua.object_ids import ObjectIds

logger = logging.getLogger('opcua.uaprotocol')


class SocketClosedException(Exception):
    pass

def get_bytes_from_sock(sock, size):
    data = utils.recv_all(sock, size)
    if len(data) < size: #socket has closed!
        raise SocketClosedException("Server socket has closed")
    return io.BytesIO(data)

class LocalizedText(auto.LocalizedText):
    def __init__(self, text=""):
        auto.LocalizedText.__init__(self)
        self.Text = text.encode()


class Hello(object):
    def __init__(self):
        self.ProtocolVersion = 0
        self.ReceiveBufferSize = 65536
        self.SendBufferSize = 65536
        self.MaxMessageSize = 0
        self.MaxChunkCount = 0
        self.EndpointUrl = ""

    def to_binary(self):
        b = []
        b.append(struct.pack("<I", self.ProtocolVersion))
        b.append(struct.pack("<I", self.ReceiveBufferSize))
        b.append(struct.pack("<I", self.SendBufferSize))
        b.append(struct.pack("<I", self.MaxMessageSize))
        b.append(struct.pack("<I", self.MaxChunkCount))
        b.append(uatypes.pack_string(self.EndpointUrl))
        return b"".join(b)

    @staticmethod
    def from_binary(data):
        hello = Hello()
        hello.ProtocolVersion = struct.unpack("<I", data.read(4))[0]
        hello.ReceiveBufferSize = struct.unpack("<I", data.read(4))[0]
        hello.SendBufferSize = struct.unpack("<I", data.read(4))[0]
        hello.MaxMessageSize = struct.unpack("<I", data.read(4))[0]
        hello.MaxChunkCount = struct.unpack("<I", data.read(4))[0]
        hello.EndpointUrl = uatypes.unpack_string(data)
        return hello



class MessageType(object):
    Invalid = b"INV" #FIXME: check value
    Hello = b"HEL"
    Acknowledge = b"ACK"
    Error = b"ERR"
    SecureOpen = b"OPN"
    SecureClose = b"CLO"
    SecureMessage = b"MSG"

class ChunkType(object):
    Invalid = b"0" #FIXME check
    Single = b"F"
    Intermediate = b"C"
    Final = b"A"
 


class Header(object):
    def __init__(self, msgType=None, chunkType=None, channelid=0):
        self.MessageType = msgType
        self.ChunkType = chunkType
        self.ChannelId = channelid
        self.body_size = 0

    def add_size(self, size):
        self.body_size += size

    def to_binary(self):
        b = []
        b.append(struct.pack("<3s", self.MessageType))
        b.append(struct.pack("<s", self.ChunkType))
        size = self.body_size + 8
        if self.MessageType in (MessageType.SecureOpen, MessageType.SecureClose, MessageType.SecureMessage):
            size += 4
        b.append(struct.pack("<I", size))
        if self.MessageType in (MessageType.SecureOpen, MessageType.SecureClose, MessageType.SecureMessage):
            b.append(struct.pack("<I", self.ChannelId))
        return b"".join(b)

    @staticmethod
    def from_stream(sock):
        data = get_bytes_from_sock(sock, 8)
        hdr = Header()
        hdr.MessageType = struct.unpack("<3s", data.read(3))[0]
        hdr.ChunkType = struct.unpack("<c", data.read(1))[0]
        hdr.body_size = struct.unpack("<I", data.read(4))[0] - 8
        if hdr.MessageType in (MessageType.SecureOpen, MessageType.SecureClose, MessageType.SecureMessage):
            hdr.body_size -= 4
            data = get_bytes_from_sock(sock, 4)
            hdr.ChannelId = struct.unpack("<I", data.read(4))[0]
        return hdr

    def __str__(self):
        return "Header(type:{}, body_size:{}, channel:{})".format(self.MessageType, self.body_size, self.ChannelId)
    __repr__ = __str__


class ErrorMessage(object):
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


class Acknowledge:
    def __init__(self):
        self.ProtocolVersion = 0
        self.ReceiveBufferSize = 65536
        self.SendBufferSize = 65536
        self.MaxMessageSize = 0 #No limits
        self.MaxChunkCount = 0 #No limits

    def to_binary(self):
        b = []
        b.append(struct.pack("<I", self.ProtocolVersion))
        b.append(struct.pack("<I", self.ReceiveBufferSize))
        b.append(struct.pack("<I", self.SendBufferSize))
        b.append(struct.pack("<I", self.MaxMessageSize))
        b.append(struct.pack("<I", self.MaxChunkCount))
        return b"".join(b)



    @staticmethod
    def from_binary(data):
        ack = Acknowledge()
        ack.ProtocolVersion = struct.unpack("<I", data.read(4))[0]
        ack.ReceiveBufferSize = struct.unpack("<I", data.read(4))[0]
        ack.SendBufferSize = struct.unpack("<I", data.read(4))[0]
        ack.MaxMessageSize = struct.unpack("<I", data.read(4))[0]
        ack.MaxChunkCount = struct.unpack("<I", data.read(4))[0]
        return ack


class Error:
    def __init__(self):
        self.Code = None
        self.Reason = None

    @staticmethod
    def from_binary(data):
        obj = Error()
        obj.Code = struct.unpack("<I", data.read(4))[0]
        size = struct.unpack("<i", data.read(4))[0]
        obj.Reason = struct.unpack("<{}s".format(size), data.read(size))[0]


class AsymmetricAlgorithmHeader:
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


class SymmetricAlgorithmHeader:
    def __init__(self):
        self.TokenId = 0

    @staticmethod
    def from_binary(data):
        obj = SymmetricAlgorithmHeader()
        obj.TokenId = struct.unpack("<I", data.read(4))[0]
        return obj

    def to_binary(self):
        return struct.pack("<I", self.TokenId)

    def __str__(self):
        return "{}(TokenId:{} )".format(self.__class__.__name__, self.TokenId)
    __repr__ = __str__


class SequenceHeader:
    def __init__(self):
        self.SequenceNumber = None
        self.RequestId = None

    @staticmethod
    def from_binary(data):
        obj = SequenceHeader()
        obj.SequenceNumber = struct.unpack("<I", data.read(4))[0]
        obj.RequestId = struct.unpack("<I", data.read(4))[0]
        return obj

    def to_binary(self):
        b = []
        b.append(struct.pack("<I", self.SequenceNumber))
        b.append(struct.pack("<I", self.RequestId))
        return b"".join(b)

    def __str__(self):
        return "{}(SequenceNumber:{}, RequestId:{} )".format(self.__class__.__name__, self.SequenceNumber, self.RequestId)
    __repr__ = __str__

###FIXES for missing switchfield in NodeAttributes classes
ana = auto.NodeAttributesMask

class ObjectAttributes(auto.ObjectAttributes):
    def __init__(self):
        auto.ObjectAttributes.__init__(self)
        self.SpecifiedAttributes = ana.DisplayName | ana.Description | ana.WriteMask | ana.UserWriteMask | ana.EventNotifier

class ObjectTypeAttributes(auto.ObjectTypeAttributes):
    def __init__(self):
        auto.ObjectTypeAttributes.__init__(self)
        self.SpecifiedAttributes = ana.DisplayName | ana.Description | ana.WriteMask | ana.UserWriteMask | ana.IsAbstract




class VariableAttributes(auto.VariableAttributes):
    def __init__(self):
        auto.VariableAttributes.__init__(self)
        self.SpecifiedAttributes = ana.DisplayName | ana.Description | ana.WriteMask | ana.UserWriteMask | ana.Value | ana.DataType | ana.ValueRank | ana.ArrayDimensions | ana.AccessLevel | ana.UserAccessLevel | ana.MinimumSamplingInterval |ana.Historizing  

class VariableTypeAttributes(auto.VariableTypeAttributes):
    def __init__(self):
        auto.VariableTypeAttributes.__init__(self)
        self.SpecifiedAttributes = ana.DisplayName | ana.Description | ana.WriteMask | ana.UserWriteMask | ana.Value | ana.DataType | ana.ValueRank | ana.ArrayDimensions | ana.IsAbstract

class MethodAttributes(auto.MethodAttributes):
    def __init__(self):
        auto.MethodAttributes.__init__(self)
        self.SpecifiedAttributes = ana.DisplayName | ana.Description | ana.WriteMask | ana.UserWriteMask | ana.Executable | ana.UserExecutable 


class ReferenceTypeAttributes(auto.ReferenceTypeAttributes):
    def __init__(self):
        auto.ReferenceTypeAttributes.__init__(self)
        self.SpecifiedAttributes = ana.DisplayName | ana.Description | ana.WriteMask | ana.UserWriteMask | ana.IsAbstract | ana.Symmetric | ana.InverseName 

class DataTypeAttributes(auto.DataTypeAttributes):
    def __init__(self):
        auto.DataTypeAttributes.__init__(self)
        self.SpecifiedAttributes = ana.DisplayName | ana.Description | ana.WriteMask | ana.UserWriteMask | ana.IsAbstract 


class ViewAttributes(auto.ViewAttributes):
    def __init__(self):
        auto.ViewAttributes.__init__(self)
        self.SpecifiedAttributes = ana.DisplayName | ana.Description | ana.WriteMask | ana.UserWriteMask | ana.ContainsNoLoops | ana.EventNotifier 

ObjectIdsInv = {v: k for k, v in ObjectIds.__dict__.items()}

def downcast_extobject(item):
    objectidname = ObjectIdsInv[item.TypeId.Identifier]
    classname = objectidname.split("_")[0]
    cmd = "{}.from_binary(utils.Buffer(item.to_binary()))".format(classname)
    #logger.debug("running %s", cmd)
    return eval(cmd)

