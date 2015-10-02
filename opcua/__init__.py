"""
Pure Python OPC-UA library
"""

# the order is important! som classes must be overriden
from opcua.binary_client import BinaryClient
import opcua.uaprotocol as ua
from opcua.node import Node
from opcua.node import create_object
from opcua.node import create_folder
from opcua.node import create_variable
from opcua.node import create_property
from opcua.node import create_method
from opcua.node import call_method
from opcua.attribute_ids import AttributeIds
from opcua.object_ids import ObjectIds
from opcua.event import Event
from opcua.subscription import Subscription
from opcua.client import Client
from opcua.server import Server
from opcua.instanciate import instanciate_node


# next we have some methods which should really be moved somewhere else

def uamethod(func):
    """
    Method decorator to automatically convert
    arguments and output to and from variants
    """
    def wrapper(parent, *args):
        if isinstance(parent, ua.NodeId):
            result = func(parent, *[arg.Value for arg in args])
        else:
            self = parent
            parent = args[0]
            args = args[1:]
            result = func(self, parent, *[arg.Value for arg in args])

        return to_variant(result)
    return wrapper


def to_variant(*args):
    uaargs = []
    for arg in args:
        uaargs.append(ua.Variant(arg))
    return uaargs


