"""
Socket server forwarding request to internal server
"""
import logging
try:
    import socketserver
except ImportError:
    import SocketServer as socketserver
from threading import Thread

from opcua import ua
from opcua.uaprocessor import UAProcessor

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
        self.socket_server = ThreadingTCPServer((self.hostname, self.port), UAHandler)
        #self.socket_server.daemon_threads = True # this will force a shutdown of all threads, maybe too hard
        self.socket_server.internal_server = self.iserver #allow handler to acces server properties
        self.socket_server.serve_forever()

    def stop(self):
        logger.warning("server shutdown request")
        self.socket_server.shutdown()


class UAHandler(socketserver.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        processor = UAProcessor(self.server.internal_server, self.request, self.client_address)
        try:
            processor.loop()
        except ua.SocketClosedException as ex:
            logger.warning("Client has closed connection: %s", ex)


class ThreadingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


