"""
parse xml file from opcua-spec
"""
import logging
import re
import sys

import xml.etree.ElementTree as ET


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

    def __iter__(self):
        self.it = iter(self.root)
        return self

    def __next__(self):
        while True:
            if sys.version_info[0] < 3:
                child = self.it.next()
            else:
                child = self.it.__next__()
            name = self._retag.match(child.tag).groups()[1]
            if name == "Aliases":
                for el in child:
                    self.aliases[el.attrib["Alias"]] = el.text
            elif name == 'NamespaceUris':
                for ns_index, ns_element in enumerate(child):
                    ns_uri = ns_element.text
                    ns_server_index = self.server.register_namespace(ns_uri)
                    self.namespaces[ns_index + 1] = (ns_server_index, ns_uri)
            else:
                node = self._parse_node(name, child)
                return node

    def next(self):  # support for python2
        return self.__next__()

    def _get_node_id(self, value):
        """
        Check if the nodeid given in the xml model file must be converted
        to a already existing namespace id based on the files namespace uri

        :returns: NodeId (str)
        """
        result = value
        r_match = self._re_nodeid.search(value)
        if r_match:
            node_ns, node_id = r_match.groups()
            ns_server = self.namespaces.get(int(node_ns), None)
            if ns_server:
                result = "ns={};i={}".format(ns_server[0], node_id)
        return result

    def _parse_node(self, name, child):
        obj = NodeData()
        obj.nodetype = name
        for key, val in child.attrib.items():
            self._set_attr(key, val, obj)
        obj.displayname = obj.browsename  # give a default value to display name
        for el in child:
            self._parse_tag(el, obj)
        return obj

    def _set_attr(self, key, val, obj):
        if key == "NodeId":
            obj.nodeid = self._get_node_id(val)
        elif key == "BrowseName":
            obj.browsename = val
        elif key == "SymbolicName":
            obj.symname = val
        elif key == "ParentNodeId":
            obj.parent = self._get_node_id(val)
        elif key == "DataType":
            obj.datatype = val
        elif key == "IsAbstract":
            obj.abstract = val
        elif key == "EventNotifier":
            obj.eventnotifier = 1 if val == "1" else 0
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
            if ntag in ("Int8", "UInt8", "Int16", "UInt16", "Int32", "UInt32", "Int64", "UInt64"):
                obj.value = int(val.text)
            elif ntag in ("Float", "Double"):
                obj.value = float(val.text)
            elif ntag in ("Boolean"):
                if val.text in ("True", "true", "1", "on", "On"):
                    obj.value = bool(1)
                else:
                    obj.value = bool(0)
            elif ntag in ("ByteString", "String"):
                mytext = val.text
                if mytext is None:  # support importing null strings
                    mytext = ""
                mytext = mytext.replace('\n', '').replace('\r', '')
                # obj.value.append('b"{}"'.format(mytext))
                obj.value = mytext
            elif ntag == "ListOfExtensionObject":
                obj.value, obj.valuetype = self._parse_list_of_extension_object(el)
            elif ntag == "ListOfLocalizedText":
                obj.value = self._parse_list_of_localized_text(el)
            else:
                self.logger.info("Value type not implemented: %s", ntag)

    def _get_text(self, el):
        txt = ""
        for text in el.itertext():
            txt += text
        return txt

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
        
        Return an array with a value of each uax:ExtensionObject/*/* (each element is convert to a netry in a dict.
               also the valuetype is returned. The valuetype is  uax:ExtensionObject/*/tag()
        '''
        value = []
        valuetype = None
        for extension_object_list in el:
            for extension_object in extension_object_list:
                extension_object.find('Body')
                for extension_object_part in extension_object:
                    ntag = self._retag.match(extension_object_part.tag).groups()[1]
                    if ntag == 'Body':
                        data = {}
                        ntag = self._retag.match(extension_object_part.find('*').tag).groups()[1]
                        valuetype = ntag
                        for body_item in extension_object_part.findall('*/*'):
                            ntag = self._retag.match(body_item.tag).groups()[1]

                            child = body_item.find('*')
                            if child is not None:
                                data[ntag] = self._get_text(child)
                            else:
                                data[ntag] = self._get_text(body_item)
                        value.append(data)
        return value, valuetype

    def _parse_refs(self, el, obj):
        for ref in el:
            if ref.attrib["ReferenceType"] == "HasTypeDefinition":
                obj.typedef = self._get_node_id(ref.text)
            elif "IsForward" in ref.attrib and ref.attrib["IsForward"] == "false":
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
