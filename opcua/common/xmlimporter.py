"""
add node defined in XML to address space
format is the one from opc-ua specification
"""
import logging


from opcua import ua
from opcua.common import xmlparser


class XmlImporter(object):

    def __init__(self, server):
        self.logger = logging.getLogger(__name__)
        self.parser = None
        self.server = server

    def import_xml(self, xmlpath, act_server):
        """
        import xml and return added nodes
        """
        self.logger.info("Importing XML file %s", xmlpath)
        self.parser = xmlparser.XMLParser(xmlpath, act_server)
        nodes = []
        for node in self.parser:
            if node.nodetype == 'UAObject':
                node = self.add_object(node)
            elif node.nodetype == 'UAObjectType':
                node = self.add_object_type(node)
            elif node.nodetype == 'UAVariable':
                node = self.add_variable(node)
            elif node.nodetype == 'UAVariableType':
                node = self.add_variable_type(node)
            elif node.nodetype == 'UAReferenceType':
                node = self.add_reference(node)
            elif node.nodetype == 'UADataType':
                node = self.add_datatype(node)
            elif node.nodetype == 'UAMethod':
                node = self.add_method(node)
            else:
                self.logger.info("Not implemented node type: %s ", node.nodetype)
            nodes.append(node)
        return nodes

    def _get_node(self, obj):
        node = ua.AddNodesItem()
        node.RequestedNewNodeId = ua.NodeId.from_string(obj.nodeid)
        node.BrowseName = ua.QualifiedName.from_string(obj.browsename)
        node.NodeClass = getattr(ua.NodeClass, obj.nodetype[2:])
        if obj.parent:
            node.ParentNodeId = ua.NodeId.from_string(obj.parent)
        if obj.parentlink:
            node.ReferenceTypeId = self.to_nodeid(obj.parentlink)
        if obj.typedef:
            node.TypeDefinition = ua.NodeId.from_string(obj.typedef)
        return node

    def to_nodeid(self, nodeid):
        if not nodeid:
            return ua.NodeId(ua.ObjectIds.String)
        elif "=" in nodeid:
            return ua.NodeId.from_string(nodeid)
        elif hasattr(ua.ObjectIds, nodeid):
            return ua.NodeId(getattr(ua.ObjectIds, nodeid))
        else:
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
        res = self.server.add_nodes([node])
        self._add_refs(obj)
        return res[0].AddedNodeId

    def add_object_type(self, obj):
        node = self._get_node(obj)
        attrs = ua.ObjectTypeAttributes()
        if obj.desc:
            attrs.Description = ua.LocalizedText(obj.desc)
        attrs.DisplayName = ua.LocalizedText(obj.displayname)
        attrs.IsAbstract = obj.abstract
        node.NodeAttributes = attrs
        res = self.server.add_nodes([node])
        self._add_refs(obj)
        return res[0].AddedNodeId

    def add_variable(self, obj):
        node = self._get_node(obj)
        attrs = ua.VariableAttributes()
        if obj.desc:
            attrs.Description = ua.LocalizedText(obj.desc)
        attrs.DisplayName = ua.LocalizedText(obj.displayname)
        attrs.DataType = self.to_nodeid(obj.datatype)
        # if obj.value and len(obj.value) == 1:
        if obj.value is not None:
            attrs.Value = self._add_variable_value(obj, )
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
        res = self.server.add_nodes([node])
        self._add_refs(obj)
        return res[0].AddedNodeId

    def _add_variable_value(self, obj):
        """
        Returns the value for a Variable based on the objects valuetype. 
        """
        if obj.valuetype == 'ListOfLocalizedText':
            return ua.Variant([ua.LocalizedText(txt) for txt in obj.value], None)
        elif obj.valuetype == 'EnumValueType':
            values = []
            for ev in obj.value:
                enum_value = ua.EnumValueType()
                enum_value.DisplayName = ua.LocalizedText(ev['DisplayName'])
                enum_value.Description = ua.LocalizedText(ev['Description'])
                enum_value.Value = int(ev['Value'])
                values.append(enum_value)
            return values
        elif obj.valuetype == 'Argument':
            values = []
            for arg in obj.value:
                argument = ua.Argument()
                argument.Name = arg['Name']
                argument.Description = ua.LocalizedText(arg['Description'])
                argument.DataType = self.to_nodeid(arg['DataType'])
                argument.ValueRank = int(arg['ValueRank'])
                argument.ArrayDimensions = arg['ArrayDimensions']
                values.append(argument)
            return values

        return ua.Variant(obj.value, getattr(ua.VariantType, obj.valuetype))


    def add_variable_type(self, obj):
        node = self._get_node(obj)
        attrs = ua.VariableTypeAttributes()
        if obj.desc:
            attrs.Description = ua.LocalizedText(obj.desc)
        attrs.DisplayName = ua.LocalizedText(obj.displayname)
        attrs.DataType = self.to_nodeid(obj.datatype)
        if obj.value and len(obj.value) == 1:
            attrs.Value = obj.value[0]
        if obj.rank:
            attrs.ValueRank = obj.rank
        if obj.abstract:
            attrs.IsAbstract = obj.abstract
        if obj.dimensions:
            attrs.ArrayDimensions = obj.dimensions
        node.NodeAttributes = attrs
        res = self.server.add_nodes([node])
        self._add_refs(obj)
        return res[0].AddedNodeId

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
        res = self.server.add_nodes([node])
        self._add_refs(obj)
        return res[0].AddedNodeId

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
        res = self.server.add_nodes([node])
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
        res = self.server.add_nodes([node])
        self._add_refs(obj)
        return res[0].AddedNodeId

    def _add_refs(self, obj):
        if not obj.refs:
            return
        refs = []
        for data in obj.refs:
            ref = ua.AddReferencesItem()
            ref.IsForward = True
            ref.ReferenceTypeId = self.to_nodeid(data.reftype)
            ref.SourceNodeId = ua.NodeId.from_string(obj.nodeid)
            ref.TargetNodeClass = ua.NodeClass.DataType
            ref.TargetNodeId = ua.NodeId.from_string(data.target)
            refs.append(ref)
        self.server.add_references(refs)
