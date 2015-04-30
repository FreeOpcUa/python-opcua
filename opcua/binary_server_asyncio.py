"""
Socket server forwarding request to internal server
"""
import logging
import functools
try:
    # we prefer to use bundles asyncio version, otherwise fallback to trollius
    import asyncio
except ImportError:
    import trollius as asyncio
    from trollius import From



from opcua import ua
from opcua.uaprocessor import UAProcessor

logger = logging.getLogger(__name__)


class BinaryServer(object):

    def __init__(self, internal_server, hostname, port):
        self.logger = logging.getLogger(__name__)
        self.hostname = hostname
        self.port = port
        self.iserver = internal_server
        self.loop = internal_server.loop
        self._server = None

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

            def connection_made(self, transport):
                self.peername = transport.get_extra_info('peername')
                print('New connection from {}'.format(self.peername))
                self.transport = transport
                self.processor = UAProcessor(self.iserver, self.transport, self.peername)
                self.data = b""

            def connection_lost(self, ex):
                print('Lost connection from ', self.peername, ex)
                self.transport.close()

            def data_received(self, data):
                logger.debug("received %s bytes from socket", len(data))
                if self.data:
                    data = self.data + data
                    self.data = b""
                self._process_data(data)

            def _process_data(self, data):
                while True:
                    try:
                        buf = ua.utils.Buffer(data[:])
                        hdr = ua.Header.from_string(buf)
                        if len(buf) < hdr.body_size:
                            logger.warn("We did not receive enough data from server, waiting for more")
                            self.data = data
                            return
                        ret = self.processor.process(hdr, buf)
                        if not ret:
                            logger.warn("processor returned False, we close connection")
                            self.transport.close()
                            return
                        if len(data) <= hdr.packet_size:
                            return
                        data  = data[hdr.packet_size:]
                    except utils.NotEnoughData:
                        logger.warn("Not a complete packet in data from client, waiting for more data")
                        self.data = buf.data
                        break
                    except Exception:
                        logger.exception("Exception raised while parsing message from client, closing")
                        self.transport.close()
                        break

        logger.warning("Listening on %s:%s", self.hostname, self.port)
        coro = self.loop.create_server(OPCUAProtocol, self.hostname, self.port)
        self._server = self.loop.run_coro_and_wait(coro)
        logger.warning('Listening on %s', self._server.sockets[0].getsockname())

    def stop(self):
        self.logger.warn("Closing asyncio socket server")
        self._server.close()
        self.loop.run_coro_and_wait(self._server.wait_closed())





