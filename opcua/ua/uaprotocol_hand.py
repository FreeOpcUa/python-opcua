import struct
import logging
import hashlib
from datetime import datetime

from opcua.ua import uaprotocol_auto as auto
from opcua.ua import uatypes
from opcua.ua import ua_binary as uabin
from opcua.ua import UaError
from opcua.common import utils
from opcua.ua.uatypes import AccessLevel

logger = logging.getLogger('opcua.uaprotocol')

OPC_TCP_SCHEME = 'opc.tcp'


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
        b.append(uabin.Primitives.UInt32.pack(self.ProtocolVersion))
        b.append(uabin.Primitives.UInt32.pack(self.ReceiveBufferSize))
        b.append(uabin.Primitives.UInt32.pack(self.SendBufferSize))
        b.append(uabin.Primitives.UInt32.pack(self.MaxMessageSize))
        b.append(uabin.Primitives.UInt32.pack(self.MaxChunkCount))
        b.append(uabin.Primitives.String.pack(self.EndpointUrl))
        return b"".join(b)

    @staticmethod
    def from_binary(data):
        hello = Hello()
        hello.ProtocolVersion = uabin.Primitives.UInt32.unpack(data)
        hello.ReceiveBufferSize = uabin.Primitives.UInt32.unpack(data)
        hello.SendBufferSize = uabin.Primitives.UInt32.unpack(data)
        hello.MaxMessageSize = uabin.Primitives.UInt32.unpack(data)
        hello.MaxChunkCount = uabin.Primitives.UInt32.unpack(data)
        hello.EndpointUrl = uabin.Primitives.String.unpack(data)
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
        b.append(uabin.Primitives.UInt32.pack(size))
        if self.MessageType in (MessageType.SecureOpen, MessageType.SecureClose, MessageType.SecureMessage):
            b.append(uabin.Primitives.UInt32.pack(self.ChannelId))
        return b"".join(b)

    @staticmethod
    def from_string(data):
        hdr = Header()
        hdr.MessageType, hdr.ChunkType, hdr.packet_size = struct.unpack("<3scI", data.read(8))
        hdr.body_size = hdr.packet_size - 8
        if hdr.MessageType in (MessageType.SecureOpen, MessageType.SecureClose, MessageType.SecureMessage):
            hdr.body_size -= 4
            hdr.ChannelId = uabin.Primitives.UInt32.unpack(data)
        return hdr

    @staticmethod
    def max_size():
        return struct.calcsize("<3scII")

    def __str__(self):
        return "Header(type:{0}, chunk_type:{1}, body_size:{2}, channel:{3})".format(
            self.MessageType, self.ChunkType, self.body_size, self.ChannelId)
    __repr__ = __str__


class ErrorMessage(uatypes.FrozenClass):

    def __init__(self):
        self.Error = uatypes.StatusCode()
        self.Reason = ""
        self._freeze = True

    def to_binary(self):
        b = []
        b.append(self.Error.to_binary())
        b.append(uabin.Primitives.String.pack(self.Reason))
        return b"".join(b)

    @staticmethod
    def from_binary(data):
        ack = ErrorMessage()
        ack.Error = uatypes.StatusCode.from_binary(data)
        ack.Reason = uabin.Primitives.String.unpack(data)
        return ack

    def __str__(self):
        return "MessageAbort(error:{0}, reason:{1})".format(self.Error, self.Reason)
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
        self.SenderCertificate = None
        self.ReceiverCertificateThumbPrint = None
        self._freeze = True

    def to_binary(self):
        b = []
        b.append(uabin.Primitives.String.pack(self.SecurityPolicyURI))
        b.append(uabin.Primitives.String.pack(self.SenderCertificate))
        b.append(uabin.Primitives.String.pack(self.ReceiverCertificateThumbPrint))
        return b"".join(b)

    @staticmethod
    def from_binary(data):
        hdr = AsymmetricAlgorithmHeader()
        hdr.SecurityPolicyURI = uabin.Primitives.String.unpack(data)
        hdr.SenderCertificate = uabin.Primitives.Bytes.unpack(data)
        hdr.ReceiverCertificateThumbPrint = uabin.Primitives.Bytes.unpack(data)
        return hdr

    def __str__(self):
        return "{0}(SecurityPolicy:{1}, certificatesize:{2}, receiverCertificatesize:{3} )".format(
            self.__class__.__name__, self.SecurityPolicyURI, len(self.SenderCertificate),
            len(self.ReceiverCertificateThumbPrint))
    __repr__ = __str__


class SymmetricAlgorithmHeader(uatypes.FrozenClass):

    def __init__(self):
        self.TokenId = 0
        self._freeze = True

    @staticmethod
    def from_binary(data):
        obj = SymmetricAlgorithmHeader()
        obj.TokenId = uabin.Primitives.UInt32.unpack(data)
        return obj

    def to_binary(self):
        return uabin.Primitives.UInt32.pack(self.TokenId)

    @staticmethod
    def max_size():
        return struct.calcsize("<I")

    def __str__(self):
        return "{0}(TokenId:{1} )".format(self.__class__.__name__, self.TokenId)
    __repr__ = __str__


class SequenceHeader(uatypes.FrozenClass):

    def __init__(self):
        self.SequenceNumber = None
        self.RequestId = None
        self._freeze = True

    @staticmethod
    def from_binary(data):
        obj = SequenceHeader()
        obj.SequenceNumber = uabin.Primitives.UInt32.unpack(data)
        obj.RequestId = uabin.Primitives.UInt32.unpack(data)
        return obj

    def to_binary(self):
        b = []
        b.append(uabin.Primitives.UInt32.pack(self.SequenceNumber))
        b.append(uabin.Primitives.UInt32.pack(self.RequestId))
        return b"".join(b)

    @staticmethod
    def max_size():
        return struct.calcsize("<II")

    def __str__(self):
        return "{0}(SequenceNumber:{1}, RequestId:{2} )".format(
            self.__class__.__name__, self.SequenceNumber, self.RequestId)
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


class SecurityPolicy(object):
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
        self.server_certificate = None
        self.client_certificate = None

    def make_symmetric_key(self, a, b):
        pass


class SecurityPolicyFactory(object):
    """
    Helper class for creating server-side SecurityPolicy.
    Server has one certificate and private key, but needs a separate
    SecurityPolicy for every client and client's certificate
    """

    def __init__(self, cls=SecurityPolicy, mode=auto.MessageSecurityMode.None_,
                 certificate=None, private_key=None):
        self.cls = cls
        self.mode = mode
        self.certificate = certificate
        self.private_key = private_key

    def matches(self, uri, mode=None):
        return self.cls.URI == uri and (mode is None or self.mode == mode)

    def create(self, peer_certificate):
        if self.cls is SecurityPolicy:
            return self.cls()
        else:
            return self.cls(peer_certificate,
                            self.certificate, self.private_key,
                            self.mode)


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
            raise UaError("Unsupported message type: {0}".format(msg_type))
        self.SequenceHeader = SequenceHeader()
        self.Body = body
        self._security_policy = security_policy

    @staticmethod
    def from_binary(security_policy, data):
        h = Header.from_string(data)
        return MessageChunk.from_header_and_body(security_policy, h, data)

    @staticmethod
    def from_header_and_body(security_policy, header, buf):
        assert len(buf) >= header.body_size, 'Full body expected here'
        data = buf.copy(header.body_size)
        buf.skip(header.body_size)
        if header.MessageType in (MessageType.SecureMessage, MessageType.SecureClose):
            security_header = SymmetricAlgorithmHeader.from_binary(data)
            crypto = security_policy.symmetric_cryptography
        elif header.MessageType == MessageType.SecureOpen:
            security_header = AsymmetricAlgorithmHeader.from_binary(data)
            crypto = security_policy.asymmetric_cryptography
        else:
            raise UaError("Unsupported message type: {0}".format(header.MessageType))
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
    def message_to_chunks(security_policy, body, max_chunk_size,
                          message_type=MessageType.SecureMessage, channel_id=1, request_id=1, token_id=1):
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
                chunk.SecurityHeader.ReceiverCertificateThumbPrint =\
                    hashlib.sha1(security_policy.server_certificate).digest()
            chunk.MessageHeader.ChannelId = channel_id
            chunk.SequenceHeader.RequestId = request_id
            return [chunk]

        crypto = security_policy.symmetric_cryptography
        max_size = MessageChunk.max_body_size(crypto, max_chunk_size)

        chunks = []
        for i in range(0, len(body), max_size):
            part = body[i:i + max_size]
            if i + max_size >= len(body):
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
        return "{0}({1}, {2}, {3}, {4} bytes)".format(self.__class__.__name__,
                                                 self.MessageHeader, self.SequenceHeader,
                                                 self.SecurityHeader, len(self.Body))
    __repr__ = __str__


class Message(object):

    def __init__(self, chunks):
        self._chunks = chunks

    def request_id(self):
        return self._chunks[0].SequenceHeader.RequestId

    def SequenceHeader(self):
        return self._chunks[0].SequenceHeader

    def SecurityHeader(self):
        return self._chunks[0].SecurityHeader

    def body(self):
        body = b"".join([c.Body for c in self._chunks])
        return utils.Buffer(body)


class SecureConnection(object):
    """
    Common logic for client and server
    """

    def __init__(self, security_policy):
        self._sequence_number = 0
        self._peer_sequence_number = None
        self._incoming_parts = []
        self._security_policy = security_policy
        self._policies = []
        self.channel = auto.OpenSecureChannelResult()
        self._old_tokens = []
        self._open = False
        self._max_chunk_size = 65536

    def set_channel(self, channel):
        """
        Called on client side when getting secure channel data from server
        """
        self.channel = channel

    def open(self, params, server):
        """
        called on server side to open secure channel
        """
        if not self._open or params.RequestType == auto.SecurityTokenRequestType.Issue:
            self._open = True
            self.channel = auto.OpenSecureChannelResult()
            self.channel.SecurityToken.TokenId = 13  # random value
            self.channel.SecurityToken.ChannelId = server.get_new_channel_id()
            self.channel.SecurityToken.RevisedLifetime = params.RequestedLifetime
        else:
            self._old_tokens.append(self.channel.SecurityToken.TokenId)
        self.channel.SecurityToken.TokenId += 1
        self.channel.SecurityToken.CreatedAt = datetime.utcnow()
        self.channel.SecurityToken.RevisedLifetime = params.RequestedLifetime
        self.channel.ServerNonce = utils.create_nonce(self._security_policy.symmetric_key_size)
        self._security_policy.make_symmetric_key(self.channel.ServerNonce, params.ClientNonce)
        return self.channel

    def close(self):
        self._open = False

    def is_open(self):
        return self._open

    def set_policy_factories(self, policies):
        """
        Set a list of available security policies.
        Use this in servers with multiple endpoints with different security
        """
        self._policies = policies

    @staticmethod
    def _policy_matches(policy, uri, mode=None):
        return policy.URI == uri and (mode is None or policy.Mode == mode)

    def select_policy(self, uri, peer_certificate, mode=None):
        for policy in self._policies:
            if policy.matches(uri, mode):
                self._security_policy = policy.create(peer_certificate)
                return
        if self._security_policy.URI != uri or (mode is not None and
                                                self._security_policy.Mode != mode):
            raise UaError("No matching policy: {0}, {1}".format(uri, mode))

    def tcp_to_binary(self, message_type, message):
        """
        Convert OPC UA TCP message (see OPC UA specs Part 6, 7.1) to binary.
        The only supported types are Hello, Acknowledge and ErrorMessage
        """
        header = Header(message_type, ChunkType.Single)
        binmsg = message.to_binary()
        header.body_size = len(binmsg)
        return header.to_binary() + binmsg

    def message_to_binary(self, message, message_type=MessageType.SecureMessage, request_id=0, algohdr=None):
        """
        Convert OPC UA secure message to binary.
        The only supported types are SecureOpen, SecureMessage, SecureClose
        if message_type is SecureMessage, the AlgoritmHeader should be passed as arg
        """
        if algohdr is None:
            token_id = self.channel.SecurityToken.TokenId
        else:
            token_id = algohdr.TokenId
        chunks = MessageChunk.message_to_chunks(
            self._security_policy, message, self._max_chunk_size,
            message_type=message_type,
            channel_id=self.channel.SecurityToken.ChannelId,
            request_id=request_id,
            token_id=token_id)
        for chunk in chunks:
            self._sequence_number += 1
            if self._sequence_number >= (1 << 32):
                logger.debug("Wrapping sequence number: %d -> 1", self._sequence_number)
                self._sequence_number = 1
            chunk.SequenceHeader.SequenceNumber = self._sequence_number
        return b"".join([chunk.to_binary() for chunk in chunks])

    def _check_incoming_chunk(self, chunk):
        assert isinstance(chunk, MessageChunk), "Expected chunk, got: {0}".format(chunk)
        if chunk.MessageHeader.MessageType != MessageType.SecureOpen:
            if chunk.MessageHeader.ChannelId != self.channel.SecurityToken.ChannelId:
                raise UaError("Wrong channel id {0}, expected {1}".format(
                    chunk.MessageHeader.ChannelId,
                    self.channel.SecurityToken.ChannelId))
            if chunk.SecurityHeader.TokenId != self.channel.SecurityToken.TokenId:
                if chunk.SecurityHeader.TokenId not in self._old_tokens:
                    logger.warning("Received a chunk with wrong token id %s, expected %s", chunk.SecurityHeader.TokenId, self.channel.SecurityToken.TokenId)

                    #raise UaError("Wrong token id {}, expected {}, old tokens are {}".format(
                        #chunk.SecurityHeader.TokenId,
                        #self.channel.SecurityToken.TokenId,
                        #self._old_tokens))

                else:
                    # Do some cleanup, spec says we can remove old tokens when new one are used
                    idx = self._old_tokens.index(chunk.SecurityHeader.TokenId)
                    if idx != 0:
                        self._old_tokens = self._old_tokens[idx:]
        if self._incoming_parts:
            if self._incoming_parts[0].SequenceHeader.RequestId != chunk.SequenceHeader.RequestId:
                raise UaError("Wrong request id {0}, expected {1}".format(
                    chunk.SequenceHeader.RequestId,
                    self._incoming_parts[0].SequenceHeader.RequestId))

        # sequence number must be incremented or wrapped
        num = chunk.SequenceHeader.SequenceNumber
        if self._peer_sequence_number is not None:
            if num != self._peer_sequence_number + 1:
                wrap = (1 << 32) - 1024
                if num < 1024 and self._peer_sequence_number >= wrap:
                    # specs Part 6, 6.7.2
                    logger.debug("Sequence number wrapped: %d -> %d",
                                 self._peer_sequence_number, num)
                else:
                    raise UaError(
                        "Wrong sequence {0} -> {1} (server bug or replay attack)"
                        .format(self._peer_sequence_number, num))
        self._peer_sequence_number = num

    def receive_from_header_and_body(self, header, body):
        """
        Convert MessageHeader and binary body to OPC UA TCP message (see OPC UA
        specs Part 6, 7.1: Hello, Acknowledge or ErrorMessage), or a Message
        object, or None (if intermediate chunk is received)
        """
        if header.MessageType == MessageType.SecureOpen:
            data = body.copy(header.body_size)
            security_header = AsymmetricAlgorithmHeader.from_binary(data)
            self.select_policy(security_header.SecurityPolicyURI, security_header.SenderCertificate)

        if header.MessageType in (MessageType.SecureMessage,
                                  MessageType.SecureOpen,
                                  MessageType.SecureClose):
            chunk = MessageChunk.from_header_and_body(self._security_policy,
                                                      header, body)
            return self._receive(chunk)
        elif header.MessageType == MessageType.Hello:
            msg = Hello.from_binary(body)
            self._max_chunk_size = msg.ReceiveBufferSize
            return msg
        elif header.MessageType == MessageType.Acknowledge:
            msg = Acknowledge.from_binary(body)
            self._max_chunk_size = msg.SendBufferSize
            return msg
        elif header.MessageType == MessageType.Error:
            msg = ErrorMessage.from_binary(body)
            logger.warning("Received an error: %s", msg)
            return msg
        else:
            raise UaError("Unsupported message type {0}".format(header.MessageType))

    def receive_from_socket(self, socket):
        """
        Convert binary stream to OPC UA TCP message (see OPC UA
        specs Part 6, 7.1: Hello, Acknowledge or ErrorMessage), or a Message
        object, or None (if intermediate chunk is received)
        """
        logger.debug("Waiting for header")
        header = Header.from_string(socket)
        logger.info("received header: %s", header)
        body = socket.read(header.body_size)
        if len(body) != header.body_size:
            raise UaError("{0} bytes expected, {1} available".format(header.body_size, len(body)))
        return self.receive_from_header_and_body(header, utils.Buffer(body))

    def _receive(self, msg):
        self._check_incoming_chunk(msg)
        self._incoming_parts.append(msg)
        if msg.MessageHeader.ChunkType == ChunkType.Intermediate:
            return None
        if msg.MessageHeader.ChunkType == ChunkType.Abort:
            err = ErrorMessage.from_binary(utils.Buffer(msg.Body))
            logger.warning("Message %s aborted: %s", msg, err)
            # specs Part 6, 6.7.3 say that aborted message shall be ignored
            # and SecureChannel should not be closed
            self._incoming_parts = []
            return None
        elif msg.MessageHeader.ChunkType == ChunkType.Single:
            message = Message(self._incoming_parts)
            self._incoming_parts = []
            return message
        else:
            raise UaError("Unsupported chunk type: {0}".format(msg))


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
        self.AccessLevel = AccessLevel.CurrentRead.mask
        self.UserAccessLevel = AccessLevel.CurrentRead.mask


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

#AttributeIdsInv = {v: k for k, v in AttributeIds.__dict__.items()}
