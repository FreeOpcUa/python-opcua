"""
High level functions to create nodes
"""
from opcua import ua
from opcua.common import node


def _parse_add_args(*args):
    try:
        if isinstance(args[0], int):
            nodeid = ua.NodeId(0, int(args[0]))
            qname = ua.QualifiedName(args[1], int(args[0]))
            return nodeid, qname
        if isinstance(args[0], ua.NodeId):
            nodeid = args[0]
        elif isinstance(args[0], str):
            nodeid = ua.NodeId.from_string(args[0])
        else:
            raise RuntimeError()
        if isinstance(args[1], ua.QualifiedName):
            qname = args[1]
        elif isinstance(args[1], str):
            qname = ua.QualifiedName.from_string(args[1])
        else:
            raise RuntimeError()
        return nodeid, qname
    except ua.UaError:
        raise
    except Exception as ex:
        raise TypeError("This method takes either a namespace index and a string as argument or a nodeid and a qualifiedname. Received arguments {} and got exception {}".format(args, ex))


def create_folder(parent, *args):
    """
    create a child node folder
    arguments are nodeid, browsename
    or namespace index, name
    """
    nodeid, qname = _parse_add_args(*args)
    return node.Node(parent.server, _create_object(parent.server, parent.nodeid, nodeid, qname, ua.ObjectIds.FolderType))


def create_object(parent, *args):
    """
    create a child node object
    arguments are nodeid, browsename
    or namespace index, name
    """
    nodeid, qname = _parse_add_args(*args)
    objecttype = ua.ObjectIds.BaseObjectType
    if(len(args) == 3):
        objecttype = args[2]
        try:
            if isinstance(objecttype, int):
                objecttype = ua.NodeId(objecttype)
            elif isinstance(objecttype, ua.NodeId):
                objecttype = objecttype
            elif isinstance(objecttype, str):
                objecttype = ua.NodeId.from_string(objecttype)
            else:
                raise RuntimeError()
            return nodeid, qname
        except ua.UaError:
            raise
        except Exception as ex:
            raise TypeError("This provided objecttype takes either a index, nodeid or string. Received arguments {} and got exception {}".format(args, ex))
    return node.Node(parent.server, _create_object(parent.server, parent.nodeid, nodeid, qname, objecttype))


def create_property(parent, *args):
    """
    create a child node property
    args are nodeid, browsename, value, [variant type]
    or idx, name, value, [variant type]
    """
    nodeid, qname = _parse_add_args(*args[:2])
    val = _to_variant(*args[2:])
    return node.Node(parent.server, _create_variable(parent.server, parent.nodeid, nodeid, qname, val, isproperty=True))


def create_variable(parent, *args):
    """
    create a child node variable
    args are nodeid, browsename, value, [variant type]
    or idx, name, value, [variant type]
    """
    nodeid, qname = _parse_add_args(*args[:2])
    val = _to_variant(*args[2:])
    return node.Node(parent.server, _create_variable(parent.server, parent.nodeid, nodeid, qname, val, isproperty=False))


def create_method(parent, *args):
    """
    create a child method object
    This is only possible on server side!!
    args are nodeid, browsename, method_to_be_called, [input argument types], [output argument types]
    or idx, name, method_to_be_called, [input argument types], [output argument types]
    if argument types is specified, child nodes advertising what arguments the method uses and returns will be created
    a callback is a method accepting the nodeid of the parent as first argument and variants after. returns a list of variants
    """
    nodeid, qname = _parse_add_args(*args[:2])
    callback = args[2]
    if len(args) > 3:
        inputs = args[3]
    else:
        inputs = []
    if len(args) > 4:
        outputs = args[4]
    else:
        outputs = []
    return node.Node(parent.server, _create_method(parent, nodeid, qname, callback, inputs, outputs))


def create_subtype(parent, *args):
    """
    create a child node subtype
    arguments are nodeid, browsename
    or namespace index, name
    """
    nodeid, qname = _parse_add_args(*args)
    return node.Node(parent.server, _create_object(parent.server, parent.nodeid, nodeid, qname, None))


def _create_object(server, parentnodeid, nodeid, qname, objecttype):
    addnode = ua.AddNodesItem()
    addnode.RequestedNewNodeId = nodeid
    addnode.BrowseName = qname
    addnode.ParentNodeId = parentnodeid
    #TODO: maybe move to address_space.py and implement for all node types?
    if not objecttype:
        addnode.ReferenceTypeId = ua.NodeId(ua.ObjectIds.HasSubtype)
        addnode.NodeClass = ua.NodeClass.ObjectType
        attrs = ua.ObjectTypeAttributes()
        attrs.IsAbstract = True
    else:
        if node.Node(server, parentnodeid).get_type_definition() == ua.ObjectIds.FolderType:
            addnode.ReferenceTypeId = ua.NodeId(ua.ObjectIds.Organizes)
        else:
            addnode.ReferenceTypeId = ua.NodeId(ua.ObjectIds.HasComponent)

        addnode.NodeClass = ua.NodeClass.Object
        if isinstance(objecttype, int):
            addnode.TypeDefinition = ua.NodeId(objecttype)
        elif isinstance(objecttype, ua.NodeId):
            addnode.TypeDefinition = objecttype
        attrs = ua.ObjectAttributes()
        attrs.EventNotifier = 0

    attrs.Description = ua.LocalizedText(qname.Name)
    attrs.DisplayName = ua.LocalizedText(qname.Name)
    attrs.WriteMask = 0
    attrs.UserWriteMask = 0
    addnode.NodeAttributes = attrs
    results = server.add_nodes([addnode])
    results[0].StatusCode.check()
    return results[0].AddedNodeId


def _to_variant(val, vtype=None):
    if isinstance(val, ua.Variant):
        return val
    else:
        return ua.Variant(val, vtype)


def _create_variable(server, parentnodeid, nodeid, qname, val, isproperty=False):
    addnode = ua.AddNodesItem()
    addnode.RequestedNewNodeId = nodeid
    addnode.BrowseName = qname
    addnode.NodeClass = ua.NodeClass.Variable
    addnode.ParentNodeId = parentnodeid
    if isproperty:
        addnode.ReferenceTypeId = ua.NodeId(ua.ObjectIds.HasProperty)
        addnode.TypeDefinition = ua.NodeId(ua.ObjectIds.PropertyType)
    else:
        addnode.ReferenceTypeId = ua.NodeId(ua.ObjectIds.HasComponent)
        addnode.TypeDefinition = ua.NodeId(ua.ObjectIds.BaseDataVariableType)
    attrs = ua.VariableAttributes()
    attrs.Description = ua.LocalizedText(qname.Name)
    attrs.DisplayName = ua.LocalizedText(qname.Name)
    attrs.DataType = _guess_uatype(val)
    attrs.Value = val
    if isinstance(val, list) or isinstance(val, tuple):
        attrs.ValueRank = ua.ValueRank.OneDimension
    else:
        attrs.ValueRank = ua.ValueRank.Scalar
    #attrs.ArrayDimensions = None
    attrs.WriteMask = 0
    attrs.UserWriteMask = 0
    attrs.Historizing = 0
    attrs.AccessLevel = ua.AccessLevelMask.CurrentRead
    attrs.UserAccessLevel = ua.AccessLevelMask.CurrentRead
    addnode.NodeAttributes = attrs
    results = server.add_nodes([addnode])
    results[0].StatusCode.check()
    return results[0].AddedNodeId


def _create_method(parent, nodeid, qname, callback, inputs, outputs):
    addnode = ua.AddNodesItem()
    addnode.RequestedNewNodeId = nodeid
    addnode.BrowseName = qname
    addnode.NodeClass = ua.NodeClass.Method
    addnode.ParentNodeId = parent.nodeid
    addnode.ReferenceTypeId = ua.NodeId(ua.ObjectIds.HasComponent)
    #node.TypeDefinition = ua.NodeId(ua.ObjectIds.BaseObjectType)
    attrs = ua.MethodAttributes()
    attrs.Description = ua.LocalizedText(qname.Name)
    attrs.DisplayName = ua.LocalizedText(qname.Name)
    attrs.WriteMask = 0
    attrs.UserWriteMask = 0
    attrs.Executable = True
    attrs.UserExecutable = True
    addnode.NodeAttributes = attrs
    results = parent.server.add_nodes([addnode])
    results[0].StatusCode.check()
    method = node.Node(parent.server, results[0].AddedNodeId)
    if inputs:
        create_property(method, ua.NodeId(), ua.QualifiedName("InputArguments", 0), [_vtype_to_argument(vtype) for vtype in inputs])
    if outputs:
        create_property(method, ua.NodeId(), ua.QualifiedName("OutputArguments", 0), [_vtype_to_argument(vtype) for vtype in outputs])
    parent.server.add_method_callback(method.nodeid, callback)
    return results[0].AddedNodeId


def _vtype_to_argument(vtype):
    if isinstance(vtype, ua.Argument):
        return vtype

    arg = ua.Argument()
    v = ua.Variant(None, vtype)
    arg.DataType = _guess_uatype(v)
    return arg


def _guess_uatype(variant):
    if variant.VariantType == ua.VariantType.ExtensionObject:
        if variant.Value is None:
            raise ua.UaError("Cannot guess DataType from Null ExtensionObject")
        if type(variant.Value) in (list, tuple):
            if len(variant.Value) == 0:
                raise ua.UaError("Cannot guess DataType from Null ExtensionObject")
            extobj = variant.Value[0]
        else:
            extobj = variant.Value
        classname = extobj.__class__.__name__
        return ua.NodeId(getattr(ua.ObjectIds, classname))
    else:
        return ua.NodeId(getattr(ua.ObjectIds, variant.VariantType.name))


def delete_nodes(server, nodes, recursive=False):
    """
    Delete specified nodes. Optionally delete recursively all nodes with a
    downward hierachic references to the node
    """
    nodestodelete = []
    if recursive:
        nodes += _add_childs(nodes)
    for mynode in nodes:
        it = ua.DeleteNodesItem()
        it.NodeId = mynode.nodeid
        it.DeleteTargetReferences = True
        nodestodelete.append(it)
    return server.delete_nodes(nodestodelete)


def _add_childs(nodes):
    results = []
    for mynode in nodes[:]:
        results += mynode.get_children()
    return results


