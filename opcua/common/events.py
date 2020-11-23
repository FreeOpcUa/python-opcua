import copy

from opcua import ua
import opcua
from opcua.ua.uaerrors import UaError
from opcua.common import ua_utils


class Event(object):
    """
    OPC UA Event object.
    This is class in inherited by the common event objects such as BaseEvent,
    other auto standard events and custom events
    Events are used to trigger events on server side and are
    sent to clients for every events from server

    Developper Warning:
    On server side the data type of attributes should be known, thus
    add properties using the add_property method!!!
    """

    def __init__(self, emitting_node=ua.ObjectIds.Server):
        self.server_handle = None
        self.select_clauses = None
        self.event_fields = None
        self.data_types = {}
        if isinstance(emitting_node, ua.NodeId):
            self.emitting_node = emitting_node
        else:
            self.emitting_node = ua.NodeId(emitting_node)
        # save current attributes
        self.internal_properties = list(self.__dict__.keys())[:] + ["internal_properties"]

    def __str__(self):
        return "{0}({1})".format(
            self.__class__.__name__,
            [str(k) + ":" + str(v) for k, v in self.__dict__.items() if k not in self.internal_properties])
    __repr__ = __str__

    def add_property(self, name, val, datatype):
        """
        Add a property to event and tore its data type
        """
        setattr(self, name, val)
        self.data_types[name] = datatype

    def get_event_props_as_fields_dict(self):
        """
        convert all properties of the Event class to a dict of variants
        """
        field_vars = {}
        for key, value in vars(self).items():
            if not key.startswith("__") and key not in self.internal_properties:
                field_vars[key] = ua.Variant(value, self.data_types[key])
        return field_vars

    @staticmethod
    def from_field_dict(fields):
        """
        Create an Event object from a dict of name and variants
        """
        ev = Event()
        for k, v in fields.items():
            ev.add_property(k, v.Value, v.VariantType)
        return ev

    def to_event_fields_using_subscription_fields(self, select_clauses):
        """
        Using a new select_clauses and the original select_clauses
        used during subscription, return a field list
        """
        fields = []
        for sattr in select_clauses:
            for idx, o_sattr in enumerate(self.select_clauses):
                if sattr.BrowsePath == o_sattr.BrowsePath and sattr.AttributeId == o_sattr.AttributeId:
                    fields.append(self.event_fields[idx])
                    break
        return fields

    def to_event_fields(self, select_clauses):
        """
        return a field list using a select clause and the object properties
        """
        none_field = ua.Variant(None, ua.VariantType.Null)
        fields = []
        for sattr in select_clauses:
            if not sattr.BrowsePath:
                name = ua.AttributeIds(sattr.AttributeId).name
            else:
                name = sattr.BrowsePath[0].Name
            try:
                val = getattr(self, name)
            except AttributeError:
                field = none_field
            else:
                field = ua.Variant(copy.deepcopy(val), self.data_types[name])
            fields.append(field)
        return fields

    @staticmethod
    def from_event_fields(select_clauses, fields):
        """
        Instantiate an Event object from a select_clauses and fields
        """
        ev = Event()
        ev.select_clauses = select_clauses
        ev.event_fields = fields
        for idx, sattr in enumerate(select_clauses):
            if len(sattr.BrowsePath) == 0:
                name = sattr.AttributeId.name
            else:
                name = sattr.BrowsePath[0].Name
            ev.add_property(name, fields[idx].Value, fields[idx].VariantType)
        return ev


def get_filter_from_event_type(eventtypes):
    evfilter = ua.EventFilter()
    evfilter.SelectClauses = select_clauses_from_evtype(eventtypes)
    evfilter.WhereClause = where_clause_from_evtype(eventtypes)
    return evfilter


def select_clauses_from_evtype(evtypes):
    clauses = []

    selected_paths = []
    for evtype in evtypes:
        for prop in get_event_properties_from_type_node(evtype):
            if prop.get_browse_name() not in selected_paths:
                op = ua.SimpleAttributeOperand()
                op.AttributeId = ua.AttributeIds.Value
                op.BrowsePath = [prop.get_browse_name()]
                clauses.append(op)
                selected_paths.append(prop.get_browse_name())
    return clauses


def where_clause_from_evtype(evtypes):
    cf = ua.ContentFilter()
    el = ua.ContentFilterElement()

    # operands can be ElementOperand, LiteralOperand, AttributeOperand, SimpleAttribute
    # Create a clause where the generate event type property EventType
    # must be a subtype of events in evtypes argument

    # the first operand is the attribute event type
    op = ua.SimpleAttributeOperand()
    # op.TypeDefinitionId = evtype.nodeid
    op.BrowsePath.append(ua.QualifiedName("EventType", 0))
    op.AttributeId = ua.AttributeIds.Value
    el.FilterOperands.append(op)

    # now create a list of all subtypes we want to accept
    subtypes = []
    for evtype in evtypes:
        subtypes += [st.nodeid for st in ua_utils.get_node_subtypes(evtype)]
    subtypes = list(set(subtypes))  # remove duplicates
    for subtypeid in subtypes:
        op = ua.LiteralOperand()
        op.Value = ua.Variant(subtypeid)
        el.FilterOperands.append(op)

    el.FilterOperator = ua.FilterOperator.InList
    cf.Elements.append(el)

    return cf


def get_event_properties_from_type_node(node):
    properties = []
    curr_node = node

    while True:
        properties.extend(curr_node.get_properties())

        if curr_node.nodeid.Identifier == ua.ObjectIds.BaseEventType:
            break

        parents = curr_node.get_referenced_nodes(refs=ua.ObjectIds.HasSubtype, direction=ua.BrowseDirection.Inverse, includesubtypes=True)
        if len(parents) != 1:  # Something went wrong
            return None
        curr_node = parents[0]

    return properties


def get_event_obj_from_type_node(node):
    """
    return an Event object from an event type node
    """
    if node.nodeid.Identifier in opcua.common.event_objects.IMPLEMENTED_EVENTS.keys():
        return opcua.common.event_objects.IMPLEMENTED_EVENTS[node.nodeid.Identifier]()
    else:
        parent_identifier, parent_eventtype = _find_parent_eventtype(node)

        class CustomEvent(parent_eventtype):

            def __init__(self):
                parent_eventtype.__init__(self)
                self.EventType = node.nodeid
                curr_node = node

                while curr_node.nodeid.Identifier != parent_identifier:
                    for prop in curr_node.get_properties():
                        name = prop.get_browse_name().Name
                        val = prop.get_data_value()
                        self.add_property(name, val.Value.Value, val.Value.VariantType)
                    parents = curr_node.get_referenced_nodes(refs=ua.ObjectIds.HasSubtype, direction=ua.BrowseDirection.Inverse, includesubtypes=True)

                    if len(parents) != 1:  # Something went wrong
                        raise UaError("Parent of event type could notbe found")
                    curr_node = parents[0]

                self._freeze = True

    return CustomEvent()


def _find_parent_eventtype(node):
    """
    """
    parents = node.get_referenced_nodes(refs=ua.ObjectIds.HasSubtype, direction=ua.BrowseDirection.Inverse, includesubtypes=True)

    if len(parents) != 1:   # Something went wrong
        raise UaError("Parent of event type could notbe found")
    if parents[0].nodeid.Identifier in opcua.common.event_objects.IMPLEMENTED_EVENTS.keys():
        return parents[0].nodeid.Identifier, opcua.common.event_objects.IMPLEMENTED_EVENTS[parents[0].nodeid.Identifier]
    else:
        return _find_parent_eventtype(parents[0])

