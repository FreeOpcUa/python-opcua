import socket

def recv_all(socket, size):
    """
    Receive up to size bytes from socket
    """
    data = b''
    while size > 0:
        chunk = socket.recv(size)
        if not chunk:
            break
        data += chunk
        size -= len(chunk)
    return data
