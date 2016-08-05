"""
High level node object, to access node attribute
and browse address space
"""

from opcua import ua
from opcua.common import events
import opcua.common 

class Node(object):

    """
    High level node object, to access node attribute,
    browse and populate address space.
    Node objects are usefull as-is but they do not expose the entire
    OPC-UA protocol. Feel free to look at the code of this class and call
    directly UA services methods to optimize your code
    """

    def __init__(self, server, nodeid):
        self.server = server
        self.nodeid = None
        if isinstance(nodeid, Node):
            self.nodeid = nodeid.nodeid
        elif isinstance(nodeid, ua.NodeId):
            self.nodeid = nodeid
        elif type(nodeid) in (str, bytes):
            self.nodeid = ua.NodeId.from_string(nodeid)
        elif isinstance(nodeid, int):
            self.nodeid = ua.NodeId(nodeid, 0)
        else:
            raise ua.UaError("argument to node must be a NodeId object or a string defining a nodeid found {} of type {}".format(nodeid, type(nodeid)))

    def __eq__(self, other):
        if isinstance(other, Node) and self.nodeid == other.nodeid:
            return True
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return "Node({})".format(self.nodeid)
    __repr__ = __str__

    def __hash__(self):
        return self.nodeid.__hash__()

    def get_browse_name(self):
        """
        Get browse name of a node. A browse name is a QualifiedName object
        composed of a string(name) and a namespace index.
        """
        result = self.get_attribute(ua.AttributeIds.BrowseName)
        return result.Value.Value

    def get_display_name(self):
        """
        get description attribute of node
        """
        result = self.get_attribute(ua.AttributeIds.DisplayName)
        return result.Value.Value

    def get_data_type(self):
        """
        get data type of node as NodeId
        """
        result = self.get_attribute(ua.AttributeIds.DataType)
        return result.Value.Value

    def get_data_type_as_variant_type(self):
        """
        get data type of node as VariantType
        This only works if node is a variable, otherwise type
        may not be convertible to VariantType
        """
        result = self.get_attribute(ua.AttributeIds.DataType)
        return ua.DataType_to_VariantType(result.Value.Value)

    def get_access_level(self):
        """
        Get the access level attribute of the node as a set of AccessLevel enum values.
        """
        result = self.get_attribute(ua.AttributeIds.AccessLevel)
        return ua.AccessLevel.parse_bitfield(result.Value.Value)

    def get_user_access_level(self):
        """
        Get the user access level attribute of the node as a set of AccessLevel enum values.
        """
        result = self.get_attribute(ua.AttributeIds.UserAccessLevel)
        return ua.AccessLevel.parse_bitfield(result.Value.Value)

    def get_event_notifier(self):
        """
        Get the event notifier attribute of the node as a set of EventNotifier enum values.
        """
        result = self.get_attribute(ua.AttributeIds.EventNotifier)
        return ua.EventNotifier.parse_bitfield(result.Value.Value)

    def set_event_notifier(self, values):
        """
        Set the event notifier attribute.

        :param values: an iterable of EventNotifier enum values.
        """
        event_notifier_bitfield = ua.EventNotifier.to_bitfield(values)
        self.set_attribute(ua.AttributeIds.EventNotifier, ua.DataValue(ua.Variant(event_notifier_bitfield, ua.VariantType.Byte)))

    def get_node_class(self):
        """
        get node class attribute of node
        """
        result = self.get_attribute(ua.AttributeIds.NodeClass)
        return result.Value.Value

    def get_description(self):
        """
        get description attribute class of node
        """
        result = self.get_attribute(ua.AttributeIds.Description)
        return result.Value.Value

    def get_value(self):
        """
        Get value of a node as a python type. Only variables ( and properties) have values.
        An exception will be generated for other node types.
        """
        result = self.get_data_value()
        return result.Value.Value

    def get_data_value(self):
        """
        Get value of a node as a DataValue object. Only variables (and properties) have values.
        An exception will be generated for other node types.
        DataValue contain a variable value as a variant as well as server and source timestamps
        """
        return self.get_attribute(ua.AttributeIds.Value)

    def set_array_dimensions(self, value):
        """
        Set attribute ArrayDimensions of node
        make sure it has the correct data type
        """
        v = ua.Variant(value, ua.VariantType.UInt32)
        self.set_attribute(ua.AttributeIds.ArrayDimensions, ua.DataValue(v))

    def get_array_dimensions(self):
        """
        Read and return ArrayDimensions attribute of node
        """
        res = self.get_attribute(ua.AttributeIds.ArrayDimensions)
        return res.Value.Value

    def set_value_rank(self, value):
        """
        Set attribute ArrayDimensions of node
        """
        v = ua.Variant(value, ua.VariantType.Int32)
        self.set_attribute(ua.AttributeIds.ValueRank, ua.DataValue(v))

    def get_value_rank(self):
        """
        Read and return ArrayDimensions attribute of node
        """
        res = self.get_attribute(ua.AttributeIds.ValueRank)
        return res.Value.Value

    def set_value(self, value, varianttype=None):
        """
        Set value of a node. Only variables(properties) have values.
        An exception will be generated for other node types.
        value argument is either:
        * a python built-in type, converted to opc-ua
        optionnaly using the variantype argument.
        * a ua.Variant, varianttype is then ignored
        * a ua.DataValue, you then have full control over data send to server
        """
        datavalue = None
        if isinstance(value, ua.DataValue):
            datavalue = value
        elif isinstance(value, ua.Variant):
            datavalue = ua.DataValue(value)
        else:
            datavalue = ua.DataValue(ua.Variant(value, varianttype))
        self.set_attribute(ua.AttributeIds.Value, datavalue)

    set_data_value = set_value

    def set_writable(self, writable=True):
        """
        Set node as writable by clients.
        A node is always writable on server side.
        """
        if writable:
            self.set_attr_bit(ua.AttributeIds.AccessLevel, ua.AccessLevel.CurrentWrite)
            self.set_attr_bit(ua.AttributeIds.UserAccessLevel, ua.AccessLevel.CurrentWrite)
        else:
            self.unset_attr_bit(ua.AttributeIds.AccessLevel, ua.AccessLevel.CurrentWrite)
            self.unset_attr_bit(ua.AttributeIds.UserAccessLevel, ua.AccessLevel.CurrentWrite)

    def set_attr_bit(self, attr, bit):
        val = self.get_attribute(attr)
        val.Value.Value = ua.set_bit(val.Value.Value, bit)
        self.set_attribute(attr, val)

    def unset_attr_bit(self, attr, bit):
        val = self.get_attribute(attr)
        val.Value.Value = ua.unset_bit(val.Value.Value, bit)
        self.set_attribute(attr, val)

    def set_read_only(self):
        """
        Set a node as read-only for clients.
        A node is always writable on server side.
        """
        return self.set_writable(False)

    def set_attribute(self, attributeid, datavalue):
        """
        Set an attribute of a node
        attributeid is a member of ua.AttributeIds
        datavalue is a ua.DataValue object
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
        Read one attribute of a node
        result code from server is checked and an exception is raised in case of error
        """
        rv = ua.ReadValueId()
        rv.NodeId = self.nodeid
        rv.AttributeId = attr
        params = ua.ReadParameters()
        params.NodesToRead.append(rv)
        result = self.server.read(params)
        result[0].StatusCode.check()
        return result[0]

    def get_attributes(self, attrs):
        """
        Read several attributes of a node
        list of DataValue is returned
        """
        params = ua.ReadParameters()
        for attr in attrs:
            rv = ua.ReadValueId()
            rv.NodeId = self.nodeid
            rv.AttributeId = attr
            params.NodesToRead.append(rv)

        results = self.server.read(params)
        return results

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
        return self.get_referenced_nodes(refs, ua.BrowseDirection.Forward, nodeclassmask)

    def get_properties(self):
        """
        return properties of node.
        properties are child nodes with a reference of type HasProperty and a NodeClass of Variable
        """
        return self.get_children(refs=ua.ObjectIds.HasProperty, nodeclassmask=ua.NodeClass.Variable)

    def get_variables(self):
        """
        return variables of node.
        properties are child nodes with a reference of type HasComponent and a NodeClass of Variable
        """
        return self.get_children(refs=ua.ObjectIds.HasComponent, nodeclassmask=ua.NodeClass.Variable)

    def get_methods(self):
        """
        return methods of node.
        properties are child nodes with a reference of type HasComponent and a NodeClass of Method
        """
        return self.get_children(refs=ua.ObjectIds.HasComponent, nodeclassmask=ua.NodeClass.Method)

    def get_children_descriptions(self, refs=ua.ObjectIds.HierarchicalReferences, nodeclassmask=ua.NodeClass.Unspecified, includesubtypes=True):
        return self.get_references(refs, ua.BrowseDirection.Forward, nodeclassmask, includesubtypes)

    def get_references(self, refs=ua.ObjectIds.References, direction=ua.BrowseDirection.Both, nodeclassmask=ua.NodeClass.Unspecified, includesubtypes=True):
        """
        returns references of the node based on specific filter defined with:

        refs = ObjectId of the Reference
        direction = Browse direction for references
        nodeclassmask = filter nodes based on specific class
        includesubtypes = If true subtypes of the reference (ref) are also included
        """
        desc = ua.BrowseDescription()
        desc.BrowseDirection = direction
        desc.ReferenceTypeId = ua.TwoByteNodeId(refs)
        desc.IncludeSubtypes = includesubtypes
        desc.NodeClassMask = nodeclassmask
        desc.ResultMask = ua.BrowseResultMask.All

        desc.NodeId = self.nodeid
        params = ua.BrowseParameters()
        params.View.Timestamp = ua.win_epoch_to_datetime(0)
        params.NodesToBrowse.append(desc)
        results = self.server.browse(params)
        return results[0].References

    def get_referenced_nodes(self, refs=ua.ObjectIds.References, direction=ua.BrowseDirection.Both, nodeclassmask=ua.NodeClass.Unspecified, includesubtypes=True):
        """
        returns referenced nodes based on specific filter
        Paramters are the same as for get_references

        """
        references = self.get_references(refs, direction, nodeclassmask, includesubtypes)
        nodes = []
        for desc in references:
            node = Node(self.server, desc.NodeId)
            nodes.append(node)
        return nodes

    def get_type_definition(self):
        """
        returns type definition of the node.
        """
        references = self.get_references(refs=ua.ObjectIds.HasTypeDefinition, direction=ua.BrowseDirection.Forward)
        if len(references) == 0:
            return None
        return references[0].NodeId

    def get_parent(self):
        """
        returns parent of the node.
        """
        refs = self.get_references(refs=ua.ObjectIds.HierarchicalReferences, direction=ua.BrowseDirection.Inverse)

        return Node(self.server, refs[0].NodeId)

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
        rpath = self._make_relative_path(path)
        bpath = ua.BrowsePath()
        bpath.StartingNode = self.nodeid
        bpath.RelativePath = rpath
        result = self.server.translate_browsepaths_to_nodeids([bpath])
        result = result[0]
        result.StatusCode.check()
        # FIXME: seems this method may return several nodes
        return Node(self.server, result.Targets[0].TargetId)

    def _make_relative_path(self, path):
        rpath = ua.RelativePath()
        for item in path:
            el = ua.RelativePathElement()
            el.ReferenceTypeId = ua.TwoByteNodeId(ua.ObjectIds.HierarchicalReferences)
            el.IsInverse = False
            el.IncludeSubtypes = True
            if isinstance(item, ua.QualifiedName):
                el.TargetName = item
            else:
                el.TargetName = ua.QualifiedName.from_string(item)
            rpath.Elements.append(el)
        return rpath

    def read_raw_history(self, starttime=None, endtime=None, numvalues=0):
        """
        Read raw history of a node
        result code from server is checked and an exception is raised in case of error
        If numvalues is > 0 and number of events in period is > numvalues
        then result will be truncated
        """
        details = ua.ReadRawModifiedDetails()
        details.IsReadModified = False
        if starttime:
            details.StartTime = starttime
        else:
            details.StartTime = ua.DateTimeMinValue
        if endtime:
            details.EndTime = endtime
        else:
            details.EndTime = ua.DateTimeMinValue
        details.NumValuesPerNode = numvalues
        details.ReturnBounds = True
        result = self.history_read(details)
        return result.HistoryData.DataValues

    def history_read(self, details):
        """
        Read raw history of a node, low-level function
        result code from server is checked and an exception is raised in case of error
        """
        valueid = ua.HistoryReadValueId()
        valueid.NodeId = self.nodeid
        valueid.IndexRange = ''

        params = ua.HistoryReadParameters()
        params.HistoryReadDetails = details
        params.TimestampsToReturn = ua.TimestampsToReturn.Both
        params.ReleaseContinuationPoints = False
        params.NodesToRead.append(valueid)
        result = self.server.history_read(params)[0]
        return result

    def read_event_history(self, starttime=None, endtime=None, numvalues=0, evtypes=ua.ObjectIds.BaseEventType):
        """
        Read event history of a source node
        result code from server is checked and an exception is raised in case of error
        If numvalues is > 0 and number of events in period is > numvalues
        then result will be truncated
        """

        details = ua.ReadEventDetails()
        if starttime:
            details.StartTime = starttime
        else:
            details.StartTime = ua.DateTimeMinValue
        if endtime:
            details.EndTime = endtime
        else:
            details.EndTime = ua.DateTimeMinValue
        details.NumValuesPerNode = numvalues

        if not isinstance(evtypes, (list, tuple)):
            evtypes = [evtypes]

        evtypes = [Node(self.server, evtype) for evtype in evtypes]

        evfilter = events.get_filter_from_event_type(evtypes)
        details.Filter = evfilter

        result = self.history_read_events(details)
        event_res = []
        for res in result.HistoryData.Events:
            event_res.append(events.Event.from_event_fields(evfilter.SelectClauses, res.EventFields))
        return event_res

    def history_read_events(self, details):
        """
        Read event history of a node, low-level function
        result code from server is checked and an exception is raised in case of error
        """
        valueid = ua.HistoryReadValueId()
        valueid.NodeId = self.nodeid
        valueid.IndexRange = ''

        params = ua.HistoryReadParameters()
        params.HistoryReadDetails = details
        params.TimestampsToReturn = ua.TimestampsToReturn.Both
        params.ReleaseContinuationPoints = False
        params.NodesToRead.append(valueid)
        result = self.server.history_read(params)[0]
        return result

    def add_folder(self, nodeid, bname):
        return  opcua.common.manage_nodes.create_folder(self, nodeid, bname)
 
    def add_object(self, nodeid, bname, objecttype=None):
        return opcua.common.manage_nodes.create_object(self, nodeid, bname, objecttype)
 
    def add_variable(self, nodeid, bname, val, varianttype=None, datatype=None):
        return opcua.common.manage_nodes.create_variable(self, nodeid, bname, val, varianttype, datatype)
 
    def add_object_type(self, nodeid, bname):
        return opcua.common.manage_nodes.create_object_type(self, nodeid, bname)
 
    def add_variable_type(self, nodeid, bname, datatype):
        return opcua.common.manage_nodes.create_variable_type(self, nodeid, bname, datatype)
 
    def add_data_type(self, nodeid, bname, description=None):
        return opcua.common.manage_nodes.create_data_type(self, nodeid, bname, description=None)
 
    def add_property(self, nodeid, bname, val, varianttype=None, datatype=None):
        return opcua.common.manage_nodes.create_property(self, nodeid, bname, val, varianttype, datatype)
 
    def add_method(self, *args):
        return opcua.common.manage_nodes.create_method(self, *args)
 
    def add_reference_type(self, parent, nodeid, bname):
        return opcua.common.manage_nodes.create_reference_type(parent, nodeid, bname)
    
    def call_method(parent, methodid, *args):
        return opcua.common.methods.call_method(parent, methodid, *args)