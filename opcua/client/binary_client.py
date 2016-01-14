"""
Low level binary client
"""

import logging
import threading
from concurrent.futures import Future
from functools import partial
try:
    # we prefer to use bundles asyncio version, otherwise fallback to trollius
    import asyncio
except ImportError:
    import trollius as asyncio

from opcua import ua
from opcua.common import utils


class UAClientProtocol(asyncio.Protocol):
    def __init__(self, security_connection, disconnected_cb):
        asyncio.Protocol.__init__(self)
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
            if not fut.done():
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
        # TODO: call pause/resume enable flow control
        self._buffer.write(data)
        self._process_msg()

    def _process_msg(self):
        try:
            while True:
                hdr = self._get_header()
                if hdr is None or len(self._buffer) < hdr.body_size:
                    return
                # entire packet recieved, clear curent header and process it
                self._cur_header = None
                self._process_one_packet(hdr)
        except Exception as e:
            self.close(e)

    def _process_one_packet(self, hdr):
            msg = self._connection.receive_from_header_and_body(hdr, self._buffer)
            if msg is None:
                # wait for more chunk
                return
            elif isinstance(msg, ua.Message):
                self._set_result(msg.request_id(), msg.body())
            elif isinstance(msg, ua.Acknowledge):
                self._set_result(0, msg)
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

    def set_authentication_token(self, token):
        self.authentication_token = token

    def send_request(self, request, timeout_hint, fut):
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
            binreq = self._to_binreq(request, timeout_hint)
            self._request_id += 1
            reqid = self._request_id
            msg = self._connection.message_to_binary(binreq, msgtype, reqid)
        self.transport.write(msg)
        self.futuremap[reqid] = fut

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


class BinaryClient(object):

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
        self._loop_ready = False
        self._proto_connected = False

    def _start_loop(self, host, port):
        fut = Future()
        try:
            self._loop = asyncio.new_event_loop()
            self._thread = threading.Thread(target=self._loop_run, args=(host, port, fut))
            self._thread.daemon = True
            self._thread.start()
        except:
            self._loop = None
            self._thread = None
            raise
        fut.result()
        self._loop_ready = True
        self._proto_connected = True

    def _loop_run(self, host, port, fut):
        self.logger.info("start client thread")
        try:
            coro = self._loop.create_connection(lambda: self._proto, host, port)
            self._loop.run_until_complete(coro)
        except Exception as e:
            self._loop.close()
            fut.set_exception(e)
            self.logger.info("stop client thread")
            return
        fut.set_result(None)
        self._loop.run_forever()
        self._proto.close()
        self._loop.close()
        self.logger.info("stop client thread")

    def _stop_loop(self):
        if self._loop_ready:
            self._loop.call_soon_threadsafe(self._loop.stop)
            self._thread.join()
            self._loop_ready = False
            self._loop = None
            self._thread = None

    def _in_loop_thread(self):
        return self._thread.ident == threading.current_thread().ident

    def set_security(self, policy):
        self._security_policy = policy

    def connect_socket(self, host, port):
        """
        connect to server socket and start receiving thread
        """
        self._connection = ua.SecureConnection(self._security_policy)
        self._proto = UAClientProtocol(self._connection, self._disconn_cb)
        self._start_loop(host, port)

    def _disconn_cb(self, ex):
        self._proto_connected = False

    def disconnect_socket(self):
        self._stop_loop()
        self._proto = None
        self._connection = None
        self._publishcallbacks.clear()

    def _check_answer(self, data):
        if not isinstance(data, utils.Buffer):
            # may be an ack etc...
            return
        data = data.copy()
        typeid = ua.NodeId.from_binary(data)
        if typeid == ua.FourByteNodeId(ua.ObjectIds.ServiceFault_Encoding_DefaultBinary):
            self.logger.warning("ServiceFault from server received")
            hdr = ua.ResponseHeader.from_binary(data)
            hdr.ServiceResult.check()

    def _on_response_data(self, fut, on_response, data_fut):
        if data_fut.cancelled():
            fut.cancel()
            return
        ex = data_fut.exception()
        if ex is not None:
            fut.set_exception(ex)
            return
        try:
            data = data_fut.result()
            self._check_answer(data)
            rs = on_response(data)
        except Exception as e:
            fut.set_exception(e)
            return
        fut.set_result(rs)

    def _loop_send(self, new_request, on_response, fut):
        try:
            req = new_request()
            data_fut = asyncio.Future(loop=self._loop)
            data_fut.add_done_callback(partial(self._on_response_data, fut, on_response))
            self.logger.info("sending %s", req.__class__.__name__)
            self._proto.send_request(req, int(self._timeout * 1000), data_fut)
        except Exception as e:
            fut.set_exception(e)

    def _send_request(self, new_request, on_response):
        if not self._proto_connected:
            raise ua.UAError("client is disconnected")
        if self._in_loop_thread():
            raise ua.UAError("can not send reqeust in client loop thread")
        fut = Future()
        self._loop.call_soon_threadsafe(self._loop_send, new_request, on_response, fut)
        return fut.result(self._timeout)

    def _loop_call(self, fut, func, *args, **kwargs):
        try:
            ret = func(*args, **kwargs)
        except Exception as e:
            fut.set_exception(e)
        fut.set_result(ret)

    def _async_call(self, func, *args, **kwargs):
        if self._in_loop_thread():
            return func(*args, **kwargs)
        fut = Future()
        self._loop.call_soon_threadsafe(partial(self._loop_call, fut, func, *args, **kwargs))
        return fut.result(self._timeout)

    def send_hello(self, url):
        def new_req():
            hello = ua.Hello()
            hello.EndpointUrl = url
            return hello

        return self._send_request(new_req, lambda x: x)

    def open_secure_channel(self, params):
        def new_req():
            request = ua.OpenSecureChannelRequest()
            request.Parameters = params
            return request

        def on_resp(data):
            response = ua.OpenSecureChannelResponse.from_binary(data)
            response.ResponseHeader.ServiceResult.check()
            self._connection.set_security_token(response.Parameters.SecurityToken)
            return response.Parameters

        return self._send_request(new_req, on_resp)

    def close_secure_channel(self):
        """
        close secure channel. It seems to trigger a shutdown of socket
        in most servers, so be prepare to reconnect.
        OPC UA specs Part 6, 7.1.4 say that Server does not send a CloseSecureChannel response
        and should just close socket
        """
        try:
            self._send_request(ua.CloseSecureChannelRequest, lambda x: x)
        except asyncio.CancelledError:
            # some servers send a response here, most do not ... so we ignore
            pass

    def create_session(self, parameters):
        def new_req():
            request = ua.CreateSessionRequest()
            request.Parameters = parameters
            return request

        def on_resp(data):
            response = ua.CreateSessionResponse.from_binary(data)
            response.ResponseHeader.ServiceResult.check()
            self._proto.set_authentication_token(response.Parameters.AuthenticationToken)
            return response.Parameters

        return self._send_request(new_req, on_resp)

    def activate_session(self, parameters):
        def new_req():
            request = ua.ActivateSessionRequest()
            request.Parameters = parameters
            return request

        def on_resp(data):
            response = ua.ActivateSessionResponse.from_binary(data)
            response.ResponseHeader.ServiceResult.check()
            return response.Parameters

        return self._send_request(new_req, on_resp)

    def close_session(self, deletesubscriptions):
        def new_req():
            request = ua.CloseSessionRequest()
            request.DeleteSubscriptions = deletesubscriptions
            return request

        def on_resp(data):
            ua.CloseSessionResponse.from_binary(data)
            # disabled, it seems we sent wrong session Id,
            # but where is the sessionId supposed to be sent???
            # response.ResponseHeader.ServiceResult.check()

        self._send_request(new_req, on_resp)

    def browse(self, parameters):
        def new_req():
            request = ua.BrowseRequest()
            request.Parameters = parameters
            return request

        def on_resp(data):
            response = ua.BrowseResponse.from_binary(data)
            response.ResponseHeader.ServiceResult.check()
            return response.Results

        return self._send_request(new_req, on_resp)

    def read(self, parameters):
        def new_req():
            request = ua.ReadRequest()
            request.Parameters = parameters
            return request

        def on_resp(data):
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
            return response.Results

        return self._send_request(new_req, on_resp)

    def write(self, params):
        def new_req():
            request = ua.WriteRequest()
            request.Parameters = params
            return request

        def on_resp(data):
            response = ua.WriteResponse.from_binary(data)
            response.ResponseHeader.ServiceResult.check()
            return response.Results

        return self._send_request(new_req, on_resp)

    def get_endpoints(self, params):
        def new_req():
            request = ua.GetEndpointsRequest()
            request.Parameters = params
            return request

        def on_resp(data):
            response = ua.GetEndpointsResponse.from_binary(data)
            response.ResponseHeader.ServiceResult.check()
            return response.Endpoints

        return self._send_request(new_req, on_resp)

    def find_servers(self, params):
        def new_req():
            request = ua.FindServersRequest()
            request.Parameters = params
            return request

        def on_resp(data):
            response = ua.FindServersResponse.from_binary(data)
            response.ResponseHeader.ServiceResult.check()
            return response.Servers

        return self._send_request(new_req, on_resp)

    def find_servers_on_network(self, params):
        def new_req():
            request = ua.FindServersOnNetworkRequest()
            request.Parameters = params
            return request

        def on_resp(data):
            response = ua.FindServersOnNetworkResponse.from_binary(data)
            response.ResponseHeader.ServiceResult.check()
            return response.Parameters

        return self._send_request(new_req, on_resp)

    def register_server(self, registered_server):
        def new_req():
            request = ua.RegisterServerRequest()
            request.Server = registered_server
            return request

        def on_resp(data):
            response = ua.RegisterServerResponse.from_binary(data)
            response.ResponseHeader.ServiceResult.check()

        self._send_request(new_req, on_resp)

    def register_server2(self, params):
        def new_req():
            request = ua.RegisterServer2Request()
            request.Parameters = params
            return request

        def on_resp(data):
            response = ua.RegisterServer2Response.from_binary(data)
            response.ResponseHeader.ServiceResult.check()
            return response.ConfigurationResults

        return self._send_request(new_req, on_resp)

    def translate_browsepaths_to_nodeids(self, browsepaths):
        def new_req():
            request = ua.TranslateBrowsePathsToNodeIdsRequest()
            request.Parameters.BrowsePaths = browsepaths
            return request

        def on_resp(data):
            response = ua.TranslateBrowsePathsToNodeIdsResponse.from_binary(data)
            response.ResponseHeader.ServiceResult.check()
            return response.Results

        return self._send_request(new_req, on_resp)

    def create_subscription(self, params, callback):
        def new_req():
            request = ua.CreateSubscriptionRequest()
            request.Parameters = params
            return request

        def on_resp(data):
            response = ua.CreateSubscriptionResponse.from_binary(data)
            response.ResponseHeader.ServiceResult.check()
            self._publishcallbacks[response.Parameters.SubscriptionId] = callback
            return response.Parameters

        return self._send_request(new_req, on_resp)

    def delete_subscriptions(self, subscriptionids):
        def new_req():
            request = ua.DeleteSubscriptionsRequest()
            request.Parameters.SubscriptionIds = subscriptionids
            return request

        def on_resp(data):
            response = ua.DeleteSubscriptionsResponse.from_binary(data)
            response.ResponseHeader.ServiceResult.check()
            for sid in subscriptionids:
                self._publishcallbacks.pop(sid)
            return response.Results

        return self._send_request(new_req, on_resp)

    def _loop_publish(self, acks):
        self.logger.info("sending PublishRequest")
        request = ua.PublishRequest()
        request.Parameters.SubscriptionAcknowledgements = acks
        data_fut = asyncio.Future(loop=self._loop)
        data_fut.add_done_callback(self._call_publish_callback)
        self._proto.send_request(request, int(9e8), data_fut)

    def publish(self, acks=None):
        if not self._proto_connected:
            raise ua.UAError("client is disconnected")
        if acks is None:
            acks = []
        return self._async_call(self._loop_publish, acks)

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

    def create_monitored_items(self, params):
        def new_req():
            request = ua.CreateMonitoredItemsRequest()
            request.Parameters = params
            return request

        def on_resp(data):
            response = ua.CreateMonitoredItemsResponse.from_binary(data)
            response.ResponseHeader.ServiceResult.check()
            return response.Results

        return self._send_request(new_req, on_resp)

    def delete_monitored_items(self, params):
        def new_req():
            request = ua.DeleteMonitoredItemsRequest()
            request.Parameters = params
            return request

        def on_resp(data):
            response = ua.DeleteMonitoredItemsResponse.from_binary(data)
            response.ResponseHeader.ServiceResult.check()
            return response.Results

        return self._send_request(new_req, on_resp)

    def add_nodes(self, nodestoadd):
        def new_req():
            request = ua.AddNodesRequest()
            request.Parameters.NodesToAdd = nodestoadd
            return request

        def on_resp(data):
            response = ua.AddNodesResponse.from_binary(data)
            response.ResponseHeader.ServiceResult.check()
            return response.Results

        return self._send_request(new_req, on_resp)

    def delete_nodes(self, nodestodelete):
        def new_req():
            request = ua.DeleteNodesRequest()
            request.Parameters.NodesToDelete = nodestodelete
            return request

        def on_resp(data):
            response = ua.AddNodesResponse.from_binary(data)
            response.ResponseHeader.ServiceResult.check()
            return response.Results

        return self._send_request(new_req, on_resp)

    def call(self, methodstocall):
        def new_req():
            request = ua.CallRequest()
            request.Parameters.MethodsToCall = methodstocall
            return request

        def on_resp(data):
            response = ua.CallResponse.from_binary(data)
            response.ResponseHeader.ServiceResult.check()
            return response.Results

        return self._send_request(new_req, on_resp)

    def history_read(self, params):
        def new_req():
            request = ua.HistoryReadRequest()
            request.Parameters = params
            return request

        def on_resp(data):
            response = ua.HistoryReadResponse.from_binary(data)
            response.ResponseHeader.ServiceResult.check()
            return response.Results

        return self._send_request(new_req, on_resp)
