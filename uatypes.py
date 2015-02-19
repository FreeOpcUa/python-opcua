"""
implement ua datatypes
"""

import uuid
import struct 

class Guid(object):
    def __init__(self):
        self.uuid = uuid.uuid4()

    def to_binary(self):
        return self.uuid.bytes 

    def from_binary(self, data):
        self.uuid = uuid.UUID(bytes=data.read(16))

class ByteString(object):
    def __init__(self):
        self.data = b""

    def to_binary(self):
        if not self.data:
            return struct.pack("!i", -1)
        size = len(self.data)
        data = struct.pack("!i", size)
        data += struct.pack("!{}B".format(size), *self.data)
        return data

    def from_binary(self, data):
        size = struct.unpack("!i", data.read(4))[0]
        self.data = struct.unpack("!{}c".format(size), data.read(size))
        self.data = b"".join(self.data)

class StatusCode(object):
    def __init__(self):
        self.data = b""

    def to_binary(self):
        return struct.pack("!I", self.data)
    
    def from_binary(self, data):
        self.data = struct.unpack("!I", data.read(4))[0]


if __name__ == "__main__":
    import io
    from IPython import embed
    bs = ByteString()
    g = Guid()
    sc = StatusCode()
    s = b"this is a test string"
    stream = io.BytesIO(s)
    bs.data = s
    d=bs.to_binary()
    print(d)
    bs.from_binary(io.BytesIO(d))
    embed()
