
from . import uaprotocol as ua

class Node(object):
    def __init__(self, server, nodeid):
        self.server = server
        self.nodeid = nodeid

    def __str__(self):
        return "Node({})".format(self.nodeid)
    __repr__ = __str__

    def get_name(self):
        result = self.get_attribute(ua.AttributeIds.BrowseName)
        return result.Value.Value

    def get_attribute(self, attr):
        rv = ua.ReadValueId()
        rv.NodeId = self.nodeid
        rv.AttributeId = attr
        params = ua.ReadParameters()
        params.NodesToRead.append(rv)
        result = self.server.read(params)
        print(result)
        return result[0]

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
        
