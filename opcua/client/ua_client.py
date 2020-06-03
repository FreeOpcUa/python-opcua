"""
Low level binary client
"""

import logging
import socket
import errno
from threading import Thread, Lock
from concurrent.futures import Future, CancelledError
from functools import partial

from opcua import ua
from opcua.ua.ua_binary import struct_from_binary, uatcp_to_binary, struct_to_binary, nodeid_from_binary
from opcua.ua.uaerrors import UaError, BadTimeout, BadNoSubscription, BadSessionClosed
from opcua.common.connection import SecureConnection


class UASocketClient(object):
    """
    handle socket connection and send ua messages
    timeout is the timeout used while waiting for an ua answer from server
    """
    def __init__(self, timeout=1, security_policy=ua.SecurityPolicy()):
        self.logger = logging.getLogger(__name__ + ".Socket")
        self._thread = None
        self._lock = Lock()
        self.timeout = timeout
        self._socket = None
        self._do_stop = False
        self.authentication_token = ua.NodeId()
        self._request_id = 0
        self._request_handle = 0
        self._callbackmap = {}
        self._connection = SecureConnection(security_policy)

    def start(self):
        """
        Start receiving thread.
        this is called automatically in connect and
        should not be necessary to call directly
        """
        self._thread = Thread(target=self._run)
        self._thread.start()

    def _send_request(self, request, callback=None, timeout=1000, message_type=ua.MessageType.SecureMessage):
        """
        send request to server, lower-level method
        timeout is the timeout written in ua header
        returns future
        """
        with self._lock:
            request.RequestHeader = self._create_request_header(timeout)
            self.logger.debug("Sending: %s", request)
            try:
                binreq = struct_to_binary(request)
            except Exception:
                # reset reqeust handle if any error
                # see self._create_request_header
                self._request_handle -= 1
                raise
            self._request_id += 1
            future = Future()
            if callback:
                future.add_done_callback(callback)
            self._callbackmap[self._request_id] = future

            # Change to the new security token if the connection has been renewed.
            if self._connection.next_security_token.TokenId != 0:
                self._connection.revolve_tokens()

            msg = self._connection.message_to_binary(binreq, message_type=message_type, request_id=self._request_id)
            self._socket.write(msg)
        return future

    def send_request(self, request, callback=None, timeout=1000, message_type=ua.MessageType.SecureMessage):
        """
        send request to server.
        timeout is the timeout written in ua header
        returns response object if no callback is provided
        """
        future = self._send_request(request, callback, timeout, message_type)
        if not callback:
            data = future.result(self.timeout)
            self.check_answer(data, " in response to " + request.__class__.__name__)
            return data

    def check_answer(self, data, context):
        data = data.copy()
        typeid = nodeid_from_binary(data)
        if typeid == ua.FourByteNodeId(ua.ObjectIds.ServiceFault_Encoding_DefaultBinary):
            self.logger.warning("ServiceFault from server received %s", context)
            hdr = struct_from_binary(ua.ResponseHeader, data)
            hdr.ServiceResult.check()
            return False
        return True

    def _run(self):
        self.logger.info("Thread started")
        while not self._do_stop:
            try:
                self._receive()
            except ua.utils.SocketClosedException:
                self.logger.info("Socket has closed connection")
                self._connection.close()
                break
            except UaError:
                self.logger.exception("Protocol Error")
        self._cancel_all_callbacks()
        self.logger.info("Thread ended")

    def _receive(self):
        msg = self._connection.receive_from_socket(self._socket)
        if msg is None:
            return
        if isinstance(msg, ua.Message):
            self._call_callback(msg.request_id(), msg.body())
        elif isinstance(msg, ua.Acknowledge):
            self._call_callback(0, msg)
        elif isinstance(msg, ua.ErrorMessage):
            self.logger.fatal("Received an error: %s", msg)
            self._call_callback(0, ua.UaStatusCodeError(msg.Error.value))
        else:
            raise ua.UaError("Unsupported message type: {}".format(msg))

    def _call_callback(self, request_id, body):
        with self._lock:
            future = self._callbackmap.pop(request_id, None)
            if future is None:
                raise ua.UaError(
                    "No future object found for request: {0}, callbacks in list are {1}"
                    .format(request_id, self._callbackmap.keys())
                )
        future.set_result(body)

    def _cancel_all_callbacks(self):
        for request_id, fut in self._callbackmap.items():
            self.logger.info("Cancelling request {:d}".format(request_id))
            fut.cancel()
        self._callbackmap.clear()

    def _create_request_header(self, timeout=1000):
        hdr = ua.RequestHeader()
        hdr.AuthenticationToken = self.authentication_token
        self._request_handle += 1
        hdr.RequestHandle = self._request_handle
        hdr.TimeoutHint = timeout
        return hdr

    def connect_socket(self, host, port):
        """
        connect to server socket and start receiving thread
        """
        self.logger.info("opening connection")
        # Create socket with timeout for initial connection
        sock = socket.create_connection((host, port), timeout=self.timeout)
        # set to blocking mode again
        sock.settimeout(None)
        # nodelay necessary to avoid packing in one frame, some servers do not like it
        sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        self._socket = ua.utils.SocketWrapper(sock)
        self.start()

    def disconnect_socket(self):
        self.logger.info("Request to close socket received")
        self._do_stop = True
        try:
            self._socket.socket.shutdown(socket.SHUT_RDWR)
        except (socket.error, OSError) as exc:
            if exc.errno in (errno.ENOTCONN, errno.EBADF):
                pass # Socket is not connected, so can't send FIN packet.
            else:
                raise
        self._socket.socket.close()
        self.logger.info("Socket closed, waiting for receiver thread to terminate...")
        if self._thread and self._thread.is_alive():
            self._thread.join()
        self._cancel_all_callbacks()
        self.logger.info("Done closing socket: Receiving thread terminated, socket disconnected")

    def send_hello(self, url, max_messagesize=0, max_chunkcount=0):
        hello = ua.Hello()
        hello.EndpointUrl = url
        hello.MaxMessageSize = max_messagesize
        hello.MaxChunkCount = max_chunkcount
        future = Future()
        with self._lock:
            self._callbackmap[0] = future
        binmsg = uatcp_to_binary(ua.MessageType.Hello, hello)
        self._socket.write(binmsg)
        ack = future.result(self.timeout)
        return ack

    def open_secure_channel(self, params):
        self.logger.info("open_secure_channel")
        request = ua.OpenSecureChannelRequest()
        request.Parameters = params

        # use callback to make sure channel security parameters are set immedialty
        # and we do no get race conditions
        def clb(future):
            response = struct_from_binary(ua.OpenSecureChannelResponse, future.result())
            response.ResponseHeader.ServiceResult.check()
            self._connection.set_channel(response.Parameters, params.RequestType, params.ClientNonce)
            clb.future.set_result(response)
        clb.future = Future()  # hack to have a variable only shared between a callback and us

        self._send_request(request, message_type=ua.MessageType.SecureOpen, callback=clb)
        # wait for our callbackto finish rexecuting before returning
        response = clb.future.result(self.timeout)
        response.ResponseHeader.ServiceResult.check()

        return response.Parameters

    def close_secure_channel(self):
        """
        close secure channel. It seems to trigger a shutdown of socket in most servers, so be prepare to reconnect.
        OPC UA specs Part 6, 7.1.4 say that Server does not send a CloseSecureChannel response and should just close
        socket
        """
        self.logger.info("close_secure_channel")
        request = ua.CloseSecureChannelRequest()
        try:
            future = self._send_request(request, message_type=ua.MessageType.SecureClose)
            with self._lock:
                # some servers send a response here, most do not ... so we ignore
                future.cancel()
        except (socket.error, OSError) as exc:
            if exc.errno in (errno.ENOTCONN, errno.EBADF):
                # Socket is closed, so can't send CloseSecureChannelRequest.
                self.logger.warning("close_secure_channel() failed: socket already closed")
            else:
                raise

    def is_secure_channel_open(self):
        return self._connection.is_open()


class UaClient(object):

    """
    low level OPC-UA client.

    It implements (almost) all methods defined in opcua spec
    taking in argument the structures defined in opcua spec.

    In this Python implementation  most of the structures are defined in
    uaprotocol_auto.py and uaprotocol_hand.py available under opcua.ua
    """

    def __init__(self, timeout=1):
        self.logger = logging.getLogger(__name__)
        # _publishcallbacks should be accessed in recv thread only
        self._publishcallbacks = {}
        self._timeout = timeout
        self._uasocket = None
        self.security_policy = ua.SecurityPolicy()

    def set_security(self, policy):
        self.security_policy = policy

    def connect_socket(self, host, port):
        """
        connect to server socket and start receiving thread
        """
        self._uasocket = UASocketClient(self._timeout, security_policy=self.security_policy)
        return self._uasocket.connect_socket(host, port)

    def disconnect_socket(self):
        return self._uasocket.disconnect_socket()

    def send_hello(self, url, max_messagesize=0, max_chunkcount=0):
        return self._uasocket.send_hello(url, max_messagesize, max_chunkcount)

    def open_secure_channel(self, params):
        return self._uasocket.open_secure_channel(params)

    def close_secure_channel(self):
        """
        close secure channel. It seems to trigger a shutdown of socket
        in most servers, so be prepare to reconnect
        """
        return self._uasocket.close_secure_channel()

    def create_session(self, parameters):
        self.logger.info("create_session")
        request = ua.CreateSessionRequest()
        request.Parameters = parameters
        data = self._uasocket.send_request(request)
        response = struct_from_binary(ua.CreateSessionResponse, data)
        self.logger.debug(response)
        response.ResponseHeader.ServiceResult.check()
        self._uasocket.authentication_token = response.Parameters.AuthenticationToken
        return response.Parameters

    def activate_session(self, parameters):
        self.logger.info("activate_session")
        request = ua.ActivateSessionRequest()
        request.Parameters = parameters
        data = self._uasocket.send_request(request)
        response = struct_from_binary(ua.ActivateSessionResponse, data)
        self.logger.debug(response)
        response.ResponseHeader.ServiceResult.check()
        return response.Parameters

    def close_session(self, deletesubscriptions):
        self.logger.info("close_session")
        # Bail out if we don't have an open server-channel to unsubscribe ourself.
        if not self._uasocket.is_secure_channel_open():
            return
        request = ua.CloseSessionRequest()
        request.DeleteSubscriptions = deletesubscriptions
        data = self._uasocket.send_request(request)
        response = struct_from_binary(ua.CloseSessionResponse, data)
        try:
            response.ResponseHeader.ServiceResult.check()
        except BadSessionClosed:
            # Problem: closing the session with open publish requests leads to BadSessionClosed responses
            #          we can just ignore it therefore.
            #          Alternatively we could make sure that there are no publish requests in flight when
            #          closing the session.
            pass

    def browse(self, parameters):
        self.logger.info("browse")
        request = ua.BrowseRequest()
        request.Parameters = parameters
        data = self._uasocket.send_request(request)
        response = struct_from_binary(ua.BrowseResponse, data)
        self.logger.debug(response)
        response.ResponseHeader.ServiceResult.check()
        return response.Results

    def browse_next(self, parameters):
        self.logger.info("browse next")
        request = ua.BrowseNextRequest()
        request.Parameters = parameters
        data = self._uasocket.send_request(request)
        response = struct_from_binary(ua.BrowseNextResponse, data)
        self.logger.debug(response)
        response.ResponseHeader.ServiceResult.check()
        return response.Parameters.Results

    def read(self, parameters):
        self.logger.info("read")
        request = ua.ReadRequest()
        request.Parameters = parameters
        data = self._uasocket.send_request(request)
        response = struct_from_binary(ua.ReadResponse, data)
        self.logger.debug(response)
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

    def write(self, params):
        self.logger.info("read")
        request = ua.WriteRequest()
        request.Parameters = params
        data = self._uasocket.send_request(request)
        response = struct_from_binary(ua.WriteResponse, data)
        self.logger.debug(response)
        response.ResponseHeader.ServiceResult.check()
        return response.Results

    def get_endpoints(self, params):
        self.logger.info("get_endpoint")
        request = ua.GetEndpointsRequest()
        request.Parameters = params
        data = self._uasocket.send_request(request)
        response = struct_from_binary(ua.GetEndpointsResponse, data)
        self.logger.debug(response)
        response.ResponseHeader.ServiceResult.check()
        return response.Endpoints

    def find_servers(self, params):
        self.logger.info("find_servers")
        request = ua.FindServersRequest()
        request.Parameters = params
        data = self._uasocket.send_request(request)
        response = struct_from_binary(ua.FindServersResponse, data)
        self.logger.debug(response)
        response.ResponseHeader.ServiceResult.check()
        return response.Servers

    def find_servers_on_network(self, params):
        self.logger.info("find_servers_on_network")
        request = ua.FindServersOnNetworkRequest()
        request.Parameters = params
        data = self._uasocket.send_request(request)
        response = struct_from_binary(ua.FindServersOnNetworkResponse, data)
        self.logger.debug(response)
        response.ResponseHeader.ServiceResult.check()
        return response.Parameters

    def register_server(self, registered_server):
        self.logger.info("register_server")
        request = ua.RegisterServerRequest()
        request.Server = registered_server
        data = self._uasocket.send_request(request)
        response = struct_from_binary(ua.RegisterServerResponse, data)
        self.logger.debug(response)
        response.ResponseHeader.ServiceResult.check()
        # nothing to return for this service

    def register_server2(self, params):
        self.logger.info("register_server2")
        request = ua.RegisterServer2Request()
        request.Parameters = params
        data = self._uasocket.send_request(request)
        response = struct_from_binary(ua.RegisterServer2Response, data)
        self.logger.debug(response)
        response.ResponseHeader.ServiceResult.check()
        return response.ConfigurationResults

    def translate_browsepaths_to_nodeids(self, browsepaths):
        self.logger.info("translate_browsepath_to_nodeid")
        request = ua.TranslateBrowsePathsToNodeIdsRequest()
        request.Parameters.BrowsePaths = browsepaths
        data = self._uasocket.send_request(request)
        response = struct_from_binary(ua.TranslateBrowsePathsToNodeIdsResponse, data)
        self.logger.debug(response)
        response.ResponseHeader.ServiceResult.check()
        return response.Results

    def create_subscription(self, params, publish_callback, ready_callback=None):
        self.logger.info("create_subscription")
        request = ua.CreateSubscriptionRequest()
        request.Parameters = params
        resp_fut = Future()
        mycallbak = partial(self._create_subscription_callback, publish_callback, ready_callback, resp_fut)
        self._uasocket.send_request(request, mycallbak)
        return resp_fut.result(self._timeout)

    def _create_subscription_callback(self, pub_callback, ready_callback, resp_fut, data_fut):
        self.logger.info("_create_subscription_callback")
        data = data_fut.result()
        response = struct_from_binary(ua.CreateSubscriptionResponse, data)
        self.logger.debug(response)
        response.ResponseHeader.ServiceResult.check()
        if ready_callback:
            ready_callback(response)
        self._publishcallbacks[response.Parameters.SubscriptionId] = pub_callback
        resp_fut.set_result(response.Parameters)

    def registered_subscriptions(self):
        """Get all subscriptions we know about"""
        return [cb.__self__ for cb in self._publishcallbacks.values()]

    def delete_subscriptions(self, subscriptionids):
        self.logger.info("delete_subscription")
        request = ua.DeleteSubscriptionsRequest()
        request.Parameters.SubscriptionIds = subscriptionids
        resp_fut = Future()
        mycallbak = partial(self._delete_subscriptions_callback, subscriptionids, resp_fut)
        self._uasocket.send_request(request, mycallbak)
        return resp_fut.result(self._timeout)

    def _delete_subscriptions_callback(self, subscriptionids, resp_fut, data_fut):
        self.logger.info("_delete_subscriptions_callback")
        data = data_fut.result()
        response = struct_from_binary(ua.DeleteSubscriptionsResponse, data)
        self.logger.debug(response)
        response.ResponseHeader.ServiceResult.check()
        for sid in subscriptionids:
            self._publishcallbacks.pop(sid)
        resp_fut.set_result(response.Results)

    def publish(self, acks=None):
        self.logger.info("publish")
        if acks is None:
            acks = []
        request = ua.PublishRequest()
        request.Parameters.SubscriptionAcknowledgements = acks
        self._uasocket.send_request(request, self._call_publish_callback, timeout=0)

    def _call_publish_callback(self, future):
        self.logger.info("call_publish_callback")
        try:
            data = future.result()
        except CancelledError:  # we are cancelled, we just return
            return

        # check if answer looks ok
        try:
            self._uasocket.check_answer(data, "while waiting for publish response")
        except BadTimeout:  # Spec Part 4, 7.28
            self.publish()
            return
        except BadNoSubscription:  # Spec Part 5, 13.8.1
            # BadNoSubscription is expected after deleting the last subscription.
            #
            # We should therefore also check for len(self._publishcallbacks) == 0, but
            # this gets us into trouble if a Publish response arrives before the
            # DeleteSubscription response.
            #
            # We could remove the callback already when sending the DeleteSubscription request,
            # but there are some legitimate reasons to keep them around, such as when the server
            # responds with "BadTimeout" and we should try again later instead of just removing
            # the subscription client-side.
            #
            # There are a variety of ways to act correctly, but the most practical solution seems
            # to be to just ignore any BadNoSubscription responses.
            self.logger.info("BadNoSubscription received, ignoring because it's probably valid.")
            return

        # parse publish response
        try:
            response = struct_from_binary(ua.PublishResponse, data)
            self.logger.debug(response)
        except Exception:
            # INFO: catching the exception here might be obsolete because we already
            #       catch BadTimeout above. However, it's not really clear what this code
            #       does so it stays in, doesn't seem to hurt.
            self.logger.exception("Error parsing notificatipn from server")
            self.publish([])  # send publish request ot server so he does stop sending notifications
            return

        # look for callback
        try:
            callback = self._publishcallbacks[response.Parameters.SubscriptionId]
        except KeyError:
            self.logger.warning("Received data for unknown subscription: %s ", response.Parameters.SubscriptionId)
            return

        # do callback
        try:
            callback(response.Parameters)
        except Exception:  # we call client code, catch everything!
            self.logger.exception("Exception while calling user callback: %s")

    def create_monitored_items(self, params):
        self.logger.info("create_monitored_items")
        request = ua.CreateMonitoredItemsRequest()
        request.Parameters = params
        data = self._uasocket.send_request(request)
        response = struct_from_binary(ua.CreateMonitoredItemsResponse, data)
        self.logger.debug(response)
        response.ResponseHeader.ServiceResult.check()
        return response.Results

    def delete_monitored_items(self, params):
        self.logger.info("delete_monitored_items")
        request = ua.DeleteMonitoredItemsRequest()
        request.Parameters = params
        data = self._uasocket.send_request(request)
        response = struct_from_binary(ua.DeleteMonitoredItemsResponse, data)
        self.logger.debug(response)
        response.ResponseHeader.ServiceResult.check()
        return response.Results

    def add_nodes(self, nodestoadd):
        self.logger.info("add_nodes")
        request = ua.AddNodesRequest()
        request.Parameters.NodesToAdd = nodestoadd
        data = self._uasocket.send_request(request)
        response = struct_from_binary(ua.AddNodesResponse, data)
        self.logger.debug(response)
        response.ResponseHeader.ServiceResult.check()
        return response.Results

    def add_references(self, refs):
        self.logger.info("add_references")
        request = ua.AddReferencesRequest()
        request.Parameters.ReferencesToAdd = refs
        data = self._uasocket.send_request(request)
        response = struct_from_binary(ua.AddReferencesResponse, data)
        self.logger.debug(response)
        response.ResponseHeader.ServiceResult.check()
        return response.Results

    def delete_references(self, refs):
        self.logger.info("delete")
        request = ua.DeleteReferencesRequest()
        request.Parameters.ReferencesToDelete = refs
        data = self._uasocket.send_request(request)
        response = struct_from_binary(ua.DeleteReferencesResponse, data)
        self.logger.debug(response)
        response.ResponseHeader.ServiceResult.check()
        return response.Parameters.Results

    def delete_nodes(self, params):
        self.logger.info("delete_nodes")
        request = ua.DeleteNodesRequest()
        request.Parameters = params
        data = self._uasocket.send_request(request)
        response = struct_from_binary(ua.DeleteNodesResponse, data)
        self.logger.debug(response)
        response.ResponseHeader.ServiceResult.check()
        return response.Results

    def call(self, methodstocall):
        request = ua.CallRequest()
        request.Parameters.MethodsToCall = methodstocall
        data = self._uasocket.send_request(request)
        response = struct_from_binary(ua.CallResponse, data)
        self.logger.debug(response)
        response.ResponseHeader.ServiceResult.check()
        return response.Results

    def history_read(self, params):
        self.logger.info("history_read")
        request = ua.HistoryReadRequest()
        request.Parameters = params
        data = self._uasocket.send_request(request)
        response = struct_from_binary(ua.HistoryReadResponse, data)
        self.logger.debug(response)
        response.ResponseHeader.ServiceResult.check()
        return response.Results

    def modify_monitored_items(self, params):
        self.logger.info("modify_monitored_items")
        request = ua.ModifyMonitoredItemsRequest()
        request.Parameters = params
        data = self._uasocket.send_request(request)
        response = struct_from_binary(ua.ModifyMonitoredItemsResponse, data)
        self.logger.debug(response)
        response.ResponseHeader.ServiceResult.check()
        return response.Results

    def register_nodes(self, nodes):
        self.logger.info("register_nodes")
        request = ua.RegisterNodesRequest()
        request.Parameters.NodesToRegister = nodes
        data = self._uasocket.send_request(request)
        response = struct_from_binary(ua.RegisterNodesResponse, data)
        self.logger.debug(response)
        response.ResponseHeader.ServiceResult.check()
        return response.Parameters.RegisteredNodeIds

    def unregister_nodes(self, nodes):
        self.logger.info("unregister_nodes")
        request = ua.UnregisterNodesRequest()
        request.Parameters.NodesToUnregister = nodes
        data = self._uasocket.send_request(request)
        response = struct_from_binary(ua.UnregisterNodesResponse, data)
        self.logger.debug(response)
        response.ResponseHeader.ServiceResult.check()
        # nothing to return for this service

    def get_attributes(self, nodes, attr):
        self.logger.info("get_attribute")
        request = ua.ReadRequest()
        for node in nodes:
            rv = ua.ReadValueId()
            rv.NodeId = node
            rv.AttributeId = attr
            request.Parameters.NodesToRead.append(rv)
        data = self._uasocket.send_request(request)
        response = struct_from_binary(ua.ReadResponse, data)
        response.ResponseHeader.ServiceResult.check()
        return response.Results

    def set_attributes(self, nodeids, datavalues, attributeid=ua.AttributeIds.Value):
        """
        Set an attribute of multiple nodes
        datavalue is a ua.DataValue object
        """
        self.logger.info("set_attributes of several nodes")
        request = ua.WriteRequest()
        for idx, nodeid in enumerate(nodeids):
            attr = ua.WriteValue()
            attr.NodeId = nodeid
            attr.AttributeId = attributeid
            attr.Value = datavalues[idx]
            request.Parameters.NodesToWrite.append(attr)
        data = self._uasocket.send_request(request)
        response = struct_from_binary(ua.WriteResponse, data)
        response.ResponseHeader.ServiceResult.check()
        return response.Results

