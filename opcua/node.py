"""
High level node object, to access node attribute 
and browse address space
"""

import opcua.uaprotocol as ua

class Node(object):
    """
    High level node object, to access node attribute,
    browse and populate address space
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
        return result.Value

    def get_display_name(self):
        """
        get description attribute of node
        """
        result = self.get_attribute(ua.AttributeIds.DisplayName)
        return result.Value

    def get_node_class(self):
        """
        get node class attribute of node
        """
        result = self.get_attribute(ua.AttributeIds.NodeClass)
        return result.Value

    def get_description(self):
        """
        get description attribute class of node
        """
        result = self.get_attribute(ua.AttributeIds.Description)
        return result.Value

    def get_value(self):
        """
        Get value of a node. Only variables(properties) have values. 
        An exception will be generated for other node types.
        """
        result = self.get_attribute(ua.AttributeIds.Value)
        return result.Value

    def set_value(self, value, varianttype=None):
        """
        Set value of a node. Only variables(properties) have values. 
        An exception will be generated for other node types.
        """
        variant = None
        if type(value) == ua.Variant:
            variant = value
        else:
            variant = ua.Variant(value, varianttype)
        self.set_attribute(ua.AttributeIds.Value, ua.DataValue(variant))

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
        Get an attribute of a node
        """
        rv = ua.ReadValueId()
        rv.NodeId = self.nodeid
        rv.AttributeId = attr
        params = ua.ReadParameters()
        params.NodesToRead.append(rv)
        result = self.server.read(params)
        result[0].StatusCode.check()
        return result[0].Value

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
        desc = ua.BrowseDescription()
        desc.BrowseDirection = ua.BrowseDirection.Forward
        desc.ReferenceTypeId = ua.TwoByteNodeId(refs)
        desc.IncludeSubtypes = includesubtypes
        desc.NodeClassMask = nodeclassmask
        desc.ResultMask = ua.BrowseResultMask.All
 
        desc.NodeId = self.nodeid
        params = ua.BrowseParameters()
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
            if type(item) == ua.QualifiedName:
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
        #FIXME: seems this method may return several nodes
        return Node(self.server, result.Targets[0].TargetId)

    def add_folder(self, *args):
        """
        create a child node folder
        arguments are nodeid, browsename
        or namespace index, name
        """
        nodeid, qname = self._parse_add_args(*args)
        return self._add_folder(nodeid, qname)
    
    def _add_folder(self, nodeid, qname):
        node = ua.AddNodesItem()
        node.RequestedNewNodeId = nodeid 
        node.BrowseName = qname 
        node.NodeClass = ua.NodeClass.Object
        node.ParentNodeId = self.nodeid
        node.ReferenceTypeId = ua.NodeId.from_string("i=35")
        node.TypeDefinition = ua.NodeId.from_string("i=61")
        attrs = ua.ObjectAttributes()
        attrs.Description = ua.LocalizedText(qname.Name)
        attrs.DisplayName = ua.LocalizedText(qname.Name)
        attrs.EventNotifier = 0
        node.NodeAttributes = attrs
        results = self.server.add_nodes([node])
        results[0].StatusCode.check()
        return Node(self.server, nodeid)
 
    def add_object(self, *args):
        """
        create a child node object
        arguments are nodeid, browsename
        or namespace index, name
        """
        nodeid, qname = self._parse_add_args(*args)
        return self._add_object(nodeid, qname)
    
    def _add_object(self, nodeid, qname):
        node = ua.AddNodesItem()
        node.RequestedNewNodeId = nodeid 
        node.BrowseName = qname 
        node.NodeClass = ua.NodeClass.Object
        node.ParentNodeId = self.nodeid 
        node.ReferenceTypeId = ua.NodeId.from_string("i=35")
        node.TypeDefinition = ua.NodeId(ua.ObjectIds.BaseObjectType)
        attrs = ua.ObjectAttributes()
        attrs.Description = ua.LocalizedText(qname.Name)
        attrs.DisplayName = ua.LocalizedText(qname.Name)
        attrs.EventNotifier = 0
        node.NodeAttributes = attrs
        results = self.server.add_nodes([node])
        results[0].StatusCode.check()
        return Node(self.server, nodeid)

    def add_property(self, *args):
        """
        create a child node property
        args are nodeid, browsename, value, [variant type]
        or idx, name, value, [variant type]
        """
        nodeid, qname = self._parse_add_args(*args[:2])
        val = self._to_variant(*args[2:])
        return self._add_variable(nodeid, qname, val, isproperty=True)
        
    def add_variable(self, *args):
        """
        create a child node variable
        args are nodeid, browsename, value, [variant type]
        or idx, name, value, [variant type]
        """
        nodeid, qname = self._parse_add_args(*args[:2])
        val = self._to_variant(*args[2:])
        return self._add_variable(nodeid, qname, val, isproperty=False)

    def _to_variant(self, val, vtype=None):
        if isinstance(val, ua.Variant):
            return val
        else:
            return ua.Variant(val, vtype)

    def _add_variable(self, nodeid, qname, val, isproperty=False):
        node = ua.AddNodesItem()
        node.RequestedNewNodeId = nodeid 
        node.BrowseName = qname 
        node.NodeClass = ua.NodeClass.Variable
        node.ParentNodeId = self.nodeid 
        if isproperty:
            node.ReferenceTypeId = ua.NodeId(ua.ObjectIds.HasProperty)
            node.TypeDefinition = ua.NodeId(ua.ObjectIds.PropertyType)
        else:
            node.ReferenceTypeId = ua.NodeId(ua.ObjectIds.HasComponent)
            node.TypeDefinition = ua.NodeId(ua.ObjectIds.BaseDataVariableType)
        attrs = ua.VariableAttributes()
        attrs.Description = ua.LocalizedText(qname.Name)
        attrs.DisplayName = ua.LocalizedText(qname.Name)
        attrs.DataType = self._guess_uatype(val)
        attrs.Value = val
        attrs.ValueRank = 0 
        attrs.WriteMask = 0
        attrs.UserWriteMask = 0
        attrs.Historizing = 0
        node.NodeAttributes = attrs
        results = self.server.add_nodes([node])
        results[0].StatusCode.check()
        return Node(self.server, nodeid)

    def add_method(self, *args):
        """
        create a child method object
        This is only possible on server side!!
        args are nodeid, browsename, method_to_be_called, [input argument types], [output argument types]
        or idx, name, method_to_be_called, [input argument types], [output argument types]
        if argument types is specified, child nodes advertising what arguments the method uses and returns will be created
        a callback is a method accepting the nodeid of the parent as first argument and variants after. returns a list of variants
        """
        nodeid, qname = self._parse_add_args(*args[:2])
        callback = args[2]
        if len(args) > 3:
            inputs = args[3] 
        if len(args) > 4:
            outputs = args[4] 
        return self._add_method(nodeid, qname, callback, inputs, outputs)
    
    def _add_method(self, nodeid, qname, callback, inputs, outputs):
        node = ua.AddNodesItem()
        node.RequestedNewNodeId = nodeid 
        node.BrowseName = qname 
        node.NodeClass = ua.NodeClass.Method
        node.ParentNodeId = self.nodeid 
        node.ReferenceTypeId = ua.NodeId.from_string("i=47")
        #node.TypeDefinition = ua.NodeId(ua.ObjectIds.BaseObjectType)
        attrs = ua.MethodAttributes()
        attrs.Description = ua.LocalizedText(qname.Name)
        attrs.DisplayName = ua.LocalizedText(qname.Name)
        attrs.WriteMask = 0
        attrs.UserWriteMask = 0
        attrs.Executable = True
        attrs.UserExecutable = True
        node.NodeAttributes = attrs
        results = self.server.add_nodes([node])
        results[0].StatusCode.check()
        method = Node(self.server, nodeid)
        if inputs:
            method.add_property(qname.NamespaceIndex, "InputArguments", [self._vtype_to_argument(vtype) for vtype in inputs])
        if outputs:
            method.add_property(qname.NamespaceIndex, "OutputArguments", [self._vtype_to_argument(vtype) for vtype in inputs])
        self.server.add_method_callback(method.nodeid, callback)
        return method
        

    def call_method(self, methodid, *args):
        """
        Call an OPC-UA method. methodid is browse name of child method or the 
        nodeid of method as a NodeId object 
        arguments are variants or python object convertible to variants.
        which may be of different types
        returns a list of variants which are output of the method 
        """
        if type(methodid) is str:
            methodid = self.get_child(methodid).nodeid
        elif type(methodid) is Node:
            methodid = methodid.nodeid

        arguments = []
        for arg in args:
            if not isinstance(arg, ua.Variant):
                arg = ua.Variant(arg)
            arguments.append(arg)

        request = ua.CallMethodRequest()
        request.ObjectId = self.nodeid
        request.MethodId = methodid
        request.InputArguments = arguments
        methodstocall = [request]
        results = self.server.call(methodstocall)
        res = results[0]
        res.StatusCode.check()
        if len(res.OutputArguments) == 0:
            return None
        elif len(res.OutputArguments) == 1:
            return res.OutputArguments[0].Value
        else:
            return [var.Value for var in res.OutputArguments]

    def _vtype_to_argument(self, vtype):
        arg = ua.Argument()
        v = ua.Variant(None, vtype)
        arg.DataType = self._guess_uatype(v)
        return ua.ExtensionObject.from_object(arg)

    def _guess_uatype(self, variant):
        if variant.VariantType == ua.VariantType.ExtensionObject:
            if variant.Value is None:
                raise Exception("Cannot guess DataType from Null ExtensionObject")
            if type(variant.Value) in (list, tuple):
                if len(variant.Value) == 0:
                    raise Exception("Cannot guess DataType from Null ExtensionObject")
                extobj = variant.Value[0]
            else:
                extobj = variant.Value
            objectidname = ua.ObjectIdsInv[extobj.TypeId.Identifier]
            classname = objectidname.split("_")[0]
            return eval("ua.NodeId(ua.ObjectIds.{})".format(classname))
        else:
            return eval("ua.NodeId(ua.ObjectIds.{})".format(variant.VariantType.name))

    def _parse_add_args(self, *args):
        if type(args[0]) is ua.NodeId:
            return args[0], args[1]
        elif type(args[0]) is str:
            return ua.NodeId.from_string(args[0]), ua.QualifiedName.from_string(args[1])
        elif type(args[0]) is int:
            return generate_nodeid(args[0]), ua.QualifiedName(args[1], args[0])
        else:
            raise TypeError("Add methods takes a nodeid and a qualifiedname as argument, received %s" % args)


__nodeid_counter = 2000
def generate_nodeid(idx):
    global __nodeid_counter
    __nodeid_counter += 1
    return ua.NodeId(__nodeid_counter, idx)
        

      
