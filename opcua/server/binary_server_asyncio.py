"""
Socket server forwarding request to internal server
"""
import logging
try:
    # we prefer to use bundles asyncio version, otherwise fallback to trollius
    import asyncio
except ImportError:
    import trollius as asyncio


from opcua import ua
from opcua.server.uaprocessor import UaProcessor

logger = logging.getLogger(__name__)


class BinaryServer(object):

    def __init__(self, internal_server, hostname, port):
        self.logger = logging.getLogger(__name__)
        self.hostname = hostname
        self.port = port
        self.iserver = internal_server
        self.loop = internal_server.loop
        self._server = None
        self._policies = []

    def set_policies(self, policies):
        self._policies = policies

    def start(self):

        class OPCUAProtocol(asyncio.Protocol):

            """
            instanciated for every connection
            defined as internal class since it needs access
            to the internal server object
            FIXME: find another solution
            """

            iserver = self.iserver
            loop = self.loop
            logger = self.logger
            policies = self._policies

            def connection_made(self, transport):
                self.peername = transport.get_extra_info('peername')
                self.logger.info('New connection from %s', self.peername)
                self.transport = transport
                self.processor = UaProcessor(self.iserver, self.transport)
                self.processor.set_policies(self.policies)
                self.data = b""
                self.iserver.asyncio_transports.append(transport)

            def connection_lost(self, ex):
                self.logger.info('Lost connection from %s, %s', self.peername, ex)
                self.transport.close()
                self.iserver.asyncio_transports.remove(self.transport)
                self.processor.close()

            def data_received(self, data):
                logger.debug("received %s bytes from socket", len(data))
                if self.data:
                    data = self.data + data
                    self.data = b""
                self._process_data(data)

            def _process_data(self, data):
                buf = ua.utils.Buffer(data)
                while True:
                    try:
                        backup_buf = buf.copy()
                        try:
                            hdr = ua.Header.from_string(buf)
                        except ua.utils.NotEnoughData:
                            logger.info("We did not receive enough data from client, waiting for more")
                            self.data = backup_buf.read(len(backup_buf))
                            return
                        if len(buf) < hdr.body_size:
                            logger.info("We did not receive enough data from client, waiting for more")
                            self.data = backup_buf.read(len(backup_buf))
                            return
                        ret = self.processor.process(hdr, buf)
                        if not ret:
                            logger.info("processor returned False, we close connection from %s", self.peername)
                            self.transport.close()
                            return
                        if len(buf) == 0:
                            return
                    except Exception:
                        logger.exception("Exception raised while parsing message from client, closing")
                        return

        coro = self.loop.create_server(OPCUAProtocol, self.hostname, self.port)
        self._server = self.loop.run_coro_and_wait(coro)
        # get the port and the hostname from the created server socket
        # only relevant for dynamic port asignment (when self.port == 0)
        if self.port == 0 and len(self._server.sockets) == 1:
            # will work for AF_INET and AF_INET6 socket names
            # these are to only families supported by the create_server call
            sockname = self._server.sockets[0].getsockname()
            self.hostname = sockname[0]
            self.port = sockname[1]
        print('Listening on {0}:{1}'.format(self.hostname, self.port))

    def stop(self):
        self.logger.info("Closing asyncio socket server")
        for transport in self.iserver.asyncio_transports:
            transport.close()
        self.loop.call_soon(self._server.close)
        self.loop.run_coro_and_wait(self._server.wait_closed())
