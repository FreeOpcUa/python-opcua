"""
add node defined in XML to address space
format is the one from opc-ua specification
"""
import logging


from opcua import ua
from opcua import xmlparser


class XmlImporter(object):

    def __init__(self, server):
        self.logger = logging.getLogger(__name__)
        self.parser = None
        self.server = server

    def import_xml(self, xmlpath):
        self.logger.info("Importing XML file %s", xmlpath)
        self.parser = xmlparser.XMLParser(xmlpath)
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
        # if obj.value and len(obj.value) == 1:
        if obj.value is not None:
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
