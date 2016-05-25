from opcua import ua


class EventResult(object):
    """
    To be sent to clients for every events from server
    """

    def __init__(self):
        self.server_handle = None

    def __str__(self):
        return "EventResult({})".format([str(k) + ":" + str(v) for k, v in self.__dict__.items()])
    __repr__ = __str__

    def get_event_props_as_fields_dict(self):
        """
        convert all properties of the EventResult class to a dict of variants
        """
        field_vars = {}
        for key, value in vars(self).items():
            if not key.startswith("__") and key is not "server_handle":
                field_vars[key] = ua.Variant(value)
        return field_vars


def event_obj_from_event_fields(select_clauses, fields):
    result = EventResult()
    for idx, sattr in enumerate(select_clauses):
        if len(sattr.BrowsePath) == 0:
            setattr(result, sattr.AttributeId.name, fields[idx].Value)
        else:
            setattr(result, sattr.BrowsePath[0].Name, fields[idx].Value)
    return result


def get_filter_from_event_type(eventtype):
    evfilter = ua.EventFilter()
    evfilter.SelectClauses = select_clauses_from_evtype(eventtype)
    evfilter.WhereClause = where_clause_from_evtype(eventtype)
    return evfilter


def select_clauses_from_evtype(evtype):
    clauses = []
    for prop in get_event_properties_from_type_node(evtype):
        op = ua.SimpleAttributeOperand()
        op.TypeDefinitionId = evtype.nodeid
        op.AttributeId = ua.AttributeIds.Value
        op.BrowsePath = [prop.get_browse_name()]
        clauses.append(op)
    return clauses


def where_clause_from_evtype(evtype):
    cf = ua.ContentFilter()
    el = ua.ContentFilterElement()
    # operands can be ElementOperand, LiteralOperand, AttributeOperand, SimpleAttribute
    op = ua.SimpleAttributeOperand()
    op.TypeDefinitionId = evtype.nodeid
    op.BrowsePath.append(ua.QualifiedName("EventType", 0))
    op.AttributeId = ua.AttributeIds.Value
    el.FilterOperands.append(op)
    for subtypeid in [st.nodeid for st in get_node_subtypes(evtype)]:
        op = ua.LiteralOperand()
        op.Value = ua.Variant(subtypeid)
        el.FilterOperands.append(op)
    el.FilterOperator = ua.FilterOperator.InList

    cf.Elements.append(el)
    return cf


def get_node_subtypes(node, nodes=None):
    if nodes is None:
        nodes = [node]
    for child in node.get_children(refs=ua.ObjectIds.HasSubtype):
        nodes.append(child)
        get_node_subtypes(child, nodes)
    return nodes


def get_event_properties_from_type_node(node):
    properties = []
    curr_node = node

    while True:
        properties.extend(curr_node.get_properties())

        if curr_node.nodeid.Identifier == ua.ObjectIds.BaseEventType:
            break

        parents = curr_node.get_referenced_nodes(refs=ua.ObjectIds.HasSubtype, direction=ua.BrowseDirection.Inverse, includesubtypes=False)
        if len(parents) != 1:  # Something went wrong
            return None
        curr_node = parents[0]

    return properties
