"""
High level node object, to access node attribute
and browse address space
"""

from opcua import ua


def create_folder(parent, *args):
    """
    create a child node folder
    arguments are nodeid, browsename
    or namespace index, name
    """
    nodeid, qname = _parse_add_args(*args)
    return Node(parent.server, _create_folder(parent.server, parent.nodeid, nodeid, qname))


def create_object(parent, *args):
    """
    create a child node object
    arguments are nodeid, browsename
    or namespace index, name
    """
    nodeid, qname = _parse_add_args(*args)
    return Node(parent.server, _create_object(parent.server, parent.nodeid, nodeid, qname))


def create_property(parent, *args):
    """
    create a child node property
    args are nodeid, browsename, value, [variant type]
    or idx, name, value, [variant type]
    """
    nodeid, qname = _parse_add_args(*args[:2])
    val = _to_variant(*args[2:])
    return Node(parent.server, _create_variable(parent.server, parent.nodeid, nodeid, qname, val, isproperty=True))


def create_variable(parent, *args):
    """
    create a child node variable
    args are nodeid, browsename, value, [variant type]
    or idx, name, value, [variant type]
    """
    nodeid, qname = _parse_add_args(*args[:2])
    val = _to_variant(*args[2:])
    return Node(parent.server, _create_variable(parent.server, parent.nodeid, nodeid, qname, val, isproperty=False))


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
    if len(args) > 4:
        outputs = args[4]
    return _create_method(parent, nodeid, qname, callback, inputs, outputs)


def call_method(parent, methodid, *args):
    """
    Call an OPC-UA method. methodid is browse name of child method or the
    nodeid of method as a NodeId object
    arguments are variants or python object convertible to variants.
    which may be of different types
    returns a list of variants which are output of the method
    """
    if isinstance(methodid, str):
        methodid = parent.get_child(methodid).nodeid
    elif isinstance(methodid, Node):
        methodid = methodid.nodeid

    arguments = []
    for arg in args:
        if not isinstance(arg, ua.Variant):
            arg = ua.Variant(arg)
        arguments.append(arg)

    result = _call_method(parent.server, parent.nodeid, methodid, arguments)

    if len(result.OutputArguments) == 0:
        return None
    elif len(result.OutputArguments) == 1:
        return result.OutputArguments[0].Value
    else:
        return [var.Value for var in result.OutputArguments]


class Node(object):

    """
    High level node object, to access node attribute,
    browse and populate address space.
    Node objects are usefull as-is but they do not expose the entire possibilities of the OPC-UA protocol. Feel free to look at Node code and
    """

    def __init__(self, server, nodeid):
        self.server = server
        self.nodeid = None
        if isinstance(nodeid, ua.NodeId):
            self.nodeid = nodeid
        elif type(nodeid) in (str, bytes):
            self.nodeid = ua.NodeId.from_string(nodeid)
        elif isinstance(nodeid, int):
            self.nodeid = ua.NodeId(nodeid, 0)
        else:
            raise Exception("argument to node must be a NodeId object or a string defining a nodeid found {} of type {}".format(nodeid, type(nodeid)))

    def __eq__(self, other):
        if isinstance(other, Node) and self.nodeid == other.nodeid:
            return True
        return False

    def __str__(self):
        return "Node({})".format(self.nodeid)
    __repr__ = __str__

    def get_browse_name(self):
        """
        Get browse name of a node. A browse name is a QualifiedName object
        composed of a string(name) and a namespace index.
        """
        result = self.get_attribute(ua.AttributeIds.BrowseName)
        return result.Value.Value

    def get_display_name(self):
        """
        get description attribute of node
        """
        result = self.get_attribute(ua.AttributeIds.DisplayName)
        return result.Value.Value

    def get_data_type(self):
        """
        get data type of node
        """
        result = self.get_attribute(ua.AttributeIds.DataType)
        return result.Value.Value

    def get_node_class(self):
        """
        get node class attribute of node
        """
        result = self.get_attribute(ua.AttributeIds.NodeClass)
        return result.Value.Value

    def get_description(self):
        """
        get description attribute class of node
        """
        result = self.get_attribute(ua.AttributeIds.Description)
        return result.Value.Value

    def get_value(self):
        """
        Get value of a node as a python type. Only variables ( and properties) have values.
        An exception will be generated for other node types.
        """
        result = self.get_data_value()
        return result.Value.Value

    def get_data_value(self):
        """
        Get value of a node as a DataValue object. Only variables (and properties) have values.
        An exception will be generated for other node types.
        DataValue contain a variable value as a variant as well as server and source timestamps
        """
        return self.get_attribute(ua.AttributeIds.Value)

    def set_value(self, value, varianttype=None):
        """
        Set value of a node. Only variables(properties) have values.
        An exception will be generated for other node types.
        value argument is either:
        * a python built-in type, converted to opc-ua
        optionnaly using the variantype argument.
        * a ua.Variant, varianttype is then ignored
        * a ua.DataValue, you then have full control over data send to server
        """
        datavalue = None
        if isinstance(value, ua.DataValue):
            datavalue = value
        elif isinstance(value, ua.Variant):
            datavalue = ua.DataValue(value)
        else:
            datavalue = ua.DataValue(ua.Variant(value, varianttype))
        self.set_attribute(ua.AttributeIds.Value, datavalue)

    set_data_value = set_value

    def set_writable(self, writable=True):
        """
        Set node as writable by clients.
        A node is always writable on server side.
        """
        if writable:
            self.set_attribute(ua.AttributeIds.AccessLevel, ua.DataValue(ua.Variant(ua.AccessLevelMask.CurrentWrite, ua.VariantType.Byte)))
            self.set_attribute(ua.AttributeIds.UserAccessLevel, ua.DataValue(ua.Variant(ua.AccessLevelMask.CurrentWrite, ua.VariantType.Byte)))
        else:
            self.set_attribute(ua.AttributeIds.AccessLevel, ua.DataValue(ua.Variant(ua.AccessLevelMask.CurrentRead, ua.VariantType.Byte)))
            self.set_attribute(ua.AttributeIds.AccessLevel, ua.DataValue(ua.Variant(ua.AccessLevelMask.CurrentRead, ua.VariantType.Byte)))

    def set_read_only(self):
        """
        Set a node as read-only for clients.
        A node is always writable on server side.
        """
        return self.set_writable(False)

    def set_attribute(self, attributeid, datavalue):
        """
        Set an attribute of a node
        """
        attr = ua.WriteValue()
        attr.NodeId = self.nodeid
        attr.AttributeId = attributeid
        attr.Value = datavalue
        params = ua.WriteParameters()
        params.NodesToWrite = [attr]
        result = self.server.write(params)
        result[0].check()

    def get_attribute(self, attr):
        """
        Read one attribute of a node
        result code from server is checked and an exception is raised in case of error
        """
        rv = ua.ReadValueId()
        rv.NodeId = self.nodeid
        rv.AttributeId = attr
        params = ua.ReadParameters()
        params.NodesToRead.append(rv)
        result = self.server.read(params)
        result[0].StatusCode.check()
        return result[0]

    def get_attributes(self, attrs):
        """
        Read several attributes of a node
        list of DataValue is returned
        """
        params = ua.ReadParameters()
        for attr in attrs:
            rv = ua.ReadValueId()
            rv.NodeId = self.nodeid
            rv.AttributeId = attr
            params.NodesToRead.append(rv)

        results = self.server.read(params)
        return results

    def get_children(self, refs=ua.ObjectIds.HierarchicalReferences, nodeclassmask=ua.NodeClass.Unspecified):
        """
        Get all children of a node. By default hierarchical references and all node classes are returned.
        Other reference types may be given:
        References = 31
        NonHierarchicalReferences = 32
        HierarchicalReferences = 33
        HasChild = 34
        Organizes = 35
        HasEventSource = 36
        HasModellingRule = 37
        HasEncoding = 38
        HasDescription = 39
        HasTypeDefinition = 40
        GeneratesEvent = 41
        Aggregates = 44
        HasSubtype = 45
        HasProperty = 46
        HasComponent = 47
        HasNotifier = 48
        HasOrderedComponent = 49
        """
        references = self.get_children_descriptions(refs, nodeclassmask)
        nodes = []
        for desc in references:
            node = Node(self.server, desc.NodeId)
            nodes.append(node)
        return nodes

    def get_properties(self):
        """
        return properties of node.
        properties are child nodes with a reference of type HasProperty and a NodeClass of Variable
        """
        return self.get_children(refs=ua.ObjectIds.HasProperty, nodeclassmask=ua.NodeClass.Variable)

    def get_children_descriptions(self, refs=ua.ObjectIds.HierarchicalReferences, nodeclassmask=ua.NodeClass.Unspecified, includesubtypes=True):
        """
        return all attributes of child nodes as UA BrowseResult structs
        """
        desc = ua.BrowseDescription()
        desc.BrowseDirection = ua.BrowseDirection.Forward
        desc.ReferenceTypeId = ua.TwoByteNodeId(refs)
        desc.IncludeSubtypes = includesubtypes
        desc.NodeClassMask = nodeclassmask
        desc.ResultMask = ua.BrowseResultMask.All

        desc.NodeId = self.nodeid
        params = ua.BrowseParameters()
        params.View.Timestamp = ua.win_epoch_to_datetime(0)
        params.NodesToBrowse.append(desc)
        results = self.server.browse(params)
        return results[0].References

    def get_child(self, path):
        """
        get a child specified by its path from this node.
        A path might be:
        * a string representing a qualified name.
        * a qualified name
        * a list of string
        * a list of qualified names
        """
        if type(path) not in (list, tuple):
            path = [path]
        rpath = ua.RelativePath()
        for item in path:
            el = ua.RelativePathElement()
            el.ReferenceTypeId = ua.TwoByteNodeId(ua.ObjectIds.HierarchicalReferences)
            el.IsInverse = False
            el.IncludeSubtypes = True
            if isinstance(item, ua.QualifiedName):
                el.TargetName = item
            else:
                el.TargetName = ua.QualifiedName.from_string(item)
            rpath.Elements.append(el)
        bpath = ua.BrowsePath()
        bpath.StartingNode = self.nodeid
        bpath.RelativePath = rpath
        result = self.server.translate_browsepaths_to_nodeids([bpath])
        result = result[0]
        result.StatusCode.check()
        # FIXME: seems this method may return several nodes
        return Node(self.server, result.Targets[0].TargetId)

    def read_raw_history(self, starttime=None, endtime=None, numvalues=0, returnbounds=True):
        """
        Read raw history of a node
        result code from server is checked and an exception is raised in case of error
        """
        details = ua.ReadRawModifiedDetails()
        details.IsReadModified = False
        if starttime:
            details.StartTime = starttime
        if endtime:
            details.EndTime = endtime
        details.NumValuesPerNode = numvalues
        details.ReturnBounds = returnbounds
        return self.history_read(details)

    def history_read(self, details):
        """
        Read raw history of a node, low-level function
        result code from server is checked and an exception is raised in case of error
        """
        valueid = ua.HistoryReadValueId()
        valueid.NodeId = self.nodeid
        valueid.IndexRange = ''

        params = ua.HistoryReadParameters()
        params.HistoryReadDetails = details
        params.TimestampsToReturn = ua.TimestampsToReturn.Both
        params.ReleaseContinuationPoints = False
        params.NodesToRead.append(valueid)
        result = self.server.history_read(params)[0]
        return result.HistoryData

    # Convenience legacy methods
    add_folder = create_folder
    add_property = create_property
    add_object = create_object
    add_variable = create_variable
    add_method = create_method
    call_method = call_method


def _create_folder(server, parentnodeid, nodeid, qname):
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = nodeid
    node.BrowseName = qname
    node.NodeClass = ua.NodeClass.Object
    node.ParentNodeId = parentnodeid
    node.ReferenceTypeId = ua.NodeId.from_string("i=35")
    node.TypeDefinition = ua.NodeId.from_string("i=61")
    attrs = ua.ObjectAttributes()
    attrs.Description = ua.LocalizedText(qname.Name)
    attrs.DisplayName = ua.LocalizedText(qname.Name)
    attrs.WriteMask = ua.OpenFileMode.Read
    attrs.UserWriteMask = ua.OpenFileMode.Read
    attrs.EventNotifier = 0
    node.NodeAttributes = attrs
    results = server.add_nodes([node])
    results[0].StatusCode.check()
    return nodeid


def _create_object(server, parentnodeid, nodeid, qname):
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = nodeid
    node.BrowseName = qname
    node.NodeClass = ua.NodeClass.Object
    node.ParentNodeId = parentnodeid
    node.ReferenceTypeId = ua.NodeId.from_string("i=35")
    node.TypeDefinition = ua.NodeId(ua.ObjectIds.BaseObjectType)
    attrs = ua.ObjectAttributes()
    attrs.Description = ua.LocalizedText(qname.Name)
    attrs.DisplayName = ua.LocalizedText(qname.Name)
    attrs.EventNotifier = 0
    attrs.WriteMask = ua.OpenFileMode.Read
    attrs.UserWriteMask = ua.OpenFileMode.Read
    node.NodeAttributes = attrs
    results = server.add_nodes([node])
    results[0].StatusCode.check()
    return nodeid


def _to_variant(val, vtype=None):
    if isinstance(val, ua.Variant):
        return val
    else:
        return ua.Variant(val, vtype)


def _create_variable(server, parentnodeid, nodeid, qname, val, isproperty=False):
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = nodeid
    node.BrowseName = qname
    node.NodeClass = ua.NodeClass.Variable
    node.ParentNodeId = parentnodeid
    if isproperty:
        node.ReferenceTypeId = ua.NodeId(ua.ObjectIds.HasProperty)
        node.TypeDefinition = ua.NodeId(ua.ObjectIds.PropertyType)
    else:
        node.ReferenceTypeId = ua.NodeId(ua.ObjectIds.HasComponent)
        node.TypeDefinition = ua.NodeId(ua.ObjectIds.BaseDataVariableType)
    attrs = ua.VariableAttributes()
    attrs.Description = ua.LocalizedText(qname.Name)
    attrs.DisplayName = ua.LocalizedText(qname.Name)
    attrs.DataType = _guess_uatype(val)
    attrs.Value = val
    attrs.ValueRank = 0
    attrs.WriteMask = ua.OpenFileMode.Read
    attrs.UserWriteMask = ua.OpenFileMode.Read
    attrs.Historizing = 0
    node.NodeAttributes = attrs
    results = server.add_nodes([node])
    results[0].StatusCode.check()
    return nodeid


def _create_method(parent, nodeid, qname, callback, inputs, outputs):
    node = ua.AddNodesItem()
    node.RequestedNewNodeId = nodeid
    node.BrowseName = qname
    node.NodeClass = ua.NodeClass.Method
    node.ParentNodeId = parent.nodeid
    node.ReferenceTypeId = ua.NodeId.from_string("i=47")
    #node.TypeDefinition = ua.NodeId(ua.ObjectIds.BaseObjectType)
    attrs = ua.MethodAttributes()
    attrs.Description = ua.LocalizedText(qname.Name)
    attrs.DisplayName = ua.LocalizedText(qname.Name)
    attrs.WriteMask = ua.OpenFileMode.Read
    attrs.UserWriteMask = ua.OpenFileMode.Read
    attrs.Executable = True
    attrs.UserExecutable = True
    node.NodeAttributes = attrs
    results = parent.server.add_nodes([node])
    results[0].StatusCode.check()
    method = Node(parent.server, nodeid)
    if inputs:
        create_property(method, ua.generate_nodeid(qname.NamespaceIndex), ua.QualifiedName("InputArguments", 0), [_vtype_to_argument(vtype) for vtype in inputs])
    if outputs:
        create_property(method, ua.generate_nodeid(qname.NamespaceIndex), ua.QualifiedName("OutputArguments", 0), [_vtype_to_argument(vtype) for vtype in outputs])
    parent.server.add_method_callback(method.nodeid, callback)
    return nodeid


def _call_method(server, parentnodeid, methodid, arguments):
    request = ua.CallMethodRequest()
    request.ObjectId = parentnodeid
    request.MethodId = methodid
    request.InputArguments = arguments
    methodstocall = [request]
    results = server.call(methodstocall)
    res = results[0]
    res.StatusCode.check()
    return res


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
            raise Exception("Cannot guess DataType from Null ExtensionObject")
        if type(variant.Value) in (list, tuple):
            if len(variant.Value) == 0:
                raise Exception("Cannot guess DataType from Null ExtensionObject")
            extobj = variant.Value[0]
        else:
            extobj = variant.Value
        classname = extobj.__class__.__name__
        return ua.NodeId(getattr(ua.ObjectIds, classname))
    else:
        return ua.NodeId(getattr(ua.ObjectIds, variant.VariantType.name))


def _parse_add_args(*args):
    if isinstance(args[0], ua.NodeId):
        return args[0], args[1]
    elif isinstance(args[0], str):
        return ua.NodeId.from_string(args[0]), ua.QualifiedName.from_string(args[1])
    elif isinstance(args[0], int):
        return ua.generate_nodeid(args[0]), ua.QualifiedName(args[1], args[0])
    else:
        raise TypeError("Add methods takes a nodeid and a qualifiedname as argument, received %s" % args)
