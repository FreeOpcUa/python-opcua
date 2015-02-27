"""
Low level binary client
"""
import io
import logging
import socket
from threading import Thread, Condition

from . import uaprotocol as ua

class RequestCallback(object):
    def __init__(self, callback=None):
        self.condition = Condition()
        self.data = None


class BinaryClient(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.logger = logging.getLogger(self.__class__.__name__)
        self.socket = None
        self._do_stop = False
        self._security_token = ua.ChannelSecurityToken()
        self._authentication_token = ua.NodeId()
        self._sequence_number = 0
        self._request_id = 0
        self._request_handle = 0
        self._callbackmap = {}
        self._dostop = False

    def run(self):
        self.logger.info("Thread started")
        while not self._dostop:
            data = self._receive()
        self.logger.info("Thread ended")

    def _recv_header(self):
        data = self.socket.recv(8)
        header = ua.Header.from_binary(io.BytesIO(data))
        self.logger.info(header)
        return header

    def _receive(self):
        self.logger.info("Waiting for socket data")
        data = self.socket.recv(12)
        while len(data) != 12:
            self.logger.warn("received %s bytes, we expected 12, waiting", len(data))
            data += self.socket.recv(12-len(data))
            return
        header = ua.SecureHeader.from_binary(io.BytesIO(data))
        self.logger.info("received header: %s", header)
        if header.MessageType == ua.MessageType.Error:
            self.logger.warn("Received an error message type")
            return None
        nbbytes = header.Size - 12
        self.logger.info("reading rest of message (%s bytes)", nbbytes)
        data = self.socket.recv(nbbytes)
        self.logger.info("Asked socket for {} bytes, received {}".format(nbbytes, len(data)))
        if nbbytes != len(data):
            self.logger.warn("Error, did not received expected number of bytes")
            return None
        data = io.BytesIO(data)
        if header.MessageType == ua.MessageType.SecureOpen:
            algohdr = ua.AsymmetricAlgorithmHeader.from_binary(data)
        elif header.MessageType == ua.MessageType.SecureMessage:
            algohdr = ua.SymmetricAlgorithmHeader.from_binary(data)
        else:
            self.logger.warn("Unsupported message type")
            return
        self.logger.info(algohdr)
        seqhdr = ua.SequenceHeader.from_binary(data)
        self.logger.info(seqhdr)
        if not seqhdr.RequestId in self._callbackmap:
            self.logger.warn("No callback object found for request: {}", seqhdr.RequestId)
            return
        rcall = self._callbackmap[seqhdr.RequestId]
        rcall.condition.acquire()
        rcall.data = data
        rcall.condition.notify_all()
        rcall.condition.release()
        del(self._callbackmap[seqhdr.RequestId])

    def stop(self):
        self._do_stop = True

    def connect(self):
        self.logger.info("opening connection")
        self.socket = socket.create_connection(('localhost', 4841))

    def send_hello(self, url):
        hello = ua.Hello()
        hello.EndpointUrl = url
        header = ua.Header(ua.MessageType.Hello, ua.ChunkType.Single)
        self._write_socket(header, hello)
        header = self._recv_header()
        data = self.socket.recv(header.Size)
        return  ua.Acknowledge.from_binary(io.BytesIO(data))
    
    def _write_socket(self, hdr, *args):
        self.logger.info("wrtting to socket")
        alle = []
        for arg in args:
            data = arg.to_binary()
            hdr.add_size(len(data))
            self.logger.debug("preparing to write: %s with length %s and data %s",  arg, len(data), data)
            alle.append(data)
        alle.insert(0, hdr.to_binary())
        #self.logger.info(data)
        alle = b"".join(alle)
        self.socket.send(alle)

    def open_secure_channel(self, params):
        self.logger.info("open_secure_channel")
        request = ua.OpenSecureChannelRequest()
        request.Parameters = params
        request.RequestHeader = self._create_request_header()

        hdr = ua.SecureHeader(ua.MessageType.SecureOpen, ua.ChunkType.Single, self._security_token.TokenId)
        asymhdr = ua.AsymmetricAlgorithmHeader()
        seqhdr = self._create_sequence_header()
        self._write_socket(hdr, asymhdr, seqhdr, request)

        rcall = RequestCallback()
        self._callbackmap[seqhdr.RequestId] = rcall
        rcall.condition.acquire()
        rcall.condition.wait()
        #FICME: could copy data here ....
        rcall.condition.release()


        response = ua.OpenSecureChannelResponse.from_binary(rcall.data)
        self._security_token = response.Parameters.SecurityToken
        self.logger.info(response)
        return response

    def create_session(self, parameters):
        self.logger.info("create_session")
        request = ua.CreateSessionRequest()
        request.Parameters = parameters
        response = self._send_request(request)
        response = ua.CreateSessionResponse.from_binary(data)
        return response.Parameters

    def get_endpoints(self, params, callback=None):
        self.logger.info("get_endpoint")
        request = ua.GetEndpointsRequest()
        request.Parameters = params
        print(request)
        data = self._send_request(request)
        response = ua.GetEndpointsResponse.from_binary(data)
        self.logger.info(response)
        return response.Endpoints

    def _send_request(self, request):
        request.RequestHeader = self._create_request_header()
        hdr = ua.SecureHeader(ua.MessageType.SecureMessage, ua.ChunkType.Single, self._security_token.TokenId)
        symhdr = ua.SymmetricAlgorithmHeader()
        seqhdr = self._create_sequence_header()
        self._write_socket(hdr, symhdr, seqhdr, request)
        rcall = RequestCallback()
        self._callbackmap[seqhdr.RequestId] = rcall
        with rcall.condition:
            rcall.condition.wait()
            return rcall.data

    def _create_request_header(self):
        hdr = ua.RequestHeader()
        hdr.AuthenticationToken = self._authentication_token
        self._request_handle += 1
        hdr.RequestHandle = self._request_handle
        hdr.TimeoutHint = 10000
        return hdr

    def _create_algo_header(self):
        hdr = ua.SymmetricAlgorithmHeader()
        hdr.TokenId = self._security_token.TokenId
        return hdr

    def _create_sequence_header(self):
        hdr = ua.SequenceHeader()
        self._sequence_number += 1
        hdr.SequenceNumber = self._sequence_number
        self._request_id += 1
        hdr.RequestId = self._request_id
        return hdr

