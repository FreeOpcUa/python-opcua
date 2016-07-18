"""
Pure Python OPC-UA library
"""

from opcua.common.node import Node
from opcua.common.manage_nodes import create_folder
from opcua.common.manage_nodes import create_object
from opcua.common.manage_nodes import create_variable
from opcua.common.manage_nodes import create_object_type
from opcua.common.manage_nodes import create_variable_type
from opcua.common.manage_nodes import create_reference_type
from opcua.common.manage_nodes import create_data_type
from opcua.common.manage_nodes import create_property
from opcua.common.manage_nodes import create_method
from opcua.common.methods import call_method
# FIXME: ugly hack to avoid circular import issue and still split file
Node.add_folder = create_folder
Node.add_object = create_object
Node.add_variable = create_variable
Node.add_property = create_property
Node.add_method = create_method
Node.call_method = call_method
Node.add_data_type = create_data_type
Node.add_object_type = create_object_type
Node.add_variable_type = create_variable_type
Node.add_reference_type = create_reference_type

from opcua.common.methods import uamethod
from opcua.common.subscription import Subscription
from opcua.client.client import Client
from opcua.server.server import Server
from opcua.server.event_generator import EventGenerator
from opcua.common.instantiate import instantiate



