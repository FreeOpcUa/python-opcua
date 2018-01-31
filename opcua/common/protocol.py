
import asyncio


class UASocketProtocol(asyncio.Protocol):
    """
    Handle socket connection and send ua messages.
    Timeout is the timeout used while waiting for an ua answer from server.
    """

    def __init__(self, timeout=1, security_policy=ua.SecurityPolicy()):
        self.logger = logging.getLogger(__name__ + ".UASocketProtocol")
        self.loop = asyncio.get_event_loop()
        self.transport = None
        self.receive_buffer = asyncio.Queue()
        self.is_receiving = False
        self.timeout = timeout
        self.authentication_token = ua.NodeId()
        self._request_id = 0
        self._request_handle = 0
        self._callbackmap = {}
        self._connection = SecureConnection(security_policy)
        self._leftover_chunk = None

    def connection_made(self, transport: asyncio.Transport):
        self.transport = transport

    def connection_lost(self, exc):
        self.logger.info("Socket has closed connection")
        self.transport = None

    def data_received(self, data: bytes):
        self.receive_buffer.put_nowait(data)
        if not self.is_receiving:
            self.is_receiving = True
            self.loop.create_task(self._receive())

    async def read(self, size: int):
        """Receive up to size bytes from socket."""
        data = b''
        self.logger.debug('read %s bytes from socket', size)
        while size > 0:
            self.logger.debug('data is now %s, waiting for %s bytes', len(data), size)
            # ToDo: abort on timeout, socket close
            # raise SocketClosedException("Server socket has closed")
            if self._leftover_chunk:
                self.logger.debug('leftover bytes %s', len(self._leftover_chunk))
                # use leftover chunk first
                chunk = self._leftover_chunk
                self._leftover_chunk = None
            else:
                chunk = await self.receive_buffer.get()
            self.logger.debug('got chunk %s needed_length is %s', len(chunk), size)
            if len(chunk) <= size:
                _chunk = chunk
            else:
                # chunk is too big
                _chunk = chunk[:size]
                self._leftover_chunk = chunk[size:]
            data += _chunk
            size -= len(_chunk)
        return data
