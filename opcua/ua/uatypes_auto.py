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
    def __init__(self, sourcenode=NodeId(ObjectIds.Server), message=None, severity=1, extended=False):
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
        s = 'BaseEventType(EventId:{}'.format(self.EventId)
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
