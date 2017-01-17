"""
add nodes defined in XML to address space
format is the one from opc-ua specification
"""
import logging
import uuid
from copy import copy

import opcua
from opcua import ua
from opcua.common import xmlparser


class XmlImporter(object):

    def __init__(self, server):
        self.logger = logging.getLogger(__name__)
        self.parser = None
        self.server = server
        self.namespaces = {}
        self.aliases = {}

    def _map_namespaces(self, namespaces_uris):
        """
        creates a mapping between the namespaces in the xml file and in the server.
        if not present the namespace is registered.
        """
        namespaces = {}
        for ns_index, ns_uri in enumerate(namespaces_uris):
            ns_server_index = self.server.register_namespace(ns_uri)
            namespaces[ns_index + 1] = ns_server_index
        return namespaces

    def _map_aliases(self, aliases):
        """
        maps the import aliases to the correct namespaces        
        """
        aliases_mapped = {}
        for alias, node_id in aliases.items():
            aliases_mapped[alias] = self._migrate_ns(self.to_nodeid(node_id))
        return aliases_mapped

    def import_xml(self, xmlpath):
        """
        import xml and return added nodes
        """
        self.logger.info("Importing XML file %s", xmlpath)
        self.parser = xmlparser.XMLParser(xmlpath)

        self.namespaces = self._map_namespaces(self.parser.get_used_namespaces())
        self.aliases = self._map_aliases(self.parser.get_aliases())
        
        dnodes = self.parser.get_node_datas()
        dnodes = self.make_objects(dnodes)
        nodes_parsed = self._sort_nodes_by_parentid(dnodes)

        nodes = []
        for nodedata in nodes_parsed:  # self.parser:
            try:
                node = self._add_node_data(nodedata)
            except Exception:
                self.logger.warning("failure adding node %s", nodedata)
                raise
            nodes.append(node)
        return nodes

    def _add_node_data(self, nodedata):
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
        return node

    def _add_node(self, node):
        if isinstance(self.server, opcua.server.server.Server):
            return self.server.iserver.isession.add_nodes([node])
        else:
            return self.server.uaclient.add_nodes([node])

    def _add_references(self, refs):
        if isinstance(self.server, opcua.server.server.Server):
            return self.server.iserver.isession.add_references(refs)
        else:
            return self.server.uaclient.add_references(refs)
    
    def make_objects(self, node_datas):
        new_nodes = []
        for ndata in node_datas:
            ndata.nodeid = ua.NodeId.from_string(ndata.nodeid)
            ndata.browsename = ua.QualifiedName.from_string(ndata.browsename)
            if ndata.parent:
                ndata.parent = ua.NodeId.from_string(ndata.parent)
            if ndata.parentlink:
                ndata.parentlink = self.to_nodeid(ndata.parentlink)
            if ndata.typedef:
                ndata.typedef = self.to_nodeid(ndata.typedef)
            new_nodes.append(ndata)
        return new_nodes

    def _migrate_ns(self, nodeid):
        """
        Check if the index of nodeid or browsename  given in the xml model file
        must be converted to a already existing namespace id based on the files
        namespace uri

        :returns: NodeId (str)
        """
        if nodeid.NamespaceIndex in self.namespaces:
            nodeid = copy(nodeid)
            nodeid.NamespaceIndex = self.namespaces[nodeid.NamespaceIndex]
        return nodeid

    def _get_node(self, obj):
        node = ua.AddNodesItem()
        node.RequestedNewNodeId = self._migrate_ns(obj.nodeid)
        node.BrowseName = self._migrate_ns(obj.browsename)
        self.logger.info("Importing xml node (%s, %s) as (%s %s)", obj.browsename, obj.nodeid, node.BrowseName, node.RequestedNewNodeId)
        node.NodeClass = getattr(ua.NodeClass, obj.nodetype[2:])
        if obj.parent:
            node.ParentNodeId = self._migrate_ns(obj.parent)
        if obj.parentlink:
            node.ReferenceTypeId = self._migrate_ns(obj.parentlink)
        if obj.typedef:
            node.TypeDefinition = self._migrate_ns(obj.typedef)
        return node

    def to_nodeid(self, nodeid):
        if isinstance(nodeid, ua.NodeId):
            return nodeid
        elif not nodeid:
            return ua.NodeId(ua.ObjectIds.String)
        elif "=" in nodeid:
            return ua.NodeId.from_string(nodeid)
        elif hasattr(ua.ObjectIds, nodeid):
            return ua.NodeId(getattr(ua.ObjectIds, nodeid))
        else:
            if nodeid in self.aliases:
                return self.aliases[nodeid]
            else:
                return ua.NodeId(getattr(ua.ObjectIds, nodeid))

    def add_object(self, obj):
        node = self._get_node(obj)
        attrs = ua.ObjectAttributes()
        if obj.desc:
            attrs.Description = ua.LocalizedText(obj.desc)
        attrs.DisplayName = ua.LocalizedText(obj.displayname)
        attrs.EventNotifier = obj.eventnotifier
        node.NodeAttributes = attrs
        res = self._add_node(node)
        self._add_refs(obj)
        res[0].StatusCode.check()
        return res[0].AddedNodeId

    def add_object_type(self, obj):
        node = self._get_node(obj)
        attrs = ua.ObjectTypeAttributes()
        if obj.desc:
            attrs.Description = ua.LocalizedText(obj.desc)
        attrs.DisplayName = ua.LocalizedText(obj.displayname)
        attrs.IsAbstract = obj.abstract
        node.NodeAttributes = attrs
        res = self._add_node(node)
        self._add_refs(obj)
        res[0].StatusCode.check()
        return res[0].AddedNodeId

    def add_variable(self, obj):
        node = self._get_node(obj)
        attrs = ua.VariableAttributes()
        if obj.desc:
            attrs.Description = ua.LocalizedText(obj.desc)
        attrs.DisplayName = ua.LocalizedText(obj.displayname)
        attrs.DataType = self.to_nodeid(obj.datatype)
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
        res = self._add_node(node)
        self._add_refs(obj)
        res[0].StatusCode.check()
        return res[0].AddedNodeId

    def _make_ext_obj(self, obj):
        ext = getattr(ua, obj.objname)()
        for name, val in obj.body:
            if isinstance(val, str):
                raise Exception("Error val should a dict", name, val)
            else:
                for attname, v in val:
                    self._set_attr(ext, attname, v)
        return ext

    def _set_attr(self, obj, attname, val):
        # tow possible values:
        # either we get value directly
        # or a dict if it s an object or a list
        if isinstance(val, str):
            pval = xmlparser.ua_type_to_python(val, obj.ua_types[attname])
            setattr(obj, attname, pval)
        else:
            # so we have either an object or a list...
            obj2 = getattr(obj, attname)
            if isinstance(obj2, ua.NodeId):  # NodeId representation does not follow common rules!!
                for attname2, v2 in val:
                    if attname2 == "Identifier":
                        obj2 = ua.NodeId.from_string(v2)
                        setattr(obj, attname, obj2)
                        break
            elif not isinstance(obj2, ua.NodeId) and not hasattr(obj2, "ua_types"):
                # we probably have a list
                my_list = []
                for vtype, v2 in val:
                    my_list.append(xmlparser.ua_type_to_python(v2, vtype))
                setattr(obj, attname, my_list)
            else:
                for attname2, v2 in val:
                    self._set_attr(obj2, attname2, v2)
                setattr(obj, attname, obj2)

    def _add_variable_value(self, obj):
        """
        Returns the value for a Variable based on the objects value type.
        """
        self.logger.debug("Setting value with type %s and value %s", obj.valuetype, obj.value)
        if obj.valuetype == 'ListOfExtensionObject':
            values = []
            for ext in obj.value:
                extobj = self._make_ext_obj(ext)
                values.append(extobj)
            return ua.Variant(values, ua.VariantType.ExtensionObject)
        elif obj.valuetype == 'ListOfGuid':
            return ua.Variant([
                uuid.UUID(guid) for guid in obj.value
            ], getattr(ua.VariantType, obj.valuetype[6:]))
        elif obj.valuetype.startswith("ListOf"):
            vtype = obj.valuetype[6:]
            if hasattr(ua.ua_binary.Primitives, vtype):
                return ua.Variant(obj.value, getattr(ua.VariantType, vtype))
            else:
                return ua.Variant([getattr(ua, vtype)(v) for v in obj.value])
        elif obj.valuetype == 'ExtensionObject':
            extobj = self._make_ext_obj(obj.value)
            return ua.Variant(extobj, getattr(ua.VariantType, obj.valuetype))
        elif obj.valuetype == 'Guid':
            return ua.Variant(uuid.UUID(obj.value), getattr(ua.VariantType, obj.valuetype))
        elif obj.valuetype == 'LocalizedText':
            ltext = ua.LocalizedText()
            for name, val in obj.value:
                if name == "Text":
                    ltext.Text = val.encode("utf-8")
                else:
                    self.logger.warning("While parsing localizedText value, unkown element: %s with val: %s", name, val)
            return ua.Variant(ltext, ua.VariantType.LocalizedText)
        elif obj.valuetype == 'NodeId':
            return ua.Variant(ua.NodeId.from_string(obj.value))
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
        res = self._add_node(node)
        self._add_refs(obj)
        res[0].StatusCode.check()
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
        res = self._add_node(node)
        self._add_refs(obj)
        res[0].StatusCode.check()
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
        res = self._add_node(node)
        self._add_refs(obj)
        res[0].StatusCode.check()
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
        res = self._add_node(node)
        self._add_refs(obj)
        res[0].StatusCode.check()
        return res[0].AddedNodeId

    def _add_refs(self, obj):
        if not obj.refs:
            return
        refs = []
        for data in obj.refs:
            ref = ua.AddReferencesItem()
            ref.IsForward = True
            ref.ReferenceTypeId = self.to_nodeid(data.reftype)
            ref.SourceNodeId = self._migrate_ns(obj.nodeid)
            ref.TargetNodeClass = ua.NodeClass.DataType
            ref.TargetNodeId = self._migrate_ns(self.to_nodeid(data.target))
            refs.append(ref)
        self._add_references(refs)

    def _sort_nodes_by_parentid(self, ndatas):
        """
        Sort the list of nodes according their parent node in order to respect
        the dependency between nodes.

        :param nodes: list of NodeDataObjects
        :returns: list of sorted nodes
        """
        _ndatas = list(ndatas)
        # list of node ids that are already sorted / inserted
        sorted_nodes_ids = []
        # list of sorted nodes (i.e. XML Elements)
        sorted_ndatas = []
        all_node_ids = [data.nodeid for data in ndatas]
        # list of namespace indexes that are relevant for this import
        # we can only respect ordering nodes for namespaces indexes that
        # are defined in the xml file itself. Thus we assume that all other
        # references namespaces are already known to the server and should
        # not create any dependency problems (like "NodeNotFound")
        while len(_ndatas) > 0:
            pop_nodes = []
            for ndata in _ndatas:
                # Insert nodes that
                #   (1) have no parent / parent_ns is None (e.g. namespace 0)
                #   (2) ns is not in list of relevant namespaces
                if ndata.nodeid.NamespaceIndex not in self.namespaces or \
                        ndata.parent is None or \
                        ndata.parent not in all_node_ids:
                    sorted_ndatas.append(ndata)
                    sorted_nodes_ids.append(ndata.nodeid)
                    pop_nodes.append(ndata)
                else:
                    # Check if the nodes parent is already in the list of
                    # inserted nodes
                    if ndata.parent in sorted_nodes_ids:
                        sorted_ndatas.append(ndata)
                        sorted_nodes_ids.append(ndata.nodeid)
                        pop_nodes.append(ndata)
            # Remove inserted nodes from the list
            for ndata in pop_nodes:
                _ndatas.pop(_ndatas.index(ndata))
        return sorted_ndatas
