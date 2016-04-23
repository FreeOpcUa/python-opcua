
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

    def __init__(self, isession, etype=ua.BaseEvent(), source=ua.ObjectIds.Server):
        self.isession = isession
        self.event = None
        node = None

        if isinstance(etype, ua.BaseEvent):
            self.event = etype
        elif isinstance(etype, Node):
            node = etype
        elif isinstance(etype, ua.NodeId):
            node = Node(self.isession, etype)
        else:
            node = Node(self.isession, ua.NodeId(etype))

        if node:
            self.event = get_event_from_node(node)

        if isinstance(source, Node):
            pass
        elif isinstance(source, ua.NodeId):
            source = Node(isession, source)
        else:
            source = Node(isession, ua.NodeId(source))

        if self.event.SourceNode.Identifier:
            source = Node(self.isession, self.event.SourceNode)

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
        self.event.RecieveTime = datetime.utcnow()
        #FIXME: LocalTime is wrong but currently know better. For description s. Part 5 page 18
        self.event.LocalTime = datetime.utcnow()
        if message:
            self.Message = ua.LocalizedText(message)
        elif not self.event.Message:
            self.event.Message = ua.LocalizedText(self.source.get_browse_name().Text)
        self.isession.subscription_service.trigger_event(self.event)


def get_event_from_node(node):
    event = None
    if node.nodeid.Identifier in ua.uaevents_auto.IMPLEMNTED_EVENTS.keys():
        event = ua.uaevents_auto.IMPLEMNTED_EVENTS[node.nodeid.Identifier]()

    else:
        pass
        #node.get

        #class CustomEvent():

            #pass
    #references = node.get_children_descriptions(refs=ua.ObjectIds.HasProperty)
    #for desc in references:
        #child = Node(self.isession, desc.NodeId)
        #setattr(self.event, desc.BrowseName.Name, child.get_value())

    return event


class CustomEvent(ua.BaseEvent):

    def __init__(self, etype=ua.BaseEvent, sourcenode=ua.NodeId(ua.ObjectIds.Server), message=None, severity=1):
        super(CustomEvent, self).__init__(sourcenode, message, severity, True)
        #TODO: Add fileds

    #TODO: Extend to show all fields of CustomEvent
    def __str__(self):
        s = 'CustomEvent('
        s += 'EventId:{}'.format(self.EventId)
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
