
from datetime import datetime

from opcua import ua
from opcua import Node
import uuid


class Event(object):

    """
    Create an event based on an event type. Per default is BaseEventType used.
    Object members are dynamically created from the base event type and send to
    client when evebt is triggered (see example code in source)

    Arguments to constructor are:

        server: The InternalSession object to use for query and event triggering

        source: The emiting source for the node, either an objectId, NodeId or a Node

        etype: The event type, either an objectId, a NodeId or a Node object
    """

    def __init__(self, isession, etype=ua.ObjectIds.BaseEventType, source=ua.ObjectIds.Server):
        self.isession = isession

        if isinstance(etype, Node):
            self.node = etype
        elif isinstance(etype, ua.NodeId):
            self.node = Node(self.isession, etype)
        else:
            self.node = Node(self.isession, ua.NodeId(etype))

        self._set_members_from_node(self.node)
        if isinstance(source, Node):
            self.SourceNode = source.NodeId
        elif isinstance(etype, ua.NodeId):
            self.SourceNode = source.NodeId
        else:
            self.SourceNode = ua.NodeId(source)

        # set some default values for attributes from BaseEventType, thus that all event must have
        self.EventId = uuid.uuid4().bytes
        self.EventType = self.node.nodeid
        self.LocaleTime = datetime.utcnow()
        self.ReceiveTime = datetime.utcnow()
        self.Time = datetime.utcnow()
        self.Message = ua.LocalizedText()
        self.Severity = ua.Variant(1, ua.VariantType.UInt16)
        self.SourceName = "Server"

        # og set some node attributed we also are expected to have
        self.BrowseName = self.node.get_browse_name()
        self.DisplayName = self.node.get_display_name()
        self.NodeId = self.node.nodeid
        self.NodeClass = self.node.get_node_class()
        self.Description = self.node.get_description()

    def __str__(self):
        return "Event(Type:{}, Source:{}, Time:{}, Message: {})".format(self.EventType, self.SourceNode, self.Time, self.Message)
    __repr__ = __str__

    def trigger(self):
        """
        Trigger the event. This will send a notification to all subscribed clients
        """
        self.isession.subscription_service.trigger_event(self)

    def _set_members_from_node(self, node):
        references = node.get_children_descriptions(refs=ua.ObjectIds.HasProperty)
        for desc in references:
            node = Node(self.isession, desc.NodeId)
            setattr(self, desc.BrowseName.Name, node.get_value())
