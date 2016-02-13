"""
High level functions to create nodes
"""
from opcua import ua
from opcua.common import node


def _parse_add_args(*args):
    if isinstance(args[0], ua.NodeId):
        return args[0], args[1]
    elif isinstance(args[0], str):
        return ua.NodeId.from_string(args[0]), ua.QualifiedName.from_string(args[1])
    elif isinstance(args[0], int):
        return ua.generate_nodeid(args[0]), ua.QualifiedName(args[1], args[0])
    else:
        raise TypeError("Add methods takes a nodeid and a qualifiedname as argument, received %s" % args)


def create_folder(parent, *args):
    """
    create a child node folder
    arguments are nodeid, browsename
    or namespace index, name
    """
    nodeid, qname = _parse_add_args(*args)
    return node.Node(parent.server, _create_folder(parent.server, parent.nodeid, nodeid, qname))


def create_object(parent, *args):
    """
    create a child node object
    arguments are nodeid, browsename
    or namespace index, name
    """
    nodeid, qname = _parse_add_args(*args)
    return node.Node(parent.server, _create_object(parent.server, parent.nodeid, nodeid, qname))


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
    return _create_method(parent, nodeid, qname, callback, inputs, outputs)


def _create_folder(server, parentnodeid, nodeid, qname):
    addnode = ua.AddNodesItem()
    addnode.RequestedNewNodeId = nodeid
    addnode.BrowseName = qname
    addnode.NodeClass = ua.NodeClass.Object
    addnode.ParentNodeId = parentnodeid
    addnode.ReferenceTypeId = ua.NodeId.from_string("i=35")
    addnode.TypeDefinition = ua.NodeId.from_string("i=61")
    attrs = ua.ObjectAttributes()
    attrs.Description = ua.LocalizedText(qname.Name)
    attrs.DisplayName = ua.LocalizedText(qname.Name)
    attrs.WriteMask = ua.OpenFileMode.Read
    attrs.UserWriteMask = ua.OpenFileMode.Read
    attrs.EventNotifier = 0
    addnode.NodeAttributes = attrs
    results = server.add_nodes([addnode])
    results[0].StatusCode.check()
    return nodeid


def _create_object(server, parentnodeid, nodeid, qname):
    addnode = ua.AddNodesItem()
    addnode.RequestedNewNodeId = nodeid
    addnode.BrowseName = qname
    addnode.NodeClass = ua.NodeClass.Object
    addnode.ParentNodeId = parentnodeid
    addnode.ReferenceTypeId = ua.NodeId.from_string("i=35")
    addnode.TypeDefinition = ua.NodeId(ua.ObjectIds.BaseObjectType)
    attrs = ua.ObjectAttributes()
    attrs.Description = ua.LocalizedText(qname.Name)
    attrs.DisplayName = ua.LocalizedText(qname.Name)
    attrs.EventNotifier = 0
    attrs.WriteMask = ua.OpenFileMode.Read
    attrs.UserWriteMask = ua.OpenFileMode.Read
    addnode.NodeAttributes = attrs
    results = server.add_nodes([addnode])
    results[0].StatusCode.check()
    return nodeid


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
    attrs.WriteMask = ua.OpenFileMode.Read
    attrs.UserWriteMask = ua.OpenFileMode.Read
    attrs.Historizing = 0
    addnode.NodeAttributes = attrs
    results = server.add_nodes([addnode])
    results[0].StatusCode.check()
    return nodeid


def _create_method(parent, nodeid, qname, callback, inputs, outputs):
    addnode = ua.AddNodesItem()
    addnode.RequestedNewNodeId = nodeid
    addnode.BrowseName = qname
    addnode.NodeClass = ua.NodeClass.Method
    addnode.ParentNodeId = parent.nodeid
    addnode.ReferenceTypeId = ua.NodeId.from_string("i=47")
    #node.TypeDefinition = ua.NodeId(ua.ObjectIds.BaseObjectType)
    attrs = ua.MethodAttributes()
    attrs.Description = ua.LocalizedText(qname.Name)
    attrs.DisplayName = ua.LocalizedText(qname.Name)
    attrs.WriteMask = ua.OpenFileMode.Read
    attrs.UserWriteMask = ua.OpenFileMode.Read
    attrs.Executable = True
    attrs.UserExecutable = True
    addnode.NodeAttributes = attrs
    results = parent.server.add_nodes([addnode])
    results[0].StatusCode.check()
    method = node.Node(parent.server, nodeid)
    if inputs:
        create_property(method, ua.generate_nodeid(qname.NamespaceIndex), ua.QualifiedName("InputArguments", 0), [_vtype_to_argument(vtype) for vtype in inputs])
    if outputs:
        create_property(method, ua.generate_nodeid(qname.NamespaceIndex), ua.QualifiedName("OutputArguments", 0), [_vtype_to_argument(vtype) for vtype in outputs])
    parent.server.add_method_callback(method.nodeid, callback)
    return nodeid


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


