'''
Example auto_generated file with UA Types

For now only events!
'''

from opcua.ua import *


# TODO: This should be autogeneratd form XML description of EventTypes
class BaseEvent(FrozenClass):
    '''
    BaseEvent implements BaseEventType from which inherit all other events and it is used per default.
    '''
    def __init__(self, sourcenode=None, message=None, severity=1, extended=False):
        self.EventId = bytes()
        self.EventType = NodeId(ObjectIds.BaseEventType)
        self.SourceNode = sourcenode
        self.SourceName = None
        self.Time = None
        self.RecieveTime = None
        self.LocalTime = None
        self.Message = LocalizedText(message)
        self.Severity = Variant(severity, VariantType.UInt16)
        if not extended:
            self._freeze = True

    def __str__(self):
        return "{}({})".format(type(self).__name__, [str(k) + ":" + str(v) for k, v in self.__dict__.items()])
    __repr__ = __str__


class AuditEvent(BaseEvent):
    '''
    Audit implements AuditEventType from which inherit all other Audit events.
    '''
    def __init__(self, sourcenode=None, message=None, severity=1, extended=False):
        super(AuditEvent, self).__init__(sourcenode, message, severity, True)

        self.ActionTimeStamp = None
        self.Status = False
        self.ServerId = None
        self.ClientAuditEntryId = None
        self.ClientUserId = None
        if not extended:
            self._freeze = True


IMPLEMNTED_EVENTS = {
    ObjectIds.BaseEventType: BaseEvent,
    ObjectIds.AuditEventType: AuditEvent,
    }
