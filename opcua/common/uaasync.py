import sys

if sys.version_info[0] < 3 or sys.version_info[1] <= 2:
    # python 2.7 - python 3.2
    from trollius import coroutine, From, Return
    import trollius as asyncio
else:
    # python 3.3 or above
    from asyncio import coroutine
    import asyncio

    def From(*args, **kwargs):
        # we don't want anyone catch it using try: ... except Exception: ...
        raise BaseException("'yield from' shoud be used, not yield From()")

    class Return(BaseException):
        pass

import threading
try:
    from threading import get_ident as _get_thread_ident
except ImportError:
    # Python 2
    from threading import _get_ident as _get_thread_ident
import logging
from concurrent.futures import Future
from functools import wraps, partial
from .uaerrors import UAError

logger = logging.getLogger(__name__)


class LoopController(object):
    def __init__(self):
        self.loop = None
        self.external = False
        self.lock = threading.Lock()
        self.count = 0
        self.thread = None
        self.thread_id = None

    def install_loop(self, loop):
        with self.lock:
            if self.count > 0 or self.thread is not None or self.external is True:
                raise UAError("install_loop must be called before using the opcua library")
            self.loop = loop
            self.external = True

    def start_loop(self):
        if self.external:
            raise UAError("synchonized interface unavilable after install_loop()")
        with self.lock:
            if self.count > 0:
                self.count += 1
                return
            self._start_loop_thread()
            self.count = 1

    def stop_loop(self):
        if self.external:
            return
        with self.lock:
            if self.count < 1:
                return
            elif self.count > 1:
                self.count -= 1
                return
            self._stop_loop_thread()
            self.count = 0

    def _start_loop_thread(self):
        loop = asyncio.new_event_loop()
        cond = threading.Condition()
        thread = threading.Thread(target=self._loop_run, args=(loop, cond))
        thread.daemon = True
        with cond:
            thread.start()
            cond.wait()
        self.thread = thread
        self.loop = loop

    def _stop_loop_thread(self):
        self.loop.call_soon_threadsafe(self.loop.stop)
        self.thread.join(10)
        if self.thread.is_alive():
            raise UAError("can not stop loop thread")
        self.thread = None
        self.loop.close()
        self.loop = None

    def _loop_run(self, loop, cond):
        logger.info("start loop thread")
        self.thread_id = _get_thread_ident()
        with cond:
            cond.notify_all()
        del cond
        try:
            loop.run_forever()
        finally:
            self.thread_id = None
            logger.info("stop loop thread")

    def in_loop_thread(self):
        if self.thread_id is None:
            raise UAError("loop thread is not running")
        return self.thread_id == _get_thread_ident()


_ctrl = LoopController()


def install_loop(loop):
    _ctrl.install_loop(loop)


def get_loop():
    return _ctrl.loop


def start_loop():
    _ctrl.start_loop()


def stop_loop():
    _ctrl.stop_loop()


def new_future():
    return asyncio.Future(loop=_ctrl.loop)


def call_soon(*args):
    return _ctrl.loop.call_soon(*args)


def call_later(*args):
    return _ctrl.loop.call_later(*args)


def call_at(*args):
    return _ctrl.loop.call_at(*args)


def call_soon_threadsafe(*args):
    return _ctrl.loop.call_soon_threadsafe(*args)


def wait_for(*args):
    return asyncio.wait_for(*args, loop=_ctrl.loop)


def _transfer_future(dstfut, srcfut):
    if srcfut.cancelled():
        dstfut.cancel()
        return
    ex = srcfut.exception()
    if ex is not None:
        dstfut.set_exception(ex)
        return
    dstfut.set_result(srcfut.result())


def _wait_coro_in_loop(fut, coro, args, kwargs):
    task = asyncio.async(coro(*args, **kwargs), loop=_ctrl.loop)
    task.add_done_callback(partial(_transfer_future, fut))


def await_coro(coro, *args, **kwargs):
    if _ctrl.in_loop_thread():
        raise UAError("coro should not be called in loop thread")
    fut = Future()
    call_soon_threadsafe(_wait_coro_in_loop, fut, coro, args, kwargs)
    return fut.result()


def await_super_coro(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if _ctrl.in_loop_thread():
            raise UAError("coro %s should not be called in loop thread" % func.__name__)
        coro = getattr(super(self.__class__, self), func.__name__)
        fut = Future()
        call_soon_threadsafe(_wait_coro_in_loop, fut, coro, args, kwargs)
        return fut.result()
    return wrapper


def _wait_call_in_loop(fut, func, args, kwargs):
    try:
        rs = func(*args, **kwargs)
    except Exception as e:
        fut.set_exception(e)
    fut.set_result(rs)


def await_call(func, *args, **kwargs):
    if _ctrl.in_loop_thread():
        return func(*args, **kwargs)
    fut = Future()
    call_soon_threadsafe(_wait_call_in_loop, fut, func, args, kwargs)
    return fut.result()


def await_super_call(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        method = getattr(super(self.__class__, self), func.__name__)
        if _ctrl.in_loop_thread():
            return method(*args, **kwargs)
        fut = Future()
        call_soon_threadsafe(_wait_call_in_loop, fut, method, args, kwargs)
        return fut.result()
    return wrapper

__all__ = [
    "asyncio", "coroutine", "From", "Return",
    "install_loop", "get_loop", "start_loop", "stop_loop",
    "new_future", "call_soon", "call_soon_threadsafe",
    "call_later", "call_at", "wait_for",
    "await_coro", "await_super_coro",
    "await_call", "await_super_call",
]
