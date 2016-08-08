"""
Instantiate a new node and its child nodes from a node type.
"""


from opcua import Node
from opcua import ua
from opcua.common import ua_utils 


def instantiate(parent, node_type, nodeid=None, bname=None, idx=0):
    """
    instantiate a node type under a parent node.
    nodeid and browse name of new node can be specified, or just namespace index
    If they exists children of the node type, such as components, variables and 
    properties are also instantiated
    """

    results = node_type.get_attributes([ua.AttributeIds.NodeClass, ua.AttributeIds.BrowseName, ua.AttributeIds.DisplayName])
    nclass, qname, dname = [res.Value.Value for res in results]

    rdesc = ua.ReferenceDescription()
    rdesc.NodeId = node_type.nodeid
    rdesc.BrowseName = qname
    rdesc.DisplayName = dname
    rdesc.NodeClass = nclass
    if parent.get_type_definition() == ua.NodeId(ua.ObjectIds.FolderType):
        rdesc.ReferenceTypeId = ua.NodeId(ua.ObjectIds.Organizes)
    else:
        rdesc.ReferenceTypeId = ua.NodeId(ua.ObjectIds.HasComponent)
    rdesc.TypeDefinition = node_type.nodeid
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
    
    addnode = ua.AddNodesItem()
    addnode.RequestedNewNodeId = nodeid
    addnode.BrowseName = bname
    addnode.ParentNodeId = parentid
    addnode.ReferenceTypeId = rdesc.ReferenceTypeId
    addnode.TypeDefinition = rdesc.TypeDefinition

    node_type = Node(server, rdesc.NodeId)
    
    refs = node_type.get_referenced_nodes(refs=ua.ObjectIds.HasModellingRule)
    # skip optional elements
    if not(len(refs) == 1 and refs[0].nodeid == ua.NodeId(ua.ObjectIds.ModellingRule_Optional) ):
        
        if rdesc.NodeClass in (ua.NodeClass.Object, ua.NodeClass.ObjectType):
            addnode.NodeClass = ua.NodeClass.Object
            _read_and_copy_attrs(node_type, ua.ObjectAttributes(), addnode)

        elif rdesc.NodeClass in (ua.NodeClass.Variable, ua.NodeClass.VariableType):
            addnode.NodeClass = ua.NodeClass.Variable
            _read_and_copy_attrs(node_type, ua.VariableAttributes(), addnode)            
        elif rdesc.NodeClass in (ua.NodeClass.Method,):
            addnode.NodeClass = ua.NodeClass.Method
            _read_and_copy_attrs(node_type, ua.MethodAttributes(), addnode)
        else:
            print("Instantiate: Node class not supported: ", rdesc.NodeClass)
            return
    
        res = server.add_nodes([addnode])[0]
        
        if recursive:
            parents = ua_utils.get_node_supertypes(node_type, includeitself = True)
            node = Node(server, res.AddedNodeId)
            for parent in parents:
                descs = parent.get_children_descriptions(includesubtypes=False)
                for c_rdesc in descs:
                    # skip items that already exists, prefer the 'lowest' one in object hierarchy
                    if not ua_utils.is_child_present(node, c_rdesc.BrowseName):                    
                        _instantiate_node(server, res.AddedNodeId, c_rdesc, nodeid=ua.NodeId(namespaceidx=res.AddedNodeId.NamespaceIndex), bname=c_rdesc.BrowseName)
                    
        return Node(server, res.AddedNodeId)
    
    else:
        return None


def _read_and_copy_attrs(node_type, struct, addnode):
    names = [name for name in struct.__dict__.keys() if not name.startswith("_") and name not in ("BodyLength", "TypeId", "SpecifiedAttributes", "Encoding", "IsAbstract", "EventNotifier")]
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
            print("Instantiate: while copying attributes from node type %s, attribute %s, statuscode is %s" % (node_type, name, results[idx].StatusCode))            
    addnode.NodeAttributes = struct
