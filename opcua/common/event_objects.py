"""
This file contains event types as Python objects.

TODO: This should be auto-generated but is not!!!!!

"""

from opcua import ua
from opcua.common.events import Event


class BaseEvent(Event):
    """
    BaseEvent implements BaseEventType from which inherit all other events and it is used per default.
    """
    def __init__(self, sourcenode=None, message=None, severity=1):
        Event.__init__(self)
        self.add_property("EventId", bytes(), ua.VariantType.ByteString)
        self.add_property("EventType", ua.NodeId(ua.ObjectIds.BaseEventType), ua.VariantType.NodeId)
        self.add_property("SourceNode", sourcenode, ua.VariantType.NodeId)
        self.add_property("SourceName", None, ua.VariantType.String)
        self.add_property("Time", None, ua.VariantType.DateTime)
        self.add_property("ReceiveTime", None, ua.VariantType.DateTime)
        self.add_property("LocalTime", None, ua.VariantType.DateTime)
        self.add_property("Message", ua.LocalizedText(message), ua.VariantType.LocalizedText)
        self.add_property("Severity", severity, ua.VariantType.UInt16)


class AuditEvent(BaseEvent):
    """
    Audit implements AuditEventType from which inherit all other Audit events.
    """
    def __init__(self, sourcenode=None, message=None, severity=1):
        super(AuditEvent, self).__init__(sourcenode, message, severity)
        self.EventType = ua.NodeId(ua.ObjectIds.AuditEventType)
        self.add_property("ActionTimeStamp", None, ua.VariantType.DateTime)
        self.add_property("Status", False, ua.VariantType.Boolean)
        self.add_property("ServerId", None, ua.VariantType.String)
        self.add_property("ClientAuditEntryId", None, ua.VariantType.String)
        self.add_property("ClientUserId", None, ua.VariantType.String)


IMPLEMENTED_EVENTS = {
    ua.ObjectIds.BaseEventType: BaseEvent,
    ua.ObjectIds.AuditEventType: AuditEvent,
    }
