"""
Instantiate a new node and its child nodes from a node type.
"""


from opcua import Node
from opcua import ua
from opcua.common import ua_utils
from opcua.common.copy_node import _rdesc_from_node, _read_and_copy_attrs


def instantiate(parent, node_type, nodeid=None, bname=None, idx=0):
    """
    instantiate a node type under a parent node.
    nodeid and browse name of new node can be specified, or just namespace index
    If they exists children of the node type, such as components, variables and
    properties are also instantiated
    """
    rdesc = _rdesc_from_node(parent, node_type)
    rdesc.TypeDefinition = node_type.nodeid

    if nodeid is None:
        nodeid = ua.NodeId(namespaceidx=idx)  # will trigger automatic node generation in namespace idx
    if bname is None:
        bname = rdesc.BrowseName
    elif isinstance(bname, str):
        bname = ua.QualifiedName.from_string(bname)

    nodeids = _instantiate_node(parent.server, parent.nodeid, rdesc, nodeid, bname)
    return [Node(parent.server, nid) for nid in nodeids]


def _instantiate_node(server, parentid, rdesc, nodeid, bname, recursive=True):
    """
    instantiate a node type under parent
    """
    node_type = Node(server, rdesc.NodeId)
    refs = node_type.get_referenced_nodes(refs=ua.ObjectIds.HasModellingRule)

    # skip optional elements
    if len(refs) == 1 and refs[0].nodeid == ua.NodeId(ua.ObjectIds.ModellingRule_Optional):
        return []

    addnode = ua.AddNodesItem()
    addnode.RequestedNewNodeId = nodeid
    addnode.BrowseName = bname
    addnode.ParentNodeId = parentid
    addnode.ReferenceTypeId = rdesc.ReferenceTypeId
    addnode.TypeDefinition = rdesc.TypeDefinition

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
    added_nodes = [res.AddedNodeId]

    if recursive:
        parents = ua_utils.get_node_supertypes(node_type, includeitself=True)
        node = Node(server, res.AddedNodeId)
        for parent in parents:
            descs = parent.get_children_descriptions(includesubtypes=False)
            for c_rdesc in descs:
                # skip items that already exists, prefer the 'lowest' one in object hierarchy
                if not ua_utils.is_child_present(node, c_rdesc.BrowseName):
                    # if root node being instantiated has a String NodeId, create the children with a String NodeId
                    if res.AddedNodeId.NodeIdType is ua.NodeIdType.String:
                        inst_nodeid = res.AddedNodeId.Identifier + "." + c_rdesc.BrowseName.Name
                        nodeids = _instantiate_node(server, res.AddedNodeId, c_rdesc, nodeid=ua.NodeId(identifier=inst_nodeid, namespaceidx=res.AddedNodeId.NamespaceIndex), bname=c_rdesc.BrowseName)
                    else:
                        nodeids = _instantiate_node(server, res.AddedNodeId, c_rdesc, nodeid=ua.NodeId(namespaceidx=res.AddedNodeId.NamespaceIndex), bname=c_rdesc.BrowseName)
                    added_nodes.extend(nodeids)

    return added_nodes


