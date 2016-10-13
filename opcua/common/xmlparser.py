"""
parse xml file from opcua-spec
"""
import logging
import re
import sys

import xml.etree.ElementTree as ET


def _to_bool(val):
    if val in ("True", "true", "on", "On", "1"):
        return True
    else:
        return False



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
        self.value = None
        self.valuetype = None
        self.dimensions = None
        self.accesslevel = None
        self.useraccesslevel = None
        self.minsample = None

        # referencetype
        self.inversename = ""
        self.abstract = False
        self.symmetric = False

        # datatype
        self.definition = []


class RefStruct(object):

    def __init__(self):
        self.reftype = None
        self.forward = True
        self.target = None


class ExtObj(object):

    def __init__(self):
        self.typeid = None
        self.objname = None
        self.bodytype = None
        self.body = {}


class XMLParser(object):

    def __init__(self, xmlpath, server):
        self.server = server  # POC
        self.logger = logging.getLogger(__name__)
        self._retag = re.compile(r"(\{.*\})(.*)")
        self.path = xmlpath
        self.aliases = {}

        self.tree = ET.parse(xmlpath)
        self.root = self.tree.getroot()
        self.it = None

        self.namespaces = {}
        self._re_nodeid = re.compile(r"^ns=(?P<ns>\d+[^;]*);i=(?P<i>\d+)")

    def get_used_namespaces(self):
        """
        Return the used namespace uris in this import file
        """
        namespaces_uris = []
        for child in self.root:
            name = self._retag.match(child.tag).groups()[1]
            if name == 'NamespaceUris':
                namespaces_uris = [ns_element.text for ns_element in child]
                break
        return namespaces_uris

    def __iter__(self):
        nodes = []
        for child in self.root:
            name = self._retag.match(child.tag).groups()[1]
            if name == "Aliases":
                for el in child:
                    self.aliases[el.attrib["Alias"]] = self._get_node_id(el.text)
            elif name == 'NamespaceUris':
                print(child.tag)
                for ns_index, ns_element in enumerate(child):
                    ns_uri = ns_element.text
                    ns_server_index = self.server.register_namespace(ns_uri)
                    self.namespaces[ns_index + 1] = (ns_server_index, ns_uri)
                    print("namespace offset", ns_index + 1, (ns_server_index, ns_uri))
            else:
                node = self._parse_node(name, child)
                nodes.append(node)

        # The ordering of nodes currently only works if namespaces are
        # defined in XML.
        # Also, it is recommended not to use node ids without namespace prefix!
        if self.namespaces:
            nodes = self._sort_nodes_by_parentid(nodes)

        self.it = iter(nodes)
        return self

    def __next__(self):
        while True:
            if sys.version_info[0] < 3:
                child = self.it.next()
            else:
                child = self.it.__next__()
            return child

    def next(self):  # support for python2
        return self.__next__()

    def _sort_nodes_by_parentid(self, nodes):
        """
        Sort the list of nodes according theire parent node in order to respect
        the depency between nodes.

        :param nodes: list of NodeDataObjects
        :returns: list of sorted nodes
        """
        _nodes = list(nodes)
        # list of node ids that are already sorted / inserted
        sorted_nodes_ids = []
        # list of sorted nodes (i.e. XML Elements)
        sorted_nodes = []
        # list of namespace indexes that are relevant for this import
        # we can only respect ordering nodes for namespaces indexes that
        # are defined in the xml file itself. Thus we assume that all other
        # references namespaces are already known to the server and should
        # not create any dependency problems (like "NodeNotFound")
        relevant_namespaces = [str(i[0]) for i in self.namespaces.values()]
        while len(_nodes) > 0:
            pop_nodes = []
            for node in _nodes:
                insert = None
                # Get the node and parent node namespace and id parts
                node_ns, node_id = self._split_node_id(node.nodeid)
                parent_ns, parent_id = self._split_node_id(node.parent)

                # Insert nodes that
                #   (1) have no parent / parent_ns is None (e.g. namespace 0)
                #   (2) ns is not in list of relevant namespaces
                if (parent_ns is None or node_ns not in relevant_namespaces or
                    parent_id is None):
                    insert = 0
                else:
                    # Check if the nodes parent is already in the list of
                    # inserted nodes
                    if node.parent in sorted_nodes_ids:
                        insert = -1

                if insert == 0:
                    sorted_nodes.insert(insert, node)
                    sorted_nodes_ids.insert(insert, node.nodeid)
                    pop_nodes.append(node)
                elif insert == -1:
                    sorted_nodes.append(node)
                    sorted_nodes_ids.append(node.nodeid)
                    pop_nodes.append(node)

            # Remove inserted nodes from the list
            for node in pop_nodes:
                _nodes.pop(_nodes.index(node))
        return sorted_nodes

    def _split_node_id(self, value):
        """
        Split the fq node id into namespace and id part.

        :returns: (namespace, id)
        """
        if not value:
            return (None, value)
        r_match = self._re_nodeid.search(value)
        if r_match:
            return r_match.groups()

        return (None, value)

    def _get_node_id(self, value):
        """
        Check if the nodeid given in the xml model file must be converted
        to a already existing namespace id based on the files namespace uri

        :returns: NodeId (str)
        """
        result = value

        node_ns, node_id = self._split_node_id(value)
        if node_ns:
            ns_server = self.namespaces.get(int(node_ns), None)
            if ns_server:
                result = "ns={};i={}".format(ns_server[0], node_id)
        return result

    def _parse_bname(self, bname):
        """
        Parse a browsename and correct the namespace index.
        """
        if bname.find(':') != -1:
            browse_ns, browse_name = bname.split(':')
            if browse_ns:
                ns_server = self.namespaces.get(int(browse_ns), None)
                if ns_server:
                    return '%d:%s' % (ns_server[0], browse_name)
        return bname

    def _parse_node(self, name, child):
        """
        Parse a XML node and create a NodeData object.
        """
        obj = NodeData()
        obj.nodetype = name
        for key, val in child.attrib.items():
            self._set_attr(key, val, obj)
        self.logger.info("\n     Parsing node: %s %s", obj.nodeid, obj.browsename)
        obj.displayname = obj.browsename  # give a default value to display name
        for el in child:
            self._parse_tag(el, obj)
        return obj

    def _set_attr(self, key, val, obj):
        if key == "NodeId":
            obj.nodeid = self._get_node_id(val)
        elif key == "BrowseName":
            obj.browsename = self._parse_bname(val)
        elif key == "SymbolicName":
            obj.symname = val
        elif key == "ParentNodeId":
            obj.parent = self._get_node_id(val)
        elif key == "DataType":
            obj.datatype = val
        elif key == "IsAbstract":
            obj.abstract = _to_bool(val)
        elif key == "Executable":
            obj.executable = _to_bool(val)
        elif key == "EventNotifier":
            obj.eventnotifier = int(val)
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
            obj.symmetric = _to_bool(val)
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
        self.logger.info("Parsing value")
        for val in el:
            self.logger.info("tag %s", val.tag)
            ntag = self._retag.match(val.tag).groups()[1]
            obj.valuetype = ntag
            if ntag in ("Int8", "UInt8", "Int16", "UInt16", "Int32", "UInt32", "Int64", "UInt64"):
                obj.value = int(val.text)
            elif ntag in ("Float", "Double"):
                obj.value = float(val.text)
            elif ntag in ("Boolean"):
                obj.value = _to_bool(val.text)
            elif ntag in ("ByteString", "String"):
                mytext = val.text
                if mytext is None:  # support importing null strings
                    mytext = ""
                mytext = mytext.replace('\n', '').replace('\r', '')
                # obj.value.append('b"{}"'.format(mytext))
                obj.value = mytext
            elif ntag in ("Guid"):
                self._parse_value(val, obj)
            elif ntag == "ListOfExtensionObject":
                obj.value = self._parse_list_of_extension_object(el)
            elif ntag == "ListOfLocalizedText":
                obj.value = self._parse_list_of_localized_text(el)
            elif ntag == "ExtensionObject":
                obj.value = self._parse_extension_object(el)
            else:
                self.logger.warning("Value type not implemented: '%s'", ntag)

    def _get_text(self, el):
        txtlist = [txt.strip() for txt in el.itertext()]
        return "".join(txtlist)

    def _parse_list_of_localized_text(self, el):
        value = []
        for localized_text_list in el:
            for localized_text in localized_text_list:
                ntag = self._retag.match(localized_text.tag).groups()[1]
                for child in localized_text:
                    ntag = self._retag.match(child.tag).groups()[1]
                    if ntag == 'Text':
                        value.append(self._get_text(child))
        return value

    def _parse_list_of_extension_object(self, el):
        '''
        Parse a uax:ListOfExtensionObject Value
        Return an list of ExtObj
        '''
        value = []
        for extension_object_list in el:
            for extension_object in extension_object_list:
                ext_obj = self._parse_ext_obj(extension_object)
                value.append(ext_obj)
        return value

    def _parse_extension_object(self, el):
        for ext_obj in el:
            return self._parse_ext_obj(ext_obj)

    def _parse_ext_obj(self, el):
        ext = ExtObj()
        for extension_object_part in el:
            ntag = self._retag.match(extension_object_part.tag).groups()[1]
            if ntag == 'TypeId':
                ntag = self._retag.match(extension_object_part.find('*').tag).groups()[1]
                ext.typeid = self._get_text(extension_object_part)
            elif ntag == 'Body':
                ext.objname = self._retag.match(extension_object_part.find('*').tag).groups()[1]
                ext.body = self._parse_body(extension_object_part)
            else:
                print("Uknown ndtag", ntag)
        return ext

    def _parse_body(self, el):
        body = []
        for body_item in el:
            otag = self._retag.match(body_item.tag).groups()[1]
            childs = [i for i in body_item]
            if not childs:
                val = self._get_text(body_item)
            else:
                val = self._parse_body(body_item)
            if val:
                body.append((otag, val))
        return body

    def _parse_refs(self, el, obj):
        for ref in el:
            if ref.attrib["ReferenceType"] == "HasTypeDefinition":
                obj.typedef = self._get_node_id(ref.text)
            elif "IsForward" in ref.attrib and ref.attrib["IsForward"] in ("false", "False"):
                # if obj.parent:
                    # sys.stderr.write("Parent is already set with: "+ obj.parent + " " + ref.text + "\n")
                obj.parent = self._get_node_id(ref.text)
                obj.parentlink = ref.attrib["ReferenceType"]
            else:
                struct = RefStruct()
                if "IsForward" in ref.attrib:
                    struct.forward = ref.attrib["IsForward"]
                struct.target = self._get_node_id(ref.text)
                struct.reftype = ref.attrib["ReferenceType"]
                obj.refs.append(struct)
