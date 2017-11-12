import unittest
import os.path
import xml.etree.ElementTree as ET

from opcua import ua
from opcua.server.address_space import AddressSpace
from opcua.server.address_space import NodeManagementService
from opcua.server.standard_address_space import standard_address_space

def find_elem(parent, name, ns = None):
    if ns is None:
        try:
            return parent.find(parent.tag[0:parent.tag.index('}')+1]+name)
        except ValueError:
            return parent.find(name)
    return parent.find(ns+name)

def remove_elem(parent, name):
    e = find_elem(parent, name)
    if e is not None:
        parent.remove(e)

def try_apply(item, aliases):
    attrib = item.attrib
    for name in ('ReferenceType', 'DataType'):
        try:
            value  = attrib[name]
            attrib[name] = aliases[value]
        except KeyError:
            pass

def read_nodes(path):
    tree = ET.parse(path)
    root = tree.getroot()

    aliases_elem = find_elem(root, 'Aliases')
    aliases = dict( (a.attrib['Alias'], a.text) for a in aliases_elem)

    any(try_apply(i, aliases) for i in root.iter())
    root.remove(aliases_elem)

    remove_elem(root, "Models")
    remove_elem(root, "NamespaceUris")

    return dict((e.attrib['NodeId'],e) for e in root)

def get_refs(e):
    return set((r.attrib['ReferenceType'], r.text, r.attrib.get('IsForward', 'true') == 'true') for r in find_elem(e, 'References'))

class StandardAddressSpaceTests(unittest.TestCase):

    def setUp(self):
        self.aspace = AddressSpace()
        self.node_mgt_service = NodeManagementService(self.aspace)
        standard_address_space.fill_address_space(self.node_mgt_service)

    def test_std_address_space_references(self):
        std_nodes = read_nodes(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'schemas', 'Opc.Ua.NodeSet2.xml')))
        for k in self.aspace.keys():
            refs = set((r.ReferenceTypeId.to_string(), r.NodeId.to_string(), r.IsForward) for r in self.aspace[k].references)
            xml_refs = set((r.attrib['ReferenceType'], r.text, r.attrib.get('IsForward', 'true') == 'true') for r in find_elem(std_nodes[k.to_string()], 'References'))
            self.assertTrue(len(xml_refs-refs)==0)
