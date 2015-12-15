
cdef class Buffer(object):

    """
    alternative to io.BytesIO making debug easier
    and added a few conveniance methods
    """
    cdef public bytes data
    cdef int rsize
    def __init__(self, bytes data):
        # self.logger = logging.getLogger(__name__)
        self.data = data
        self.rsize = 0

    def __str__(self):
        return "Buffer(size:{}, data:{})".format(len(self.data), self.data)
    __repr__ = __str__

    def __len__(self):
        return len(self.data) - self.rsize

    def read(self, int size):
        """
        read and pop number of bytes for buffer
        """
        cdef int rsize, nrsize
        rsize = self.rsize
        if size < 0:
            return self.data[rsize:]
        nrsize = rsize + size
        if nrsize > len(self.data):
            raise Exception("Not enough data left in buffer, request for {}, we have {}".format(size, self))
        #self.logger.debug("Request for %s bytes, from %s", size, self)
        data = self.data[rsize:nrsize]
        self.rsize = nrsize
        #self.logger.debug("Returning: %s ", data)
        return data

    def copy(self, size=None):
        """
        return a copy, optionnaly only copy 'size' bytes
        """
        if size is None:
            return Buffer(self.data[self.rsize:])
        else:
            return Buffer(self.data[self.rsize:self.rsize + size])

    def test_read(self, size):
        """
        read 'size' bytes from buffer, without removing them from buffer
        """
        if size > len(self.data):
            raise Exception("Not enough data left in buffer, request for {}, we have {}".format(size, self))
        return self.data[:size]