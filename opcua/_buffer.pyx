
cdef class Buffer(object):

    """
    alternative to io.BytesIO making debug easier
    and added a few conveniance methods
    """
    cdef bytes _data
    cdef int rsize, data_len
    def __init__(self, bytes data):
        self._data = data
        self.data_len  = len(data)
        self.rsize = 0

    def __str__(self):
        return "Buffer(size:{}, data:{})".format(self.data_len - self.rsize, self.data)
    __repr__ = __str__

    def __len__(self):
        return  self.data_len - self.rsize

    def read(self, int size):
        """
        read and pop number of bytes for buffer
        """
        cdef int rsize, nrsize
        rsize = self.rsize
        nrsize = rsize + size
        if nrsize > self.data_len:
            raise Exception("Not enough data left in buffer, request for {}, we have {}".format(size, self))
        data = self._data[rsize:nrsize]
        self.rsize = nrsize
        return data

    def copy(self, int size=-1):
        """
        return a copy, optionnaly only copy 'size' bytes
        """
        if size == -1:
            return Buffer(self._data[self.rsize:])
        else:
            return Buffer(self._data[self.rsize:self.rsize + size])

    def test_read(self, int size):
        """
        read 'size' bytes from buffer, without removing them from buffer
        """
        if size + self.rsize > self.data_len:
            raise Exception("Not enough data left in buffer, request for {}, we have {}".format(size, self))
        return self.data[self.rsize:self.rsize + size]

    property data:

        def __get__(self):
            return self._data[self.rsize:] 

        def __set__(self, v):
            self._data = v
            self.data_len  = len(v)
            self.rsize = 0
