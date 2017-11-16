"""
Autogenerated code from xml spec
"""

from opcua import ua
from opcua.common.events import Event

class BaseEvent(Event):
    """
    BaseEvent: The base type for all events.
    """
    def __init__(self, sourcenode=None, message=None, severity=1):
        Event.__init__(self)
        self.add_property('EventId', None, ua.VariantType.ByteString)
        self.add_property('EventType', ua.NodeId(ua.ObjectIds.BaseEventType), ua.VariantType.NodeId)
        self.add_property('SourceNode', sourcenode, ua.VariantType.NodeId)
        self.add_property('SourceName', None, ua.VariantType.String)
        self.add_property('Time', None, ua.VariantType.DateTime)
        self.add_property('ReceiveTime', None, ua.VariantType.DateTime)
        self.add_property('LocalTime', None, ua.VariantType.DateTime)
        self.add_property('Message', ua.LocalizedText(message), ua.VariantType.LocalizedText)
        self.add_property('Severity', severity, ua.VariantType.UInt16)

class AuditEvent(BaseEvent):
    """
    AuditEvent: A base type for events used to track client initiated changes to the server state.
    """
    def __init__(self, sourcenode=None, message=None, severity=1):
        super(AuditEvent, self).__init__(sourcenode, message, severity)
        self.EventType = ua.NodeId(ua.ObjectIds.AuditEventType)
        self.add_property('ActionTimeStamp', None, ua.NodeId(ua.ObjectIds.UtcTime))
        self.add_property('Status', False, ua.VariantType.Boolean)
        self.add_property('ServerId', None, ua.VariantType.String)
        self.add_property('ClientAuditEntryId', None, ua.VariantType.String)
        self.add_property('ClientUserId', None, ua.VariantType.String)

class AuditSecurityEvent(AuditEvent):
    """
    AuditSecurityEvent: A base type for events used to track security related changes.
    """
    def __init__(self, sourcenode=None, message=None, severity=1):
        super(AuditSecurityEvent, self).__init__(sourcenode, message, severity)
        self.EventType = ua.NodeId(ua.ObjectIds.AuditSecurityEventType)

class AuditChannelEvent(AuditSecurityEvent):
    """
    AuditChannelEvent: A base type for events used to track related changes to a secure channel.
    """
    def __init__(self, sourcenode=None, message=None, severity=1):
        super(AuditChannelEvent, self).__init__(sourcenode, message, severity)
        self.EventType = ua.NodeId(ua.ObjectIds.AuditChannelEventType)
        self.add_property('SecureChannelId', None, ua.VariantType.String)

class AuditOpenSecureChannelEvent(AuditChannelEvent):
    """
    AuditOpenSecureChannelEvent: An event that is raised when a secure channel is opened.
    """
    def __init__(self, sourcenode=None, message=None, severity=1):
        super(AuditOpenSecureChannelEvent, self).__init__(sourcenode, message, severity)
        self.EventType = ua.NodeId(ua.ObjectIds.AuditOpenSecureChannelEventType)
        self.add_property('ClientCertificate', None, ua.VariantType.ByteString)
        self.add_property('ClientCertificateThumbprint', None, ua.VariantType.String)
        self.add_property('RequestType', None, ua.NodeId(ua.ObjectIds.SecurityTokenRequestType))
        self.add_property('SecurityPolicyUri', None, ua.VariantType.String)
        self.add_property('SecurityMode', None, ua.NodeId(ua.ObjectIds.MessageSecurityMode))
        self.add_property('RequestedLifetime', None, ua.NodeId(ua.ObjectIds.Duration))

class AuditSessionEvent(AuditSecurityEvent):
    """
    AuditSessionEvent: A base type for events used to track related changes to a session.
    """
    def __init__(self, sourcenode=None, message=None, severity=1):
        super(AuditSessionEvent, self).__init__(sourcenode, message, severity)
        self.EventType = ua.NodeId(ua.ObjectIds.AuditSessionEventType)
        self.add_property('SessionId', ua.NodeId(ua.ObjectIds.AuditSessionEventType), ua.VariantType.NodeId)

class AuditCreateSessionEvent(AuditSessionEvent):
    """
    AuditCreateSessionEvent: An event that is raised when a session is created.
    """
    def __init__(self, sourcenode=None, message=None, severity=1):
        super(AuditCreateSessionEvent, self).__init__(sourcenode, message, severity)
        self.EventType = ua.NodeId(ua.ObjectIds.AuditCreateSessionEventType)
        self.add_property('SecureChannelId', None, ua.VariantType.String)
        self.add_property('ClientCertificate', None, ua.VariantType.ByteString)
        self.add_property('ClientCertificateThumbprint', None, ua.VariantType.String)
        self.add_property('RevisedSessionTimeout', None, ua.NodeId(ua.ObjectIds.Duration))

class AuditActivateSessionEvent(AuditSessionEvent):
    """
    AuditActivateSessionEvent: 
    """
    def __init__(self, sourcenode=None, message=None, severity=1):
        super(AuditActivateSessionEvent, self).__init__(sourcenode, message, severity)
        self.EventType = ua.NodeId(ua.ObjectIds.AuditActivateSessionEventType)
        self.add_property('ClientSoftwareCertificates', None, ua.NodeId(ua.ObjectIds.SignedSoftwareCertificate))
        self.add_property('UserIdentityToken', None, ua.NodeId(ua.ObjectIds.UserIdentityToken))
        self.add_property('SecureChannelId', None, ua.VariantType.String)

class AuditCancelEvent(AuditSessionEvent):
    """
    AuditCancelEvent: 
    """
    def __init__(self, sourcenode=None, message=None, severity=1):
        super(AuditCancelEvent, self).__init__(sourcenode, message, severity)
        self.EventType = ua.NodeId(ua.ObjectIds.AuditCancelEventType)
        self.add_property('RequestHandle', None, ua.VariantType.UInt32)

class AuditCertificateEvent(AuditSecurityEvent):
    """
    AuditCertificateEvent: 
    """
    def __init__(self, sourcenode=None, message=None, severity=1):
        super(AuditCertificateEvent, self).__init__(sourcenode, message, severity)
        self.EventType = ua.NodeId(ua.ObjectIds.AuditCertificateEventType)
        self.add_property('Certificate', None, ua.VariantType.ByteString)

class AuditCertificateDataMismatchEvent(AuditCertificateEvent):
    """
    AuditCertificateDataMismatchEvent: 
    """
    def __init__(self, sourcenode=None, message=None, severity=1):
        super(AuditCertificateDataMismatchEvent, self).__init__(sourcenode, message, severity)
        self.EventType = ua.NodeId(ua.ObjectIds.AuditCertificateDataMismatchEventType)
        self.add_property('InvalidHostname', None, ua.VariantType.String)
        self.add_property('InvalidUri', None, ua.VariantType.String)

class AuditCertificateExpiredEvent(AuditCertificateEvent):
    """
    AuditCertificateExpiredEvent: 
    """
    def __init__(self, sourcenode=None, message=None, severity=1):
        super(AuditCertificateExpiredEvent, self).__init__(sourcenode, message, severity)
        self.EventType = ua.NodeId(ua.ObjectIds.AuditCertificateExpiredEventType)

class AuditCertificateInvalidEvent(AuditCertificateEvent):
    """
    AuditCertificateInvalidEvent: 
    """
    def __init__(self, sourcenode=None, message=None, severity=1):
        super(AuditCertificateInvalidEvent, self).__init__(sourcenode, message, severity)
        self.EventType = ua.NodeId(ua.ObjectIds.AuditCertificateInvalidEventType)

class AuditCertificateUntrustedEvent(AuditCertificateEvent):
    """
    AuditCertificateUntrustedEvent: 
    """
    def __init__(self, sourcenode=None, message=None, severity=1):
        super(AuditCertificateUntrustedEvent, self).__init__(sourcenode, message, severity)
        self.EventType = ua.NodeId(ua.ObjectIds.AuditCertificateUntrustedEventType)

class AuditCertificateRevokedEvent(AuditCertificateEvent):
    """
    AuditCertificateRevokedEvent: 
    """
    def __init__(self, sourcenode=None, message=None, severity=1):
        super(AuditCertificateRevokedEvent, self).__init__(sourcenode, message, severity)
        self.EventType = ua.NodeId(ua.ObjectIds.AuditCertificateRevokedEventType)

class AuditCertificateMismatchEvent(AuditCertificateEvent):
    """
    AuditCertificateMismatchEvent: 
    """
    def __init__(self, sourcenode=None, message=None, severity=1):
        super(AuditCertificateMismatchEvent, self).__init__(sourcenode, message, severity)
        self.EventType = ua.NodeId(ua.ObjectIds.AuditCertificateMismatchEventType)

class AuditNodeManagementEvent(AuditEvent):
    """
    AuditNodeManagementEvent: 
    """
    def __init__(self, sourcenode=None, message=None, severity=1):
        super(AuditNodeManagementEvent, self).__init__(sourcenode, message, severity)
        self.EventType = ua.NodeId(ua.ObjectIds.AuditNodeManagementEventType)

class AuditAddNodesEvent(AuditNodeManagementEvent):
    """
    AuditAddNodesEvent: 
    """
    def __init__(self, sourcenode=None, message=None, severity=1):
        super(AuditAddNodesEvent, self).__init__(sourcenode, message, severity)
        self.EventType = ua.NodeId(ua.ObjectIds.AuditAddNodesEventType)
        self.add_property('NodesToAdd', None, ua.NodeId(ua.ObjectIds.AddNodesItem))

class AuditDeleteNodesEvent(AuditNodeManagementEvent):
    """
    AuditDeleteNodesEvent: 
    """
    def __init__(self, sourcenode=None, message=None, severity=1):
        super(AuditDeleteNodesEvent, self).__init__(sourcenode, message, severity)
        self.EventType = ua.NodeId(ua.ObjectIds.AuditDeleteNodesEventType)
        self.add_property('NodesToDelete', None, ua.NodeId(ua.ObjectIds.DeleteNodesItem))

class AuditAddReferencesEvent(AuditNodeManagementEvent):
    """
    AuditAddReferencesEvent: 
    """
    def __init__(self, sourcenode=None, message=None, severity=1):
        super(AuditAddReferencesEvent, self).__init__(sourcenode, message, severity)
        self.EventType = ua.NodeId(ua.ObjectIds.AuditAddReferencesEventType)
        self.add_property('ReferencesToAdd', None, ua.NodeId(ua.ObjectIds.AddReferencesItem))

class AuditDeleteReferencesEvent(AuditNodeManagementEvent):
    """
    AuditDeleteReferencesEvent: 
    """
    def __init__(self, sourcenode=None, message=None, severity=1):
        super(AuditDeleteReferencesEvent, self).__init__(sourcenode, message, severity)
        self.EventType = ua.NodeId(ua.ObjectIds.AuditDeleteReferencesEventType)
        self.add_property('ReferencesToDelete', None, ua.NodeId(ua.ObjectIds.DeleteReferencesItem))

class AuditUpdateEvent(AuditEvent):
    """
    AuditUpdateEvent: 
    """
    def __init__(self, sourcenode=None, message=None, severity=1):
        super(AuditUpdateEvent, self).__init__(sourcenode, message, severity)
        self.EventType = ua.NodeId(ua.ObjectIds.AuditUpdateEventType)

class AuditWriteUpdateEvent(AuditUpdateEvent):
    """
    AuditWriteUpdateEvent: 
    """
    def __init__(self, sourcenode=None, message=None, severity=1):
        super(AuditWriteUpdateEvent, self).__init__(sourcenode, message, severity)
        self.EventType = ua.NodeId(ua.ObjectIds.AuditWriteUpdateEventType)
        self.add_property('AttributeId', None, ua.VariantType.UInt32)
        self.add_property('IndexRange', None, ua.NodeId(ua.ObjectIds.NumericRange))
        self.add_property('OldValue', None, ua.VariantType.Variant)
        self.add_property('NewValue', None, ua.VariantType.Variant)

class AuditHistoryUpdateEvent(AuditUpdateEvent):
    """
    AuditHistoryUpdateEvent: 
    """
    def __init__(self, sourcenode=None, message=None, severity=1):
        super(AuditHistoryUpdateEvent, self).__init__(sourcenode, message, severity)
        self.EventType = ua.NodeId(ua.ObjectIds.AuditHistoryUpdateEventType)
        self.add_property('ParameterDataTypeId', ua.NodeId(ua.ObjectIds.AuditHistoryUpdateEventType), ua.VariantType.NodeId)

class AuditUpdateMethodEvent(AuditEvent):
    """
    AuditUpdateMethodEvent: 
    """
    def __init__(self, sourcenode=None, message=None, severity=1):
        super(AuditUpdateMethodEvent, self).__init__(sourcenode, message, severity)
        self.EventType = ua.NodeId(ua.ObjectIds.AuditUpdateMethodEventType)
        self.add_property('MethodId', ua.NodeId(ua.ObjectIds.AuditUpdateMethodEventType), ua.VariantType.NodeId)
        self.add_property('InputArguments', None, ua.VariantType.Variant)

class SystemEvent(BaseEvent):
    """
    SystemEvent: 
    """
    def __init__(self, sourcenode=None, message=None, severity=1):
        super(SystemEvent, self).__init__(sourcenode, message, severity)
        self.EventType = ua.NodeId(ua.ObjectIds.SystemEventType)

class DeviceFailureEvent(SystemEvent):
    """
    DeviceFailureEvent: 
    """
    def __init__(self, sourcenode=None, message=None, severity=1):
        super(DeviceFailureEvent, self).__init__(sourcenode, message, severity)
        self.EventType = ua.NodeId(ua.ObjectIds.DeviceFailureEventType)

class BaseModelChangeEvent(BaseEvent):
    """
    BaseModelChangeEvent: 
    """
    def __init__(self, sourcenode=None, message=None, severity=1):
        super(BaseModelChangeEvent, self).__init__(sourcenode, message, severity)
        self.EventType = ua.NodeId(ua.ObjectIds.BaseModelChangeEventType)

class GeneralModelChangeEvent(BaseModelChangeEvent):
    """
    GeneralModelChangeEvent: 
    """
    def __init__(self, sourcenode=None, message=None, severity=1):
        super(GeneralModelChangeEvent, self).__init__(sourcenode, message, severity)
        self.EventType = ua.NodeId(ua.ObjectIds.GeneralModelChangeEventType)
        self.add_property('Changes', None, ua.NodeId(ua.ObjectIds.ModelChangeStructureDataType))

class TransitionEvent(BaseEvent):
    """
    TransitionEvent: 
    """
    def __init__(self, sourcenode=None, message=None, severity=1):
        super(TransitionEvent, self).__init__(sourcenode, message, severity)
        self.EventType = ua.NodeId(ua.ObjectIds.TransitionEventType)

class AuditUpdateStateEvent(AuditUpdateMethodEvent):
    """
    AuditUpdateStateEvent: 
    """
    def __init__(self, sourcenode=None, message=None, severity=1):
        super(AuditUpdateStateEvent, self).__init__(sourcenode, message, severity)
        self.EventType = ua.NodeId(ua.ObjectIds.AuditUpdateStateEventType)
        self.add_property('OldStateId', None, ua.VariantType.Variant)
        self.add_property('NewStateId', None, ua.VariantType.Variant)

class ProgramTransitionEvent(TransitionEvent):
    """
    ProgramTransitionEvent: 
    """
    def __init__(self, sourcenode=None, message=None, severity=1):
        super(ProgramTransitionEvent, self).__init__(sourcenode, message, severity)
        self.EventType = ua.NodeId(ua.ObjectIds.ProgramTransitionEventType)
        self.add_property('IntermediateResult', None, ua.VariantType.Variant)

class SemanticChangeEvent(BaseModelChangeEvent):
    """
    SemanticChangeEvent: 
    """
    def __init__(self, sourcenode=None, message=None, severity=1):
        super(SemanticChangeEvent, self).__init__(sourcenode, message, severity)
        self.EventType = ua.NodeId(ua.ObjectIds.SemanticChangeEventType)
        self.add_property('Changes', None, ua.NodeId(ua.ObjectIds.SemanticChangeStructureDataType))

class AuditUrlMismatchEvent(AuditCreateSessionEvent):
    """
    AuditUrlMismatchEvent: 
    """
    def __init__(self, sourcenode=None, message=None, severity=1):
        super(AuditUrlMismatchEvent, self).__init__(sourcenode, message, severity)
        self.EventType = ua.NodeId(ua.ObjectIds.AuditUrlMismatchEventType)
        self.add_property('EndpointUrl', None, ua.VariantType.String)

class RefreshStartEvent(SystemEvent):
    """
    RefreshStartEvent: 
    """
    def __init__(self, sourcenode=None, message=None, severity=1):
        super(RefreshStartEvent, self).__init__(sourcenode, message, severity)
        self.EventType = ua.NodeId(ua.ObjectIds.RefreshStartEventType)

class RefreshEndEvent(SystemEvent):
    """
    RefreshEndEvent: 
    """
    def __init__(self, sourcenode=None, message=None, severity=1):
        super(RefreshEndEvent, self).__init__(sourcenode, message, severity)
        self.EventType = ua.NodeId(ua.ObjectIds.RefreshEndEventType)

class RefreshRequiredEvent(SystemEvent):
    """
    RefreshRequiredEvent: 
    """
    def __init__(self, sourcenode=None, message=None, severity=1):
        super(RefreshRequiredEvent, self).__init__(sourcenode, message, severity)
        self.EventType = ua.NodeId(ua.ObjectIds.RefreshRequiredEventType)

class AuditConditionEvent(AuditUpdateMethodEvent):
    """
    AuditConditionEvent: 
    """
    def __init__(self, sourcenode=None, message=None, severity=1):
        super(AuditConditionEvent, self).__init__(sourcenode, message, severity)
        self.EventType = ua.NodeId(ua.ObjectIds.AuditConditionEventType)

class AuditConditionEnableEvent(AuditConditionEvent):
    """
    AuditConditionEnableEvent: 
    """
    def __init__(self, sourcenode=None, message=None, severity=1):
        super(AuditConditionEnableEvent, self).__init__(sourcenode, message, severity)
        self.EventType = ua.NodeId(ua.ObjectIds.AuditConditionEnableEventType)

class AuditConditionCommentEvent(AuditConditionEvent):
    """
    AuditConditionCommentEvent: 
    """
    def __init__(self, sourcenode=None, message=None, severity=1):
        super(AuditConditionCommentEvent, self).__init__(sourcenode, message, severity)
        self.EventType = ua.NodeId(ua.ObjectIds.AuditConditionCommentEventType)
        self.add_property('EventId', None, ua.VariantType.ByteString)
        self.add_property('Comment', None, ua.VariantType.LocalizedText)

class AuditHistoryEventUpdateEvent(AuditHistoryUpdateEvent):
    """
    AuditHistoryEventUpdateEvent: 
    """
    def __init__(self, sourcenode=None, message=None, severity=1):
        super(AuditHistoryEventUpdateEvent, self).__init__(sourcenode, message, severity)
        self.EventType = ua.NodeId(ua.ObjectIds.AuditHistoryEventUpdateEventType)
        self.add_property('UpdatedNode', ua.NodeId(ua.ObjectIds.AuditHistoryEventUpdateEventType), ua.VariantType.NodeId)
        self.add_property('PerformInsertReplace', None, ua.NodeId(ua.ObjectIds.PerformUpdateType))
        self.add_property('Filter', None, ua.NodeId(ua.ObjectIds.EventFilter))
        self.add_property('NewValues', None, ua.NodeId(ua.ObjectIds.HistoryEventFieldList))
        self.add_property('OldValues', None, ua.NodeId(ua.ObjectIds.HistoryEventFieldList))

class AuditHistoryValueUpdateEvent(AuditHistoryUpdateEvent):
    """
    AuditHistoryValueUpdateEvent: 
    """
    def __init__(self, sourcenode=None, message=None, severity=1):
        super(AuditHistoryValueUpdateEvent, self).__init__(sourcenode, message, severity)
        self.EventType = ua.NodeId(ua.ObjectIds.AuditHistoryValueUpdateEventType)
        self.add_property('UpdatedNode', ua.NodeId(ua.ObjectIds.AuditHistoryValueUpdateEventType), ua.VariantType.NodeId)
        self.add_property('PerformInsertReplace', None, ua.NodeId(ua.ObjectIds.PerformUpdateType))
        self.add_property('NewValues', None, ua.NodeId(ua.ObjectIds.DataValue))
        self.add_property('OldValues', None, ua.NodeId(ua.ObjectIds.DataValue))

class AuditHistoryDeleteEvent(AuditHistoryUpdateEvent):
    """
    AuditHistoryDeleteEvent: 
    """
    def __init__(self, sourcenode=None, message=None, severity=1):
        super(AuditHistoryDeleteEvent, self).__init__(sourcenode, message, severity)
        self.EventType = ua.NodeId(ua.ObjectIds.AuditHistoryDeleteEventType)
        self.add_property('UpdatedNode', ua.NodeId(ua.ObjectIds.AuditHistoryDeleteEventType), ua.VariantType.NodeId)

class AuditHistoryRawModifyDeleteEvent(AuditHistoryDeleteEvent):
    """
    AuditHistoryRawModifyDeleteEvent: 
    """
    def __init__(self, sourcenode=None, message=None, severity=1):
        super(AuditHistoryRawModifyDeleteEvent, self).__init__(sourcenode, message, severity)
        self.EventType = ua.NodeId(ua.ObjectIds.AuditHistoryRawModifyDeleteEventType)
        self.add_property('IsDeleteModified', None, ua.VariantType.Boolean)
        self.add_property('StartTime', None, ua.VariantType.DateTime)
        self.add_property('EndTime', None, ua.VariantType.DateTime)
        self.add_property('OldValues', None, ua.NodeId(ua.ObjectIds.DataValue))

class AuditHistoryAtTimeDeleteEvent(AuditHistoryDeleteEvent):
    """
    AuditHistoryAtTimeDeleteEvent: 
    """
    def __init__(self, sourcenode=None, message=None, severity=1):
        super(AuditHistoryAtTimeDeleteEvent, self).__init__(sourcenode, message, severity)
        self.EventType = ua.NodeId(ua.ObjectIds.AuditHistoryAtTimeDeleteEventType)
        self.add_property('ReqTimes', None, ua.NodeId(ua.ObjectIds.UtcTime))
        self.add_property('OldValues', None, ua.NodeId(ua.ObjectIds.DataValue))

class AuditHistoryEventDeleteEvent(AuditHistoryDeleteEvent):
    """
    AuditHistoryEventDeleteEvent: 
    """
    def __init__(self, sourcenode=None, message=None, severity=1):
        super(AuditHistoryEventDeleteEvent, self).__init__(sourcenode, message, severity)
        self.EventType = ua.NodeId(ua.ObjectIds.AuditHistoryEventDeleteEventType)
        self.add_property('EventIds', None, ua.VariantType.ByteString)
        self.add_property('OldValues', None, ua.NodeId(ua.ObjectIds.HistoryEventFieldList))

class EventQueueOverflowEvent(BaseEvent):
    """
    EventQueueOverflowEvent: 
    """
    def __init__(self, sourcenode=None, message=None, severity=1):
        super(EventQueueOverflowEvent, self).__init__(sourcenode, message, severity)
        self.EventType = ua.NodeId(ua.ObjectIds.EventQueueOverflowEventType)

class ProgramTransitionAuditEvent(AuditUpdateStateEvent):
    """
    ProgramTransitionAuditEvent: 
    """
    def __init__(self, sourcenode=None, message=None, severity=1):
        super(ProgramTransitionAuditEvent, self).__init__(sourcenode, message, severity)
        self.EventType = ua.NodeId(ua.ObjectIds.ProgramTransitionAuditEventType)

class AuditConditionRespondEvent(AuditConditionEvent):
    """
    AuditConditionRespondEvent: 
    """
    def __init__(self, sourcenode=None, message=None, severity=1):
        super(AuditConditionRespondEvent, self).__init__(sourcenode, message, severity)
        self.EventType = ua.NodeId(ua.ObjectIds.AuditConditionRespondEventType)
        self.add_property('SelectedResponse', None, ua.VariantType.Int32)

class AuditConditionAcknowledgeEvent(AuditConditionEvent):
    """
    AuditConditionAcknowledgeEvent: 
    """
    def __init__(self, sourcenode=None, message=None, severity=1):
        super(AuditConditionAcknowledgeEvent, self).__init__(sourcenode, message, severity)
        self.EventType = ua.NodeId(ua.ObjectIds.AuditConditionAcknowledgeEventType)
        self.add_property('EventId', None, ua.VariantType.ByteString)
        self.add_property('Comment', None, ua.VariantType.LocalizedText)

class AuditConditionConfirmEvent(AuditConditionEvent):
    """
    AuditConditionConfirmEvent: 
    """
    def __init__(self, sourcenode=None, message=None, severity=1):
        super(AuditConditionConfirmEvent, self).__init__(sourcenode, message, severity)
        self.EventType = ua.NodeId(ua.ObjectIds.AuditConditionConfirmEventType)
        self.add_property('EventId', None, ua.VariantType.ByteString)
        self.add_property('Comment', None, ua.VariantType.LocalizedText)

class AuditConditionShelvingEvent(AuditConditionEvent):
    """
    AuditConditionShelvingEvent: 
    """
    def __init__(self, sourcenode=None, message=None, severity=1):
        super(AuditConditionShelvingEvent, self).__init__(sourcenode, message, severity)
        self.EventType = ua.NodeId(ua.ObjectIds.AuditConditionShelvingEventType)
        self.add_property('ShelvingTime', None, ua.VariantType.DateTime)

class ProgressEvent(BaseEvent):
    """
    ProgressEvent: 
    """
    def __init__(self, sourcenode=None, message=None, severity=1):
        super(ProgressEvent, self).__init__(sourcenode, message, severity)
        self.EventType = ua.NodeId(ua.ObjectIds.ProgressEventType)
        self.add_property('Context', None, ua.VariantType.Variant)
        self.add_property('Progress', None, ua.VariantType.UInt16)

class SystemStatusChangeEvent(SystemEvent):
    """
    SystemStatusChangeEvent: 
    """
    def __init__(self, sourcenode=None, message=None, severity=1):
        super(SystemStatusChangeEvent, self).__init__(sourcenode, message, severity)
        self.EventType = ua.NodeId(ua.ObjectIds.SystemStatusChangeEventType)
        self.add_property('SystemState', None, ua.NodeId(ua.ObjectIds.ServerState))

class AuditProgramTransitionEvent(AuditUpdateStateEvent):
    """
    AuditProgramTransitionEvent: 
    """
    def __init__(self, sourcenode=None, message=None, severity=1):
        super(AuditProgramTransitionEvent, self).__init__(sourcenode, message, severity)
        self.EventType = ua.NodeId(ua.ObjectIds.AuditProgramTransitionEventType)
        self.add_property('TransitionNumber', None, ua.VariantType.UInt32)

class TrustListUpdatedAuditEvent(AuditUpdateMethodEvent):
    """
    TrustListUpdatedAuditEvent: 
    """
    def __init__(self, sourcenode=None, message=None, severity=1):
        super(TrustListUpdatedAuditEvent, self).__init__(sourcenode, message, severity)
        self.EventType = ua.NodeId(ua.ObjectIds.TrustListUpdatedAuditEventType)

class CertificateUpdatedAuditEvent(AuditUpdateMethodEvent):
    """
    CertificateUpdatedAuditEvent: 
    """
    def __init__(self, sourcenode=None, message=None, severity=1):
        super(CertificateUpdatedAuditEvent, self).__init__(sourcenode, message, severity)
        self.EventType = ua.NodeId(ua.ObjectIds.CertificateUpdatedAuditEventType)
        self.add_property('CertificateGroup', ua.NodeId(ua.ObjectIds.CertificateUpdatedAuditEventType), ua.VariantType.NodeId)
        self.add_property('CertificateType', ua.NodeId(ua.ObjectIds.CertificateUpdatedAuditEventType), ua.VariantType.NodeId)


IMPLEMENTED_EVENTS = {
    ua.ObjectIds.BaseEventType: BaseEvent,
    ua.ObjectIds.AuditEventType: AuditEvent,
    ua.ObjectIds.AuditSecurityEventType: AuditSecurityEvent,
    ua.ObjectIds.AuditChannelEventType: AuditChannelEvent,
    ua.ObjectIds.AuditOpenSecureChannelEventType: AuditOpenSecureChannelEvent,
    ua.ObjectIds.AuditSessionEventType: AuditSessionEvent,
    ua.ObjectIds.AuditCreateSessionEventType: AuditCreateSessionEvent,
    ua.ObjectIds.AuditActivateSessionEventType: AuditActivateSessionEvent,
    ua.ObjectIds.AuditCancelEventType: AuditCancelEvent,
    ua.ObjectIds.AuditCertificateEventType: AuditCertificateEvent,
    ua.ObjectIds.AuditCertificateDataMismatchEventType: AuditCertificateDataMismatchEvent,
    ua.ObjectIds.AuditCertificateExpiredEventType: AuditCertificateExpiredEvent,
    ua.ObjectIds.AuditCertificateInvalidEventType: AuditCertificateInvalidEvent,
    ua.ObjectIds.AuditCertificateUntrustedEventType: AuditCertificateUntrustedEvent,
    ua.ObjectIds.AuditCertificateRevokedEventType: AuditCertificateRevokedEvent,
    ua.ObjectIds.AuditCertificateMismatchEventType: AuditCertificateMismatchEvent,
    ua.ObjectIds.AuditNodeManagementEventType: AuditNodeManagementEvent,
    ua.ObjectIds.AuditAddNodesEventType: AuditAddNodesEvent,
    ua.ObjectIds.AuditDeleteNodesEventType: AuditDeleteNodesEvent,
    ua.ObjectIds.AuditAddReferencesEventType: AuditAddReferencesEvent,
    ua.ObjectIds.AuditDeleteReferencesEventType: AuditDeleteReferencesEvent,
    ua.ObjectIds.AuditUpdateEventType: AuditUpdateEvent,
    ua.ObjectIds.AuditWriteUpdateEventType: AuditWriteUpdateEvent,
    ua.ObjectIds.AuditHistoryUpdateEventType: AuditHistoryUpdateEvent,
    ua.ObjectIds.AuditUpdateMethodEventType: AuditUpdateMethodEvent,
    ua.ObjectIds.SystemEventType: SystemEvent,
    ua.ObjectIds.DeviceFailureEventType: DeviceFailureEvent,
    ua.ObjectIds.BaseModelChangeEventType: BaseModelChangeEvent,
    ua.ObjectIds.GeneralModelChangeEventType: GeneralModelChangeEvent,
    ua.ObjectIds.TransitionEventType: TransitionEvent,
    ua.ObjectIds.AuditUpdateStateEventType: AuditUpdateStateEvent,
    ua.ObjectIds.ProgramTransitionEventType: ProgramTransitionEvent,
    ua.ObjectIds.SemanticChangeEventType: SemanticChangeEvent,
    ua.ObjectIds.AuditUrlMismatchEventType: AuditUrlMismatchEvent,
    ua.ObjectIds.RefreshStartEventType: RefreshStartEvent,
    ua.ObjectIds.RefreshEndEventType: RefreshEndEvent,
    ua.ObjectIds.RefreshRequiredEventType: RefreshRequiredEvent,
    ua.ObjectIds.AuditConditionEventType: AuditConditionEvent,
    ua.ObjectIds.AuditConditionEnableEventType: AuditConditionEnableEvent,
    ua.ObjectIds.AuditConditionCommentEventType: AuditConditionCommentEvent,
    ua.ObjectIds.AuditHistoryEventUpdateEventType: AuditHistoryEventUpdateEvent,
    ua.ObjectIds.AuditHistoryValueUpdateEventType: AuditHistoryValueUpdateEvent,
    ua.ObjectIds.AuditHistoryDeleteEventType: AuditHistoryDeleteEvent,
    ua.ObjectIds.AuditHistoryRawModifyDeleteEventType: AuditHistoryRawModifyDeleteEvent,
    ua.ObjectIds.AuditHistoryAtTimeDeleteEventType: AuditHistoryAtTimeDeleteEvent,
    ua.ObjectIds.AuditHistoryEventDeleteEventType: AuditHistoryEventDeleteEvent,
    ua.ObjectIds.EventQueueOverflowEventType: EventQueueOverflowEvent,
    ua.ObjectIds.ProgramTransitionAuditEventType: ProgramTransitionAuditEvent,
    ua.ObjectIds.AuditConditionRespondEventType: AuditConditionRespondEvent,
    ua.ObjectIds.AuditConditionAcknowledgeEventType: AuditConditionAcknowledgeEvent,
    ua.ObjectIds.AuditConditionConfirmEventType: AuditConditionConfirmEvent,
    ua.ObjectIds.AuditConditionShelvingEventType: AuditConditionShelvingEvent,
    ua.ObjectIds.ProgressEventType: ProgressEvent,
    ua.ObjectIds.SystemStatusChangeEventType: SystemStatusChangeEvent,
    ua.ObjectIds.AuditProgramTransitionEventType: AuditProgramTransitionEvent,
    ua.ObjectIds.TrustListUpdatedAuditEventType: TrustListUpdatedAuditEvent,
    ua.ObjectIds.CertificateUpdatedAuditEventType: CertificateUpdatedAuditEvent,
    }
