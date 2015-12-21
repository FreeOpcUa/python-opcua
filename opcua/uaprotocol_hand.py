# -*- coding: utf-8 -*-

import struct
import logging
import hashlib

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


class Hello(uatypes.FrozenClass):

    def __init__(self):
        self.ProtocolVersion = 0
        self.ReceiveBufferSize = 65536
        self.SendBufferSize = 65536
        self.MaxMessageSize = 0
        self.MaxChunkCount = 0
        self.EndpointUrl = ""
        self._freeze = True

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
    Abort = b"A"    # when an error occurred and the Message is aborted (body is ErrorMessage)


class Header(uatypes.FrozenClass):

    def __init__(self, msgType=None, chunkType=None, channelid=0):
        self.MessageType = msgType
        self.ChunkType = chunkType
        self.ChannelId = channelid
        self.body_size = 0
        self.packet_size = 0
        self._freeze = True

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

    @staticmethod
    def max_size():
        return struct.calcsize("<3scII")

    def __str__(self):
        return "Header(type:{}, chunk_type:{}, body_size:{}, channel:{})".format(self.MessageType, self.ChunkType, self.body_size, self.ChannelId)
    __repr__ = __str__


class ErrorMessage(uatypes.FrozenClass):

    def __init__(self):
        self.Error = uatypes.StatusCode()
        self.Reason = ""
        self._freeze = True

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


class Acknowledge(uatypes.FrozenClass):

    def __init__(self):
        self.ProtocolVersion = 0
        self.ReceiveBufferSize = 65536
        self.SendBufferSize = 65536
        self.MaxMessageSize = 0  # No limits
        self.MaxChunkCount = 0  # No limits
        self._freeze = True

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


class AsymmetricAlgorithmHeader(uatypes.FrozenClass):

    def __init__(self):
        self.SecurityPolicyURI = "http://opcfoundation.org/UA/SecurityPolicy#None"
        self.SenderCertificate = b""
        self.ReceiverCertificateThumbPrint = b""
        self._freeze = True

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


class SymmetricAlgorithmHeader(uatypes.FrozenClass):

    def __init__(self):
        self.TokenId = 0
        self._freeze = True

    @staticmethod
    def from_binary(data):
        obj = SymmetricAlgorithmHeader()
        obj.TokenId = uatype_UInt32.unpack(data.read(4))[0]
        return obj

    def to_binary(self):
        return uatype_UInt32.pack(self.TokenId)

    @staticmethod
    def max_size():
        return struct.calcsize("<I")

    def __str__(self):
        return "{}(TokenId:{} )".format(self.__class__.__name__, self.TokenId)
    __repr__ = __str__


class SequenceHeader(uatypes.FrozenClass):

    def __init__(self):
        self.SequenceNumber = None
        self.RequestId = None
        self._freeze = True

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

    @staticmethod
    def max_size():
        return struct.calcsize("<II")

    def __str__(self):
        return "{}(SequenceNumber:{}, RequestId:{} )".format(self.__class__.__name__, self.SequenceNumber, self.RequestId)
    __repr__ = __str__


class CryptographyNone:
    """
    Base class for symmetric/asymmetric cryprography
    """
    def __init__(self):
        pass

    def plain_block_size(self):
        """
        Size of plain text block for block cipher.
        """
        return 1

    def encrypted_block_size(self):
        """
        Size of encrypted text block for block cipher.
        """
        return 1

    def padding(self, size):
        """
        Create padding for a block of given size.
        plain_size = size + len(padding) + signature_size()
        plain_size = N * plain_block_size()
        """
        return b''

    def min_padding_size(self):
        return 0

    def signature_size(self):
        return 0

    def signature(self, data):
        return b''

    def encrypt(self, data):
        return data

    def decrypt(self, data):
        return data

    def vsignature_size(self):
        return 0

    def verify(self, data, signature):
        """
        Verify signature and raise exception if signature is invalid
        """
        pass

    def remove_padding(self, data):
        return data


class SecurityPolicy:
    """
    Base class for security policy
    """
    URI = "http://opcfoundation.org/UA/SecurityPolicy#None"
    signature_key_size = 0
    symmetric_key_size = 0

    def __init__(self):
        self.asymmetric_cryptography = CryptographyNone()
        self.symmetric_cryptography = CryptographyNone()
        self.Mode = auto.MessageSecurityMode.None_
        self.server_certificate = b""
        self.client_certificate = b""

    def make_symmetric_key(self, a, b):
        pass


class MessageChunk(uatypes.FrozenClass):
    """
    Message Chunk, as described in OPC UA specs Part 6, 6.7.2.
    """
    def __init__(self, security_policy, body=b'', msg_type=MessageType.SecureMessage, chunk_type=ChunkType.Single):
        self.MessageHeader = Header(msg_type, chunk_type)
        if msg_type in (MessageType.SecureMessage, MessageType.SecureClose):
            self.SecurityHeader = SymmetricAlgorithmHeader()
        elif msg_type == MessageType.SecureOpen:
            self.SecurityHeader = AsymmetricAlgorithmHeader()
        else:
            raise Exception("Unsupported message type: {}".format(msg_type))
        self.SequenceHeader = SequenceHeader()
        self.Body = body
        self._security_policy = security_policy

    @staticmethod
    def from_binary(security_policy, data):
        h = Header.from_string(data)
        return MessageChunk.from_header_and_body(security_policy, h, data)

    @staticmethod
    def from_header_and_body(security_policy, header, data):
        if header.MessageType in (MessageType.SecureMessage, MessageType.SecureClose):
            security_header = SymmetricAlgorithmHeader.from_binary(data)
            crypto = security_policy.symmetric_cryptography
        elif header.MessageType == MessageType.SecureOpen:
            security_header = AsymmetricAlgorithmHeader.from_binary(data)
            crypto = security_policy.asymmetric_cryptography
        else:
            raise Exception("Unsupported message type: {}".format(header.MessageType))
        obj = MessageChunk(crypto)
        obj.MessageHeader = header
        obj.SecurityHeader = security_header
        decrypted = crypto.decrypt(data.read(len(data)))
        signature_size = crypto.vsignature_size()
        if signature_size > 0:
            signature = decrypted[-signature_size:]
            decrypted = decrypted[:-signature_size]
            crypto.verify(obj.MessageHeader.to_binary() + obj.SecurityHeader.to_binary() + decrypted, signature)
        data = utils.Buffer(crypto.remove_padding(decrypted))
        obj.SequenceHeader = SequenceHeader.from_binary(data)
        obj.Body = data.read(len(data))
        return obj

    def encrypted_size(self, plain_size):
        size = plain_size + self._security_policy.signature_size()
        pbs = self._security_policy.plain_block_size()
        assert(size % pbs == 0)
        return size // pbs * self._security_policy.encrypted_block_size()

    def to_binary(self):
        security = self.SecurityHeader.to_binary()
        encrypted_part = self.SequenceHeader.to_binary() + self.Body
        encrypted_part += self._security_policy.padding(len(encrypted_part))
        self.MessageHeader.body_size = len(security) + self.encrypted_size(len(encrypted_part))
        header = self.MessageHeader.to_binary()
        encrypted_part += self._security_policy.signature(header + security + encrypted_part)
        return header + security + self._security_policy.encrypt(encrypted_part)

    @staticmethod
    def max_body_size(crypto, max_chunk_size):
        max_encrypted_size = max_chunk_size - Header.max_size() - SymmetricAlgorithmHeader.max_size()
        max_plain_size = (max_encrypted_size // crypto.encrypted_block_size()) * crypto.plain_block_size()
        return max_plain_size - SequenceHeader.max_size() - crypto.signature_size() - crypto.min_padding_size()

    @staticmethod
    def message_to_chunks(security_policy, body, max_chunk_size, message_type=MessageType.SecureMessage, channel_id=1, request_id=1, token_id=1):
        """
        Pack message body (as binary string) into one or more chunks.
        Size of each chunk will not exceed max_chunk_size.
        Returns a list of MessageChunks. SequenceNumber is not initialized here,
        it must be set by Secure Channel driver.
        """
        if message_type == MessageType.SecureOpen:
            # SecureOpen message must be in a single chunk (specs, Part 6, 6.7.2)
            chunk = MessageChunk(security_policy.asymmetric_cryptography, body, message_type, ChunkType.Single)
            chunk.SecurityHeader.SecurityPolicyURI = security_policy.URI
            if security_policy.client_certificate:
                chunk.SecurityHeader.SenderCertificate = security_policy.client_certificate
            if security_policy.server_certificate:
                chunk.SecurityHeader.ReceiverCertificateThumbPrint = hashlib.sha1(security_policy.server_certificate).digest()
            chunk.MessageHeader.ChannelId = channel_id
            chunk.SequenceHeader.RequestId = request_id
            return [chunk]

        crypto = security_policy.symmetric_cryptography
        max_size = MessageChunk.max_body_size(crypto, max_chunk_size)

        chunks = []
        for i in range(0, len(body), max_size):
            part = body[i:i+max_size]
            if i+max_size >= len(body):
                chunk_type = ChunkType.Single
            else:
                chunk_type = ChunkType.Intermediate
            chunk = MessageChunk(crypto, part, message_type, chunk_type)
            chunk.SecurityHeader.TokenId = token_id
            chunk.MessageHeader.ChannelId = channel_id
            chunk.SequenceHeader.RequestId = request_id
            chunks.append(chunk)
        return chunks

    def __str__(self):
        return "{}({}, {}, {}, {} bytes)".format(self.__class__.__name__,
                self.MessageHeader, self.SequenceHeader, self.SecurityHeader, len(self.Body))
    __repr__ = __str__


def tcp_message_from_header_and_body(security_policy, header, body):
    """
    Convert binary stream to OPC UA TCP message (see OPC UA specs Part 6, 7.1)
    The only supported message types are Hello, Acknowledge and Error
    """
    if header.MessageType in (MessageType.SecureOpen, MessageType.SecureClose, MessageType.SecureMessage):
        return MessageChunk.from_header_and_body(security_policy, header, body)
    elif header.MessageType == MessageType.Hello:
        return Hello.from_binary(body)
    elif header.MessageType == MessageType.Acknowledge:
        return Acknowledge.from_binary(body)
    elif header.MessageType == MessageType.Error:
        return ErrorMessage.from_binary(body)
    else:
        raise Exception("Unsupported message type {}".format(header.MessageType))


def tcp_message_from_socket(security_policy, socket):
    logger.debug("Waiting for header")
    header = Header.from_string(socket)
    logger.info("received header: %s", header)
    body = socket.read(header.body_size)
    if len(body) != header.body_size:
        raise Exception("{} bytes expected, {} available".format(header.body_size, len(body)))
    return tcp_message_from_header_and_body(security_policy, header, utils.Buffer(body))


# FIXES for missing switchfield in NodeAttributes classes
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
        self.SpecifiedAttributes = ana.DisplayName | ana.Description | ana.WriteMask | ana.UserWriteMask | ana.Value | ana.DataType | ana.ValueRank | ana.ArrayDimensions | ana.AccessLevel | ana.UserAccessLevel | ana.MinimumSamplingInterval | ana.Historizing
        self.Historizing = False


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


class Argument(auto.Argument):

    def __init__(self):
        auto.Argument.__init__(self)
        self.ValueRank = -2


AttributeIdsInv = {v: k for k, v in AttributeIds.__dict__.items()}
