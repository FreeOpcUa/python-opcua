"""
Socket server forwarding request to internal server
"""
import logging
try:
    import socketserver
except ImportError:
    import SocketServer as socketserver
from threading import Thread, Lock

from opcua import ua
from opcua import utils

logger = logging.getLogger(__name__)

class BinaryServer(Thread):
    """
    Socket server forwarding request to internal server
    """
    def __init__(self, internal_server, hostname, port):
        Thread.__init__(self)
        self.socket_server = None
        self.hostname = hostname
        self.port = port
        self.iserver = internal_server

    def run(self):
        logger.info("Starting server on %s:%s", self.hostname, self.port)
        socketserver.TCPServer.allow_reuse_address = True #get rid of address already in used warning
        self.socket_server = socketserver.TCPServer((self.hostname, self.port), UAHandler)
        self.socket_server.internal_server = self.iserver #allow handler to acces server properties
        self.socket_server.serve_forever()

    def stop(self):
        self.socket_server.shutdown()


class UAHandler(socketserver.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        processor = UAProcessor(self.server.internal_server, self.request)
        try:
            processor.loop()
        except ua.SocketClosedException as ex:
            logger.warn("Client has closed connection")





class UAProcessor(object):
    def __init__(self, internal_server, socket):
        self.logger = logging.getLogger(__name__)
        self.iserver = internal_server
        self.socket = socket
        self.channel = None
        self._lock = Lock()
        self.session = None

    def loop(self):
        #first we want a hello message
        header = ua.Header.from_stream(self.socket)
        body = self.receive_body(header.body_size)
        if header.MessageType != ua.MessageType.Hello:
            self.logger.warn("received a message which is not a hello, sending back an error message %s", header)
            hdr = ua.Header(ua.MessageType.Error, ua.ChunkType.Single)
            self.write_socket(hdr)
            return
        hello = ua.Hello.from_binary(body)
        hdr = ua.Header(ua.MessageType.Acknowledge, ua.ChunkType.Single)
        ack = ua.Acknowledge()
        ack.ReceivebufferSize = hello.ReceiveBufferSize
        ack.SendbufferSize = hello.SendBufferSize
        self.write_socket(hdr, ack)

        while True:
            header = ua.Header.from_stream(self.socket)
            if header is None:
                return
            if header.MessageType == ua.MessageType.Error:
                self.logger.warn("Received an error message type")
                return
            body = self.receive_body(header.body_size)
            if not self.process_body(header, body):
                break

    def send_response(self, requesthandle, algohdr, seqhdr, response, msgtype=ua.MessageType.SecureMessage):
        with self._lock:
            response.ResponseHeader.RequestHandle = requesthandle
            seqhdr.SequenceNumber += 1
            hdr = ua.Header(msgtype, ua.ChunkType.Single, self.channel.SecurityToken.ChannelId)
            self.write_socket(hdr, algohdr, seqhdr, response)

    def write_socket(self, hdr, *args):
        alle = []
        for arg in args:
            data = arg.to_binary()
            hdr.add_size(len(data))
            alle.append(data)
        alle.insert(0, hdr.to_binary())
        alle = b"".join(alle)
        self.logger.info("writting %s bytes to socket, with header %s ", len(alle), hdr)
        #self.logger.info("writting data %s", hdr, [i for i in args])
        #self.logger.debug("data: %s", alle)
        self.socket.send(alle)

    def receive_body(self, size):
        self.logger.debug("reading body of message (%s bytes)", size)
        data = self.socket.recv(size)
        if size != len(data):
            raise Exception("Error, did not received expected number of bytes, got {}, asked for {}".format(len(data), size))
        return utils.Buffer(data)

    def open_secure_channel(self, body):
        algohdr = ua.AsymmetricAlgorithmHeader.from_binary(body)
        seqhdr = ua.SequenceHeader.from_binary(body)
        request = ua.OpenSecureChannelRequest.from_binary(body)

        self.channel = self.iserver.open_secure_channel(request.Parameters, self.channel)
        #send response
        hdr = ua.Header(ua.MessageType.SecureOpen, ua.ChunkType.Single, self.channel.SecurityToken.TokenId)
        response = ua.OpenSecureChannelResponse()
        response.Parameters = self.channel
        self.send_response(request.RequestHeader.RequestHandle, algohdr, seqhdr, response, ua.MessageType.SecureOpen)

    def process_body(self, header, body):
        if header.MessageType == ua.MessageType.SecureOpen:
            self.open_secure_channel(body)

        elif header.MessageType == ua.MessageType.SecureClose:
            if not self.channel or header.ChannelId != self.channel.SecurityToken.ChannelId:
                self.logger.warn("Request to close channel %s which was not issued, current channel is %s", header.ChannelId, self.channel)
                return False

        elif header.MessageType == ua.MessageType.SecureMessage:
            algohdr = ua.SymmetricAlgorithmHeader.from_binary(body)
            seqhdr = ua.SequenceHeader.from_binary(body)
            self.process_message(header, algohdr, seqhdr, body)

        else:
            self.logger.warn("Unsupported message type: %s", header.MessageType)
        return True
    
    def process_message(self, hdr, algohdr, seqhdr, body):
        typeid = ua.NodeId.from_binary(body)
        requesthdr = ua.RequestHeader.from_binary(body)
        if typeid == ua.NodeId(ua.ObjectIds.CreateSessionRequest_Encoding_DefaultBinary):
            self.logger.info("Create session request")
            params = ua.CreateSessionParameters.from_binary(body)

            self.session = self.iserver.create_session(params)

            response = ua.CreateSessionResponse()
            response.Parameters = self.session 
            self.send_response(requesthdr.RequestHandle, algohdr, seqhdr, response)

        elif typeid == ua.NodeId(ua.ObjectIds.CloseSessionRequest_Encoding_DefaultBinary):
            self.logger.info("Create session request")
            deletesubs = ua.unpack_uatype('Boolean', body)
            
            self.iserver.close_session(self.session, deletesubs)

            response = ua.CloseSessionResponse()
            self.send_response(requesthdr.RequestHandle, algohdr, seqhdr, response)

        elif typeid == ua.NodeId(ua.ObjectIds.ActivateSessionRequest_Encoding_DefaultBinary):
            self.logger.info("Activate session request")
            params = ua.ActivateSessionParameters.from_binary(body) 
            
            result = self.iserver.activate_session(self.session, params)

            response = ua.ActivateSessionResponse()
            response.Parameters = result
            self.send_response(requesthdr.RequestHandle, algohdr, seqhdr, response)

        elif typeid == ua.NodeId(ua.ObjectIds.ReadRequest_Encoding_DefaultBinary):
            self.logger.info("Read request")
            params = ua.ReadParameters.from_binary(body) 
            
            results = self.iserver.read(params)

            response = ua.ReadResponse()
            response.Results = results
            self.send_response(requesthdr.RequestHandle, algohdr, seqhdr, response)

        elif typeid == ua.NodeId(ua.ObjectIds.WriteRequest_Encoding_DefaultBinary):
            self.logger.info("Write request")
            params = ua.WriteParameters.from_binary(body) 
            
            results = self.iserver.write(params)

            response = ua.WriteResponse()
            response.Results = results
            self.send_response(requesthdr.RequestHandle, algohdr, seqhdr, response)

        elif typeid == ua.NodeId(ua.ObjectIds.BrowseRequest_Encoding_DefaultBinary):
            self.logger.info("Browse request")
            params = ua.BrowseParameters.from_binary(body) 
            
            results = self.iserver.browse(params)

            response = ua.BrowseResponse()
            response.Results = results
            self.send_response(requesthdr.RequestHandle, algohdr, seqhdr, response)
        elif typeid == ua.NodeId(ua.ObjectIds.GetEndpointsRequest_Encoding_DefaultBinary):
            self.logger.info("get endpoints request")
            params = ua.GetEndpointsParameters.from_binary(body) 
            
            endpoints = self.iserver.get_endpoints(params)

            response = ua.GetEndpointsResponse()
            response.Endpoints = endpoints
            self.send_response(requesthdr.RequestHandle, algohdr, seqhdr, response)


        else:
            self.logger.warn("Uknown message received %s", typeid)
            sf = ua.ServiceFault()
            sf.ResponseHeader.ServiceResult = ua.StatusCode(ua.StatusCodes.BadNotImplemented)
            self.send_response(requesthdr.RequestHandle, algohdr, seqhdr, sf)


