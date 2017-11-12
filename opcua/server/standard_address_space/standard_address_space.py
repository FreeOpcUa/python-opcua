
import os.path

import opcua

from opcua.server.standard_address_space.standard_address_space_part3 import create_standard_address_space_Part3
from opcua.server.standard_address_space.standard_address_space_part4 import create_standard_address_space_Part4
from opcua.server.standard_address_space.standard_address_space_part5 import create_standard_address_space_Part5
from opcua.server.standard_address_space.standard_address_space_part8 import create_standard_address_space_Part8
from opcua.server.standard_address_space.standard_address_space_part9 import create_standard_address_space_Part9
from opcua.server.standard_address_space.standard_address_space_part10 import create_standard_address_space_Part10
from opcua.server.standard_address_space.standard_address_space_part11 import create_standard_address_space_Part11
from opcua.server.standard_address_space.standard_address_space_part13 import create_standard_address_space_Part13

class PostponeReferences(object):
    def __init__(self, server):
        self.server = server
        self.postponed = None
        self.add_nodes = self.server.add_nodes

    def add_references(self, refs):
        self.postponed.extend(self.server.try_add_references(refs))
        # no return

    def __enter__(self):
        self.postponed = []
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None and exc_val is None:
            remaining = list(self.server.try_add_references(self.postponed))
            assert len(remaining) == 0, remaining

def fill_address_space(nodeservice):
    with PostponeReferences(nodeservice) as server:
        create_standard_address_space_Part3(server)
        create_standard_address_space_Part4(server)
        create_standard_address_space_Part5(server)
        create_standard_address_space_Part8(server)
        create_standard_address_space_Part9(server)
        create_standard_address_space_Part10(server)
        create_standard_address_space_Part11(server)
        create_standard_address_space_Part13(server)
        assert len(server.postponed) == 1561, len(server.postponed)
