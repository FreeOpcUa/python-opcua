"""
Instanciate a node from a node type.
Can also be used to duplicate a node tree
"""


from opcua import Node
from opcua import ua


class _ReadAdder(object):
    """
    Internal
    """
    def __init__(self, server, nodeid):
        self.server = server
        self.nodeid = nodeid
        self.params = ua.ReadParameters()
        self._debug_attr = []

    def add(self, attr):
        rv = ua.ReadValueId()
        rv.NodeId = self.nodeid
        rv.AttributeId = attr
        self.params.NodesToRead.append(rv)
        self._debug_attr.append(attr)

    def read(self):
        vals = self.server.read(self.params)
        new_vals = []
        for idx, val in enumerate(vals):
            if not val.StatusCode.is_good():
                print(val)
                print("Error attribute %s is not valid for node %s" % ( self._debug_attr[idx], self.nodeid))
            #val.StatusCode.check()
            new_vals.append(val.Value.Value)
        return new_vals


#def _read_attributed(server, nodeid, attrs_obj, *attrs):
    #ra = _ReadAdder(server, rdesc.NodeId)
    #for attr in attrs:
        #ra.add(atttr)
    #vals = ra.read()

def instanciate_node(parent, node_type, idx):
    """
    Instanciate a new node under 'parent' using a type
    """
    
    results = node_type.get_attributes([ua.AttributeIds.NodeClass, ua.AttributeIds.BrowseName, ua.AttributeIds.DisplayName])
    nclass, bname, dname = [res.Value.Value for res in results]

    #descs = node_type.get_children_descriptions(refs=ua.ObjectIds.HasTypeDefinition)
    typedef = ua.FourByteNodeId(ua.ObjectIds.BaseObjectType)
    #if len(descs) > 1:
        #print("DESCS", descs)
        #typedef = descs[0].TypeDefinition

    rdesc = ua.ReferenceDescription()
    rdesc.NodeId = node_type.nodeid
    rdesc.BrowseName = bname
    rdesc.DisplayName = dname
    rdesc.NodeClass = nclass
    rdesc.ReferenceTypeId = ua.TwoByteNodeId(ua.ObjectIds.HasComponent)
    rdesc.TypeDefinition = typedef
    print("MYRDESC", rdesc)

    return _instanciate_node(parent.server, parent.nodeid, rdesc, idx)


def _instanciate_node(server, parentid, rdesc, idx):
    """
    Instanciate a new node under 'parent' using a type
    """

    print("Instanciating: node %s in %s" % (rdesc, parentid))
    addnode = ua.AddNodesItem()
    addnode.RequestedNewNodeId = ua.generate_nodeid(idx)
    addnode.BrowseName = rdesc.BrowseName
    addnode.NodeClass = rdesc.NodeClass
    addnode.ParentNodeId = parentid
    addnode.ReferenceTypeId = ua.TwoByteNodeId(ua.ObjectIds.HasComponent)
    addnode.TypeDefinition = rdesc.TypeDefinition
    print("ADDNODE", addnode)

    node_type = Node(server, rdesc.NodeId)

    if rdesc.NodeClass in (ua.NodeClass.Object, ua.NodeClass.ObjectType):
        print(node_type, " is object")
        _read_and_copy_attrs(node_type, ua.ObjectAttributes(), addnode)
        #_add_object_attrs(addnode, rdesc, node_type)

    elif rdesc.NodeClass in (ua.NodeClass.Variable, ua.NodeClass.VariableType):
        print(node_type, " is variable")
        _read_and_copy_attrs(node_type, ua.VariableAttributes(), addnode)
        #_add_variable_attrs(addnode, rdesc, node_type)

    else:
        print("Node class not supported: ", rdesc.NodeClass)

    print("ADDNODE FINAL ", addnode)
    server.add_nodes([addnode])

    refs = []
    ref = ua.AddReferencesItem()
    ref.IsForward = True
    ref.ReferenceTypeId = addnode.ReferenceTypeId
    ref.SourceNodeId = parentid
    ref.TargetNodeClass = addnode.NodeClass
    ref.TargetNodeId = addnode.RequestedNewNodeId

    refs.append(ref)
    server.add_references(refs)

    descs = node_type.get_children_descriptions(includesubtypes=False) #FIXME: should be false
    print("node is", rdesc.NodeId, node_type, node_type.get_children())
    print("Children are: ", descs)
    for rdesc in descs:
        _instanciate_node(server, addnode.RequestedNewNodeId, rdesc, idx)
    return Node(server, addnode.RequestedNewNodeId)


def _add_object_attrs(addnode, node_type):
    results = node_type.get_attributes([
        ua.AttributeIds.BrowseName,
        ua.AttributeIds.Description,
        ua.AttributeIds.WriteMask,
        ua.AttributeIds.UserWriteMask,
        ua.AttributeIds.EventNotifier])

    attrs = ua.ObjectAttributes()
    _set_attr(attrs.DisplayName, results, 0)
    _set_attr(attrs.Description, results, 0)
    attrs.DisplayName = rdesc.BrowseName
    attrs.Description = rdesc.Description
    if results[0].StatusCode.is_good():
        attrs.Description = results[0].Value.Value
    if results[1].StatusCode.is_good():
        attrs.WriteMask = results[1].Value.Value
    if results[2].StatusCode.is_good():
        attrs.UserWriteMask = results[2].Value.Value        
    if results[3].StatusCode.is_good():
        attrs.UserWriteMask = results[3].Value.Value        

    addnode.NodeAttributes = attrs


def _read_and_copy_attrs(node_type, struct, addnode):
    names = [name for name in struct.__dict__.keys() if not name.startswith("_") and name not in ("BodyLength", "TypeId", "SpecifiedAttributes", "Encoding")]
    attrs = [getattr(ua.AttributeIds, name) for name in names]
    print("Names are ", names)
    for name in names:
        results = node_type.get_attributes(attrs)
    for idx, name in enumerate(names):
        if results[idx].StatusCode.is_good():
            if name == "Value":
                setattr(struct, name, results[idx].Value)
            else:
                setattr(struct, name, results[idx].Value.Value)
        else:
            print("!!!!!!!!!!!!Error, for nodeid %s, attribute %s, statuscode is %s" % (node_type, name, results[idx].StatusCode))
    print("struct is ", struct)
    addnode.NodeAttributes = struct


def _add_variable_attrs(addnode, rdesc, node_type):
    results = node_type.get_attributes([
                ua.AttributeIds.EventNotifier,
                ua.AttributeIds.Description,
                ua.AttributeIds.WriteMask,
                ua.AttributeIds.UserWriteMask,
                ua.AttributeIds.Value,
                ua.AttributeIds.DataType,
                ua.AttributeIds.ValueRank,
                ua.AttributeIds.ArrayDimentions,
                ua.AttributeIds.AccessLevel,
                ua.AttributeIds.UserAccessLevel,
                ua.AttributeIds.MinimumSamplingInterval,
                ua.AttributeIds.Historizing])

    attrs = ua.ObjectAttributes()
    if results[0].is_good():
        attrs.DisplayName = results[0].Value.Value
    if results[1].is_good():
        attrs.Description = results[1].Value.Value
    if results[2].is_good():
        attrs.WriteMask = results[2].Value.Value
    if results[3].is_good():
        attrs.UserWriteMask = results[3].Value.Value
    #if results[4].is_good():
        #attrs.Value = results[4].Value.Value
    if results[5].is_good():
        attrs.DataType = results[5].Value.Value
    if results[6].is_good():
        attrs.ValueRank = results[6].Value.Value
    if results[7].is_good():
        attrs.ArrayDimensions = results[7].Value.Value
    if results[8].is_good():
        attrs.AccessLevel = results[8].Value.Value
    if results[9].is_good():
        attrs.UserAccessLevel = results[9].Value.Value
    if results[10].is_good():
        attrs.MinimumSamplingInterval = results[10].Value.Value
    if results[11].is_good():
        attrs.Historizing = results[11].Value.Value

    addnode.NodeAttributes = attrs

def _set_attr(container, result, idx):
    if result.is_good():
        container = result.Value.Value


