"""
from a list of nodes in the address space, build an XML file
format is the one from opc-ua specification
"""
import logging
from collections import OrderedDict
import xml.etree.ElementTree as Et

from opcua import ua
from opcua.ua import object_ids as o_ids


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

        # add aliases to the XML etree
        self._add_alias_els()

        if uris:
            # add namespace uris to the XML etree
            self._add_namespace_uri_els(uris)

    def write_xml(self, xmlpath, pretty=True):
        """
        Write the XML etree in the exporter object to a file
        Args:
            xmlpath: string representing the path/file name

        Returns:
        """
        # try to write the XML etree to a file
        self.logger.info('Exporting XML file to %s', xmlpath)
        #from IPython import embed
        #embed()
        if pretty:
            indent(self.etree.getroot())
            self.etree.write(xmlpath, 
                             short_empty_elements=False, 
                             encoding='utf-8', 
                             xml_declaration=True
                             )
        else:
            self.etree.write(xmlpath, 
                             short_empty_elements=False, 
                             encoding='utf-8', 
                             xml_declaration=True)

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
        print("Exporting: ", node)

        if node_class is ua.NodeClass.Object:
            self.add_etree_object(node)
        elif node_class is ua.NodeClass.ObjectType:
            self.add_etree_object_type(node)
        elif node_class is ua.NodeClass.Variable:
            self.add_etree_variable(node)
        elif node_class is ua.NodeClass.VariableType:
            self.add_etree_variable_type(node)
        elif node_class is ua.NodeClass.ReferenceType:
            self.add_etree_reference(node)
        elif node_class is ua.NodeClass.DataType:
            self.add_etree_datatype(node)
        elif node_class is ua.NodeClass.Method:
            self.add_etree_method(node)
        else:
            self.logger.info("Exporting node class not implemented: %s ", node_class)

    def _add_sub_el(self, el, name, text):
        child_el = Et.SubElement(el, name)
        child_el.text = text
        return child_el

    def _add_node_common(self, nodetype, node):
        browsename = node.get_browse_name().to_string()
        nodeid = node.nodeid.to_string()
        parent = node.get_parent()
        displayname = node.get_display_name().Text.decode('utf-8')
        desc = node.get_description().Text
        print("NODE COMMON", node)
        node_el = Et.SubElement(self.etree.getroot(),
                                nodetype,
                                BrowseName=browsename,
                                NodeId=nodeid)
        if parent is not None:
            node_el.attrib["ParentNodeId"] = parent.nodeid.to_string()
        if desc not in (None, ""):
            self._add_sub_el(node_el, 'Description', desc.decode('utf-8'))
        self._add_sub_el(node_el, 'DisplayName', displayname)
        return node_el

    def add_etree_object(self, obj):
        """
        Add a UA object element to the XML etree
        """
        obj_el = self._add_node_common("UAObject", obj)
        self._add_ref_els(obj_el, obj)

    def add_etree_object_type(self, node):
        """
        Add a UA object type element to the XML etree
        """
        obj_el = self._add_node_common("UAObjectType", node)
        abstract = node.get_attribute(ua.AttributeIds.IsAbstract).Value.Value
        if abstract:
            obj_el.attrib["IsAbstract"] = 'true'
        self._add_ref_els(obj_el, node)

    def add_variable_common(self, node, el):
        dtype = node.get_data_type()
        if dtype.Identifier in o_ids.ObjectIdNames:
            dtype_name = o_ids.ObjectIdNames[dtype.Identifier]
            self.aliases[dtype_name] = dtype.to_string()
        else:
            dtype_name = dtype.to_string()
        rank = node.get_value_rank()
        el.attrib["DataType"] = dtype_name
        el.attrib["ValueRank"] = str(int(rank))
        value_to_etree(el, dtype_name, dtype, node)

    def add_etree_variable(self, node):
        """
        Add a UA variable element to the XML etree
        """
        var_el = self._add_node_common("UAVariable", node)
        self.add_variable_common(node, var_el)

        accesslevel = node.get_attribute(ua.AttributeIds.AccessLevel).Value.Value
        useraccesslevel = node.get_attribute(ua.AttributeIds.UserAccessLevel).Value.Value

        # We only write these values if they are different from defaults
        # default must of course mange the one in manage_nodes.py
        # and other OPC UA servers
        if accesslevel != ua.AccessLevel.CurrentRead.mask:
            var_el.attrib["AccessLevel"] = str(accesslevel)
        if useraccesslevel != ua.AccessLevel.CurrentRead.mask:
            var_el.attrib["UserAccessLevel"] = str(useraccesslevel)
        self._add_ref_els(var_el, node)

    def add_etree_variable_type(self, node):
        """
        Add a UA variable type element to the XML etree
        """

        var_el = self._add_node_common("UAVariable", node)
        self.add_variable_common(node, var_el)

        abstract = node.get_attribute(ua.AttributeIds.IsAbstract)
        if abstract:
            var_el.attrib["IsAbstract"] = abstract

        self._add_ref_els(var_el, node)

    def add_etree_method(self, obj):
        obj_el = self._add_node_common("UAMethod", obj)
        self._add_ref_els(obj_el, obj)

    def add_etree_reference(self, obj):
        obj_el = self._add_node_common("UAReference", obj)
        self._add_ref_els(obj_el, obj)

    def add_etree_datatype(self, obj):
        """
        Add a UA data type element to the XML etree
        """
        obj_el = self._add_node_common("UADataType", obj)
        self._add_ref_els(obj_el, obj)

    def _add_namespace_uri_els(self, uris):
        nuris_el = Et.Element('NamespaceUris')

        for uri in uris:
            self._add_sub_el(nuris_el, 'Uri', uri)

        self.etree.getroot().insert(0, nuris_el)

    def _add_alias_els(self):
        aliases_el = Et.Element('Aliases')

        for k, v in self.aliases.items():
            ref_el = Et.SubElement(aliases_el, 'Alias', Alias=k)
            ref_el.text = v

        self.etree.getroot().insert(0, aliases_el)

    def _add_ref_els(self, parent_el, obj):
        refs = obj.get_references()
        refs_el = Et.SubElement(parent_el, 'References')

        for ref in refs:
            if ref.ReferenceTypeId.Identifier in o_ids.ObjectIdNames:
                ref_name = o_ids.ObjectIdNames[ref.ReferenceTypeId.Identifier]
            else:
                ref_name = ref.ReferenceTypeId.to_string()
            ref_el = Et.SubElement(refs_el, 'Reference', ReferenceType=ref_name)
            if not ref.IsForward:
                ref_el.attrib['IsForward'] = 'false'
            ref_el.text = ref.NodeId.to_string()

            # add any references that gets used to aliases dict; this gets handled later
            self.aliases[ref_name] = ref.ReferenceTypeId.to_string()


def value_to_etree(el, dtype_name, dtype, node):
    var = node.get_data_value().Value
    val_el = Et.SubElement(el, 'Value')
    _value_to_etree(val_el, dtype_name, dtype, var.Value)


def _value_to_etree(el, dtype_name, dtype, val):
    if isinstance(val, (list, tuple)):
        list_el = Et.SubElement(el, "uax:ListOf" + dtype_name)
        for nval in val:
            _value_to_etree(list_el, dtype_name, dtype, nval)
    else:
        if dtype.Identifier is int and dtype.Identifier > 21:  # this is an extentionObject:
            _extobj_to_etree(el, dtype_name, dtype)
        else:
            val_el = Et.SubElement(el, "uax:" + dtype_name)
            val_el.text = str(val)


def _extobj_to_etree(val_el, dtype_name, dtype, val):
    obj_el = Et.SubElement(val_el, "uax:ExtensionObject")
    type_el = Et.SubElement(obj_el, "uax:TypeId")
    id_el = Et.SubElement(type_el, "uax:Identifier")
    id_el.text = val.TypeId.to_string()
    body_el = Et.SubElement(obj_el, "uax:Body")
    struct_el = Et.SubElement(body_el, "uax:" + dtype_name)
    # FIXME: finish
   

def indent(elem, level=0):
    '''
    copy and paste from http://effbot.org/zone/element-lib.htm#prettyprint
    it basically walks your tree and adds spaces and newlines so the tree is
    printed in a nice way
    '''
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i
