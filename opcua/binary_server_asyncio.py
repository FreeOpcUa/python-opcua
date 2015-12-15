"""
Socket server forwarding request to internal server
"""
import logging
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
            logger = self.logger

            def connection_made(self, transport):
                self.peername = transport.get_extra_info('peername')
                self.logger.info('New connection from %s', self.peername)
                self.transport = transport
                self.processor = UAProcessor(self.iserver, self.transport)
                self.data = b""

            def connection_lost(self, ex):
                self.logger.info('Lost connection from %s, %s', self.peername, ex)
                self.transport.close()
                self.processor.close()

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
                            logger.warning("We did not receive enough data from server, waiting for more")
                            self.data = data
                            return
                        ret = self.processor.process(hdr, buf)
                        if not ret:
                            logger.warning("processor returned False, we close connection from %s", self.peername)
                            self.transport.close()
                            return
                        if len(data) <= hdr.packet_size:
                            return
                        data = data[hdr.packet_size:]
                    except ua.utils.NotEnoughData:
                        logger.warning("Not a complete packet in data from client, waiting for more data")
                        self.data = buf.data
                        break
                    except Exception:
                        logger.exception("Exception raised while parsing message from client, closing")
                        self.transport.close()
                        break

        coro = self.loop.create_server(OPCUAProtocol, self.hostname, self.port)
        self._server = self.loop.run_coro_and_wait(coro)
        print('Listening on {}:{}'.format(self.hostname, self.port))

    def stop(self):
        self.logger.info("Closing asyncio socket server")
        self.loop.call_soon(self._server.close)
        self.loop.run_coro_and_wait(self._server.wait_closed())
