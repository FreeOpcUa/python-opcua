
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

        event: The event object
    """

    def __init__(self, isession, event=ua.BaseEvent()):
        self.isession = isession
        self.event = event

        self.source = Node(isession, self.event.SourceNode)
        if self.event.SourceNode.Identifier:
            self.event.SourceName = self.source.get_display_name().Text
            self.source.set_attribute(ua.AttributeIds.EventNotifier, ua.DataValue(ua.Variant(1, ua.VariantType.Byte)))

    def __str__(self):
        return "EventGenerator(Event:{})".format(self.event)
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
        elif not self.event.Message and self.event.SourceNode.Identifier:
            self.event.Message = ua.LocalizedText(self.source.get_browse_name().Text)
        self.isession.subscription_service.trigger_event(self.event)
