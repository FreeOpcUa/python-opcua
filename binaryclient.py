"""
Low level binary client
"""
import io
import logging
import socket
from threading import Thread

import uaprotocol as ua


class BinaryClient(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.socket = None
        self._do_stop = False

    def run(self):
        print("Thread started")
        while True:
            header = self._recv_header()
            body = self.socket.recv(header.Size)
            print("received body of size: ", len(body))

    def _recv_header(self):
        data = self.socket.recv(8)
        header = ua.Header.from_binary(io.BytesIO(data))
        print(header)
        return header

    def stop(self):
        self._do_stop = True

    def connect(self):
        print("opening connection")
        self.socket = socket.create_connection(('localhost', 4841))

    def send_hello(self, url):
        hello = ua.Hello()
        hello.EndpointUrl = url
        hello = hello.to_binary()
        header = ua.Header(ua.MessageType.Hello, ua.ChunkType.Single)
        header.Size += len(hello)
        header = header.to_binary()
        self.socket.send(header)
        self.socket.send(hello)
        header = self._recv_header()
        data = self.socket.recv(header.Size)
        return  ua.Acknowledge.from_binary(io.BytesIO(data))


if __name__ == "__main__": 
    from IPython import embed
    logging.basicConfig(level=logging.DEBUG)
    binclient = BinaryClient()
    binclient.connect()
    #binclient.start()
    ack = binclient.send_hello("opc.tcp://localhost:4841/freeopcua/server/")
    embed()
    #binclient.stop()
