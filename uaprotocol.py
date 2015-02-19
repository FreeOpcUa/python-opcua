from protocol_auto import *

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
        #s = self.EndpointUrl.encode('utf-8')
        #s = self.EndpointUrl.encode('utf-8')
        b.append(struct.pack("<I", len(self.EndpointUrl)))
        b.append(self.EndpointUrl.encode("utf-8"))
        #b.append(struct.pack("<{}s".format(len(s)), s))
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
    def __init__(self, msgType=0, chunkType=0):
        self.MessageType = msgType
        self.ChunkType = chunkType
        self.Size = 8

    def add_size(self, size):
        self.Size += size

    def to_binary(self):
        b = []
        b.append(struct.pack("<3B", *self.MessageType))
        b.append(struct.pack("<c", self.ChunkType))
        b.append(struct.pack("<I", self.Size))
        return b"".join(b)

    @staticmethod
    def from_binary(data):
        hdr = Header()
        hdr.MessageType = struct.unpack("<3c", data.read(3))[0]
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

    def from_binary(self, data):
        self.Code = struct.unpack("<I", data.read(4))[0]
        size = struct.unpack("<i", data.read(4))[0]
        self.Reason = struct.unpack("<{}s".format(size), data.read(size))[0]



#class SecureHeader:
    #def __init__(self):
      #MessageType Type;
      #ChunkType Chunk;
      #uint32_t Size;
      #uint32_t ChannelID;

    #def to_binary(self):

    #def from_binary(self, data):




if __name__ == "__main__":
    from IPython import embed
    h = Header(MessageType.Hello, ChunkType.Single)
    h.Size = 20
    print("header", h.to_binary())
    hello = Hello()
    hello.EndpointUrl = "opc.tcp::/localhost"
    print("hello", hello.to_binary())
    embed()

