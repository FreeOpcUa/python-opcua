"""
instantiate a node from a node type.
Can also be used to duplicate a node tree
"""


from opcua import Node
from opcua import ua


def instantiate(parent, node_type, nodeid=None, bname=None, idx=0):
    """
    instantiate a node type under a parent node.
    nodeid and browse name of new node can be specified, or just namespace index
    """

    results = node_type.get_attributes([ua.AttributeIds.NodeClass, ua.AttributeIds.BrowseName, ua.AttributeIds.DisplayName])
    nclass, qname, dname = [res.Value.Value for res in results]

    rdesc = ua.ReferenceDescription()
    rdesc.NodeId = node_type.nodeid
    rdesc.BrowseName = qname
    rdesc.DisplayName = dname
    rdesc.NodeClass = nclass
    rdesc.ReferenceTypeId = ua.TwoByteNodeId(ua.ObjectIds.HasComponent)
    rdesc.TypeDefinition = node_type.nodeid
    print("MYRDESC", rdesc)
    if nodeid is None:
        nodeid = ua.NodeId(namespaceidx=idx)  # will trigger automatic node generation in namespace idx
    if bname is None:
        bname = rdesc.BrowseName
    elif isinstance(bname, str):
        bname = ua.QualifiedName.from_string(bname)

    return _instantiate_node(parent.server, parent.nodeid, rdesc, nodeid, bname)


def _instantiate_node(server, parentid, rdesc, nodeid, bname, recursive=True):
    """
    instantiate a node type under parent
    """

    print("\n\nInstanciating: node %s in %s" % (nodeid, parentid))
    print(rdesc)
    addnode = ua.AddNodesItem()
    addnode.RequestedNewNodeId = nodeid 
    addnode.BrowseName = bname 
    addnode.ParentNodeId = parentid
    addnode.ReferenceTypeId = rdesc.ReferenceTypeId
    addnode.TypeDefinition = rdesc.TypeDefinition

    node_type = Node(server, rdesc.NodeId)

    if rdesc.NodeClass in (ua.NodeClass.Object, ua.NodeClass.ObjectType):
        addnode.NodeClass = ua.NodeClass.Object
        _read_and_copy_attrs(node_type, ua.ObjectAttributes(), addnode)

    elif rdesc.NodeClass in (ua.NodeClass.Variable, ua.NodeClass.VariableType):
        addnode.NodeClass = ua.NodeClass.Variable
        _read_and_copy_attrs(node_type, ua.VariableAttributes(), addnode)

    else:
        print("Node class not supported: ", rdesc.NodeClass)

    res = server.add_nodes([addnode])[0]

    if recursive:
        descs = node_type.get_children_descriptions(includesubtypes=False)
        for c_rdesc in descs:
            print("       Instanciating children", c_rdesc)
            _instantiate_node(server, res.AddedNodeId, c_rdesc, nodeid=ua.NodeId(namespaceidx=res.AddedNodeId.NamespaceIndex), bname=c_rdesc.BrowseName)
    return Node(server, addnode.RequestedNewNodeId)


def _read_and_copy_attrs(node_type, struct, addnode):
    names = [name for name in struct.__dict__.keys() if not name.startswith("_") and name not in ("BodyLength", "TypeId", "SpecifiedAttributes", "Encoding", "IsAbstract")]
    attrs = [getattr(ua.AttributeIds, name) for name in names]
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
    addnode.NodeAttributes = struct

