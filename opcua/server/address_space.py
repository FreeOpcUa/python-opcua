from threading import RLock
import logging
from datetime import datetime
import collections
import shelve
try:
    import cPickle as pickle
except:
    import pickle

from opcua import ua
from opcua.server.users import User


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
        self.call = None

    def __str__(self):
        return "NodeData(id:{}, attrs:{}, refs:{})".format(self.nodeid, self.attributes, self.references)
    __repr__ = __str__


class AttributeService(object):

    def __init__(self, aspace):
        self.logger = logging.getLogger(__name__)
        self._aspace = aspace

    def read(self, params):
        self.logger.debug("read %s", params)
        res = []
        for readvalue in params.NodesToRead:
            res.append(self._aspace.get_attribute_value(readvalue.NodeId, readvalue.AttributeId))
        return res

    def write(self, params, user=User.Admin):
        self.logger.debug("write %s as user %s", params, user)
        res = []
        for writevalue in params.NodesToWrite:
            if user != User.Admin:
                if writevalue.AttributeId != ua.AttributeIds.Value:
                    res.append(ua.StatusCode(ua.StatusCodes.BadUserAccessDenied))
                    continue
                al = self._aspace.get_attribute_value(writevalue.NodeId, ua.AttributeIds.AccessLevel)
                ual = self._aspace.get_attribute_value(writevalue.NodeId, ua.AttributeIds.UserAccessLevel)
                if not ua.test_bit(al.Value.Value, ua.AccessLevel.CurrentWrite) or not ua.test_bit(ual.Value.Value, ua.AccessLevel.CurrentWrite):
                    res.append(ua.StatusCode(ua.StatusCodes.BadUserAccessDenied))
                    continue
            res.append(self._aspace.set_attribute_value(writevalue.NodeId, writevalue.AttributeId, writevalue.Value))
        return res


class ViewService(object):

    def __init__(self, aspace):
        self.logger = logging.getLogger(__name__)
        self._aspace = aspace

    def browse(self, params):
        self.logger.debug("browse %s", params)
        res = []
        for desc in params.NodesToBrowse:
            res.append(self._browse(desc))
        return res

    def _browse(self, desc):
        res = ua.BrowseResult()
        if desc.NodeId not in self._aspace:
            res.StatusCode = ua.StatusCode(ua.StatusCodes.BadNodeIdInvalid)
            return res
        node = self._aspace[desc.NodeId]
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
        if not subtypes and ref2.Identifier == ua.ObjectIds.HasSubtype:
            return False
        if ref1.Identifier == ref2.Identifier:
            return True
        oktypes = self._get_sub_ref(ref1)
        if not subtypes and ua.NodeId(ua.ObjectIds.HasSubtype) in oktypes:
            oktypes.remove(ua.NodeId(ua.ObjectIds.HasSubtype))
        return ref2 in oktypes

    def _get_sub_ref(self, ref):
        res = []
        nodedata = self._aspace[ref]
        for ref in nodedata.references:
            if ref.ReferenceTypeId.Identifier == ua.ObjectIds.HasSubtype and ref.IsForward:
                res.append(ref.NodeId)
                res += self._get_sub_ref(ref.NodeId)
        return res

    def _suitable_direction(self, desc, isforward):
        if desc == ua.BrowseDirection.Both:
            return True
        if desc == ua.BrowseDirection.Forward and isforward:
            return True
        if desc == ua.BrowseDirection.Inverse and not isforward:
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
        if path.StartingNode not in self._aspace:
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
        nodedata = self._aspace[nodeid]
        for ref in nodedata.references:
            # FIXME: here we should check other arguments!!
            if ref.BrowseName == el.TargetName:
                return ref.NodeId
        self.logger.info("element %s was not found in node %s", el, nodeid)
        return None


class NodeManagementService(object):

    def __init__(self, aspace):
        self.logger = logging.getLogger(__name__)
        self._aspace = aspace

    def add_nodes(self, addnodeitems, user=User.Admin):
        results = []
        for item in addnodeitems:
            results.append(self._add_node(item, user))
        return results

    def _add_node(self, item, user):
        result = ua.AddNodesResult()

        # If Identifier of requested NodeId is null we generate a new NodeId using
        # the namespace of the nodeid, this is an extention of the spec to allow
        # to requests the server to generate a new nodeid in a specified namespace
        if item.RequestedNewNodeId.has_null_identifier():
            self.logger.debug("RequestedNewNodeId has null identifier, generating Identifier")
            nodedata = NodeData(self._aspace.generate_nodeid(item.RequestedNewNodeId.NamespaceIndex))
        else:
            nodedata = NodeData(item.RequestedNewNodeId)

        if nodedata.nodeid in self._aspace:
            self.logger.warning("AddNodesItem: node already exists")
            result.StatusCode = ua.StatusCode(ua.StatusCodes.BadNodeIdExists)
            return result

        if item.ParentNodeId.is_null():
            # self.logger.warning("add_node: creating node %s without parent", nodedata.nodeid)
            # should return Error here, but the standard namespace define many nodes without parents...
            pass
        elif item.ParentNodeId not in self._aspace:
            self.logger.warning("add_node: while adding node %s, requested parent node %s does not exists", nodedata.nodeid, item.ParentNodeId)
            result.StatusCode = ua.StatusCode(ua.StatusCodes.BadParentNodeIdInvalid)
            return result

        if not user == User.Admin:
            result.StatusCode = ua.StatusCode(ua.StatusCodes.BadUserAccessDenied)
            return result

        self._add_node_attributes(nodedata, item)

        # now add our node to db
        self._aspace[nodedata.nodeid] = nodedata

        if not item.ParentNodeId.is_null():
            self._add_ref_from_parent(nodedata, item)
            self._add_ref_to_parent(nodedata, item, user)

        # add type definition
        if item.TypeDefinition != ua.NodeId():
            self._add_type_definition(nodedata, item, user)

        result.StatusCode = ua.StatusCode()
        result.AddedNodeId = nodedata.nodeid

        return result

    def _add_node_attributes(self, nodedata, item):
        # add common attrs
        nodedata.attributes[ua.AttributeIds.NodeId] = AttributeValue(
            ua.DataValue(ua.Variant(nodedata.nodeid, ua.VariantType.NodeId))
        )
        nodedata.attributes[ua.AttributeIds.BrowseName] = AttributeValue(
            ua.DataValue(ua.Variant(item.BrowseName, ua.VariantType.QualifiedName))
        )
        nodedata.attributes[ua.AttributeIds.NodeClass] = AttributeValue(
            ua.DataValue(ua.Variant(item.NodeClass, ua.VariantType.Int32))
        )
        # add requested attrs
        self._add_nodeattributes(item.NodeAttributes, nodedata)

    def _add_ref_from_parent(self, nodedata, item):
        desc = ua.ReferenceDescription()
        desc.ReferenceTypeId = item.ReferenceTypeId
        desc.NodeId = nodedata.nodeid
        desc.NodeClass = item.NodeClass
        desc.BrowseName = item.BrowseName
        desc.DisplayName = ua.LocalizedText(item.BrowseName.Name)
        desc.TypeDefinition = item.TypeDefinition
        desc.IsForward = True
        self._aspace[item.ParentNodeId].references.append(desc)

    def _add_ref_to_parent(self, nodedata, item, user):
        addref = ua.AddReferencesItem()
        addref.ReferenceTypeId = item.ReferenceTypeId
        addref.SourceNodeId = nodedata.nodeid
        addref.TargetNodeId = item.ParentNodeId
        addref.TargetNodeClass = self._aspace[item.ParentNodeId].attributes[ua.AttributeIds.NodeClass].value.Value.Value
        addref.IsForward = False
        self._add_reference(addref, user)

    def _add_type_definition(self, nodedata, item, user):
        addref = ua.AddReferencesItem()
        addref.SourceNodeId = nodedata.nodeid
        addref.IsForward = True
        addref.ReferenceTypeId = ua.NodeId(ua.ObjectIds.HasTypeDefinition)
        addref.TargetNodeId = item.TypeDefinition
        addref.TargetNodeClass = ua.NodeClass.DataType
        self._add_reference(addref, user)

    def delete_nodes(self, deletenodeitems, user=User.Admin):
        results = []
        for item in deletenodeitems.NodesToDelete:
            results.append(self._delete_node(item, user))
        return results

    def _delete_node(self, item, user):
        if user != User.Admin:
            return ua.StatusCode(ua.StatusCodes.BadUserAccessDenied)

        if item.NodeId not in self._aspace:
            self.logger.warning("DeleteNodesItem: node does not exists")
            return ua.StatusCode(ua.StatusCodes.BadNodeIdUnknown)

        if item.DeleteTargetReferences:
            for elem in self._aspace.keys():
                for rdesc in self._aspace[elem].references:
                    if rdesc.NodeId == item.NodeId:
                        self._aspace[elem].references.remove(rdesc)

        self._delete_node_callbacks(self._aspace[item.NodeId])

        del(self._aspace[item.NodeId])

        return ua.StatusCode()

    def _delete_node_callbacks(self, nodedata):
        if ua.AttributeIds.Value in nodedata.attributes:
            for handle, callback in nodedata.attributes[ua.AttributeIds.Value].datachange_callbacks.items():
                try:
                    callback(handle, None, ua.StatusCode(ua.StatusCodes.BadNodeIdUnknown))
                    self._aspace.delete_datachange_callback(handle)
                except Exception as ex:
                    self.logger.exception("Error calling delete node callback callback %s, %s, %s", nodedata, ua.AttributeIds.Value, ex)

    def add_references(self, refs, user=User.Admin):
        result = []
        for ref in refs:
            result.append(self._add_reference(ref, user))
        return result

    def _add_reference(self, addref, user):
        if addref.SourceNodeId not in self._aspace:
            return ua.StatusCode(ua.StatusCodes.BadSourceNodeIdInvalid)
        if addref.TargetNodeId not in self._aspace:
            return ua.StatusCode(ua.StatusCodes.BadTargetNodeIdInvalid)
        if user != User.Admin:
            return ua.StatusCode(ua.StatusCodes.BadUserAccessDenied)
        rdesc = ua.ReferenceDescription()
        rdesc.ReferenceTypeId = addref.ReferenceTypeId
        rdesc.IsForward = addref.IsForward
        rdesc.NodeId = addref.TargetNodeId
        rdesc.NodeClass = addref.TargetNodeClass
        bname = self._aspace.get_attribute_value(addref.TargetNodeId, ua.AttributeIds.BrowseName).Value.Value
        if bname:
            rdesc.BrowseName = bname
        dname = self._aspace.get_attribute_value(addref.TargetNodeId, ua.AttributeIds.DisplayName).Value.Value
        if dname:
            rdesc.DisplayName = dname
        self._aspace[addref.SourceNodeId].references.append(rdesc)
        return ua.StatusCode()

    def delete_references(self, refs, user=User.Admin):
        result = []
        for ref in refs:
            result.append(self._delete_reference(ref, user))
        return result

    def _delete_reference(self, item, user):
        if item.SourceNodeId not in self._aspace:
            return ua.StatusCode(ua.StatusCodes.BadSourceNodeIdInvalid)
        if item.TargetNodeId not in self._aspace:
            return ua.StatusCode(ua.StatusCodes.BadTargetNodeIdInvalid)
        if user != User.Admin:
            return ua.StatusCode(ua.StatusCodes.BadUserAccessDenied)

        for rdesc in self._aspace[item.SourceNodeId].references:
            if rdesc.NodeId is item.TargetNodeId:
                if rdesc.RefrenceTypeId != item.RefrenceTypeId:
                    return ua.StatusCode(ua.StatusCodes.BadReferenceTypeIdInvalid)
                if rdesc.IsForward == item.IsForward or item.DeleteBidirectional:
                    self._aspace[item.SourceNodeId].references.remove(rdesc)

        for rdesc in self._aspace[item.TargetNodeId].references:
            if rdesc.NodeId is item.SourceNodeId:
                if rdesc.RefrenceTypeId != item.RefrenceTypeId:
                    return ua.StatusCode(ua.StatusCodes.BadReferenceTypeIdInvalid)
                if rdesc.IsForward == item.IsForward or item.DeleteBidirectional:
                    self._aspace[item.SourceNodeId].references.remove(rdesc)

        return ua.StatusCode()

    def _add_node_attr(self, item, nodedata, name, vtype=None):
        if item.SpecifiedAttributes & getattr(ua.NodeAttributesMask, name):
            dv = ua.DataValue(ua.Variant(getattr(item, name), vtype))
            dv.ServerTimestamp = datetime.utcnow()
            dv.SourceTimestamp = datetime.utcnow()
            nodedata.attributes[getattr(ua.AttributeIds, name)] = AttributeValue(dv)

    def _add_nodeattributes(self, item, nodedata):
        self._add_node_attr(item, nodedata, "AccessLevel", ua.VariantType.Byte)
        self._add_node_attr(item, nodedata, "ArrayDimensions", ua.VariantType.UInt32)
        self._add_node_attr(item, nodedata, "BrowseName", ua.VariantType.QualifiedName)
        self._add_node_attr(item, nodedata, "ContainsNoLoops", ua.VariantType.Boolean)
        self._add_node_attr(item, nodedata, "DataType", ua.VariantType.NodeId)
        self._add_node_attr(item, nodedata, "Description", ua.VariantType.LocalizedText)
        self._add_node_attr(item, nodedata, "DisplayName", ua.VariantType.LocalizedText)
        self._add_node_attr(item, nodedata, "EventNotifier", ua.VariantType.Byte)
        self._add_node_attr(item, nodedata, "Executable", ua.VariantType.Boolean)
        self._add_node_attr(item, nodedata, "Historizing", ua.VariantType.Boolean)
        self._add_node_attr(item, nodedata, "InverseName", ua.VariantType.LocalizedText)
        self._add_node_attr(item, nodedata, "IsAbstract", ua.VariantType.Boolean)
        self._add_node_attr(item, nodedata, "MinimumSamplingInterval", ua.VariantType.Double)
        self._add_node_attr(item, nodedata, "NodeClass", ua.VariantType.UInt32)
        self._add_node_attr(item, nodedata, "NodeId", ua.VariantType.NodeId)
        self._add_node_attr(item, nodedata, "Symmetric", ua.VariantType.Boolean)
        self._add_node_attr(item, nodedata, "UserAccessLevel", ua.VariantType.Byte)
        self._add_node_attr(item, nodedata, "UserExecutable", ua.VariantType.Boolean)
        self._add_node_attr(item, nodedata, "UserWriteMask", ua.VariantType.Byte)
        self._add_node_attr(item, nodedata, "ValueRank", ua.VariantType.Int32)
        self._add_node_attr(item, nodedata, "WriteMask", ua.VariantType.UInt32)
        self._add_node_attr(item, nodedata, "UserWriteMask", ua.VariantType.UInt32)
        self._add_node_attr(item, nodedata, "Value")


class MethodService(object):

    def __init__(self, aspace):
        self.logger = logging.getLogger(__name__)
        self._aspace = aspace

    def call(self, methods):
        results = []
        for method in methods:
            results.append(self._call(method))
        return results

    def _call(self, method):
        res = ua.CallMethodResult()
        if method.ObjectId not in self._aspace or method.MethodId not in self._aspace:
            res.StatusCode = ua.StatusCode(ua.StatusCodes.BadNodeIdInvalid)
        else:
            node = self._aspace[method.MethodId]
            if node.call is None:
                res.StatusCode = ua.StatusCode(ua.StatusCodes.BadNothingToDo)
            else:
                try:
                    res.OutputArguments = node.call(method.ObjectId, *method.InputArguments)
                    for _ in method.InputArguments:
                        res.InputArgumentResults.append(ua.StatusCode())
                except Exception:
                    self.logger.exception("Error executing method call %s, an exception was raised: ", method)
                    res.StatusCode = ua.StatusCode(ua.StatusCodes.BadUnexpectedError)
        return res


class AddressSpace(object):

    """
    The address space object stores all the nodes og the OPC-UA server
    and helper methods.
    The methods are threadsafe
    """

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self._nodes = {}
        self._lock = RLock()  # FIXME: should use multiple reader, one writter pattern
        self._datachange_callback_counter = 200
        self._handle_to_attribute_map = {}
        self._default_idx = 2
        self._nodeid_counter = {0: 20000, 1: 2000}

    def __getitem__(self, nodeid):
        with self._lock:
            return self._nodes.__getitem__(nodeid)

    def __setitem__(self, nodeid, value):
        with self._lock:
            return self._nodes.__setitem__(nodeid, value)

    def __contains__(self, nodeid):
        with self._lock:
            return self._nodes.__contains__(nodeid)

    def __delitem__(self, nodeid):
        with self._lock:
            self._nodes.__delitem__(nodeid)

    def generate_nodeid(self, idx=None):
        if idx is None:
            idx = self._default_idx
        if idx in self._nodeid_counter:
            self._nodeid_counter[idx] += 1
        else:
            self._nodeid_counter[idx] = 1
        nodeid = ua.NodeId(self._nodeid_counter[idx], idx)
        with self._lock:  # OK since reentrant lock
            while True:
                if nodeid in self._nodes:
                    nodeid = self.generate_nodeid(idx)
                else:
                    return nodeid

    def keys(self):
        with self._lock:
            return self._nodes.keys()

    def empty(self):
        """
        Delete all nodes in address space
        """
        with self._lock:
            self._nodes = {}

    def dump(self, path):
        """
        dump address space as binary to file
        """
        s = shelve.open(path, "n", protocol = pickle.HIGHEST_PROTOCOL)
        for nodeid in self._nodes.keys():
            s[nodeid.to_string()] = self._nodes[nodeid]
        s.close()

    def load(self, path):
        """
        load address space from file, overwritting everything current address space
        """
        class LazyLoadingDict(collections.MutableMapping):
            def __init__(self, source):
                self.source = source
                self.cache = {}

            def __getitem__(self, key):
                try:
                    return self.cache[key]
                except KeyError:
                    node = self.cache[key] = self.source[key.to_string()]
                    return node

            def __setitem__(self, key, value):
                self.cache[key] = value

            def __contains__(self, key):
                return key in self.cache or key.to_string() in self.source

            def __delitem__(self, key):
                raise NotImplementedError

            def __iter__(self):
                raise NotImplementedError

            def __len__(self):
                raise NotImplementedError

        self._nodes = LazyLoadingDict(shelve.open(path, "r"))

    def get_attribute_value(self, nodeid, attr):
        with self._lock:
            self.logger.debug("get attr val: %s %s", nodeid, attr)
            if nodeid not in self._nodes:
                dv = ua.DataValue()
                dv.StatusCode = ua.StatusCode(ua.StatusCodes.BadNodeIdUnknown)
                return dv
            node = self._nodes[nodeid]
            if attr not in node.attributes:
                dv = ua.DataValue()
                dv.StatusCode = ua.StatusCode(ua.StatusCodes.BadAttributeIdInvalid)
                return dv
            attval = node.attributes[attr]
            if attval.value_callback:
                return attval.value_callback()
            return attval.value

    def set_attribute_value(self, nodeid, attr, value):
        with self._lock:
            self.logger.debug("set attr val: %s %s %s", nodeid, attr, value)
            if nodeid not in self._nodes:
                return ua.StatusCode(ua.StatusCodes.BadNodeIdUnknown)
            node = self._nodes[nodeid]
            if attr not in node.attributes:
                return ua.StatusCode(ua.StatusCodes.BadAttributeIdInvalid)
            if not value.SourceTimestamp:
                value.SourceTimestamp = datetime.utcnow()
            if not value.ServerTimestamp:
                value.ServerTimestamp = datetime.utcnow()

            attval = node.attributes[attr]
            old = attval.value
            attval.value = value
            cbs = []
            if old.Value != value.Value:  # only send call callback when a value change has happend
                cbs = list(attval.datachange_callbacks.items())

        for k, v in cbs:
            try:
                v(k, value)
            except Exception as ex:
                self.logger.exception("Error calling datachange callback %s, %s, %s", k, v, ex)

        return ua.StatusCode()

    def add_datachange_callback(self, nodeid, attr, callback):
        with self._lock:
            self.logger.debug("set attr callback: %s %s %s", nodeid, attr, callback)
            if nodeid not in self._nodes:
                return ua.StatusCode(ua.StatusCodes.BadNodeIdUnknown), 0
            node = self._nodes[nodeid]
            if attr not in node.attributes:
                return ua.StatusCode(ua.StatusCodes.BadAttributeIdInvalid), 0
            attval = node.attributes[attr]
            self._datachange_callback_counter += 1
            handle = self._datachange_callback_counter
            attval.datachange_callbacks[handle] = callback
            self._handle_to_attribute_map[handle] = (nodeid, attr)
            return ua.StatusCode(), handle

    def delete_datachange_callback(self, handle):
        with self._lock:
            nodeid, attr = self._handle_to_attribute_map.pop(handle)
            self._nodes[nodeid].attributes[attr].datachange_callbacks.pop(handle)

    def add_method_callback(self, methodid, callback):
        with self._lock:
            node = self._nodes[methodid]
            node.call = callback
