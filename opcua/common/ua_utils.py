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
    elif vtype in (ua.VariantType.SByte, ua.VariantType.ByteString):
        val = bytes(string)
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
    parents = node.get_referenced_nodes(refs=ua.ObjectIds.HasSubtype, direction=ua.BrowseDirection.Inverse, includesubtypes=True)
    if len(parents) != 0:  
        # TODO: Is it possible to have multiple subtypes ? If so extended support for it
        basetypes.append(parents[0])  
        basetypes.extend(_get_node_supertypes(parents[0]))
       
    return basetypes


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


def dtype_to_vtype(server, dtype_node):
    """
    Given a node datatype, find out the variant type to encode
    data. This is not exactly straightforward...
    """
    # first check if datatype is a simple built in type
    identifier = dtype_node.nodeid.Identifier
    if isinstance(identifier, int) and identifier <= 22:
        return ua.VariantType(identifier)
    # now handle some special cases
    parents = _get_node_supertypes(dtype_node)
    if not parents:
        raise ua.UaError("Datatype must be a subtype of builtin types")
    parent = parents[0]
    
    if parent.nodeid.Identifier == 29:
        # we have an enumeration, we need to llok at child to find type
        descs = dtype_node.get_children_descriptions()
        bnames = [d.BrowseName.Name for d in descs]
        if "EnumStrings" in bnames:
            return ua.VariantType.LocalizedText
        elif "EnumValues" in bnames:
            return ua.VariantType.ExtensionObject
        else:
            raise ua.UaError("Enumeration must have a child node describing its type and values")

    return dtype_to_vtype(server, parents[0])

