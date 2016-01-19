"""
Low level binary client
"""

import logging
from functools import partial
from opcua.common import uaasync
from opcua.common.uaasync import coroutine, From, Return, await_super_coro
from opcua import ua
from opcua.common import utils


def _cancel_handle_cb(hdl, _):
    hdl.cancel()


class UAClientProtocol(uaasync.asyncio.Protocol):
    def __init__(self, security_connection, disconnected_cb):
        uaasync.asyncio.Protocol.__init__(self)
        self.logger = logging.getLogger(__name__ + "Protocol")
        self.authentication_token = ua.NodeId()
        self._connection = security_connection
        self.disconnected_cb = disconnected_cb
        self.transport = None
        self.futuremap = {}
        self._buffer = utils.Buffer(b"")
        self._request_id = 0
        self._request_handle = 0
        self._cur_header = None

    def connection_made(self, transport):
        self.logger.info("connect to server")
        self.transport = transport

    def connection_lost(self, ex):
        self.logger.info("connection lost")
        self.close(ex)

    def close(self, ex=None):
        for k in self.futuremap:
            # cancel all waiting response callback
            fut = self.futuremap[k]
            if fut is not None and not fut.done():
                if ex is None:
                    fut.cancel()
                else:
                    fut.set_exception(ex)
        self.futuremap.clear()
        if self.transport is not None:
            self.disconnected_cb(ex)
            self.transport.close()
            self.transport = None

    def data_received(self, data):
        self._buffer.write(data)
        self.transport.pause_reading()
        self._process_msg()

    def _process_msg(self):
        try:
            msgnum = 0
            while True:
                hdr = self._get_header()
                if hdr is None or len(self._buffer) < hdr.body_size:
                    self.transport.resume_reading()
                    return
                # entire packet recieved, clear curent header and process it
                self._cur_header = None
                msgnum += self._process_one_packet(hdr)
                if msgnum >= 1:
                    # yield cpu for packet processing
                    uaasync.call_soon(self._process_msg)
                    return
        except Exception as e:
            self.close(e)

    def _process_one_packet(self, hdr):
            msg = self._connection.receive_from_header_and_body(hdr, self._buffer)
            if msg is None:
                # wait for more chunk
                return 0
            elif isinstance(msg, ua.Message):
                self._set_result(msg.request_id(), msg.body())
                return 1
            elif isinstance(msg, ua.Acknowledge):
                self._set_result(0, msg)
                return 1
            elif isinstance(msg, ua.ErrorMessage):
                raise ua.UAError("Received an error: {}".format(msg))
            else:
                raise ua.UAError("Unsupported message type: {}".format(msg))

    def _get_header(self):
        if self._cur_header is not None:
            return self._cur_header
        buf = self._buffer
        if len(buf) < 8:
            # a UA Header is at least 8 bytes, wait for more
            return None
        try:
            header = ua.Header.from_string(buf)
        except ua.NotEnoughData:
            # not enougth data for header, wait for more
            return None
        self._cur_header = header
        return header

    def _set_result(self, reqid, body):
        if reqid not in self.futuremap:
            raise ua.UAError(
                "No future found for request: {}, futures in list are {}".format(
                    reqid, self.futuremap.keys()))
        fut = self.futuremap.pop(reqid)
        if fut is not None and not fut.done():
            fut.set_result(body)

    def _timeout_request(self, name, reqid):
        if reqid in self.futuremap:
            fut = self.futuremap[reqid]
            # keep the slot, in case a response is return in future
            self.futuremap[reqid] = None
            if fut is not None and not fut.done():
                fut.set_exception(uaasync.asyncio.TimeoutError("%s id %d timeout" % (name, reqid)))

    def set_authentication_token(self, token):
        self.authentication_token = token

    def send_request(self, request, timeout):
        if isinstance(request, ua.Hello):
            msg = self._connection.tcp_to_binary(ua.MessageType.Hello, request)
            reqid = 0
        else:
            if isinstance(request, ua.OpenSecureChannelRequest):
                msgtype = ua.MessageType.SecureOpen
            elif isinstance(request, ua.CloseSecureChannelRequest):
                msgtype = ua.MessageType.SecureClose
            else:
                msgtype = ua.MessageType.SecureMessage
            timeout_hint = int(timeout * 1000)
            binreq = self._to_binreq(request, timeout_hint)
            self._request_id += 1
            reqid = self._request_id
            msg = self._connection.message_to_binary(binreq, msgtype, reqid)
        self.transport.write(msg)
        fut = uaasync.new_future()
        self.futuremap[reqid] = fut
        handle = uaasync.call_later(timeout * 1.1, self._timeout_request, request.__class__.__name__, reqid)
        fut.add_done_callback(partial(_cancel_handle_cb, handle))
        return fut

    def _to_binreq(self, request, timeout_hint):
        hdr = ua.RequestHeader()
        hdr.AuthenticationToken = self.authentication_token
        self._request_handle += 1
        hdr.RequestHandle = self._request_handle
        hdr.TimeoutHint = timeout_hint
        request.RequestHeader = hdr
        try:
            binreq = request.to_binary()
        except:
            # reset reqeust handle if any error
            self._request_handle -= 1
            raise
        return binreq


class AsyncBinaryClient(object):

    """
    low level OPC-UA client.
    implement all(well..one day) methods defined in opcua spec
    taking in argument the structures defined in opcua spec
    in python most of the structures are defined in
    uaprotocol_auto.py and uaprotocol_hand.py
    """

    def __init__(self, timeout=1):
        self.logger = logging.getLogger(__name__)
        self._publishcallbacks = {}
        self._timeout = timeout
        self._security_policy = ua.SecurityPolicy()
        self._proto_connected = False

    def set_security(self, policy):
        self._security_policy = policy

    @coroutine
    def connect_socket(self, host, port):
        """
        connect to server socket and start receiving thread
        """
        self.logger.info("connect_socket %s %d", host, port)
        self._connection = ua.SecureConnection(self._security_policy)
        self._proto = UAClientProtocol(self._connection, self._disconn_cb)
        loop = uaasync.get_loop()
        coro = loop.create_connection(lambda: self._proto, host, port)
        yield From(coro)
        self._proto_connected = True

    def _disconn_cb(self, ex):
        self._proto_connected = False

    def disconnect_socket(self):
        self._proto.close()
        self._proto = None
        self._connection = None
        self._publishcallbacks.clear()

    def _check_answer(self, data, context=None):
        if not isinstance(data, utils.Buffer):
            # may be an ack etc...
            return
        data = data.copy()
        typeid = ua.NodeId.from_binary(data)
        if typeid == ua.FourByteNodeId(ua.ObjectIds.ServiceFault_Encoding_DefaultBinary):
            if context is None:
                self.logger.warning("ServiceFault from server received")
            else:
                self.logger.warning("ServiceFault from server received in response to %s", context)
            hdr = ua.ResponseHeader.from_binary(data)
            hdr.ServiceResult.check()

    @coroutine
    def _send_request(self, request):
        if not self._proto_connected:
            raise ua.UAError("client is disconnected")
        reqname = request.__class__.__name__
        self.logger.info("sending %s", reqname)
        fut = self._proto.send_request(request, self._timeout)
        data = yield From(fut)
        # data = yield From(uaasync.wait_for(fut, self._timeout * 1.1))
        self._check_answer(data, reqname)
        raise Return(data)

    def send_request(self, request):
        return self._send_request(request)

    @coroutine
    def send_hello(self, url):
        hello = ua.Hello()
        hello.EndpointUrl = url
        ack = yield From(self._send_request(hello))
        raise Return(ack)

    @coroutine
    def open_secure_channel(self, params):
        request = ua.OpenSecureChannelRequest()
        request.Parameters = params
        data = yield From(self._send_request(request))
        response = ua.OpenSecureChannelResponse.from_binary(data)
        response.ResponseHeader.ServiceResult.check()
        self._connection.set_security_token(response.Parameters.SecurityToken)
        raise Return(response.Parameters)

    @coroutine
    def close_secure_channel(self):
        """
        close secure channel. It seems to trigger a shutdown of socket
        in most servers, so be prepare to reconnect.
        OPC UA specs Part 6, 7.1.4 say that Server does not send a CloseSecureChannel response
        and should just close socket
        """
        reqeust = ua.CloseSecureChannelRequest()
        try:
            yield From(self._send_request(reqeust))
        except uaasync.asyncio.CancelledError:
            # some servers send a response here, most do not ... so we ignore
            pass

    @coroutine
    def create_session(self, parameters):
        request = ua.CreateSessionRequest()
        request.Parameters = parameters
        data = yield From(self._send_request(request))
        response = ua.CreateSessionResponse.from_binary(data)
        response.ResponseHeader.ServiceResult.check()
        self._proto.set_authentication_token(response.Parameters.AuthenticationToken)
        raise Return(response.Parameters)

    @coroutine
    def activate_session(self, parameters):
        request = ua.ActivateSessionRequest()
        request.Parameters = parameters
        data = yield From(self._send_request(request))
        response = ua.ActivateSessionResponse.from_binary(data)
        response.ResponseHeader.ServiceResult.check()
        raise Return(response.Parameters)

    @coroutine
    def close_session(self, deletesubscriptions):
        request = ua.CloseSessionRequest()
        request.DeleteSubscriptions = deletesubscriptions
        data = yield From(self._send_request(request))
        ua.CloseSessionResponse.from_binary(data)
        # disabled, it seems we sent wrong session Id,
        # but where is the sessionId supposed to be sent???
        # response.ResponseHeader.ServiceResult.check()

    @coroutine
    def browse(self, parameters):
        request = ua.BrowseRequest()
        request.Parameters = parameters
        data = yield From(self._send_request(request))
        response = ua.BrowseResponse.from_binary(data)
        response.ResponseHeader.ServiceResult.check()
        raise Return(response.Results)

    @coroutine
    def read(self, parameters):
        request = ua.ReadRequest()
        request.Parameters = parameters
        data = yield From(self._send_request(request))
        response = ua.ReadResponse.from_binary(data)
        response.ResponseHeader.ServiceResult.check()
        # cast to Enum attributes that need to
        for idx, rv in enumerate(parameters.NodesToRead):
            if rv.AttributeId == ua.AttributeIds.NodeClass:
                dv = response.Results[idx]
                if dv.StatusCode.is_good():
                    dv.Value.Value = ua.NodeClass(dv.Value.Value)
            elif rv.AttributeId == ua.AttributeIds.ValueRank:
                dv = response.Results[idx]
                if dv.StatusCode.is_good() and dv.Value.Value in (-3, -2, -1, 0, 1, 2, 3, 4):
                    dv.Value.Value = ua.ValueRank(dv.Value.Value)
        raise Return(response.Results)

    @coroutine
    def write(self, params):
        request = ua.WriteRequest()
        request.Parameters = params
        data = yield From(self._send_request(request))
        response = ua.WriteResponse.from_binary(data)
        response.ResponseHeader.ServiceResult.check()
        raise Return(response.Results)

    @coroutine
    def get_endpoints(self, params):
        request = ua.GetEndpointsRequest()
        request.Parameters = params
        data = yield From(self._send_request(request))
        response = ua.GetEndpointsResponse.from_binary(data)
        response.ResponseHeader.ServiceResult.check()
        raise Return(response.Endpoints)

    @coroutine
    def find_servers(self, params):
        request = ua.FindServersRequest()
        request.Parameters = params
        data = yield From(self._send_request(request))
        response = ua.FindServersResponse.from_binary(data)
        response.ResponseHeader.ServiceResult.check()
        raise Return(response.Servers)

    @coroutine
    def find_servers_on_network(self, params):
        request = ua.FindServersOnNetworkRequest()
        request.Parameters = params
        data = yield From(self._send_request(request))
        response = ua.FindServersOnNetworkResponse.from_binary(data)
        response.ResponseHeader.ServiceResult.check()
        raise Return(response.Parameters)

    @coroutine
    def register_server(self, registered_server):
        request = ua.RegisterServerRequest()
        request.Server = registered_server
        data = yield From(self._send_request(request))
        response = ua.RegisterServerResponse.from_binary(data)
        response.ResponseHeader.ServiceResult.check()

    @coroutine
    def register_server2(self, params):
        request = ua.RegisterServer2Request()
        request.Parameters = params
        data = yield From(self._send_request(request))
        response = ua.RegisterServer2Response.from_binary(data)
        response.ResponseHeader.ServiceResult.check()
        raise Return(response.ConfigurationResults)

    @coroutine
    def translate_browsepaths_to_nodeids(self, browsepaths):
        request = ua.TranslateBrowsePathsToNodeIdsRequest()
        request.Parameters.BrowsePaths = browsepaths
        data = yield From(self._send_request(request))
        response = ua.TranslateBrowsePathsToNodeIdsResponse.from_binary(data)
        response.ResponseHeader.ServiceResult.check()
        raise Return(response.Results)

    @coroutine
    def create_subscription(self, params, callback):
        request = ua.CreateSubscriptionRequest()
        request.Parameters = params
        data = yield From(self._send_request(request))
        response = ua.CreateSubscriptionResponse.from_binary(data)
        response.ResponseHeader.ServiceResult.check()
        self._publishcallbacks[response.Parameters.SubscriptionId] = callback
        raise Return(response.Parameters)

    @coroutine
    def delete_subscriptions(self, subscriptionids):
        request = ua.DeleteSubscriptionsRequest()
        request.Parameters.SubscriptionIds = subscriptionids
        data = yield From(self._send_request(request))
        response = ua.DeleteSubscriptionsResponse.from_binary(data)
        response.ResponseHeader.ServiceResult.check()
        for sid in subscriptionids:
            self._publishcallbacks.pop(sid)
        raise Return(response.Results)

    def publish(self, acks=None):
        if not self._proto_connected:
            raise ua.UAError("client is disconnected")
        if acks is None:
            acks = []
        self.logger.info("sending PublishRequest")
        request = ua.PublishRequest()
        request.Parameters.SubscriptionAcknowledgements = acks
        fut = self._proto.send_request(request, int(9e5))
        fut.add_done_callback(self._call_publish_callback)

    def _call_publish_callback(self, data_fut):
        self.logger.info("call_publish_callback")
        if data_fut.cancelled():
            return
        ex = data_fut.exception()
        if ex is not None:
            self.logger.warning("call_publish_callback got exception %s", repr(ex))
            return
        data = data_fut.result()
        self._check_answer(data)
        response = ua.PublishResponse.from_binary(data)
        if response.Parameters.SubscriptionId not in self._publishcallbacks:
            self.logger.warning("Received data for unknown subscription: %s ", response.Parameters.SubscriptionId)
            return
        callback = self._publishcallbacks[response.Parameters.SubscriptionId]
        try:
            callback(response.Parameters)
        except Exception:  # we call client code, catch everything!
            self.logger.exception("Exception while calling user callback")

    @coroutine
    def create_monitored_items(self, params):
        request = ua.CreateMonitoredItemsRequest()
        request.Parameters = params
        data = yield From(self._send_request(request))
        response = ua.CreateMonitoredItemsResponse.from_binary(data)
        response.ResponseHeader.ServiceResult.check()
        raise Return(response.Results)

    @coroutine
    def delete_monitored_items(self, params):
        request = ua.DeleteMonitoredItemsRequest()
        request.Parameters = params
        data = yield From(self._send_request(request))
        response = ua.DeleteMonitoredItemsResponse.from_binary(data)
        response.ResponseHeader.ServiceResult.check()
        raise Return(response.Results)

    @coroutine
    def add_nodes(self, nodestoadd):
        request = ua.AddNodesRequest()
        request.Parameters.NodesToAdd = nodestoadd
        data = yield From(self._send_request(request))
        response = ua.AddNodesResponse.from_binary(data)
        response.ResponseHeader.ServiceResult.check()
        raise Return(response.Results)

    @coroutine
    def delete_nodes(self, nodestodelete):
        request = ua.DeleteNodesRequest()
        request.Parameters.NodesToDelete = nodestodelete
        data = yield From(self._send_request(request))
        response = ua.AddNodesResponse.from_binary(data)
        response.ResponseHeader.ServiceResult.check()
        raise Return(response.Results)

    @coroutine
    def call(self, methodstocall):
        request = ua.CallRequest()
        request.Parameters.MethodsToCall = methodstocall
        data = yield From(self._send_request(request))
        response = ua.CallResponse.from_binary(data)
        response.ResponseHeader.ServiceResult.check()
        raise Return(response.Results)

    @coroutine
    def history_read(self, params):
        request = ua.HistoryReadRequest()
        request.Parameters = params
        data = yield From(self._send_request(request))
        response = ua.HistoryReadResponse.from_binary(data)
        response.ResponseHeader.ServiceResult.check()
        raise Return(response.Results)


class BinaryClient(AsyncBinaryClient):
    def connect_socket(self, host, port):
        uaasync.start_loop()
        uaasync.await_coro(AsyncBinaryClient.connect_socket, self, host, port)

    def disconnect_socket(self):
        uaasync.await_call(AsyncBinaryClient.disconnect_socket, self)
        uaasync.stop_loop()

    @await_super_coro
    def send_request(self, request):
        pass

    @await_super_coro
    def send_hello(self, url):
        pass

    @await_super_coro
    def open_secure_channel(self, params):
        pass

    @await_super_coro
    def close_secure_channel(self):
        pass

    @await_super_coro
    def create_session(self, parameters):
        pass

    @await_super_coro
    def activate_session(self, parameters):
        pass

    @await_super_coro
    def close_session(self, deletesubscriptions):
        pass

    @await_super_coro
    def browse(self, parameters):
        pass

    @await_super_coro
    def read(self, parameters):
        pass

    @await_super_coro
    def write(self, params):
        pass

    @await_super_coro
    def get_endpoints(self, params):
        pass

    @await_super_coro
    def find_servers(self, params):
        pass

    @await_super_coro
    def find_servers_on_network(self, params):
        pass

    @await_super_coro
    def register_server(self, registered_server):
        pass

    @await_super_coro
    def register_server2(self, params):
        pass

    @await_super_coro
    def translate_browsepaths_to_nodeids(self, browsepaths):
        pass

    @await_super_coro
    def create_subscription(self, params, callback):
        pass

    @await_super_coro
    def delete_subscriptions(self, subscriptionids):
        pass

    @uaasync.await_super_call
    def publish(self, acks=None):
        pass

    @await_super_coro
    def create_monitored_items(self, params):
        pass

    @await_super_coro
    def delete_monitored_items(self, params):
        pass

    @await_super_coro
    def add_nodes(self, nodestoadd):
        pass

    @await_super_coro
    def delete_nodes(self, nodestodelete):
        pass

    @await_super_coro
    def call(self, methodstocall):
        pass

    @await_super_coro
    def history_read(self, params):
        pass
