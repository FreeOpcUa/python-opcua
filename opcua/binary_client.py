"""
Low level binary client
"""
import io
import logging
import socket
from threading import Thread, Condition, Lock

from . import uaprotocol as ua

class RequestCallback(object):
    def __init__(self, callback=None):
        self.condition = Condition()
        self.data = None


class BinaryClient(object):
    """
    low level OPC-UA client.
    implement all(well..one day) methods defined in opcua spec
    taking in argument the structures defined in opcua spec
    in python most of the structures are defined in
    uaprotocol_auto.py and uaprotocol_hand.py
    """
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self._socket = None
        self._do_stop = False
        self._security_token = ua.ChannelSecurityToken()
        self._authentication_token = ua.NodeId()
        self._sequence_number = 0
        self._request_id = 0
        self._request_handle = 0
        self._callbackmap = {}
        self._thread = None
        self._lock = Lock()

    def start(self):
        """
        Start receiving thread.
        this is called automatically in connect and
        should not be necessary to call directly
        """
        self._thread = Thread(target=self._run)
        self._thread.start()

    def _send_request(self, request):
        with self._lock:
            request.RequestHeader = self._create_request_header()
            hdr = ua.Header(ua.MessageType.SecureMessage, ua.ChunkType.Single, self._security_token.TokenId)
            symhdr = ua.SymmetricAlgorithmHeader()
            seqhdr = self._create_sequence_header()
            rcall = RequestCallback()
            self._callbackmap[seqhdr.RequestId] = rcall
            self._write_socket(hdr, symhdr, seqhdr, request)
        with rcall.condition:
            rcall.condition.wait()
            return rcall.data

    def _run(self):
        self.logger.info("Thread started")
        while not self._do_stop:
            try:
                self._receive()
            except ua.SocketClosedException:
                self.logger.warn("Socket has closed connection")
                break
        self.logger.info("Thread ended")

    def _receive_header(self):
        self.logger.debug("Waiting for header")
        header = ua.Header.from_stream(self._socket)
        self.logger.info("received header: %s", header)
        return header

    def _receive_body(self, size):
        self.logger.info("reading body of message (%s bytes)", size)
        data = self._socket.recv(size)
        if size != len(data):
            raise Exception("Error, did not received expected number of bytes")
        return io.BytesIO(data)

    def _receive(self):
        header = self._receive_header()
        if header is None:
            return
        if header.MessageType == ua.MessageType.Error:
            self.logger.warn("Received an error message type")
            return None
        body = self._receive_body(header.body_size)
        if header.MessageType == ua.MessageType.Acknowledge:
            self._call_callback(0, body)
            return
        elif header.MessageType == ua.MessageType.SecureOpen:
            algohdr = ua.AsymmetricAlgorithmHeader.from_binary(body)
            self.logger.info(algohdr)
        elif header.MessageType == ua.MessageType.SecureMessage:
            algohdr = ua.SymmetricAlgorithmHeader.from_binary(body)
            self.logger.info(algohdr)
        else:
            self.logger.warn("Unsupported message type: %s", header.MessageType)
            return
        seqhdr = ua.SequenceHeader.from_binary(body)
        self.logger.info(seqhdr)
        self._call_callback(seqhdr.RequestId, body)

    def _call_callback(self, requestId, body):
        rcall = self._callbackmap.pop(requestId, None)
        if rcall is None:
            raise Exception("No callback object found for request: {}, callbacks in list are {}".format(requestId, self._callbackmap.keys()))
        rcall.condition.acquire()
        rcall.data = body
        rcall.condition.notify_all()
        rcall.condition.release()

    def _write_socket(self, hdr, *args):
        self.logger.info("wrtting to socket")
        alle = []
        for arg in args:
            data = arg.to_binary()
            hdr.add_size(len(data))
            self.logger.debug("writting to socket: %s with length %s ", type(arg), len(data))
            self.logger.debug("struct: %s", arg)
            self.logger.debug("data: %s", data)
            alle.append(data)
        alle.insert(0, hdr.to_binary())
        alle = b"".join(alle)
        self._socket.send(alle)

    def connect(self):
        """
        connect to server socket and start receiving thread
        """
        self.logger.info("opening connection")
        self._socket = socket.create_connection(('localhost', 4841))
        self.start()

    def disconnect(self):
        self.logger.info("stop request")
        self._do_stop = True
        self._socket.shutdown(socket.SHUT_WR)

    def send_hello(self, url):
        hello = ua.Hello()
        hello.EndpointUrl = url
        header = ua.Header(ua.MessageType.Hello, ua.ChunkType.Single)
        self._write_socket(header, hello)
        rcall = RequestCallback()
        self._callbackmap[0] = rcall
        with rcall.condition:
            rcall.condition.wait()
        return  ua.Acknowledge.from_binary(rcall.data)
 
    def open_secure_channel(self, params):
        self.logger.info("open_secure_channel")
        request = ua.OpenSecureChannelRequest()
        request.Parameters = params
        request.RequestHeader = self._create_request_header()

        hdr = ua.Header(ua.MessageType.SecureOpen, ua.ChunkType.Single, self._security_token.TokenId)
        asymhdr = ua.AsymmetricAlgorithmHeader()
        seqhdr = self._create_sequence_header()
        self._write_socket(hdr, asymhdr, seqhdr, request)

        rcall = RequestCallback()
        self._callbackmap[seqhdr.RequestId] = rcall
        with rcall.condition:
            rcall.condition.wait()
            #FICME: could copy data here ....

        response = ua.OpenSecureChannelResponse.from_binary(rcall.data)
        self._security_token = response.Parameters.SecurityToken
        self.logger.info(response)
        return response

    def create_session(self, parameters):
        self.logger.info("create_session")
        request = ua.CreateSessionRequest()
        request.Parameters = parameters
        data = self._send_request(request)
        response = ua.CreateSessionResponse.from_binary(data)
        self._authentication_token = response.Parameters.AuthenticationToken
        return response.Parameters

    def activate_session(self, parameters):
        self.logger.info("activate_session")
        request = ua.ActivateSessionRequest()
        request.Parameters = parameters
        data = self._send_request(request)
        response = ua.ActivateSessionResponse.from_binary(data)
        return response.Parameters

    def close_session(self, deletesubscriptions):
        self.logger.info("close_session")
        request = ua.CloseSessionRequest()
        request.DeleteSubscriptions = deletesubscriptions
        data = self._send_request(request)
        response = ua.CloseSessionResponse.from_binary(data)

    def browse(self, parameters):
        self.logger.info("browse")
        request = ua.BrowseRequest()
        request.Parameters = parameters
        data = self._send_request(request)
        response = ua.BrowseResponse.from_binary(data)
        return response.Results

    def read(self, parameters):
        self.logger.info("read")
        request = ua.ReadRequest()
        request.Parameters = parameters
        data = self._send_request(request)
        response = ua.ReadResponse.from_binary(data)
        return response.Results






    def get_endpoints(self, params, callback=None):
        self.logger.info("get_endpoint")
        request = ua.GetEndpointsRequest()
        request.Parameters = params
        data = self._send_request(request)
        response = ua.GetEndpointsResponse.from_binary(data)
        return response.Endpoints

    def close_secure_channel(self):
        """
        close secure channel. It seems to trigger a shutdown of socket
        in most servers, so be prepare to reconnect
        """
        self.logger.info("get_endpoint")
        request = ua.CloseSecureChannelRequest()
        request.RequestHeader = self._create_request_header()

        hdr = ua.Header(ua.MessageType.SecureClose, ua.ChunkType.Single, self._security_token.TokenId)
        symhdr = ua.SymmetricAlgorithmHeader()
        seqhdr = self._create_sequence_header()
        self._write_socket(hdr, symhdr, seqhdr, request)

        #some servers send a response here, most do not ... so we ignore

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

