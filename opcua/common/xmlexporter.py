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

    def build_etree(self, node_list):
        """
        Create an XML etree object from a list of nodes
        Args:
            node_list: list of Node objects for export

        Returns:
        """
        self.logger.info('Building XML etree')

        # add all namespace uris to the XML etree
        self._get_xml_namespace_uris()  # TODO not done yet

        # add all required aliases to the XML etree
        self._get_xml_aliases()  # TODO not done yet

        # add all nodes in the list to the XML etree
        for node in node_list:
            self.node_to_etree(node)

    def export_xml(self, xmlpath):
        """
        Write the XML etree in the exporter object to a file
        Args:
            xmlpath: string representing the path/file name

        Returns:
        """
        # try to write the XML etree to a file
        self.logger.info('Exporting XML file to %s', xmlpath)
        try:
            self.etree.write(xmlpath, short_empty_elements=False)
        except TypeError as e:  # TODO where to find which exceptions etree.write() raises?
            self.logger.error("Error writing XML to file: ", e)

    def dump_etree(self):
        """
        Dump etree to console for debugging
        Returns:
        """
        self.logger.info('Dumping XML etree to console')
        Et.dump(self.etree)

    def node_to_etree(self, node):
        """
        Add the necessary XML sub elements to the etree for exporting the node
        Args:
            node: Node object which will be added to XML etree

        Returns:
        """
        node_class = node.get_node_class()

        if node_class is ua.NodeClass.Object:
            self.add_object_xml(node)
        elif node_class is ua.NodeClass.ObjectType:
            self.add_object_type_xml(node)
        elif node_class is ua.NodeClass.Variable:
            self.add_variable_xml(node)
        elif node_class is ua.NodeClass.VariableType:
            self.add_variable_type_xml(node)
        elif node_class is ua.NodeClass.RefernceType:
            self.add_reference_xml(node)
        elif node_class is ua.NodeClass.DataType:
            self.add_datatype_xml(node)
        elif node_class is ua.NodeClass.Method:
            self.add_method_xml(node)
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

    def add_object_xml(self, obj):
        """
        Add a UA object element to the XML tree
        """
        browsename = obj.get_browse_name().to_string()
        nodeid = obj.nodeid.to_string()

        displayname = obj.get_display_name().Text.decode(encoding='UTF8')

        refs = obj.get_references()

        obj_el = Et.SubElement(self.etree.getroot(),
                               'UAObject',
                               BrowseName=browsename,
                               NodeId=nodeid)

        disp_el = Et.SubElement(obj_el, 'DisplayName', )
        disp_el.text = displayname

        self._add_ref_sub_els(obj_el, refs)

    def add_object_type_xml(self, obj):
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

    def add_variable_xml(self, obj):
        """
        Add a UA variable element to the XML tree
        """
        browsename = obj.get_browse_name().to_string()
        datatype = o_ids.ObjectIdNames[obj.get_data_type().Identifier]
        nodeid = obj.nodeid.to_string()
        parent = obj.get_parent().nodeid.to_string()
        acccesslevel = str(obj.get_attribute(ua.AttributeIds.AccessLevel).Value.Value)
        useraccesslevel = str(obj.get_attribute(ua.AttributeIds.UserAccessLevel).Value.Value)

        displayname = obj.get_display_name().Text.decode(encoding='UTF8')

        value = str(obj.get_value())

        refs = obj.get_references()  # []  # TODO get list of refs here

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

        self._add_ref_sub_els(var_el, refs)

        val_el = Et.SubElement(var_el, 'Value')

        valx_el = Et.SubElement(val_el, 'uax:' + datatype)
        valx_el.text = value

    def add_variable_type_xml(self, obj):
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

    def add_method_xml(self, obj):
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

    def add_reference_xml(self, obj):
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

    def add_datatype_xml(self, obj):
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

    def _get_xml_namespace_uris(self):
        # TODO name space uris should be exported
        pass

    def _get_xml_aliases(self):
        # TODO aliases need to be created at the top of the xml
        pass

    @staticmethod
    def _add_ref_sub_els(parent_el, refs):
        refs_el = Et.SubElement(parent_el, 'References')

        for ref in refs:
            ref_name = o_ids.ObjectIdNames[ref.ReferenceTypeId.Identifier]
            ref_forward = str(ref.IsForward)
            refx_el = Et.SubElement(refs_el, 'Reference', IsForward=ref_forward, ReferenceType=ref_name)
            refx_el.text = ref.NodeId.to_string()
