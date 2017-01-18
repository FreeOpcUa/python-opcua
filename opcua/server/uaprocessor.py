
import logging
from threading import RLock, Lock
import time

from opcua import ua
from opcua.common import utils


class PublishRequestData(object):

    def __init__(self):
        self.requesthdr = None
        self.algohdr = None
        self.seqhdr = None
        self.timestamp = time.time()


class UaProcessor(object):

    def __init__(self, internal_server, socket):
        self.logger = logging.getLogger(__name__)
        self.iserver = internal_server
        self.name = socket.get_extra_info('peername')
        self.sockname = socket.get_extra_info('sockname')
        self.session = None
        self.socket = socket
        self._socketlock = Lock()
        self._datalock = RLock()
        self._publishdata_queue = []
        self._publish_result_queue = []  # used when we need to wait for PublishRequest
        self._connection = ua.SecureConnection(ua.SecurityPolicy())

    def set_policies(self, policies):
        self._connection.set_policy_factories(policies)

    def send_response(self, requesthandle, algohdr, seqhdr, response, msgtype=ua.MessageType.SecureMessage):
        with self._socketlock:
            response.ResponseHeader.RequestHandle = requesthandle
            data = self._connection.message_to_binary(
                response.to_binary(), message_type=msgtype, request_id=seqhdr.RequestId, algohdr=algohdr)

            self.socket.write(data)

    def open_secure_channel(self, algohdr, seqhdr, body):
        request = ua.OpenSecureChannelRequest.from_binary(body)

        self._connection.select_policy(
            algohdr.SecurityPolicyURI, algohdr.SenderCertificate, request.Parameters.SecurityMode)

        channel = self._connection.open(request.Parameters, self.iserver)
        # send response
        response = ua.OpenSecureChannelResponse()
        response.Parameters = channel
        self.send_response(request.RequestHeader.RequestHandle, None, seqhdr, response, ua.MessageType.SecureOpen)

    def forward_publish_response(self, result):
        self.logger.info("forward publish response %s", result)
        with self._datalock:
            while True:
                if len(self._publishdata_queue) == 0:
                    self._publish_result_queue.append(result)
                    self.logger.info("Server wants to send publish answer but no publish request is available,"
                                     "enqueing notification, length of result queue is %s",
                                     len(self._publish_result_queue))
                    return
                requestdata = self._publishdata_queue.pop(0)
                if time.time() - requestdata.timestamp < requestdata.requesthdr.TimeoutHint / 1000:
                    break

        response = ua.PublishResponse()
        response.Parameters = result

        self.send_response(requestdata.requesthdr.RequestHandle, requestdata.algohdr, requestdata.seqhdr, response)

    def process(self, header, body):
        msg = self._connection.receive_from_header_and_body(header, body)
        if isinstance(msg, ua.Message):
            if header.MessageType == ua.MessageType.SecureOpen:
                self.open_secure_channel(msg.SecurityHeader(), msg.SequenceHeader(), msg.body())

            elif header.MessageType == ua.MessageType.SecureClose:
                self._connection.close()
                return False

            elif header.MessageType == ua.MessageType.SecureMessage:
                return self.process_message(msg.SecurityHeader(), msg.SequenceHeader(), msg.body())
        elif isinstance(msg, ua.Hello):
            ack = ua.Acknowledge()
            ack.ReceiveBufferSize = msg.ReceiveBufferSize
            ack.SendBufferSize = msg.SendBufferSize
            data = self._connection.tcp_to_binary(ua.MessageType.Acknowledge, ack)
            self.socket.write(data)
        elif isinstance(msg, ua.ErrorMessage):
            self.logger.warning("Received an error message type")
        elif msg is None:
            pass  # msg is a ChunkType.Intermediate of an ua.MessageType.SecureMessage
        else:
            self.logger.warning("Unsupported message type: %s", header.MessageType)
            raise utils.ServiceError(ua.StatusCodes.BadTcpMessageTypeInvalid)
        return True

    def process_message(self, algohdr, seqhdr, body):
        typeid = ua.NodeId.from_binary(body)
        requesthdr = ua.RequestHeader.from_binary(body)
        try:
            return self._process_message(typeid, requesthdr, algohdr, seqhdr, body)
        except utils.ServiceError as e:
            status = ua.StatusCode(e.code)
            response = ua.ServiceFault()
            response.ResponseHeader.ServiceResult = status
            self.logger.info("sending service fault response: %s (%s)", status.doc, status.name)
            self.send_response(requesthdr.RequestHandle, algohdr, seqhdr, response)
            return True

    def _process_message(self, typeid, requesthdr, algohdr, seqhdr, body):
        if typeid == ua.NodeId(ua.ObjectIds.CreateSessionRequest_Encoding_DefaultBinary):
            self.logger.info("Create session request")
            params = ua.CreateSessionParameters.from_binary(body)

            # create the session on server
            self.session = self.iserver.create_session(self.name, external=True)
            # get a session creation result to send back
            sessiondata = self.session.create_session(params, sockname=self.sockname)

            response = ua.CreateSessionResponse()
            response.Parameters = sessiondata
            response.Parameters.ServerCertificate = self._connection._security_policy.client_certificate
            if self._connection._security_policy.server_certificate is None:
                data = params.ClientNonce
            else:
                data = self._connection._security_policy.server_certificate + params.ClientNonce
            response.Parameters.ServerSignature.Signature = \
                self._connection._security_policy.asymmetric_cryptography.signature(data)

            response.Parameters.ServerSignature.Algorithm = "http://www.w3.org/2000/09/xmldsig#rsa-sha1"

            self.logger.info("sending create sesssion response")
            self.send_response(requesthdr.RequestHandle, algohdr, seqhdr, response)

        elif typeid == ua.NodeId(ua.ObjectIds.CloseSessionRequest_Encoding_DefaultBinary):
            self.logger.info("Close session request")
            deletesubs = ua.ua_binary.Primitives.Boolean.unpack(body)

            self.session.close_session(deletesubs)

            response = ua.CloseSessionResponse()
            self.logger.info("sending close sesssion response")
            self.send_response(requesthdr.RequestHandle, algohdr, seqhdr, response)

        elif typeid == ua.NodeId(ua.ObjectIds.ActivateSessionRequest_Encoding_DefaultBinary):
            self.logger.info("Activate session request")
            params = ua.ActivateSessionParameters.from_binary(body)

            if not self.session:
                self.logger.info("request to activate non-existing session")
                raise utils.ServiceError(ua.StatusCodes.BadSessionIdInvalid)

            if self._connection._security_policy.client_certificate is None:
                data = self.session.nonce
            else:
                data = self._connection._security_policy.client_certificate + self.session.nonce
            self._connection._security_policy.asymmetric_cryptography.verify(data, params.ClientSignature.Signature)

            result = self.session.activate_session(params)

            response = ua.ActivateSessionResponse()
            response.Parameters = result

            self.logger.info("sending read response")
            self.send_response(requesthdr.RequestHandle, algohdr, seqhdr, response)

        elif typeid == ua.NodeId(ua.ObjectIds.ReadRequest_Encoding_DefaultBinary):
            self.logger.info("Read request")
            params = ua.ReadParameters.from_binary(body)

            results = self.session.read(params)

            response = ua.ReadResponse()
            response.Results = results

            self.logger.info("sending read response")
            self.send_response(requesthdr.RequestHandle, algohdr, seqhdr, response)

        elif typeid == ua.NodeId(ua.ObjectIds.WriteRequest_Encoding_DefaultBinary):
            self.logger.info("Write request")
            params = ua.WriteParameters.from_binary(body)

            results = self.session.write(params)

            response = ua.WriteResponse()
            response.Results = results

            self.logger.info("sending write response")
            self.send_response(requesthdr.RequestHandle, algohdr, seqhdr, response)

        elif typeid == ua.NodeId(ua.ObjectIds.BrowseRequest_Encoding_DefaultBinary):
            self.logger.info("Browse request")
            params = ua.BrowseParameters.from_binary(body)

            results = self.session.browse(params)

            response = ua.BrowseResponse()
            response.Results = results

            self.logger.info("sending browse response")
            self.send_response(requesthdr.RequestHandle, algohdr, seqhdr, response)

        elif typeid == ua.NodeId(ua.ObjectIds.GetEndpointsRequest_Encoding_DefaultBinary):
            self.logger.info("get endpoints request")
            params = ua.GetEndpointsParameters.from_binary(body)

            endpoints = self.iserver.get_endpoints(params, sockname=self.sockname)

            response = ua.GetEndpointsResponse()
            response.Endpoints = endpoints

            self.logger.info("sending get endpoints response")
            self.send_response(requesthdr.RequestHandle, algohdr, seqhdr, response)

        elif typeid == ua.NodeId(ua.ObjectIds.FindServersRequest_Encoding_DefaultBinary):
            self.logger.info("find servers request")
            params = ua.FindServersParameters.from_binary(body)

            servers = self.iserver.find_servers(params)

            response = ua.FindServersResponse()
            response.Servers = servers

            self.logger.info("sending find servers response")
            self.send_response(requesthdr.RequestHandle, algohdr, seqhdr, response)

        elif typeid == ua.NodeId(ua.ObjectIds.RegisterServerRequest_Encoding_DefaultBinary):
            self.logger.info("register server request")
            serv = ua.RegisteredServer.from_binary(body)

            self.iserver.register_server(serv)

            response = ua.RegisterServerResponse()

            self.logger.info("sending register server response")
            self.send_response(requesthdr.RequestHandle, algohdr, seqhdr, response)

        elif typeid == ua.NodeId(ua.ObjectIds.RegisterServer2Request_Encoding_DefaultBinary):
            self.logger.info("register server 2 request")
            params = ua.RegisterServer2Parameters.from_binary(body)

            results = self.iserver.register_server2(params)

            response = ua.RegisterServer2Response()
            response.ConfigurationResults = results

            self.logger.info("sending register server 2 response")
            self.send_response(requesthdr.RequestHandle, algohdr, seqhdr, response)

        elif typeid == ua.NodeId(ua.ObjectIds.TranslateBrowsePathsToNodeIdsRequest_Encoding_DefaultBinary):
            self.logger.info("translate browsepaths to nodeids request")
            params = ua.TranslateBrowsePathsToNodeIdsParameters.from_binary(body)

            paths = self.session.translate_browsepaths_to_nodeids(params.BrowsePaths)

            response = ua.TranslateBrowsePathsToNodeIdsResponse()
            response.Results = paths

            self.logger.info("sending translate browsepaths to nodeids response")
            self.send_response(requesthdr.RequestHandle, algohdr, seqhdr, response)

        elif typeid == ua.NodeId(ua.ObjectIds.AddNodesRequest_Encoding_DefaultBinary):
            self.logger.info("add nodes request")
            params = ua.AddNodesParameters.from_binary(body)

            results = self.session.add_nodes(params.NodesToAdd)

            response = ua.AddNodesResponse()
            response.Results = results

            self.logger.info("sending add node response")
            self.send_response(requesthdr.RequestHandle, algohdr, seqhdr, response)

        elif typeid == ua.NodeId(ua.ObjectIds.DeleteNodesRequest_Encoding_DefaultBinary):
            self.logger.info("delete nodes request")
            params = ua.DeleteNodesParameters.from_binary(body)

            results = self.session.delete_nodes(params)

            response = ua.DeleteNodesResponse()
            response.Results = results

            self.logger.info("sending delete node response")
            self.send_response(requesthdr.RequestHandle, algohdr, seqhdr, response)

        elif typeid == ua.NodeId(ua.ObjectIds.AddReferencesRequest_Encoding_DefaultBinary):
            self.logger.info("add references request")
            params = ua.AddReferencesParameters.from_binary(body)

            results = self.session.add_references(params.ReferencesToAdd)

            response = ua.AddReferencesResponse()
            response.Results = results

            self.logger.info("sending add references response")
            self.send_response(requesthdr.RequestHandle, algohdr, seqhdr, response)

        elif typeid == ua.NodeId(ua.ObjectIds.CreateSubscriptionRequest_Encoding_DefaultBinary):
            self.logger.info("create subscription request")
            params = ua.CreateSubscriptionParameters.from_binary(body)

            result = self.session.create_subscription(params, self.forward_publish_response)

            response = ua.CreateSubscriptionResponse()
            response.Parameters = result

            self.logger.info("sending create subscription response")
            self.send_response(requesthdr.RequestHandle, algohdr, seqhdr, response)

        elif typeid == ua.NodeId(ua.ObjectIds.DeleteSubscriptionsRequest_Encoding_DefaultBinary):
            self.logger.info("delete subscriptions request")
            params = ua.DeleteSubscriptionsParameters.from_binary(body)

            results = self.session.delete_subscriptions(params.SubscriptionIds)

            response = ua.DeleteSubscriptionsResponse()
            response.Results = results

            self.logger.info("sending delte subscription response")
            self.send_response(requesthdr.RequestHandle, algohdr, seqhdr, response)

        elif typeid == ua.NodeId(ua.ObjectIds.CreateMonitoredItemsRequest_Encoding_DefaultBinary):
            self.logger.info("create monitored items request")
            params = ua.CreateMonitoredItemsParameters.from_binary(body)
            results = self.session.create_monitored_items(params)

            response = ua.CreateMonitoredItemsResponse()
            response.Results = results

            self.logger.info("sending create monitored items response")
            self.send_response(requesthdr.RequestHandle, algohdr, seqhdr, response)

        elif typeid == ua.NodeId(ua.ObjectIds.ModifyMonitoredItemsRequest_Encoding_DefaultBinary):
            self.logger.info("modify monitored items request")
            params = ua.ModifyMonitoredItemsParameters.from_binary(body)
            results = self.session.modify_monitored_items(params)

            response = ua.ModifyMonitoredItemsResponse()
            response.Results = results

            self.logger.info("sending modify monitored items response")
            self.send_response(requesthdr.RequestHandle, algohdr, seqhdr, response)

        elif typeid == ua.NodeId(ua.ObjectIds.DeleteMonitoredItemsRequest_Encoding_DefaultBinary):
            self.logger.info("delete monitored items request")
            params = ua.DeleteMonitoredItemsParameters.from_binary(body)

            results = self.session.delete_monitored_items(params)

            response = ua.DeleteMonitoredItemsResponse()
            response.Results = results

            self.logger.info("sending delete monitored items response")
            self.send_response(requesthdr.RequestHandle, algohdr, seqhdr, response)

        elif typeid == ua.NodeId(ua.ObjectIds.HistoryReadRequest_Encoding_DefaultBinary):
            self.logger.info("history read request")
            params = ua.HistoryReadParameters.from_binary(body)

            results = self.session.history_read(params)

            response = ua.HistoryReadResponse()
            response.Results = results

            self.logger.info("sending history read response")
            self.send_response(requesthdr.RequestHandle, algohdr, seqhdr, response)

        elif typeid == ua.NodeId(ua.ObjectIds.RegisterNodesRequest_Encoding_DefaultBinary):
            self.logger.info("register nodes request")
            params = ua.RegisterNodesParameters.from_binary(body)
            self.logger.info("Node registration not implemented")

            response = ua.RegisterNodesResponse()
            response.Parameters.RegisteredNodeIds = params.NodesToRegister

            self.logger.info("sending register nodes response")
            self.send_response(requesthdr.RequestHandle, algohdr, seqhdr, response)

        elif typeid == ua.NodeId(ua.ObjectIds.UnregisterNodesRequest_Encoding_DefaultBinary):
            self.logger.info("unregister nodes request")
            params = ua.UnregisterNodesParameters.from_binary(body)

            response = ua.UnregisterNodesResponse()

            self.logger.info("sending unregister nodes response")
            self.send_response(requesthdr.RequestHandle, algohdr, seqhdr, response)

        elif typeid == ua.NodeId(ua.ObjectIds.PublishRequest_Encoding_DefaultBinary):
            self.logger.info("publish request")

            if not self.session:
                return False

            params = ua.PublishParameters.from_binary(body)

            data = PublishRequestData()
            data.requesthdr = requesthdr
            data.seqhdr = seqhdr
            data.algohdr = algohdr
            with self._datalock:
                self._publishdata_queue.append(data)  # will be used to send publish answers from server
                if self._publish_result_queue:
                    result = self._publish_result_queue.pop(0)
                    self.forward_publish_response(result)
            self.session.publish(params.SubscriptionAcknowledgements)
            self.logger.info("publish forward to server")

        elif typeid == ua.NodeId(ua.ObjectIds.RepublishRequest_Encoding_DefaultBinary):
            self.logger.info("re-publish request")

            params = ua.RepublishParameters.from_binary(body)
            msg = self.session.republish(params)

            response = ua.RepublishResponse()
            response.NotificationMessage = msg

            self.send_response(requesthdr.RequestHandle, algohdr, seqhdr, response)

        elif typeid == ua.NodeId(ua.ObjectIds.CloseSecureChannelRequest_Encoding_DefaultBinary):
            self.logger.info("close secure channel request")
            self._connection.close()
            response = ua.CloseSecureChannelResponse()
            self.send_response(requesthdr.RequestHandle, algohdr, seqhdr, response)
            return False

        elif typeid == ua.NodeId(ua.ObjectIds.CallRequest_Encoding_DefaultBinary):
            self.logger.info("call request")

            params = ua.CallParameters.from_binary(body)

            results = self.session.call(params.MethodsToCall)

            response = ua.CallResponse()
            response.Results = results

            self.send_response(requesthdr.RequestHandle, algohdr, seqhdr, response)

        else:
            self.logger.warning("Unknown message received %s", typeid)
            raise utils.ServiceError(ua.StatusCodes.BadNotImplemented)

        return True

    def close(self):
        """
        to be called when client has disconnected to ensure we really close
        everything we should
        """
        print("Cleanup client connection: ", self.name)
        if self.session:
            self.session.close_session(True)
