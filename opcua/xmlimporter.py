"""
Generate address space c++ code from xml file specification
"""
import sys
import logging

import xml.etree.ElementTree as ET

from opcua import ua


class ObjectStruct(object):

    def __init__(self):
        self.nodetype = None
        self.nodeid = None
        self.browsename = None
        self.displayname = None
        self.symname = None
        self.parent = None
        self.parentlink = None
        self.desc = ""
        self.typedef = None
        self.refs = []
        self.nodeclass = None
        self.eventnotifier = 0

        # variable
        self.datatype = None
        self.rank = -1  # check default value
        self.value = []
        self.valuetype = None
        self.dimensions = None
        self.accesslevel = None
        self.useraccesslevel = None
        self.minsample = None

        # referencetype
        self.inversename = ""
        self.abstract = "false"
        self.symmetric = "false"

        # datatype
        self.definition = []

        # types


class RefStruct(object):

    def __init__(self):
        self.reftype = None
        self.forward = True
        self.target = None


class XmlImporter(object):

    def __init__(self, server):
        self.logger = logging.getLogger(__name__)
        self.server = server
        self.aliases = {}

    def import_xml(self, xmlpath):
        self.logger.info("Importing XML file {}".format(xmlpath))
        tree = ET.parse(xmlpath)
        root = tree.getroot()
        for child in root:
            if child.tag[51:] == 'UAObject':
                node = self.parse_node(child)
                self.make_object_code(node)
            elif child.tag[51:] == 'UAObjectType':
                node = self.parse_node(child)
                self.make_object_type_code(node)
            elif child.tag[51:] == 'UAVariable':
                node = self.parse_node(child)
                self.make_variable_code(node)
            elif child.tag[51:] == 'UAVariableType':
                node = self.parse_node(child)
                self.make_variable_type_code(node)
            elif child.tag[51:] == 'UAReferenceType':
                node = self.parse_node(child)
                self.make_reference_code(node)
            elif child.tag[51:] == 'UADataType':
                node = self.parse_node(child)
                self.make_datatype_code(node)
            elif child.tag[51:] == 'UAMethod':
                node = self.parse_node(child)
                self.make_method_code(node)
            elif child.tag[51:] == 'Aliases':
                for el in child:
                    self.aliases[el.attrib["Alias"]] = el.text
            else:
                sys.stderr.write("Not implemented node type: " + child.tag[51:] + "\n")

    def parse_node(self, child):
        obj = ObjectStruct()
        obj.nodetype = child.tag[53:]
        for key, val in child.attrib.items():
            if key == "NodeId":
                obj.nodeid = val
            elif key == "BrowseName":
                obj.browsename = val
            elif key == "SymbolicName":
                obj.symname = val
            elif key == "ParentNodeId":
                obj.parent = val
            elif key == "DataType":
                obj.datatype = val
            elif key == "IsAbstract":
                obj.abstract = val
            elif key == "EventNotifier":
                obj.eventnotifier = True if val == "true" else False
            elif key == "ValueRank":
                obj.rank = int(val)
            elif key == "ArrayDimensions":
                obj.dimensions = [int(i) for i in val.split(",")]
            elif key == "MinimumSamplingInterval":
                obj.minsample = int(val)
            elif key == "AccessLevel":
                obj.accesslevel = int(val)
            elif key == "UserAccessLevel":
                obj.useraccesslevel = int(val)
            elif key == "Symmetric":
                obj.symmetric = True if val == "true" else False
            else:
                sys.stderr.write("Attribute not implemented: " + key + " " + val + "\n")

        obj.displayname = obj.browsename  # FIXME
        for el in child:
            tag = el.tag[51:]

            if tag == "DisplayName":
                obj.displayname = el.text
            elif tag == "Description":
                obj.desc = el.text
            elif tag == "References":
                for ref in el:
                    if ref.attrib["ReferenceType"] == "HasTypeDefinition":
                        obj.typedef = ref.text
                    elif "IsForward" in ref.attrib and ref.attrib["IsForward"] == "false":
                        # if obj.parent:
                            #sys.stderr.write("Parent is already set with: "+ obj.parent + " " + ref.text + "\n")
                        obj.parent = ref.text
                        obj.parentlink = ref.attrib["ReferenceType"]
                    else:
                        struct = RefStruct()
                        if "IsForward" in ref.attrib:
                            struct.forward = ref.attrib["IsForward"]
                        struct.target = ref.text
                        struct.reftype = ref.attrib["ReferenceType"]
                        obj.refs.append(struct)
            elif tag == "Value":
                for val in el:
                    ntag = val.tag[47:]
                    obj.valuetype = ntag
                    if ntag in ("Int32", "UInt32"):
                        obj.value.append(int(val.text))
                    elif ntag in ('ByteString', 'String'):
                        mytext = val.text.replace('\n', '').replace('\r', '')
                        obj.value.append('b"{}"'.format(mytext))
                    elif ntag == "ListOfExtensionObject":
                        pass
                    elif ntag == "ListOfLocalizedText":
                        pass
                    else:
                        self.logger.warning("Missing type: %s", ntag)
            elif tag == "InverseName":
                obj.inversename = el.text
            elif tag == "Definition":
                for field in el:
                    obj.definition.append(field)
            else:
                sys.stderr.write("Not implemented tag: " + str(el) + "\n")
        return obj

    def _get_node(self, obj):
        node = ua.AddNodesItem()
        node.RequestedNewNodeId = ua.NodeId.from_string(obj.nodeid)
        node.BrowseName = ua.QualifiedName.from_string(obj.browsename)
        node.NodeClass = getattr(ua.NodeClass, obj.nodetype)
        if obj.parent:
            node.ParentNodeId = ua.NodeId.from_string(obj.parent)
        if obj.parent:
            node.ReferenceTypeId = self.to_ref_type(obj.parentlink)
        if obj.typedef:
            node.TypeDefinition = ua.NodeId.from_string(obj.typedef)
        return node

    def to_data_type(self, nodeid):
        if not nodeid:
            return ua.NodeId(ua.ObjectIds.String)
        if "=" in nodeid:
            return ua.NodeId.from_string(nodeid)
        else:
            return ua.NodeId(getattr(ua.ObjectIds, nodeid))

    def to_ref_type(self, nodeid):
        if "=" not in nodeid:
            nodeid = self.aliases[nodeid]
        return ua.NodeId.from_string(nodeid)

    def make_object_code(self, obj):
        node = self._get_node(obj)
        attrs = ua.ObjectAttributes()
        if obj.desc:
            attrs.Description = ua.LocalizedText(obj.desc)
        attrs.DisplayName = ua.LocalizedText(obj.displayname)
        attrs.EventNotifier = obj.eventnotifier
        node.NodeAttributes = attrs
        self.server.add_nodes([node])
        self._add_refs(obj)

    def make_object_type_code(self, obj):
        node = self._get_node(obj)
        attrs = ua.ObjectTypeAttributes()
        if obj.desc:
            attrs.Description = ua.LocalizedText(obj.desc)
        attrs.DisplayName = ua.LocalizedText(obj.displayname)
        attrs.IsAbstract = obj.abstract
        node.NodeAttributes = attrs
        self.server.add_nodes([node])
        self._add_refs(obj)

    def make_variable_code(self, obj):
        node = self._get_node(obj)
        attrs = ua.VariableAttributes()
        if obj.desc:
            attrs.Description = ua.LocalizedText(obj.desc)
        attrs.DisplayName = ua.LocalizedText(obj.displayname)
        attrs.DataType = self.to_data_type(obj.datatype)
        if obj.value and len(obj.value) == 1:
            attrs.Value = ua.Variant(obj.value[0], getattr(ua.VariantType, obj.valuetype))
        if obj.rank:
            attrs.ValueRank = obj.rank
        if obj.accesslevel:
            attrs.AccessLevel = obj.accesslevel
        if obj.useraccesslevel:
            attrs.UserAccessLevel = obj.useraccesslevel
        if obj.minsample:
            attrs.MinimumSamplingInterval = obj.minsample
        if obj.dimensions:
            attrs.ArrayDimensions = obj.dimensions
        node.NodeAttributes = attrs
        self.server.add_nodes([node])
        self._add_refs(obj)

    def make_variable_type_code(self, obj):
        node = self._get_node(obj)
        attrs = ua.VariableTypeAttributes()
        if obj.desc:
            attrs.Description = ua.LocalizedText(obj.desc)
        attrs.DisplayName = ua.LocalizedText(obj.displayname)
        attrs.DataType = self.to_data_type(obj.datatype)
        if obj.value and len(obj.value) == 1:
            attrs.Value = obj.value[0]
        if obj.rank:
            attrs.ValueRank = obj.rank
        if obj.abstract:
            attrs.IsAbstract = obj.abstract
        if obj.dimensions:
            attrs.ArrayDimensions = obj.dimensions
        node.NodeAttributes = attrs
        self.server.add_nodes([node])
        self._add_refs(obj)

    def make_method_code(self, obj):
        node = self._get_node(obj)
        attrs = ua.MethodAttributes()
        if obj.desc:
            attrs.Description = ua.LocalizedText(obj.desc)
        attrs.DisplayName = ua.LocalizedText(obj.displayname)
        if obj.accesslevel:
            attrs.AccessLevel = obj.accesslevel
        if obj.useraccesslevel:
            attrs.UserAccessLevel = obj.useraccesslevel
        if obj.minsample:
            attrs.MinimumSamplingInterval = obj.minsample
        if obj.dimensions:
            attrs.ArrayDimensions = obj.dimensions
        node.NodeAttributes = attrs
        self.server.add_nodes([node])
        self._add_refs(obj)

    def make_reference_code(self, obj):
        node = self._get_node(obj)
        attrs = ua.ReferenceTypeAttributes()
        if obj.desc:
            attrs.Description = ua.LocalizedText(obj.desc)
        attrs.DisplayName = ua.LocalizedText(obj.displayname)
        if obj. inversename:
            attrs.InverseName = ua.LocalizedText(obj.inversename)
        if obj.abstract:
            attrs.IsAbstract = obj.abstract
        if obj.symmetric:
            attrs.Symmetric = obj.symmetric
        node.NodeAttributes = attrs
        self.server.add_nodes([node])
        self._add_refs(obj)

    def make_datatype_code(self, obj):
        node = self._get_node(obj)
        attrs = ua.DataTypeAttributes()
        if obj.desc:
            attrs.Description = ua.LocalizedText(obj.desc)
        attrs.DisplayName = ua.LocalizedText(obj.displayname)
        if obj.abstract:
            attrs.IsAbstract = obj.abstract
        node.NodeAttributes = attrs
        self.server.add_nodes([node])
        self._add_refs(obj)

    def _add_refs(self, obj):
        if not obj.refs:
            return
        refs = []
        for data in obj.refs:
            ref = ua.AddReferencesItem()
            ref.IsForward = True
            ref.ReferenceTypeId = self.to_ref_type(data.reftype)
            ref.SourceNodeId = ua.NodeId.from_string(obj.nodeid)
            ref.TargetNodeClass = ua.NodeClass.DataType
            ref.TargetNodeId = ua.NodeId.from_string(data.target)
            refs.append(ref)
        self.server.add_references(refs)
