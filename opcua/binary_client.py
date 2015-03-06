"""
Low level binary client
"""
#import io
import logging
import socket
from threading import Thread, Condition, Lock

import opcua.uaprotocol as ua

class Buffer(object):
    """
    alternative to io.BytesIO making debug easier
    """
    def __init__(self, data):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.data = data

    def __str__(self):
        return "Buffer(size:{}, data:{})".format(len(self.data), self.data)
    __repr__ = __str__

    def read(self, size):
        if size > len(self.data):
            raise Exception("No enough data left in buffer, request for {}, we have {}".format(size, self))
        #self.logger.debug("Request for %s bytes, from %s", size, self)
        data = self.data[:size]
        self.data = self.data[size:]
        #self.logger.debug("Returning: %s ", data)
        return data


class RequestCallback(object):
    def __init__(self):
        self.condition = Condition()
        self.data = None
        self.callback = None


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
        #self._secure_channel_id = 0 
        self._authentication_token = ua.NodeId()
        self._sequence_number = 0
        self._request_id = 0
        self._request_handle = 0
        self._callbackmap = {}
        self._publishcallbacks = {}
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

    def _send_request(self, request, callback=None):
        #HACK to make sure we can convert our request to binary before increasing request counter etc ...
        request.to_binary()
        #END HACK
        with self._lock:
            request.RequestHeader = self._create_request_header()
            hdr = ua.Header(ua.MessageType.SecureMessage, ua.ChunkType.Single, self._security_token.ChannelId)
            symhdr = self._create_sym_algo_header()
            seqhdr = self._create_sequence_header()
            rcall = RequestCallback()
            rcall.callback = callback
            self._callbackmap[seqhdr.RequestId] = rcall
            self._write_socket(hdr, symhdr, seqhdr, request)
        if not callback:
            with rcall.condition:
                rcall.condition.wait()
                return rcall.data


    def _run(self):
        self.logger.info("Thread started")
        while not self._do_stop:
            try:
                self._receive()
            except ua.SocketClosedException:
                self.logger.info("Socket has closed connection")
                #FIXME: should we wake up all waiting conditions here??
                break
        self.logger.info("Thread ended")

    def _receive_header(self):
        self.logger.debug("Waiting for header")
        header = ua.Header.from_stream(self._socket)
        self.logger.info("received header: %s", header)
        return header

    def _receive_body(self, size):
        self.logger.debug("reading body of message (%s bytes)", size)
        data = self._socket.recv(size)
        if size != len(data):
            raise Exception("Error, did not received expected number of bytes, got {}, asked for {}".format(len(data), size))
        #return io.BytesIO(data)
        return Buffer(data)

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
        self.logger.debug(seqhdr)
        self._call_callback(seqhdr.RequestId, body)

    def _call_callback(self, requestId, body):
        rcall = self._callbackmap.pop(requestId, None)
        if rcall is None:
            raise Exception("No callback object found for request: {}, callbacks in list are {}".format(requestId, self._callbackmap.keys()))
        rcall.condition.acquire()
        rcall.data = body
        rcall.condition.notify_all()
        rcall.condition.release()
        if rcall.callback:
            rcall.callback(rcall)

    def _write_socket(self, hdr, *args):
        alle = []
        for arg in args:
            data = arg.to_binary()
            hdr.add_size(len(data))
            self.logger.info("writting to socket: %s with length %s ", type(arg), len(data))
            self.logger.debug("struct: %s", arg)
            self.logger.debug("data: %s", data)
            alle.append(data)
        alle.insert(0, hdr.to_binary())
        alle = b"".join(alle)
        self._socket.send(alle)

    def _create_request_header(self):
        hdr = ua.RequestHeader()
        hdr.AuthenticationToken = self._authentication_token
        self._request_handle += 1
        hdr.RequestHandle = self._request_handle
        hdr.TimeoutHint = 10000
        return hdr

    def _create_sym_algo_header(self):
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


    def connect_socket(self, host, port):
        """
        connect to server socket and start receiving thread
        """
        self.logger.info("opening connection")
        self._socket = socket.create_connection((host, port))
        self.start()

    def disconnect_socket(self):
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
        return ua.Acknowledge.from_binary(rcall.data)
 
    def open_secure_channel(self, params):
        self.logger.info("open_secure_channel")
        request = ua.OpenSecureChannelRequest()
        request.Parameters = params
        request.RequestHeader = self._create_request_header()

        hdr = ua.Header(ua.MessageType.SecureOpen, ua.ChunkType.Single, self._security_token.ChannelId)
        asymhdr = ua.AsymmetricAlgorithmHeader()
        seqhdr = self._create_sequence_header()
        self._write_socket(hdr, asymhdr, seqhdr, request)

        rcall = RequestCallback()
        self._callbackmap[seqhdr.RequestId] = rcall
        with rcall.condition:
            rcall.condition.wait()
            #FICME: could copy data here ....

        response = ua.OpenSecureChannelResponse.from_binary(rcall.data)
        response.ResponseHeader.ServiceResult.check()
        self._security_token = response.Parameters.SecurityToken
        self.logger.info(response)
        return response

    def create_session(self, parameters):
        self.logger.info("create_session")
        request = ua.CreateSessionRequest()
        request.Parameters = parameters
        data = self._send_request(request)
        response = ua.CreateSessionResponse.from_binary(data)
        response.ResponseHeader.ServiceResult.check()
        self._authentication_token = response.Parameters.AuthenticationToken
        return response.Parameters

    def activate_session(self, parameters):
        self.logger.info("activate_session")
        request = ua.ActivateSessionRequest()
        request.Parameters = parameters
        data = self._send_request(request)
        response = ua.ActivateSessionResponse.from_binary(data)
        response.ResponseHeader.ServiceResult.check()
        return response.Parameters

    def close_session(self, deletesubscriptions):
        self.logger.info("close_session")
        request = ua.CloseSessionRequest()
        request.DeleteSubscriptions = deletesubscriptions
        data = self._send_request(request)
        ua.CloseSessionResponse.from_binary(data)
        #response.ResponseHeader.ServiceResult.check() #disabled, it seems we sent wrong session Id, but where is the sessionId supposed to be sent???

    def browse(self, parameters):
        self.logger.info("browse")
        request = ua.BrowseRequest()
        request.Parameters = parameters
        data = self._send_request(request)
        response = ua.BrowseResponse.from_binary(data)
        response.ResponseHeader.ServiceResult.check()
        return response.Results

    def read(self, parameters):
        self.logger.info("read")
        request = ua.ReadRequest()
        request.Parameters = parameters
        data = self._send_request(request)
        response = ua.ReadResponse.from_binary(data)
        response.ResponseHeader.ServiceResult.check()
        return response.Results

    def write(self, nodestowrite):
        self.logger.info("read")
        request = ua.WriteRequest()
        request.NodesToWrite = nodestowrite
        data = self._send_request(request)
        response = ua.WriteResponse.from_binary(data)
        response.ResponseHeader.ServiceResult.check()
        return response.Results

    def get_endpoints(self, params):
        self.logger.info("get_endpoint")
        request = ua.GetEndpointsRequest()
        request.Parameters = params
        data = self._send_request(request)
        response = ua.GetEndpointsResponse.from_binary(data)
        response.ResponseHeader.ServiceResult.check()
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

    def translate_browsepaths_to_nodeids(self, browsepaths):
        self.logger.info("translate_browsepath_to_nodeid")
        request = ua.TranslateBrowsePathsToNodeIdsRequest()
        request.BrowsePaths = browsepaths
        data = self._send_request(request)
        response = ua.TranslateBrowsePathsToNodeIdsResponse.from_binary(data)
        response.ResponseHeader.ServiceResult.check()
        return response.Results

    def create_subscription(self, params, callback):
        self.logger.info("create_subscription")
        request = ua.CreateSubscriptionRequest()
        request.Parameters = params
        data = self._send_request(request)
        response = ua.CreateSubscriptionResponse.from_binary(data)
        response.ResponseHeader.ServiceResult.check()
        self._publishcallbacks[response.Parameters.SubscriptionId] = callback
        return response.Parameters

    def delete_subscriptions(self, subscriptionids):
        self.logger.info("delete_subscription")
        request = ua.DeleteSubscriptionsRequest()
        request.SubscriptionIds = subscriptionids
        data = self._send_request(request)
        response = ua.DeleteSubscriptionsResponse.from_binary(data)
        response.ResponseHeader.ServiceResult.check()
        for sid in subscriptionids:
            del(self._publishcallbacks[sid])
        return response.Results

    def publish(self, acks=None):
        self.logger.info("publish")
        if  acks is None:
            acks = []
        request = ua.PublishRequest()
        request.SubscriptionAcknowledgements = acks
        self._send_request(request, self._call_publish_callback)

    def _call_publish_callback(self, rcall):
        self.logger.info("call_publish_callback")
        response = ua.PublishResponse.from_binary(rcall.data)
        try:
            self._publishcallbacks[response.Parameters.SubscriptionId](response.Parameters)
        except Exception as ex: #we call client code, catch everything!
            self.logger.warn("exception while calling user callback:", ex)


    def create_monitored_items(self, params):
        self.logger.info("subscribe_data_change")
        request = ua.CreateMonitoredItemsRequest()
        request.Parameters = params
        data = self._send_request(request)
        response = ua.CreateMonitoredItemsResponse.from_binary(data)
        response.ResponseHeader.ServiceResult.check()
        return response.Results



