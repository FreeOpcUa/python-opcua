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
        self.it = None

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
        obj.displayname = obj.browsename  # give a default value to display name
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
                mytext = val.text.replace('\n', '').replace('\r', '')
                # obj.value.append('b"{}"'.format(mytext))
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
