"""
from a list of nodes in the address space, build an XML file
format is the one from opc-ua specification
"""
import logging
import xml.etree.ElementTree as Et

from opcua import ua
from opcua.ua import object_ids as o_ids  # FIXME needed because the reverse look up isn't part of ObjectIds Class


class XmlExporter(object):

    def __init__(self, server, node_set_attrs):
        self.logger = logging.getLogger(__name__)
        self.etree = Et.ElementTree(Et.Element('UANodeSet', node_set_attrs))
        self.server = server

    def export_xml(self, node_list, xmlpath):
        self.logger.info('Exporting XML file to %s', xmlpath)

        # add all nodes in the list to an XML etree
        for node in node_list:
            self.node_to_xml(node)

        # try to write the XML etree to a file
        try:
            self.etree.write(xmlpath, short_empty_elements=False)
        except TypeError as e:  # TODO where to find which exceptions etree.write() raises?
            self.logger.error("Error writing XML to file: ", e)

    def dump_xml(self):
        self.logger.info('Dumping XML file to console')
        Et.dump(self.etree)

    def node_to_xml(self, node):
        node_class = node.get_node_class()

        if node_class is ua.NodeClass.Object:
            self.add_object(node)
        elif node_class is ua.NodeClass.UaObjectType:
            self.add_object_type(node)
        elif node_class is ua.NodeClass.Variable:
            self.add_variable(node)
        elif node_class is ua.NodeClass.VariableType:
            self.add_variable_type(node)
        elif node_class is ua.NodeClass.RefernceType:
            self.add_reference(node)
        elif node_class is ua.NodeClass.DataType:
            self.add_datatype(node)
        elif node_class is ua.NodeClass.Method:
            self.add_method(node)
        else:
            self.logger.info("Not implemented node type: %s ", node_class)

    def _get_node(self, obj):
        # TODO not sure if this is required for exporter, check on functionality
        pass

        # ORIGINAL CODE FROM IMPORTER
        # node = ua.AddNodesItem()
        # node.RequestedNewNodeId = ua.NodeId.from_string(obj.nodeid)
        # node.BrowseName = ua.QualifiedName.from_string(obj.browsename)
        # node.NodeClass = getattr(ua.NodeClass, obj.nodetype[2:])
        # if obj.parent:
        #     node.ParentNodeId = ua.NodeId.from_string(obj.parent)
        # if obj.parentlink:
        #     node.ReferenceTypeId = self.to_nodeid(obj.parentlink)
        # if obj.typedef:
        #     node.TypeDefinition = ua.NodeId.from_string(obj.typedef)
        # return node

    def to_nodeid(self, nodeid):
        # TODO migrate this function to _get_xml_nodeid and delete
        pass

        # ORIGINAL CODE FROM IMPORTER
        # if not nodeid:
        #     return ua.NodeId(ua.ObjectIds.String)
        # elif "=" in nodeid:
        #     return ua.NodeId.from_string(nodeid)
        # elif hasattr(ua.ObjectIds, nodeid):
        #     return ua.NodeId(getattr(ua.ObjectIds, nodeid))
        # else:
        #     if nodeid in self.parser.aliases:
        #         nodeid = self.parser.aliases[nodeid]
        #     else:
        #         nodeid = "i={}".format(getattr(ua.ObjectIds, nodeid))
        #     return ua.NodeId.from_string(nodeid)

    def add_object(self, obj):
        pass

        # ORIGINAL CODE FROM IMPORTER
        # node = self._get_node(obj)
        # attrs = ua.ObjectAttributes()
        # if obj.desc:
        #     attrs.Description = ua.LocalizedText(obj.desc)
        # attrs.DisplayName = ua.LocalizedText(obj.displayname)
        # attrs.EventNotifier = obj.eventnotifier
        # node.NodeAttributes = attrs
        # self.server.add_nodes([node])
        # self._add_refs(obj)

    def add_object_type(self, obj):
        pass

        # ORIGINAL CODE FROM IMPORTER
        # node = self._get_node(obj)
        # attrs = ua.ObjectTypeAttributes()
        # if obj.desc:
        #     attrs.Description = ua.LocalizedText(obj.desc)
        # attrs.DisplayName = ua.LocalizedText(obj.displayname)
        # attrs.IsAbstract = obj.abstract
        # node.NodeAttributes = attrs
        # self.server.add_nodes([node])
        # self._add_refs(obj)

    def add_variable(self, obj):
        """
        Add a UA variable element to the XML tree
        """
        browsename = self._get_xml_browsename(obj)
        datatype = o_ids.ObjectIdNames[obj.get_data_type().Identifier]
        nodeid = self._get_xml_nodeid(obj)
        parent = self._get_xml_parent(obj)
        acccesslevel = str(obj.get_access_level().val)
        useraccesslevel = str(obj.get_user_access_level().val)

        displayname = obj.get_display_name().Text.decode(encoding='UTF8')

        value = str(obj.get_value())

        refs = []  # TODO get list of refs here

        var_el = Et.SubElement(self.etree.getroot(),
                               'UAVariable',
                               BrowseName=browsename,
                               DataType=datatype,
                               NodeId=nodeid,
                               ParentNodeId=parent,
                               AccessLevel=acccesslevel,
                               UserAccessLevel=useraccesslevel)

        disp_el = Et.SubElement(var_el, 'DisplayName', )
        disp_el.text = displayname

        refs_el = Et.SubElement(var_el, 'References')

        # TODO creating XML ref elements not done yet
        for ref in refs:
            refx_el = Et.SubElement(refs_el, 'Reference', ReferenceType=ref)

        val_el = Et.SubElement(var_el, 'Value')

        valx_el = Et.SubElement(val_el, 'uax:' + datatype)
        valx_el.text = value

        # ORIGINAL CODE FROM IMPORTER
        # node = self._get_node(obj)
        # attrs = ua.VariableAttributes()
        # if obj.desc:
        #     attrs.Description = ua.LocalizedText(obj.desc)
        # attrs.DisplayName = ua.LocalizedText(obj.displayname)
        # attrs.DataType = self.to_nodeid(obj.datatype)
        # # if obj.value and len(obj.value) == 1:
        # if obj.value is not None:
        #     attrs.Value = self._add_variable_value(obj, )
        # if obj.rank:
        #     attrs.ValueRank = obj.rank
        # if obj.accesslevel:
        #     attrs.AccessLevel = obj.accesslevel
        # if obj.useraccesslevel:
        #     attrs.UserAccessLevel = obj.useraccesslevel
        # if obj.minsample:
        #     attrs.MinimumSamplingInterval = obj.minsample
        # if obj.dimensions:
        #     attrs.ArrayDimensions = obj.dimensions
        # node.NodeAttributes = attrs
        # self.server.add_nodes([node])
        # self._add_refs(obj)

    def _add_variable_value(self, obj):
        """
        Returns the value for a Variable based on the objects valuetype.
        """
        # MAY NOT BE NEEDED
        pass

        # ORIGINAL CODE FROM IMPORTER
        # if obj.valuetype == 'ListOfLocalizedText':
        #     return ua.Variant([ua.LocalizedText(txt) for txt in obj.value], None)
        # elif obj.valuetype == 'EnumValueType':
        #     values = []
        #     for ev in obj.value:
        #         enum_value = ua.EnumValueType()
        #         enum_value.DisplayName = ua.LocalizedText(ev['DisplayName'])
        #         enum_value.Description = ua.LocalizedText(ev['Description'])
        #         enum_value.Value = int(ev['Value'])
        #         values.append(enum_value)
        #     return values
        # elif obj.valuetype == 'Argument':
        #     values = []
        #     for arg in obj.value:
        #         argument = ua.Argument()
        #         argument.Name = arg['Name']
        #         argument.Description = ua.LocalizedText(arg['Description'])
        #         argument.DataType = self.to_nodeid(arg['DataType'])
        #         argument.ValueRank = int(arg['ValueRank'])
        #         argument.ArrayDimensions = arg['ArrayDimensions']
        #         values.append(argument)
        #     return values
        #
        # return ua.Variant(obj.value, getattr(ua.VariantType, obj.valuetype))


    def add_variable_type(self, obj):
        pass

        # ORIGINAL CODE FROM IMPORTER
        # node = self._get_node(obj)
        # attrs = ua.VariableTypeAttributes()
        # if obj.desc:
        #     attrs.Description = ua.LocalizedText(obj.desc)
        # attrs.DisplayName = ua.LocalizedText(obj.displayname)
        # attrs.DataType = self.to_nodeid(obj.datatype)
        # if obj.value and len(obj.value) == 1:
        #     attrs.Value = obj.value[0]
        # if obj.rank:
        #     attrs.ValueRank = obj.rank
        # if obj.abstract:
        #     attrs.IsAbstract = obj.abstract
        # if obj.dimensions:
        #     attrs.ArrayDimensions = obj.dimensions
        # node.NodeAttributes = attrs
        # self.server.add_nodes([node])
        # self._add_refs(obj)

    def add_method(self, obj):
        pass

        # ORIGINAL CODE FROM IMPORTER
        # node = self._get_node(obj)
        # attrs = ua.MethodAttributes()
        # if obj.desc:
        #     attrs.Description = ua.LocalizedText(obj.desc)
        # attrs.DisplayName = ua.LocalizedText(obj.displayname)
        # if obj.accesslevel:
        #     attrs.AccessLevel = obj.accesslevel
        # if obj.useraccesslevel:
        #     attrs.UserAccessLevel = obj.useraccesslevel
        # if obj.minsample:
        #     attrs.MinimumSamplingInterval = obj.minsample
        # if obj.dimensions:
        #     attrs.ArrayDimensions = obj.dimensions
        # node.NodeAttributes = attrs
        # self.server.add_nodes([node])
        # self._add_refs(obj)

    def add_reference(self, obj):
        # MAY NOT BE NEEDED
        pass

        # ORIGINAL CODE FROM IMPORTER
        # node = self._get_node(obj)
        # attrs = ua.ReferenceTypeAttributes()
        # if obj.desc:
        #     attrs.Description = ua.LocalizedText(obj.desc)
        # attrs.DisplayName = ua.LocalizedText(obj.displayname)
        # if obj. inversename:
        #     attrs.InverseName = ua.LocalizedText(obj.inversename)
        # if obj.abstract:
        #     attrs.IsAbstract = obj.abstract
        # if obj.symmetric:
        #     attrs.Symmetric = obj.symmetric
        # node.NodeAttributes = attrs
        # self.server.add_nodes([node])
        # self._add_refs(obj)

    def add_datatype(self, obj):
        pass

        # ORIGINAL CODE FROM IMPORTER
        # node = self._get_node(obj)
        # attrs = ua.DataTypeAttributes()
        # if obj.desc:
        #     attrs.Description = ua.LocalizedText(obj.desc)
        # attrs.DisplayName = ua.LocalizedText(obj.displayname)
        # if obj.abstract:
        #     attrs.IsAbstract = obj.abstract
        # node.NodeAttributes = attrs
        # self.server.add_nodes([node])
        # self._add_refs(obj)

    def _add_refs(self, obj):
        # MAY NOT BE NEEDED
        pass

        # ORIGINAL CODE FROM IMPORTER
        # if not obj.refs:
        #     return
        # refs = []
        # for data in obj.refs:
        #     ref = ua.AddReferencesItem()
        #     ref.IsForward = True
        #     ref.ReferenceTypeId = self.to_nodeid(data.reftype)
        #     ref.SourceNodeId = ua.NodeId.from_string(obj.nodeid)
        #     ref.TargetNodeClass = ua.NodeClass.DataType
        #     ref.TargetNodeId = ua.NodeId.from_string(data.target)
        #     refs.append(ref)
        # self.server.add_references(refs)

    @staticmethod
    def _get_xml_nodeid(obj):
        """
        Convert a UA NodeId object to a formatted string for XML
        :param obj:
        :return:
        """
        return 'ns=' + str(obj.nodeid.NamespaceIndex) + ';' + str(obj.nodeid.Identifier)

    @staticmethod
    def _get_xml_browsename(obj):
        bn = obj.get_browse_name()
        return str(bn.NamespaceIndex) + ':' + bn.Name

    def _get_xml_parent(self, obj):
        return self._get_xml_nodeid(obj.get_parent())