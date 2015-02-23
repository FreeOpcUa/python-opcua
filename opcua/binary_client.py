"""
Low level binary client
"""
import io
import logging
import socket
from threading import Thread

from . import uaprotocol as ua


class BinaryClient(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.socket = None
        self._do_stop = False
        self._security_token = ua.ChannelSecurityToken()
        self._sequence_number = 0
        self._authentication_token = ua.AnonymousIdentityToken()
        self._request_handle = 0

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
        header = ua.Header(ua.MessageType.Hello, ua.ChunkType.Single)
        self._write_socket(header, hello)
        header = self._recv_header()
        data = self.socket.recv(header.Size)
        return  ua.Acknowledge.from_binary(io.BytesIO(data))
    
    def _write_socket(self, hdr, *args):
        alle = []
        for arg in args:
            data = arg.to_binary()
            hdr.add_size(len(data))
            alle.append(data)
        alle.insert(0, hdr.to_binary())
        for obj in alle:
            self.socket.send(obj)

    def open_secure_channel(self, params):
        request = ua.OpenSecureChannelRequest()
        request.Parameters = params

        response = self._send(request)

        header = self._recv_header()
        data = self.socket.recv(header.Size)
        return  io.BytesIO(data)

    def _send(self, request):
        request.RequestHeader = self._create_request_header()
        def callback():
            pass
        clb = callback
        self._send_async(request, clb)

    def _send_async(self, request, callback):
        hdr = ua.SecureHeader(ua.MessageType.SecureMessage, ua.ChunkType.Single, self._security_token.TokenId)
        symhdr = self._create_algo_header()
        seqhdr = self._create_sequence_header()
        request = request.to_binary()

        self._write_socket(hdr, symhdr, seqhdr, request)


    def _create_request_header(self):
        hdr = ua.RequestHeader()
        hdr.AuthenticationToken = self._authentication_token
        self._request_handle += 1
        hdr.RequestHandle = self._request_handle
        hdr.TimeoutHint = 10000
        return hdr

    def _create_algo_header(self):
        hdr = ua.SymmetricAlgorithmHeader()
        hdr.TokenId = self._security_token.TokenId
        return hdr

    def _create_sequence_header(self):
        hdr = ua.SequenceHeader()
        self._sequence_number += 1
        hdr.SequenceNumber = self._sequence_number
        return hdr

