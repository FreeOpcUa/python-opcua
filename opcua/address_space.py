from threading import RLock
import logging

from opcua import ua

class DataChangeCallbackData(object):
    def __init__(self):
        self.callback = None
        self.client_handle = None

class AttributeValue(object):
    def __init__(self, value):
        self.value = value
        self.value_callback = None 
        self.datachange_callbacks = {} 

    def __str__(self):
        return "AttributeValue({})".format(self.value)
    __repr__ = __str__

class NodeData(object):
    def __init__(self, nodeid):
        self.nodeid = nodeid
        self.attributes = {}
        self.references = []

    def __str__(self):
        return "NodeData(id:{}, attrs:{}, refs:{})".format(self.nodeid, self.attributes, self.references)
    __repr__ = __str__

class AddressSpace(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self._nodes = {}
        self._lock = RLock() #FIXME: should use multiple reader, one writter pattern
        self._datachange_callback_counter = 200
        self._handle_to_attribute_map = {}


    def add_nodes(self, addnodeitems):
        results = []
        for item in addnodeitems:
            results.append(self._add_node(item))
        return results

    def _add_node(self, item):
        with self._lock:
            result = ua.AddNodesResult()

            if item.RequestedNewNodeId in self._nodes:
                self.logger.warning("AddNodeItem: node already exists")
                result.StatusCode = ua.StatusCode(ua.StatusCodes.BadNodeIdExists)
                return result
            nodedata = NodeData(item.RequestedNewNodeId)
            #add common attrs
            nodedata.attributes[ua.AttributeIds.NodeId] = AttributeValue(ua.DataValue(ua.Variant(item.RequestedNewNodeId, ua.VariantType.NodeId)))
            nodedata.attributes[ua.AttributeIds.BrowseName] = AttributeValue(ua.DataValue(ua.Variant(item.BrowseName, ua.VariantType.QualifiedName)))
            nodedata.attributes[ua.AttributeIds.NodeClass] = AttributeValue(ua.DataValue(ua.Variant(item.NodeClass, ua.VariantType.Int32)))
            #add requested attrs
            self._add_nodeattributes(item.NodeAttributes, nodedata)
            
            #add parent
            if item.ParentNodeId == ua.NodeId():
                #self.logger.warning("add_node: creating node %s without parent", item.RequestedNewNodeId) 
                pass
            elif not item.ParentNodeId in self._nodes:
                #self.logger.warning("add_node: while adding node %s, requested parent node %s does not exists", item.RequestedNewNodeId, item.ParentNodeId) 
                result.StatusCode = ua.StatusCode(ua.StatusCodes.BadParentNodeIdInvalid)
                return result
            else:
                desc = ua.ReferenceDescription()
                desc.ReferenceTypeId = item.ReferenceTypeId
                desc.NodeId = item.RequestedNewNodeId
                desc.NodeClass = item.NodeClass
                desc.BrowseName = item.BrowseName
                desc.DisplayName = ua.LocalizedText(item.BrowseName.Name)
                desc.TypeDefinition = item.TypeDefinition
                desc.IsForward = True
                self._nodes[item.ParentNodeId].references.append(desc)
           
            #now add our node to db
            self._nodes[item.RequestedNewNodeId] = nodedata

            #add type definition
            if item.TypeDefinition != ua.NodeId():
                addref = ua.AddReferencesItem()
                addref.SourceNodeId = item.RequestedNewNodeId
                addref.IsForward = True
                addref.ReferenceTypeId = ua.NodeId(ua.ObjectIds.HasTypeDefinition)
                addref.TargetNodeId = item.TypeDefinition
                addref.TargetNodeClass = ua.NodeClass.DataType
                self._add_reference(addref)

            result.StatusCode = ua.StatusCode()
            result.AddedNodeId = item.RequestedNewNodeId


            return result

    def add_references(self, refs):
        result = []
        for ref in refs:
            result.append(self._add_reference(ref))
        return result

    def _add_reference(self, addref):
        with self._lock:
            if not addref.SourceNodeId in self._nodes:
                return ua.StatusCode(ua.StatusCodes.BadSourceNodeIdInvalid)
            if not addref.TargetNodeId in self._nodes:
                return ua.StatusCode(ua.StatusCodes.BadTargetNodeIdInvalid)
            rdesc = ua.ReferenceDescription()
            rdesc.ReferenceTypeId = addref.ReferenceTypeId
            rdesc.IsForward = addref.IsForward
            rdesc.NodeId = addref.TargetNodeId
            rdesc.NodeClass = addref.TargetNodeClass
            bname = self.get_attribute_value(addref.TargetNodeId, ua.AttributeIds.BrowseName).Value.Value
            if bname:
                rdesc.BrowseName = bname 
            dname = self.get_attribute_value(addref.TargetNodeId, ua.AttributeIds.DisplayName).Value.Value
            if dname:
                rdesc.DisplayName = dname 
            self._nodes[addref.SourceNodeId].references.append(rdesc)
            return ua.StatusCode()

    def get_attribute_value(self, nodeid, attr):
        with self._lock:
            #self.logger.debug("get attr val: %s %s", nodeid, attr)
            dv = ua.DataValue()
            if not nodeid in self._nodes:
                dv.StatusCode = ua.StatusCode(ua.StatusCodes.BadNodeIdUnknown)
                return dv
            node = self._nodes[nodeid]
            if attr not in node.attributes:
                dv.StatusCode = ua.StatusCode(ua.StatusCodes.BadAttributeIdInvalid)
                return dv
            attval = node.attributes[attr]
            if attval.value_callback:
                return attval.value_callback()
            return attval.value

    def set_attribute_value(self, nodeid, attr, value):
        with self._lock:
            self.logger.debug("set attr val: %s %s %s", nodeid, attr, value)
            if not nodeid in self._nodes:
                return ua.StatusCode(ua.StatusCodes.BadNodeIdUnknown)
            node = self._nodes[nodeid]
            if not attr in node.attributes:
                return ua.StatusCode(ua.StatusCodes.BadAttributeIdInvalid)
            attval = node.attributes[attr]
            attval.value = value
            if attval.value_callback:
                return attval.value_callback(nodeid, attr, value)
            for k, v in attval.datachange_callbacks.items():
                try:
                    v(k, value)
                except Exception as ex:
                    self.logger.warn("Error calling datachange callback %s, %s, %s", k, v, ex)
                    print(ex)#seems exception is truncated!?!?
            return ua.StatusCode()

    def add_datachange_callback(self, nodeid, attr, callback):
        with self._lock:
            self.logger.debug("set attr callback: %s %s %s", nodeid, attr, callback)
            if not nodeid in self._nodes:
                return ua.StatusCode(ua.StatusCodes.BadNodeIdUnknown), 0
            node = self._nodes[nodeid]
            if not attr in node.attributes:
                return ua.StatusCode(ua.StatusCodes.BadAttributeIdInvalid), 0
            attval = node.attributes[attr]
            self._datachange_callback_counter += 1
            handle = self._datachange_callback_counter
            #cb = DataChangeCallbackData()
            #cb.callback = callback
            #cb.client_handle = handle
            attval.datachange_callbacks[handle] = callback
            self._handle_to_attribute_map[handle] = (nodeid, attr)
            return ua.StatusCode(), handle

    def delete_datachange_callback(self, handle):
        nodeid, attr = self._handle_to_attribute_map.pop(handle)
        self._nodes[nodeid].attributes[attr].datachange_callbacks.pop(handle)
        


    def _add_nodeattributes(self, item, nodedata):
        item = ua.downcast_extobject(item)
        if item.SpecifiedAttributes & ua.NodeAttributesMask.AccessLevel:
            nodedata.attributes[ua.AttributeIds.AccessLevel] = AttributeValue(ua.DataValue(ua.Variant(item.AccessLevel, ua.VariantType.Byte)))
        if item.SpecifiedAttributes & ua.NodeAttributesMask.ArrayDimensions:
            nodedata.attributes[ua.AttributeIds.ArrayDimensions] = AttributeValue(ua.DataValue(ua.Variant(item.ArrayDimensions, ua.VariantType.Int32)))
        if item.SpecifiedAttributes & ua.NodeAttributesMask.BrowseName:
            nodedata.attributes[ua.AttributeIds.BrowseName] = AttributeValue(ua.DataValue(ua.Variant(item.BrowseName, ua.VariantType.QualifiedName)))
        if item.SpecifiedAttributes & ua.NodeAttributesMask.ContainsNoLoops:
            nodedata.attributes[ua.AttributeIds.ContainsNoLoops] = AttributeValue(ua.DataValue(ua.Variant(item.ContainsNoLoops, ua.VariantType.Boolean)))
        if item.SpecifiedAttributes & ua.NodeAttributesMask.DataType:
            nodedata.attributes[ua.AttributeIds.DataType] = AttributeValue(ua.DataValue(ua.Variant(item.DataType, ua.VariantType.NodeId)))
        if item.SpecifiedAttributes & ua.NodeAttributesMask.Description:
            nodedata.attributes[ua.AttributeIds.Description] = AttributeValue(ua.DataValue(ua.Variant(item.Description, ua.VariantType.LocalizedText)))
        if item.SpecifiedAttributes & ua.NodeAttributesMask.DisplayName:
            nodedata.attributes[ua.AttributeIds.DisplayName] = AttributeValue(ua.DataValue(ua.Variant(item.DisplayName, ua.VariantType.LocalizedText)))
        if item.SpecifiedAttributes & ua.NodeAttributesMask.EventNotifier:
            nodedata.attributes[ua.AttributeIds.EventNotifier] = AttributeValue(ua.DataValue(ua.Variant(item.EventNotifier, ua.VariantType.Byte)))
        if item.SpecifiedAttributes & ua.NodeAttributesMask.Executable:
            nodedata.attributes[ua.AttributeIds.Executable] = AttributeValue(ua.DataValue(ua.Variant(item.Executable, ua.VariantType.Boolean)))
        if item.SpecifiedAttributes & ua.NodeAttributesMask.Historizing:
            nodedata.attributes[ua.AttributeIds.Historizing] = AttributeValue(ua.DataValue(ua.Variant(item.Historizing, ua.VariantType.Boolean)))
        if item.SpecifiedAttributes & ua.NodeAttributesMask.InverseName:
            nodedata.attributes[ua.AttributeIds.InverseName] = AttributeValue(ua.DataValue(ua.Variant(item.InverseName, ua.VariantType.LocalizedText)))
        if item.SpecifiedAttributes & ua.NodeAttributesMask.IsAbstract:
            nodedata.attributes[ua.AttributeIds.IsAbstract] = AttributeValue(ua.DataValue(ua.Variant(item.IsAbstract, ua.VariantType.Boolean)))
        if item.SpecifiedAttributes & ua.NodeAttributesMask.MinimumSamplingInterval:
            nodedata.attributes[ua.AttributeIds.MinimumSamplingInterval] = AttributeValue(ua.DataValue(ua.Variant(item.MinimumSamplingInterval, ua.VariantType.Double)))
        if item.SpecifiedAttributes & ua.NodeAttributesMask.NodeClass:
            nodedata.attributes[ua.AttributeIds.NodeClass] = AttributeValue(ua.DataValue(ua.Variant(item.NodeClass, ua.VariantType.UInt32)))
        if item.SpecifiedAttributes & ua.NodeAttributesMask.NodeId:
            nodedata.attributes[ua.AttributeIds.NodeId] = AttributeValue(ua.DataValue(ua.Variant(item.NodeId, ua.VariantType.NodeId)))
        if item.SpecifiedAttributes & ua.NodeAttributesMask.Symmetric:
            nodedata.attributes[ua.AttributeIds.Symmetric] = AttributeValue(ua.DataValue(ua.Variant(item.Symmetric, ua.VariantType.Boolean)))
        if item.SpecifiedAttributes & ua.NodeAttributesMask.UserAccessLevel:
            nodedata.attributes[ua.AttributeIds.UserAccessLevel] = AttributeValue(ua.DataValue(ua.Variant(item.UserAccessLevel, ua.VariantType.Byte)))
        if item.SpecifiedAttributes & ua.NodeAttributesMask.UserExecutable:
            nodedata.attributes[ua.AttributeIds.UserExecutable] = AttributeValue(ua.DataValue(ua.Variant(item.UserExecutable, ua.VariantType.Boolean)))
        if item.SpecifiedAttributes & ua.NodeAttributesMask.UserWriteMask:
            nodedata.attributes[ua.AttributeIds.UserWriteMask] = AttributeValue(ua.DataValue(ua.Variant(item.UserWriteMask, ua.VariantType.Byte)))
        if item.SpecifiedAttributes & ua.NodeAttributesMask.ValueRank:
            nodedata.attributes[ua.AttributeIds.ValueRank] = AttributeValue(ua.DataValue(ua.Variant(item.ValueRank, ua.VariantType.Int32)))
        if item.SpecifiedAttributes & ua.NodeAttributesMask.WriteMask:
            nodedata.attributes[ua.AttributeIds.WriteMask] = AttributeValue(ua.DataValue(ua.Variant(item.WriteMask, ua.VariantType.Byte)))
        if item.SpecifiedAttributes & ua.NodeAttributesMask.Value:
            nodedata.attributes[ua.AttributeIds.Value] = AttributeValue(ua.DataValue(item.Value))

    def read(self, params):
        self.logger.debug("read %s", params)
        res = []
        for readvalue in params.NodesToRead:
            res.append(self.get_attribute_value(readvalue.NodeId, readvalue.AttributeId))
        return res

    def write(self, params):
        self.logger.debug("write %s", params)
        res = []
        for writevalue in params.NodesToWrite:
            res.append(self.set_attribute_value(writevalue.NodeId, writevalue.AttributeId, writevalue.Value))
        return res

    def browse(self, params):
        self.logger.debug("browse %s", params)
        res = []
        for desc in params.NodesToBrowse:
            res.append(self._browse(desc))
        return res

    def _browse(self, desc):
        with self._lock:
            res = ua.BrowseResult()
            if desc.NodeId not in self._nodes:
                res.StatusCode = ua.StatusCode(ua.StatusCodes.BadNodeIdInvalid)
                return res
            node = self._nodes[desc.NodeId]
            for ref in node.references:
                if not self._is_suitable_ref(desc, ref):
                    continue
                res.References.append(ref)
            return res

    def _is_suitable_ref(self, desc, ref):
        if not self._suitable_direction(desc.BrowseDirection, ref.IsForward):
            self.logger.debug("%s is not suitable due to direction", ref)
            return False
        if not self._suitable_reftype(desc.ReferenceTypeId, ref.ReferenceTypeId, desc.IncludeSubtypes):
            self.logger.debug("%s is not suitable due to type", ref)
            return False
        if desc.NodeClassMask and ((desc.NodeClassMask & ref.NodeClass) == 0):
            self.logger.debug("%s is not suitable due to class", ref)
            return False
        self.logger.debug("%s is a suitable ref for desc %s", ref, desc)
        return True

    def _suitable_reftype(self, ref1, ref2, subtypes):
        """
        """
        if not subtypes:
            return ref1.Identifier == ref2.Identifier
        oktype = self._get_sub_ref(ref1)
        return ref2 in oktype

    def _get_sub_ref(self, ref):
        res = []
        nodedata = self._nodes[ref]
        for ref in nodedata.references:
            if ref.ReferenceTypeId.Identifier == ua.ObjectIds.HasSubtype:
                res.append(ref.NodeId)
                res += self._get_sub_ref(ref.NodeId)
        return res

    def _suitable_direction(self, desc, isforward):
        if desc == ua.BrowseDirection.Both:
            return True
        if desc == ua.BrowseDirection.Forward and isforward:
            return True
        return False

    def translate_browsepaths_to_nodeids(self, browsepaths):
        self.logger.debug("translate browsepath: %s", browsepaths)
        results = []
        for path in browsepaths:
            results.append(self._translate_browsepath_to_nodeid(path))
        return results

    def _translate_browsepath_to_nodeid(self, path):
        self.logger.debug("looking at path: %s", path)
        res = ua.BrowsePathResult()
        with self._lock:
            if not path.StartingNode in self._nodes:
                res.StatusCode = ua.StatusCode(ua.StatusCodes.BadNodeIdInvalid)
                return res
        current = path.StartingNode
        for el in path.RelativePath.Elements:
            nodeid = self._find_element_in_node(el, current)
            if not nodeid:
                res.StatusCode = ua.StatusCode(ua.StatusCodes.BadNoMatch)
                return res
            current = nodeid
        target = ua.BrowsePathTarget()
        target.TargetId = current
        target.RemainingPathIndex = 4294967295 
        res.Targets = [target]
        return res

    def _find_element_in_node(self, el, nodeid):
        with self._lock:
            nodedata = self._nodes[nodeid]
            for ref in nodedata.references:
                #FIXME: here we should check other arguments!!
                if ref.BrowseName == el.TargetName:
                    return ref.NodeId
            self.logger.warning("element %s was not found in node %s", el, nodeid)
            return None
            







            
            

