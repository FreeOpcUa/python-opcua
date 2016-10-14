"""G
add node defined in XML to address space
format is the one from opc-ua specification
"""
import logging
import sys
import re

from opcua import ua
from opcua.common import xmlparser


def ua_type_to_python(val, uatype):
    if uatype.startswith("Int") or uatype.startswith("UInt"):
        return int(val)
    elif uatype in ("String"):
        return val
    elif uatype in ("Bytes", "Bytes", "ByteString", "ByteArray"):
        if sys.version_info.major > 2:
            return bytes(val, 'utf8')
        else:
            return val
    else:
        raise Exception("uatype nopt handled", uatype, " for val ", val)


def to_python(val, obj, attname):
    if isinstance(obj, ua.NodeId) and attname == "Identifier":
        raise RuntimeError("Error we should parse a NodeId here")
        return ua.NodeId.from_string(val)
    else:
        return ua_type_to_python(val, obj.ua_types[attname])


class XmlImporter(object):

    def __init__(self, server):
        self.logger = logging.getLogger(__name__)
        self.parser = None
        self.server = server
        self.namespaces = {}
        self.aliases = {}
        self._re_nodeid = re.compile(r"^ns=(?P<ns>\d+[^;]*);i=(?P<i>\d+)")

    def _map_namespaces(self, namespaces_uris, act_server):
        """
        creates a mapping between the namespaces in the xml file and in the server.
        if not present the namespace is registered.
        """
        namespaces = {}
        for ns_index, ns_uri in enumerate(namespaces_uris):
            ns_server_index = act_server.register_namespace(ns_uri)
            namespaces[ns_index + 1] = (ns_server_index, ns_uri)
            self.logger.info("namespace offset", ns_index + 1, (ns_server_index, ns_uri))
        return namespaces

    def _map_aliases(self, aliases):
        """
        maps the import aliases to the correct namespaces        
        """
        aliases_mapped = {}
        for alias, node_id in aliases.items():
            aliases_mapped[alias] = self._get_node_id(node_id)
        return aliases_mapped

    def import_xml(self, xmlpath, act_server):
        """
        import xml and return added nodes
        """
        self.logger.info("Importing XML file %s", xmlpath)
        self.parser = xmlparser.XMLParser(xmlpath, act_server)

        self.namespaces = self._map_namespaces(self.parser.get_used_namespaces(), act_server)
        self.aliases = self._map_aliases(self.parser.get_aliases())

        # The ordering of nodes currently only works if namespaces are
        # defined in XML.
        # Also, it is recommended not to use node ids without namespace prefix!
        nodes_parsed = self._sort_nodes_by_parentid(self.parser)

        nodes = []
        for nodedata in nodes_parsed:  # self.parser:
            if nodedata.nodetype == 'UAObject':
                node = self.add_object(nodedata)
            elif nodedata.nodetype == 'UAObjectType':
                node = self.add_object_type(nodedata)
            elif nodedata.nodetype == 'UAVariable':
                node = self.add_variable(nodedata)
            elif nodedata.nodetype == 'UAVariableType':
                node = self.add_variable_type(nodedata)
            elif nodedata.nodetype == 'UAReferenceType':
                node = self.add_reference_type(nodedata)
            elif nodedata.nodetype == 'UADataType':
                node = self.add_datatype(nodedata)
            elif nodedata.nodetype == 'UAMethod':
                node = self.add_method(nodedata)
            else:
                self.logger.warning("Not implemented node type: %s ", nodedata.nodetype)
                continue
            nodes.append(node)
        return nodes

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

    def _get_node(self, obj):
        node = ua.AddNodesItem()
        node.RequestedNewNodeId = ua.NodeId.from_string(self._get_node_id(obj.nodeid))
        node.BrowseName = ua.QualifiedName.from_string(self._parse_bname(obj.browsename))
        node.NodeClass = getattr(ua.NodeClass, obj.nodetype[2:])
        if obj.parent:
            node.ParentNodeId = ua.NodeId.from_string(self._get_node_id(obj.parent))
        if obj.parentlink:
            node.ReferenceTypeId = self.to_nodeid(self._get_node_id(obj.parentlink))
        if obj.typedef:
            node.TypeDefinition = ua.NodeId.from_string(self._get_node_id(obj.typedef))
        return node

    def to_nodeid(self, nodeid):
        if not nodeid:
            return ua.NodeId(ua.ObjectIds.String)
        elif "=" in nodeid:
            return ua.NodeId.from_string(nodeid)
        elif hasattr(ua.ObjectIds, nodeid):
            return ua.NodeId(getattr(ua.ObjectIds, nodeid))
        else:
            if nodeid in self.aliases:
                nodeid = self.aliases[nodeid]
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
            attrs.Value = self._add_variable_value(obj,)
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

    def _make_ext_obj(sefl, obj):
        ext = getattr(ua, obj.objname)()
        for name, val in obj.body:
            if type(val) is str:
                raise Exception("Error val should a dict", name, val)
            else:
                for attname, v in val:
                    # tow possible values:
                    # either we get value directly
                    # or a dict if it s an object or a list
                    if type(v) is str:
                        setattr(ext, attname, to_python(v, ext, attname))
                    else:
                        # so we habve either an object or a list...
                        obj2 = getattr(ext, attname)
                        if isinstance(obj2, ua.NodeId):
                            for attname2, v2 in v:
                                if attname2 == "Identifier":
                                    obj2 = ua.NodeId.from_string(v2)
                                    setattr(ext, attname, obj2)
                                    break
                        elif not isinstance(obj2, ua.NodeId) and not hasattr(obj2, "ua_types"):
                            # we probably have a list
                            my_list = []
                            for vtype, v2 in v:
                                my_list.append(ua_type_to_python(v2, vtype))
                            setattr(ext, attname, my_list)
                        else:
                            for attname2, v2 in v:
                                setattr(obj2, attname2, to_python(v2, obj2, attname2))
                            setattr(ext, attname, obj2)
        return ext

    def _add_variable_value(self, obj):
        """
        Returns the value for a Variable based on the objects valuetype. 
        """
        if obj.valuetype == 'ListOfExtensionObject':
            values = []
            for ext in obj.value:
                extobj = self._make_ext_obj(ext)
                values.append(extobj)
            return values
        elif obj.valuetype.startswith("ListOf"):
            vtype = obj.valuetype[6:]
            return [getattr(ua, vtype)(v) for v in obj.value]
        elif obj.valuetype == 'ExtensionObject':
            extobj = self._make_ext_obj(obj.value)
            return ua.Variant(extobj, getattr(ua.VariantType, obj.valuetype))
        else:
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

    def add_reference_type(self, obj):
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
        return res[0].AddedNodeId

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
            ref.SourceNodeId = ua.NodeId.from_string(self._get_node_id(obj.nodeid))
            ref.TargetNodeClass = ua.NodeClass.DataType
            ref.TargetNodeId = ua.NodeId.from_string(self._get_node_id(data.target))
            refs.append(ref)
        self.server.add_references(refs)

    # FIX: wrong order of node sorting .. need to find out what is wrong
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
        relevant_namespaces = [str(ns) for ns in self.namespaces.keys()]
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
                if (parent_ns is None or
                    (len(relevant_namespaces) >= 1 and node_ns not in relevant_namespaces) or
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
