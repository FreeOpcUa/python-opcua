"""
from a list of nodes in the address space, build an XML file
format is the one from opc-ua specification
"""
import logging
from collections import OrderedDict
import xml.etree.ElementTree as Et

from opcua import ua
from opcua.ua import object_ids as o_ids  # FIXME needed because the reverse look up isn't part of ObjectIds Class


class XmlExporter(object):

    def __init__(self, server):
        self.logger = logging.getLogger(__name__)
        self.server = server
        self.aliases = {}

        node_set_attributes = OrderedDict()
        node_set_attributes['xmlns:xsi'] = 'http://www.w3.org/2001/XMLSchema-instance'
        node_set_attributes['xmlns:uax'] = 'http://opcfoundation.org/UA/2008/02/Types.xsd'
        node_set_attributes['xmlns:xsd'] = 'http://www.w3.org/2001/XMLSchema'
        node_set_attributes['xmlns'] = 'http://opcfoundation.org/UA/2011/03/UANodeSet.xsd'

        self.etree = Et.ElementTree(Et.Element('UANodeSet', node_set_attributes))

    def build_etree(self, node_list, uris=None):
        """
        Create an XML etree object from a list of nodes; custom namespace uris are optional
        Args:
            node_list: list of Node objects for export
            uris: list of namespace uri strings

        Returns:
        """
        self.logger.info('Building XML etree')

        # add all nodes in the list to the XML etree
        for node in node_list:
            self.node_to_etree(node)

        # add all required aliases to the XML etree; must be done after nodes are added
        self._add_alias_els()

        if uris:
            # add all namespace uris to the XML etree; must be done after aliases are added
            self._add_namespace_uri_els(uris)

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
        symbolicname = None  # TODO when to export this?

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
        """
        Add a UA variable type element to the XML etree
        """
        browsename = obj.get_browse_name().to_string()
        nodeid = obj.nodeid.to_string()
        valuerank = None  # TODO when to export this?

        displayname = obj.get_display_name().Text.decode(encoding='UTF8')

        refs = obj.get_references()

        obj_el = Et.SubElement(self.etree.getroot(),
                               'UAObject',
                               BrowseName=browsename,
                               NodeId=nodeid)

        disp_el = Et.SubElement(obj_el, 'DisplayName', )
        disp_el.text = displayname

        self._add_ref_els(obj_el, refs)

    def add_etree_method(self, obj):
        raise NotImplemented

    def add_etree_reference(self, obj):
        raise NotImplemented

    def add_etree_datatype(self, obj):
        """
        Add a UA data type element to the XML etree
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

    def _add_namespace_uri_els(self, uris):
        nuris_el = Et.Element('NamespaceUris')

        for uri in uris:
            uri_el = Et.SubElement(nuris_el, 'Uri')
            uri_el.text = uri

        self.etree.getroot().insert(0, nuris_el)

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
