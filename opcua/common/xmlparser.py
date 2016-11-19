"""
parse xml file from opcua-spec
"""
import logging
import re
import sys

import xml.etree.ElementTree as ET


def _to_bool(val):
    return val in ("True", "true", "on", "On", "1")


def ua_type_to_python(val, uatype):
    if uatype.startswith("Int") or uatype.startswith("UInt"):
        return int(val)
    elif uatype.lower().startswith("bool"):
        return _to_bool(val)
    elif uatype in ("Double", "Float"):
        return float(val)
    elif uatype == "String":
        return val
    elif uatype in ("Bytes", "Bytes", "ByteString", "ByteArray"):
        if sys.version_info.major > 2:
            return bytes(val, 'utf8')
        else:
            return val
    else:
        raise Exception("uatype nopt handled", uatype, " for val ", val)


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

    def __str__(self):
        return "NodeData(nodeid:{0})".format(self.nodeid)
    __repr__ = __str__


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

    def __str__(self):
        return "ExtObj({0}, {1})".format(self.objname, self.body)
    __repr__ = __str__


class XMLParser(object):

    def __init__(self, xmlpath):
        self.logger = logging.getLogger(__name__)
        self._retag = re.compile(r"(\{.*\})(.*)")
        self.path = xmlpath

        self.tree = ET.parse(xmlpath)
        self.root = self.tree.getroot()
        # FIXME: hard to get these xml namespaces with ElementTree, we may have to shift to lxml
        self.ns = {
            'base': "http://opcfoundation.org/UA/2011/03/UANodeSet.xsd",
            'uax': "http://opcfoundation.org/UA/2008/02/Types.xsd",
            'xsd': "http://www.w3.org/2001/XMLSchema",
            'xsi': "http://www.w3.org/2001/XMLSchema-instance"
        }

    def get_used_namespaces(self):
        """
        Return the used namespace uris in this import file
        """
        namespaces_uris = []
        for child in self.root:
            tag = self._retag.match(child.tag).groups()[1]
            if tag == 'NamespaceUris':
                namespaces_uris = [ns_element.text for ns_element in child]
                break
        return namespaces_uris

    def get_aliases(self):
        """
        Return the used node aliases in this import file
        """
        aliases = {}
        for child in self.root:
            tag = self._retag.match(child.tag).groups()[1]
            if tag == 'Aliases':
                for el in child:
                    aliases[el.attrib["Alias"]] = el.text
                break
        return aliases

    def get_node_datas(self):
        nodes = []
        for child in self.root:
            tag = self._retag.match(child.tag).groups()[1]
            if tag not in ["Aliases", "NamespaceUris", "Extensions", "Models"]:  # these XML tags don't contain nodes
                node = self._parse_node(tag, child)
                nodes.append(node)
        return nodes

    def _parse_node(self, nodetype, child):
        """
        Parse a XML node and create a NodeData object.
        """
        obj = NodeData()
        obj.nodetype = nodetype
        for key, val in child.attrib.items():
            self._set_attr(key, val, obj)
        self.logger.info("Parsing node: %s %s", obj.nodeid, obj.browsename)
        obj.displayname = obj.browsename  # give a default value to display name
        for el in child:
            self._parse_attr(el, obj)
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

    def _parse_attr(self, el, obj):
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

    def _parse_value(self, val_el, obj):
        child_el = val_el.find(".//")  # should be only one child
        if child_el is not None:
            ntag = self._retag.match(child_el.tag).groups()[1]
        else:
            ntag = "Null"
        obj.valuetype = ntag

        if ntag in ("Int8", "UInt8", "Int16", "UInt16", "Int32", "UInt32", "Int64", "UInt64"):
            obj.value = int(child_el.text)
        elif ntag in ("Float", "Double"):
            obj.value = float(child_el.text)
        elif ntag == "Boolean":
            obj.value = _to_bool(child_el.text)
        elif ntag in ("ByteString", "String"):
            mytext = child_el.text
            if mytext is None:  # support importing null strings
                mytext = ""
            mytext = mytext.replace('\n', '').replace('\r', '')
            obj.value = mytext
        elif ntag == "DateTime":
            obj.value = child_el.text
        elif ntag == "Guid":
            self._parse_value(child_el, obj)
            obj.valuetype = obj.datatype  # override parsed string type to guid
        elif ntag == "LocalizedText":
            obj.value = self._parse_body(child_el)
        elif ntag == "NodeId":
            id_el = child_el.find("uax:Identifier", self.ns)
            if id_el is not None:
                obj.value = id_el.text
        elif ntag == "ListOfExtensionObject":
            obj.value = self._parse_list_of_extension_object(child_el)
        elif ntag == "ListOfLocalizedText":
            obj.value = self._parse_list_of_localized_text(child_el)
        elif ntag.startswith("ListOf"):
            obj.value = self._parse_list(child_el)
        elif ntag == "ExtensionObject":
            obj.value = self._parse_ext_obj(child_el)
        elif ntag == "Null":
            obj.value = None
        else:
            self.logger.warning("Parsing value of type '%s' not implemented", ntag)

    def _get_text(self, el):
        txtlist = [txt.strip() for txt in el.itertext()]
        return "".join(txtlist)

    def _parse_list(self, el):
        value = []
        for val_el in el:
            ntag = self._retag.match(val_el.tag).groups()[1]
            if ntag.startswith("ListOf"):
                val = self._parse_list(val_el)
            else:
                val = ua_type_to_python(val_el.text, ntag)
            value.append(val)
        return value

    def _parse_list_of_localized_text(self, el):
        value = []
        for localized_text in el:
            ntag = self._retag.match(localized_text.tag).groups()[1]
            for child in localized_text:
                ntag = self._retag.match(child.tag).groups()[1]
                if ntag == 'Text':
                    value.append(self._get_text(child))
        return value

    def _parse_list_of_extension_object(self, el):
        """
        Parse a uax:ListOfExtensionObject Value
        Return an list of ExtObj
        """
        value = []
        for extension_object in el:
            ext_obj = self._parse_ext_obj(extension_object)
            value.append(ext_obj)
        return value

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
                obj.typedef = ref.text
            elif "IsForward" in ref.attrib and ref.attrib["IsForward"] in ("false", "False"):
                # if obj.parent:
                    # sys.stderr.write("Parent is already set with: "+ obj.parent + " " + ref.text + "\n")
                obj.parent = ref.text
                obj.parentlink = ref.attrib["ReferenceType"]
            else:
                struct = RefStruct()
                if "IsForward" in ref.attrib:
                    struct.forward = ref.attrib["IsForward"]
                struct.target = ref.text
                struct.reftype = ref.attrib["ReferenceType"]
                obj.refs.append(struct)
