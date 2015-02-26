#from . import uaprotocol_auto as auto
from .uaprotocol_auto import *
import struct 

class Hello(object):
    def __init__(self):
        self.ProtocolVersion = 0
        self.ReceiveBufferSize = 65536
        self.SendBufferSize = 65536
        self.MaxMessageSize = 65536
        self.MaxChunkCount = 256
        self.EndpointUrl = ""

    def to_binary(self):
        b = []
        b.append(struct.pack("<I", self.ProtocolVersion))
        b.append(struct.pack("<I", self.ReceiveBufferSize))
        b.append(struct.pack("<I", self.SendBufferSize))
        b.append(struct.pack("<I", self.MaxMessageSize))
        b.append(struct.pack("<I", self.MaxChunkCount))
        b.append(pack_string(self.EndpointUrl))
        return b"".join(b)

    def get_binary_size(self):
        return 5*4


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
    def __init__(self, msgType=None, chunkType=None):
        self.MessageType = msgType
        self.ChunkType = chunkType
        self.Size = 8

    def add_size(self, size):
        self.Size += size

    def to_binary(self):
        b = []
        b.append(struct.pack("<3s", self.MessageType))
        b.append(struct.pack("<s", self.ChunkType))
        b.append(struct.pack("<I", self.Size))
        return b"".join(b)

    @staticmethod
    def from_binary(data):
        hdr = Header()
        hdr.MessageType = struct.unpack("<3s", data.read(3))[0]
        hdr.ChunkType = struct.unpack("<c", data.read(1))[0]
        hdr.Size = struct.unpack("<I", data.read(4))[0]
        return hdr

    def __str__(self):
        return "Header(type:{},size:{})".format(self.MessageType, self.Size)
    __repr__ = __str__


class Acknowledge:
    def __init__(self):
        self.ProtocolVersion = None
        self.ReceiveBufferSize = None
        self.SendBufferSize = None
        self.MaxMessageSize = None
        self.MaxChunkCount = None

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



class SecureHeader(Header):
    def __init__(self, msgtype=None, chunktype=None, channelid=0):
        Header.__init__(self, msgtype, chunktype)
        self.ChannelId = channelid
        self.Size = 12

    def to_binary(self):
        b = []
        b.append(Header.to_binary(self))
        b.append(struct.pack("<I", self.ChannelId))
        return b"".join(b)

    @staticmethod
    def from_binary(data):
        hdr = SecureHeader()
        hdr.MessageType = struct.unpack("<3s", data.read(3))[0]
        hdr.ChunkType = struct.unpack("<c", data.read(1))[0]
        hdr.Size = struct.unpack("<I", data.read(4))[0]
        hdr.ChannelId = struct.unpack("<I", data.read(4))[0]
        return hdr

    def __str__(self):
        return "Header(type:{},size:{},channel:{})".format(self.MessageType, self.Size, self.ChannelId)
    __repr__ = __str__

class AsymmetricAlgorithmHeader:
    def __init__(self):
        self.SecurityPolicyURI = "http://opcfoundation.org/UA/SecurityPolicy#None"
        self.SenderCertificate = b""
        self.ReceiverCertificateThumbPrint = b""

    def to_binary(self):
        b = []
        b.append(pack_string(self.SecurityPolicyURI))
        b.append(pack_string(self.SenderCertificate))
        b.append(pack_string(self.ReceiverCertificateThumbPrint))
        return b"".join(b)

    @staticmethod
    def from_binary(data):
        hdr = AsymmetricAlgorithmHeader()
        hdr.SecurityPolicyURI = unpack_bytes(data)
        hdr.SenderCertificate = unpack_bytes(data)
        hdr.ReceiverCertificateThumbPrint = unpack_bytes(data)
        return hdr

    def __str__(self):
        return "{}(SecurytyPolicy:{}, certificatesize:{}, receiverCertificatesize )".format(self.__class__.__name__, self.SecurityPolicyURI, len(self.SenderCertificate), len(self.ReceiverCertificateThumbPrint))
    __repr__ = __str__


class SymmetricAlgorithmHeader:
    def __init__(self):
        self.TokenId = None

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
        return "{}(SequenceNumber:{}, RequestId )".format(self.__class__.__name__, self.SequenceNumber, self.RequestId)
    __repr__ = __str__


if __name__ == "__main__":
    from IPython import embed
    h = Header(MessageType.Hello, ChunkType.Single)
    h.Size = 20
    print("header", h.to_binary())
    hello = Hello()
    hello.EndpointUrl = "opc.tcp::/localhost"
    print("hello", hello.to_binary())
    embed()

