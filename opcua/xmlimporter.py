"""
Generate address space c++ code from xml file specification
"""
import logging
import re
import sys

import xml.etree.ElementTree as ET

from opcua import ua


class NodeData(object):

    def __init__(self):
        self.nodetype = None
        self.nodeid = None
        self.browsename = None
        self.displayname = None
        self.symname = None  # FIXME: this param is never used, why?
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


class RefStruct(object):

    def __init__(self):
        self.reftype = None
        self.forward = True
        self.target = None


class XMLParser(object):

    def __init__(self, xmlpath):
        self.logger = logging.getLogger(__name__)
        self._retag = re.compile(r"(\{.*\})(.*)")
        self.path = xmlpath
        self.aliases = {}

        self.tree = ET.parse(xmlpath)
        self.root = self.tree.getroot()
        self.iter = None

    def __iter__(self):
        self.iter = self.tree.iter()
        return self

    def __next__(self):
        while True:
            if sys.version_info[0] < 3:
                child = self.iter.next()
            else:
                child = self.iter.__next__()
            name = self._retag.match(child.tag).groups()[1]
            if name == "Aliases":
                for el in child:
                    self.aliases[el.attrib["Alias"]] = el.text
            else:
                node = self._parse_node(name, child)
                return node

    def next(self):  # support for python2
        return self.__next__() 

    def _parse_node(self, name, child):
        obj = NodeData()
        obj.nodetype = name 
        for key, val in child.attrib.items():
            self._set_attr(key, val, obj)
        obj.displayname = obj.browsename  # gice a default value to display name
        for el in child:
            self._parse_tag(el, obj)
        return obj

    def _set_attr(self, key, val, obj):
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
            self.logger.info("Attribute not implemented: %s:%s", key, val)

    def _parse_tag(self, el, obj):
        tag = self._retag.match(el.tag).groups()[1]

        if tag == "DisplayName":
            obj.displayname = el.text
        elif tag == "Description":
            obj.desc = el.text
        elif tag == "References":
            self._parse_refs(el, obj)
        elif tag == "Value":
            self._parse_value(el, obj)
        elif tag == "InverseName":
            obj.inversename = el.text
        elif tag == "Definition":
            for field in el:
                obj.definition.append(field)
        else:
            self.logger.info("Not implemented tag: %s", el)

    def _parse_value(self, el, obj):
        for val in el:
            ntag = self._retag.match(val.tag).groups()[1]
            obj.valuetype = ntag
            if ntag in ("Int32", "UInt32"):
                obj.value = int(val.text)
            elif ntag in ('ByteString', 'String'):
                mytext = val.text.replace('\n', '').replace('\r', '')
                #obj.value.append('b"{}"'.format(mytext))
                obj.value = mytext
            elif ntag == "ListOfExtensionObject":
                self.logger.info("Value type not implemented: %s", ntag)
            elif ntag == "ListOfLocalizedText":
                self.logger.info("Value type not implemented: %s", ntag)
            else:
                self.logger.info("Value type not implemented: %s", ntag)

    def _parse_refs(self, el, obj):
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



class XmlImporter(object):

    def __init__(self, server):
        self.logger = logging.getLogger(__name__)
        self.parser = None
        self.server = server

    def import_xml(self, xmlpath):
        self.logger.info("Importing XML file {}".format(xmlpath))
        self.parser = XMLParser(xmlpath)
        for node in self.parser:
            if node.nodetype == 'UAObject':
                self.add_object(node)
            elif node.nodetype == 'UAObjectType':
                self.add_object_type(node)
            elif node.nodetype == 'UAVariable':
                self.add_variable(node)
            elif node.nodetype == 'UAVariableType':
                self.add_variable_type(node)
            elif node.nodetype == 'UAReferenceType':
                self.add_reference(node)
            elif node.nodetype == 'UADataType':
                self.add_datatype(node)
            elif node.nodetype == 'UAMethod':
                self.add_method(node)
            else:
                self.logger.info("Not implemented node type: %s ", node.nodetype)

    def _get_node(self, obj):
        node = ua.AddNodesItem()
        node.RequestedNewNodeId = ua.NodeId.from_string(obj.nodeid)
        node.BrowseName = ua.QualifiedName.from_string(obj.browsename)
        node.NodeClass = getattr(ua.NodeClass, obj.nodetype[2:])
        if obj.parent:
            node.ParentNodeId = ua.NodeId.from_string(obj.parent)
        if obj.parentlink:
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
            if nodeid in self.parser.aliases:
                nodeid = self.parser.aliases[nodeid]
            else:
                nodeid = "i={}".format(getattr(ua.ObjectIds, nodeid))

        return ua.NodeId.from_string(nodeid)

    def add_object(self, obj):
        node = self._get_node(obj)
        attrs = ua.ObjectAttributes()
        if obj.desc:
            attrs.Description = ua.LocalizedText(obj.desc)
        attrs.DisplayName = ua.LocalizedText(obj.displayname)
        attrs.EventNotifier = obj.eventnotifier
        node.NodeAttributes = attrs
        self.server.add_nodes([node])
        self._add_refs(obj)

    def add_object_type(self, obj):
        node = self._get_node(obj)
        attrs = ua.ObjectTypeAttributes()
        if obj.desc:
            attrs.Description = ua.LocalizedText(obj.desc)
        attrs.DisplayName = ua.LocalizedText(obj.displayname)
        attrs.IsAbstract = obj.abstract
        node.NodeAttributes = attrs
        self.server.add_nodes([node])
        self._add_refs(obj)

    def add_variable(self, obj):
        node = self._get_node(obj)
        attrs = ua.VariableAttributes()
        if obj.desc:
            attrs.Description = ua.LocalizedText(obj.desc)
        attrs.DisplayName = ua.LocalizedText(obj.displayname)
        attrs.DataType = self.to_data_type(obj.datatype)
        #if obj.value and len(obj.value) == 1:
        if obj.value:
            attrs.Value = ua.Variant(obj.value, getattr(ua.VariantType, obj.valuetype))
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

    def add_variable_type(self, obj):
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

    def add_method(self, obj):
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

    def add_reference(self, obj):
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

    def add_datatype(self, obj):
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
