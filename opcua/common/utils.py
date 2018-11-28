"""
Helper function and classes that do not rely on opcua library.
Helper function and classes depending on ua object are in ua_utils.py
"""

import logging
import os
from concurrent.futures import Future
import functools
import threading
from socket import error as SocketError
from collections import MutableMapping

try:
    import asyncio
except ImportError:
    import trollius as asyncio


from opcua.ua.uaerrors import UaError


class ServiceError(UaError):
    def __init__(self, code):
        super(ServiceError, self).__init__('UA Service Error')
        self.code = code


class NotEnoughData(UaError):
    pass


class SocketClosedException(UaError):
    pass


class Buffer(object):

    """
    alternative to io.BytesIO making debug easier
    and added a few conveniance methods
    """

    def __init__(self, data, start_pos=0, size=-1):
        # self.logger = logging.getLogger(__name__)
        self._data = data
        self._cur_pos = start_pos
        if size == -1:
            size = len(data) - start_pos
        self._size = size

    def __str__(self):
        return "Buffer(size:{0}, data:{1})".format(
            self._size,
            self._data[self._cur_pos:self._cur_pos + self._size])
    __repr__ = __str__

    def __len__(self):
        return self._size

    def read(self, size):
        """
        read and pop number of bytes for buffer
        """
        if size > self._size:
            raise NotEnoughData("Not enough data left in buffer, request for {0}, we have {1}".format(size, self))
        # self.logger.debug("Request for %s bytes, from %s", size, self)
        self._size -= size
        pos = self._cur_pos
        self._cur_pos += size
        data = self._data[pos:self._cur_pos]
        # self.logger.debug("Returning: %s ", data)
        return data

    def copy(self, size=-1):
        """
        return a shadow copy, optionnaly only copy 'size' bytes
        """
        if size == -1 or size > self._size:
            size = self._size
        return Buffer(self._data, self._cur_pos, size)

    def skip(self, size):
        """
        skip size bytes in buffer
        """
        if size > self._size:
            raise NotEnoughData("Not enough data left in buffer, request for {0}, we have {1}".format(size, self))
        self._size -= size
        self._cur_pos += size


class SocketWrapper(object):
    """
    wrapper to make it possible to have same api for
    normal sockets, socket from asyncio, StringIO, etc....
    """

    def __init__(self, sock):
        self.socket = sock

    def read(self, size):
        """
        Receive up to size bytes from socket
        """
        data = b''
        while size > 0:
            try:
                chunk = self.socket.recv(size)
            except (OSError, SocketError) as ex:
                raise SocketClosedException("Server socket has closed", ex)
            if not chunk:
                raise SocketClosedException("Server socket has closed")
            data += chunk
            size -= len(chunk)
        return data

    def write(self, data):
        self.socket.sendall(data)


def create_nonce(size=32):
    return os.urandom(size)


class ThreadLoop(threading.Thread):
    """
    run an asyncio loop in a thread
    """

    def __init__(self):
        threading.Thread.__init__(self)
        self.logger = logging.getLogger(__name__)
        self.loop = None
        self._cond = threading.Condition()

    def start(self):
        with self._cond:
            threading.Thread.start(self)
            self._cond.wait()

    def run(self):
        self.logger.debug("Starting subscription thread")
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        with self._cond:
            self._cond.notify_all()
        self.loop.run_forever()
        self.logger.debug("subscription thread ended")

    def create_server(self, proto, hostname, port):
        return self.loop.create_server(proto, hostname, port)

    def stop(self):
        """
        stop subscription loop, thus the subscription thread
        """
        self.loop.call_soon_threadsafe(self.loop.stop)

    def close(self):
        self.loop.close()
        self.loop = None

    def call_soon(self, callback):
        self.loop.call_soon_threadsafe(callback)

    def call_later(self, delay, callback):
        """
        threadsafe call_later from asyncio
        """
        p = functools.partial(self.loop.call_later, delay, callback)
        self.loop.call_soon_threadsafe(p)

    def _create_task(self, future, coro, cb=None):
        #task = self.loop.create_task(coro)
        task = asyncio.ensure_future(coro, loop=self.loop) 
        if cb:
            task.add_done_callback(cb)
        future.set_result(task)

    def create_task(self, coro, cb=None):
        """
        threadsafe create_task from asyncio
        """
        future = Future()
        p = functools.partial(self._create_task, future, coro, cb)
        self.loop.call_soon_threadsafe(p)
        return future.result()

    def run_coro_and_wait(self, coro):
        cond = threading.Condition()
        def cb(_):
            with cond:
                cond.notify_all()
        with cond:
            task = self.create_task(coro, cb)
            cond.wait()
        return task.result()

    def _run_until_complete(self, future, coro):
        task = self.loop.run_until_complete(coro)
        future.set_result(task)

    def run_until_complete(self, coro):
        """
        threadsafe run_until_completed from asyncio
        """
        future = Future()
        p = functools.partial(self._run_until_complete, future, coro)
        self.loop.call_soon_threadsafe(p)
        return future.result()


class ThreadSafeDict(MutableMapping):

    def __init__(self, cache=None):
        self._lock = cache._lock if hasattr(cache, '_lock') else threading.RLock()  # FIXME: should use multiple reader, one writter pattern
        if cache is None:
            self._cache = {}
        else:
            assert(isinstance(cache, (dict, ThreadSafeDict)))
            self._cache = cache

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._cache = None

    def __getitem__(self, key):
        with self._lock:
            return self._cache.__getitem__(key)

    def get(self, key, value=None):
        with self._lock:
            return self._cache.get(key, value)

    def __setitem__(self, key, value):
        with self._lock:
            return self._cache.__setitem__(key, value)

    def __contains__(self, key):
        with self._lock:
            return self._cache.__contains__(key)

    def __delitem__(self, key):
        with self._lock:
            del self._cache[key]

    def __iter__(self):
        with self._lock:
            return self._cache.__iter__()

    def __len__(self):
        return len(self._cache)

    def keys(self):
        with self._lock:
            return self._cache.keys()

    def empty(self):
        with self._lock:
            self._cache = {}
