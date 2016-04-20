
from datetime import datetime

from opcua import ua
from opcua import Node
import uuid


class EventGenerator(object):

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
        self.node = None
        self.event = etype

        if isinstance(etype, ua.BaseEvent):
            pass
        elif isinstance(etype, Node):
            self.node = etype
        elif isinstance(etype, ua.NodeId):
            self.node = Node(self.isession, etype)
        else:
            self.node = Node(self.isession, ua.NodeId(etype))

        if self.node:
            event = CustomEvent()
            references = node.get_children_descriptions(refs=ua.ObjectIds.HasProperty)
            for desc in references:
                node = Node(self.isession, desc.NodeId)
                setattr(self, desc.BrowseName.Name, node.get_value())

        if isinstance(source, Node):
            pass
        elif isinstance(source, NodeId):
            source = ua.Node(isession, source)
        else:
            source = Node(isession, ua.NodeId(source))

        if self.event.SourceNode.Identifier:
            source = Node(self.iserver.isession, self.event.SourceNode)

        self.event.SourceName = source.get_display_name().Text
        source.set_attribute(ua.AttributeIds.EventNotifier, ua.DataValue(ua.Variant(1, ua.VariantType.Byte)))

    def __str__(self):
        return "EventGenerator(Type:{}, Source:{}, Time:{}, Message: {})".format(self.EventType, self.SourceNode, self.Time, self.Message)
    __repr__ = __str__

    def trigger(self, time=None, message=None):
        """
        Trigger the event. This will send a notification to all subscribed clients
        """
        self.event.EventId = ua.Variant(uuid.uuid4().hex, ua.VariantType.ByteString)
        if time:
            self.event.Time = time
        else:
            self.event.Time = datetime.utcnow()
        self.event.ReciveTime = datetime.utcnow()
        #FIXME: LocalTime is wrong but currently know better. For description s. Part 5 page 18
        self.event.LocaleTime = datetime.utcnow()
        if message:
            self.Message = ua.LocalizedText(message)
        elif not self.event.Message:
            self.event.Message = ua.LocalizedText(self.source.get_browse_name().Text)
        self.isession.subscription_service.trigger_event(self.event)


class CustomEvent(ua.BaseEvent):

    def __init__(self, etype=ua.ObjectIds.BaseEventType, sourcenode=ua.NodeId(ua.ObjectIds.Server), message=None, severity=1):
        super(ua.BaseEvent, self).__init__(sourcenode, message, severity, True)
        #TODO: Add fileds

    #TODO: Extend to show all fields of CustomEvent
    def __str__(self):
        s = 'CustomEvent(EventId:{}'.format(self.EventId)
        s += ', EventType:{}'.format(self.EventType)
        s += ', SourceNode:{}'.format(self.SourceNode)
        s += ', SourceName:{}'.format(self.SourceName)
        s += ', Time:{}'.format(self.Time)
        s += ', RecieveTime:{}'.format(self.RecieveTime)
        s += ', LocalTime:{}'.format(self.LocalTime)
        s += ', Message:{}'.format(self.Message)
        s += ', Severity:{}'.format(self.Severity)
        s += ')'
        return s
    __repr__ = __str__
