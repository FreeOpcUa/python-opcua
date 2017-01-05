"""
Low level binary client
"""

import logging
import socket
from threading import Thread, Lock
from concurrent.futures import Future
from functools import partial

from opcua import ua
from opcua.common import utils
from opcua.ua.uaerrors import UaError, BadTimeout, BadNoSubscription, BadSessionClosed


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
        self._connection = ua.SecureConnection(security_policy)

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
                binreq = request.to_binary()
            except:
                # reset reqeust handle if any error
                # see self._create_request_header
                self._request_handle -= 1
                raise
            self._request_id += 1
            future = Future()
            if callback:
                future.add_done_callback(callback)
            self._callbackmap[self._request_id] = future
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
        typeid = ua.NodeId.from_binary(data)
        if typeid == ua.FourByteNodeId(ua.ObjectIds.ServiceFault_Encoding_DefaultBinary):
            self.logger.warning("ServiceFault from server received %s", context)
            hdr = ua.ResponseHeader.from_binary(data)
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
                break
            except UaError:
                self.logger.exception("Protocol Error")
        self.logger.info("Thread ended")

    def _receive(self):
        msg = self._connection.receive_from_socket(self._socket)
        if msg is None:
            return
        elif isinstance(msg, ua.Message):
            self._call_callback(msg.request_id(), msg.body())
        elif isinstance(msg, ua.Acknowledge):
            self._call_callback(0, msg)
        elif isinstance(msg, ua.ErrorMessage):
            self.logger.warning("Received an error: %s", msg)
        else:
            raise ua.UaError("Unsupported message type: %s", msg)

    def _call_callback(self, request_id, body):
        with self._lock:
            future = self._callbackmap.pop(request_id, None)
            if future is None:
                raise ua.UaError("No future object found for request: {0}, callbacks in list are {1}".format(request_id, self._callbackmap.keys()))
        future.set_result(body)

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
        sock = socket.create_connection((host, port))
        sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)  # nodelay ncessary to avoid packing in one frame, some servers do not like it
        self._socket = utils.SocketWrapper(sock)
        self.start()

    def disconnect_socket(self):
        self.logger.info("stop request")
        self._do_stop = True
        self._socket.socket.shutdown(socket.SHUT_RDWR)
        self._socket.socket.close()

    def send_hello(self, url):
        hello = ua.Hello()
        hello.EndpointUrl = url
        future = Future()
        with self._lock:
            self._callbackmap[0] = future
        binmsg = self._connection.tcp_to_binary(ua.MessageType.Hello, hello)
        self._socket.write(binmsg)
        ack = future.result(self.timeout)
        return ack

    def open_secure_channel(self, params):
        self.logger.info("open_secure_channel")
        request = ua.OpenSecureChannelRequest()
        request.Parameters = params
        future = self._send_request(request, message_type=ua.MessageType.SecureOpen)
        
        # FIXME: we have a race condition here
        # we can get a packet with the new token id before we reach to store it..
        response = ua.OpenSecureChannelResponse.from_binary(future.result(self.timeout))
        response.ResponseHeader.ServiceResult.check()
        self._connection.set_channel(response.Parameters)
        return response.Parameters

    def close_secure_channel(self):
        """
        close secure channel. It seems to trigger a shutdown of socket
        in most servers, so be prepare to reconnect.
        OPC UA specs Part 6, 7.1.4 say that Server does not send a CloseSecureChannel response and should just close socket
        """
        self.logger.info("close_secure_channel")
        request = ua.CloseSecureChannelRequest()
        future = self._send_request(request, message_type=ua.MessageType.SecureClose)
        with self._lock:
            # don't expect any more answers
            future.cancel()
            self._callbackmap.clear()

        # some servers send a response here, most do not ... so we ignore


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
        self._security_policy = ua.SecurityPolicy()

    def set_security(self, policy):
        self._security_policy = policy

    def connect_socket(self, host, port):
        """
        connect to server socket and start receiving thread
        """
        self._uasocket = UASocketClient(self._timeout, security_policy=self._security_policy)
        return self._uasocket.connect_socket(host, port)

    def disconnect_socket(self):
        return self._uasocket.disconnect_socket()

    def send_hello(self, url):
        return self._uasocket.send_hello(url)

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
        response = ua.CreateSessionResponse.from_binary(data)
        self.logger.debug(response)
        response.ResponseHeader.ServiceResult.check()
        self._uasocket.authentication_token = response.Parameters.AuthenticationToken
        return response.Parameters

    def activate_session(self, parameters):
        self.logger.info("activate_session")
        request = ua.ActivateSessionRequest()
        request.Parameters = parameters
        data = self._uasocket.send_request(request)
        response = ua.ActivateSessionResponse.from_binary(data)
        self.logger.debug(response)
        response.ResponseHeader.ServiceResult.check()
        return response.Parameters

    def close_session(self, deletesubscriptions):
        self.logger.info("close_session")
        request = ua.CloseSessionRequest()
        request.DeleteSubscriptions = deletesubscriptions
        data = self._uasocket.send_request(request)
        response = ua.CloseSessionResponse.from_binary(data)
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
        response = ua.BrowseResponse.from_binary(data)
        self.logger.debug(response)
        response.ResponseHeader.ServiceResult.check()
        return response.Results

    def browse_next(self, parameters):
        self.logger.info("browse next")
        request = ua.BrowseNextRequest()
        request.Parameters = parameters
        data = self._uasocket.send_request(request)
        response = ua.BrowseNextResponse.from_binary(data)
        self.logger.debug(response)
        response.ResponseHeader.ServiceResult.check()
        return response.Parameters.Results

    def read(self, parameters):
        self.logger.info("read")
        request = ua.ReadRequest()
        request.Parameters = parameters
        data = self._uasocket.send_request(request)
        response = ua.ReadResponse.from_binary(data)
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
        response = ua.WriteResponse.from_binary(data)
        self.logger.debug(response)
        response.ResponseHeader.ServiceResult.check()
        return response.Results

    def get_endpoints(self, params):
        self.logger.info("get_endpoint")
        request = ua.GetEndpointsRequest()
        request.Parameters = params
        data = self._uasocket.send_request(request)
        response = ua.GetEndpointsResponse.from_binary(data)
        self.logger.debug(response)
        response.ResponseHeader.ServiceResult.check()
        return response.Endpoints

    def find_servers(self, params):
        self.logger.info("find_servers")
        request = ua.FindServersRequest()
        request.Parameters = params
        data = self._uasocket.send_request(request)
        response = ua.FindServersResponse.from_binary(data)
        self.logger.debug(response)
        response.ResponseHeader.ServiceResult.check()
        return response.Servers

    def find_servers_on_network(self, params):
        self.logger.info("find_servers_on_network")
        request = ua.FindServersOnNetworkRequest()
        request.Parameters = params
        data = self._uasocket.send_request(request)
        response = ua.FindServersOnNetworkResponse.from_binary(data)
        self.logger.debug(response)
        response.ResponseHeader.ServiceResult.check()
        return response.Parameters

    def register_server(self, registered_server):
        self.logger.info("register_server")
        request = ua.RegisterServerRequest()
        request.Server = registered_server
        data = self._uasocket.send_request(request)
        response = ua.RegisterServerResponse.from_binary(data)
        self.logger.debug(response)
        response.ResponseHeader.ServiceResult.check()
        # nothing to return for this service

    def register_server2(self, params):
        self.logger.info("register_server2")
        request = ua.RegisterServer2Request()
        request.Parameters = params
        data = self._uasocket.send_request(request)
        response = ua.RegisterServer2Response.from_binary(data)
        self.logger.debug(response)
        response.ResponseHeader.ServiceResult.check()
        return response.ConfigurationResults

    def translate_browsepaths_to_nodeids(self, browsepaths):
        self.logger.info("translate_browsepath_to_nodeid")
        request = ua.TranslateBrowsePathsToNodeIdsRequest()
        request.Parameters.BrowsePaths = browsepaths
        data = self._uasocket.send_request(request)
        response = ua.TranslateBrowsePathsToNodeIdsResponse.from_binary(data)
        self.logger.debug(response)
        response.ResponseHeader.ServiceResult.check()
        return response.Results

    def create_subscription(self, params, callback):
        self.logger.info("create_subscription")
        request = ua.CreateSubscriptionRequest()
        request.Parameters = params
        resp_fut = Future()
        mycallbak = partial(self._create_subscription_callback, callback, resp_fut)
        self._uasocket.send_request(request, mycallbak)
        return resp_fut.result(self._timeout)

    def _create_subscription_callback(self, pub_callback, resp_fut, data_fut):
        self.logger.info("_create_subscription_callback")
        data = data_fut.result()
        response = ua.CreateSubscriptionResponse.from_binary(data)
        self.logger.debug(response)
        response.ResponseHeader.ServiceResult.check()
        self._publishcallbacks[response.Parameters.SubscriptionId] = pub_callback
        resp_fut.set_result(response.Parameters)

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
        response = ua.DeleteSubscriptionsResponse.from_binary(data)
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
        # timeout could be set to 0 (= no timeout) but some servers do not support it
        self._uasocket.send_request(request, self._call_publish_callback, timeout=int(9e8)) # 250 days

    def _call_publish_callback(self, future):
        self.logger.info("call_publish_callback")
        data = future.result()

        # check if answer looks ok
        try:
            self._uasocket.check_answer(data, "while waiting for publish response")
        except BadTimeout: # Spec Part 4, 7.28
            self.publish()
            return
        except BadNoSubscription: # Spec Part 5, 13.8.1
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
            response = ua.PublishResponse.from_binary(data)
            self.logger.debug(response)
        except Exception:
            # INFO: catching the exception here might be obsolete because we already
            #       catch BadTimeout above. However, it's not really clear what this code
            #       does so it stays in, doesn't seem to hurt.
            self.logger.exception("Error parsing notificatipn from server")
            self.publish([]) #send publish request ot server so he does stop sending notifications
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
        response = ua.CreateMonitoredItemsResponse.from_binary(data)
        self.logger.debug(response)
        response.ResponseHeader.ServiceResult.check()
        return response.Results

    def delete_monitored_items(self, params):
        self.logger.info("delete_monitored_items")
        request = ua.DeleteMonitoredItemsRequest()
        request.Parameters = params
        data = self._uasocket.send_request(request)
        response = ua.DeleteMonitoredItemsResponse.from_binary(data)
        self.logger.debug(response)
        response.ResponseHeader.ServiceResult.check()
        return response.Results

    def add_nodes(self, nodestoadd):
        self.logger.info("add_nodes")
        request = ua.AddNodesRequest()
        request.Parameters.NodesToAdd = nodestoadd
        data = self._uasocket.send_request(request)
        response = ua.AddNodesResponse.from_binary(data)
        self.logger.debug(response)
        response.ResponseHeader.ServiceResult.check()
        return response.Results

    def add_references(self, refs):
        self.logger.info("add_references")
        request = ua.AddReferencesRequest()
        request.Parameters.ReferencesToAdd = refs
        data = self._uasocket.send_request(request)
        response = ua.AddReferencesResponse.from_binary(data)
        self.logger.debug(response)
        response.ResponseHeader.ServiceResult.check()
        return response.Results

    def delete_nodes(self, params):
        self.logger.info("delete_nodes")
        request = ua.DeleteNodesRequest()
        request.Parameters = params
        data = self._uasocket.send_request(request)
        response = ua.DeleteNodesResponse.from_binary(data)
        self.logger.debug(response)
        response.ResponseHeader.ServiceResult.check()
        return response.Results

    def call(self, methodstocall):
        request = ua.CallRequest()
        request.Parameters.MethodsToCall = methodstocall
        data = self._uasocket.send_request(request)
        response = ua.CallResponse.from_binary(data)
        self.logger.debug(response)
        response.ResponseHeader.ServiceResult.check()
        return response.Results

    def history_read(self, params):
        self.logger.info("history_read")
        request = ua.HistoryReadRequest()
        request.Parameters = params
        data = self._uasocket.send_request(request)
        response = ua.HistoryReadResponse.from_binary(data)
        self.logger.debug(response)
        response.ResponseHeader.ServiceResult.check()
        return response.Results

    def modify_monitored_items(self, params):
        self.logger.info("modify_monitored_items")
        request = ua.ModifyMonitoredItemsRequest()
        request.Parameters = params
        data = self._uasocket.send_request(request)
        response = ua.ModifyMonitoredItemsResponse.from_binary(data)
        self.logger.debug(response)
        response.ResponseHeader.ServiceResult.check()
        return response.Results
