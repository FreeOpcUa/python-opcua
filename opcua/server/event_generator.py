import logging
from datetime import datetime
import uuid

from opcua import ua
from opcua import Node
from opcua.common import events
from opcua.common import event_objects


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

    def __init__(self, isession, etype=None, source=ua.ObjectIds.Server):
        if not etype:
            etype = event_objects.BaseEvent()

        self.logger = logging.getLogger(__name__)
        self.isession = isession
        self.event = None
        node = None

        if isinstance(etype, event_objects.BaseEvent):
            self.event = etype
        elif isinstance(etype, Node):
            node = etype
        elif isinstance(etype, ua.NodeId):
            node = Node(self.isession, etype)
        else:
            node = Node(self.isession, ua.NodeId(etype))

        if node:
            self.event = events.get_event_obj_from_type_node(node)

        if isinstance(source, Node):
            pass
        elif isinstance(source, ua.NodeId):
            source = Node(isession, source)
        else:
            source = Node(isession, ua.NodeId(source))

        if self.event.SourceNode:
            if source.nodeid != self.event.SourceNode:
                self.logger.warning(
                    "Source NodeId: '%s' and event SourceNode: '%s' are not the same. Using '%s' as SourceNode",
                    str(source.nodeid), str(self.event.SourceNode), str(self.event.SourceNode))
                source = Node(self.isession, self.event.SourceNode)

        self.event.SourceNode = source.nodeid
        self.event.SourceName = source.get_browse_name().Name

        source.set_event_notifier([ua.EventNotifier.SubscribeToEvents, ua.EventNotifier.HistoryRead])
        refs = []
        ref = ua.AddReferencesItem()
        ref.IsForward = True
        ref.ReferenceTypeId = ua.NodeId(ua.ObjectIds.GeneratesEvent)
        ref.SourceNodeId = source.nodeid
        ref.TargetNodeClass = ua.NodeClass.ObjectType
        ref.TargetNodeId = self.event.EventType
        refs.append(ref)
        results = self.isession.add_references(refs)
        # result.StatusCode.check()

    def __str__(self):
        return "EventGenerator(Type:{0}, Source:{1}, Time:{2}, Message: {3})".format(self.event.EventType,
                                                                                 self.event.SourceNode,
                                                                                 self.event.Time,
                                                                                 self.event.Message)
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
        self.event.ReceiveTime = datetime.utcnow()
        # FIXME: LocalTime is wrong but currently know better. For description s. Part 5 page 18
        self.event.LocalTime = datetime.utcnow()
        if message:
            self.event.Message = ua.LocalizedText(message)
        elif not self.event.Message:
            self.event.Message = ua.LocalizedText(Node(self.isession, self.event.SourceNode).get_browse_name().Text)
        self.isession.subscription_service.trigger_event(self.event)
