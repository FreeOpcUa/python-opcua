from opcua import ua


class EventResult(object):
    """
    To be sent to clients for every events from server
    """

    def __init__(self):
        self.server_handle = None
        self.select_clauses = None
        self.event_fields = None
        self.data_types = {}
        # save current attributes
        self.internal_properties = list(self.__dict__.keys())[:] + ["internal_properties"]

    def __str__(self):
        return "EventResult({})".format([str(k) + ":" + str(v) for k, v in self.__dict__.items() if k not in self.internal_properties])
    __repr__ = __str__

    def get_event_props_as_fields_dict(self):
        """
        convert all properties of the EventResult class to a dict of variants
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
        result = EventResult()
        for k, v in fields.items():
            setattr(result, k, v.Value)
            result.data_types[k] = v.VariantType
        return result

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
        fields = []
        for sattr in select_clauses:
            if len(sattr.BrowsePath) == 0:
                name = sattr.AttributeId.name
            else:
                name = sattr.BrowsePath[0].Name
            field = getattr(self, name)
            fields.append(ua.Variant(field, self.data_types[name]))
        return fields

    @staticmethod
    def from_event_fields(select_clauses, fields):
        """
        Instanciate an Event object from a select_clauses and fields 
        """
        result = EventResult()
        result.select_clauses = select_clauses
        result.event_fields = fields
        for idx, sattr in enumerate(select_clauses):
            if len(sattr.BrowsePath) == 0:
                name = sattr.AttributeId.name
            else:
                name = sattr.BrowsePath[0].Name
            setattr(result, name, fields[idx].Value)
            result.data_types[name] = fields[idx].VariantType
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


