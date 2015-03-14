
import logging

from opcua import ua

class AttributeValue(object):
    def __init__(self, attr, value):
        self.attr = attr
        self.value = value
        self.value_callback = None 
        self.data_change_callback = None 

class NodeData(object):
    def __init__(self, nodeid):
        self.nodeid = nodeid
        self.attributes = {}
        self.references = []

class AddressSpace(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.nodes = {}


    def add_nodes(self, addnodeitems):
        results = []
        for item in addnodeitems:
            results.append(self.add_node(item))
        return results

    def add_node(self, item):
        result = ua.AddNodesResult()

        if item.RequestedNodeId in self.nodes:
            self.logger.warn("AddNodeItem: node already exists")
            result.StatusCode = ua.StatusCode(ua.StatusCodes.BadNodeIdExists)
            return result
        nodedata = NodeData(item.RequestedNodeId)
        #add common attrs
        #nodedata.attributes[ua.AttributeIds.BrowseName] = ua.Variant(item.BrowseName, ua.VariantType.QualifiedName)
        #nodedata.attributes[ua.AttributeIds.NodeClass] = ua.Variant(item.NodeClass, ua.VariantType.Int32)
        #add requested attrs
        self._add_nodeattributes(item.Attributes, nodedata)

        self.nodes[item.RequestedNodeId] = nodedata

        if item.ParentNodeId == ua.NodeId():
            self.logger.warn("creating node without parent: %s", item.RequestedNodeId) 
        elif not item.ParentNodeId in self.nodes:
            self.logger.warn("requeste parent node does not exists: %s", item.RequestedNodeId) 
        else:
            desc = ua.ReferenceDescription()
            desc.ReferenceTypeId = item.ReferenceTypeId
            desc.NodeId = item.RequestedNodeId
            desc.NodeClass = item.NodeClass
            desc.BrowseName = item.BrowseName
            desc.DisplayName = ua.LocalizedText(item.BrowseName.Name)
            desc.TargetNodeTypeDefinition = item.TypeDefinition
            desc.IsForward = True

            self.nodes[item.ParentNodeId].References.append(desc)

        #type definition
        addref = ua.AddReferencesItem()
        addref.SourceNodeId = item.RequestedNodeId
        addref.IsForward = True
        addref.ReferenceTypeId = ua.ObjectIds.HasTypeDefinition
        addref.NodeId = item.TypeDefinition
        addref.NodeClass = ua.NodeClass.DataType
        self.add_references(addref)

        result.StatusCode = ua.StatusCode()
        result.AddedNodeId = item.RequestedNodeId
        self.logger.info("Node %s added", item.RequestedNodeId)

        return result

    def add_references(self, addref):
        if not addref.SourceNodeId in self.nodes:
            self.logger.warn("source node does not exists")
            return ua.StatusCode(ua.StatusCodes.BadSourceNodeIdInvalid)
        if not addref.TargetNodeId in self.nodes:
            self.logger.warn("target node does not exists")
            return ua.StatusCode(ua.StatusCodes.BadTargetNodeIdInvalid)
        rdesc = ua.ReferenceDescription()
        rdesc.ReferencetypeId = addref.ReferenceTypeId
        rdesc.IsForware = addref.IsForward
        rdesc.NodeId = addref.TargetModeId
        rdesc.NodeClass = addref.NodeClass
        rdesc.BrowseName = self.get_attribute_value(addref.TargetNodeId, ua.AttributeIds.BrowseName)
        rdesc.DisplayName = self.get_attribute_value(addref.TargetNodeId, ua.AttributeIds.DisplayName)
        self.nodes[addref.TargetNodeId].references.append(rdesc)

    def get_attribute_value(self, nodeid, attr):
        dv = ua.DataValue()
        if not nodeid in self.nodes:
            dv.StatusCode = ua.StatusCode(ua.StatusCodes.BadNodeIdUnknown)
            return dv
        node = self.nodes[nodeid]
        if not attr in node.attributes:
            dv.StatusCode = ua.StatusCode(ua.StatusCodes.BadAttributeIdInvalid)
            return dv
        attval = node.Attributes[attr]
        if attval.value_callback:
            return attval.value_callback()
        return attval.value

    def set_attribute_value(self, nodeid, attr, value):
        if not nodeid in self.nodes:
            return ua.StatusCode(ua.StatusCodes.BadNodeIdUnknown)
        node = self.nodes[nodeid]
        if not attr in node.attributes:
            return ua.StatusCode(ua.StatusCodes.BadAttributeIdInvalid)
        attval = self.nodes[nodeid].Attributes[attr]
        attval.value = value
        if attval.datachange_callback:
            return attval.value_callback(nodeid, attr, value)
        return ua.StatusCode()

    def _add_nodeattributes(self, item, nodedata):
        item = ua.downcast_extobject(item)
        if item.SpecifiedAttributes & ua.NodeAttributesMask.AccessLevel:
            nodedata.attributes[ua.AttributeIds.AccessLevel] = ua.DataValue(ua.Variant(item.AccessLevel, ua.VariantType.Byte))
        if item.SpecifiedAttributes & ua.NodeAttributesMask.ArrayDimensions:
            nodedata.attributes[ua.AttributeIds.ArrayDimensions] = ua.DataValue(ua.Variant(item.ArrayDimensions, ua.VariantType.Int32))
        if item.SpecifiedAttributes & ua.NodeAttributesMask.BrowseName:
            nodedata.attributes[ua.AttributeIds.BrowseName] = ua.DataValue(ua.Variant(item.BrowseName, ua.VariantType.QualifiedName))
        if item.SpecifiedAttributes & ua.NodeAttributesMask.ContainsNoLoops:
            nodedata.attributes[ua.AttributeIds.ContainsNoLoops] = ua.DataValue(ua.Variant(item.ContainsNoLoops, ua.VariantType.Boolean))
        if item.SpecifiedAttributes & ua.NodeAttributesMask.DataType:
            nodedata.attributes[ua.AttributeIds.DataType] = ua.DataValue(ua.Variant(item.DataType, ua.VariantType.NodeId))
        if item.SpecifiedAttributes & ua.NodeAttributesMask.DataType:
            nodedata.attributes[ua.AttributeIds.Description] = ua.DataValue(ua.Variant(item.Description, ua.VariantType.LocalizedText))
        if item.SpecifiedAttributes & ua.NodeAttributesMask.DisplayName:
            nodedata.attributes[ua.AttributeIds.DisplayName] = ua.DataValue(ua.Variant(item.DisplayName, ua.VariantType.LocalizedText))
        if item.SpecifiedAttributes & ua.NodeAttributesMask.EventNotifier:
            nodedata.attributes[ua.AttributeIds.EventNotifier] = ua.DataValue(ua.Variant(item.EventNotifier, ua.VariantType.Boolean))
        if item.SpecifiedAttributes & ua.NodeAttributesMask.Executable:
            nodedata.attributes[ua.AttributeIds.Executable] = ua.DataValue(ua.Variant(item.Executable, ua.VariantType.Boolean))
        if item.SpecifiedAttributes & ua.NodeAttributesMask.Historizing:
            nodedata.attributes[ua.AttributeIds.Historizing] = ua.DataValue(ua.Variant(item.Historizing, ua.VariantType.Boolean))
        if item.SpecifiedAttributes & ua.NodeAttributesMask.InverseName:
            nodedata.attributes[ua.AttributeIds.InverseName] = ua.DataValue(ua.Variant(item.InverseName, ua.VariantType.LocalizedText))
        if item.SpecifiedAttributes & ua.NodeAttributesMask.IsAbstract:
            nodedata.attributes[ua.AttributeIds.IsAbstract] = ua.DataValue(ua.Variant(item.IsAbstract, ua.VariantType.Boolean))
        if item.SpecifiedAttributes & ua.NodeAttributesMask.MinimumSamplingInterval:
            nodedata.attributes[ua.AttributeIds.MinimumSamplingInterval] = ua.DataValue(ua.Variant(item.MinimumSamplingInterval, ua.VariantType.Double))
        if item.SpecifiedAttributes & ua.NodeAttributesMask.NodeClass:
            nodedata.attributes[ua.AttributeIds.NodeClass] = ua.DataValue(ua.Variant(item.NodeClass, ua.VariantType.UInt32))
        if item.SpecifiedAttributes & ua.NodeAttributesMask.NodeId:
            nodedata.attributes[ua.AttributeIds.NodeId] = ua.DataValue(ua.Variant(item.NodeId, ua.VariantType.NodeId))
        if item.SpecifiedAttributes & ua.NodeAttributesMask.Symmetric:
            nodedata.attributes[ua.AttributeIds.Symmetric] = ua.DataValue(ua.Variant(item.Symmetric, ua.VariantType.Boolean))
        if item.SpecifiedAttributes & ua.NodeAttributesMask.UserAccessLevel:
            nodedata.attributes[ua.AttributeIds.UserAccessLevel] = ua.DataValue(ua.Variant(item.UserAccessLevel, ua.VariantType.Byte))
        if item.SpecifiedAttributes & ua.NodeAttributesMask.UserExecutable:
            nodedata.attributes[ua.AttributeIds.UserExecutable] = ua.DataValue(ua.Variant(item.UserExecutable, ua.VariantType.Boolean))
        if item.SpecifiedAttributes & ua.NodeAttributesMask.UserWriteMask:
            nodedata.attributes[ua.AttributeIds.UserWriteMask] = ua.DataValue(ua.Variant(item.UserWriteMask, ua.VariantType.Byte))
        if item.SpecifiedAttributes & ua.NodeAttributesMask.ValueRank:
            nodedata.attributes[ua.AttributeIds.ValueRank] = ua.DataValue(ua.Variant(item.ValueRank, ua.VariantType.Int32))
        if item.SpecifiedAttributes & ua.NodeAttributesMask.WriteMask:
            nodedata.attributes[ua.AttributeIds.WriteMask] = ua.DataValue(ua.Variant(item.WriteMask, ua.VariantType.Byte))
        if item.SpecifiedAttributes & ua.NodeAttributesMask.Value:
            nodedata.attributes[ua.AttributeIds.Value] = ua.DataValue(item.Value)


            
            

