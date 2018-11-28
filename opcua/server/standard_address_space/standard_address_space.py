
import os.path

from opcua import ua

from opcua.server.standard_address_space.standard_address_space_part3 import create_standard_address_space_Part3
from opcua.server.standard_address_space.standard_address_space_part4 import create_standard_address_space_Part4
from opcua.server.standard_address_space.standard_address_space_part5 import create_standard_address_space_Part5
from opcua.server.standard_address_space.standard_address_space_part8 import create_standard_address_space_Part8
from opcua.server.standard_address_space.standard_address_space_part9 import create_standard_address_space_Part9
from opcua.server.standard_address_space.standard_address_space_part10 import create_standard_address_space_Part10
from opcua.server.standard_address_space.standard_address_space_part11 import create_standard_address_space_Part11
from opcua.server.standard_address_space.standard_address_space_part13 import create_standard_address_space_Part13

class PostponeReferences(object):
    def __init__(self, nodeservice):
        self.nodeservice = nodeservice
        self.postponed_refs = None
        self.postponed_nodes = None
        #self.add_nodes = self.server.add_nodes

    def add_nodes(self,nodes):
        self.postponed_nodes.extend(self.nodeservice.try_add_nodes(nodes, check=False))

    def add_references(self, refs):
        self.postponed_refs.extend(self.nodeservice.try_add_references(refs))
        # no return

    def __enter__(self):
        self.postponed_refs = []
        self.postponed_nodes = []
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None and exc_val is None:
            remaining_nodes = list(self.nodeservice.try_add_nodes(self.postponed_nodes, check=False))
            assert len(remaining_nodes) == 0, remaining_nodes
            remaining_refs = list(self.nodeservice.try_add_references(self.postponed_refs))
            assert len(remaining_refs) == 0, remaining_refs

def _address_space_fixes(nodeservice):
    """
    Looks like the xml definition of address space has some error. This is a good place to fix them
    """
    
    it = ua.AddReferencesItem()
    it.SourceNodeId = ua.NodeId(ua.ObjectIds.BaseObjectType)
    it.ReferenceTypeId = ua.NodeId(ua.ObjectIds.Organizes)
    it.IsForward = False
    it.TargetNodeId = ua.NodeId(ua.ObjectIds.ObjectTypesFolder)
    it.TargetNodeClass = ua.NodeClass.Object
    
    it2 = ua.AddReferencesItem()
    it2.SourceNodeId = ua.NodeId(ua.ObjectIds.BaseDataType)
    it2.ReferenceTypeId = ua.NodeId(ua.ObjectIds.Organizes)
    it2.IsForward = False
    it2.TargetNodeId = ua.NodeId(ua.ObjectIds.DataTypesFolder)
    it2.TargetNodeClass = ua.NodeClass.Object
    
    results = nodeservice.add_references([it, it2])

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

    _address_space_fixes(nodeservice)
