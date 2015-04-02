"""
Low level binary client
"""

import logging
import socket
from threading import Thread, Lock
from concurrent.futures import Future

import opcua.uaprotocol as ua
import opcua.utils as utils


class BinaryClient(object):
    """
    low level OPC-UA client.
    implement all(well..one day) methods defined in opcua spec
    taking in argument the structures defined in opcua spec
    in python most of the structures are defined in
    uaprotocol_auto.py and uaprotocol_hand.py
    """
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self._socket = None
        self._do_stop = False
        self._security_token = ua.ChannelSecurityToken() 
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

    def _send_request(self, request, callback=None, timeout=1000):
        #HACK to make sure we can convert our request to binary before increasing request counter etc ...
        request.to_binary()
        #END HACK
        with self._lock:
            request.RequestHeader = self._create_request_header(timeout)
            hdr = ua.Header(ua.MessageType.SecureMessage, ua.ChunkType.Single, self._security_token.ChannelId)
            symhdr = self._create_sym_algo_header()
            seqhdr = self._create_sequence_header()
            future = Future()
            if callback:
                future.add_done_callback(callback)
            self._callbackmap[seqhdr.RequestId] = future
            self._write_socket(hdr, symhdr, seqhdr, request)
        if not callback:
            data = future.result()
            self._check_answer(data, " in response to " + request.__class__.__name__)
            return data

    def _check_answer(self, data, context):
        data = data.copy(50)#FIXME check max length nodeid + responseheader
        typeid = ua.NodeId.from_binary(data)
        if typeid == ua.FourByteNodeId(ua.ObjectIds.ServiceFault_Encoding_DefaultBinary):
            self.logger.warning("ServiceFault from server received %s", context)
            hdr = ua.ResponseHeader.from_binary(data)
            hdr.ServiceResult.check()

    def _run(self):
        self.logger.info("Thread started")
        while not self._do_stop:
            try:
                self._receive()
            except ua.SocketClosedException:
                self.logger.info("Socket has closed connection")
                break
        self.logger.info("Thread ended")

    def _receive_header(self):
        self.logger.debug("Waiting for header")
        header = ua.Header.from_stream(self._socket)
        self.logger.info("received header: %s", header)
        return header

    def _receive_body(self, size):
        self.logger.debug("reading body of message (%s bytes)", size)
        data = utils.recv_all(self._socket, size)
        if size != len(data):
            raise Exception("Error, did not received expected number of bytes, got {}, asked for {}".format(len(data), size))
        return utils.Buffer(data)

    def _receive(self):
        header = self._receive_header()
        if header is None:
            return
        body = self._receive_body(header.body_size)
        if header.MessageType == ua.MessageType.Error:
            self.logger.warning("Received an error message type")
            err = ua.ErrorMessage.from_binary(body)
            self.logger.warning(err)
            return None
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
            self.logger.warning("Unsupported message type: %s", header.MessageType)
            return
        seqhdr = ua.SequenceHeader.from_binary(body)
        self.logger.debug(seqhdr)
        self._call_callback(seqhdr.RequestId, body)

    def _call_callback(self, request_id, body):
        future = self._callbackmap.pop(request_id, None)
        if future is None:
            raise Exception("No future object found for request: {}, callbacks in list are {}".format(request_id, self._callbackmap.keys()))
        future.set_result(body)

    def _write_socket(self, hdr, *args):
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
        self._socket.sendall(alle)

    def _create_request_header(self, timeout=1000):
        hdr = ua.RequestHeader()
        hdr.AuthenticationToken = self._authentication_token
        self._request_handle += 1
        hdr.RequestHandle = self._request_handle
        hdr.TimeoutHint = timeout
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
        self._socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)#nodelay ncessary to avoid packing in one frame, some servers do not like it
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
        future = Future()
        self._callbackmap[0] = future
        return ua.Acknowledge.from_binary(future.result())
 
    def open_secure_channel(self, params):
        self.logger.info("open_secure_channel")
        request = ua.OpenSecureChannelRequest()
        request.Parameters = params
        request.RequestHeader = self._create_request_header()

        hdr = ua.Header(ua.MessageType.SecureOpen, ua.ChunkType.Single, self._security_token.ChannelId)
        asymhdr = ua.AsymmetricAlgorithmHeader()
        seqhdr = self._create_sequence_header()
        self._write_socket(hdr, asymhdr, seqhdr, request)

        future = Future()
        self._callbackmap[seqhdr.RequestId] = future

        response = ua.OpenSecureChannelResponse.from_binary(future.result())
        response.ResponseHeader.ServiceResult.check()
        self._security_token = response.Parameters.SecurityToken
        return response.Parameters

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

    def write(self, params):
        self.logger.info("read")
        request = ua.WriteRequest()
        request.Parameters = params
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

        hdr = ua.Header(ua.MessageType.SecureClose, ua.ChunkType.Single, self._security_token.ChannelId)
        symhdr = ua.SymmetricAlgorithmHeader()
        seqhdr = self._create_sequence_header()
        self._write_socket(hdr, symhdr, seqhdr, request)

        #some servers send a response here, most do not ... so we ignore

    def translate_browsepaths_to_nodeids(self, browsepaths):
        self.logger.info("translate_browsepath_to_nodeid")
        request = ua.TranslateBrowsePathsToNodeIdsRequest()
        request.Parameters.BrowsePaths = browsepaths
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
        request.Parameters.SubscriptionIds = subscriptionids
        data = self._send_request(request)
        response = ua.DeleteSubscriptionsResponse.from_binary(data)
        response.ResponseHeader.ServiceResult.check()
        for sid in subscriptionids:
            self._publishcallbacks.pop(sid)
        return response.Results

    def publish(self, acks=None):
        self.logger.info("publish")
        if  acks is None:
            acks = []
        request = ua.PublishRequest()
        request.SubscriptionAcknowledgements = acks
        self._send_request(request, self._call_publish_callback, timeout=0)

    def _call_publish_callback(self, future):
        self.logger.info("call_publish_callback")
        response = ua.PublishResponse.from_binary(future.result())
        try:
            self._publishcallbacks[response.Parameters.SubscriptionId](response.Parameters)
        except Exception as ex: #we call client code, catch everything!
            self.logger.warning("exception while calling user callback: %s", ex)


    def create_monitored_items(self, params):
        self.logger.info("create_monitored_items")
        request = ua.CreateMonitoredItemsRequest()
        request.Parameters = params
        data = self._send_request(request)
        response = ua.CreateMonitoredItemsResponse.from_binary(data)
        response.ResponseHeader.ServiceResult.check()
        return response.Results

    def delete_monitored_items(self, params):
        self.logger.info("delete_monitored_items")
        request = ua.DeleteMonitoredItemsRequest()
        request.Parameters = params
        data = self._send_request(request)
        response = ua.DeleteMonitoredItemsResponse.from_binary(data)
        response.ResponseHeader.ServiceResult.check()
        return response.Results



    def add_nodes(self, nodestoadd):
        self.logger.info("add_nodes")
        request = ua.AddNodesRequest()
        request.Parameters.NodesToAdd = nodestoadd
        data = self._send_request(request)
        response = ua.AddNodesResponse.from_binary(data)
        response.ResponseHeader.ServiceResult.check()
        return response.Results



