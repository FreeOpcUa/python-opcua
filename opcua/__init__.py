"""
Pure Python OPC-UA library
"""

from opcua.client.binary_client import BinaryClient
from opcua.common.node import Node
from opcua.common.node import create_object
from opcua.common.node import create_folder
from opcua.common.node import create_variable
from opcua.common.node import create_property
from opcua.common.node import create_method
from opcua.common.node import call_method
from opcua.common.event import Event
from opcua.common.subscription import Subscription
from opcua.client.client import Client
from opcua.server.server import Server
from opcua.common.instanciate import instanciate_node
from opcua.ua import ObjectIds
from opcua.ua import AttributeIds
from opcua.ua import StatusCodes


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


