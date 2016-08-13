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
        self.aliases = {}

    def build_etree(self, node_list):
        """
        Create an XML etree object from a list of nodes
        Args:
            node_list: list of Node objects for export

        Returns:
        """
        self.logger.info('Building XML etree')

        # add all namespace uris to the XML etree
        self._add_namespace_uri_els()  # TODO not done yet

        # add all nodes in the list to the XML etree
        for node in node_list:
            self.node_to_etree(node)

        # add all required aliases to the XML etree; must be done after nodes are added
        self._add_alias_els()

    def write_xml(self, xmlpath):
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
            self.add_etree_object(node)
        elif node_class is ua.NodeClass.ObjectType:
            self.add_etree_object_type(node)
        elif node_class is ua.NodeClass.Variable:
            self.add_etree_variable(node)
        elif node_class is ua.NodeClass.VariableType:
            self.add_etree_variable_type(node)
        elif node_class is ua.NodeClass.RefernceType:
            self.add_etree_reference(node)
        elif node_class is ua.NodeClass.DataType:
            self.add_etree_datatype(node)
        elif node_class is ua.NodeClass.Method:
            self.add_etree_method(node)
        else:
            self.logger.info("Exporting node class not implemented: %s ", node_class)

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

    def add_etree_object(self, obj):
        """
        Add a UA object element to the XML etree
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

        self._add_ref_els(obj_el, refs)

    def add_etree_object_type(self, obj):
        """
        Add a UA object type element to the XML etree
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

        self._add_ref_els(obj_el, refs)

    def add_etree_variable(self, obj):
        """
        Add a UA variable element to the XML etree
        """
        browsename = obj.get_browse_name().to_string()
        datatype = o_ids.ObjectIdNames[obj.get_data_type().Identifier]
        datatype_nodeid = obj.get_data_type().to_string()
        nodeid = obj.nodeid.to_string()
        parent = obj.get_parent().nodeid.to_string()
        acccesslevel = str(obj.get_attribute(ua.AttributeIds.AccessLevel).Value.Value)
        useraccesslevel = str(obj.get_attribute(ua.AttributeIds.UserAccessLevel).Value.Value)

        displayname = obj.get_display_name().Text.decode(encoding='UTF8')

        value = str(obj.get_value())

        refs = obj.get_references()

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

        self._add_ref_els(var_el, refs)

        val_el = Et.SubElement(var_el, 'Value')

        valx_el = Et.SubElement(val_el, 'uax:' + datatype)
        valx_el.text = value

        # add any references that get used to aliases dict; this gets handled later
        self.aliases[datatype] = datatype_nodeid

    def add_etree_variable_type(self, obj):
        pass

    def add_etree_method(self, obj):
        pass

    def add_etree_reference(self, obj):
        pass

    def add_etree_datatype(self, obj):
        pass

    def _add_namespace_uri_els(self):
        # TODO name space uris should be exported
        pass

    def _add_alias_els(self):

        aliases_el = Et.Element('Aliases')

        for k, v in self.aliases.items():
            ref_el = Et.SubElement(aliases_el, 'Alias', Alias=k)
            ref_el.text = v

        self.etree.getroot().insert(0, aliases_el)

    def _add_ref_els(self, parent_el, refs):
        refs_el = Et.SubElement(parent_el, 'References')

        for ref in refs:
            ref_name = o_ids.ObjectIdNames[ref.ReferenceTypeId.Identifier]
            ref_forward = str(ref.IsForward)
            ref_nodeid = ref.NodeId.to_string()
            ref_el = Et.SubElement(refs_el, 'Reference', IsForward=ref_forward, ReferenceType=ref_name)
            ref_el.text = ref_nodeid

            # add any references that gets used to aliases dict; this gets handled later
            self.aliases[ref_name] = ref_nodeid
