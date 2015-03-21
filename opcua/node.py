"""
High level node object, to access node attribute 
and browse address space
"""

import opcua.uaprotocol as ua

class Node(object):
    """
    High level node object, to access node attribute 
    and browse address space
    """
    def __init__(self, server, nodeid):
        self.server = server
        self.nodeid = None
        if isinstance(nodeid, ua.NodeId):
            self.nodeid = nodeid
        elif type(nodeid) in (str, bytes):
            self.nodeid = ua.NodeId.from_string(nodeid)
        else:
            raise Exception("argument to node must be a NodeId object or a string defining a nodeid found {} of type {}".format(nodeid, type(nodeid)))
    def __eq__(self, other):
        if isinstance(other, Node) and self.nodeid == other.nodeid:
            return True
        return False

    def __str__(self):
        return "Node({})".format(self.nodeid)
    __repr__ = __str__

    def get_name(self):
        result = self.get_attribute(ua.AttributeIds.BrowseName)
        return result.Value

    def get_value(self):
        result = self.get_attribute(ua.AttributeIds.Value)
        return result.Value

    def _value(self):
        result = self.get_attribute(ua.AttributeIds.Value)
        return result.Value

    def set_value(self, value, varianttype=None):
        variant = None
        if type(value) == ua.Variant:
            variant = value
        else:
            variant = ua.Variant(value, varianttype)
        self.set_attribute(ua.AttributeIds.Value, ua.DataValue(variant))

    def set_attribute(self, attributeid, datavalue):
        attr = ua.WriteValue()
        attr.NodeId = self.nodeid
        attr.AttributeId = attributeid
        attr.Value = datavalue
        params = ua.WriteParameters()
        params.NodesToWrite = [attr]
        result = self.server.write(params)
        result[0].check()

    def get_attribute(self, attr):
        rv = ua.ReadValueId()
        rv.NodeId = self.nodeid
        rv.AttributeId = attr
        params = ua.ReadParameters()
        params.NodesToRead.append(rv)
        result = self.server.read(params)
        result[0].StatusCode.check()
        return result[0].Value

    def get_children(self):
        desc = ua.BrowseDescription()
        desc.BrowseDirection = ua.BrowseDirection.Forward
        desc.ReferenceTypeId = ua.TwoByteNodeId(ua.ObjectIds.References)
        desc.IncludeSubtypes = True
        desc.NodeClassMask = ua.NodeClass.Unspecified
        desc.ResultMask = ua.BrowseResultMask.None_
 
        desc.NodeId = self.nodeid
        params = ua.BrowseParameters()
        params.NodesToBrowse.append(desc)
        results = self.server.browse(params)
        nodes = []
        for desc in results[0].References:
            node = Node(self.server, desc.NodeId)
            nodes.append(node)
        return nodes

    def get_child(self, path):
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
                print(item, type(item))
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
        return self.add_variable(*args, isproperty=True)


    def add_variable(self, *args, isproperty=False):
        """
        create a child node variable
        args are nodeid, browsename, value, [variant type]
        or idx, name, value, [variant type]
        """
        nodeid, qname = self._parse_add_args(*args[:2])
        val = args[2]
        if type(val) is ua.Variant:
            return self._add_variable(nodeid, qname, val)
        else:
            if len(args) > 3:
                val = ua.Variant(val, args[3])
            else:
                val = ua.Variant(val)
            return self._add_variable(nodeid, qname, val, isproperty)
        
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
        attrs.DataType = self._vtype_to_uatype(val.VariantType)
        attrs.Value = val
        attrs.ValueRank = 0 
        attrs.WriteMask = 0
        attrs.UserWriteMask = 0
        attrs.Historizing = 0
        node.NodeAttributes = attrs
        results = self.server.add_nodes([node])
        results[0].StatusCode.check()
        return Node(self.server, nodeid)
     
    def _vtype_to_uatype(self, vtype):
        return eval("ua.NodeId(ua.ObjectIds.{})".format(vtype.name))

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
        

      
