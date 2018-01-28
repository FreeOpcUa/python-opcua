
import asyncio
import logging
from opcua.common.connection import SecureConnection
from opcua.ua.async_ua_binary import header_from_binary
from opcua import ua

logger = logging.getLogger('opcua.uaprotocol')


class AsyncSecureConnection(SecureConnection):
    """
    Async version of SecureConnection
    """

    async def receive_from_socket(self, protocol):
        """
        Convert binary stream to OPC UA TCP message (see OPC UA
        specs Part 6, 7.1: Hello, Acknowledge or ErrorMessage), or a Message
        object, or None (if intermediate chunk is received)
        """
        logger.debug("Waiting for header")
        header = await header_from_binary(protocol)
        logger.info("received header: %s", header)
        body = await protocol.read(header.body_size)
        if len(body) != header.body_size:
            # ToDo: should never happen since UASocketProtocol.read() waits until `size` bytes are received. Remove?
            raise ua.UaError("{0} bytes expected, {1} available".format(header.body_size, len(body)))
        return self.receive_from_header_and_body(header, ua.utils.Buffer(body))
