"""
Usefull method and classes not belonging anywhere and depending on opcua library
"""

from dateutil import parser
from datetime import datetime
from enum import Enum, IntEnum
import uuid

from opcua import ua
from opcua.ua.uaerrors import UaError


def val_to_string(val):
    """
    convert a python object or python-opcua object to a string
    which should be easy to understand for human
    easy to modify, and not too hard to parse back ....not easy
    meant for UI or command lines

    """
    if isinstance(val, (list, tuple)):
        res = []
        for v in val:
            res.append(val_to_string(v))
        return "[" + ", ".join(res) + "]"

    if hasattr(val, "to_string"):
        val = val.to_string()
    elif isinstance(val, ua.StatusCode):
        val = val.name
    elif isinstance(val, (Enum, IntEnum)):
        val = val.name
    elif isinstance(val, ua.DataValue):
        val = variant_to_string(val.Value)
    elif isinstance(val, str):
        pass
    elif isinstance(val, bytes):
        val = str(val)
    elif isinstance(val, datetime):
        val = val.isoformat()
    elif isinstance(val, (int, float)):
        val = str(val)
    else:
        # FIXME: Some types are probably missing!
        val = str(val)
    return val


def variant_to_string(var):
    """
    convert a variant to a string which should be easy to understand for human
    easy to modify, and not too hard to parse back ....not easy
    meant for UI or command lines
    """
    return val_to_string(var.Value)


def string_to_val(string, vtype):
    """
    Convert back a string to a python or python-opcua object
    Note: no error checking is done here, supplying null strings could raise exceptions (datetime and guid)
    """
    string = string.strip()
    if string.startswith("["):
        string = string[1:-1]
        var = []
        for s in string.split(","):
            s = s.strip()
            val = string_to_val(s, vtype)
            var.append(val)
        return var

    if vtype == ua.VariantType.Null:
        val = None
    elif vtype == ua.VariantType.Boolean:
        if string in ("True", "true", "on", "On", "1"):
            val = True
        else:
            val = False
    elif vtype in (ua.VariantType.Int16, ua.VariantType.Int32, ua.VariantType.Int64):
        val = int(string)
    elif vtype in (ua.VariantType.UInt16, ua.VariantType.UInt32, ua.VariantType.UInt64):
        val = int(string)
    elif vtype in (ua.VariantType.Float, ua.VariantType.Double):
        val = float(string)
    elif vtype in (ua.VariantType.String, ua.VariantType.XmlElement):
        val = string
    elif vtype in (ua.VariantType.Byte, ua.VariantType.SByte, ua.VariantType.ByteString):
        val = string.encode("utf-8")
    elif vtype in (ua.VariantType.NodeId, ua.VariantType.ExpandedNodeId):
        val = ua.NodeId.from_string(string)
    elif vtype == ua.VariantType.QualifiedName:
        val = ua.QualifiedName.from_string(string)
    elif vtype == ua.VariantType.DateTime:
        val = parser.parse(string)
    elif vtype == ua.VariantType.LocalizedText:
        val = ua.LocalizedText(string)
    elif vtype == ua.VariantType.StatusCode:
        val = ua.StatusCode(string)
    elif vtype == ua.VariantType.Guid:
        val = uuid.UUID(string)
    else:
        # FIXME: Some types are probably missing!
        raise NotImplementedError
    return val


def string_to_variant(string, vtype):
    """
    convert back a string to an ua.Variant
    """
    return ua.Variant(string_to_val(string, vtype), vtype)


def get_node_children(node, nodes=None):
    """
    Get recursively all children of a node
    """
    if nodes is None:
        nodes = [node]
    for child in node.get_children():
        nodes.append(child)
        get_node_children(child, nodes)
    return nodes


def get_node_subtypes(node, nodes=None):
    if nodes is None:
        nodes = [node]
    for child in node.get_children(refs=ua.ObjectIds.HasSubtype):
        nodes.append(child)
        get_node_subtypes(child, nodes)
    return nodes


def get_node_supertypes(node, includeitself=False, skipbase=True):
    """
    return get all subtype parents of node recursive
    :param node: can be a ua.Node or ua.NodeId
    :param includeitself: include also node to the list
    :param skipbase don't include the toplevel one
    :returns list of ua.Node, top parent first 
    """
    parents = []
    if includeitself:
        parents.append(node)
    parents.extend(_get_node_supertypes(node))
    if skipbase and len(parents) > 1:
        parents = parents[:-1]

    return parents


def _get_node_supertypes(node):
    """
    recursive implementation of get_node_derived_from_types
    """
    basetypes = []
    parent = get_node_supertype(node)
    if parent:
        basetypes.append(parent)
        basetypes.extend(_get_node_supertypes(parent))

    return basetypes


def get_node_supertype(node):
    """
    return node supertype or None
    """
    supertypes = node.get_referenced_nodes(refs=ua.ObjectIds.HasSubtype,
                                           direction=ua.BrowseDirection.Inverse,
                                           includesubtypes=True)
    if supertypes:
        return supertypes[0]
    else:
        return None


def is_child_present(node, browsename):
    """
    return if a browsename is present a child from the provide node
    :param node: node wherein to find the browsename
    :param browsename: browsename to search
    :returns returne True if the browsename is present else False 
    """
    child_descs = node.get_children_descriptions()
    for child_desc in child_descs:
        if child_desc.BrowseName == browsename:
            return True

    return False


def data_type_to_variant_type(dtype_node):
    """
    Given a Node datatype, find out the variant type to encode
    data. This is not exactly straightforward...
    """
    base = get_base_data_type(dtype_node)

    if base.nodeid.Identifier != 29:
        return ua.VariantType(base.nodeid.Identifier)
    else:
        # we have an enumeration, we need to look at child to find type
        descs = dtype_node.get_children_descriptions()
        bnames = [d.BrowseName.Name for d in descs]
        if "EnumStrings" in bnames:
            return ua.VariantType.LocalizedText
        elif "EnumValues" in bnames:
            return ua.VariantType.ExtensionObject
        else:
            raise ua.UaError("Enumeration must have a child node describing its type and values")


def get_base_data_type(datatype):
    """
    Looks up the base datatype of the provided datatype Node
    The base datatype is either:
    A primitive type (ns=0, i<=21) or a complex one (ns=0 i>21 and i<=30) like Enum and Struct.
    
    Args:
        datatype: NodeId of a datype of a variable
    Returns:
        NodeId of datatype base or None in case base datype can not be determined
    """
    base = datatype
    while base:
        if base.nodeid.NamespaceIndex == 0 and isinstance(base.nodeid.Identifier, int) and base.nodeid.Identifier <= 30:
            return base
        base = get_node_supertype(base)
    raise ua.UaError("Datatype must be a subtype of builtin types {0!s}".format(datatype))


def get_nodes_of_namespace(server, namespaces=None):
    """
    Get the nodes of one or more namespaces .      
    Args:
        server: opc ua server to use
        namespaces: list of string uri or int indexes of the namespace to export
    Returns:
        List of nodes that are part of the provided namespaces
    """
    if namespaces is None:
        namespaces = []
    ns_available = server.get_namespace_array()

    if not namespaces:
        namespaces = ns_available[1:]
    elif isinstance(namespaces, (str, int)):
        namespaces = [namespaces]

    # make sure all namespace are indexes (if needed convert strings to indexes)
    namespace_indexes = [n if isinstance(n, int) else ns_available.index(n) for n in namespaces]

    # filter nodeis based on the provide namespaces and convert the nodeid to a node
    nodes = [server.get_node(nodeid) for nodeid in server.iserver.aspace.keys()
             if nodeid.NamespaceIndex != 0 and nodeid.NamespaceIndex in namespace_indexes]
    return nodes
