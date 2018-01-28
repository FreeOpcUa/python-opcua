
import struct
from opcua import ua
from opcua.ua.ua_binary import Primitives


async def header_from_binary(data):
    hdr = ua.Header()
    hdr.MessageType, hdr.ChunkType, hdr.packet_size = struct.unpack("<3scI", await data.read(8))
    hdr.body_size = hdr.packet_size - 8
    if hdr.MessageType in (ua.MessageType.SecureOpen, ua.MessageType.SecureClose, ua.MessageType.SecureMessage):
        hdr.body_size -= 4
        hdr.ChannelId = Primitives.UInt32.unpack(ua.utils.Buffer(await data.read(4)))
    return hdr
