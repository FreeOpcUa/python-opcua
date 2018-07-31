'''
Autogenerate code from xml spec
'''

from datetime import datetime
from enum import IntEnum

from opcua.ua.uatypes import *
from opcua.ua.object_ids import ObjectIds


class NamingRuleType(IntEnum):
    '''
    :ivar Mandatory:
    :vartype Mandatory: 1
    :ivar Optional:
    :vartype Optional: 2
    :ivar Constraint:
    :vartype Constraint: 3
    '''
    Mandatory = 1
    Optional = 2
    Constraint = 3


class OpenFileMode(IntEnum):
    '''
    :ivar Read:
    :vartype Read: 1
    :ivar Write:
    :vartype Write: 2
    :ivar EraseExisting:
    :vartype EraseExisting: 4
    :ivar Append:
    :vartype Append: 8
    '''
    Read = 1
    Write = 2
    EraseExisting = 4
    Append = 8


class IdentityCriteriaType(IntEnum):
    '''
    :ivar UserName:
    :vartype UserName: 1
    :ivar Thumbprint:
    :vartype Thumbprint: 2
    :ivar Role:
    :vartype Role: 3
    :ivar GroupId:
    :vartype GroupId: 4
    :ivar Anonymous:
    :vartype Anonymous: 5
    :ivar AuthenticatedUser:
    :vartype AuthenticatedUser: 6
    '''
    UserName = 1
    Thumbprint = 2
    Role = 3
    GroupId = 4
    Anonymous = 5
    AuthenticatedUser = 6


class TrustListMasks(IntEnum):
    '''
    :ivar None_:
    :vartype None_: 0
    :ivar TrustedCertificates:
    :vartype TrustedCertificates: 1
    :ivar TrustedCrls:
    :vartype TrustedCrls: 2
    :ivar IssuerCertificates:
    :vartype IssuerCertificates: 4
    :ivar IssuerCrls:
    :vartype IssuerCrls: 8
    :ivar All:
    :vartype All: 15
    '''
    None_ = 0
    TrustedCertificates = 1
    TrustedCrls = 2
    IssuerCertificates = 4
    IssuerCrls = 8
    All = 15


class PubSubState(IntEnum):
    '''
    :ivar Disabled:
    :vartype Disabled: 0
    :ivar Paused:
    :vartype Paused: 1
    :ivar Operational:
    :vartype Operational: 2
    :ivar Error:
    :vartype Error: 3
    '''
    Disabled = 0
    Paused = 1
    Operational = 2
    Error = 3


class DataSetFieldFlags(IntEnum):
    '''
    :ivar PromotedField:
    :vartype PromotedField: 1
    '''
    PromotedField = 1


class DataSetFieldContentMask(IntEnum):
    '''
    :ivar StatusCode:
    :vartype StatusCode: 1
    :ivar SourceTimestamp:
    :vartype SourceTimestamp: 2
    :ivar ServerTimestamp:
    :vartype ServerTimestamp: 4
    :ivar SourcePicoSeconds:
    :vartype SourcePicoSeconds: 8
    :ivar ServerPicoSeconds:
    :vartype ServerPicoSeconds: 16
    :ivar RawDataEncoding:
    :vartype RawDataEncoding: 32
    '''
    StatusCode = 1
    SourceTimestamp = 2
    ServerTimestamp = 4
    SourcePicoSeconds = 8
    ServerPicoSeconds = 16
    RawDataEncoding = 32


class OverrideValueHandling(IntEnum):
    '''
    :ivar Disabled:
    :vartype Disabled: 0
    :ivar LastUseableValue:
    :vartype LastUseableValue: 1
    :ivar OverrideValue:
    :vartype OverrideValue: 2
    '''
    Disabled = 0
    LastUseableValue = 1
    OverrideValue = 2


class DataSetOrderingType(IntEnum):
    '''
    :ivar Undefined:
    :vartype Undefined: 0
    :ivar AscendingWriterId:
    :vartype AscendingWriterId: 1
    :ivar AscendingWriterIdSingle:
    :vartype AscendingWriterIdSingle: 2
    '''
    Undefined = 0
    AscendingWriterId = 1
    AscendingWriterIdSingle = 2


class UadpNetworkMessageContentMask(IntEnum):
    '''
    :ivar PublisherId:
    :vartype PublisherId: 1
    :ivar GroupHeader:
    :vartype GroupHeader: 2
    :ivar WriterGroupId:
    :vartype WriterGroupId: 4
    :ivar GroupVersion:
    :vartype GroupVersion: 8
    :ivar NetworkMessageNumber:
    :vartype NetworkMessageNumber: 16
    :ivar SequenceNumber:
    :vartype SequenceNumber: 32
    :ivar PayloadHeader:
    :vartype PayloadHeader: 64
    :ivar Timestamp:
    :vartype Timestamp: 128
    :ivar Picoseconds:
    :vartype Picoseconds: 256
    :ivar DataSetClassId:
    :vartype DataSetClassId: 512
    :ivar PromotedFields:
    :vartype PromotedFields: 1024
    '''
    PublisherId = 1
    GroupHeader = 2
    WriterGroupId = 4
    GroupVersion = 8
    NetworkMessageNumber = 16
    SequenceNumber = 32
    PayloadHeader = 64
    Timestamp = 128
    Picoseconds = 256
    DataSetClassId = 512
    PromotedFields = 1024


class UadpDataSetMessageContentMask(IntEnum):
    '''
    :ivar Timestamp:
    :vartype Timestamp: 1
    :ivar PicoSeconds:
    :vartype PicoSeconds: 2
    :ivar Status:
    :vartype Status: 4
    :ivar MajorVersion:
    :vartype MajorVersion: 8
    :ivar MinorVersion:
    :vartype MinorVersion: 16
    :ivar SequenceNumber:
    :vartype SequenceNumber: 32
    '''
    Timestamp = 1
    PicoSeconds = 2
    Status = 4
    MajorVersion = 8
    MinorVersion = 16
    SequenceNumber = 32


class JsonNetworkMessageContentMask(IntEnum):
    '''
    :ivar NetworkMessageHeader:
    :vartype NetworkMessageHeader: 1
    :ivar DataSetMessageHeader:
    :vartype DataSetMessageHeader: 2
    :ivar SingleDataSetMessage:
    :vartype SingleDataSetMessage: 4
    :ivar PublisherId:
    :vartype PublisherId: 8
    :ivar DataSetClassId:
    :vartype DataSetClassId: 16
    :ivar ReplyTo:
    :vartype ReplyTo: 32
    '''
    NetworkMessageHeader = 1
    DataSetMessageHeader = 2
    SingleDataSetMessage = 4
    PublisherId = 8
    DataSetClassId = 16
    ReplyTo = 32


class JsonDataSetMessageContentMask(IntEnum):
    '''
    :ivar DataSetWriterId:
    :vartype DataSetWriterId: 1
    :ivar MetaDataVersion:
    :vartype MetaDataVersion: 2
    :ivar SequenceNumber:
    :vartype SequenceNumber: 4
    :ivar Timestamp:
    :vartype Timestamp: 8
    :ivar Status:
    :vartype Status: 16
    '''
    DataSetWriterId = 1
    MetaDataVersion = 2
    SequenceNumber = 4
    Timestamp = 8
    Status = 16


class BrokerTransportQualityOfService(IntEnum):
    '''
    :ivar NotSpecified:
    :vartype NotSpecified: 0
    :ivar BestEffort:
    :vartype BestEffort: 1
    :ivar AtLeastOnce:
    :vartype AtLeastOnce: 2
    :ivar AtMostOnce:
    :vartype AtMostOnce: 3
    :ivar ExactlyOnce:
    :vartype ExactlyOnce: 4
    '''
    NotSpecified = 0
    BestEffort = 1
    AtLeastOnce = 2
    AtMostOnce = 3
    ExactlyOnce = 4


class DiagnosticsLevel(IntEnum):
    '''
    :ivar Basic:
    :vartype Basic: 0
    :ivar Advanced:
    :vartype Advanced: 1
    :ivar Info:
    :vartype Info: 2
    :ivar Log:
    :vartype Log: 3
    :ivar Debug:
    :vartype Debug: 4
    '''
    Basic = 0
    Advanced = 1
    Info = 2
    Log = 3
    Debug = 4


class PubSubDiagnosticsCounterClassification(IntEnum):
    '''
    :ivar Information:
    :vartype Information: 0
    :ivar Error:
    :vartype Error: 1
    '''
    Information = 0
    Error = 1


class IdType(IntEnum):
    '''
    The type of identifier used in a node id.

    :ivar Numeric:
    :vartype Numeric: 0
    :ivar String:
    :vartype String: 1
    :ivar Guid:
    :vartype Guid: 2
    :ivar Opaque:
    :vartype Opaque: 3
    '''
    Numeric = 0
    String = 1
    Guid = 2
    Opaque = 3


class NodeClass(IntEnum):
    '''
    A mask specifying the class of the node.

    :ivar Unspecified:
    :vartype Unspecified: 0
    :ivar Object:
    :vartype Object: 1
    :ivar Variable:
    :vartype Variable: 2
    :ivar Method:
    :vartype Method: 4
    :ivar ObjectType:
    :vartype ObjectType: 8
    :ivar VariableType:
    :vartype VariableType: 16
    :ivar ReferenceType:
    :vartype ReferenceType: 32
    :ivar DataType:
    :vartype DataType: 64
    :ivar View:
    :vartype View: 128
    '''
    Unspecified = 0
    Object = 1
    Variable = 2
    Method = 4
    ObjectType = 8
    VariableType = 16
    ReferenceType = 32
    DataType = 64
    View = 128


class AccessLevelType(IntEnum):
    '''
    :ivar None_:
    :vartype None_: 0
    :ivar CurrentRead:
    :vartype CurrentRead: 1
    :ivar CurrentWrite:
    :vartype CurrentWrite: 2
    :ivar HistoryRead:
    :vartype HistoryRead: 4
    :ivar HistoryWrite:
    :vartype HistoryWrite: 16
    :ivar StatusWrite:
    :vartype StatusWrite: 32
    :ivar TimestampWrite:
    :vartype TimestampWrite: 64
    '''
    None_ = 0
    CurrentRead = 1
    CurrentWrite = 2
    HistoryRead = 4
    HistoryWrite = 16
    StatusWrite = 32
    TimestampWrite = 64


class AccessLevelExType(IntEnum):
    '''
    :ivar None_:
    :vartype None_: 0
    :ivar CurrentRead:
    :vartype CurrentRead: 1
    :ivar CurrentWrite:
    :vartype CurrentWrite: 2
    :ivar HistoryRead:
    :vartype HistoryRead: 4
    :ivar HistoryWrite:
    :vartype HistoryWrite: 16
    :ivar StatusWrite:
    :vartype StatusWrite: 32
    :ivar TimestampWrite:
    :vartype TimestampWrite: 64
    :ivar NonatomicRead:
    :vartype NonatomicRead: 65536
    :ivar NonatomicWrite:
    :vartype NonatomicWrite: 131072
    :ivar WriteFullArrayOnly:
    :vartype WriteFullArrayOnly: 262144
    '''
    None_ = 0
    CurrentRead = 1
    CurrentWrite = 2
    HistoryRead = 4
    HistoryWrite = 16
    StatusWrite = 32
    TimestampWrite = 64
    NonatomicRead = 65536
    NonatomicWrite = 131072
    WriteFullArrayOnly = 262144


class EventNotifierType(IntEnum):
    '''
    :ivar None_:
    :vartype None_: 0
    :ivar SubscribeToEvents:
    :vartype SubscribeToEvents: 1
    :ivar HistoryRead:
    :vartype HistoryRead: 4
    :ivar HistoryWrite:
    :vartype HistoryWrite: 8
    '''
    None_ = 0
    SubscribeToEvents = 1
    HistoryRead = 4
    HistoryWrite = 8


class StructureType(IntEnum):
    '''
    :ivar Structure:
    :vartype Structure: 0
    :ivar StructureWithOptionalFields:
    :vartype StructureWithOptionalFields: 1
    :ivar Union:
    :vartype Union: 2
    '''
    Structure = 0
    StructureWithOptionalFields = 1
    Union = 2


class ApplicationType(IntEnum):
    '''
    The types of applications.

    :ivar Server:
    :vartype Server: 0
    :ivar Client:
    :vartype Client: 1
    :ivar ClientAndServer:
    :vartype ClientAndServer: 2
    :ivar DiscoveryServer:
    :vartype DiscoveryServer: 3
    '''
    Server = 0
    Client = 1
    ClientAndServer = 2
    DiscoveryServer = 3


class MessageSecurityMode(IntEnum):
    '''
    The type of security to use on a message.

    :ivar Invalid:
    :vartype Invalid: 0
    :ivar None_:
    :vartype None_: 1
    :ivar Sign:
    :vartype Sign: 2
    :ivar SignAndEncrypt:
    :vartype SignAndEncrypt: 3
    '''
    Invalid = 0
    None_ = 1
    Sign = 2
    SignAndEncrypt = 3


class UserTokenType(IntEnum):
    '''
    The possible user token types.

    :ivar Anonymous:
    :vartype Anonymous: 0
    :ivar UserName:
    :vartype UserName: 1
    :ivar Certificate:
    :vartype Certificate: 2
    :ivar IssuedToken:
    :vartype IssuedToken: 3
    '''
    Anonymous = 0
    UserName = 1
    Certificate = 2
    IssuedToken = 3


class SecurityTokenRequestType(IntEnum):
    '''
    Indicates whether a token if being created or renewed.

    :ivar Issue:
    :vartype Issue: 0
    :ivar Renew:
    :vartype Renew: 1
    '''
    Issue = 0
    Renew = 1


class NodeAttributesMask(IntEnum):
    '''
    The bits used to specify default attributes for a new node.

    :ivar None_:
    :vartype None_: 0
    :ivar AccessLevel:
    :vartype AccessLevel: 1
    :ivar ArrayDimensions:
    :vartype ArrayDimensions: 2
    :ivar BrowseName:
    :vartype BrowseName: 4
    :ivar ContainsNoLoops:
    :vartype ContainsNoLoops: 8
    :ivar DataType:
    :vartype DataType: 16
    :ivar Description:
    :vartype Description: 32
    :ivar DisplayName:
    :vartype DisplayName: 64
    :ivar EventNotifier:
    :vartype EventNotifier: 128
    :ivar Executable:
    :vartype Executable: 256
    :ivar Historizing:
    :vartype Historizing: 512
    :ivar InverseName:
    :vartype InverseName: 1024
    :ivar IsAbstract:
    :vartype IsAbstract: 2048
    :ivar MinimumSamplingInterval:
    :vartype MinimumSamplingInterval: 4096
    :ivar NodeClass:
    :vartype NodeClass: 8192
    :ivar NodeId:
    :vartype NodeId: 16384
    :ivar Symmetric:
    :vartype Symmetric: 32768
    :ivar UserAccessLevel:
    :vartype UserAccessLevel: 65536
    :ivar UserExecutable:
    :vartype UserExecutable: 131072
    :ivar UserWriteMask:
    :vartype UserWriteMask: 262144
    :ivar ValueRank:
    :vartype ValueRank: 524288
    :ivar WriteMask:
    :vartype WriteMask: 1048576
    :ivar Value:
    :vartype Value: 2097152
    :ivar DataTypeDefinition:
    :vartype DataTypeDefinition: 4194304
    :ivar RolePermissions:
    :vartype RolePermissions: 8388608
    :ivar AccessRestrictions:
    :vartype AccessRestrictions: 16777216
    :ivar All:
    :vartype All: 33554431
    :ivar BaseNode:
    :vartype BaseNode: 26501220
    :ivar Object:
    :vartype Object: 26501348
    :ivar ObjectType:
    :vartype ObjectType: 26503268
    :ivar Variable:
    :vartype Variable: 26571383
    :ivar VariableType:
    :vartype VariableType: 28600438
    :ivar Method:
    :vartype Method: 26632548
    :ivar ReferenceType:
    :vartype ReferenceType: 26537060
    :ivar View:
    :vartype View: 26501356
    '''
    None_ = 0
    AccessLevel = 1
    ArrayDimensions = 2
    BrowseName = 4
    ContainsNoLoops = 8
    DataType = 16
    Description = 32
    DisplayName = 64
    EventNotifier = 128
    Executable = 256
    Historizing = 512
    InverseName = 1024
    IsAbstract = 2048
    MinimumSamplingInterval = 4096
    NodeClass = 8192
    NodeId = 16384
    Symmetric = 32768
    UserAccessLevel = 65536
    UserExecutable = 131072
    UserWriteMask = 262144
    ValueRank = 524288
    WriteMask = 1048576
    Value = 2097152
    DataTypeDefinition = 4194304
    RolePermissions = 8388608
    AccessRestrictions = 16777216
    All = 33554431
    BaseNode = 26501220
    Object = 26501348
    ObjectType = 26503268
    Variable = 26571383
    VariableType = 28600438
    Method = 26632548
    ReferenceType = 26537060
    View = 26501356


class AttributeWriteMask(IntEnum):
    '''
    Define bits used to indicate which attributes are writable.

    :ivar None_:
    :vartype None_: 0
    :ivar AccessLevel:
    :vartype AccessLevel: 1
    :ivar ArrayDimensions:
    :vartype ArrayDimensions: 2
    :ivar BrowseName:
    :vartype BrowseName: 4
    :ivar ContainsNoLoops:
    :vartype ContainsNoLoops: 8
    :ivar DataType:
    :vartype DataType: 16
    :ivar Description:
    :vartype Description: 32
    :ivar DisplayName:
    :vartype DisplayName: 64
    :ivar EventNotifier:
    :vartype EventNotifier: 128
    :ivar Executable:
    :vartype Executable: 256
    :ivar Historizing:
    :vartype Historizing: 512
    :ivar InverseName:
    :vartype InverseName: 1024
    :ivar IsAbstract:
    :vartype IsAbstract: 2048
    :ivar MinimumSamplingInterval:
    :vartype MinimumSamplingInterval: 4096
    :ivar NodeClass:
    :vartype NodeClass: 8192
    :ivar NodeId:
    :vartype NodeId: 16384
    :ivar Symmetric:
    :vartype Symmetric: 32768
    :ivar UserAccessLevel:
    :vartype UserAccessLevel: 65536
    :ivar UserExecutable:
    :vartype UserExecutable: 131072
    :ivar UserWriteMask:
    :vartype UserWriteMask: 262144
    :ivar ValueRank:
    :vartype ValueRank: 524288
    :ivar WriteMask:
    :vartype WriteMask: 1048576
    :ivar ValueForVariableType:
    :vartype ValueForVariableType: 2097152
    :ivar DataTypeDefinition:
    :vartype DataTypeDefinition: 4194304
    :ivar RolePermissions:
    :vartype RolePermissions: 8388608
    :ivar AccessRestrictions:
    :vartype AccessRestrictions: 16777216
    :ivar AccessLevelEx:
    :vartype AccessLevelEx: 33554432
    '''
    None_ = 0
    AccessLevel = 1
    ArrayDimensions = 2
    BrowseName = 4
    ContainsNoLoops = 8
    DataType = 16
    Description = 32
    DisplayName = 64
    EventNotifier = 128
    Executable = 256
    Historizing = 512
    InverseName = 1024
    IsAbstract = 2048
    MinimumSamplingInterval = 4096
    NodeClass = 8192
    NodeId = 16384
    Symmetric = 32768
    UserAccessLevel = 65536
    UserExecutable = 131072
    UserWriteMask = 262144
    ValueRank = 524288
    WriteMask = 1048576
    ValueForVariableType = 2097152
    DataTypeDefinition = 4194304
    RolePermissions = 8388608
    AccessRestrictions = 16777216
    AccessLevelEx = 33554432


class BrowseDirection(IntEnum):
    '''
    The directions of the references to return.

    :ivar Forward:
    :vartype Forward: 0
    :ivar Inverse:
    :vartype Inverse: 1
    :ivar Both:
    :vartype Both: 2
    :ivar Invalid:
    :vartype Invalid: 3
    '''
    Forward = 0
    Inverse = 1
    Both = 2
    Invalid = 3


class BrowseResultMask(IntEnum):
    '''
    A bit mask which specifies what should be returned in a browse response.

    :ivar None_:
    :vartype None_: 0
    :ivar ReferenceTypeId:
    :vartype ReferenceTypeId: 1
    :ivar IsForward:
    :vartype IsForward: 2
    :ivar NodeClass:
    :vartype NodeClass: 4
    :ivar BrowseName:
    :vartype BrowseName: 8
    :ivar DisplayName:
    :vartype DisplayName: 16
    :ivar TypeDefinition:
    :vartype TypeDefinition: 32
    :ivar All:
    :vartype All: 63
    :ivar ReferenceTypeInfo:
    :vartype ReferenceTypeInfo: 3
    :ivar TargetInfo:
    :vartype TargetInfo: 60
    '''
    None_ = 0
    ReferenceTypeId = 1
    IsForward = 2
    NodeClass = 4
    BrowseName = 8
    DisplayName = 16
    TypeDefinition = 32
    All = 63
    ReferenceTypeInfo = 3
    TargetInfo = 60


class FilterOperator(IntEnum):
    '''
    :ivar Equals:
    :vartype Equals: 0
    :ivar IsNull:
    :vartype IsNull: 1
    :ivar GreaterThan:
    :vartype GreaterThan: 2
    :ivar LessThan:
    :vartype LessThan: 3
    :ivar GreaterThanOrEqual:
    :vartype GreaterThanOrEqual: 4
    :ivar LessThanOrEqual:
    :vartype LessThanOrEqual: 5
    :ivar Like:
    :vartype Like: 6
    :ivar Not:
    :vartype Not: 7
    :ivar Between:
    :vartype Between: 8
    :ivar InList:
    :vartype InList: 9
    :ivar And:
    :vartype And: 10
    :ivar Or:
    :vartype Or: 11
    :ivar Cast:
    :vartype Cast: 12
    :ivar InView:
    :vartype InView: 13
    :ivar OfType:
    :vartype OfType: 14
    :ivar RelatedTo:
    :vartype RelatedTo: 15
    :ivar BitwiseAnd:
    :vartype BitwiseAnd: 16
    :ivar BitwiseOr:
    :vartype BitwiseOr: 17
    '''
    Equals = 0
    IsNull = 1
    GreaterThan = 2
    LessThan = 3
    GreaterThanOrEqual = 4
    LessThanOrEqual = 5
    Like = 6
    Not = 7
    Between = 8
    InList = 9
    And = 10
    Or = 11
    Cast = 12
    InView = 13
    OfType = 14
    RelatedTo = 15
    BitwiseAnd = 16
    BitwiseOr = 17


class TimestampsToReturn(IntEnum):
    '''
    :ivar Source:
    :vartype Source: 0
    :ivar Server:
    :vartype Server: 1
    :ivar Both:
    :vartype Both: 2
    :ivar Neither:
    :vartype Neither: 3
    :ivar Invalid:
    :vartype Invalid: 4
    '''
    Source = 0
    Server = 1
    Both = 2
    Neither = 3
    Invalid = 4


class HistoryUpdateType(IntEnum):
    '''
    :ivar Insert:
    :vartype Insert: 1
    :ivar Replace:
    :vartype Replace: 2
    :ivar Update:
    :vartype Update: 3
    :ivar Delete:
    :vartype Delete: 4
    '''
    Insert = 1
    Replace = 2
    Update = 3
    Delete = 4


class PerformUpdateType(IntEnum):
    '''
    :ivar Insert:
    :vartype Insert: 1
    :ivar Replace:
    :vartype Replace: 2
    :ivar Update:
    :vartype Update: 3
    :ivar Remove:
    :vartype Remove: 4
    '''
    Insert = 1
    Replace = 2
    Update = 3
    Remove = 4


class MonitoringMode(IntEnum):
    '''
    :ivar Disabled:
    :vartype Disabled: 0
    :ivar Sampling:
    :vartype Sampling: 1
    :ivar Reporting:
    :vartype Reporting: 2
    '''
    Disabled = 0
    Sampling = 1
    Reporting = 2


class DataChangeTrigger(IntEnum):
    '''
    :ivar Status:
    :vartype Status: 0
    :ivar StatusValue:
    :vartype StatusValue: 1
    :ivar StatusValueTimestamp:
    :vartype StatusValueTimestamp: 2
    '''
    Status = 0
    StatusValue = 1
    StatusValueTimestamp = 2


class DeadbandType(IntEnum):
    '''
    :ivar None_:
    :vartype None_: 0
    :ivar Absolute:
    :vartype Absolute: 1
    :ivar Percent:
    :vartype Percent: 2
    '''
    None_ = 0
    Absolute = 1
    Percent = 2


class RedundancySupport(IntEnum):
    '''
    :ivar None_:
    :vartype None_: 0
    :ivar Cold:
    :vartype Cold: 1
    :ivar Warm:
    :vartype Warm: 2
    :ivar Hot:
    :vartype Hot: 3
    :ivar Transparent:
    :vartype Transparent: 4
    :ivar HotAndMirrored:
    :vartype HotAndMirrored: 5
    '''
    None_ = 0
    Cold = 1
    Warm = 2
    Hot = 3
    Transparent = 4
    HotAndMirrored = 5


class ServerState(IntEnum):
    '''
    :ivar Running:
    :vartype Running: 0
    :ivar Failed:
    :vartype Failed: 1
    :ivar NoConfiguration:
    :vartype NoConfiguration: 2
    :ivar Suspended:
    :vartype Suspended: 3
    :ivar Shutdown:
    :vartype Shutdown: 4
    :ivar Test:
    :vartype Test: 5
    :ivar CommunicationFault:
    :vartype CommunicationFault: 6
    :ivar Unknown:
    :vartype Unknown: 7
    '''
    Running = 0
    Failed = 1
    NoConfiguration = 2
    Suspended = 3
    Shutdown = 4
    Test = 5
    CommunicationFault = 6
    Unknown = 7


class ModelChangeStructureVerbMask(IntEnum):
    '''
    :ivar NodeAdded:
    :vartype NodeAdded: 1
    :ivar NodeDeleted:
    :vartype NodeDeleted: 2
    :ivar ReferenceAdded:
    :vartype ReferenceAdded: 4
    :ivar ReferenceDeleted:
    :vartype ReferenceDeleted: 8
    :ivar DataTypeChanged:
    :vartype DataTypeChanged: 16
    '''
    NodeAdded = 1
    NodeDeleted = 2
    ReferenceAdded = 4
    ReferenceDeleted = 8
    DataTypeChanged = 16


class AxisScaleEnumeration(IntEnum):
    '''
    :ivar Linear:
    :vartype Linear: 0
    :ivar Log:
    :vartype Log: 1
    :ivar Ln:
    :vartype Ln: 2
    '''
    Linear = 0
    Log = 1
    Ln = 2


class ExceptionDeviationFormat(IntEnum):
    '''
    :ivar AbsoluteValue:
    :vartype AbsoluteValue: 0
    :ivar PercentOfValue:
    :vartype PercentOfValue: 1
    :ivar PercentOfRange:
    :vartype PercentOfRange: 2
    :ivar PercentOfEURange:
    :vartype PercentOfEURange: 3
    :ivar Unknown:
    :vartype Unknown: 4
    '''
    AbsoluteValue = 0
    PercentOfValue = 1
    PercentOfRange = 2
    PercentOfEURange = 3
    Unknown = 4


class DataTypeDefinition(FrozenClass):
    '''
    '''

    ua_types = [
               ]

    def __init__(self):
        self._freeze = True

    def __str__(self):
        return 'DataTypeDefinition(' +  + ')'

    __repr__ = __str__


class DiagnosticInfo(FrozenClass):
    '''
    A recursive structure containing diagnostic information associated with a status code.

    :ivar Encoding:
    :vartype Encoding: Byte
    :ivar SymbolicId:
    :vartype SymbolicId: Int32
    :ivar NamespaceURI:
    :vartype NamespaceURI: Int32
    :ivar Locale:
    :vartype Locale: Int32
    :ivar LocalizedText:
    :vartype LocalizedText: Int32
    :ivar AdditionalInfo:
    :vartype AdditionalInfo: String
    :ivar InnerStatusCode:
    :vartype InnerStatusCode: StatusCode
    :ivar InnerDiagnosticInfo:
    :vartype InnerDiagnosticInfo: DiagnosticInfo
    '''

    ua_switches = {
        'SymbolicId': ('Encoding', 0),
        'NamespaceURI': ('Encoding', 1),
        'Locale': ('Encoding', 2),
        'LocalizedText': ('Encoding', 3),
        'AdditionalInfo': ('Encoding', 4),
        'InnerStatusCode': ('Encoding', 5),
        'InnerDiagnosticInfo': ('Encoding', 6),
               }
    ua_types = [
        ('Encoding', 'Byte'),
        ('SymbolicId', 'Int32'),
        ('NamespaceURI', 'Int32'),
        ('Locale', 'Int32'),
        ('LocalizedText', 'Int32'),
        ('AdditionalInfo', 'String'),
        ('InnerStatusCode', 'StatusCode'),
        ('InnerDiagnosticInfo', 'DiagnosticInfo'),
               ]

    def __init__(self):
        self.Encoding = 0
        self.SymbolicId = None
        self.NamespaceURI = None
        self.Locale = None
        self.LocalizedText = None
        self.AdditionalInfo = None
        self.InnerStatusCode = None
        self.InnerDiagnosticInfo = None
        self._freeze = True

    def __str__(self):
        return 'DiagnosticInfo(' + 'Encoding:' + str(self.Encoding) + ', ' + \
               'SymbolicId:' + str(self.SymbolicId) + ', ' + \
               'NamespaceURI:' + str(self.NamespaceURI) + ', ' + \
               'Locale:' + str(self.Locale) + ', ' + \
               'LocalizedText:' + str(self.LocalizedText) + ', ' + \
               'AdditionalInfo:' + str(self.AdditionalInfo) + ', ' + \
               'InnerStatusCode:' + str(self.InnerStatusCode) + ', ' + \
               'InnerDiagnosticInfo:' + str(self.InnerDiagnosticInfo) + ')'

    __repr__ = __str__


class KeyValuePair(FrozenClass):
    '''
    :ivar Key:
    :vartype Key: QualifiedName
    :ivar Value:
    :vartype Value: Variant
    '''

    ua_types = [
        ('Key', 'QualifiedName'),
        ('Value', 'Variant'),
               ]

    def __init__(self):
        self.Key = QualifiedName()
        self.Value = Variant()
        self._freeze = True

    def __str__(self):
        return 'KeyValuePair(' + 'Key:' + str(self.Key) + ', ' + \
               'Value:' + str(self.Value) + ')'

    __repr__ = __str__


class EndpointType(FrozenClass):
    '''
    :ivar EndpointUrl:
    :vartype EndpointUrl: String
    :ivar SecurityMode:
    :vartype SecurityMode: MessageSecurityMode
    :ivar SecurityPolicyUri:
    :vartype SecurityPolicyUri: String
    :ivar TransportProfileUri:
    :vartype TransportProfileUri: String
    '''

    ua_types = [
        ('EndpointUrl', 'String'),
        ('SecurityMode', 'MessageSecurityMode'),
        ('SecurityPolicyUri', 'String'),
        ('TransportProfileUri', 'String'),
               ]

    def __init__(self):
        self.EndpointUrl = None
        self.SecurityMode = MessageSecurityMode(0)
        self.SecurityPolicyUri = None
        self.TransportProfileUri = None
        self._freeze = True

    def __str__(self):
        return 'EndpointType(' + 'EndpointUrl:' + str(self.EndpointUrl) + ', ' + \
               'SecurityMode:' + str(self.SecurityMode) + ', ' + \
               'SecurityPolicyUri:' + str(self.SecurityPolicyUri) + ', ' + \
               'TransportProfileUri:' + str(self.TransportProfileUri) + ')'

    __repr__ = __str__


class IdentityMappingRuleType(FrozenClass):
    '''
    :ivar CriteriaType:
    :vartype CriteriaType: IdentityCriteriaType
    :ivar Criteria:
    :vartype Criteria: String
    '''

    ua_types = [
        ('CriteriaType', 'IdentityCriteriaType'),
        ('Criteria', 'String'),
               ]

    def __init__(self):
        self.CriteriaType = IdentityCriteriaType(0)
        self.Criteria = None
        self._freeze = True

    def __str__(self):
        return 'IdentityMappingRuleType(' + 'CriteriaType:' + str(self.CriteriaType) + ', ' + \
               'Criteria:' + str(self.Criteria) + ')'

    __repr__ = __str__


class TrustListDataType(FrozenClass):
    '''
    :ivar SpecifiedLists:
    :vartype SpecifiedLists: UInt32
    :ivar TrustedCertificates:
    :vartype TrustedCertificates: ByteString
    :ivar TrustedCrls:
    :vartype TrustedCrls: ByteString
    :ivar IssuerCertificates:
    :vartype IssuerCertificates: ByteString
    :ivar IssuerCrls:
    :vartype IssuerCrls: ByteString
    '''

    ua_types = [
        ('SpecifiedLists', 'UInt32'),
        ('TrustedCertificates', 'ListOfByteString'),
        ('TrustedCrls', 'ListOfByteString'),
        ('IssuerCertificates', 'ListOfByteString'),
        ('IssuerCrls', 'ListOfByteString'),
               ]

    def __init__(self):
        self.SpecifiedLists = 0
        self.TrustedCertificates = []
        self.TrustedCrls = []
        self.IssuerCertificates = []
        self.IssuerCrls = []
        self._freeze = True

    def __str__(self):
        return 'TrustListDataType(' + 'SpecifiedLists:' + str(self.SpecifiedLists) + ', ' + \
               'TrustedCertificates:' + str(self.TrustedCertificates) + ', ' + \
               'TrustedCrls:' + str(self.TrustedCrls) + ', ' + \
               'IssuerCertificates:' + str(self.IssuerCertificates) + ', ' + \
               'IssuerCrls:' + str(self.IssuerCrls) + ')'

    __repr__ = __str__


class DecimalDataType(FrozenClass):
    '''
    :ivar Scale:
    :vartype Scale: Int16
    :ivar Value:
    :vartype Value: ByteString
    '''

    ua_types = [
        ('Scale', 'Int16'),
        ('Value', 'ByteString'),
               ]

    def __init__(self):
        self.Scale = 0
        self.Value = None
        self._freeze = True

    def __str__(self):
        return 'DecimalDataType(' + 'Scale:' + str(self.Scale) + ', ' + \
               'Value:' + str(self.Value) + ')'

    __repr__ = __str__


class DataTypeSchemaHeader(FrozenClass):
    '''
    :ivar Namespaces:
    :vartype Namespaces: String
    :ivar StructureDataTypes:
    :vartype StructureDataTypes: StructureDescription
    :ivar EnumDataTypes:
    :vartype EnumDataTypes: EnumDescription
    :ivar SimpleDataTypes:
    :vartype SimpleDataTypes: SimpleTypeDescription
    '''

    ua_types = [
        ('Namespaces', 'ListOfString'),
        ('StructureDataTypes', 'ListOfStructureDescription'),
        ('EnumDataTypes', 'ListOfEnumDescription'),
        ('SimpleDataTypes', 'ListOfSimpleTypeDescription'),
               ]

    def __init__(self):
        self.Namespaces = []
        self.StructureDataTypes = []
        self.EnumDataTypes = []
        self.SimpleDataTypes = []
        self._freeze = True

    def __str__(self):
        return 'DataTypeSchemaHeader(' + 'Namespaces:' + str(self.Namespaces) + ', ' + \
               'StructureDataTypes:' + str(self.StructureDataTypes) + ', ' + \
               'EnumDataTypes:' + str(self.EnumDataTypes) + ', ' + \
               'SimpleDataTypes:' + str(self.SimpleDataTypes) + ')'

    __repr__ = __str__


class DataTypeDescription(FrozenClass):
    '''
    :ivar DataTypeId:
    :vartype DataTypeId: NodeId
    :ivar Name:
    :vartype Name: QualifiedName
    '''

    ua_types = [
        ('DataTypeId', 'NodeId'),
        ('Name', 'QualifiedName'),
               ]

    def __init__(self):
        self.DataTypeId = NodeId()
        self.Name = QualifiedName()
        self._freeze = True

    def __str__(self):
        return 'DataTypeDescription(' + 'DataTypeId:' + str(self.DataTypeId) + ', ' + \
               'Name:' + str(self.Name) + ')'

    __repr__ = __str__


class StructureDescription(FrozenClass):
    '''
    :ivar DataTypeId:
    :vartype DataTypeId: NodeId
    :ivar Name:
    :vartype Name: QualifiedName
    :ivar StructureDefinition:
    :vartype StructureDefinition: StructureDefinition
    '''

    ua_types = [
        ('DataTypeId', 'NodeId'),
        ('Name', 'QualifiedName'),
        ('StructureDefinition', 'StructureDefinition'),
               ]

    def __init__(self):
        self.DataTypeId = NodeId()
        self.Name = QualifiedName()
        self.StructureDefinition = StructureDefinition()
        self._freeze = True

    def __str__(self):
        return 'StructureDescription(' + 'DataTypeId:' + str(self.DataTypeId) + ', ' + \
               'Name:' + str(self.Name) + ', ' + \
               'StructureDefinition:' + str(self.StructureDefinition) + ')'

    __repr__ = __str__


class EnumDescription(FrozenClass):
    '''
    :ivar DataTypeId:
    :vartype DataTypeId: NodeId
    :ivar Name:
    :vartype Name: QualifiedName
    :ivar EnumDefinition:
    :vartype EnumDefinition: EnumDefinition
    :ivar BuiltInType:
    :vartype BuiltInType: Byte
    '''

    ua_types = [
        ('DataTypeId', 'NodeId'),
        ('Name', 'QualifiedName'),
        ('EnumDefinition', 'EnumDefinition'),
        ('BuiltInType', 'Byte'),
               ]

    def __init__(self):
        self.DataTypeId = NodeId()
        self.Name = QualifiedName()
        self.EnumDefinition = EnumDefinition()
        self.BuiltInType = 0
        self._freeze = True

    def __str__(self):
        return 'EnumDescription(' + 'DataTypeId:' + str(self.DataTypeId) + ', ' + \
               'Name:' + str(self.Name) + ', ' + \
               'EnumDefinition:' + str(self.EnumDefinition) + ', ' + \
               'BuiltInType:' + str(self.BuiltInType) + ')'

    __repr__ = __str__


class SimpleTypeDescription(FrozenClass):
    '''
    :ivar DataTypeId:
    :vartype DataTypeId: NodeId
    :ivar Name:
    :vartype Name: QualifiedName
    :ivar BaseDataType:
    :vartype BaseDataType: NodeId
    :ivar BuiltInType:
    :vartype BuiltInType: Byte
    '''

    ua_types = [
        ('DataTypeId', 'NodeId'),
        ('Name', 'QualifiedName'),
        ('BaseDataType', 'NodeId'),
        ('BuiltInType', 'Byte'),
               ]

    def __init__(self):
        self.DataTypeId = NodeId()
        self.Name = QualifiedName()
        self.BaseDataType = NodeId()
        self.BuiltInType = 0
        self._freeze = True

    def __str__(self):
        return 'SimpleTypeDescription(' + 'DataTypeId:' + str(self.DataTypeId) + ', ' + \
               'Name:' + str(self.Name) + ', ' + \
               'BaseDataType:' + str(self.BaseDataType) + ', ' + \
               'BuiltInType:' + str(self.BuiltInType) + ')'

    __repr__ = __str__


class UABinaryFileDataType(FrozenClass):
    '''
    :ivar Namespaces:
    :vartype Namespaces: String
    :ivar StructureDataTypes:
    :vartype StructureDataTypes: StructureDescription
    :ivar EnumDataTypes:
    :vartype EnumDataTypes: EnumDescription
    :ivar SimpleDataTypes:
    :vartype SimpleDataTypes: SimpleTypeDescription
    :ivar SchemaLocation:
    :vartype SchemaLocation: String
    :ivar FileHeader:
    :vartype FileHeader: KeyValuePair
    :ivar Body:
    :vartype Body: Variant
    '''

    ua_types = [
        ('Namespaces', 'ListOfString'),
        ('StructureDataTypes', 'ListOfStructureDescription'),
        ('EnumDataTypes', 'ListOfEnumDescription'),
        ('SimpleDataTypes', 'ListOfSimpleTypeDescription'),
        ('SchemaLocation', 'String'),
        ('FileHeader', 'ListOfKeyValuePair'),
        ('Body', 'Variant'),
               ]

    def __init__(self):
        self.Namespaces = []
        self.StructureDataTypes = []
        self.EnumDataTypes = []
        self.SimpleDataTypes = []
        self.SchemaLocation = None
        self.FileHeader = []
        self.Body = Variant()
        self._freeze = True

    def __str__(self):
        return 'UABinaryFileDataType(' + 'Namespaces:' + str(self.Namespaces) + ', ' + \
               'StructureDataTypes:' + str(self.StructureDataTypes) + ', ' + \
               'EnumDataTypes:' + str(self.EnumDataTypes) + ', ' + \
               'SimpleDataTypes:' + str(self.SimpleDataTypes) + ', ' + \
               'SchemaLocation:' + str(self.SchemaLocation) + ', ' + \
               'FileHeader:' + str(self.FileHeader) + ', ' + \
               'Body:' + str(self.Body) + ')'

    __repr__ = __str__


class DataSetMetaDataType(FrozenClass):
    '''
    :ivar Namespaces:
    :vartype Namespaces: String
    :ivar StructureDataTypes:
    :vartype StructureDataTypes: StructureDescription
    :ivar EnumDataTypes:
    :vartype EnumDataTypes: EnumDescription
    :ivar SimpleDataTypes:
    :vartype SimpleDataTypes: SimpleTypeDescription
    :ivar Name:
    :vartype Name: String
    :ivar Description:
    :vartype Description: LocalizedText
    :ivar Fields:
    :vartype Fields: FieldMetaData
    :ivar DataSetClassId:
    :vartype DataSetClassId: Guid
    :ivar ConfigurationVersion:
    :vartype ConfigurationVersion: ConfigurationVersionDataType
    '''

    ua_types = [
        ('Namespaces', 'ListOfString'),
        ('StructureDataTypes', 'ListOfStructureDescription'),
        ('EnumDataTypes', 'ListOfEnumDescription'),
        ('SimpleDataTypes', 'ListOfSimpleTypeDescription'),
        ('Name', 'String'),
        ('Description', 'LocalizedText'),
        ('Fields', 'ListOfFieldMetaData'),
        ('DataSetClassId', 'Guid'),
        ('ConfigurationVersion', 'ConfigurationVersionDataType'),
               ]

    def __init__(self):
        self.Namespaces = []
        self.StructureDataTypes = []
        self.EnumDataTypes = []
        self.SimpleDataTypes = []
        self.Name = None
        self.Description = LocalizedText()
        self.Fields = []
        self.DataSetClassId = Guid()
        self.ConfigurationVersion = ConfigurationVersionDataType()
        self._freeze = True

    def __str__(self):
        return 'DataSetMetaDataType(' + 'Namespaces:' + str(self.Namespaces) + ', ' + \
               'StructureDataTypes:' + str(self.StructureDataTypes) + ', ' + \
               'EnumDataTypes:' + str(self.EnumDataTypes) + ', ' + \
               'SimpleDataTypes:' + str(self.SimpleDataTypes) + ', ' + \
               'Name:' + str(self.Name) + ', ' + \
               'Description:' + str(self.Description) + ', ' + \
               'Fields:' + str(self.Fields) + ', ' + \
               'DataSetClassId:' + str(self.DataSetClassId) + ', ' + \
               'ConfigurationVersion:' + str(self.ConfigurationVersion) + ')'

    __repr__ = __str__


class FieldMetaData(FrozenClass):
    '''
    :ivar Name:
    :vartype Name: String
    :ivar Description:
    :vartype Description: LocalizedText
    :ivar FieldFlags:
    :vartype FieldFlags: DataSetFieldFlags
    :ivar BuiltInType:
    :vartype BuiltInType: Byte
    :ivar DataType:
    :vartype DataType: NodeId
    :ivar ValueRank:
    :vartype ValueRank: Int32
    :ivar ArrayDimensions:
    :vartype ArrayDimensions: UInt32
    :ivar MaxStringLength:
    :vartype MaxStringLength: UInt32
    :ivar DataSetFieldId:
    :vartype DataSetFieldId: Guid
    :ivar Properties:
    :vartype Properties: KeyValuePair
    '''

    ua_types = [
        ('Name', 'String'),
        ('Description', 'LocalizedText'),
        ('FieldFlags', 'DataSetFieldFlags'),
        ('BuiltInType', 'Byte'),
        ('DataType', 'NodeId'),
        ('ValueRank', 'Int32'),
        ('ArrayDimensions', 'ListOfUInt32'),
        ('MaxStringLength', 'UInt32'),
        ('DataSetFieldId', 'Guid'),
        ('Properties', 'ListOfKeyValuePair'),
               ]

    def __init__(self):
        self.Name = None
        self.Description = LocalizedText()
        self.FieldFlags = DataSetFieldFlags(0)
        self.BuiltInType = 0
        self.DataType = NodeId()
        self.ValueRank = 0
        self.ArrayDimensions = []
        self.MaxStringLength = 0
        self.DataSetFieldId = Guid()
        self.Properties = []
        self._freeze = True

    def __str__(self):
        return 'FieldMetaData(' + 'Name:' + str(self.Name) + ', ' + \
               'Description:' + str(self.Description) + ', ' + \
               'FieldFlags:' + str(self.FieldFlags) + ', ' + \
               'BuiltInType:' + str(self.BuiltInType) + ', ' + \
               'DataType:' + str(self.DataType) + ', ' + \
               'ValueRank:' + str(self.ValueRank) + ', ' + \
               'ArrayDimensions:' + str(self.ArrayDimensions) + ', ' + \
               'MaxStringLength:' + str(self.MaxStringLength) + ', ' + \
               'DataSetFieldId:' + str(self.DataSetFieldId) + ', ' + \
               'Properties:' + str(self.Properties) + ')'

    __repr__ = __str__


class ConfigurationVersionDataType(FrozenClass):
    '''
    :ivar MajorVersion:
    :vartype MajorVersion: UInt32
    :ivar MinorVersion:
    :vartype MinorVersion: UInt32
    '''

    ua_types = [
        ('MajorVersion', 'UInt32'),
        ('MinorVersion', 'UInt32'),
               ]

    def __init__(self):
        self.MajorVersion = 0
        self.MinorVersion = 0
        self._freeze = True

    def __str__(self):
        return 'ConfigurationVersionDataType(' + 'MajorVersion:' + str(self.MajorVersion) + ', ' + \
               'MinorVersion:' + str(self.MinorVersion) + ')'

    __repr__ = __str__


class PublishedDataSetDataType(FrozenClass):
    '''
    :ivar Name:
    :vartype Name: String
    :ivar DataSetFolder:
    :vartype DataSetFolder: String
    :ivar DataSetMetaData:
    :vartype DataSetMetaData: DataSetMetaDataType
    :ivar ExtensionFields:
    :vartype ExtensionFields: KeyValuePair
    :ivar DataSetSource:
    :vartype DataSetSource: ExtensionObject
    '''

    ua_types = [
        ('Name', 'String'),
        ('DataSetFolder', 'ListOfString'),
        ('DataSetMetaData', 'DataSetMetaDataType'),
        ('ExtensionFields', 'ListOfKeyValuePair'),
        ('DataSetSource', 'ExtensionObject'),
               ]

    def __init__(self):
        self.Name = None
        self.DataSetFolder = []
        self.DataSetMetaData = DataSetMetaDataType()
        self.ExtensionFields = []
        self.DataSetSource = ExtensionObject()
        self._freeze = True

    def __str__(self):
        return 'PublishedDataSetDataType(' + 'Name:' + str(self.Name) + ', ' + \
               'DataSetFolder:' + str(self.DataSetFolder) + ', ' + \
               'DataSetMetaData:' + str(self.DataSetMetaData) + ', ' + \
               'ExtensionFields:' + str(self.ExtensionFields) + ', ' + \
               'DataSetSource:' + str(self.DataSetSource) + ')'

    __repr__ = __str__


class PublishedDataSetSourceDataType(FrozenClass):
    '''
    '''

    ua_types = [
               ]

    def __init__(self):
        self._freeze = True

    def __str__(self):
        return 'PublishedDataSetSourceDataType(' +  + ')'

    __repr__ = __str__


class PublishedVariableDataType(FrozenClass):
    '''
    :ivar PublishedVariable:
    :vartype PublishedVariable: NodeId
    :ivar AttributeId:
    :vartype AttributeId: UInt32
    :ivar SamplingIntervalHint:
    :vartype SamplingIntervalHint: Double
    :ivar DeadbandType:
    :vartype DeadbandType: UInt32
    :ivar DeadbandValue:
    :vartype DeadbandValue: Double
    :ivar IndexRange:
    :vartype IndexRange: String
    :ivar SubstituteValue:
    :vartype SubstituteValue: Variant
    :ivar MetaDataProperties:
    :vartype MetaDataProperties: QualifiedName
    '''

    ua_types = [
        ('PublishedVariable', 'NodeId'),
        ('AttributeId', 'UInt32'),
        ('SamplingIntervalHint', 'Double'),
        ('DeadbandType', 'UInt32'),
        ('DeadbandValue', 'Double'),
        ('IndexRange', 'String'),
        ('SubstituteValue', 'Variant'),
        ('MetaDataProperties', 'ListOfQualifiedName'),
               ]

    def __init__(self):
        self.PublishedVariable = NodeId()
        self.AttributeId = 0
        self.SamplingIntervalHint = 0
        self.DeadbandType = 0
        self.DeadbandValue = 0
        self.IndexRange = None
        self.SubstituteValue = Variant()
        self.MetaDataProperties = []
        self._freeze = True

    def __str__(self):
        return 'PublishedVariableDataType(' + 'PublishedVariable:' + str(self.PublishedVariable) + ', ' + \
               'AttributeId:' + str(self.AttributeId) + ', ' + \
               'SamplingIntervalHint:' + str(self.SamplingIntervalHint) + ', ' + \
               'DeadbandType:' + str(self.DeadbandType) + ', ' + \
               'DeadbandValue:' + str(self.DeadbandValue) + ', ' + \
               'IndexRange:' + str(self.IndexRange) + ', ' + \
               'SubstituteValue:' + str(self.SubstituteValue) + ', ' + \
               'MetaDataProperties:' + str(self.MetaDataProperties) + ')'

    __repr__ = __str__


class PublishedDataItemsDataType(FrozenClass):
    '''
    :ivar PublishedData:
    :vartype PublishedData: PublishedVariableDataType
    '''

    ua_types = [
        ('PublishedData', 'ListOfPublishedVariableDataType'),
               ]

    def __init__(self):
        self.PublishedData = []
        self._freeze = True

    def __str__(self):
        return 'PublishedDataItemsDataType(' + 'PublishedData:' + str(self.PublishedData) + ')'

    __repr__ = __str__


class PublishedEventsDataType(FrozenClass):
    '''
    :ivar EventNotifier:
    :vartype EventNotifier: NodeId
    :ivar SelectedFields:
    :vartype SelectedFields: SimpleAttributeOperand
    :ivar Filter:
    :vartype Filter: ContentFilter
    '''

    ua_types = [
        ('EventNotifier', 'NodeId'),
        ('SelectedFields', 'ListOfSimpleAttributeOperand'),
        ('Filter', 'ContentFilter'),
               ]

    def __init__(self):
        self.EventNotifier = NodeId()
        self.SelectedFields = []
        self.Filter = ContentFilter()
        self._freeze = True

    def __str__(self):
        return 'PublishedEventsDataType(' + 'EventNotifier:' + str(self.EventNotifier) + ', ' + \
               'SelectedFields:' + str(self.SelectedFields) + ', ' + \
               'Filter:' + str(self.Filter) + ')'

    __repr__ = __str__


class DataSetWriterDataType(FrozenClass):
    '''
    :ivar Name:
    :vartype Name: String
    :ivar Enabled:
    :vartype Enabled: Boolean
    :ivar DataSetWriterId:
    :vartype DataSetWriterId: UInt16
    :ivar DataSetFieldContentMask:
    :vartype DataSetFieldContentMask: DataSetFieldContentMask
    :ivar KeyFrameCount:
    :vartype KeyFrameCount: UInt32
    :ivar DataSetName:
    :vartype DataSetName: String
    :ivar DataSetWriterProperties:
    :vartype DataSetWriterProperties: KeyValuePair
    :ivar TransportSettings:
    :vartype TransportSettings: ExtensionObject
    :ivar MessageSettings:
    :vartype MessageSettings: ExtensionObject
    '''

    ua_types = [
        ('Name', 'String'),
        ('Enabled', 'Boolean'),
        ('DataSetWriterId', 'UInt16'),
        ('DataSetFieldContentMask', 'DataSetFieldContentMask'),
        ('KeyFrameCount', 'UInt32'),
        ('DataSetName', 'String'),
        ('DataSetWriterProperties', 'ListOfKeyValuePair'),
        ('TransportSettings', 'ExtensionObject'),
        ('MessageSettings', 'ExtensionObject'),
               ]

    def __init__(self):
        self.Name = None
        self.Enabled = True
        self.DataSetWriterId = 0
        self.DataSetFieldContentMask = DataSetFieldContentMask(0)
        self.KeyFrameCount = 0
        self.DataSetName = None
        self.DataSetWriterProperties = []
        self.TransportSettings = ExtensionObject()
        self.MessageSettings = ExtensionObject()
        self._freeze = True

    def __str__(self):
        return 'DataSetWriterDataType(' + 'Name:' + str(self.Name) + ', ' + \
               'Enabled:' + str(self.Enabled) + ', ' + \
               'DataSetWriterId:' + str(self.DataSetWriterId) + ', ' + \
               'DataSetFieldContentMask:' + str(self.DataSetFieldContentMask) + ', ' + \
               'KeyFrameCount:' + str(self.KeyFrameCount) + ', ' + \
               'DataSetName:' + str(self.DataSetName) + ', ' + \
               'DataSetWriterProperties:' + str(self.DataSetWriterProperties) + ', ' + \
               'TransportSettings:' + str(self.TransportSettings) + ', ' + \
               'MessageSettings:' + str(self.MessageSettings) + ')'

    __repr__ = __str__


class DataSetWriterTransportDataType(FrozenClass):
    '''
    '''

    ua_types = [
               ]

    def __init__(self):
        self._freeze = True

    def __str__(self):
        return 'DataSetWriterTransportDataType(' +  + ')'

    __repr__ = __str__


class DataSetWriterMessageDataType(FrozenClass):
    '''
    '''

    ua_types = [
               ]

    def __init__(self):
        self._freeze = True

    def __str__(self):
        return 'DataSetWriterMessageDataType(' +  + ')'

    __repr__ = __str__


class PubSubGroupDataType(FrozenClass):
    '''
    :ivar Name:
    :vartype Name: String
    :ivar Enabled:
    :vartype Enabled: Boolean
    :ivar SecurityMode:
    :vartype SecurityMode: MessageSecurityMode
    :ivar SecurityGroupId:
    :vartype SecurityGroupId: String
    :ivar SecurityKeyServices:
    :vartype SecurityKeyServices: EndpointDescription
    :ivar MaxNetworkMessageSize:
    :vartype MaxNetworkMessageSize: UInt32
    :ivar GroupProperties:
    :vartype GroupProperties: KeyValuePair
    '''

    ua_types = [
        ('Name', 'String'),
        ('Enabled', 'Boolean'),
        ('SecurityMode', 'MessageSecurityMode'),
        ('SecurityGroupId', 'String'),
        ('SecurityKeyServices', 'ListOfEndpointDescription'),
        ('MaxNetworkMessageSize', 'UInt32'),
        ('GroupProperties', 'ListOfKeyValuePair'),
               ]

    def __init__(self):
        self.Name = None
        self.Enabled = True
        self.SecurityMode = MessageSecurityMode(0)
        self.SecurityGroupId = None
        self.SecurityKeyServices = []
        self.MaxNetworkMessageSize = 0
        self.GroupProperties = []
        self._freeze = True

    def __str__(self):
        return 'PubSubGroupDataType(' + 'Name:' + str(self.Name) + ', ' + \
               'Enabled:' + str(self.Enabled) + ', ' + \
               'SecurityMode:' + str(self.SecurityMode) + ', ' + \
               'SecurityGroupId:' + str(self.SecurityGroupId) + ', ' + \
               'SecurityKeyServices:' + str(self.SecurityKeyServices) + ', ' + \
               'MaxNetworkMessageSize:' + str(self.MaxNetworkMessageSize) + ', ' + \
               'GroupProperties:' + str(self.GroupProperties) + ')'

    __repr__ = __str__


class WriterGroupDataType(FrozenClass):
    '''
    :ivar Name:
    :vartype Name: String
    :ivar Enabled:
    :vartype Enabled: Boolean
    :ivar SecurityMode:
    :vartype SecurityMode: MessageSecurityMode
    :ivar SecurityGroupId:
    :vartype SecurityGroupId: String
    :ivar SecurityKeyServices:
    :vartype SecurityKeyServices: EndpointDescription
    :ivar MaxNetworkMessageSize:
    :vartype MaxNetworkMessageSize: UInt32
    :ivar GroupProperties:
    :vartype GroupProperties: KeyValuePair
    :ivar WriterGroupId:
    :vartype WriterGroupId: UInt16
    :ivar PublishingInterval:
    :vartype PublishingInterval: Double
    :ivar KeepAliveTime:
    :vartype KeepAliveTime: Double
    :ivar Priority:
    :vartype Priority: Byte
    :ivar LocaleIds:
    :vartype LocaleIds: String
    :ivar TransportSettings:
    :vartype TransportSettings: ExtensionObject
    :ivar MessageSettings:
    :vartype MessageSettings: ExtensionObject
    :ivar DataSetWriters:
    :vartype DataSetWriters: DataSetWriterDataType
    '''

    ua_types = [
        ('Name', 'String'),
        ('Enabled', 'Boolean'),
        ('SecurityMode', 'MessageSecurityMode'),
        ('SecurityGroupId', 'String'),
        ('SecurityKeyServices', 'ListOfEndpointDescription'),
        ('MaxNetworkMessageSize', 'UInt32'),
        ('GroupProperties', 'ListOfKeyValuePair'),
        ('WriterGroupId', 'UInt16'),
        ('PublishingInterval', 'Double'),
        ('KeepAliveTime', 'Double'),
        ('Priority', 'Byte'),
        ('LocaleIds', 'ListOfString'),
        ('TransportSettings', 'ExtensionObject'),
        ('MessageSettings', 'ExtensionObject'),
        ('DataSetWriters', 'ListOfDataSetWriterDataType'),
               ]

    def __init__(self):
        self.Name = None
        self.Enabled = True
        self.SecurityMode = MessageSecurityMode(0)
        self.SecurityGroupId = None
        self.SecurityKeyServices = []
        self.MaxNetworkMessageSize = 0
        self.GroupProperties = []
        self.WriterGroupId = 0
        self.PublishingInterval = 0
        self.KeepAliveTime = 0
        self.Priority = 0
        self.LocaleIds = []
        self.TransportSettings = ExtensionObject()
        self.MessageSettings = ExtensionObject()
        self.DataSetWriters = []
        self._freeze = True

    def __str__(self):
        return 'WriterGroupDataType(' + 'Name:' + str(self.Name) + ', ' + \
               'Enabled:' + str(self.Enabled) + ', ' + \
               'SecurityMode:' + str(self.SecurityMode) + ', ' + \
               'SecurityGroupId:' + str(self.SecurityGroupId) + ', ' + \
               'SecurityKeyServices:' + str(self.SecurityKeyServices) + ', ' + \
               'MaxNetworkMessageSize:' + str(self.MaxNetworkMessageSize) + ', ' + \
               'GroupProperties:' + str(self.GroupProperties) + ', ' + \
               'WriterGroupId:' + str(self.WriterGroupId) + ', ' + \
               'PublishingInterval:' + str(self.PublishingInterval) + ', ' + \
               'KeepAliveTime:' + str(self.KeepAliveTime) + ', ' + \
               'Priority:' + str(self.Priority) + ', ' + \
               'LocaleIds:' + str(self.LocaleIds) + ', ' + \
               'TransportSettings:' + str(self.TransportSettings) + ', ' + \
               'MessageSettings:' + str(self.MessageSettings) + ', ' + \
               'DataSetWriters:' + str(self.DataSetWriters) + ')'

    __repr__ = __str__


class WriterGroupTransportDataType(FrozenClass):
    '''
    '''

    ua_types = [
               ]

    def __init__(self):
        self._freeze = True

    def __str__(self):
        return 'WriterGroupTransportDataType(' +  + ')'

    __repr__ = __str__


class WriterGroupMessageDataType(FrozenClass):
    '''
    '''

    ua_types = [
               ]

    def __init__(self):
        self._freeze = True

    def __str__(self):
        return 'WriterGroupMessageDataType(' +  + ')'

    __repr__ = __str__


class PubSubConnectionDataType(FrozenClass):
    '''
    :ivar Name:
    :vartype Name: String
    :ivar Enabled:
    :vartype Enabled: Boolean
    :ivar PublisherId:
    :vartype PublisherId: Variant
    :ivar TransportProfileUri:
    :vartype TransportProfileUri: String
    :ivar Address:
    :vartype Address: ExtensionObject
    :ivar ConnectionProperties:
    :vartype ConnectionProperties: KeyValuePair
    :ivar TransportSettings:
    :vartype TransportSettings: ExtensionObject
    :ivar WriterGroups:
    :vartype WriterGroups: WriterGroupDataType
    :ivar ReaderGroups:
    :vartype ReaderGroups: ReaderGroupDataType
    '''

    ua_types = [
        ('Name', 'String'),
        ('Enabled', 'Boolean'),
        ('PublisherId', 'Variant'),
        ('TransportProfileUri', 'String'),
        ('Address', 'ExtensionObject'),
        ('ConnectionProperties', 'ListOfKeyValuePair'),
        ('TransportSettings', 'ExtensionObject'),
        ('WriterGroups', 'ListOfWriterGroupDataType'),
        ('ReaderGroups', 'ListOfReaderGroupDataType'),
               ]

    def __init__(self):
        self.Name = None
        self.Enabled = True
        self.PublisherId = Variant()
        self.TransportProfileUri = None
        self.Address = ExtensionObject()
        self.ConnectionProperties = []
        self.TransportSettings = ExtensionObject()
        self.WriterGroups = []
        self.ReaderGroups = []
        self._freeze = True

    def __str__(self):
        return 'PubSubConnectionDataType(' + 'Name:' + str(self.Name) + ', ' + \
               'Enabled:' + str(self.Enabled) + ', ' + \
               'PublisherId:' + str(self.PublisherId) + ', ' + \
               'TransportProfileUri:' + str(self.TransportProfileUri) + ', ' + \
               'Address:' + str(self.Address) + ', ' + \
               'ConnectionProperties:' + str(self.ConnectionProperties) + ', ' + \
               'TransportSettings:' + str(self.TransportSettings) + ', ' + \
               'WriterGroups:' + str(self.WriterGroups) + ', ' + \
               'ReaderGroups:' + str(self.ReaderGroups) + ')'

    __repr__ = __str__


class ConnectionTransportDataType(FrozenClass):
    '''
    '''

    ua_types = [
               ]

    def __init__(self):
        self._freeze = True

    def __str__(self):
        return 'ConnectionTransportDataType(' +  + ')'

    __repr__ = __str__


class NetworkAddressDataType(FrozenClass):
    '''
    :ivar NetworkInterface:
    :vartype NetworkInterface: String
    '''

    ua_types = [
        ('NetworkInterface', 'String'),
               ]

    def __init__(self):
        self.NetworkInterface = None
        self._freeze = True

    def __str__(self):
        return 'NetworkAddressDataType(' + 'NetworkInterface:' + str(self.NetworkInterface) + ')'

    __repr__ = __str__


class NetworkAddressUrlDataType(FrozenClass):
    '''
    :ivar NetworkInterface:
    :vartype NetworkInterface: String
    :ivar Url:
    :vartype Url: String
    '''

    ua_types = [
        ('NetworkInterface', 'String'),
        ('Url', 'String'),
               ]

    def __init__(self):
        self.NetworkInterface = None
        self.Url = None
        self._freeze = True

    def __str__(self):
        return 'NetworkAddressUrlDataType(' + 'NetworkInterface:' + str(self.NetworkInterface) + ', ' + \
               'Url:' + str(self.Url) + ')'

    __repr__ = __str__


class ReaderGroupDataType(FrozenClass):
    '''
    :ivar Name:
    :vartype Name: String
    :ivar Enabled:
    :vartype Enabled: Boolean
    :ivar SecurityMode:
    :vartype SecurityMode: MessageSecurityMode
    :ivar SecurityGroupId:
    :vartype SecurityGroupId: String
    :ivar SecurityKeyServices:
    :vartype SecurityKeyServices: EndpointDescription
    :ivar MaxNetworkMessageSize:
    :vartype MaxNetworkMessageSize: UInt32
    :ivar GroupProperties:
    :vartype GroupProperties: KeyValuePair
    :ivar TransportSettings:
    :vartype TransportSettings: ExtensionObject
    :ivar MessageSettings:
    :vartype MessageSettings: ExtensionObject
    :ivar DataSetReaders:
    :vartype DataSetReaders: DataSetReaderDataType
    '''

    ua_types = [
        ('Name', 'String'),
        ('Enabled', 'Boolean'),
        ('SecurityMode', 'MessageSecurityMode'),
        ('SecurityGroupId', 'String'),
        ('SecurityKeyServices', 'ListOfEndpointDescription'),
        ('MaxNetworkMessageSize', 'UInt32'),
        ('GroupProperties', 'ListOfKeyValuePair'),
        ('TransportSettings', 'ExtensionObject'),
        ('MessageSettings', 'ExtensionObject'),
        ('DataSetReaders', 'ListOfDataSetReaderDataType'),
               ]

    def __init__(self):
        self.Name = None
        self.Enabled = True
        self.SecurityMode = MessageSecurityMode(0)
        self.SecurityGroupId = None
        self.SecurityKeyServices = []
        self.MaxNetworkMessageSize = 0
        self.GroupProperties = []
        self.TransportSettings = ExtensionObject()
        self.MessageSettings = ExtensionObject()
        self.DataSetReaders = []
        self._freeze = True

    def __str__(self):
        return 'ReaderGroupDataType(' + 'Name:' + str(self.Name) + ', ' + \
               'Enabled:' + str(self.Enabled) + ', ' + \
               'SecurityMode:' + str(self.SecurityMode) + ', ' + \
               'SecurityGroupId:' + str(self.SecurityGroupId) + ', ' + \
               'SecurityKeyServices:' + str(self.SecurityKeyServices) + ', ' + \
               'MaxNetworkMessageSize:' + str(self.MaxNetworkMessageSize) + ', ' + \
               'GroupProperties:' + str(self.GroupProperties) + ', ' + \
               'TransportSettings:' + str(self.TransportSettings) + ', ' + \
               'MessageSettings:' + str(self.MessageSettings) + ', ' + \
               'DataSetReaders:' + str(self.DataSetReaders) + ')'

    __repr__ = __str__


class ReaderGroupTransportDataType(FrozenClass):
    '''
    '''

    ua_types = [
               ]

    def __init__(self):
        self._freeze = True

    def __str__(self):
        return 'ReaderGroupTransportDataType(' +  + ')'

    __repr__ = __str__


class ReaderGroupMessageDataType(FrozenClass):
    '''
    '''

    ua_types = [
               ]

    def __init__(self):
        self._freeze = True

    def __str__(self):
        return 'ReaderGroupMessageDataType(' +  + ')'

    __repr__ = __str__


class DataSetReaderDataType(FrozenClass):
    '''
    :ivar Name:
    :vartype Name: String
    :ivar Enabled:
    :vartype Enabled: Boolean
    :ivar PublisherId:
    :vartype PublisherId: Variant
    :ivar WriterGroupId:
    :vartype WriterGroupId: UInt16
    :ivar DataSetWriterId:
    :vartype DataSetWriterId: UInt16
    :ivar DataSetMetaData:
    :vartype DataSetMetaData: DataSetMetaDataType
    :ivar DataSetFieldContentMask:
    :vartype DataSetFieldContentMask: DataSetFieldContentMask
    :ivar MessageReceiveTimeout:
    :vartype MessageReceiveTimeout: Double
    :ivar SecurityMode:
    :vartype SecurityMode: MessageSecurityMode
    :ivar SecurityGroupId:
    :vartype SecurityGroupId: String
    :ivar SecurityKeyServices:
    :vartype SecurityKeyServices: EndpointDescription
    :ivar DataSetReaderProperties:
    :vartype DataSetReaderProperties: KeyValuePair
    :ivar TransportSettings:
    :vartype TransportSettings: ExtensionObject
    :ivar MessageSettings:
    :vartype MessageSettings: ExtensionObject
    :ivar SubscribedDataSet:
    :vartype SubscribedDataSet: ExtensionObject
    '''

    ua_types = [
        ('Name', 'String'),
        ('Enabled', 'Boolean'),
        ('PublisherId', 'Variant'),
        ('WriterGroupId', 'UInt16'),
        ('DataSetWriterId', 'UInt16'),
        ('DataSetMetaData', 'DataSetMetaDataType'),
        ('DataSetFieldContentMask', 'DataSetFieldContentMask'),
        ('MessageReceiveTimeout', 'Double'),
        ('SecurityMode', 'MessageSecurityMode'),
        ('SecurityGroupId', 'String'),
        ('SecurityKeyServices', 'ListOfEndpointDescription'),
        ('DataSetReaderProperties', 'ListOfKeyValuePair'),
        ('TransportSettings', 'ExtensionObject'),
        ('MessageSettings', 'ExtensionObject'),
        ('SubscribedDataSet', 'ExtensionObject'),
               ]

    def __init__(self):
        self.Name = None
        self.Enabled = True
        self.PublisherId = Variant()
        self.WriterGroupId = 0
        self.DataSetWriterId = 0
        self.DataSetMetaData = DataSetMetaDataType()
        self.DataSetFieldContentMask = DataSetFieldContentMask(0)
        self.MessageReceiveTimeout = 0
        self.SecurityMode = MessageSecurityMode(0)
        self.SecurityGroupId = None
        self.SecurityKeyServices = []
        self.DataSetReaderProperties = []
        self.TransportSettings = ExtensionObject()
        self.MessageSettings = ExtensionObject()
        self.SubscribedDataSet = ExtensionObject()
        self._freeze = True

    def __str__(self):
        return 'DataSetReaderDataType(' + 'Name:' + str(self.Name) + ', ' + \
               'Enabled:' + str(self.Enabled) + ', ' + \
               'PublisherId:' + str(self.PublisherId) + ', ' + \
               'WriterGroupId:' + str(self.WriterGroupId) + ', ' + \
               'DataSetWriterId:' + str(self.DataSetWriterId) + ', ' + \
               'DataSetMetaData:' + str(self.DataSetMetaData) + ', ' + \
               'DataSetFieldContentMask:' + str(self.DataSetFieldContentMask) + ', ' + \
               'MessageReceiveTimeout:' + str(self.MessageReceiveTimeout) + ', ' + \
               'SecurityMode:' + str(self.SecurityMode) + ', ' + \
               'SecurityGroupId:' + str(self.SecurityGroupId) + ', ' + \
               'SecurityKeyServices:' + str(self.SecurityKeyServices) + ', ' + \
               'DataSetReaderProperties:' + str(self.DataSetReaderProperties) + ', ' + \
               'TransportSettings:' + str(self.TransportSettings) + ', ' + \
               'MessageSettings:' + str(self.MessageSettings) + ', ' + \
               'SubscribedDataSet:' + str(self.SubscribedDataSet) + ')'

    __repr__ = __str__


class DataSetReaderTransportDataType(FrozenClass):
    '''
    '''

    ua_types = [
               ]

    def __init__(self):
        self._freeze = True

    def __str__(self):
        return 'DataSetReaderTransportDataType(' +  + ')'

    __repr__ = __str__


class DataSetReaderMessageDataType(FrozenClass):
    '''
    '''

    ua_types = [
               ]

    def __init__(self):
        self._freeze = True

    def __str__(self):
        return 'DataSetReaderMessageDataType(' +  + ')'

    __repr__ = __str__


class SubscribedDataSetDataType(FrozenClass):
    '''
    '''

    ua_types = [
               ]

    def __init__(self):
        self._freeze = True

    def __str__(self):
        return 'SubscribedDataSetDataType(' +  + ')'

    __repr__ = __str__


class TargetVariablesDataType(FrozenClass):
    '''
    :ivar TargetVariables:
    :vartype TargetVariables: FieldTargetDataType
    '''

    ua_types = [
        ('TargetVariables', 'ListOfFieldTargetDataType'),
               ]

    def __init__(self):
        self.TargetVariables = []
        self._freeze = True

    def __str__(self):
        return 'TargetVariablesDataType(' + 'TargetVariables:' + str(self.TargetVariables) + ')'

    __repr__ = __str__


class FieldTargetDataType(FrozenClass):
    '''
    :ivar DataSetFieldId:
    :vartype DataSetFieldId: Guid
    :ivar ReceiverIndexRange:
    :vartype ReceiverIndexRange: String
    :ivar TargetNodeId:
    :vartype TargetNodeId: NodeId
    :ivar AttributeId:
    :vartype AttributeId: UInt32
    :ivar WriteIndexRange:
    :vartype WriteIndexRange: String
    :ivar OverrideValueHandling:
    :vartype OverrideValueHandling: OverrideValueHandling
    :ivar OverrideValue:
    :vartype OverrideValue: Variant
    '''

    ua_types = [
        ('DataSetFieldId', 'Guid'),
        ('ReceiverIndexRange', 'String'),
        ('TargetNodeId', 'NodeId'),
        ('AttributeId', 'UInt32'),
        ('WriteIndexRange', 'String'),
        ('OverrideValueHandling', 'OverrideValueHandling'),
        ('OverrideValue', 'Variant'),
               ]

    def __init__(self):
        self.DataSetFieldId = Guid()
        self.ReceiverIndexRange = None
        self.TargetNodeId = NodeId()
        self.AttributeId = 0
        self.WriteIndexRange = None
        self.OverrideValueHandling = OverrideValueHandling(0)
        self.OverrideValue = Variant()
        self._freeze = True

    def __str__(self):
        return 'FieldTargetDataType(' + 'DataSetFieldId:' + str(self.DataSetFieldId) + ', ' + \
               'ReceiverIndexRange:' + str(self.ReceiverIndexRange) + ', ' + \
               'TargetNodeId:' + str(self.TargetNodeId) + ', ' + \
               'AttributeId:' + str(self.AttributeId) + ', ' + \
               'WriteIndexRange:' + str(self.WriteIndexRange) + ', ' + \
               'OverrideValueHandling:' + str(self.OverrideValueHandling) + ', ' + \
               'OverrideValue:' + str(self.OverrideValue) + ')'

    __repr__ = __str__


class SubscribedDataSetMirrorDataType(FrozenClass):
    '''
    :ivar ParentNodeName:
    :vartype ParentNodeName: String
    :ivar RolePermissions:
    :vartype RolePermissions: RolePermissionType
    '''

    ua_types = [
        ('ParentNodeName', 'String'),
        ('RolePermissions', 'ListOfRolePermissionType'),
               ]

    def __init__(self):
        self.ParentNodeName = None
        self.RolePermissions = []
        self._freeze = True

    def __str__(self):
        return 'SubscribedDataSetMirrorDataType(' + 'ParentNodeName:' + str(self.ParentNodeName) + ', ' + \
               'RolePermissions:' + str(self.RolePermissions) + ')'

    __repr__ = __str__


class PubSubConfigurationDataType(FrozenClass):
    '''
    :ivar PublishedDataSets:
    :vartype PublishedDataSets: PublishedDataSetDataType
    :ivar Connections:
    :vartype Connections: PubSubConnectionDataType
    :ivar Enabled:
    :vartype Enabled: Boolean
    '''

    ua_types = [
        ('PublishedDataSets', 'ListOfPublishedDataSetDataType'),
        ('Connections', 'ListOfPubSubConnectionDataType'),
        ('Enabled', 'Boolean'),
               ]

    def __init__(self):
        self.PublishedDataSets = []
        self.Connections = []
        self.Enabled = True
        self._freeze = True

    def __str__(self):
        return 'PubSubConfigurationDataType(' + 'PublishedDataSets:' + str(self.PublishedDataSets) + ', ' + \
               'Connections:' + str(self.Connections) + ', ' + \
               'Enabled:' + str(self.Enabled) + ')'

    __repr__ = __str__


class UadpWriterGroupMessageDataType(FrozenClass):
    '''
    :ivar GroupVersion:
    :vartype GroupVersion: UInt32
    :ivar DataSetOrdering:
    :vartype DataSetOrdering: DataSetOrderingType
    :ivar NetworkMessageContentMask:
    :vartype NetworkMessageContentMask: UadpNetworkMessageContentMask
    :ivar SamplingOffset:
    :vartype SamplingOffset: Double
    :ivar PublishingOffset:
    :vartype PublishingOffset: Double
    '''

    ua_types = [
        ('GroupVersion', 'UInt32'),
        ('DataSetOrdering', 'DataSetOrderingType'),
        ('NetworkMessageContentMask', 'UadpNetworkMessageContentMask'),
        ('SamplingOffset', 'Double'),
        ('PublishingOffset', 'ListOfDouble'),
               ]

    def __init__(self):
        self.GroupVersion = 0
        self.DataSetOrdering = DataSetOrderingType(0)
        self.NetworkMessageContentMask = UadpNetworkMessageContentMask(0)
        self.SamplingOffset = 0
        self.PublishingOffset = []
        self._freeze = True

    def __str__(self):
        return 'UadpWriterGroupMessageDataType(' + 'GroupVersion:' + str(self.GroupVersion) + ', ' + \
               'DataSetOrdering:' + str(self.DataSetOrdering) + ', ' + \
               'NetworkMessageContentMask:' + str(self.NetworkMessageContentMask) + ', ' + \
               'SamplingOffset:' + str(self.SamplingOffset) + ', ' + \
               'PublishingOffset:' + str(self.PublishingOffset) + ')'

    __repr__ = __str__


class UadpDataSetWriterMessageDataType(FrozenClass):
    '''
    :ivar DataSetMessageContentMask:
    :vartype DataSetMessageContentMask: UadpDataSetMessageContentMask
    :ivar ConfiguredSize:
    :vartype ConfiguredSize: UInt16
    :ivar NetworkMessageNumber:
    :vartype NetworkMessageNumber: UInt16
    :ivar DataSetOffset:
    :vartype DataSetOffset: UInt16
    '''

    ua_types = [
        ('DataSetMessageContentMask', 'UadpDataSetMessageContentMask'),
        ('ConfiguredSize', 'UInt16'),
        ('NetworkMessageNumber', 'UInt16'),
        ('DataSetOffset', 'UInt16'),
               ]

    def __init__(self):
        self.DataSetMessageContentMask = UadpDataSetMessageContentMask(0)
        self.ConfiguredSize = 0
        self.NetworkMessageNumber = 0
        self.DataSetOffset = 0
        self._freeze = True

    def __str__(self):
        return 'UadpDataSetWriterMessageDataType(' + 'DataSetMessageContentMask:' + str(self.DataSetMessageContentMask) + ', ' + \
               'ConfiguredSize:' + str(self.ConfiguredSize) + ', ' + \
               'NetworkMessageNumber:' + str(self.NetworkMessageNumber) + ', ' + \
               'DataSetOffset:' + str(self.DataSetOffset) + ')'

    __repr__ = __str__


class UadpDataSetReaderMessageDataType(FrozenClass):
    '''
    :ivar GroupVersion:
    :vartype GroupVersion: UInt32
    :ivar NetworkMessageNumber:
    :vartype NetworkMessageNumber: UInt16
    :ivar DataSetOffset:
    :vartype DataSetOffset: UInt16
    :ivar DataSetClassId:
    :vartype DataSetClassId: Guid
    :ivar NetworkMessageContentMask:
    :vartype NetworkMessageContentMask: UadpNetworkMessageContentMask
    :ivar DataSetMessageContentMask:
    :vartype DataSetMessageContentMask: UadpDataSetMessageContentMask
    :ivar PublishingInterval:
    :vartype PublishingInterval: Double
    :ivar ReceiveOffset:
    :vartype ReceiveOffset: Double
    :ivar ProcessingOffset:
    :vartype ProcessingOffset: Double
    '''

    ua_types = [
        ('GroupVersion', 'UInt32'),
        ('NetworkMessageNumber', 'UInt16'),
        ('DataSetOffset', 'UInt16'),
        ('DataSetClassId', 'Guid'),
        ('NetworkMessageContentMask', 'UadpNetworkMessageContentMask'),
        ('DataSetMessageContentMask', 'UadpDataSetMessageContentMask'),
        ('PublishingInterval', 'Double'),
        ('ReceiveOffset', 'Double'),
        ('ProcessingOffset', 'Double'),
               ]

    def __init__(self):
        self.GroupVersion = 0
        self.NetworkMessageNumber = 0
        self.DataSetOffset = 0
        self.DataSetClassId = Guid()
        self.NetworkMessageContentMask = UadpNetworkMessageContentMask(0)
        self.DataSetMessageContentMask = UadpDataSetMessageContentMask(0)
        self.PublishingInterval = 0
        self.ReceiveOffset = 0
        self.ProcessingOffset = 0
        self._freeze = True

    def __str__(self):
        return 'UadpDataSetReaderMessageDataType(' + 'GroupVersion:' + str(self.GroupVersion) + ', ' + \
               'NetworkMessageNumber:' + str(self.NetworkMessageNumber) + ', ' + \
               'DataSetOffset:' + str(self.DataSetOffset) + ', ' + \
               'DataSetClassId:' + str(self.DataSetClassId) + ', ' + \
               'NetworkMessageContentMask:' + str(self.NetworkMessageContentMask) + ', ' + \
               'DataSetMessageContentMask:' + str(self.DataSetMessageContentMask) + ', ' + \
               'PublishingInterval:' + str(self.PublishingInterval) + ', ' + \
               'ReceiveOffset:' + str(self.ReceiveOffset) + ', ' + \
               'ProcessingOffset:' + str(self.ProcessingOffset) + ')'

    __repr__ = __str__


class JsonWriterGroupMessageDataType(FrozenClass):
    '''
    :ivar NetworkMessageContentMask:
    :vartype NetworkMessageContentMask: JsonNetworkMessageContentMask
    '''

    ua_types = [
        ('NetworkMessageContentMask', 'JsonNetworkMessageContentMask'),
               ]

    def __init__(self):
        self.NetworkMessageContentMask = JsonNetworkMessageContentMask(0)
        self._freeze = True

    def __str__(self):
        return 'JsonWriterGroupMessageDataType(' + 'NetworkMessageContentMask:' + str(self.NetworkMessageContentMask) + ')'

    __repr__ = __str__


class JsonDataSetWriterMessageDataType(FrozenClass):
    '''
    :ivar DataSetMessageContentMask:
    :vartype DataSetMessageContentMask: JsonDataSetMessageContentMask
    '''

    ua_types = [
        ('DataSetMessageContentMask', 'JsonDataSetMessageContentMask'),
               ]

    def __init__(self):
        self.DataSetMessageContentMask = JsonDataSetMessageContentMask(0)
        self._freeze = True

    def __str__(self):
        return 'JsonDataSetWriterMessageDataType(' + 'DataSetMessageContentMask:' + str(self.DataSetMessageContentMask) + ')'

    __repr__ = __str__


class JsonDataSetReaderMessageDataType(FrozenClass):
    '''
    :ivar NetworkMessageContentMask:
    :vartype NetworkMessageContentMask: JsonNetworkMessageContentMask
    :ivar DataSetMessageContentMask:
    :vartype DataSetMessageContentMask: JsonDataSetMessageContentMask
    '''

    ua_types = [
        ('NetworkMessageContentMask', 'JsonNetworkMessageContentMask'),
        ('DataSetMessageContentMask', 'JsonDataSetMessageContentMask'),
               ]

    def __init__(self):
        self.NetworkMessageContentMask = JsonNetworkMessageContentMask(0)
        self.DataSetMessageContentMask = JsonDataSetMessageContentMask(0)
        self._freeze = True

    def __str__(self):
        return 'JsonDataSetReaderMessageDataType(' + 'NetworkMessageContentMask:' + str(self.NetworkMessageContentMask) + ', ' + \
               'DataSetMessageContentMask:' + str(self.DataSetMessageContentMask) + ')'

    __repr__ = __str__


class DatagramConnectionTransportDataType(FrozenClass):
    '''
    :ivar DiscoveryAddress:
    :vartype DiscoveryAddress: ExtensionObject
    '''

    ua_types = [
        ('DiscoveryAddress', 'ExtensionObject'),
               ]

    def __init__(self):
        self.DiscoveryAddress = ExtensionObject()
        self._freeze = True

    def __str__(self):
        return 'DatagramConnectionTransportDataType(' + 'DiscoveryAddress:' + str(self.DiscoveryAddress) + ')'

    __repr__ = __str__


class DatagramWriterGroupTransportDataType(FrozenClass):
    '''
    :ivar MessageRepeatCount:
    :vartype MessageRepeatCount: Byte
    :ivar MessageRepeatDelay:
    :vartype MessageRepeatDelay: Double
    '''

    ua_types = [
        ('MessageRepeatCount', 'Byte'),
        ('MessageRepeatDelay', 'Double'),
               ]

    def __init__(self):
        self.MessageRepeatCount = 0
        self.MessageRepeatDelay = 0
        self._freeze = True

    def __str__(self):
        return 'DatagramWriterGroupTransportDataType(' + 'MessageRepeatCount:' + str(self.MessageRepeatCount) + ', ' + \
               'MessageRepeatDelay:' + str(self.MessageRepeatDelay) + ')'

    __repr__ = __str__


class BrokerConnectionTransportDataType(FrozenClass):
    '''
    :ivar ResourceUri:
    :vartype ResourceUri: String
    :ivar AuthenticationProfileUri:
    :vartype AuthenticationProfileUri: String
    '''

    ua_types = [
        ('ResourceUri', 'String'),
        ('AuthenticationProfileUri', 'String'),
               ]

    def __init__(self):
        self.ResourceUri = None
        self.AuthenticationProfileUri = None
        self._freeze = True

    def __str__(self):
        return 'BrokerConnectionTransportDataType(' + 'ResourceUri:' + str(self.ResourceUri) + ', ' + \
               'AuthenticationProfileUri:' + str(self.AuthenticationProfileUri) + ')'

    __repr__ = __str__


class BrokerWriterGroupTransportDataType(FrozenClass):
    '''
    :ivar QueueName:
    :vartype QueueName: String
    :ivar ResourceUri:
    :vartype ResourceUri: String
    :ivar AuthenticationProfileUri:
    :vartype AuthenticationProfileUri: String
    :ivar RequestedDeliveryGuarantee:
    :vartype RequestedDeliveryGuarantee: BrokerTransportQualityOfService
    '''

    ua_types = [
        ('QueueName', 'String'),
        ('ResourceUri', 'String'),
        ('AuthenticationProfileUri', 'String'),
        ('RequestedDeliveryGuarantee', 'BrokerTransportQualityOfService'),
               ]

    def __init__(self):
        self.QueueName = None
        self.ResourceUri = None
        self.AuthenticationProfileUri = None
        self.RequestedDeliveryGuarantee = BrokerTransportQualityOfService(0)
        self._freeze = True

    def __str__(self):
        return 'BrokerWriterGroupTransportDataType(' + 'QueueName:' + str(self.QueueName) + ', ' + \
               'ResourceUri:' + str(self.ResourceUri) + ', ' + \
               'AuthenticationProfileUri:' + str(self.AuthenticationProfileUri) + ', ' + \
               'RequestedDeliveryGuarantee:' + str(self.RequestedDeliveryGuarantee) + ')'

    __repr__ = __str__


class BrokerDataSetWriterTransportDataType(FrozenClass):
    '''
    :ivar QueueName:
    :vartype QueueName: String
    :ivar ResourceUri:
    :vartype ResourceUri: String
    :ivar AuthenticationProfileUri:
    :vartype AuthenticationProfileUri: String
    :ivar MetaDataQueueName:
    :vartype MetaDataQueueName: String
    :ivar MetaDataUpdateTime:
    :vartype MetaDataUpdateTime: Double
    '''

    ua_types = [
        ('QueueName', 'String'),
        ('ResourceUri', 'String'),
        ('AuthenticationProfileUri', 'String'),
        ('MetaDataQueueName', 'String'),
        ('MetaDataUpdateTime', 'Double'),
               ]

    def __init__(self):
        self.QueueName = None
        self.ResourceUri = None
        self.AuthenticationProfileUri = None
        self.MetaDataQueueName = None
        self.MetaDataUpdateTime = 0
        self._freeze = True

    def __str__(self):
        return 'BrokerDataSetWriterTransportDataType(' + 'QueueName:' + str(self.QueueName) + ', ' + \
               'ResourceUri:' + str(self.ResourceUri) + ', ' + \
               'AuthenticationProfileUri:' + str(self.AuthenticationProfileUri) + ', ' + \
               'MetaDataQueueName:' + str(self.MetaDataQueueName) + ', ' + \
               'MetaDataUpdateTime:' + str(self.MetaDataUpdateTime) + ')'

    __repr__ = __str__


class BrokerDataSetReaderTransportDataType(FrozenClass):
    '''
    :ivar QueueName:
    :vartype QueueName: String
    :ivar ResourceUri:
    :vartype ResourceUri: String
    :ivar AuthenticationProfileUri:
    :vartype AuthenticationProfileUri: String
    :ivar RequestedDeliveryGuarantee:
    :vartype RequestedDeliveryGuarantee: BrokerTransportQualityOfService
    :ivar MetaDataQueueName:
    :vartype MetaDataQueueName: String
    '''

    ua_types = [
        ('QueueName', 'String'),
        ('ResourceUri', 'String'),
        ('AuthenticationProfileUri', 'String'),
        ('RequestedDeliveryGuarantee', 'BrokerTransportQualityOfService'),
        ('MetaDataQueueName', 'String'),
               ]

    def __init__(self):
        self.QueueName = None
        self.ResourceUri = None
        self.AuthenticationProfileUri = None
        self.RequestedDeliveryGuarantee = BrokerTransportQualityOfService(0)
        self.MetaDataQueueName = None
        self._freeze = True

    def __str__(self):
        return 'BrokerDataSetReaderTransportDataType(' + 'QueueName:' + str(self.QueueName) + ', ' + \
               'ResourceUri:' + str(self.ResourceUri) + ', ' + \
               'AuthenticationProfileUri:' + str(self.AuthenticationProfileUri) + ', ' + \
               'RequestedDeliveryGuarantee:' + str(self.RequestedDeliveryGuarantee) + ', ' + \
               'MetaDataQueueName:' + str(self.MetaDataQueueName) + ')'

    __repr__ = __str__


class RolePermissionType(FrozenClass):
    '''
    :ivar RoleId:
    :vartype RoleId: NodeId
    :ivar Permissions:
    :vartype Permissions: UInt32
    '''

    ua_types = [
        ('RoleId', 'NodeId'),
        ('Permissions', 'UInt32'),
               ]

    def __init__(self):
        self.RoleId = NodeId()
        self.Permissions = 0
        self._freeze = True

    def __str__(self):
        return 'RolePermissionType(' + 'RoleId:' + str(self.RoleId) + ', ' + \
               'Permissions:' + str(self.Permissions) + ')'

    __repr__ = __str__


class StructureField(FrozenClass):
    '''
    :ivar Name:
    :vartype Name: String
    :ivar Description:
    :vartype Description: LocalizedText
    :ivar DataType:
    :vartype DataType: NodeId
    :ivar ValueRank:
    :vartype ValueRank: Int32
    :ivar ArrayDimensions:
    :vartype ArrayDimensions: UInt32
    :ivar MaxStringLength:
    :vartype MaxStringLength: UInt32
    :ivar IsOptional:
    :vartype IsOptional: Boolean
    '''

    ua_types = [
        ('Name', 'String'),
        ('Description', 'LocalizedText'),
        ('DataType', 'NodeId'),
        ('ValueRank', 'Int32'),
        ('ArrayDimensions', 'ListOfUInt32'),
        ('MaxStringLength', 'UInt32'),
        ('IsOptional', 'Boolean'),
               ]

    def __init__(self):
        self.Name = None
        self.Description = LocalizedText()
        self.DataType = NodeId()
        self.ValueRank = 0
        self.ArrayDimensions = []
        self.MaxStringLength = 0
        self.IsOptional = True
        self._freeze = True

    def __str__(self):
        return 'StructureField(' + 'Name:' + str(self.Name) + ', ' + \
               'Description:' + str(self.Description) + ', ' + \
               'DataType:' + str(self.DataType) + ', ' + \
               'ValueRank:' + str(self.ValueRank) + ', ' + \
               'ArrayDimensions:' + str(self.ArrayDimensions) + ', ' + \
               'MaxStringLength:' + str(self.MaxStringLength) + ', ' + \
               'IsOptional:' + str(self.IsOptional) + ')'

    __repr__ = __str__


class StructureDefinition(FrozenClass):
    '''
    :ivar DefaultEncodingId:
    :vartype DefaultEncodingId: NodeId
    :ivar BaseDataType:
    :vartype BaseDataType: NodeId
    :ivar StructureType:
    :vartype StructureType: StructureType
    :ivar Fields:
    :vartype Fields: StructureField
    '''

    ua_types = [
        ('DefaultEncodingId', 'NodeId'),
        ('BaseDataType', 'NodeId'),
        ('StructureType', 'StructureType'),
        ('Fields', 'ListOfStructureField'),
               ]

    def __init__(self):
        self.DefaultEncodingId = NodeId()
        self.BaseDataType = NodeId()
        self.StructureType = StructureType(0)
        self.Fields = []
        self._freeze = True

    def __str__(self):
        return 'StructureDefinition(' + 'DefaultEncodingId:' + str(self.DefaultEncodingId) + ', ' + \
               'BaseDataType:' + str(self.BaseDataType) + ', ' + \
               'StructureType:' + str(self.StructureType) + ', ' + \
               'Fields:' + str(self.Fields) + ')'

    __repr__ = __str__


class EnumDefinition(FrozenClass):
    '''
    :ivar Fields:
    :vartype Fields: EnumField
    '''

    ua_types = [
        ('Fields', 'ListOfEnumField'),
               ]

    def __init__(self):
        self.Fields = []
        self._freeze = True

    def __str__(self):
        return 'EnumDefinition(' + 'Fields:' + str(self.Fields) + ')'

    __repr__ = __str__


class Argument(FrozenClass):
    '''
    An argument for a method.

    :ivar Name:
    :vartype Name: String
    :ivar DataType:
    :vartype DataType: NodeId
    :ivar ValueRank:
    :vartype ValueRank: Int32
    :ivar ArrayDimensions:
    :vartype ArrayDimensions: UInt32
    :ivar Description:
    :vartype Description: LocalizedText
    '''

    ua_types = [
        ('Name', 'String'),
        ('DataType', 'NodeId'),
        ('ValueRank', 'Int32'),
        ('ArrayDimensions', 'ListOfUInt32'),
        ('Description', 'LocalizedText'),
               ]

    def __init__(self):
        self.Name = None
        self.DataType = NodeId()
        self.ValueRank = 0
        self.ArrayDimensions = []
        self.Description = LocalizedText()
        self._freeze = True

    def __str__(self):
        return 'Argument(' + 'Name:' + str(self.Name) + ', ' + \
               'DataType:' + str(self.DataType) + ', ' + \
               'ValueRank:' + str(self.ValueRank) + ', ' + \
               'ArrayDimensions:' + str(self.ArrayDimensions) + ', ' + \
               'Description:' + str(self.Description) + ')'

    __repr__ = __str__


class EnumValueType(FrozenClass):
    '''
    A mapping between a value of an enumerated type and a name and description.

    :ivar Value:
    :vartype Value: Int64
    :ivar DisplayName:
    :vartype DisplayName: LocalizedText
    :ivar Description:
    :vartype Description: LocalizedText
    '''

    ua_types = [
        ('Value', 'Int64'),
        ('DisplayName', 'LocalizedText'),
        ('Description', 'LocalizedText'),
               ]

    def __init__(self):
        self.Value = 0
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self._freeze = True

    def __str__(self):
        return 'EnumValueType(' + 'Value:' + str(self.Value) + ', ' + \
               'DisplayName:' + str(self.DisplayName) + ', ' + \
               'Description:' + str(self.Description) + ')'

    __repr__ = __str__


class EnumField(FrozenClass):
    '''
    :ivar Value:
    :vartype Value: Int64
    :ivar DisplayName:
    :vartype DisplayName: LocalizedText
    :ivar Description:
    :vartype Description: LocalizedText
    :ivar Name:
    :vartype Name: String
    '''

    ua_types = [
        ('Value', 'Int64'),
        ('DisplayName', 'LocalizedText'),
        ('Description', 'LocalizedText'),
        ('Name', 'String'),
               ]

    def __init__(self):
        self.Value = 0
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.Name = None
        self._freeze = True

    def __str__(self):
        return 'EnumField(' + 'Value:' + str(self.Value) + ', ' + \
               'DisplayName:' + str(self.DisplayName) + ', ' + \
               'Description:' + str(self.Description) + ', ' + \
               'Name:' + str(self.Name) + ')'

    __repr__ = __str__


class OptionSet(FrozenClass):
    '''
    This abstract Structured DataType is the base DataType for all DataTypes representing a bit mask.

    :ivar Value:
    :vartype Value: ByteString
    :ivar ValidBits:
    :vartype ValidBits: ByteString
    '''

    ua_types = [
        ('Value', 'ByteString'),
        ('ValidBits', 'ByteString'),
               ]

    def __init__(self):
        self.Value = None
        self.ValidBits = None
        self._freeze = True

    def __str__(self):
        return 'OptionSet(' + 'Value:' + str(self.Value) + ', ' + \
               'ValidBits:' + str(self.ValidBits) + ')'

    __repr__ = __str__


class Union(FrozenClass):
    '''
    This abstract DataType is the base DataType for all union DataTypes.

    '''

    ua_types = [
               ]

    def __init__(self):
        self._freeze = True

    def __str__(self):
        return 'Union(' +  + ')'

    __repr__ = __str__


class TimeZoneDataType(FrozenClass):
    '''
    :ivar Offset:
    :vartype Offset: Int16
    :ivar DaylightSavingInOffset:
    :vartype DaylightSavingInOffset: Boolean
    '''

    ua_types = [
        ('Offset', 'Int16'),
        ('DaylightSavingInOffset', 'Boolean'),
               ]

    def __init__(self):
        self.Offset = 0
        self.DaylightSavingInOffset = True
        self._freeze = True

    def __str__(self):
        return 'TimeZoneDataType(' + 'Offset:' + str(self.Offset) + ', ' + \
               'DaylightSavingInOffset:' + str(self.DaylightSavingInOffset) + ')'

    __repr__ = __str__


class ApplicationDescription(FrozenClass):
    '''
    Describes an application and how to find it.

    :ivar ApplicationUri:
    :vartype ApplicationUri: String
    :ivar ProductUri:
    :vartype ProductUri: String
    :ivar ApplicationName:
    :vartype ApplicationName: LocalizedText
    :ivar ApplicationType:
    :vartype ApplicationType: ApplicationType
    :ivar GatewayServerUri:
    :vartype GatewayServerUri: String
    :ivar DiscoveryProfileUri:
    :vartype DiscoveryProfileUri: String
    :ivar DiscoveryUrls:
    :vartype DiscoveryUrls: String
    '''

    ua_types = [
        ('ApplicationUri', 'String'),
        ('ProductUri', 'String'),
        ('ApplicationName', 'LocalizedText'),
        ('ApplicationType', 'ApplicationType'),
        ('GatewayServerUri', 'String'),
        ('DiscoveryProfileUri', 'String'),
        ('DiscoveryUrls', 'ListOfString'),
               ]

    def __init__(self):
        self.ApplicationUri = None
        self.ProductUri = None
        self.ApplicationName = LocalizedText()
        self.ApplicationType = ApplicationType(0)
        self.GatewayServerUri = None
        self.DiscoveryProfileUri = None
        self.DiscoveryUrls = []
        self._freeze = True

    def __str__(self):
        return 'ApplicationDescription(' + 'ApplicationUri:' + str(self.ApplicationUri) + ', ' + \
               'ProductUri:' + str(self.ProductUri) + ', ' + \
               'ApplicationName:' + str(self.ApplicationName) + ', ' + \
               'ApplicationType:' + str(self.ApplicationType) + ', ' + \
               'GatewayServerUri:' + str(self.GatewayServerUri) + ', ' + \
               'DiscoveryProfileUri:' + str(self.DiscoveryProfileUri) + ', ' + \
               'DiscoveryUrls:' + str(self.DiscoveryUrls) + ')'

    __repr__ = __str__


class RequestHeader(FrozenClass):
    '''
    The header passed with every server request.

    :ivar AuthenticationToken:
    :vartype AuthenticationToken: NodeId
    :ivar Timestamp:
    :vartype Timestamp: DateTime
    :ivar RequestHandle:
    :vartype RequestHandle: UInt32
    :ivar ReturnDiagnostics:
    :vartype ReturnDiagnostics: UInt32
    :ivar AuditEntryId:
    :vartype AuditEntryId: String
    :ivar TimeoutHint:
    :vartype TimeoutHint: UInt32
    :ivar AdditionalHeader:
    :vartype AdditionalHeader: ExtensionObject
    '''

    ua_types = [
        ('AuthenticationToken', 'NodeId'),
        ('Timestamp', 'DateTime'),
        ('RequestHandle', 'UInt32'),
        ('ReturnDiagnostics', 'UInt32'),
        ('AuditEntryId', 'String'),
        ('TimeoutHint', 'UInt32'),
        ('AdditionalHeader', 'ExtensionObject'),
               ]

    def __init__(self):
        self.AuthenticationToken = NodeId()
        self.Timestamp = datetime.utcnow()
        self.RequestHandle = 0
        self.ReturnDiagnostics = 0
        self.AuditEntryId = None
        self.TimeoutHint = 0
        self.AdditionalHeader = ExtensionObject()
        self._freeze = True

    def __str__(self):
        return 'RequestHeader(' + 'AuthenticationToken:' + str(self.AuthenticationToken) + ', ' + \
               'Timestamp:' + str(self.Timestamp) + ', ' + \
               'RequestHandle:' + str(self.RequestHandle) + ', ' + \
               'ReturnDiagnostics:' + str(self.ReturnDiagnostics) + ', ' + \
               'AuditEntryId:' + str(self.AuditEntryId) + ', ' + \
               'TimeoutHint:' + str(self.TimeoutHint) + ', ' + \
               'AdditionalHeader:' + str(self.AdditionalHeader) + ')'

    __repr__ = __str__


class ResponseHeader(FrozenClass):
    '''
    The header passed with every server response.

    :ivar Timestamp:
    :vartype Timestamp: DateTime
    :ivar RequestHandle:
    :vartype RequestHandle: UInt32
    :ivar ServiceResult:
    :vartype ServiceResult: StatusCode
    :ivar ServiceDiagnostics:
    :vartype ServiceDiagnostics: DiagnosticInfo
    :ivar StringTable:
    :vartype StringTable: String
    :ivar AdditionalHeader:
    :vartype AdditionalHeader: ExtensionObject
    '''

    ua_types = [
        ('Timestamp', 'DateTime'),
        ('RequestHandle', 'UInt32'),
        ('ServiceResult', 'StatusCode'),
        ('ServiceDiagnostics', 'DiagnosticInfo'),
        ('StringTable', 'ListOfString'),
        ('AdditionalHeader', 'ExtensionObject'),
               ]

    def __init__(self):
        self.Timestamp = datetime.utcnow()
        self.RequestHandle = 0
        self.ServiceResult = StatusCode()
        self.ServiceDiagnostics = DiagnosticInfo()
        self.StringTable = []
        self.AdditionalHeader = ExtensionObject()
        self._freeze = True

    def __str__(self):
        return 'ResponseHeader(' + 'Timestamp:' + str(self.Timestamp) + ', ' + \
               'RequestHandle:' + str(self.RequestHandle) + ', ' + \
               'ServiceResult:' + str(self.ServiceResult) + ', ' + \
               'ServiceDiagnostics:' + str(self.ServiceDiagnostics) + ', ' + \
               'StringTable:' + str(self.StringTable) + ', ' + \
               'AdditionalHeader:' + str(self.AdditionalHeader) + ')'

    __repr__ = __str__


class ServiceFault(FrozenClass):
    '''
    The response returned by all services when there is a service level error.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('ResponseHeader', 'ResponseHeader'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.ServiceFault_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self._freeze = True

    def __str__(self):
        return 'ServiceFault(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'ResponseHeader:' + str(self.ResponseHeader) + ')'

    __repr__ = __str__


class SessionlessInvokeRequestType(FrozenClass):
    '''
    :ivar UrisVersion:
    :vartype UrisVersion: UInt32
    :ivar NamespaceUris:
    :vartype NamespaceUris: String
    :ivar ServerUris:
    :vartype ServerUris: String
    :ivar LocaleIds:
    :vartype LocaleIds: String
    :ivar ServiceId:
    :vartype ServiceId: UInt32
    '''

    ua_types = [
        ('UrisVersion', 'ListOfUInt32'),
        ('NamespaceUris', 'ListOfString'),
        ('ServerUris', 'ListOfString'),
        ('LocaleIds', 'ListOfString'),
        ('ServiceId', 'UInt32'),
               ]

    def __init__(self):
        self.UrisVersion = []
        self.NamespaceUris = []
        self.ServerUris = []
        self.LocaleIds = []
        self.ServiceId = 0
        self._freeze = True

    def __str__(self):
        return 'SessionlessInvokeRequestType(' + 'UrisVersion:' + str(self.UrisVersion) + ', ' + \
               'NamespaceUris:' + str(self.NamespaceUris) + ', ' + \
               'ServerUris:' + str(self.ServerUris) + ', ' + \
               'LocaleIds:' + str(self.LocaleIds) + ', ' + \
               'ServiceId:' + str(self.ServiceId) + ')'

    __repr__ = __str__


class SessionlessInvokeResponseType(FrozenClass):
    '''
    :ivar NamespaceUris:
    :vartype NamespaceUris: String
    :ivar ServerUris:
    :vartype ServerUris: String
    :ivar ServiceId:
    :vartype ServiceId: UInt32
    '''

    ua_types = [
        ('NamespaceUris', 'ListOfString'),
        ('ServerUris', 'ListOfString'),
        ('ServiceId', 'UInt32'),
               ]

    def __init__(self):
        self.NamespaceUris = []
        self.ServerUris = []
        self.ServiceId = 0
        self._freeze = True

    def __str__(self):
        return 'SessionlessInvokeResponseType(' + 'NamespaceUris:' + str(self.NamespaceUris) + ', ' + \
               'ServerUris:' + str(self.ServerUris) + ', ' + \
               'ServiceId:' + str(self.ServiceId) + ')'

    __repr__ = __str__


class FindServersParameters(FrozenClass):
    '''
    :ivar EndpointUrl:
    :vartype EndpointUrl: String
    :ivar LocaleIds:
    :vartype LocaleIds: String
    :ivar ServerUris:
    :vartype ServerUris: String
    '''

    ua_types = [
        ('EndpointUrl', 'String'),
        ('LocaleIds', 'ListOfString'),
        ('ServerUris', 'ListOfString'),
               ]

    def __init__(self):
        self.EndpointUrl = None
        self.LocaleIds = []
        self.ServerUris = []
        self._freeze = True

    def __str__(self):
        return 'FindServersParameters(' + 'EndpointUrl:' + str(self.EndpointUrl) + ', ' + \
               'LocaleIds:' + str(self.LocaleIds) + ', ' + \
               'ServerUris:' + str(self.ServerUris) + ')'

    __repr__ = __str__


class FindServersRequest(FrozenClass):
    '''
    Finds the servers known to the discovery server.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: FindServersParameters
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('RequestHeader', 'RequestHeader'),
        ('Parameters', 'FindServersParameters'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.FindServersRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = FindServersParameters()
        self._freeze = True

    def __str__(self):
        return 'FindServersRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'RequestHeader:' + str(self.RequestHeader) + ', ' + \
               'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class FindServersResponse(FrozenClass):
    '''
    Finds the servers known to the discovery server.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    :ivar Servers:
    :vartype Servers: ApplicationDescription
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('ResponseHeader', 'ResponseHeader'),
        ('Servers', 'ListOfApplicationDescription'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.FindServersResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Servers = []
        self._freeze = True

    def __str__(self):
        return 'FindServersResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
               'Servers:' + str(self.Servers) + ')'

    __repr__ = __str__


class ServerOnNetwork(FrozenClass):
    '''
    :ivar RecordId:
    :vartype RecordId: UInt32
    :ivar ServerName:
    :vartype ServerName: String
    :ivar DiscoveryUrl:
    :vartype DiscoveryUrl: String
    :ivar ServerCapabilities:
    :vartype ServerCapabilities: String
    '''

    ua_types = [
        ('RecordId', 'UInt32'),
        ('ServerName', 'String'),
        ('DiscoveryUrl', 'String'),
        ('ServerCapabilities', 'ListOfString'),
               ]

    def __init__(self):
        self.RecordId = 0
        self.ServerName = None
        self.DiscoveryUrl = None
        self.ServerCapabilities = []
        self._freeze = True

    def __str__(self):
        return 'ServerOnNetwork(' + 'RecordId:' + str(self.RecordId) + ', ' + \
               'ServerName:' + str(self.ServerName) + ', ' + \
               'DiscoveryUrl:' + str(self.DiscoveryUrl) + ', ' + \
               'ServerCapabilities:' + str(self.ServerCapabilities) + ')'

    __repr__ = __str__


class FindServersOnNetworkParameters(FrozenClass):
    '''
    :ivar StartingRecordId:
    :vartype StartingRecordId: UInt32
    :ivar MaxRecordsToReturn:
    :vartype MaxRecordsToReturn: UInt32
    :ivar ServerCapabilityFilter:
    :vartype ServerCapabilityFilter: String
    '''

    ua_types = [
        ('StartingRecordId', 'UInt32'),
        ('MaxRecordsToReturn', 'UInt32'),
        ('ServerCapabilityFilter', 'ListOfString'),
               ]

    def __init__(self):
        self.StartingRecordId = 0
        self.MaxRecordsToReturn = 0
        self.ServerCapabilityFilter = []
        self._freeze = True

    def __str__(self):
        return 'FindServersOnNetworkParameters(' + 'StartingRecordId:' + str(self.StartingRecordId) + ', ' + \
               'MaxRecordsToReturn:' + str(self.MaxRecordsToReturn) + ', ' + \
               'ServerCapabilityFilter:' + str(self.ServerCapabilityFilter) + ')'

    __repr__ = __str__


class FindServersOnNetworkRequest(FrozenClass):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: FindServersOnNetworkParameters
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('RequestHeader', 'RequestHeader'),
        ('Parameters', 'FindServersOnNetworkParameters'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.FindServersOnNetworkRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = FindServersOnNetworkParameters()
        self._freeze = True

    def __str__(self):
        return 'FindServersOnNetworkRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'RequestHeader:' + str(self.RequestHeader) + ', ' + \
               'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class FindServersOnNetworkResult(FrozenClass):
    '''
    :ivar LastCounterResetTime:
    :vartype LastCounterResetTime: DateTime
    :ivar Servers:
    :vartype Servers: ServerOnNetwork
    '''

    ua_types = [
        ('LastCounterResetTime', 'DateTime'),
        ('Servers', 'ListOfServerOnNetwork'),
               ]

    def __init__(self):
        self.LastCounterResetTime = datetime.utcnow()
        self.Servers = []
        self._freeze = True

    def __str__(self):
        return 'FindServersOnNetworkResult(' + 'LastCounterResetTime:' + str(self.LastCounterResetTime) + ', ' + \
               'Servers:' + str(self.Servers) + ')'

    __repr__ = __str__


class FindServersOnNetworkResponse(FrozenClass):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    :ivar Parameters:
    :vartype Parameters: FindServersOnNetworkResult
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('ResponseHeader', 'ResponseHeader'),
        ('Parameters', 'FindServersOnNetworkResult'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.FindServersOnNetworkResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = FindServersOnNetworkResult()
        self._freeze = True

    def __str__(self):
        return 'FindServersOnNetworkResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
               'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class UserTokenPolicy(FrozenClass):
    '''
    Describes a user token that can be used with a server.

    :ivar PolicyId:
    :vartype PolicyId: String
    :ivar TokenType:
    :vartype TokenType: UserTokenType
    :ivar IssuedTokenType:
    :vartype IssuedTokenType: String
    :ivar IssuerEndpointUrl:
    :vartype IssuerEndpointUrl: String
    :ivar SecurityPolicyUri:
    :vartype SecurityPolicyUri: String
    '''

    ua_types = [
        ('PolicyId', 'String'),
        ('TokenType', 'UserTokenType'),
        ('IssuedTokenType', 'String'),
        ('IssuerEndpointUrl', 'String'),
        ('SecurityPolicyUri', 'String'),
               ]

    def __init__(self):
        self.PolicyId = None
        self.TokenType = UserTokenType(0)
        self.IssuedTokenType = None
        self.IssuerEndpointUrl = None
        self.SecurityPolicyUri = None
        self._freeze = True

    def __str__(self):
        return 'UserTokenPolicy(' + 'PolicyId:' + str(self.PolicyId) + ', ' + \
               'TokenType:' + str(self.TokenType) + ', ' + \
               'IssuedTokenType:' + str(self.IssuedTokenType) + ', ' + \
               'IssuerEndpointUrl:' + str(self.IssuerEndpointUrl) + ', ' + \
               'SecurityPolicyUri:' + str(self.SecurityPolicyUri) + ')'

    __repr__ = __str__


class EndpointDescription(FrozenClass):
    '''
    The description of a endpoint that can be used to access a server.

    :ivar EndpointUrl:
    :vartype EndpointUrl: String
    :ivar Server:
    :vartype Server: ApplicationDescription
    :ivar ServerCertificate:
    :vartype ServerCertificate: ByteString
    :ivar SecurityMode:
    :vartype SecurityMode: MessageSecurityMode
    :ivar SecurityPolicyUri:
    :vartype SecurityPolicyUri: String
    :ivar UserIdentityTokens:
    :vartype UserIdentityTokens: UserTokenPolicy
    :ivar TransportProfileUri:
    :vartype TransportProfileUri: String
    :ivar SecurityLevel:
    :vartype SecurityLevel: Byte
    '''

    ua_types = [
        ('EndpointUrl', 'String'),
        ('Server', 'ApplicationDescription'),
        ('ServerCertificate', 'ByteString'),
        ('SecurityMode', 'MessageSecurityMode'),
        ('SecurityPolicyUri', 'String'),
        ('UserIdentityTokens', 'ListOfUserTokenPolicy'),
        ('TransportProfileUri', 'String'),
        ('SecurityLevel', 'Byte'),
               ]

    def __init__(self):
        self.EndpointUrl = None
        self.Server = ApplicationDescription()
        self.ServerCertificate = None
        self.SecurityMode = MessageSecurityMode(0)
        self.SecurityPolicyUri = None
        self.UserIdentityTokens = []
        self.TransportProfileUri = None
        self.SecurityLevel = 0
        self._freeze = True

    def __str__(self):
        return 'EndpointDescription(' + 'EndpointUrl:' + str(self.EndpointUrl) + ', ' + \
               'Server:' + str(self.Server) + ', ' + \
               'ServerCertificate:' + str(self.ServerCertificate) + ', ' + \
               'SecurityMode:' + str(self.SecurityMode) + ', ' + \
               'SecurityPolicyUri:' + str(self.SecurityPolicyUri) + ', ' + \
               'UserIdentityTokens:' + str(self.UserIdentityTokens) + ', ' + \
               'TransportProfileUri:' + str(self.TransportProfileUri) + ', ' + \
               'SecurityLevel:' + str(self.SecurityLevel) + ')'

    __repr__ = __str__


class GetEndpointsParameters(FrozenClass):
    '''
    :ivar EndpointUrl:
    :vartype EndpointUrl: String
    :ivar LocaleIds:
    :vartype LocaleIds: String
    :ivar ProfileUris:
    :vartype ProfileUris: String
    '''

    ua_types = [
        ('EndpointUrl', 'String'),
        ('LocaleIds', 'ListOfString'),
        ('ProfileUris', 'ListOfString'),
               ]

    def __init__(self):
        self.EndpointUrl = None
        self.LocaleIds = []
        self.ProfileUris = []
        self._freeze = True

    def __str__(self):
        return 'GetEndpointsParameters(' + 'EndpointUrl:' + str(self.EndpointUrl) + ', ' + \
               'LocaleIds:' + str(self.LocaleIds) + ', ' + \
               'ProfileUris:' + str(self.ProfileUris) + ')'

    __repr__ = __str__


class GetEndpointsRequest(FrozenClass):
    '''
    Gets the endpoints used by the server.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: GetEndpointsParameters
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('RequestHeader', 'RequestHeader'),
        ('Parameters', 'GetEndpointsParameters'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.GetEndpointsRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = GetEndpointsParameters()
        self._freeze = True

    def __str__(self):
        return 'GetEndpointsRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'RequestHeader:' + str(self.RequestHeader) + ', ' + \
               'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class GetEndpointsResponse(FrozenClass):
    '''
    Gets the endpoints used by the server.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    :ivar Endpoints:
    :vartype Endpoints: EndpointDescription
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('ResponseHeader', 'ResponseHeader'),
        ('Endpoints', 'ListOfEndpointDescription'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.GetEndpointsResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Endpoints = []
        self._freeze = True

    def __str__(self):
        return 'GetEndpointsResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
               'Endpoints:' + str(self.Endpoints) + ')'

    __repr__ = __str__


class RegisteredServer(FrozenClass):
    '''
    The information required to register a server with a discovery server.

    :ivar ServerUri:
    :vartype ServerUri: String
    :ivar ProductUri:
    :vartype ProductUri: String
    :ivar ServerNames:
    :vartype ServerNames: LocalizedText
    :ivar ServerType:
    :vartype ServerType: ApplicationType
    :ivar GatewayServerUri:
    :vartype GatewayServerUri: String
    :ivar DiscoveryUrls:
    :vartype DiscoveryUrls: String
    :ivar SemaphoreFilePath:
    :vartype SemaphoreFilePath: String
    :ivar IsOnline:
    :vartype IsOnline: Boolean
    '''

    ua_types = [
        ('ServerUri', 'String'),
        ('ProductUri', 'String'),
        ('ServerNames', 'ListOfLocalizedText'),
        ('ServerType', 'ApplicationType'),
        ('GatewayServerUri', 'String'),
        ('DiscoveryUrls', 'ListOfString'),
        ('SemaphoreFilePath', 'String'),
        ('IsOnline', 'Boolean'),
               ]

    def __init__(self):
        self.ServerUri = None
        self.ProductUri = None
        self.ServerNames = []
        self.ServerType = ApplicationType(0)
        self.GatewayServerUri = None
        self.DiscoveryUrls = []
        self.SemaphoreFilePath = None
        self.IsOnline = True
        self._freeze = True

    def __str__(self):
        return 'RegisteredServer(' + 'ServerUri:' + str(self.ServerUri) + ', ' + \
               'ProductUri:' + str(self.ProductUri) + ', ' + \
               'ServerNames:' + str(self.ServerNames) + ', ' + \
               'ServerType:' + str(self.ServerType) + ', ' + \
               'GatewayServerUri:' + str(self.GatewayServerUri) + ', ' + \
               'DiscoveryUrls:' + str(self.DiscoveryUrls) + ', ' + \
               'SemaphoreFilePath:' + str(self.SemaphoreFilePath) + ', ' + \
               'IsOnline:' + str(self.IsOnline) + ')'

    __repr__ = __str__


class RegisterServerRequest(FrozenClass):
    '''
    Registers a server with the discovery server.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Server:
    :vartype Server: RegisteredServer
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('RequestHeader', 'RequestHeader'),
        ('Server', 'RegisteredServer'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.RegisterServerRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Server = RegisteredServer()
        self._freeze = True

    def __str__(self):
        return 'RegisterServerRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'RequestHeader:' + str(self.RequestHeader) + ', ' + \
               'Server:' + str(self.Server) + ')'

    __repr__ = __str__


class RegisterServerResponse(FrozenClass):
    '''
    Registers a server with the discovery server.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('ResponseHeader', 'ResponseHeader'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.RegisterServerResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self._freeze = True

    def __str__(self):
        return 'RegisterServerResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'ResponseHeader:' + str(self.ResponseHeader) + ')'

    __repr__ = __str__


class DiscoveryConfiguration(FrozenClass):
    '''
    A base type for discovery configuration information.

    '''

    ua_types = [
               ]

    def __init__(self):
        self._freeze = True

    def __str__(self):
        return 'DiscoveryConfiguration(' +  + ')'

    __repr__ = __str__


class MdnsDiscoveryConfiguration(FrozenClass):
    '''
    The discovery information needed for mDNS registration.

    :ivar MdnsServerName:
    :vartype MdnsServerName: String
    :ivar ServerCapabilities:
    :vartype ServerCapabilities: String
    '''

    ua_types = [
        ('MdnsServerName', 'String'),
        ('ServerCapabilities', 'ListOfString'),
               ]

    def __init__(self):
        self.MdnsServerName = None
        self.ServerCapabilities = []
        self._freeze = True

    def __str__(self):
        return 'MdnsDiscoveryConfiguration(' + 'MdnsServerName:' + str(self.MdnsServerName) + ', ' + \
               'ServerCapabilities:' + str(self.ServerCapabilities) + ')'

    __repr__ = __str__


class RegisterServer2Parameters(FrozenClass):
    '''
    :ivar Server:
    :vartype Server: RegisteredServer
    :ivar DiscoveryConfiguration:
    :vartype DiscoveryConfiguration: ExtensionObject
    '''

    ua_types = [
        ('Server', 'RegisteredServer'),
        ('DiscoveryConfiguration', 'ListOfExtensionObject'),
               ]

    def __init__(self):
        self.Server = RegisteredServer()
        self.DiscoveryConfiguration = []
        self._freeze = True

    def __str__(self):
        return 'RegisterServer2Parameters(' + 'Server:' + str(self.Server) + ', ' + \
               'DiscoveryConfiguration:' + str(self.DiscoveryConfiguration) + ')'

    __repr__ = __str__


class RegisterServer2Request(FrozenClass):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: RegisterServer2Parameters
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('RequestHeader', 'RequestHeader'),
        ('Parameters', 'RegisterServer2Parameters'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.RegisterServer2Request_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = RegisterServer2Parameters()
        self._freeze = True

    def __str__(self):
        return 'RegisterServer2Request(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'RequestHeader:' + str(self.RequestHeader) + ', ' + \
               'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class RegisterServer2Response(FrozenClass):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    :ivar ConfigurationResults:
    :vartype ConfigurationResults: StatusCode
    :ivar DiagnosticInfos:
    :vartype DiagnosticInfos: DiagnosticInfo
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('ResponseHeader', 'ResponseHeader'),
        ('ConfigurationResults', 'ListOfStatusCode'),
        ('DiagnosticInfos', 'ListOfDiagnosticInfo'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.RegisterServer2Response_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.ConfigurationResults = []
        self.DiagnosticInfos = []
        self._freeze = True

    def __str__(self):
        return 'RegisterServer2Response(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
               'ConfigurationResults:' + str(self.ConfigurationResults) + ', ' + \
               'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'

    __repr__ = __str__


class ChannelSecurityToken(FrozenClass):
    '''
    The token that identifies a set of keys for an active secure channel.

    :ivar ChannelId:
    :vartype ChannelId: UInt32
    :ivar TokenId:
    :vartype TokenId: UInt32
    :ivar CreatedAt:
    :vartype CreatedAt: DateTime
    :ivar RevisedLifetime:
    :vartype RevisedLifetime: UInt32
    '''

    ua_types = [
        ('ChannelId', 'UInt32'),
        ('TokenId', 'UInt32'),
        ('CreatedAt', 'DateTime'),
        ('RevisedLifetime', 'UInt32'),
               ]

    def __init__(self):
        self.ChannelId = 0
        self.TokenId = 0
        self.CreatedAt = datetime.utcnow()
        self.RevisedLifetime = 0
        self._freeze = True

    def __str__(self):
        return 'ChannelSecurityToken(' + 'ChannelId:' + str(self.ChannelId) + ', ' + \
               'TokenId:' + str(self.TokenId) + ', ' + \
               'CreatedAt:' + str(self.CreatedAt) + ', ' + \
               'RevisedLifetime:' + str(self.RevisedLifetime) + ')'

    __repr__ = __str__


class OpenSecureChannelParameters(FrozenClass):
    '''
    :ivar ClientProtocolVersion:
    :vartype ClientProtocolVersion: UInt32
    :ivar RequestType:
    :vartype RequestType: SecurityTokenRequestType
    :ivar SecurityMode:
    :vartype SecurityMode: MessageSecurityMode
    :ivar ClientNonce:
    :vartype ClientNonce: ByteString
    :ivar RequestedLifetime:
    :vartype RequestedLifetime: UInt32
    '''

    ua_types = [
        ('ClientProtocolVersion', 'UInt32'),
        ('RequestType', 'SecurityTokenRequestType'),
        ('SecurityMode', 'MessageSecurityMode'),
        ('ClientNonce', 'ByteString'),
        ('RequestedLifetime', 'UInt32'),
               ]

    def __init__(self):
        self.ClientProtocolVersion = 0
        self.RequestType = SecurityTokenRequestType(0)
        self.SecurityMode = MessageSecurityMode(0)
        self.ClientNonce = None
        self.RequestedLifetime = 0
        self._freeze = True

    def __str__(self):
        return 'OpenSecureChannelParameters(' + 'ClientProtocolVersion:' + str(self.ClientProtocolVersion) + ', ' + \
               'RequestType:' + str(self.RequestType) + ', ' + \
               'SecurityMode:' + str(self.SecurityMode) + ', ' + \
               'ClientNonce:' + str(self.ClientNonce) + ', ' + \
               'RequestedLifetime:' + str(self.RequestedLifetime) + ')'

    __repr__ = __str__


class OpenSecureChannelRequest(FrozenClass):
    '''
    Creates a secure channel with a server.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: OpenSecureChannelParameters
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('RequestHeader', 'RequestHeader'),
        ('Parameters', 'OpenSecureChannelParameters'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.OpenSecureChannelRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = OpenSecureChannelParameters()
        self._freeze = True

    def __str__(self):
        return 'OpenSecureChannelRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'RequestHeader:' + str(self.RequestHeader) + ', ' + \
               'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class OpenSecureChannelResult(FrozenClass):
    '''
    :ivar ServerProtocolVersion:
    :vartype ServerProtocolVersion: UInt32
    :ivar SecurityToken:
    :vartype SecurityToken: ChannelSecurityToken
    :ivar ServerNonce:
    :vartype ServerNonce: ByteString
    '''

    ua_types = [
        ('ServerProtocolVersion', 'UInt32'),
        ('SecurityToken', 'ChannelSecurityToken'),
        ('ServerNonce', 'ByteString'),
               ]

    def __init__(self):
        self.ServerProtocolVersion = 0
        self.SecurityToken = ChannelSecurityToken()
        self.ServerNonce = None
        self._freeze = True

    def __str__(self):
        return 'OpenSecureChannelResult(' + 'ServerProtocolVersion:' + str(self.ServerProtocolVersion) + ', ' + \
               'SecurityToken:' + str(self.SecurityToken) + ', ' + \
               'ServerNonce:' + str(self.ServerNonce) + ')'

    __repr__ = __str__


class OpenSecureChannelResponse(FrozenClass):
    '''
    Creates a secure channel with a server.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    :ivar Parameters:
    :vartype Parameters: OpenSecureChannelResult
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('ResponseHeader', 'ResponseHeader'),
        ('Parameters', 'OpenSecureChannelResult'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.OpenSecureChannelResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = OpenSecureChannelResult()
        self._freeze = True

    def __str__(self):
        return 'OpenSecureChannelResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
               'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class CloseSecureChannelRequest(FrozenClass):
    '''
    Closes a secure channel.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('RequestHeader', 'RequestHeader'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.CloseSecureChannelRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self._freeze = True

    def __str__(self):
        return 'CloseSecureChannelRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'RequestHeader:' + str(self.RequestHeader) + ')'

    __repr__ = __str__


class CloseSecureChannelResponse(FrozenClass):
    '''
    Closes a secure channel.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('ResponseHeader', 'ResponseHeader'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.CloseSecureChannelResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self._freeze = True

    def __str__(self):
        return 'CloseSecureChannelResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'ResponseHeader:' + str(self.ResponseHeader) + ')'

    __repr__ = __str__


class SignedSoftwareCertificate(FrozenClass):
    '''
    A software certificate with a digital signature.

    :ivar CertificateData:
    :vartype CertificateData: ByteString
    :ivar Signature:
    :vartype Signature: ByteString
    '''

    ua_types = [
        ('CertificateData', 'ByteString'),
        ('Signature', 'ByteString'),
               ]

    def __init__(self):
        self.CertificateData = None
        self.Signature = None
        self._freeze = True

    def __str__(self):
        return 'SignedSoftwareCertificate(' + 'CertificateData:' + str(self.CertificateData) + ', ' + \
               'Signature:' + str(self.Signature) + ')'

    __repr__ = __str__


class SignatureData(FrozenClass):
    '''
    A digital signature.

    :ivar Algorithm:
    :vartype Algorithm: String
    :ivar Signature:
    :vartype Signature: ByteString
    '''

    ua_types = [
        ('Algorithm', 'String'),
        ('Signature', 'ByteString'),
               ]

    def __init__(self):
        self.Algorithm = None
        self.Signature = None
        self._freeze = True

    def __str__(self):
        return 'SignatureData(' + 'Algorithm:' + str(self.Algorithm) + ', ' + \
               'Signature:' + str(self.Signature) + ')'

    __repr__ = __str__


class CreateSessionParameters(FrozenClass):
    '''
    :ivar ClientDescription:
    :vartype ClientDescription: ApplicationDescription
    :ivar ServerUri:
    :vartype ServerUri: String
    :ivar EndpointUrl:
    :vartype EndpointUrl: String
    :ivar SessionName:
    :vartype SessionName: String
    :ivar ClientNonce:
    :vartype ClientNonce: ByteString
    :ivar ClientCertificate:
    :vartype ClientCertificate: ByteString
    :ivar RequestedSessionTimeout:
    :vartype RequestedSessionTimeout: Double
    :ivar MaxResponseMessageSize:
    :vartype MaxResponseMessageSize: UInt32
    '''

    ua_types = [
        ('ClientDescription', 'ApplicationDescription'),
        ('ServerUri', 'String'),
        ('EndpointUrl', 'String'),
        ('SessionName', 'String'),
        ('ClientNonce', 'ByteString'),
        ('ClientCertificate', 'ByteString'),
        ('RequestedSessionTimeout', 'Double'),
        ('MaxResponseMessageSize', 'UInt32'),
               ]

    def __init__(self):
        self.ClientDescription = ApplicationDescription()
        self.ServerUri = None
        self.EndpointUrl = None
        self.SessionName = None
        self.ClientNonce = None
        self.ClientCertificate = None
        self.RequestedSessionTimeout = 0
        self.MaxResponseMessageSize = 0
        self._freeze = True

    def __str__(self):
        return 'CreateSessionParameters(' + 'ClientDescription:' + str(self.ClientDescription) + ', ' + \
               'ServerUri:' + str(self.ServerUri) + ', ' + \
               'EndpointUrl:' + str(self.EndpointUrl) + ', ' + \
               'SessionName:' + str(self.SessionName) + ', ' + \
               'ClientNonce:' + str(self.ClientNonce) + ', ' + \
               'ClientCertificate:' + str(self.ClientCertificate) + ', ' + \
               'RequestedSessionTimeout:' + str(self.RequestedSessionTimeout) + ', ' + \
               'MaxResponseMessageSize:' + str(self.MaxResponseMessageSize) + ')'

    __repr__ = __str__


class CreateSessionRequest(FrozenClass):
    '''
    Creates a new session with the server.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: CreateSessionParameters
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('RequestHeader', 'RequestHeader'),
        ('Parameters', 'CreateSessionParameters'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.CreateSessionRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = CreateSessionParameters()
        self._freeze = True

    def __str__(self):
        return 'CreateSessionRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'RequestHeader:' + str(self.RequestHeader) + ', ' + \
               'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class CreateSessionResult(FrozenClass):
    '''
    :ivar SessionId:
    :vartype SessionId: NodeId
    :ivar AuthenticationToken:
    :vartype AuthenticationToken: NodeId
    :ivar RevisedSessionTimeout:
    :vartype RevisedSessionTimeout: Double
    :ivar ServerNonce:
    :vartype ServerNonce: ByteString
    :ivar ServerCertificate:
    :vartype ServerCertificate: ByteString
    :ivar ServerEndpoints:
    :vartype ServerEndpoints: EndpointDescription
    :ivar ServerSoftwareCertificates:
    :vartype ServerSoftwareCertificates: SignedSoftwareCertificate
    :ivar ServerSignature:
    :vartype ServerSignature: SignatureData
    :ivar MaxRequestMessageSize:
    :vartype MaxRequestMessageSize: UInt32
    '''

    ua_types = [
        ('SessionId', 'NodeId'),
        ('AuthenticationToken', 'NodeId'),
        ('RevisedSessionTimeout', 'Double'),
        ('ServerNonce', 'ByteString'),
        ('ServerCertificate', 'ByteString'),
        ('ServerEndpoints', 'ListOfEndpointDescription'),
        ('ServerSoftwareCertificates', 'ListOfSignedSoftwareCertificate'),
        ('ServerSignature', 'SignatureData'),
        ('MaxRequestMessageSize', 'UInt32'),
               ]

    def __init__(self):
        self.SessionId = NodeId()
        self.AuthenticationToken = NodeId()
        self.RevisedSessionTimeout = 0
        self.ServerNonce = None
        self.ServerCertificate = None
        self.ServerEndpoints = []
        self.ServerSoftwareCertificates = []
        self.ServerSignature = SignatureData()
        self.MaxRequestMessageSize = 0
        self._freeze = True

    def __str__(self):
        return 'CreateSessionResult(' + 'SessionId:' + str(self.SessionId) + ', ' + \
               'AuthenticationToken:' + str(self.AuthenticationToken) + ', ' + \
               'RevisedSessionTimeout:' + str(self.RevisedSessionTimeout) + ', ' + \
               'ServerNonce:' + str(self.ServerNonce) + ', ' + \
               'ServerCertificate:' + str(self.ServerCertificate) + ', ' + \
               'ServerEndpoints:' + str(self.ServerEndpoints) + ', ' + \
               'ServerSoftwareCertificates:' + str(self.ServerSoftwareCertificates) + ', ' + \
               'ServerSignature:' + str(self.ServerSignature) + ', ' + \
               'MaxRequestMessageSize:' + str(self.MaxRequestMessageSize) + ')'

    __repr__ = __str__


class CreateSessionResponse(FrozenClass):
    '''
    Creates a new session with the server.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    :ivar Parameters:
    :vartype Parameters: CreateSessionResult
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('ResponseHeader', 'ResponseHeader'),
        ('Parameters', 'CreateSessionResult'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.CreateSessionResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = CreateSessionResult()
        self._freeze = True

    def __str__(self):
        return 'CreateSessionResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
               'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class UserIdentityToken(FrozenClass):
    '''
    A base type for a user identity token.

    :ivar PolicyId:
    :vartype PolicyId: String
    '''

    ua_types = [
        ('PolicyId', 'String'),
               ]

    def __init__(self):
        self.PolicyId = None
        self._freeze = True

    def __str__(self):
        return 'UserIdentityToken(' + 'PolicyId:' + str(self.PolicyId) + ')'

    __repr__ = __str__


class AnonymousIdentityToken(FrozenClass):
    '''
    A token representing an anonymous user.

    :ivar PolicyId:
    :vartype PolicyId: String
    '''

    ua_types = [
        ('PolicyId', 'String'),
               ]

    def __init__(self):
        self.PolicyId = None
        self._freeze = True

    def __str__(self):
        return 'AnonymousIdentityToken(' + 'PolicyId:' + str(self.PolicyId) + ')'

    __repr__ = __str__


class UserNameIdentityToken(FrozenClass):
    '''
    A token representing a user identified by a user name and password.

    :ivar PolicyId:
    :vartype PolicyId: String
    :ivar UserName:
    :vartype UserName: String
    :ivar Password:
    :vartype Password: ByteString
    :ivar EncryptionAlgorithm:
    :vartype EncryptionAlgorithm: String
    '''

    ua_types = [
        ('PolicyId', 'String'),
        ('UserName', 'String'),
        ('Password', 'ByteString'),
        ('EncryptionAlgorithm', 'String'),
               ]

    def __init__(self):
        self.PolicyId = None
        self.UserName = None
        self.Password = None
        self.EncryptionAlgorithm = None
        self._freeze = True

    def __str__(self):
        return 'UserNameIdentityToken(' + 'PolicyId:' + str(self.PolicyId) + ', ' + \
               'UserName:' + str(self.UserName) + ', ' + \
               'Password:' + str(self.Password) + ', ' + \
               'EncryptionAlgorithm:' + str(self.EncryptionAlgorithm) + ')'

    __repr__ = __str__


class X509IdentityToken(FrozenClass):
    '''
    A token representing a user identified by an X509 certificate.

    :ivar PolicyId:
    :vartype PolicyId: String
    :ivar CertificateData:
    :vartype CertificateData: ByteString
    '''

    ua_types = [
        ('PolicyId', 'String'),
        ('CertificateData', 'ByteString'),
               ]

    def __init__(self):
        self.PolicyId = None
        self.CertificateData = None
        self._freeze = True

    def __str__(self):
        return 'X509IdentityToken(' + 'PolicyId:' + str(self.PolicyId) + ', ' + \
               'CertificateData:' + str(self.CertificateData) + ')'

    __repr__ = __str__


class IssuedIdentityToken(FrozenClass):
    '''
    A token representing a user identified by a WS-Security XML token.

    :ivar PolicyId:
    :vartype PolicyId: String
    :ivar TokenData:
    :vartype TokenData: ByteString
    :ivar EncryptionAlgorithm:
    :vartype EncryptionAlgorithm: String
    '''

    ua_types = [
        ('PolicyId', 'String'),
        ('TokenData', 'ByteString'),
        ('EncryptionAlgorithm', 'String'),
               ]

    def __init__(self):
        self.PolicyId = None
        self.TokenData = None
        self.EncryptionAlgorithm = None
        self._freeze = True

    def __str__(self):
        return 'IssuedIdentityToken(' + 'PolicyId:' + str(self.PolicyId) + ', ' + \
               'TokenData:' + str(self.TokenData) + ', ' + \
               'EncryptionAlgorithm:' + str(self.EncryptionAlgorithm) + ')'

    __repr__ = __str__


class ActivateSessionParameters(FrozenClass):
    '''
    :ivar ClientSignature:
    :vartype ClientSignature: SignatureData
    :ivar ClientSoftwareCertificates:
    :vartype ClientSoftwareCertificates: SignedSoftwareCertificate
    :ivar LocaleIds:
    :vartype LocaleIds: String
    :ivar UserIdentityToken:
    :vartype UserIdentityToken: ExtensionObject
    :ivar UserTokenSignature:
    :vartype UserTokenSignature: SignatureData
    '''

    ua_types = [
        ('ClientSignature', 'SignatureData'),
        ('ClientSoftwareCertificates', 'ListOfSignedSoftwareCertificate'),
        ('LocaleIds', 'ListOfString'),
        ('UserIdentityToken', 'ExtensionObject'),
        ('UserTokenSignature', 'SignatureData'),
               ]

    def __init__(self):
        self.ClientSignature = SignatureData()
        self.ClientSoftwareCertificates = []
        self.LocaleIds = []
        self.UserIdentityToken = ExtensionObject()
        self.UserTokenSignature = SignatureData()
        self._freeze = True

    def __str__(self):
        return 'ActivateSessionParameters(' + 'ClientSignature:' + str(self.ClientSignature) + ', ' + \
               'ClientSoftwareCertificates:' + str(self.ClientSoftwareCertificates) + ', ' + \
               'LocaleIds:' + str(self.LocaleIds) + ', ' + \
               'UserIdentityToken:' + str(self.UserIdentityToken) + ', ' + \
               'UserTokenSignature:' + str(self.UserTokenSignature) + ')'

    __repr__ = __str__


class ActivateSessionRequest(FrozenClass):
    '''
    Activates a session with the server.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: ActivateSessionParameters
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('RequestHeader', 'RequestHeader'),
        ('Parameters', 'ActivateSessionParameters'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.ActivateSessionRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = ActivateSessionParameters()
        self._freeze = True

    def __str__(self):
        return 'ActivateSessionRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'RequestHeader:' + str(self.RequestHeader) + ', ' + \
               'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class ActivateSessionResult(FrozenClass):
    '''
    :ivar ServerNonce:
    :vartype ServerNonce: ByteString
    :ivar Results:
    :vartype Results: StatusCode
    :ivar DiagnosticInfos:
    :vartype DiagnosticInfos: DiagnosticInfo
    '''

    ua_types = [
        ('ServerNonce', 'ByteString'),
        ('Results', 'ListOfStatusCode'),
        ('DiagnosticInfos', 'ListOfDiagnosticInfo'),
               ]

    def __init__(self):
        self.ServerNonce = None
        self.Results = []
        self.DiagnosticInfos = []
        self._freeze = True

    def __str__(self):
        return 'ActivateSessionResult(' + 'ServerNonce:' + str(self.ServerNonce) + ', ' + \
               'Results:' + str(self.Results) + ', ' + \
               'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'

    __repr__ = __str__


class ActivateSessionResponse(FrozenClass):
    '''
    Activates a session with the server.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    :ivar Parameters:
    :vartype Parameters: ActivateSessionResult
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('ResponseHeader', 'ResponseHeader'),
        ('Parameters', 'ActivateSessionResult'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.ActivateSessionResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = ActivateSessionResult()
        self._freeze = True

    def __str__(self):
        return 'ActivateSessionResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
               'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class CloseSessionRequest(FrozenClass):
    '''
    Closes a session with the server.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar DeleteSubscriptions:
    :vartype DeleteSubscriptions: Boolean
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('RequestHeader', 'RequestHeader'),
        ('DeleteSubscriptions', 'Boolean'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.CloseSessionRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.DeleteSubscriptions = True
        self._freeze = True

    def __str__(self):
        return 'CloseSessionRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'RequestHeader:' + str(self.RequestHeader) + ', ' + \
               'DeleteSubscriptions:' + str(self.DeleteSubscriptions) + ')'

    __repr__ = __str__


class CloseSessionResponse(FrozenClass):
    '''
    Closes a session with the server.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('ResponseHeader', 'ResponseHeader'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.CloseSessionResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self._freeze = True

    def __str__(self):
        return 'CloseSessionResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'ResponseHeader:' + str(self.ResponseHeader) + ')'

    __repr__ = __str__


class CancelParameters(FrozenClass):
    '''
    :ivar RequestHandle:
    :vartype RequestHandle: UInt32
    '''

    ua_types = [
        ('RequestHandle', 'UInt32'),
               ]

    def __init__(self):
        self.RequestHandle = 0
        self._freeze = True

    def __str__(self):
        return 'CancelParameters(' + 'RequestHandle:' + str(self.RequestHandle) + ')'

    __repr__ = __str__


class CancelRequest(FrozenClass):
    '''
    Cancels an outstanding request.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: CancelParameters
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('RequestHeader', 'RequestHeader'),
        ('Parameters', 'CancelParameters'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.CancelRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = CancelParameters()
        self._freeze = True

    def __str__(self):
        return 'CancelRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'RequestHeader:' + str(self.RequestHeader) + ', ' + \
               'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class CancelResult(FrozenClass):
    '''
    :ivar CancelCount:
    :vartype CancelCount: UInt32
    '''

    ua_types = [
        ('CancelCount', 'UInt32'),
               ]

    def __init__(self):
        self.CancelCount = 0
        self._freeze = True

    def __str__(self):
        return 'CancelResult(' + 'CancelCount:' + str(self.CancelCount) + ')'

    __repr__ = __str__


class CancelResponse(FrozenClass):
    '''
    Cancels an outstanding request.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    :ivar Parameters:
    :vartype Parameters: CancelResult
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('ResponseHeader', 'ResponseHeader'),
        ('Parameters', 'CancelResult'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.CancelResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = CancelResult()
        self._freeze = True

    def __str__(self):
        return 'CancelResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
               'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class NodeAttributes(FrozenClass):
    '''
    The base attributes for all nodes.

    :ivar SpecifiedAttributes:
    :vartype SpecifiedAttributes: UInt32
    :ivar DisplayName:
    :vartype DisplayName: LocalizedText
    :ivar Description:
    :vartype Description: LocalizedText
    :ivar WriteMask:
    :vartype WriteMask: UInt32
    :ivar UserWriteMask:
    :vartype UserWriteMask: UInt32
    '''

    ua_types = [
        ('SpecifiedAttributes', 'UInt32'),
        ('DisplayName', 'LocalizedText'),
        ('Description', 'LocalizedText'),
        ('WriteMask', 'UInt32'),
        ('UserWriteMask', 'UInt32'),
               ]

    def __init__(self):
        self.SpecifiedAttributes = 0
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self.UserWriteMask = 0
        self._freeze = True

    def __str__(self):
        return 'NodeAttributes(' + 'SpecifiedAttributes:' + str(self.SpecifiedAttributes) + ', ' + \
               'DisplayName:' + str(self.DisplayName) + ', ' + \
               'Description:' + str(self.Description) + ', ' + \
               'WriteMask:' + str(self.WriteMask) + ', ' + \
               'UserWriteMask:' + str(self.UserWriteMask) + ')'

    __repr__ = __str__


class ObjectAttributes(FrozenClass):
    '''
    The attributes for an object node.

    :ivar SpecifiedAttributes:
    :vartype SpecifiedAttributes: UInt32
    :ivar DisplayName:
    :vartype DisplayName: LocalizedText
    :ivar Description:
    :vartype Description: LocalizedText
    :ivar WriteMask:
    :vartype WriteMask: UInt32
    :ivar UserWriteMask:
    :vartype UserWriteMask: UInt32
    :ivar EventNotifier:
    :vartype EventNotifier: Byte
    '''

    ua_types = [
        ('SpecifiedAttributes', 'UInt32'),
        ('DisplayName', 'LocalizedText'),
        ('Description', 'LocalizedText'),
        ('WriteMask', 'UInt32'),
        ('UserWriteMask', 'UInt32'),
        ('EventNotifier', 'Byte'),
               ]

    def __init__(self):
        self.SpecifiedAttributes = 0
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self.UserWriteMask = 0
        self.EventNotifier = 0
        self._freeze = True

    def __str__(self):
        return 'ObjectAttributes(' + 'SpecifiedAttributes:' + str(self.SpecifiedAttributes) + ', ' + \
               'DisplayName:' + str(self.DisplayName) + ', ' + \
               'Description:' + str(self.Description) + ', ' + \
               'WriteMask:' + str(self.WriteMask) + ', ' + \
               'UserWriteMask:' + str(self.UserWriteMask) + ', ' + \
               'EventNotifier:' + str(self.EventNotifier) + ')'

    __repr__ = __str__


class VariableAttributes(FrozenClass):
    '''
    The attributes for a variable node.

    :ivar SpecifiedAttributes:
    :vartype SpecifiedAttributes: UInt32
    :ivar DisplayName:
    :vartype DisplayName: LocalizedText
    :ivar Description:
    :vartype Description: LocalizedText
    :ivar WriteMask:
    :vartype WriteMask: UInt32
    :ivar UserWriteMask:
    :vartype UserWriteMask: UInt32
    :ivar Value:
    :vartype Value: Variant
    :ivar DataType:
    :vartype DataType: NodeId
    :ivar ValueRank:
    :vartype ValueRank: Int32
    :ivar ArrayDimensions:
    :vartype ArrayDimensions: UInt32
    :ivar AccessLevel:
    :vartype AccessLevel: Byte
    :ivar UserAccessLevel:
    :vartype UserAccessLevel: Byte
    :ivar MinimumSamplingInterval:
    :vartype MinimumSamplingInterval: Double
    :ivar Historizing:
    :vartype Historizing: Boolean
    '''

    ua_types = [
        ('SpecifiedAttributes', 'UInt32'),
        ('DisplayName', 'LocalizedText'),
        ('Description', 'LocalizedText'),
        ('WriteMask', 'UInt32'),
        ('UserWriteMask', 'UInt32'),
        ('Value', 'Variant'),
        ('DataType', 'NodeId'),
        ('ValueRank', 'Int32'),
        ('ArrayDimensions', 'ListOfUInt32'),
        ('AccessLevel', 'Byte'),
        ('UserAccessLevel', 'Byte'),
        ('MinimumSamplingInterval', 'Double'),
        ('Historizing', 'Boolean'),
               ]

    def __init__(self):
        self.SpecifiedAttributes = 0
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self.UserWriteMask = 0
        self.Value = Variant()
        self.DataType = NodeId()
        self.ValueRank = 0
        self.ArrayDimensions = []
        self.AccessLevel = 0
        self.UserAccessLevel = 0
        self.MinimumSamplingInterval = 0
        self.Historizing = True
        self._freeze = True

    def __str__(self):
        return 'VariableAttributes(' + 'SpecifiedAttributes:' + str(self.SpecifiedAttributes) + ', ' + \
               'DisplayName:' + str(self.DisplayName) + ', ' + \
               'Description:' + str(self.Description) + ', ' + \
               'WriteMask:' + str(self.WriteMask) + ', ' + \
               'UserWriteMask:' + str(self.UserWriteMask) + ', ' + \
               'Value:' + str(self.Value) + ', ' + \
               'DataType:' + str(self.DataType) + ', ' + \
               'ValueRank:' + str(self.ValueRank) + ', ' + \
               'ArrayDimensions:' + str(self.ArrayDimensions) + ', ' + \
               'AccessLevel:' + str(self.AccessLevel) + ', ' + \
               'UserAccessLevel:' + str(self.UserAccessLevel) + ', ' + \
               'MinimumSamplingInterval:' + str(self.MinimumSamplingInterval) + ', ' + \
               'Historizing:' + str(self.Historizing) + ')'

    __repr__ = __str__


class MethodAttributes(FrozenClass):
    '''
    The attributes for a method node.

    :ivar SpecifiedAttributes:
    :vartype SpecifiedAttributes: UInt32
    :ivar DisplayName:
    :vartype DisplayName: LocalizedText
    :ivar Description:
    :vartype Description: LocalizedText
    :ivar WriteMask:
    :vartype WriteMask: UInt32
    :ivar UserWriteMask:
    :vartype UserWriteMask: UInt32
    :ivar Executable:
    :vartype Executable: Boolean
    :ivar UserExecutable:
    :vartype UserExecutable: Boolean
    '''

    ua_types = [
        ('SpecifiedAttributes', 'UInt32'),
        ('DisplayName', 'LocalizedText'),
        ('Description', 'LocalizedText'),
        ('WriteMask', 'UInt32'),
        ('UserWriteMask', 'UInt32'),
        ('Executable', 'Boolean'),
        ('UserExecutable', 'Boolean'),
               ]

    def __init__(self):
        self.SpecifiedAttributes = 0
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self.UserWriteMask = 0
        self.Executable = True
        self.UserExecutable = True
        self._freeze = True

    def __str__(self):
        return 'MethodAttributes(' + 'SpecifiedAttributes:' + str(self.SpecifiedAttributes) + ', ' + \
               'DisplayName:' + str(self.DisplayName) + ', ' + \
               'Description:' + str(self.Description) + ', ' + \
               'WriteMask:' + str(self.WriteMask) + ', ' + \
               'UserWriteMask:' + str(self.UserWriteMask) + ', ' + \
               'Executable:' + str(self.Executable) + ', ' + \
               'UserExecutable:' + str(self.UserExecutable) + ')'

    __repr__ = __str__


class ObjectTypeAttributes(FrozenClass):
    '''
    The attributes for an object type node.

    :ivar SpecifiedAttributes:
    :vartype SpecifiedAttributes: UInt32
    :ivar DisplayName:
    :vartype DisplayName: LocalizedText
    :ivar Description:
    :vartype Description: LocalizedText
    :ivar WriteMask:
    :vartype WriteMask: UInt32
    :ivar UserWriteMask:
    :vartype UserWriteMask: UInt32
    :ivar IsAbstract:
    :vartype IsAbstract: Boolean
    '''

    ua_types = [
        ('SpecifiedAttributes', 'UInt32'),
        ('DisplayName', 'LocalizedText'),
        ('Description', 'LocalizedText'),
        ('WriteMask', 'UInt32'),
        ('UserWriteMask', 'UInt32'),
        ('IsAbstract', 'Boolean'),
               ]

    def __init__(self):
        self.SpecifiedAttributes = 0
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self.UserWriteMask = 0
        self.IsAbstract = True
        self._freeze = True

    def __str__(self):
        return 'ObjectTypeAttributes(' + 'SpecifiedAttributes:' + str(self.SpecifiedAttributes) + ', ' + \
               'DisplayName:' + str(self.DisplayName) + ', ' + \
               'Description:' + str(self.Description) + ', ' + \
               'WriteMask:' + str(self.WriteMask) + ', ' + \
               'UserWriteMask:' + str(self.UserWriteMask) + ', ' + \
               'IsAbstract:' + str(self.IsAbstract) + ')'

    __repr__ = __str__


class VariableTypeAttributes(FrozenClass):
    '''
    The attributes for a variable type node.

    :ivar SpecifiedAttributes:
    :vartype SpecifiedAttributes: UInt32
    :ivar DisplayName:
    :vartype DisplayName: LocalizedText
    :ivar Description:
    :vartype Description: LocalizedText
    :ivar WriteMask:
    :vartype WriteMask: UInt32
    :ivar UserWriteMask:
    :vartype UserWriteMask: UInt32
    :ivar Value:
    :vartype Value: Variant
    :ivar DataType:
    :vartype DataType: NodeId
    :ivar ValueRank:
    :vartype ValueRank: Int32
    :ivar ArrayDimensions:
    :vartype ArrayDimensions: UInt32
    :ivar IsAbstract:
    :vartype IsAbstract: Boolean
    '''

    ua_types = [
        ('SpecifiedAttributes', 'UInt32'),
        ('DisplayName', 'LocalizedText'),
        ('Description', 'LocalizedText'),
        ('WriteMask', 'UInt32'),
        ('UserWriteMask', 'UInt32'),
        ('Value', 'Variant'),
        ('DataType', 'NodeId'),
        ('ValueRank', 'Int32'),
        ('ArrayDimensions', 'ListOfUInt32'),
        ('IsAbstract', 'Boolean'),
               ]

    def __init__(self):
        self.SpecifiedAttributes = 0
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self.UserWriteMask = 0
        self.Value = Variant()
        self.DataType = NodeId()
        self.ValueRank = 0
        self.ArrayDimensions = []
        self.IsAbstract = True
        self._freeze = True

    def __str__(self):
        return 'VariableTypeAttributes(' + 'SpecifiedAttributes:' + str(self.SpecifiedAttributes) + ', ' + \
               'DisplayName:' + str(self.DisplayName) + ', ' + \
               'Description:' + str(self.Description) + ', ' + \
               'WriteMask:' + str(self.WriteMask) + ', ' + \
               'UserWriteMask:' + str(self.UserWriteMask) + ', ' + \
               'Value:' + str(self.Value) + ', ' + \
               'DataType:' + str(self.DataType) + ', ' + \
               'ValueRank:' + str(self.ValueRank) + ', ' + \
               'ArrayDimensions:' + str(self.ArrayDimensions) + ', ' + \
               'IsAbstract:' + str(self.IsAbstract) + ')'

    __repr__ = __str__


class ReferenceTypeAttributes(FrozenClass):
    '''
    The attributes for a reference type node.

    :ivar SpecifiedAttributes:
    :vartype SpecifiedAttributes: UInt32
    :ivar DisplayName:
    :vartype DisplayName: LocalizedText
    :ivar Description:
    :vartype Description: LocalizedText
    :ivar WriteMask:
    :vartype WriteMask: UInt32
    :ivar UserWriteMask:
    :vartype UserWriteMask: UInt32
    :ivar IsAbstract:
    :vartype IsAbstract: Boolean
    :ivar Symmetric:
    :vartype Symmetric: Boolean
    :ivar InverseName:
    :vartype InverseName: LocalizedText
    '''

    ua_types = [
        ('SpecifiedAttributes', 'UInt32'),
        ('DisplayName', 'LocalizedText'),
        ('Description', 'LocalizedText'),
        ('WriteMask', 'UInt32'),
        ('UserWriteMask', 'UInt32'),
        ('IsAbstract', 'Boolean'),
        ('Symmetric', 'Boolean'),
        ('InverseName', 'LocalizedText'),
               ]

    def __init__(self):
        self.SpecifiedAttributes = 0
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self.UserWriteMask = 0
        self.IsAbstract = True
        self.Symmetric = True
        self.InverseName = LocalizedText()
        self._freeze = True

    def __str__(self):
        return 'ReferenceTypeAttributes(' + 'SpecifiedAttributes:' + str(self.SpecifiedAttributes) + ', ' + \
               'DisplayName:' + str(self.DisplayName) + ', ' + \
               'Description:' + str(self.Description) + ', ' + \
               'WriteMask:' + str(self.WriteMask) + ', ' + \
               'UserWriteMask:' + str(self.UserWriteMask) + ', ' + \
               'IsAbstract:' + str(self.IsAbstract) + ', ' + \
               'Symmetric:' + str(self.Symmetric) + ', ' + \
               'InverseName:' + str(self.InverseName) + ')'

    __repr__ = __str__


class DataTypeAttributes(FrozenClass):
    '''
    The attributes for a data type node.

    :ivar SpecifiedAttributes:
    :vartype SpecifiedAttributes: UInt32
    :ivar DisplayName:
    :vartype DisplayName: LocalizedText
    :ivar Description:
    :vartype Description: LocalizedText
    :ivar WriteMask:
    :vartype WriteMask: UInt32
    :ivar UserWriteMask:
    :vartype UserWriteMask: UInt32
    :ivar IsAbstract:
    :vartype IsAbstract: Boolean
    '''

    ua_types = [
        ('SpecifiedAttributes', 'UInt32'),
        ('DisplayName', 'LocalizedText'),
        ('Description', 'LocalizedText'),
        ('WriteMask', 'UInt32'),
        ('UserWriteMask', 'UInt32'),
        ('IsAbstract', 'Boolean'),
               ]

    def __init__(self):
        self.SpecifiedAttributes = 0
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self.UserWriteMask = 0
        self.IsAbstract = True
        self._freeze = True

    def __str__(self):
        return 'DataTypeAttributes(' + 'SpecifiedAttributes:' + str(self.SpecifiedAttributes) + ', ' + \
               'DisplayName:' + str(self.DisplayName) + ', ' + \
               'Description:' + str(self.Description) + ', ' + \
               'WriteMask:' + str(self.WriteMask) + ', ' + \
               'UserWriteMask:' + str(self.UserWriteMask) + ', ' + \
               'IsAbstract:' + str(self.IsAbstract) + ')'

    __repr__ = __str__


class ViewAttributes(FrozenClass):
    '''
    The attributes for a view node.

    :ivar SpecifiedAttributes:
    :vartype SpecifiedAttributes: UInt32
    :ivar DisplayName:
    :vartype DisplayName: LocalizedText
    :ivar Description:
    :vartype Description: LocalizedText
    :ivar WriteMask:
    :vartype WriteMask: UInt32
    :ivar UserWriteMask:
    :vartype UserWriteMask: UInt32
    :ivar ContainsNoLoops:
    :vartype ContainsNoLoops: Boolean
    :ivar EventNotifier:
    :vartype EventNotifier: Byte
    '''

    ua_types = [
        ('SpecifiedAttributes', 'UInt32'),
        ('DisplayName', 'LocalizedText'),
        ('Description', 'LocalizedText'),
        ('WriteMask', 'UInt32'),
        ('UserWriteMask', 'UInt32'),
        ('ContainsNoLoops', 'Boolean'),
        ('EventNotifier', 'Byte'),
               ]

    def __init__(self):
        self.SpecifiedAttributes = 0
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self.UserWriteMask = 0
        self.ContainsNoLoops = True
        self.EventNotifier = 0
        self._freeze = True

    def __str__(self):
        return 'ViewAttributes(' + 'SpecifiedAttributes:' + str(self.SpecifiedAttributes) + ', ' + \
               'DisplayName:' + str(self.DisplayName) + ', ' + \
               'Description:' + str(self.Description) + ', ' + \
               'WriteMask:' + str(self.WriteMask) + ', ' + \
               'UserWriteMask:' + str(self.UserWriteMask) + ', ' + \
               'ContainsNoLoops:' + str(self.ContainsNoLoops) + ', ' + \
               'EventNotifier:' + str(self.EventNotifier) + ')'

    __repr__ = __str__


class GenericAttributeValue(FrozenClass):
    '''
    :ivar AttributeId:
    :vartype AttributeId: UInt32
    :ivar Value:
    :vartype Value: Variant
    '''

    ua_types = [
        ('AttributeId', 'UInt32'),
        ('Value', 'Variant'),
               ]

    def __init__(self):
        self.AttributeId = 0
        self.Value = Variant()
        self._freeze = True

    def __str__(self):
        return 'GenericAttributeValue(' + 'AttributeId:' + str(self.AttributeId) + ', ' + \
               'Value:' + str(self.Value) + ')'

    __repr__ = __str__


class GenericAttributes(FrozenClass):
    '''
    :ivar SpecifiedAttributes:
    :vartype SpecifiedAttributes: UInt32
    :ivar DisplayName:
    :vartype DisplayName: LocalizedText
    :ivar Description:
    :vartype Description: LocalizedText
    :ivar WriteMask:
    :vartype WriteMask: UInt32
    :ivar UserWriteMask:
    :vartype UserWriteMask: UInt32
    :ivar AttributeValues:
    :vartype AttributeValues: GenericAttributeValue
    '''

    ua_types = [
        ('SpecifiedAttributes', 'UInt32'),
        ('DisplayName', 'LocalizedText'),
        ('Description', 'LocalizedText'),
        ('WriteMask', 'UInt32'),
        ('UserWriteMask', 'UInt32'),
        ('AttributeValues', 'ListOfGenericAttributeValue'),
               ]

    def __init__(self):
        self.SpecifiedAttributes = 0
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self.UserWriteMask = 0
        self.AttributeValues = []
        self._freeze = True

    def __str__(self):
        return 'GenericAttributes(' + 'SpecifiedAttributes:' + str(self.SpecifiedAttributes) + ', ' + \
               'DisplayName:' + str(self.DisplayName) + ', ' + \
               'Description:' + str(self.Description) + ', ' + \
               'WriteMask:' + str(self.WriteMask) + ', ' + \
               'UserWriteMask:' + str(self.UserWriteMask) + ', ' + \
               'AttributeValues:' + str(self.AttributeValues) + ')'

    __repr__ = __str__


class AddNodesItem(FrozenClass):
    '''
    A request to add a node to the server address space.

    :ivar ParentNodeId:
    :vartype ParentNodeId: ExpandedNodeId
    :ivar ReferenceTypeId:
    :vartype ReferenceTypeId: NodeId
    :ivar RequestedNewNodeId:
    :vartype RequestedNewNodeId: ExpandedNodeId
    :ivar BrowseName:
    :vartype BrowseName: QualifiedName
    :ivar NodeClass:
    :vartype NodeClass: NodeClass
    :ivar NodeAttributes:
    :vartype NodeAttributes: ExtensionObject
    :ivar TypeDefinition:
    :vartype TypeDefinition: ExpandedNodeId
    '''

    ua_types = [
        ('ParentNodeId', 'ExpandedNodeId'),
        ('ReferenceTypeId', 'NodeId'),
        ('RequestedNewNodeId', 'ExpandedNodeId'),
        ('BrowseName', 'QualifiedName'),
        ('NodeClass', 'NodeClass'),
        ('NodeAttributes', 'ExtensionObject'),
        ('TypeDefinition', 'ExpandedNodeId'),
               ]

    def __init__(self):
        self.ParentNodeId = ExpandedNodeId()
        self.ReferenceTypeId = NodeId()
        self.RequestedNewNodeId = ExpandedNodeId()
        self.BrowseName = QualifiedName()
        self.NodeClass = NodeClass(0)
        self.NodeAttributes = ExtensionObject()
        self.TypeDefinition = ExpandedNodeId()
        self._freeze = True

    def __str__(self):
        return 'AddNodesItem(' + 'ParentNodeId:' + str(self.ParentNodeId) + ', ' + \
               'ReferenceTypeId:' + str(self.ReferenceTypeId) + ', ' + \
               'RequestedNewNodeId:' + str(self.RequestedNewNodeId) + ', ' + \
               'BrowseName:' + str(self.BrowseName) + ', ' + \
               'NodeClass:' + str(self.NodeClass) + ', ' + \
               'NodeAttributes:' + str(self.NodeAttributes) + ', ' + \
               'TypeDefinition:' + str(self.TypeDefinition) + ')'

    __repr__ = __str__


class AddNodesResult(FrozenClass):
    '''
    A result of an add node operation.

    :ivar StatusCode:
    :vartype StatusCode: StatusCode
    :ivar AddedNodeId:
    :vartype AddedNodeId: NodeId
    '''

    ua_types = [
        ('StatusCode', 'StatusCode'),
        ('AddedNodeId', 'NodeId'),
               ]

    def __init__(self):
        self.StatusCode = StatusCode()
        self.AddedNodeId = NodeId()
        self._freeze = True

    def __str__(self):
        return 'AddNodesResult(' + 'StatusCode:' + str(self.StatusCode) + ', ' + \
               'AddedNodeId:' + str(self.AddedNodeId) + ')'

    __repr__ = __str__


class AddNodesParameters(FrozenClass):
    '''
    :ivar NodesToAdd:
    :vartype NodesToAdd: AddNodesItem
    '''

    ua_types = [
        ('NodesToAdd', 'ListOfAddNodesItem'),
               ]

    def __init__(self):
        self.NodesToAdd = []
        self._freeze = True

    def __str__(self):
        return 'AddNodesParameters(' + 'NodesToAdd:' + str(self.NodesToAdd) + ')'

    __repr__ = __str__


class AddNodesRequest(FrozenClass):
    '''
    Adds one or more nodes to the server address space.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: AddNodesParameters
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('RequestHeader', 'RequestHeader'),
        ('Parameters', 'AddNodesParameters'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.AddNodesRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = AddNodesParameters()
        self._freeze = True

    def __str__(self):
        return 'AddNodesRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'RequestHeader:' + str(self.RequestHeader) + ', ' + \
               'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class AddNodesResponse(FrozenClass):
    '''
    Adds one or more nodes to the server address space.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    :ivar Results:
    :vartype Results: AddNodesResult
    :ivar DiagnosticInfos:
    :vartype DiagnosticInfos: DiagnosticInfo
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('ResponseHeader', 'ResponseHeader'),
        ('Results', 'ListOfAddNodesResult'),
        ('DiagnosticInfos', 'ListOfDiagnosticInfo'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.AddNodesResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Results = []
        self.DiagnosticInfos = []
        self._freeze = True

    def __str__(self):
        return 'AddNodesResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
               'Results:' + str(self.Results) + ', ' + \
               'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'

    __repr__ = __str__


class AddReferencesItem(FrozenClass):
    '''
    A request to add a reference to the server address space.

    :ivar SourceNodeId:
    :vartype SourceNodeId: NodeId
    :ivar ReferenceTypeId:
    :vartype ReferenceTypeId: NodeId
    :ivar IsForward:
    :vartype IsForward: Boolean
    :ivar TargetServerUri:
    :vartype TargetServerUri: String
    :ivar TargetNodeId:
    :vartype TargetNodeId: ExpandedNodeId
    :ivar TargetNodeClass:
    :vartype TargetNodeClass: NodeClass
    '''

    ua_types = [
        ('SourceNodeId', 'NodeId'),
        ('ReferenceTypeId', 'NodeId'),
        ('IsForward', 'Boolean'),
        ('TargetServerUri', 'String'),
        ('TargetNodeId', 'ExpandedNodeId'),
        ('TargetNodeClass', 'NodeClass'),
               ]

    def __init__(self):
        self.SourceNodeId = NodeId()
        self.ReferenceTypeId = NodeId()
        self.IsForward = True
        self.TargetServerUri = None
        self.TargetNodeId = ExpandedNodeId()
        self.TargetNodeClass = NodeClass(0)
        self._freeze = True

    def __str__(self):
        return 'AddReferencesItem(' + 'SourceNodeId:' + str(self.SourceNodeId) + ', ' + \
               'ReferenceTypeId:' + str(self.ReferenceTypeId) + ', ' + \
               'IsForward:' + str(self.IsForward) + ', ' + \
               'TargetServerUri:' + str(self.TargetServerUri) + ', ' + \
               'TargetNodeId:' + str(self.TargetNodeId) + ', ' + \
               'TargetNodeClass:' + str(self.TargetNodeClass) + ')'

    __repr__ = __str__


class AddReferencesParameters(FrozenClass):
    '''
    :ivar ReferencesToAdd:
    :vartype ReferencesToAdd: AddReferencesItem
    '''

    ua_types = [
        ('ReferencesToAdd', 'ListOfAddReferencesItem'),
               ]

    def __init__(self):
        self.ReferencesToAdd = []
        self._freeze = True

    def __str__(self):
        return 'AddReferencesParameters(' + 'ReferencesToAdd:' + str(self.ReferencesToAdd) + ')'

    __repr__ = __str__


class AddReferencesRequest(FrozenClass):
    '''
    Adds one or more references to the server address space.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: AddReferencesParameters
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('RequestHeader', 'RequestHeader'),
        ('Parameters', 'AddReferencesParameters'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.AddReferencesRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = AddReferencesParameters()
        self._freeze = True

    def __str__(self):
        return 'AddReferencesRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'RequestHeader:' + str(self.RequestHeader) + ', ' + \
               'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class AddReferencesResponse(FrozenClass):
    '''
    Adds one or more references to the server address space.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    :ivar Results:
    :vartype Results: StatusCode
    :ivar DiagnosticInfos:
    :vartype DiagnosticInfos: DiagnosticInfo
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('ResponseHeader', 'ResponseHeader'),
        ('Results', 'ListOfStatusCode'),
        ('DiagnosticInfos', 'ListOfDiagnosticInfo'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.AddReferencesResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Results = []
        self.DiagnosticInfos = []
        self._freeze = True

    def __str__(self):
        return 'AddReferencesResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
               'Results:' + str(self.Results) + ', ' + \
               'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'

    __repr__ = __str__


class DeleteNodesItem(FrozenClass):
    '''
    A request to delete a node to the server address space.

    :ivar NodeId:
    :vartype NodeId: NodeId
    :ivar DeleteTargetReferences:
    :vartype DeleteTargetReferences: Boolean
    '''

    ua_types = [
        ('NodeId', 'NodeId'),
        ('DeleteTargetReferences', 'Boolean'),
               ]

    def __init__(self):
        self.NodeId = NodeId()
        self.DeleteTargetReferences = True
        self._freeze = True

    def __str__(self):
        return 'DeleteNodesItem(' + 'NodeId:' + str(self.NodeId) + ', ' + \
               'DeleteTargetReferences:' + str(self.DeleteTargetReferences) + ')'

    __repr__ = __str__


class DeleteNodesParameters(FrozenClass):
    '''
    :ivar NodesToDelete:
    :vartype NodesToDelete: DeleteNodesItem
    '''

    ua_types = [
        ('NodesToDelete', 'ListOfDeleteNodesItem'),
               ]

    def __init__(self):
        self.NodesToDelete = []
        self._freeze = True

    def __str__(self):
        return 'DeleteNodesParameters(' + 'NodesToDelete:' + str(self.NodesToDelete) + ')'

    __repr__ = __str__


class DeleteNodesRequest(FrozenClass):
    '''
    Delete one or more nodes from the server address space.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: DeleteNodesParameters
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('RequestHeader', 'RequestHeader'),
        ('Parameters', 'DeleteNodesParameters'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.DeleteNodesRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = DeleteNodesParameters()
        self._freeze = True

    def __str__(self):
        return 'DeleteNodesRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'RequestHeader:' + str(self.RequestHeader) + ', ' + \
               'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class DeleteNodesResponse(FrozenClass):
    '''
    Delete one or more nodes from the server address space.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    :ivar Results:
    :vartype Results: StatusCode
    :ivar DiagnosticInfos:
    :vartype DiagnosticInfos: DiagnosticInfo
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('ResponseHeader', 'ResponseHeader'),
        ('Results', 'ListOfStatusCode'),
        ('DiagnosticInfos', 'ListOfDiagnosticInfo'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.DeleteNodesResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Results = []
        self.DiagnosticInfos = []
        self._freeze = True

    def __str__(self):
        return 'DeleteNodesResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
               'Results:' + str(self.Results) + ', ' + \
               'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'

    __repr__ = __str__


class DeleteReferencesItem(FrozenClass):
    '''
    A request to delete a node from the server address space.

    :ivar SourceNodeId:
    :vartype SourceNodeId: NodeId
    :ivar ReferenceTypeId:
    :vartype ReferenceTypeId: NodeId
    :ivar IsForward:
    :vartype IsForward: Boolean
    :ivar TargetNodeId:
    :vartype TargetNodeId: ExpandedNodeId
    :ivar DeleteBidirectional:
    :vartype DeleteBidirectional: Boolean
    '''

    ua_types = [
        ('SourceNodeId', 'NodeId'),
        ('ReferenceTypeId', 'NodeId'),
        ('IsForward', 'Boolean'),
        ('TargetNodeId', 'ExpandedNodeId'),
        ('DeleteBidirectional', 'Boolean'),
               ]

    def __init__(self):
        self.SourceNodeId = NodeId()
        self.ReferenceTypeId = NodeId()
        self.IsForward = True
        self.TargetNodeId = ExpandedNodeId()
        self.DeleteBidirectional = True
        self._freeze = True

    def __str__(self):
        return 'DeleteReferencesItem(' + 'SourceNodeId:' + str(self.SourceNodeId) + ', ' + \
               'ReferenceTypeId:' + str(self.ReferenceTypeId) + ', ' + \
               'IsForward:' + str(self.IsForward) + ', ' + \
               'TargetNodeId:' + str(self.TargetNodeId) + ', ' + \
               'DeleteBidirectional:' + str(self.DeleteBidirectional) + ')'

    __repr__ = __str__


class DeleteReferencesParameters(FrozenClass):
    '''
    :ivar ReferencesToDelete:
    :vartype ReferencesToDelete: DeleteReferencesItem
    '''

    ua_types = [
        ('ReferencesToDelete', 'ListOfDeleteReferencesItem'),
               ]

    def __init__(self):
        self.ReferencesToDelete = []
        self._freeze = True

    def __str__(self):
        return 'DeleteReferencesParameters(' + 'ReferencesToDelete:' + str(self.ReferencesToDelete) + ')'

    __repr__ = __str__


class DeleteReferencesRequest(FrozenClass):
    '''
    Delete one or more references from the server address space.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: DeleteReferencesParameters
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('RequestHeader', 'RequestHeader'),
        ('Parameters', 'DeleteReferencesParameters'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.DeleteReferencesRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = DeleteReferencesParameters()
        self._freeze = True

    def __str__(self):
        return 'DeleteReferencesRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'RequestHeader:' + str(self.RequestHeader) + ', ' + \
               'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class DeleteReferencesResult(FrozenClass):
    '''
    :ivar Results:
    :vartype Results: StatusCode
    :ivar DiagnosticInfos:
    :vartype DiagnosticInfos: DiagnosticInfo
    '''

    ua_types = [
        ('Results', 'ListOfStatusCode'),
        ('DiagnosticInfos', 'ListOfDiagnosticInfo'),
               ]

    def __init__(self):
        self.Results = []
        self.DiagnosticInfos = []
        self._freeze = True

    def __str__(self):
        return 'DeleteReferencesResult(' + 'Results:' + str(self.Results) + ', ' + \
               'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'

    __repr__ = __str__


class DeleteReferencesResponse(FrozenClass):
    '''
    Delete one or more references from the server address space.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    :ivar Parameters:
    :vartype Parameters: DeleteReferencesResult
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('ResponseHeader', 'ResponseHeader'),
        ('Parameters', 'DeleteReferencesResult'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.DeleteReferencesResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = DeleteReferencesResult()
        self._freeze = True

    def __str__(self):
        return 'DeleteReferencesResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
               'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class ViewDescription(FrozenClass):
    '''
    The view to browse.

    :ivar ViewId:
    :vartype ViewId: NodeId
    :ivar Timestamp:
    :vartype Timestamp: DateTime
    :ivar ViewVersion:
    :vartype ViewVersion: UInt32
    '''

    ua_types = [
        ('ViewId', 'NodeId'),
        ('Timestamp', 'DateTime'),
        ('ViewVersion', 'UInt32'),
               ]

    def __init__(self):
        self.ViewId = NodeId()
        self.Timestamp = datetime.utcnow()
        self.ViewVersion = 0
        self._freeze = True

    def __str__(self):
        return 'ViewDescription(' + 'ViewId:' + str(self.ViewId) + ', ' + \
               'Timestamp:' + str(self.Timestamp) + ', ' + \
               'ViewVersion:' + str(self.ViewVersion) + ')'

    __repr__ = __str__


class BrowseDescription(FrozenClass):
    '''
    A request to browse the the references from a node.

    :ivar NodeId:
    :vartype NodeId: NodeId
    :ivar BrowseDirection:
    :vartype BrowseDirection: BrowseDirection
    :ivar ReferenceTypeId:
    :vartype ReferenceTypeId: NodeId
    :ivar IncludeSubtypes:
    :vartype IncludeSubtypes: Boolean
    :ivar NodeClassMask:
    :vartype NodeClassMask: UInt32
    :ivar ResultMask:
    :vartype ResultMask: UInt32
    '''

    ua_types = [
        ('NodeId', 'NodeId'),
        ('BrowseDirection', 'BrowseDirection'),
        ('ReferenceTypeId', 'NodeId'),
        ('IncludeSubtypes', 'Boolean'),
        ('NodeClassMask', 'UInt32'),
        ('ResultMask', 'UInt32'),
               ]

    def __init__(self):
        self.NodeId = NodeId()
        self.BrowseDirection = BrowseDirection(0)
        self.ReferenceTypeId = NodeId()
        self.IncludeSubtypes = True
        self.NodeClassMask = 0
        self.ResultMask = 0
        self._freeze = True

    def __str__(self):
        return 'BrowseDescription(' + 'NodeId:' + str(self.NodeId) + ', ' + \
               'BrowseDirection:' + str(self.BrowseDirection) + ', ' + \
               'ReferenceTypeId:' + str(self.ReferenceTypeId) + ', ' + \
               'IncludeSubtypes:' + str(self.IncludeSubtypes) + ', ' + \
               'NodeClassMask:' + str(self.NodeClassMask) + ', ' + \
               'ResultMask:' + str(self.ResultMask) + ')'

    __repr__ = __str__


class ReferenceDescription(FrozenClass):
    '''
    The description of a reference.

    :ivar ReferenceTypeId:
    :vartype ReferenceTypeId: NodeId
    :ivar IsForward:
    :vartype IsForward: Boolean
    :ivar NodeId:
    :vartype NodeId: ExpandedNodeId
    :ivar BrowseName:
    :vartype BrowseName: QualifiedName
    :ivar DisplayName:
    :vartype DisplayName: LocalizedText
    :ivar NodeClass:
    :vartype NodeClass: NodeClass
    :ivar TypeDefinition:
    :vartype TypeDefinition: ExpandedNodeId
    '''

    ua_types = [
        ('ReferenceTypeId', 'NodeId'),
        ('IsForward', 'Boolean'),
        ('NodeId', 'ExpandedNodeId'),
        ('BrowseName', 'QualifiedName'),
        ('DisplayName', 'LocalizedText'),
        ('NodeClass', 'NodeClass'),
        ('TypeDefinition', 'ExpandedNodeId'),
               ]

    def __init__(self):
        self.ReferenceTypeId = NodeId()
        self.IsForward = True
        self.NodeId = ExpandedNodeId()
        self.BrowseName = QualifiedName()
        self.DisplayName = LocalizedText()
        self.NodeClass = NodeClass(0)
        self.TypeDefinition = ExpandedNodeId()
        self._freeze = True

    def __str__(self):
        return 'ReferenceDescription(' + 'ReferenceTypeId:' + str(self.ReferenceTypeId) + ', ' + \
               'IsForward:' + str(self.IsForward) + ', ' + \
               'NodeId:' + str(self.NodeId) + ', ' + \
               'BrowseName:' + str(self.BrowseName) + ', ' + \
               'DisplayName:' + str(self.DisplayName) + ', ' + \
               'NodeClass:' + str(self.NodeClass) + ', ' + \
               'TypeDefinition:' + str(self.TypeDefinition) + ')'

    __repr__ = __str__


class BrowseResult(FrozenClass):
    '''
    The result of a browse operation.

    :ivar StatusCode:
    :vartype StatusCode: StatusCode
    :ivar ContinuationPoint:
    :vartype ContinuationPoint: ByteString
    :ivar References:
    :vartype References: ReferenceDescription
    '''

    ua_types = [
        ('StatusCode', 'StatusCode'),
        ('ContinuationPoint', 'ByteString'),
        ('References', 'ListOfReferenceDescription'),
               ]

    def __init__(self):
        self.StatusCode = StatusCode()
        self.ContinuationPoint = None
        self.References = []
        self._freeze = True

    def __str__(self):
        return 'BrowseResult(' + 'StatusCode:' + str(self.StatusCode) + ', ' + \
               'ContinuationPoint:' + str(self.ContinuationPoint) + ', ' + \
               'References:' + str(self.References) + ')'

    __repr__ = __str__


class BrowseParameters(FrozenClass):
    '''
    :ivar View:
    :vartype View: ViewDescription
    :ivar RequestedMaxReferencesPerNode:
    :vartype RequestedMaxReferencesPerNode: UInt32
    :ivar NodesToBrowse:
    :vartype NodesToBrowse: BrowseDescription
    '''

    ua_types = [
        ('View', 'ViewDescription'),
        ('RequestedMaxReferencesPerNode', 'UInt32'),
        ('NodesToBrowse', 'ListOfBrowseDescription'),
               ]

    def __init__(self):
        self.View = ViewDescription()
        self.RequestedMaxReferencesPerNode = 0
        self.NodesToBrowse = []
        self._freeze = True

    def __str__(self):
        return 'BrowseParameters(' + 'View:' + str(self.View) + ', ' + \
               'RequestedMaxReferencesPerNode:' + str(self.RequestedMaxReferencesPerNode) + ', ' + \
               'NodesToBrowse:' + str(self.NodesToBrowse) + ')'

    __repr__ = __str__


class BrowseRequest(FrozenClass):
    '''
    Browse the references for one or more nodes from the server address space.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: BrowseParameters
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('RequestHeader', 'RequestHeader'),
        ('Parameters', 'BrowseParameters'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.BrowseRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = BrowseParameters()
        self._freeze = True

    def __str__(self):
        return 'BrowseRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'RequestHeader:' + str(self.RequestHeader) + ', ' + \
               'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class BrowseResponse(FrozenClass):
    '''
    Browse the references for one or more nodes from the server address space.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    :ivar Results:
    :vartype Results: BrowseResult
    :ivar DiagnosticInfos:
    :vartype DiagnosticInfos: DiagnosticInfo
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('ResponseHeader', 'ResponseHeader'),
        ('Results', 'ListOfBrowseResult'),
        ('DiagnosticInfos', 'ListOfDiagnosticInfo'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.BrowseResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Results = []
        self.DiagnosticInfos = []
        self._freeze = True

    def __str__(self):
        return 'BrowseResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
               'Results:' + str(self.Results) + ', ' + \
               'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'

    __repr__ = __str__


class BrowseNextParameters(FrozenClass):
    '''
    :ivar ReleaseContinuationPoints:
    :vartype ReleaseContinuationPoints: Boolean
    :ivar ContinuationPoints:
    :vartype ContinuationPoints: ByteString
    '''

    ua_types = [
        ('ReleaseContinuationPoints', 'Boolean'),
        ('ContinuationPoints', 'ListOfByteString'),
               ]

    def __init__(self):
        self.ReleaseContinuationPoints = True
        self.ContinuationPoints = []
        self._freeze = True

    def __str__(self):
        return 'BrowseNextParameters(' + 'ReleaseContinuationPoints:' + str(self.ReleaseContinuationPoints) + ', ' + \
               'ContinuationPoints:' + str(self.ContinuationPoints) + ')'

    __repr__ = __str__


class BrowseNextRequest(FrozenClass):
    '''
    Continues one or more browse operations.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: BrowseNextParameters
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('RequestHeader', 'RequestHeader'),
        ('Parameters', 'BrowseNextParameters'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.BrowseNextRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = BrowseNextParameters()
        self._freeze = True

    def __str__(self):
        return 'BrowseNextRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'RequestHeader:' + str(self.RequestHeader) + ', ' + \
               'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class BrowseNextResult(FrozenClass):
    '''
    :ivar Results:
    :vartype Results: BrowseResult
    :ivar DiagnosticInfos:
    :vartype DiagnosticInfos: DiagnosticInfo
    '''

    ua_types = [
        ('Results', 'ListOfBrowseResult'),
        ('DiagnosticInfos', 'ListOfDiagnosticInfo'),
               ]

    def __init__(self):
        self.Results = []
        self.DiagnosticInfos = []
        self._freeze = True

    def __str__(self):
        return 'BrowseNextResult(' + 'Results:' + str(self.Results) + ', ' + \
               'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'

    __repr__ = __str__


class BrowseNextResponse(FrozenClass):
    '''
    Continues one or more browse operations.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    :ivar Parameters:
    :vartype Parameters: BrowseNextResult
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('ResponseHeader', 'ResponseHeader'),
        ('Parameters', 'BrowseNextResult'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.BrowseNextResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = BrowseNextResult()
        self._freeze = True

    def __str__(self):
        return 'BrowseNextResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
               'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class RelativePathElement(FrozenClass):
    '''
    An element in a relative path.

    :ivar ReferenceTypeId:
    :vartype ReferenceTypeId: NodeId
    :ivar IsInverse:
    :vartype IsInverse: Boolean
    :ivar IncludeSubtypes:
    :vartype IncludeSubtypes: Boolean
    :ivar TargetName:
    :vartype TargetName: QualifiedName
    '''

    ua_types = [
        ('ReferenceTypeId', 'NodeId'),
        ('IsInverse', 'Boolean'),
        ('IncludeSubtypes', 'Boolean'),
        ('TargetName', 'QualifiedName'),
               ]

    def __init__(self):
        self.ReferenceTypeId = NodeId()
        self.IsInverse = True
        self.IncludeSubtypes = True
        self.TargetName = QualifiedName()
        self._freeze = True

    def __str__(self):
        return 'RelativePathElement(' + 'ReferenceTypeId:' + str(self.ReferenceTypeId) + ', ' + \
               'IsInverse:' + str(self.IsInverse) + ', ' + \
               'IncludeSubtypes:' + str(self.IncludeSubtypes) + ', ' + \
               'TargetName:' + str(self.TargetName) + ')'

    __repr__ = __str__


class RelativePath(FrozenClass):
    '''
    A relative path constructed from reference types and browse names.

    :ivar Elements:
    :vartype Elements: RelativePathElement
    '''

    ua_types = [
        ('Elements', 'ListOfRelativePathElement'),
               ]

    def __init__(self):
        self.Elements = []
        self._freeze = True

    def __str__(self):
        return 'RelativePath(' + 'Elements:' + str(self.Elements) + ')'

    __repr__ = __str__


class BrowsePath(FrozenClass):
    '''
    A request to translate a path into a node id.

    :ivar StartingNode:
    :vartype StartingNode: NodeId
    :ivar RelativePath:
    :vartype RelativePath: RelativePath
    '''

    ua_types = [
        ('StartingNode', 'NodeId'),
        ('RelativePath', 'RelativePath'),
               ]

    def __init__(self):
        self.StartingNode = NodeId()
        self.RelativePath = RelativePath()
        self._freeze = True

    def __str__(self):
        return 'BrowsePath(' + 'StartingNode:' + str(self.StartingNode) + ', ' + \
               'RelativePath:' + str(self.RelativePath) + ')'

    __repr__ = __str__


class BrowsePathTarget(FrozenClass):
    '''
    The target of the translated path.

    :ivar TargetId:
    :vartype TargetId: ExpandedNodeId
    :ivar RemainingPathIndex:
    :vartype RemainingPathIndex: UInt32
    '''

    ua_types = [
        ('TargetId', 'ExpandedNodeId'),
        ('RemainingPathIndex', 'UInt32'),
               ]

    def __init__(self):
        self.TargetId = ExpandedNodeId()
        self.RemainingPathIndex = 0
        self._freeze = True

    def __str__(self):
        return 'BrowsePathTarget(' + 'TargetId:' + str(self.TargetId) + ', ' + \
               'RemainingPathIndex:' + str(self.RemainingPathIndex) + ')'

    __repr__ = __str__


class BrowsePathResult(FrozenClass):
    '''
    The result of a translate opearation.

    :ivar StatusCode:
    :vartype StatusCode: StatusCode
    :ivar Targets:
    :vartype Targets: BrowsePathTarget
    '''

    ua_types = [
        ('StatusCode', 'StatusCode'),
        ('Targets', 'ListOfBrowsePathTarget'),
               ]

    def __init__(self):
        self.StatusCode = StatusCode()
        self.Targets = []
        self._freeze = True

    def __str__(self):
        return 'BrowsePathResult(' + 'StatusCode:' + str(self.StatusCode) + ', ' + \
               'Targets:' + str(self.Targets) + ')'

    __repr__ = __str__


class TranslateBrowsePathsToNodeIdsParameters(FrozenClass):
    '''
    :ivar BrowsePaths:
    :vartype BrowsePaths: BrowsePath
    '''

    ua_types = [
        ('BrowsePaths', 'ListOfBrowsePath'),
               ]

    def __init__(self):
        self.BrowsePaths = []
        self._freeze = True

    def __str__(self):
        return 'TranslateBrowsePathsToNodeIdsParameters(' + 'BrowsePaths:' + str(self.BrowsePaths) + ')'

    __repr__ = __str__


class TranslateBrowsePathsToNodeIdsRequest(FrozenClass):
    '''
    Translates one or more paths in the server address space.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: TranslateBrowsePathsToNodeIdsParameters
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('RequestHeader', 'RequestHeader'),
        ('Parameters', 'TranslateBrowsePathsToNodeIdsParameters'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.TranslateBrowsePathsToNodeIdsRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = TranslateBrowsePathsToNodeIdsParameters()
        self._freeze = True

    def __str__(self):
        return 'TranslateBrowsePathsToNodeIdsRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'RequestHeader:' + str(self.RequestHeader) + ', ' + \
               'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class TranslateBrowsePathsToNodeIdsResponse(FrozenClass):
    '''
    Translates one or more paths in the server address space.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    :ivar Results:
    :vartype Results: BrowsePathResult
    :ivar DiagnosticInfos:
    :vartype DiagnosticInfos: DiagnosticInfo
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('ResponseHeader', 'ResponseHeader'),
        ('Results', 'ListOfBrowsePathResult'),
        ('DiagnosticInfos', 'ListOfDiagnosticInfo'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.TranslateBrowsePathsToNodeIdsResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Results = []
        self.DiagnosticInfos = []
        self._freeze = True

    def __str__(self):
        return 'TranslateBrowsePathsToNodeIdsResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
               'Results:' + str(self.Results) + ', ' + \
               'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'

    __repr__ = __str__


class RegisterNodesParameters(FrozenClass):
    '''
    :ivar NodesToRegister:
    :vartype NodesToRegister: NodeId
    '''

    ua_types = [
        ('NodesToRegister', 'ListOfNodeId'),
               ]

    def __init__(self):
        self.NodesToRegister = []
        self._freeze = True

    def __str__(self):
        return 'RegisterNodesParameters(' + 'NodesToRegister:' + str(self.NodesToRegister) + ')'

    __repr__ = __str__


class RegisterNodesRequest(FrozenClass):
    '''
    Registers one or more nodes for repeated use within a session.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: RegisterNodesParameters
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('RequestHeader', 'RequestHeader'),
        ('Parameters', 'RegisterNodesParameters'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.RegisterNodesRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = RegisterNodesParameters()
        self._freeze = True

    def __str__(self):
        return 'RegisterNodesRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'RequestHeader:' + str(self.RequestHeader) + ', ' + \
               'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class RegisterNodesResult(FrozenClass):
    '''
    :ivar RegisteredNodeIds:
    :vartype RegisteredNodeIds: NodeId
    '''

    ua_types = [
        ('RegisteredNodeIds', 'ListOfNodeId'),
               ]

    def __init__(self):
        self.RegisteredNodeIds = []
        self._freeze = True

    def __str__(self):
        return 'RegisterNodesResult(' + 'RegisteredNodeIds:' + str(self.RegisteredNodeIds) + ')'

    __repr__ = __str__


class RegisterNodesResponse(FrozenClass):
    '''
    Registers one or more nodes for repeated use within a session.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    :ivar Parameters:
    :vartype Parameters: RegisterNodesResult
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('ResponseHeader', 'ResponseHeader'),
        ('Parameters', 'RegisterNodesResult'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.RegisterNodesResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = RegisterNodesResult()
        self._freeze = True

    def __str__(self):
        return 'RegisterNodesResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
               'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class UnregisterNodesParameters(FrozenClass):
    '''
    :ivar NodesToUnregister:
    :vartype NodesToUnregister: NodeId
    '''

    ua_types = [
        ('NodesToUnregister', 'ListOfNodeId'),
               ]

    def __init__(self):
        self.NodesToUnregister = []
        self._freeze = True

    def __str__(self):
        return 'UnregisterNodesParameters(' + 'NodesToUnregister:' + str(self.NodesToUnregister) + ')'

    __repr__ = __str__


class UnregisterNodesRequest(FrozenClass):
    '''
    Unregisters one or more previously registered nodes.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: UnregisterNodesParameters
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('RequestHeader', 'RequestHeader'),
        ('Parameters', 'UnregisterNodesParameters'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.UnregisterNodesRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = UnregisterNodesParameters()
        self._freeze = True

    def __str__(self):
        return 'UnregisterNodesRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'RequestHeader:' + str(self.RequestHeader) + ', ' + \
               'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class UnregisterNodesResponse(FrozenClass):
    '''
    Unregisters one or more previously registered nodes.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('ResponseHeader', 'ResponseHeader'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.UnregisterNodesResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self._freeze = True

    def __str__(self):
        return 'UnregisterNodesResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'ResponseHeader:' + str(self.ResponseHeader) + ')'

    __repr__ = __str__


class EndpointConfiguration(FrozenClass):
    '''
    :ivar OperationTimeout:
    :vartype OperationTimeout: Int32
    :ivar UseBinaryEncoding:
    :vartype UseBinaryEncoding: Boolean
    :ivar MaxStringLength:
    :vartype MaxStringLength: Int32
    :ivar MaxByteStringLength:
    :vartype MaxByteStringLength: Int32
    :ivar MaxArrayLength:
    :vartype MaxArrayLength: Int32
    :ivar MaxMessageSize:
    :vartype MaxMessageSize: Int32
    :ivar MaxBufferSize:
    :vartype MaxBufferSize: Int32
    :ivar ChannelLifetime:
    :vartype ChannelLifetime: Int32
    :ivar SecurityTokenLifetime:
    :vartype SecurityTokenLifetime: Int32
    '''

    ua_types = [
        ('OperationTimeout', 'Int32'),
        ('UseBinaryEncoding', 'Boolean'),
        ('MaxStringLength', 'Int32'),
        ('MaxByteStringLength', 'Int32'),
        ('MaxArrayLength', 'Int32'),
        ('MaxMessageSize', 'Int32'),
        ('MaxBufferSize', 'Int32'),
        ('ChannelLifetime', 'Int32'),
        ('SecurityTokenLifetime', 'Int32'),
               ]

    def __init__(self):
        self.OperationTimeout = 0
        self.UseBinaryEncoding = True
        self.MaxStringLength = 0
        self.MaxByteStringLength = 0
        self.MaxArrayLength = 0
        self.MaxMessageSize = 0
        self.MaxBufferSize = 0
        self.ChannelLifetime = 0
        self.SecurityTokenLifetime = 0
        self._freeze = True

    def __str__(self):
        return 'EndpointConfiguration(' + 'OperationTimeout:' + str(self.OperationTimeout) + ', ' + \
               'UseBinaryEncoding:' + str(self.UseBinaryEncoding) + ', ' + \
               'MaxStringLength:' + str(self.MaxStringLength) + ', ' + \
               'MaxByteStringLength:' + str(self.MaxByteStringLength) + ', ' + \
               'MaxArrayLength:' + str(self.MaxArrayLength) + ', ' + \
               'MaxMessageSize:' + str(self.MaxMessageSize) + ', ' + \
               'MaxBufferSize:' + str(self.MaxBufferSize) + ', ' + \
               'ChannelLifetime:' + str(self.ChannelLifetime) + ', ' + \
               'SecurityTokenLifetime:' + str(self.SecurityTokenLifetime) + ')'

    __repr__ = __str__


class QueryDataDescription(FrozenClass):
    '''
    :ivar RelativePath:
    :vartype RelativePath: RelativePath
    :ivar AttributeId:
    :vartype AttributeId: UInt32
    :ivar IndexRange:
    :vartype IndexRange: String
    '''

    ua_types = [
        ('RelativePath', 'RelativePath'),
        ('AttributeId', 'UInt32'),
        ('IndexRange', 'String'),
               ]

    def __init__(self):
        self.RelativePath = RelativePath()
        self.AttributeId = 0
        self.IndexRange = None
        self._freeze = True

    def __str__(self):
        return 'QueryDataDescription(' + 'RelativePath:' + str(self.RelativePath) + ', ' + \
               'AttributeId:' + str(self.AttributeId) + ', ' + \
               'IndexRange:' + str(self.IndexRange) + ')'

    __repr__ = __str__


class NodeTypeDescription(FrozenClass):
    '''
    :ivar TypeDefinitionNode:
    :vartype TypeDefinitionNode: ExpandedNodeId
    :ivar IncludeSubTypes:
    :vartype IncludeSubTypes: Boolean
    :ivar DataToReturn:
    :vartype DataToReturn: QueryDataDescription
    '''

    ua_types = [
        ('TypeDefinitionNode', 'ExpandedNodeId'),
        ('IncludeSubTypes', 'Boolean'),
        ('DataToReturn', 'ListOfQueryDataDescription'),
               ]

    def __init__(self):
        self.TypeDefinitionNode = ExpandedNodeId()
        self.IncludeSubTypes = True
        self.DataToReturn = []
        self._freeze = True

    def __str__(self):
        return 'NodeTypeDescription(' + 'TypeDefinitionNode:' + str(self.TypeDefinitionNode) + ', ' + \
               'IncludeSubTypes:' + str(self.IncludeSubTypes) + ', ' + \
               'DataToReturn:' + str(self.DataToReturn) + ')'

    __repr__ = __str__


class QueryDataSet(FrozenClass):
    '''
    :ivar NodeId:
    :vartype NodeId: ExpandedNodeId
    :ivar TypeDefinitionNode:
    :vartype TypeDefinitionNode: ExpandedNodeId
    :ivar Values:
    :vartype Values: Variant
    '''

    ua_types = [
        ('NodeId', 'ExpandedNodeId'),
        ('TypeDefinitionNode', 'ExpandedNodeId'),
        ('Values', 'ListOfVariant'),
               ]

    def __init__(self):
        self.NodeId = ExpandedNodeId()
        self.TypeDefinitionNode = ExpandedNodeId()
        self.Values = []
        self._freeze = True

    def __str__(self):
        return 'QueryDataSet(' + 'NodeId:' + str(self.NodeId) + ', ' + \
               'TypeDefinitionNode:' + str(self.TypeDefinitionNode) + ', ' + \
               'Values:' + str(self.Values) + ')'

    __repr__ = __str__


class NodeReference(FrozenClass):
    '''
    :ivar NodeId:
    :vartype NodeId: NodeId
    :ivar ReferenceTypeId:
    :vartype ReferenceTypeId: NodeId
    :ivar IsForward:
    :vartype IsForward: Boolean
    :ivar ReferencedNodeIds:
    :vartype ReferencedNodeIds: NodeId
    '''

    ua_types = [
        ('NodeId', 'NodeId'),
        ('ReferenceTypeId', 'NodeId'),
        ('IsForward', 'Boolean'),
        ('ReferencedNodeIds', 'ListOfNodeId'),
               ]

    def __init__(self):
        self.NodeId = NodeId()
        self.ReferenceTypeId = NodeId()
        self.IsForward = True
        self.ReferencedNodeIds = []
        self._freeze = True

    def __str__(self):
        return 'NodeReference(' + 'NodeId:' + str(self.NodeId) + ', ' + \
               'ReferenceTypeId:' + str(self.ReferenceTypeId) + ', ' + \
               'IsForward:' + str(self.IsForward) + ', ' + \
               'ReferencedNodeIds:' + str(self.ReferencedNodeIds) + ')'

    __repr__ = __str__


class ContentFilterElement(FrozenClass):
    '''
    :ivar FilterOperator:
    :vartype FilterOperator: FilterOperator
    :ivar FilterOperands:
    :vartype FilterOperands: ExtensionObject
    '''

    ua_types = [
        ('FilterOperator', 'FilterOperator'),
        ('FilterOperands', 'ListOfExtensionObject'),
               ]

    def __init__(self):
        self.FilterOperator = FilterOperator(0)
        self.FilterOperands = []
        self._freeze = True

    def __str__(self):
        return 'ContentFilterElement(' + 'FilterOperator:' + str(self.FilterOperator) + ', ' + \
               'FilterOperands:' + str(self.FilterOperands) + ')'

    __repr__ = __str__


class ContentFilter(FrozenClass):
    '''
    :ivar Elements:
    :vartype Elements: ContentFilterElement
    '''

    ua_types = [
        ('Elements', 'ListOfContentFilterElement'),
               ]

    def __init__(self):
        self.Elements = []
        self._freeze = True

    def __str__(self):
        return 'ContentFilter(' + 'Elements:' + str(self.Elements) + ')'

    __repr__ = __str__


class ElementOperand(FrozenClass):
    '''
    :ivar Index:
    :vartype Index: UInt32
    '''

    ua_types = [
        ('Index', 'UInt32'),
               ]

    def __init__(self):
        self.Index = 0
        self._freeze = True

    def __str__(self):
        return 'ElementOperand(' + 'Index:' + str(self.Index) + ')'

    __repr__ = __str__


class LiteralOperand(FrozenClass):
    '''
    :ivar Value:
    :vartype Value: Variant
    '''

    ua_types = [
        ('Value', 'Variant'),
               ]

    def __init__(self):
        self.Value = Variant()
        self._freeze = True

    def __str__(self):
        return 'LiteralOperand(' + 'Value:' + str(self.Value) + ')'

    __repr__ = __str__


class AttributeOperand(FrozenClass):
    '''
    :ivar NodeId:
    :vartype NodeId: NodeId
    :ivar Alias:
    :vartype Alias: String
    :ivar BrowsePath:
    :vartype BrowsePath: RelativePath
    :ivar AttributeId:
    :vartype AttributeId: UInt32
    :ivar IndexRange:
    :vartype IndexRange: String
    '''

    ua_types = [
        ('NodeId', 'NodeId'),
        ('Alias', 'String'),
        ('BrowsePath', 'RelativePath'),
        ('AttributeId', 'UInt32'),
        ('IndexRange', 'String'),
               ]

    def __init__(self):
        self.NodeId = NodeId()
        self.Alias = None
        self.BrowsePath = RelativePath()
        self.AttributeId = 0
        self.IndexRange = None
        self._freeze = True

    def __str__(self):
        return 'AttributeOperand(' + 'NodeId:' + str(self.NodeId) + ', ' + \
               'Alias:' + str(self.Alias) + ', ' + \
               'BrowsePath:' + str(self.BrowsePath) + ', ' + \
               'AttributeId:' + str(self.AttributeId) + ', ' + \
               'IndexRange:' + str(self.IndexRange) + ')'

    __repr__ = __str__


class SimpleAttributeOperand(FrozenClass):
    '''
    :ivar TypeDefinitionId:
    :vartype TypeDefinitionId: NodeId
    :ivar BrowsePath:
    :vartype BrowsePath: QualifiedName
    :ivar AttributeId:
    :vartype AttributeId: UInt32
    :ivar IndexRange:
    :vartype IndexRange: String
    '''

    ua_types = [
        ('TypeDefinitionId', 'NodeId'),
        ('BrowsePath', 'ListOfQualifiedName'),
        ('AttributeId', 'UInt32'),
        ('IndexRange', 'String'),
               ]

    def __init__(self):
        self.TypeDefinitionId = NodeId()
        self.BrowsePath = []
        self.AttributeId = 0
        self.IndexRange = None
        self._freeze = True

    def __str__(self):
        return 'SimpleAttributeOperand(' + 'TypeDefinitionId:' + str(self.TypeDefinitionId) + ', ' + \
               'BrowsePath:' + str(self.BrowsePath) + ', ' + \
               'AttributeId:' + str(self.AttributeId) + ', ' + \
               'IndexRange:' + str(self.IndexRange) + ')'

    __repr__ = __str__


class ContentFilterElementResult(FrozenClass):
    '''
    :ivar StatusCode:
    :vartype StatusCode: StatusCode
    :ivar OperandStatusCodes:
    :vartype OperandStatusCodes: StatusCode
    :ivar OperandDiagnosticInfos:
    :vartype OperandDiagnosticInfos: DiagnosticInfo
    '''

    ua_types = [
        ('StatusCode', 'StatusCode'),
        ('OperandStatusCodes', 'ListOfStatusCode'),
        ('OperandDiagnosticInfos', 'ListOfDiagnosticInfo'),
               ]

    def __init__(self):
        self.StatusCode = StatusCode()
        self.OperandStatusCodes = []
        self.OperandDiagnosticInfos = []
        self._freeze = True

    def __str__(self):
        return 'ContentFilterElementResult(' + 'StatusCode:' + str(self.StatusCode) + ', ' + \
               'OperandStatusCodes:' + str(self.OperandStatusCodes) + ', ' + \
               'OperandDiagnosticInfos:' + str(self.OperandDiagnosticInfos) + ')'

    __repr__ = __str__


class ContentFilterResult(FrozenClass):
    '''
    :ivar ElementResults:
    :vartype ElementResults: ContentFilterElementResult
    :ivar ElementDiagnosticInfos:
    :vartype ElementDiagnosticInfos: DiagnosticInfo
    '''

    ua_types = [
        ('ElementResults', 'ListOfContentFilterElementResult'),
        ('ElementDiagnosticInfos', 'ListOfDiagnosticInfo'),
               ]

    def __init__(self):
        self.ElementResults = []
        self.ElementDiagnosticInfos = []
        self._freeze = True

    def __str__(self):
        return 'ContentFilterResult(' + 'ElementResults:' + str(self.ElementResults) + ', ' + \
               'ElementDiagnosticInfos:' + str(self.ElementDiagnosticInfos) + ')'

    __repr__ = __str__


class ParsingResult(FrozenClass):
    '''
    :ivar StatusCode:
    :vartype StatusCode: StatusCode
    :ivar DataStatusCodes:
    :vartype DataStatusCodes: StatusCode
    :ivar DataDiagnosticInfos:
    :vartype DataDiagnosticInfos: DiagnosticInfo
    '''

    ua_types = [
        ('StatusCode', 'StatusCode'),
        ('DataStatusCodes', 'ListOfStatusCode'),
        ('DataDiagnosticInfos', 'ListOfDiagnosticInfo'),
               ]

    def __init__(self):
        self.StatusCode = StatusCode()
        self.DataStatusCodes = []
        self.DataDiagnosticInfos = []
        self._freeze = True

    def __str__(self):
        return 'ParsingResult(' + 'StatusCode:' + str(self.StatusCode) + ', ' + \
               'DataStatusCodes:' + str(self.DataStatusCodes) + ', ' + \
               'DataDiagnosticInfos:' + str(self.DataDiagnosticInfos) + ')'

    __repr__ = __str__


class QueryFirstParameters(FrozenClass):
    '''
    :ivar View:
    :vartype View: ViewDescription
    :ivar NodeTypes:
    :vartype NodeTypes: NodeTypeDescription
    :ivar Filter:
    :vartype Filter: ContentFilter
    :ivar MaxDataSetsToReturn:
    :vartype MaxDataSetsToReturn: UInt32
    :ivar MaxReferencesToReturn:
    :vartype MaxReferencesToReturn: UInt32
    '''

    ua_types = [
        ('View', 'ViewDescription'),
        ('NodeTypes', 'ListOfNodeTypeDescription'),
        ('Filter', 'ContentFilter'),
        ('MaxDataSetsToReturn', 'UInt32'),
        ('MaxReferencesToReturn', 'UInt32'),
               ]

    def __init__(self):
        self.View = ViewDescription()
        self.NodeTypes = []
        self.Filter = ContentFilter()
        self.MaxDataSetsToReturn = 0
        self.MaxReferencesToReturn = 0
        self._freeze = True

    def __str__(self):
        return 'QueryFirstParameters(' + 'View:' + str(self.View) + ', ' + \
               'NodeTypes:' + str(self.NodeTypes) + ', ' + \
               'Filter:' + str(self.Filter) + ', ' + \
               'MaxDataSetsToReturn:' + str(self.MaxDataSetsToReturn) + ', ' + \
               'MaxReferencesToReturn:' + str(self.MaxReferencesToReturn) + ')'

    __repr__ = __str__


class QueryFirstRequest(FrozenClass):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: QueryFirstParameters
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('RequestHeader', 'RequestHeader'),
        ('Parameters', 'QueryFirstParameters'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.QueryFirstRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = QueryFirstParameters()
        self._freeze = True

    def __str__(self):
        return 'QueryFirstRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'RequestHeader:' + str(self.RequestHeader) + ', ' + \
               'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class QueryFirstResult(FrozenClass):
    '''
    :ivar QueryDataSets:
    :vartype QueryDataSets: QueryDataSet
    :ivar ContinuationPoint:
    :vartype ContinuationPoint: ByteString
    :ivar ParsingResults:
    :vartype ParsingResults: ParsingResult
    :ivar DiagnosticInfos:
    :vartype DiagnosticInfos: DiagnosticInfo
    :ivar FilterResult:
    :vartype FilterResult: ContentFilterResult
    '''

    ua_types = [
        ('QueryDataSets', 'ListOfQueryDataSet'),
        ('ContinuationPoint', 'ByteString'),
        ('ParsingResults', 'ListOfParsingResult'),
        ('DiagnosticInfos', 'ListOfDiagnosticInfo'),
        ('FilterResult', 'ContentFilterResult'),
               ]

    def __init__(self):
        self.QueryDataSets = []
        self.ContinuationPoint = None
        self.ParsingResults = []
        self.DiagnosticInfos = []
        self.FilterResult = ContentFilterResult()
        self._freeze = True

    def __str__(self):
        return 'QueryFirstResult(' + 'QueryDataSets:' + str(self.QueryDataSets) + ', ' + \
               'ContinuationPoint:' + str(self.ContinuationPoint) + ', ' + \
               'ParsingResults:' + str(self.ParsingResults) + ', ' + \
               'DiagnosticInfos:' + str(self.DiagnosticInfos) + ', ' + \
               'FilterResult:' + str(self.FilterResult) + ')'

    __repr__ = __str__


class QueryFirstResponse(FrozenClass):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    :ivar Parameters:
    :vartype Parameters: QueryFirstResult
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('ResponseHeader', 'ResponseHeader'),
        ('Parameters', 'QueryFirstResult'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.QueryFirstResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = QueryFirstResult()
        self._freeze = True

    def __str__(self):
        return 'QueryFirstResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
               'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class QueryNextParameters(FrozenClass):
    '''
    :ivar ReleaseContinuationPoint:
    :vartype ReleaseContinuationPoint: Boolean
    :ivar ContinuationPoint:
    :vartype ContinuationPoint: ByteString
    '''

    ua_types = [
        ('ReleaseContinuationPoint', 'Boolean'),
        ('ContinuationPoint', 'ByteString'),
               ]

    def __init__(self):
        self.ReleaseContinuationPoint = True
        self.ContinuationPoint = None
        self._freeze = True

    def __str__(self):
        return 'QueryNextParameters(' + 'ReleaseContinuationPoint:' + str(self.ReleaseContinuationPoint) + ', ' + \
               'ContinuationPoint:' + str(self.ContinuationPoint) + ')'

    __repr__ = __str__


class QueryNextRequest(FrozenClass):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: QueryNextParameters
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('RequestHeader', 'RequestHeader'),
        ('Parameters', 'QueryNextParameters'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.QueryNextRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = QueryNextParameters()
        self._freeze = True

    def __str__(self):
        return 'QueryNextRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'RequestHeader:' + str(self.RequestHeader) + ', ' + \
               'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class QueryNextResult(FrozenClass):
    '''
    :ivar QueryDataSets:
    :vartype QueryDataSets: QueryDataSet
    :ivar RevisedContinuationPoint:
    :vartype RevisedContinuationPoint: ByteString
    '''

    ua_types = [
        ('QueryDataSets', 'ListOfQueryDataSet'),
        ('RevisedContinuationPoint', 'ByteString'),
               ]

    def __init__(self):
        self.QueryDataSets = []
        self.RevisedContinuationPoint = None
        self._freeze = True

    def __str__(self):
        return 'QueryNextResult(' + 'QueryDataSets:' + str(self.QueryDataSets) + ', ' + \
               'RevisedContinuationPoint:' + str(self.RevisedContinuationPoint) + ')'

    __repr__ = __str__


class QueryNextResponse(FrozenClass):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    :ivar Parameters:
    :vartype Parameters: QueryNextResult
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('ResponseHeader', 'ResponseHeader'),
        ('Parameters', 'QueryNextResult'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.QueryNextResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = QueryNextResult()
        self._freeze = True

    def __str__(self):
        return 'QueryNextResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
               'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class ReadValueId(FrozenClass):
    '''
    :ivar NodeId:
    :vartype NodeId: NodeId
    :ivar AttributeId:
    :vartype AttributeId: UInt32
    :ivar IndexRange:
    :vartype IndexRange: String
    :ivar DataEncoding:
    :vartype DataEncoding: QualifiedName
    '''

    ua_types = [
        ('NodeId', 'NodeId'),
        ('AttributeId', 'UInt32'),
        ('IndexRange', 'String'),
        ('DataEncoding', 'QualifiedName'),
               ]

    def __init__(self):
        self.NodeId = NodeId()
        self.AttributeId = 0
        self.IndexRange = None
        self.DataEncoding = QualifiedName()
        self._freeze = True

    def __str__(self):
        return 'ReadValueId(' + 'NodeId:' + str(self.NodeId) + ', ' + \
               'AttributeId:' + str(self.AttributeId) + ', ' + \
               'IndexRange:' + str(self.IndexRange) + ', ' + \
               'DataEncoding:' + str(self.DataEncoding) + ')'

    __repr__ = __str__


class ReadParameters(FrozenClass):
    '''
    :ivar MaxAge:
    :vartype MaxAge: Double
    :ivar TimestampsToReturn:
    :vartype TimestampsToReturn: TimestampsToReturn
    :ivar NodesToRead:
    :vartype NodesToRead: ReadValueId
    '''

    ua_types = [
        ('MaxAge', 'Double'),
        ('TimestampsToReturn', 'TimestampsToReturn'),
        ('NodesToRead', 'ListOfReadValueId'),
               ]

    def __init__(self):
        self.MaxAge = 0
        self.TimestampsToReturn = TimestampsToReturn(0)
        self.NodesToRead = []
        self._freeze = True

    def __str__(self):
        return 'ReadParameters(' + 'MaxAge:' + str(self.MaxAge) + ', ' + \
               'TimestampsToReturn:' + str(self.TimestampsToReturn) + ', ' + \
               'NodesToRead:' + str(self.NodesToRead) + ')'

    __repr__ = __str__


class ReadRequest(FrozenClass):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: ReadParameters
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('RequestHeader', 'RequestHeader'),
        ('Parameters', 'ReadParameters'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.ReadRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = ReadParameters()
        self._freeze = True

    def __str__(self):
        return 'ReadRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'RequestHeader:' + str(self.RequestHeader) + ', ' + \
               'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class ReadResponse(FrozenClass):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    :ivar Results:
    :vartype Results: DataValue
    :ivar DiagnosticInfos:
    :vartype DiagnosticInfos: DiagnosticInfo
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('ResponseHeader', 'ResponseHeader'),
        ('Results', 'ListOfDataValue'),
        ('DiagnosticInfos', 'ListOfDiagnosticInfo'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.ReadResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Results = []
        self.DiagnosticInfos = []
        self._freeze = True

    def __str__(self):
        return 'ReadResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
               'Results:' + str(self.Results) + ', ' + \
               'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'

    __repr__ = __str__


class HistoryReadValueId(FrozenClass):
    '''
    :ivar NodeId:
    :vartype NodeId: NodeId
    :ivar IndexRange:
    :vartype IndexRange: String
    :ivar DataEncoding:
    :vartype DataEncoding: QualifiedName
    :ivar ContinuationPoint:
    :vartype ContinuationPoint: ByteString
    '''

    ua_types = [
        ('NodeId', 'NodeId'),
        ('IndexRange', 'String'),
        ('DataEncoding', 'QualifiedName'),
        ('ContinuationPoint', 'ByteString'),
               ]

    def __init__(self):
        self.NodeId = NodeId()
        self.IndexRange = None
        self.DataEncoding = QualifiedName()
        self.ContinuationPoint = None
        self._freeze = True

    def __str__(self):
        return 'HistoryReadValueId(' + 'NodeId:' + str(self.NodeId) + ', ' + \
               'IndexRange:' + str(self.IndexRange) + ', ' + \
               'DataEncoding:' + str(self.DataEncoding) + ', ' + \
               'ContinuationPoint:' + str(self.ContinuationPoint) + ')'

    __repr__ = __str__


class HistoryReadResult(FrozenClass):
    '''
    :ivar StatusCode:
    :vartype StatusCode: StatusCode
    :ivar ContinuationPoint:
    :vartype ContinuationPoint: ByteString
    :ivar HistoryData:
    :vartype HistoryData: ExtensionObject
    '''

    ua_types = [
        ('StatusCode', 'StatusCode'),
        ('ContinuationPoint', 'ByteString'),
        ('HistoryData', 'ExtensionObject'),
               ]

    def __init__(self):
        self.StatusCode = StatusCode()
        self.ContinuationPoint = None
        self.HistoryData = ExtensionObject()
        self._freeze = True

    def __str__(self):
        return 'HistoryReadResult(' + 'StatusCode:' + str(self.StatusCode) + ', ' + \
               'ContinuationPoint:' + str(self.ContinuationPoint) + ', ' + \
               'HistoryData:' + str(self.HistoryData) + ')'

    __repr__ = __str__


class HistoryReadDetails(FrozenClass):
    '''
    '''

    ua_types = [
               ]

    def __init__(self):
        self._freeze = True

    def __str__(self):
        return 'HistoryReadDetails(' +  + ')'

    __repr__ = __str__


class ReadEventDetails(FrozenClass):
    '''
    :ivar NumValuesPerNode:
    :vartype NumValuesPerNode: UInt32
    :ivar StartTime:
    :vartype StartTime: DateTime
    :ivar EndTime:
    :vartype EndTime: DateTime
    :ivar Filter:
    :vartype Filter: EventFilter
    '''

    ua_types = [
        ('NumValuesPerNode', 'UInt32'),
        ('StartTime', 'DateTime'),
        ('EndTime', 'DateTime'),
        ('Filter', 'EventFilter'),
               ]

    def __init__(self):
        self.NumValuesPerNode = 0
        self.StartTime = datetime.utcnow()
        self.EndTime = datetime.utcnow()
        self.Filter = EventFilter()
        self._freeze = True

    def __str__(self):
        return 'ReadEventDetails(' + 'NumValuesPerNode:' + str(self.NumValuesPerNode) + ', ' + \
               'StartTime:' + str(self.StartTime) + ', ' + \
               'EndTime:' + str(self.EndTime) + ', ' + \
               'Filter:' + str(self.Filter) + ')'

    __repr__ = __str__


class ReadRawModifiedDetails(FrozenClass):
    '''
    :ivar IsReadModified:
    :vartype IsReadModified: Boolean
    :ivar StartTime:
    :vartype StartTime: DateTime
    :ivar EndTime:
    :vartype EndTime: DateTime
    :ivar NumValuesPerNode:
    :vartype NumValuesPerNode: UInt32
    :ivar ReturnBounds:
    :vartype ReturnBounds: Boolean
    '''

    ua_types = [
        ('IsReadModified', 'Boolean'),
        ('StartTime', 'DateTime'),
        ('EndTime', 'DateTime'),
        ('NumValuesPerNode', 'UInt32'),
        ('ReturnBounds', 'Boolean'),
               ]

    def __init__(self):
        self.IsReadModified = True
        self.StartTime = datetime.utcnow()
        self.EndTime = datetime.utcnow()
        self.NumValuesPerNode = 0
        self.ReturnBounds = True
        self._freeze = True

    def __str__(self):
        return 'ReadRawModifiedDetails(' + 'IsReadModified:' + str(self.IsReadModified) + ', ' + \
               'StartTime:' + str(self.StartTime) + ', ' + \
               'EndTime:' + str(self.EndTime) + ', ' + \
               'NumValuesPerNode:' + str(self.NumValuesPerNode) + ', ' + \
               'ReturnBounds:' + str(self.ReturnBounds) + ')'

    __repr__ = __str__


class ReadProcessedDetails(FrozenClass):
    '''
    :ivar StartTime:
    :vartype StartTime: DateTime
    :ivar EndTime:
    :vartype EndTime: DateTime
    :ivar ProcessingInterval:
    :vartype ProcessingInterval: Double
    :ivar AggregateType:
    :vartype AggregateType: NodeId
    :ivar AggregateConfiguration:
    :vartype AggregateConfiguration: AggregateConfiguration
    '''

    ua_types = [
        ('StartTime', 'DateTime'),
        ('EndTime', 'DateTime'),
        ('ProcessingInterval', 'Double'),
        ('AggregateType', 'ListOfNodeId'),
        ('AggregateConfiguration', 'AggregateConfiguration'),
               ]

    def __init__(self):
        self.StartTime = datetime.utcnow()
        self.EndTime = datetime.utcnow()
        self.ProcessingInterval = 0
        self.AggregateType = []
        self.AggregateConfiguration = AggregateConfiguration()
        self._freeze = True

    def __str__(self):
        return 'ReadProcessedDetails(' + 'StartTime:' + str(self.StartTime) + ', ' + \
               'EndTime:' + str(self.EndTime) + ', ' + \
               'ProcessingInterval:' + str(self.ProcessingInterval) + ', ' + \
               'AggregateType:' + str(self.AggregateType) + ', ' + \
               'AggregateConfiguration:' + str(self.AggregateConfiguration) + ')'

    __repr__ = __str__


class ReadAtTimeDetails(FrozenClass):
    '''
    :ivar ReqTimes:
    :vartype ReqTimes: DateTime
    :ivar UseSimpleBounds:
    :vartype UseSimpleBounds: Boolean
    '''

    ua_types = [
        ('ReqTimes', 'ListOfDateTime'),
        ('UseSimpleBounds', 'Boolean'),
               ]

    def __init__(self):
        self.ReqTimes = []
        self.UseSimpleBounds = True
        self._freeze = True

    def __str__(self):
        return 'ReadAtTimeDetails(' + 'ReqTimes:' + str(self.ReqTimes) + ', ' + \
               'UseSimpleBounds:' + str(self.UseSimpleBounds) + ')'

    __repr__ = __str__


class HistoryData(FrozenClass):
    '''
    :ivar DataValues:
    :vartype DataValues: DataValue
    '''

    ua_types = [
        ('DataValues', 'ListOfDataValue'),
               ]

    def __init__(self):
        self.DataValues = []
        self._freeze = True

    def __str__(self):
        return 'HistoryData(' + 'DataValues:' + str(self.DataValues) + ')'

    __repr__ = __str__


class ModificationInfo(FrozenClass):
    '''
    :ivar ModificationTime:
    :vartype ModificationTime: DateTime
    :ivar UpdateType:
    :vartype UpdateType: HistoryUpdateType
    :ivar UserName:
    :vartype UserName: String
    '''

    ua_types = [
        ('ModificationTime', 'DateTime'),
        ('UpdateType', 'HistoryUpdateType'),
        ('UserName', 'String'),
               ]

    def __init__(self):
        self.ModificationTime = datetime.utcnow()
        self.UpdateType = HistoryUpdateType(0)
        self.UserName = None
        self._freeze = True

    def __str__(self):
        return 'ModificationInfo(' + 'ModificationTime:' + str(self.ModificationTime) + ', ' + \
               'UpdateType:' + str(self.UpdateType) + ', ' + \
               'UserName:' + str(self.UserName) + ')'

    __repr__ = __str__


class HistoryModifiedData(FrozenClass):
    '''
    :ivar DataValues:
    :vartype DataValues: DataValue
    :ivar ModificationInfos:
    :vartype ModificationInfos: ModificationInfo
    '''

    ua_types = [
        ('DataValues', 'ListOfDataValue'),
        ('ModificationInfos', 'ListOfModificationInfo'),
               ]

    def __init__(self):
        self.DataValues = []
        self.ModificationInfos = []
        self._freeze = True

    def __str__(self):
        return 'HistoryModifiedData(' + 'DataValues:' + str(self.DataValues) + ', ' + \
               'ModificationInfos:' + str(self.ModificationInfos) + ')'

    __repr__ = __str__


class HistoryEvent(FrozenClass):
    '''
    :ivar Events:
    :vartype Events: HistoryEventFieldList
    '''

    ua_types = [
        ('Events', 'ListOfHistoryEventFieldList'),
               ]

    def __init__(self):
        self.Events = []
        self._freeze = True

    def __str__(self):
        return 'HistoryEvent(' + 'Events:' + str(self.Events) + ')'

    __repr__ = __str__


class HistoryReadParameters(FrozenClass):
    '''
    :ivar HistoryReadDetails:
    :vartype HistoryReadDetails: ExtensionObject
    :ivar TimestampsToReturn:
    :vartype TimestampsToReturn: TimestampsToReturn
    :ivar ReleaseContinuationPoints:
    :vartype ReleaseContinuationPoints: Boolean
    :ivar NodesToRead:
    :vartype NodesToRead: HistoryReadValueId
    '''

    ua_types = [
        ('HistoryReadDetails', 'ExtensionObject'),
        ('TimestampsToReturn', 'TimestampsToReturn'),
        ('ReleaseContinuationPoints', 'Boolean'),
        ('NodesToRead', 'ListOfHistoryReadValueId'),
               ]

    def __init__(self):
        self.HistoryReadDetails = ExtensionObject()
        self.TimestampsToReturn = TimestampsToReturn(0)
        self.ReleaseContinuationPoints = True
        self.NodesToRead = []
        self._freeze = True

    def __str__(self):
        return 'HistoryReadParameters(' + 'HistoryReadDetails:' + str(self.HistoryReadDetails) + ', ' + \
               'TimestampsToReturn:' + str(self.TimestampsToReturn) + ', ' + \
               'ReleaseContinuationPoints:' + str(self.ReleaseContinuationPoints) + ', ' + \
               'NodesToRead:' + str(self.NodesToRead) + ')'

    __repr__ = __str__


class HistoryReadRequest(FrozenClass):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: HistoryReadParameters
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('RequestHeader', 'RequestHeader'),
        ('Parameters', 'HistoryReadParameters'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.HistoryReadRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = HistoryReadParameters()
        self._freeze = True

    def __str__(self):
        return 'HistoryReadRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'RequestHeader:' + str(self.RequestHeader) + ', ' + \
               'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class HistoryReadResponse(FrozenClass):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    :ivar Results:
    :vartype Results: HistoryReadResult
    :ivar DiagnosticInfos:
    :vartype DiagnosticInfos: DiagnosticInfo
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('ResponseHeader', 'ResponseHeader'),
        ('Results', 'ListOfHistoryReadResult'),
        ('DiagnosticInfos', 'ListOfDiagnosticInfo'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.HistoryReadResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Results = []
        self.DiagnosticInfos = []
        self._freeze = True

    def __str__(self):
        return 'HistoryReadResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
               'Results:' + str(self.Results) + ', ' + \
               'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'

    __repr__ = __str__


class WriteValue(FrozenClass):
    '''
    :ivar NodeId:
    :vartype NodeId: NodeId
    :ivar AttributeId:
    :vartype AttributeId: UInt32
    :ivar IndexRange:
    :vartype IndexRange: String
    :ivar Value:
    :vartype Value: DataValue
    '''

    ua_types = [
        ('NodeId', 'NodeId'),
        ('AttributeId', 'UInt32'),
        ('IndexRange', 'String'),
        ('Value', 'DataValue'),
               ]

    def __init__(self):
        self.NodeId = NodeId()
        self.AttributeId = 0
        self.IndexRange = None
        self.Value = DataValue()
        self._freeze = True

    def __str__(self):
        return 'WriteValue(' + 'NodeId:' + str(self.NodeId) + ', ' + \
               'AttributeId:' + str(self.AttributeId) + ', ' + \
               'IndexRange:' + str(self.IndexRange) + ', ' + \
               'Value:' + str(self.Value) + ')'

    __repr__ = __str__


class WriteParameters(FrozenClass):
    '''
    :ivar NodesToWrite:
    :vartype NodesToWrite: WriteValue
    '''

    ua_types = [
        ('NodesToWrite', 'ListOfWriteValue'),
               ]

    def __init__(self):
        self.NodesToWrite = []
        self._freeze = True

    def __str__(self):
        return 'WriteParameters(' + 'NodesToWrite:' + str(self.NodesToWrite) + ')'

    __repr__ = __str__


class WriteRequest(FrozenClass):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: WriteParameters
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('RequestHeader', 'RequestHeader'),
        ('Parameters', 'WriteParameters'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.WriteRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = WriteParameters()
        self._freeze = True

    def __str__(self):
        return 'WriteRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'RequestHeader:' + str(self.RequestHeader) + ', ' + \
               'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class WriteResponse(FrozenClass):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    :ivar Results:
    :vartype Results: StatusCode
    :ivar DiagnosticInfos:
    :vartype DiagnosticInfos: DiagnosticInfo
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('ResponseHeader', 'ResponseHeader'),
        ('Results', 'ListOfStatusCode'),
        ('DiagnosticInfos', 'ListOfDiagnosticInfo'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.WriteResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Results = []
        self.DiagnosticInfos = []
        self._freeze = True

    def __str__(self):
        return 'WriteResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
               'Results:' + str(self.Results) + ', ' + \
               'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'

    __repr__ = __str__


class HistoryUpdateDetails(FrozenClass):
    '''
    :ivar NodeId:
    :vartype NodeId: NodeId
    '''

    ua_types = [
        ('NodeId', 'NodeId'),
               ]

    def __init__(self):
        self.NodeId = NodeId()
        self._freeze = True

    def __str__(self):
        return 'HistoryUpdateDetails(' + 'NodeId:' + str(self.NodeId) + ')'

    __repr__ = __str__


class UpdateDataDetails(FrozenClass):
    '''
    :ivar NodeId:
    :vartype NodeId: NodeId
    :ivar PerformInsertReplace:
    :vartype PerformInsertReplace: PerformUpdateType
    :ivar UpdateValues:
    :vartype UpdateValues: DataValue
    '''

    ua_types = [
        ('NodeId', 'NodeId'),
        ('PerformInsertReplace', 'PerformUpdateType'),
        ('UpdateValues', 'ListOfDataValue'),
               ]

    def __init__(self):
        self.NodeId = NodeId()
        self.PerformInsertReplace = PerformUpdateType(0)
        self.UpdateValues = []
        self._freeze = True

    def __str__(self):
        return 'UpdateDataDetails(' + 'NodeId:' + str(self.NodeId) + ', ' + \
               'PerformInsertReplace:' + str(self.PerformInsertReplace) + ', ' + \
               'UpdateValues:' + str(self.UpdateValues) + ')'

    __repr__ = __str__


class UpdateStructureDataDetails(FrozenClass):
    '''
    :ivar NodeId:
    :vartype NodeId: NodeId
    :ivar PerformInsertReplace:
    :vartype PerformInsertReplace: PerformUpdateType
    :ivar UpdateValues:
    :vartype UpdateValues: DataValue
    '''

    ua_types = [
        ('NodeId', 'NodeId'),
        ('PerformInsertReplace', 'PerformUpdateType'),
        ('UpdateValues', 'ListOfDataValue'),
               ]

    def __init__(self):
        self.NodeId = NodeId()
        self.PerformInsertReplace = PerformUpdateType(0)
        self.UpdateValues = []
        self._freeze = True

    def __str__(self):
        return 'UpdateStructureDataDetails(' + 'NodeId:' + str(self.NodeId) + ', ' + \
               'PerformInsertReplace:' + str(self.PerformInsertReplace) + ', ' + \
               'UpdateValues:' + str(self.UpdateValues) + ')'

    __repr__ = __str__


class UpdateEventDetails(FrozenClass):
    '''
    :ivar NodeId:
    :vartype NodeId: NodeId
    :ivar PerformInsertReplace:
    :vartype PerformInsertReplace: PerformUpdateType
    :ivar Filter:
    :vartype Filter: EventFilter
    :ivar EventData:
    :vartype EventData: HistoryEventFieldList
    '''

    ua_types = [
        ('NodeId', 'NodeId'),
        ('PerformInsertReplace', 'PerformUpdateType'),
        ('Filter', 'EventFilter'),
        ('EventData', 'ListOfHistoryEventFieldList'),
               ]

    def __init__(self):
        self.NodeId = NodeId()
        self.PerformInsertReplace = PerformUpdateType(0)
        self.Filter = EventFilter()
        self.EventData = []
        self._freeze = True

    def __str__(self):
        return 'UpdateEventDetails(' + 'NodeId:' + str(self.NodeId) + ', ' + \
               'PerformInsertReplace:' + str(self.PerformInsertReplace) + ', ' + \
               'Filter:' + str(self.Filter) + ', ' + \
               'EventData:' + str(self.EventData) + ')'

    __repr__ = __str__


class DeleteRawModifiedDetails(FrozenClass):
    '''
    :ivar NodeId:
    :vartype NodeId: NodeId
    :ivar IsDeleteModified:
    :vartype IsDeleteModified: Boolean
    :ivar StartTime:
    :vartype StartTime: DateTime
    :ivar EndTime:
    :vartype EndTime: DateTime
    '''

    ua_types = [
        ('NodeId', 'NodeId'),
        ('IsDeleteModified', 'Boolean'),
        ('StartTime', 'DateTime'),
        ('EndTime', 'DateTime'),
               ]

    def __init__(self):
        self.NodeId = NodeId()
        self.IsDeleteModified = True
        self.StartTime = datetime.utcnow()
        self.EndTime = datetime.utcnow()
        self._freeze = True

    def __str__(self):
        return 'DeleteRawModifiedDetails(' + 'NodeId:' + str(self.NodeId) + ', ' + \
               'IsDeleteModified:' + str(self.IsDeleteModified) + ', ' + \
               'StartTime:' + str(self.StartTime) + ', ' + \
               'EndTime:' + str(self.EndTime) + ')'

    __repr__ = __str__


class DeleteAtTimeDetails(FrozenClass):
    '''
    :ivar NodeId:
    :vartype NodeId: NodeId
    :ivar ReqTimes:
    :vartype ReqTimes: DateTime
    '''

    ua_types = [
        ('NodeId', 'NodeId'),
        ('ReqTimes', 'ListOfDateTime'),
               ]

    def __init__(self):
        self.NodeId = NodeId()
        self.ReqTimes = []
        self._freeze = True

    def __str__(self):
        return 'DeleteAtTimeDetails(' + 'NodeId:' + str(self.NodeId) + ', ' + \
               'ReqTimes:' + str(self.ReqTimes) + ')'

    __repr__ = __str__


class DeleteEventDetails(FrozenClass):
    '''
    :ivar NodeId:
    :vartype NodeId: NodeId
    :ivar EventIds:
    :vartype EventIds: ByteString
    '''

    ua_types = [
        ('NodeId', 'NodeId'),
        ('EventIds', 'ListOfByteString'),
               ]

    def __init__(self):
        self.NodeId = NodeId()
        self.EventIds = []
        self._freeze = True

    def __str__(self):
        return 'DeleteEventDetails(' + 'NodeId:' + str(self.NodeId) + ', ' + \
               'EventIds:' + str(self.EventIds) + ')'

    __repr__ = __str__


class HistoryUpdateResult(FrozenClass):
    '''
    :ivar StatusCode:
    :vartype StatusCode: StatusCode
    :ivar OperationResults:
    :vartype OperationResults: StatusCode
    :ivar DiagnosticInfos:
    :vartype DiagnosticInfos: DiagnosticInfo
    '''

    ua_types = [
        ('StatusCode', 'StatusCode'),
        ('OperationResults', 'ListOfStatusCode'),
        ('DiagnosticInfos', 'ListOfDiagnosticInfo'),
               ]

    def __init__(self):
        self.StatusCode = StatusCode()
        self.OperationResults = []
        self.DiagnosticInfos = []
        self._freeze = True

    def __str__(self):
        return 'HistoryUpdateResult(' + 'StatusCode:' + str(self.StatusCode) + ', ' + \
               'OperationResults:' + str(self.OperationResults) + ', ' + \
               'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'

    __repr__ = __str__


class HistoryUpdateParameters(FrozenClass):
    '''
    :ivar HistoryUpdateDetails:
    :vartype HistoryUpdateDetails: ExtensionObject
    '''

    ua_types = [
        ('HistoryUpdateDetails', 'ListOfExtensionObject'),
               ]

    def __init__(self):
        self.HistoryUpdateDetails = []
        self._freeze = True

    def __str__(self):
        return 'HistoryUpdateParameters(' + 'HistoryUpdateDetails:' + str(self.HistoryUpdateDetails) + ')'

    __repr__ = __str__


class HistoryUpdateRequest(FrozenClass):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: HistoryUpdateParameters
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('RequestHeader', 'RequestHeader'),
        ('Parameters', 'HistoryUpdateParameters'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.HistoryUpdateRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = HistoryUpdateParameters()
        self._freeze = True

    def __str__(self):
        return 'HistoryUpdateRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'RequestHeader:' + str(self.RequestHeader) + ', ' + \
               'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class HistoryUpdateResponse(FrozenClass):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    :ivar Results:
    :vartype Results: HistoryUpdateResult
    :ivar DiagnosticInfos:
    :vartype DiagnosticInfos: DiagnosticInfo
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('ResponseHeader', 'ResponseHeader'),
        ('Results', 'ListOfHistoryUpdateResult'),
        ('DiagnosticInfos', 'ListOfDiagnosticInfo'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.HistoryUpdateResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Results = []
        self.DiagnosticInfos = []
        self._freeze = True

    def __str__(self):
        return 'HistoryUpdateResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
               'Results:' + str(self.Results) + ', ' + \
               'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'

    __repr__ = __str__


class CallMethodRequest(FrozenClass):
    '''
    :ivar ObjectId:
    :vartype ObjectId: NodeId
    :ivar MethodId:
    :vartype MethodId: NodeId
    :ivar InputArguments:
    :vartype InputArguments: Variant
    '''

    ua_types = [
        ('ObjectId', 'NodeId'),
        ('MethodId', 'NodeId'),
        ('InputArguments', 'ListOfVariant'),
               ]

    def __init__(self):
        self.ObjectId = NodeId()
        self.MethodId = NodeId()
        self.InputArguments = []
        self._freeze = True

    def __str__(self):
        return 'CallMethodRequest(' + 'ObjectId:' + str(self.ObjectId) + ', ' + \
               'MethodId:' + str(self.MethodId) + ', ' + \
               'InputArguments:' + str(self.InputArguments) + ')'

    __repr__ = __str__


class CallMethodResult(FrozenClass):
    '''
    :ivar StatusCode:
    :vartype StatusCode: StatusCode
    :ivar InputArgumentResults:
    :vartype InputArgumentResults: StatusCode
    :ivar InputArgumentDiagnosticInfos:
    :vartype InputArgumentDiagnosticInfos: DiagnosticInfo
    :ivar OutputArguments:
    :vartype OutputArguments: Variant
    '''

    ua_types = [
        ('StatusCode', 'StatusCode'),
        ('InputArgumentResults', 'ListOfStatusCode'),
        ('InputArgumentDiagnosticInfos', 'ListOfDiagnosticInfo'),
        ('OutputArguments', 'ListOfVariant'),
               ]

    def __init__(self):
        self.StatusCode = StatusCode()
        self.InputArgumentResults = []
        self.InputArgumentDiagnosticInfos = []
        self.OutputArguments = []
        self._freeze = True

    def __str__(self):
        return 'CallMethodResult(' + 'StatusCode:' + str(self.StatusCode) + ', ' + \
               'InputArgumentResults:' + str(self.InputArgumentResults) + ', ' + \
               'InputArgumentDiagnosticInfos:' + str(self.InputArgumentDiagnosticInfos) + ', ' + \
               'OutputArguments:' + str(self.OutputArguments) + ')'

    __repr__ = __str__


class CallParameters(FrozenClass):
    '''
    :ivar MethodsToCall:
    :vartype MethodsToCall: CallMethodRequest
    '''

    ua_types = [
        ('MethodsToCall', 'ListOfCallMethodRequest'),
               ]

    def __init__(self):
        self.MethodsToCall = []
        self._freeze = True

    def __str__(self):
        return 'CallParameters(' + 'MethodsToCall:' + str(self.MethodsToCall) + ')'

    __repr__ = __str__


class CallRequest(FrozenClass):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: CallParameters
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('RequestHeader', 'RequestHeader'),
        ('Parameters', 'CallParameters'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.CallRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = CallParameters()
        self._freeze = True

    def __str__(self):
        return 'CallRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'RequestHeader:' + str(self.RequestHeader) + ', ' + \
               'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class CallResponse(FrozenClass):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    :ivar Results:
    :vartype Results: CallMethodResult
    :ivar DiagnosticInfos:
    :vartype DiagnosticInfos: DiagnosticInfo
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('ResponseHeader', 'ResponseHeader'),
        ('Results', 'ListOfCallMethodResult'),
        ('DiagnosticInfos', 'ListOfDiagnosticInfo'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.CallResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Results = []
        self.DiagnosticInfos = []
        self._freeze = True

    def __str__(self):
        return 'CallResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
               'Results:' + str(self.Results) + ', ' + \
               'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'

    __repr__ = __str__


class MonitoringFilter(FrozenClass):
    '''
    '''

    ua_types = [
               ]

    def __init__(self):
        self._freeze = True

    def __str__(self):
        return 'MonitoringFilter(' +  + ')'

    __repr__ = __str__


class DataChangeFilter(FrozenClass):
    '''
    :ivar Trigger:
    :vartype Trigger: DataChangeTrigger
    :ivar DeadbandType:
    :vartype DeadbandType: UInt32
    :ivar DeadbandValue:
    :vartype DeadbandValue: Double
    '''

    ua_types = [
        ('Trigger', 'DataChangeTrigger'),
        ('DeadbandType', 'UInt32'),
        ('DeadbandValue', 'Double'),
               ]

    def __init__(self):
        self.Trigger = DataChangeTrigger(0)
        self.DeadbandType = 0
        self.DeadbandValue = 0
        self._freeze = True

    def __str__(self):
        return 'DataChangeFilter(' + 'Trigger:' + str(self.Trigger) + ', ' + \
               'DeadbandType:' + str(self.DeadbandType) + ', ' + \
               'DeadbandValue:' + str(self.DeadbandValue) + ')'

    __repr__ = __str__


class EventFilter(FrozenClass):
    '''
    :ivar SelectClauses:
    :vartype SelectClauses: SimpleAttributeOperand
    :ivar WhereClause:
    :vartype WhereClause: ContentFilter
    '''

    ua_types = [
        ('SelectClauses', 'ListOfSimpleAttributeOperand'),
        ('WhereClause', 'ContentFilter'),
               ]

    def __init__(self):
        self.SelectClauses = []
        self.WhereClause = ContentFilter()
        self._freeze = True

    def __str__(self):
        return 'EventFilter(' + 'SelectClauses:' + str(self.SelectClauses) + ', ' + \
               'WhereClause:' + str(self.WhereClause) + ')'

    __repr__ = __str__


class AggregateConfiguration(FrozenClass):
    '''
    :ivar UseServerCapabilitiesDefaults:
    :vartype UseServerCapabilitiesDefaults: Boolean
    :ivar TreatUncertainAsBad:
    :vartype TreatUncertainAsBad: Boolean
    :ivar PercentDataBad:
    :vartype PercentDataBad: Byte
    :ivar PercentDataGood:
    :vartype PercentDataGood: Byte
    :ivar UseSlopedExtrapolation:
    :vartype UseSlopedExtrapolation: Boolean
    '''

    ua_types = [
        ('UseServerCapabilitiesDefaults', 'Boolean'),
        ('TreatUncertainAsBad', 'Boolean'),
        ('PercentDataBad', 'Byte'),
        ('PercentDataGood', 'Byte'),
        ('UseSlopedExtrapolation', 'Boolean'),
               ]

    def __init__(self):
        self.UseServerCapabilitiesDefaults = True
        self.TreatUncertainAsBad = True
        self.PercentDataBad = 0
        self.PercentDataGood = 0
        self.UseSlopedExtrapolation = True
        self._freeze = True

    def __str__(self):
        return 'AggregateConfiguration(' + 'UseServerCapabilitiesDefaults:' + str(self.UseServerCapabilitiesDefaults) + ', ' + \
               'TreatUncertainAsBad:' + str(self.TreatUncertainAsBad) + ', ' + \
               'PercentDataBad:' + str(self.PercentDataBad) + ', ' + \
               'PercentDataGood:' + str(self.PercentDataGood) + ', ' + \
               'UseSlopedExtrapolation:' + str(self.UseSlopedExtrapolation) + ')'

    __repr__ = __str__


class AggregateFilter(FrozenClass):
    '''
    :ivar StartTime:
    :vartype StartTime: DateTime
    :ivar AggregateType:
    :vartype AggregateType: NodeId
    :ivar ProcessingInterval:
    :vartype ProcessingInterval: Double
    :ivar AggregateConfiguration:
    :vartype AggregateConfiguration: AggregateConfiguration
    '''

    ua_types = [
        ('StartTime', 'DateTime'),
        ('AggregateType', 'NodeId'),
        ('ProcessingInterval', 'Double'),
        ('AggregateConfiguration', 'AggregateConfiguration'),
               ]

    def __init__(self):
        self.StartTime = datetime.utcnow()
        self.AggregateType = NodeId()
        self.ProcessingInterval = 0
        self.AggregateConfiguration = AggregateConfiguration()
        self._freeze = True

    def __str__(self):
        return 'AggregateFilter(' + 'StartTime:' + str(self.StartTime) + ', ' + \
               'AggregateType:' + str(self.AggregateType) + ', ' + \
               'ProcessingInterval:' + str(self.ProcessingInterval) + ', ' + \
               'AggregateConfiguration:' + str(self.AggregateConfiguration) + ')'

    __repr__ = __str__


class MonitoringFilterResult(FrozenClass):
    '''
    '''

    ua_types = [
               ]

    def __init__(self):
        self._freeze = True

    def __str__(self):
        return 'MonitoringFilterResult(' +  + ')'

    __repr__ = __str__


class EventFilterResult(FrozenClass):
    '''
    :ivar SelectClauseResults:
    :vartype SelectClauseResults: StatusCode
    :ivar SelectClauseDiagnosticInfos:
    :vartype SelectClauseDiagnosticInfos: DiagnosticInfo
    :ivar WhereClauseResult:
    :vartype WhereClauseResult: ContentFilterResult
    '''

    ua_types = [
        ('SelectClauseResults', 'ListOfStatusCode'),
        ('SelectClauseDiagnosticInfos', 'ListOfDiagnosticInfo'),
        ('WhereClauseResult', 'ContentFilterResult'),
               ]

    def __init__(self):
        self.SelectClauseResults = []
        self.SelectClauseDiagnosticInfos = []
        self.WhereClauseResult = ContentFilterResult()
        self._freeze = True

    def __str__(self):
        return 'EventFilterResult(' + 'SelectClauseResults:' + str(self.SelectClauseResults) + ', ' + \
               'SelectClauseDiagnosticInfos:' + str(self.SelectClauseDiagnosticInfos) + ', ' + \
               'WhereClauseResult:' + str(self.WhereClauseResult) + ')'

    __repr__ = __str__


class AggregateFilterResult(FrozenClass):
    '''
    :ivar RevisedStartTime:
    :vartype RevisedStartTime: DateTime
    :ivar RevisedProcessingInterval:
    :vartype RevisedProcessingInterval: Double
    :ivar RevisedAggregateConfiguration:
    :vartype RevisedAggregateConfiguration: AggregateConfiguration
    '''

    ua_types = [
        ('RevisedStartTime', 'DateTime'),
        ('RevisedProcessingInterval', 'Double'),
        ('RevisedAggregateConfiguration', 'AggregateConfiguration'),
               ]

    def __init__(self):
        self.RevisedStartTime = datetime.utcnow()
        self.RevisedProcessingInterval = 0
        self.RevisedAggregateConfiguration = AggregateConfiguration()
        self._freeze = True

    def __str__(self):
        return 'AggregateFilterResult(' + 'RevisedStartTime:' + str(self.RevisedStartTime) + ', ' + \
               'RevisedProcessingInterval:' + str(self.RevisedProcessingInterval) + ', ' + \
               'RevisedAggregateConfiguration:' + str(self.RevisedAggregateConfiguration) + ')'

    __repr__ = __str__


class MonitoringParameters(FrozenClass):
    '''
    :ivar ClientHandle:
    :vartype ClientHandle: UInt32
    :ivar SamplingInterval:
    :vartype SamplingInterval: Double
    :ivar Filter:
    :vartype Filter: ExtensionObject
    :ivar QueueSize:
    :vartype QueueSize: UInt32
    :ivar DiscardOldest:
    :vartype DiscardOldest: Boolean
    '''

    ua_types = [
        ('ClientHandle', 'UInt32'),
        ('SamplingInterval', 'Double'),
        ('Filter', 'ExtensionObject'),
        ('QueueSize', 'UInt32'),
        ('DiscardOldest', 'Boolean'),
               ]

    def __init__(self):
        self.ClientHandle = 0
        self.SamplingInterval = 0
        self.Filter = ExtensionObject()
        self.QueueSize = 0
        self.DiscardOldest = True
        self._freeze = True

    def __str__(self):
        return 'MonitoringParameters(' + 'ClientHandle:' + str(self.ClientHandle) + ', ' + \
               'SamplingInterval:' + str(self.SamplingInterval) + ', ' + \
               'Filter:' + str(self.Filter) + ', ' + \
               'QueueSize:' + str(self.QueueSize) + ', ' + \
               'DiscardOldest:' + str(self.DiscardOldest) + ')'

    __repr__ = __str__


class MonitoredItemCreateRequest(FrozenClass):
    '''
    :ivar ItemToMonitor:
    :vartype ItemToMonitor: ReadValueId
    :ivar MonitoringMode:
    :vartype MonitoringMode: MonitoringMode
    :ivar RequestedParameters:
    :vartype RequestedParameters: MonitoringParameters
    '''

    ua_types = [
        ('ItemToMonitor', 'ReadValueId'),
        ('MonitoringMode', 'MonitoringMode'),
        ('RequestedParameters', 'MonitoringParameters'),
               ]

    def __init__(self):
        self.ItemToMonitor = ReadValueId()
        self.MonitoringMode = MonitoringMode(0)
        self.RequestedParameters = MonitoringParameters()
        self._freeze = True

    def __str__(self):
        return 'MonitoredItemCreateRequest(' + 'ItemToMonitor:' + str(self.ItemToMonitor) + ', ' + \
               'MonitoringMode:' + str(self.MonitoringMode) + ', ' + \
               'RequestedParameters:' + str(self.RequestedParameters) + ')'

    __repr__ = __str__


class MonitoredItemCreateResult(FrozenClass):
    '''
    :ivar StatusCode:
    :vartype StatusCode: StatusCode
    :ivar MonitoredItemId:
    :vartype MonitoredItemId: UInt32
    :ivar RevisedSamplingInterval:
    :vartype RevisedSamplingInterval: Double
    :ivar RevisedQueueSize:
    :vartype RevisedQueueSize: UInt32
    :ivar FilterResult:
    :vartype FilterResult: ExtensionObject
    '''

    ua_types = [
        ('StatusCode', 'StatusCode'),
        ('MonitoredItemId', 'UInt32'),
        ('RevisedSamplingInterval', 'Double'),
        ('RevisedQueueSize', 'UInt32'),
        ('FilterResult', 'ExtensionObject'),
               ]

    def __init__(self):
        self.StatusCode = StatusCode()
        self.MonitoredItemId = 0
        self.RevisedSamplingInterval = 0
        self.RevisedQueueSize = 0
        self.FilterResult = ExtensionObject()
        self._freeze = True

    def __str__(self):
        return 'MonitoredItemCreateResult(' + 'StatusCode:' + str(self.StatusCode) + ', ' + \
               'MonitoredItemId:' + str(self.MonitoredItemId) + ', ' + \
               'RevisedSamplingInterval:' + str(self.RevisedSamplingInterval) + ', ' + \
               'RevisedQueueSize:' + str(self.RevisedQueueSize) + ', ' + \
               'FilterResult:' + str(self.FilterResult) + ')'

    __repr__ = __str__


class CreateMonitoredItemsParameters(FrozenClass):
    '''
    :ivar SubscriptionId:
    :vartype SubscriptionId: UInt32
    :ivar TimestampsToReturn:
    :vartype TimestampsToReturn: TimestampsToReturn
    :ivar ItemsToCreate:
    :vartype ItemsToCreate: MonitoredItemCreateRequest
    '''

    ua_types = [
        ('SubscriptionId', 'UInt32'),
        ('TimestampsToReturn', 'TimestampsToReturn'),
        ('ItemsToCreate', 'ListOfMonitoredItemCreateRequest'),
               ]

    def __init__(self):
        self.SubscriptionId = 0
        self.TimestampsToReturn = TimestampsToReturn(0)
        self.ItemsToCreate = []
        self._freeze = True

    def __str__(self):
        return 'CreateMonitoredItemsParameters(' + 'SubscriptionId:' + str(self.SubscriptionId) + ', ' + \
               'TimestampsToReturn:' + str(self.TimestampsToReturn) + ', ' + \
               'ItemsToCreate:' + str(self.ItemsToCreate) + ')'

    __repr__ = __str__


class CreateMonitoredItemsRequest(FrozenClass):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: CreateMonitoredItemsParameters
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('RequestHeader', 'RequestHeader'),
        ('Parameters', 'CreateMonitoredItemsParameters'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.CreateMonitoredItemsRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = CreateMonitoredItemsParameters()
        self._freeze = True

    def __str__(self):
        return 'CreateMonitoredItemsRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'RequestHeader:' + str(self.RequestHeader) + ', ' + \
               'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class CreateMonitoredItemsResponse(FrozenClass):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    :ivar Results:
    :vartype Results: MonitoredItemCreateResult
    :ivar DiagnosticInfos:
    :vartype DiagnosticInfos: DiagnosticInfo
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('ResponseHeader', 'ResponseHeader'),
        ('Results', 'ListOfMonitoredItemCreateResult'),
        ('DiagnosticInfos', 'ListOfDiagnosticInfo'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.CreateMonitoredItemsResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Results = []
        self.DiagnosticInfos = []
        self._freeze = True

    def __str__(self):
        return 'CreateMonitoredItemsResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
               'Results:' + str(self.Results) + ', ' + \
               'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'

    __repr__ = __str__


class MonitoredItemModifyRequest(FrozenClass):
    '''
    :ivar MonitoredItemId:
    :vartype MonitoredItemId: UInt32
    :ivar RequestedParameters:
    :vartype RequestedParameters: MonitoringParameters
    '''

    ua_types = [
        ('MonitoredItemId', 'UInt32'),
        ('RequestedParameters', 'MonitoringParameters'),
               ]

    def __init__(self):
        self.MonitoredItemId = 0
        self.RequestedParameters = MonitoringParameters()
        self._freeze = True

    def __str__(self):
        return 'MonitoredItemModifyRequest(' + 'MonitoredItemId:' + str(self.MonitoredItemId) + ', ' + \
               'RequestedParameters:' + str(self.RequestedParameters) + ')'

    __repr__ = __str__


class MonitoredItemModifyResult(FrozenClass):
    '''
    :ivar StatusCode:
    :vartype StatusCode: StatusCode
    :ivar RevisedSamplingInterval:
    :vartype RevisedSamplingInterval: Double
    :ivar RevisedQueueSize:
    :vartype RevisedQueueSize: UInt32
    :ivar FilterResult:
    :vartype FilterResult: ExtensionObject
    '''

    ua_types = [
        ('StatusCode', 'StatusCode'),
        ('RevisedSamplingInterval', 'Double'),
        ('RevisedQueueSize', 'UInt32'),
        ('FilterResult', 'ExtensionObject'),
               ]

    def __init__(self):
        self.StatusCode = StatusCode()
        self.RevisedSamplingInterval = 0
        self.RevisedQueueSize = 0
        self.FilterResult = ExtensionObject()
        self._freeze = True

    def __str__(self):
        return 'MonitoredItemModifyResult(' + 'StatusCode:' + str(self.StatusCode) + ', ' + \
               'RevisedSamplingInterval:' + str(self.RevisedSamplingInterval) + ', ' + \
               'RevisedQueueSize:' + str(self.RevisedQueueSize) + ', ' + \
               'FilterResult:' + str(self.FilterResult) + ')'

    __repr__ = __str__


class ModifyMonitoredItemsParameters(FrozenClass):
    '''
    :ivar SubscriptionId:
    :vartype SubscriptionId: UInt32
    :ivar TimestampsToReturn:
    :vartype TimestampsToReturn: TimestampsToReturn
    :ivar ItemsToModify:
    :vartype ItemsToModify: MonitoredItemModifyRequest
    '''

    ua_types = [
        ('SubscriptionId', 'UInt32'),
        ('TimestampsToReturn', 'TimestampsToReturn'),
        ('ItemsToModify', 'ListOfMonitoredItemModifyRequest'),
               ]

    def __init__(self):
        self.SubscriptionId = 0
        self.TimestampsToReturn = TimestampsToReturn(0)
        self.ItemsToModify = []
        self._freeze = True

    def __str__(self):
        return 'ModifyMonitoredItemsParameters(' + 'SubscriptionId:' + str(self.SubscriptionId) + ', ' + \
               'TimestampsToReturn:' + str(self.TimestampsToReturn) + ', ' + \
               'ItemsToModify:' + str(self.ItemsToModify) + ')'

    __repr__ = __str__


class ModifyMonitoredItemsRequest(FrozenClass):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: ModifyMonitoredItemsParameters
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('RequestHeader', 'RequestHeader'),
        ('Parameters', 'ModifyMonitoredItemsParameters'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.ModifyMonitoredItemsRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = ModifyMonitoredItemsParameters()
        self._freeze = True

    def __str__(self):
        return 'ModifyMonitoredItemsRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'RequestHeader:' + str(self.RequestHeader) + ', ' + \
               'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class ModifyMonitoredItemsResponse(FrozenClass):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    :ivar Results:
    :vartype Results: MonitoredItemModifyResult
    :ivar DiagnosticInfos:
    :vartype DiagnosticInfos: DiagnosticInfo
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('ResponseHeader', 'ResponseHeader'),
        ('Results', 'ListOfMonitoredItemModifyResult'),
        ('DiagnosticInfos', 'ListOfDiagnosticInfo'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.ModifyMonitoredItemsResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Results = []
        self.DiagnosticInfos = []
        self._freeze = True

    def __str__(self):
        return 'ModifyMonitoredItemsResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
               'Results:' + str(self.Results) + ', ' + \
               'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'

    __repr__ = __str__


class SetMonitoringModeParameters(FrozenClass):
    '''
    :ivar SubscriptionId:
    :vartype SubscriptionId: UInt32
    :ivar MonitoringMode:
    :vartype MonitoringMode: MonitoringMode
    :ivar MonitoredItemIds:
    :vartype MonitoredItemIds: UInt32
    '''

    ua_types = [
        ('SubscriptionId', 'UInt32'),
        ('MonitoringMode', 'MonitoringMode'),
        ('MonitoredItemIds', 'ListOfUInt32'),
               ]

    def __init__(self):
        self.SubscriptionId = 0
        self.MonitoringMode = MonitoringMode(0)
        self.MonitoredItemIds = []
        self._freeze = True

    def __str__(self):
        return 'SetMonitoringModeParameters(' + 'SubscriptionId:' + str(self.SubscriptionId) + ', ' + \
               'MonitoringMode:' + str(self.MonitoringMode) + ', ' + \
               'MonitoredItemIds:' + str(self.MonitoredItemIds) + ')'

    __repr__ = __str__


class SetMonitoringModeRequest(FrozenClass):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: SetMonitoringModeParameters
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('RequestHeader', 'RequestHeader'),
        ('Parameters', 'SetMonitoringModeParameters'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.SetMonitoringModeRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = SetMonitoringModeParameters()
        self._freeze = True

    def __str__(self):
        return 'SetMonitoringModeRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'RequestHeader:' + str(self.RequestHeader) + ', ' + \
               'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class SetMonitoringModeResult(FrozenClass):
    '''
    :ivar Results:
    :vartype Results: StatusCode
    :ivar DiagnosticInfos:
    :vartype DiagnosticInfos: DiagnosticInfo
    '''

    ua_types = [
        ('Results', 'ListOfStatusCode'),
        ('DiagnosticInfos', 'ListOfDiagnosticInfo'),
               ]

    def __init__(self):
        self.Results = []
        self.DiagnosticInfos = []
        self._freeze = True

    def __str__(self):
        return 'SetMonitoringModeResult(' + 'Results:' + str(self.Results) + ', ' + \
               'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'

    __repr__ = __str__


class SetMonitoringModeResponse(FrozenClass):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    :ivar Parameters:
    :vartype Parameters: SetMonitoringModeResult
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('ResponseHeader', 'ResponseHeader'),
        ('Parameters', 'SetMonitoringModeResult'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.SetMonitoringModeResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = SetMonitoringModeResult()
        self._freeze = True

    def __str__(self):
        return 'SetMonitoringModeResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
               'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class SetTriggeringParameters(FrozenClass):
    '''
    :ivar SubscriptionId:
    :vartype SubscriptionId: UInt32
    :ivar TriggeringItemId:
    :vartype TriggeringItemId: UInt32
    :ivar LinksToAdd:
    :vartype LinksToAdd: UInt32
    :ivar LinksToRemove:
    :vartype LinksToRemove: UInt32
    '''

    ua_types = [
        ('SubscriptionId', 'UInt32'),
        ('TriggeringItemId', 'UInt32'),
        ('LinksToAdd', 'ListOfUInt32'),
        ('LinksToRemove', 'ListOfUInt32'),
               ]

    def __init__(self):
        self.SubscriptionId = 0
        self.TriggeringItemId = 0
        self.LinksToAdd = []
        self.LinksToRemove = []
        self._freeze = True

    def __str__(self):
        return 'SetTriggeringParameters(' + 'SubscriptionId:' + str(self.SubscriptionId) + ', ' + \
               'TriggeringItemId:' + str(self.TriggeringItemId) + ', ' + \
               'LinksToAdd:' + str(self.LinksToAdd) + ', ' + \
               'LinksToRemove:' + str(self.LinksToRemove) + ')'

    __repr__ = __str__


class SetTriggeringRequest(FrozenClass):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: SetTriggeringParameters
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('RequestHeader', 'RequestHeader'),
        ('Parameters', 'SetTriggeringParameters'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.SetTriggeringRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = SetTriggeringParameters()
        self._freeze = True

    def __str__(self):
        return 'SetTriggeringRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'RequestHeader:' + str(self.RequestHeader) + ', ' + \
               'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class SetTriggeringResult(FrozenClass):
    '''
    :ivar AddResults:
    :vartype AddResults: StatusCode
    :ivar AddDiagnosticInfos:
    :vartype AddDiagnosticInfos: DiagnosticInfo
    :ivar RemoveResults:
    :vartype RemoveResults: StatusCode
    :ivar RemoveDiagnosticInfos:
    :vartype RemoveDiagnosticInfos: DiagnosticInfo
    '''

    ua_types = [
        ('AddResults', 'ListOfStatusCode'),
        ('AddDiagnosticInfos', 'ListOfDiagnosticInfo'),
        ('RemoveResults', 'ListOfStatusCode'),
        ('RemoveDiagnosticInfos', 'ListOfDiagnosticInfo'),
               ]

    def __init__(self):
        self.AddResults = []
        self.AddDiagnosticInfos = []
        self.RemoveResults = []
        self.RemoveDiagnosticInfos = []
        self._freeze = True

    def __str__(self):
        return 'SetTriggeringResult(' + 'AddResults:' + str(self.AddResults) + ', ' + \
               'AddDiagnosticInfos:' + str(self.AddDiagnosticInfos) + ', ' + \
               'RemoveResults:' + str(self.RemoveResults) + ', ' + \
               'RemoveDiagnosticInfos:' + str(self.RemoveDiagnosticInfos) + ')'

    __repr__ = __str__


class SetTriggeringResponse(FrozenClass):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    :ivar Parameters:
    :vartype Parameters: SetTriggeringResult
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('ResponseHeader', 'ResponseHeader'),
        ('Parameters', 'SetTriggeringResult'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.SetTriggeringResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = SetTriggeringResult()
        self._freeze = True

    def __str__(self):
        return 'SetTriggeringResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
               'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class DeleteMonitoredItemsParameters(FrozenClass):
    '''
    :ivar SubscriptionId:
    :vartype SubscriptionId: UInt32
    :ivar MonitoredItemIds:
    :vartype MonitoredItemIds: UInt32
    '''

    ua_types = [
        ('SubscriptionId', 'UInt32'),
        ('MonitoredItemIds', 'ListOfUInt32'),
               ]

    def __init__(self):
        self.SubscriptionId = 0
        self.MonitoredItemIds = []
        self._freeze = True

    def __str__(self):
        return 'DeleteMonitoredItemsParameters(' + 'SubscriptionId:' + str(self.SubscriptionId) + ', ' + \
               'MonitoredItemIds:' + str(self.MonitoredItemIds) + ')'

    __repr__ = __str__


class DeleteMonitoredItemsRequest(FrozenClass):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: DeleteMonitoredItemsParameters
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('RequestHeader', 'RequestHeader'),
        ('Parameters', 'DeleteMonitoredItemsParameters'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.DeleteMonitoredItemsRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = DeleteMonitoredItemsParameters()
        self._freeze = True

    def __str__(self):
        return 'DeleteMonitoredItemsRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'RequestHeader:' + str(self.RequestHeader) + ', ' + \
               'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class DeleteMonitoredItemsResponse(FrozenClass):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    :ivar Results:
    :vartype Results: StatusCode
    :ivar DiagnosticInfos:
    :vartype DiagnosticInfos: DiagnosticInfo
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('ResponseHeader', 'ResponseHeader'),
        ('Results', 'ListOfStatusCode'),
        ('DiagnosticInfos', 'ListOfDiagnosticInfo'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.DeleteMonitoredItemsResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Results = []
        self.DiagnosticInfos = []
        self._freeze = True

    def __str__(self):
        return 'DeleteMonitoredItemsResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
               'Results:' + str(self.Results) + ', ' + \
               'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'

    __repr__ = __str__


class CreateSubscriptionParameters(FrozenClass):
    '''
    :ivar RequestedPublishingInterval:
    :vartype RequestedPublishingInterval: Double
    :ivar RequestedLifetimeCount:
    :vartype RequestedLifetimeCount: UInt32
    :ivar RequestedMaxKeepAliveCount:
    :vartype RequestedMaxKeepAliveCount: UInt32
    :ivar MaxNotificationsPerPublish:
    :vartype MaxNotificationsPerPublish: UInt32
    :ivar PublishingEnabled:
    :vartype PublishingEnabled: Boolean
    :ivar Priority:
    :vartype Priority: Byte
    '''

    ua_types = [
        ('RequestedPublishingInterval', 'Double'),
        ('RequestedLifetimeCount', 'UInt32'),
        ('RequestedMaxKeepAliveCount', 'UInt32'),
        ('MaxNotificationsPerPublish', 'UInt32'),
        ('PublishingEnabled', 'Boolean'),
        ('Priority', 'Byte'),
               ]

    def __init__(self):
        self.RequestedPublishingInterval = 0
        self.RequestedLifetimeCount = 0
        self.RequestedMaxKeepAliveCount = 0
        self.MaxNotificationsPerPublish = 0
        self.PublishingEnabled = True
        self.Priority = 0
        self._freeze = True

    def __str__(self):
        return 'CreateSubscriptionParameters(' + 'RequestedPublishingInterval:' + str(self.RequestedPublishingInterval) + ', ' + \
               'RequestedLifetimeCount:' + str(self.RequestedLifetimeCount) + ', ' + \
               'RequestedMaxKeepAliveCount:' + str(self.RequestedMaxKeepAliveCount) + ', ' + \
               'MaxNotificationsPerPublish:' + str(self.MaxNotificationsPerPublish) + ', ' + \
               'PublishingEnabled:' + str(self.PublishingEnabled) + ', ' + \
               'Priority:' + str(self.Priority) + ')'

    __repr__ = __str__


class CreateSubscriptionRequest(FrozenClass):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: CreateSubscriptionParameters
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('RequestHeader', 'RequestHeader'),
        ('Parameters', 'CreateSubscriptionParameters'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.CreateSubscriptionRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = CreateSubscriptionParameters()
        self._freeze = True

    def __str__(self):
        return 'CreateSubscriptionRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'RequestHeader:' + str(self.RequestHeader) + ', ' + \
               'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class CreateSubscriptionResult(FrozenClass):
    '''
    :ivar SubscriptionId:
    :vartype SubscriptionId: UInt32
    :ivar RevisedPublishingInterval:
    :vartype RevisedPublishingInterval: Double
    :ivar RevisedLifetimeCount:
    :vartype RevisedLifetimeCount: UInt32
    :ivar RevisedMaxKeepAliveCount:
    :vartype RevisedMaxKeepAliveCount: UInt32
    '''

    ua_types = [
        ('SubscriptionId', 'UInt32'),
        ('RevisedPublishingInterval', 'Double'),
        ('RevisedLifetimeCount', 'UInt32'),
        ('RevisedMaxKeepAliveCount', 'UInt32'),
               ]

    def __init__(self):
        self.SubscriptionId = 0
        self.RevisedPublishingInterval = 0
        self.RevisedLifetimeCount = 0
        self.RevisedMaxKeepAliveCount = 0
        self._freeze = True

    def __str__(self):
        return 'CreateSubscriptionResult(' + 'SubscriptionId:' + str(self.SubscriptionId) + ', ' + \
               'RevisedPublishingInterval:' + str(self.RevisedPublishingInterval) + ', ' + \
               'RevisedLifetimeCount:' + str(self.RevisedLifetimeCount) + ', ' + \
               'RevisedMaxKeepAliveCount:' + str(self.RevisedMaxKeepAliveCount) + ')'

    __repr__ = __str__


class CreateSubscriptionResponse(FrozenClass):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    :ivar Parameters:
    :vartype Parameters: CreateSubscriptionResult
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('ResponseHeader', 'ResponseHeader'),
        ('Parameters', 'CreateSubscriptionResult'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.CreateSubscriptionResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = CreateSubscriptionResult()
        self._freeze = True

    def __str__(self):
        return 'CreateSubscriptionResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
               'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class ModifySubscriptionParameters(FrozenClass):
    '''
    :ivar SubscriptionId:
    :vartype SubscriptionId: UInt32
    :ivar RequestedPublishingInterval:
    :vartype RequestedPublishingInterval: Double
    :ivar RequestedLifetimeCount:
    :vartype RequestedLifetimeCount: UInt32
    :ivar RequestedMaxKeepAliveCount:
    :vartype RequestedMaxKeepAliveCount: UInt32
    :ivar MaxNotificationsPerPublish:
    :vartype MaxNotificationsPerPublish: UInt32
    :ivar Priority:
    :vartype Priority: Byte
    '''

    ua_types = [
        ('SubscriptionId', 'UInt32'),
        ('RequestedPublishingInterval', 'Double'),
        ('RequestedLifetimeCount', 'UInt32'),
        ('RequestedMaxKeepAliveCount', 'UInt32'),
        ('MaxNotificationsPerPublish', 'UInt32'),
        ('Priority', 'Byte'),
               ]

    def __init__(self):
        self.SubscriptionId = 0
        self.RequestedPublishingInterval = 0
        self.RequestedLifetimeCount = 0
        self.RequestedMaxKeepAliveCount = 0
        self.MaxNotificationsPerPublish = 0
        self.Priority = 0
        self._freeze = True

    def __str__(self):
        return 'ModifySubscriptionParameters(' + 'SubscriptionId:' + str(self.SubscriptionId) + ', ' + \
               'RequestedPublishingInterval:' + str(self.RequestedPublishingInterval) + ', ' + \
               'RequestedLifetimeCount:' + str(self.RequestedLifetimeCount) + ', ' + \
               'RequestedMaxKeepAliveCount:' + str(self.RequestedMaxKeepAliveCount) + ', ' + \
               'MaxNotificationsPerPublish:' + str(self.MaxNotificationsPerPublish) + ', ' + \
               'Priority:' + str(self.Priority) + ')'

    __repr__ = __str__


class ModifySubscriptionRequest(FrozenClass):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: ModifySubscriptionParameters
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('RequestHeader', 'RequestHeader'),
        ('Parameters', 'ModifySubscriptionParameters'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.ModifySubscriptionRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = ModifySubscriptionParameters()
        self._freeze = True

    def __str__(self):
        return 'ModifySubscriptionRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'RequestHeader:' + str(self.RequestHeader) + ', ' + \
               'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class ModifySubscriptionResult(FrozenClass):
    '''
    :ivar RevisedPublishingInterval:
    :vartype RevisedPublishingInterval: Double
    :ivar RevisedLifetimeCount:
    :vartype RevisedLifetimeCount: UInt32
    :ivar RevisedMaxKeepAliveCount:
    :vartype RevisedMaxKeepAliveCount: UInt32
    '''

    ua_types = [
        ('RevisedPublishingInterval', 'Double'),
        ('RevisedLifetimeCount', 'UInt32'),
        ('RevisedMaxKeepAliveCount', 'UInt32'),
               ]

    def __init__(self):
        self.RevisedPublishingInterval = 0
        self.RevisedLifetimeCount = 0
        self.RevisedMaxKeepAliveCount = 0
        self._freeze = True

    def __str__(self):
        return 'ModifySubscriptionResult(' + 'RevisedPublishingInterval:' + str(self.RevisedPublishingInterval) + ', ' + \
               'RevisedLifetimeCount:' + str(self.RevisedLifetimeCount) + ', ' + \
               'RevisedMaxKeepAliveCount:' + str(self.RevisedMaxKeepAliveCount) + ')'

    __repr__ = __str__


class ModifySubscriptionResponse(FrozenClass):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    :ivar Parameters:
    :vartype Parameters: ModifySubscriptionResult
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('ResponseHeader', 'ResponseHeader'),
        ('Parameters', 'ModifySubscriptionResult'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.ModifySubscriptionResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = ModifySubscriptionResult()
        self._freeze = True

    def __str__(self):
        return 'ModifySubscriptionResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
               'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class SetPublishingModeParameters(FrozenClass):
    '''
    :ivar PublishingEnabled:
    :vartype PublishingEnabled: Boolean
    :ivar SubscriptionIds:
    :vartype SubscriptionIds: UInt32
    '''

    ua_types = [
        ('PublishingEnabled', 'Boolean'),
        ('SubscriptionIds', 'ListOfUInt32'),
               ]

    def __init__(self):
        self.PublishingEnabled = True
        self.SubscriptionIds = []
        self._freeze = True

    def __str__(self):
        return 'SetPublishingModeParameters(' + 'PublishingEnabled:' + str(self.PublishingEnabled) + ', ' + \
               'SubscriptionIds:' + str(self.SubscriptionIds) + ')'

    __repr__ = __str__


class SetPublishingModeRequest(FrozenClass):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: SetPublishingModeParameters
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('RequestHeader', 'RequestHeader'),
        ('Parameters', 'SetPublishingModeParameters'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.SetPublishingModeRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = SetPublishingModeParameters()
        self._freeze = True

    def __str__(self):
        return 'SetPublishingModeRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'RequestHeader:' + str(self.RequestHeader) + ', ' + \
               'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class SetPublishingModeResult(FrozenClass):
    '''
    :ivar Results:
    :vartype Results: StatusCode
    :ivar DiagnosticInfos:
    :vartype DiagnosticInfos: DiagnosticInfo
    '''

    ua_types = [
        ('Results', 'ListOfStatusCode'),
        ('DiagnosticInfos', 'ListOfDiagnosticInfo'),
               ]

    def __init__(self):
        self.Results = []
        self.DiagnosticInfos = []
        self._freeze = True

    def __str__(self):
        return 'SetPublishingModeResult(' + 'Results:' + str(self.Results) + ', ' + \
               'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'

    __repr__ = __str__


class SetPublishingModeResponse(FrozenClass):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    :ivar Parameters:
    :vartype Parameters: SetPublishingModeResult
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('ResponseHeader', 'ResponseHeader'),
        ('Parameters', 'SetPublishingModeResult'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.SetPublishingModeResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = SetPublishingModeResult()
        self._freeze = True

    def __str__(self):
        return 'SetPublishingModeResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
               'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class NotificationMessage(FrozenClass):
    '''
    :ivar SequenceNumber:
    :vartype SequenceNumber: UInt32
    :ivar PublishTime:
    :vartype PublishTime: DateTime
    :ivar NotificationData:
    :vartype NotificationData: ExtensionObject
    '''

    ua_types = [
        ('SequenceNumber', 'UInt32'),
        ('PublishTime', 'DateTime'),
        ('NotificationData', 'ListOfExtensionObject'),
               ]

    def __init__(self):
        self.SequenceNumber = 0
        self.PublishTime = datetime.utcnow()
        self.NotificationData = []
        self._freeze = True

    def __str__(self):
        return 'NotificationMessage(' + 'SequenceNumber:' + str(self.SequenceNumber) + ', ' + \
               'PublishTime:' + str(self.PublishTime) + ', ' + \
               'NotificationData:' + str(self.NotificationData) + ')'

    __repr__ = __str__


class NotificationData(FrozenClass):
    '''
    '''

    ua_types = [
               ]

    def __init__(self):
        self._freeze = True

    def __str__(self):
        return 'NotificationData(' +  + ')'

    __repr__ = __str__


class DataChangeNotification(FrozenClass):
    '''
    :ivar MonitoredItems:
    :vartype MonitoredItems: MonitoredItemNotification
    :ivar DiagnosticInfos:
    :vartype DiagnosticInfos: DiagnosticInfo
    '''

    ua_types = [
        ('MonitoredItems', 'ListOfMonitoredItemNotification'),
        ('DiagnosticInfos', 'ListOfDiagnosticInfo'),
               ]

    def __init__(self):
        self.MonitoredItems = []
        self.DiagnosticInfos = []
        self._freeze = True

    def __str__(self):
        return 'DataChangeNotification(' + 'MonitoredItems:' + str(self.MonitoredItems) + ', ' + \
               'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'

    __repr__ = __str__


class MonitoredItemNotification(FrozenClass):
    '''
    :ivar ClientHandle:
    :vartype ClientHandle: UInt32
    :ivar Value:
    :vartype Value: DataValue
    '''

    ua_types = [
        ('ClientHandle', 'UInt32'),
        ('Value', 'DataValue'),
               ]

    def __init__(self):
        self.ClientHandle = 0
        self.Value = DataValue()
        self._freeze = True

    def __str__(self):
        return 'MonitoredItemNotification(' + 'ClientHandle:' + str(self.ClientHandle) + ', ' + \
               'Value:' + str(self.Value) + ')'

    __repr__ = __str__


class EventNotificationList(FrozenClass):
    '''
    :ivar Events:
    :vartype Events: EventFieldList
    '''

    ua_types = [
        ('Events', 'ListOfEventFieldList'),
               ]

    def __init__(self):
        self.Events = []
        self._freeze = True

    def __str__(self):
        return 'EventNotificationList(' + 'Events:' + str(self.Events) + ')'

    __repr__ = __str__


class EventFieldList(FrozenClass):
    '''
    :ivar ClientHandle:
    :vartype ClientHandle: UInt32
    :ivar EventFields:
    :vartype EventFields: Variant
    '''

    ua_types = [
        ('ClientHandle', 'UInt32'),
        ('EventFields', 'ListOfVariant'),
               ]

    def __init__(self):
        self.ClientHandle = 0
        self.EventFields = []
        self._freeze = True

    def __str__(self):
        return 'EventFieldList(' + 'ClientHandle:' + str(self.ClientHandle) + ', ' + \
               'EventFields:' + str(self.EventFields) + ')'

    __repr__ = __str__


class HistoryEventFieldList(FrozenClass):
    '''
    :ivar EventFields:
    :vartype EventFields: Variant
    '''

    ua_types = [
        ('EventFields', 'ListOfVariant'),
               ]

    def __init__(self):
        self.EventFields = []
        self._freeze = True

    def __str__(self):
        return 'HistoryEventFieldList(' + 'EventFields:' + str(self.EventFields) + ')'

    __repr__ = __str__


class StatusChangeNotification(FrozenClass):
    '''
    :ivar Status:
    :vartype Status: StatusCode
    :ivar DiagnosticInfo:
    :vartype DiagnosticInfo: DiagnosticInfo
    '''

    ua_types = [
        ('Status', 'StatusCode'),
        ('DiagnosticInfo', 'DiagnosticInfo'),
               ]

    def __init__(self):
        self.Status = StatusCode()
        self.DiagnosticInfo = DiagnosticInfo()
        self._freeze = True

    def __str__(self):
        return 'StatusChangeNotification(' + 'Status:' + str(self.Status) + ', ' + \
               'DiagnosticInfo:' + str(self.DiagnosticInfo) + ')'

    __repr__ = __str__


class SubscriptionAcknowledgement(FrozenClass):
    '''
    :ivar SubscriptionId:
    :vartype SubscriptionId: UInt32
    :ivar SequenceNumber:
    :vartype SequenceNumber: UInt32
    '''

    ua_types = [
        ('SubscriptionId', 'UInt32'),
        ('SequenceNumber', 'UInt32'),
               ]

    def __init__(self):
        self.SubscriptionId = 0
        self.SequenceNumber = 0
        self._freeze = True

    def __str__(self):
        return 'SubscriptionAcknowledgement(' + 'SubscriptionId:' + str(self.SubscriptionId) + ', ' + \
               'SequenceNumber:' + str(self.SequenceNumber) + ')'

    __repr__ = __str__


class PublishParameters(FrozenClass):
    '''
    :ivar SubscriptionAcknowledgements:
    :vartype SubscriptionAcknowledgements: SubscriptionAcknowledgement
    '''

    ua_types = [
        ('SubscriptionAcknowledgements', 'ListOfSubscriptionAcknowledgement'),
               ]

    def __init__(self):
        self.SubscriptionAcknowledgements = []
        self._freeze = True

    def __str__(self):
        return 'PublishParameters(' + 'SubscriptionAcknowledgements:' + str(self.SubscriptionAcknowledgements) + ')'

    __repr__ = __str__


class PublishRequest(FrozenClass):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: PublishParameters
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('RequestHeader', 'RequestHeader'),
        ('Parameters', 'PublishParameters'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.PublishRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = PublishParameters()
        self._freeze = True

    def __str__(self):
        return 'PublishRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'RequestHeader:' + str(self.RequestHeader) + ', ' + \
               'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class PublishResult(FrozenClass):
    '''
    :ivar SubscriptionId:
    :vartype SubscriptionId: UInt32
    :ivar AvailableSequenceNumbers:
    :vartype AvailableSequenceNumbers: UInt32
    :ivar MoreNotifications:
    :vartype MoreNotifications: Boolean
    :ivar NotificationMessage:
    :vartype NotificationMessage: NotificationMessage
    :ivar Results:
    :vartype Results: StatusCode
    :ivar DiagnosticInfos:
    :vartype DiagnosticInfos: DiagnosticInfo
    '''

    ua_types = [
        ('SubscriptionId', 'UInt32'),
        ('AvailableSequenceNumbers', 'ListOfUInt32'),
        ('MoreNotifications', 'Boolean'),
        ('NotificationMessage', 'NotificationMessage'),
        ('Results', 'ListOfStatusCode'),
        ('DiagnosticInfos', 'ListOfDiagnosticInfo'),
               ]

    def __init__(self):
        self.SubscriptionId = 0
        self.AvailableSequenceNumbers = []
        self.MoreNotifications = True
        self.NotificationMessage = NotificationMessage()
        self.Results = []
        self.DiagnosticInfos = []
        self._freeze = True

    def __str__(self):
        return 'PublishResult(' + 'SubscriptionId:' + str(self.SubscriptionId) + ', ' + \
               'AvailableSequenceNumbers:' + str(self.AvailableSequenceNumbers) + ', ' + \
               'MoreNotifications:' + str(self.MoreNotifications) + ', ' + \
               'NotificationMessage:' + str(self.NotificationMessage) + ', ' + \
               'Results:' + str(self.Results) + ', ' + \
               'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'

    __repr__ = __str__


class PublishResponse(FrozenClass):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    :ivar Parameters:
    :vartype Parameters: PublishResult
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('ResponseHeader', 'ResponseHeader'),
        ('Parameters', 'PublishResult'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.PublishResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = PublishResult()
        self._freeze = True

    def __str__(self):
        return 'PublishResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
               'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class RepublishParameters(FrozenClass):
    '''
    :ivar SubscriptionId:
    :vartype SubscriptionId: UInt32
    :ivar RetransmitSequenceNumber:
    :vartype RetransmitSequenceNumber: UInt32
    '''

    ua_types = [
        ('SubscriptionId', 'UInt32'),
        ('RetransmitSequenceNumber', 'UInt32'),
               ]

    def __init__(self):
        self.SubscriptionId = 0
        self.RetransmitSequenceNumber = 0
        self._freeze = True

    def __str__(self):
        return 'RepublishParameters(' + 'SubscriptionId:' + str(self.SubscriptionId) + ', ' + \
               'RetransmitSequenceNumber:' + str(self.RetransmitSequenceNumber) + ')'

    __repr__ = __str__


class RepublishRequest(FrozenClass):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: RepublishParameters
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('RequestHeader', 'RequestHeader'),
        ('Parameters', 'RepublishParameters'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.RepublishRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = RepublishParameters()
        self._freeze = True

    def __str__(self):
        return 'RepublishRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'RequestHeader:' + str(self.RequestHeader) + ', ' + \
               'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class RepublishResponse(FrozenClass):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    :ivar NotificationMessage:
    :vartype NotificationMessage: NotificationMessage
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('ResponseHeader', 'ResponseHeader'),
        ('NotificationMessage', 'NotificationMessage'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.RepublishResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.NotificationMessage = NotificationMessage()
        self._freeze = True

    def __str__(self):
        return 'RepublishResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
               'NotificationMessage:' + str(self.NotificationMessage) + ')'

    __repr__ = __str__


class TransferResult(FrozenClass):
    '''
    :ivar StatusCode:
    :vartype StatusCode: StatusCode
    :ivar AvailableSequenceNumbers:
    :vartype AvailableSequenceNumbers: UInt32
    '''

    ua_types = [
        ('StatusCode', 'StatusCode'),
        ('AvailableSequenceNumbers', 'ListOfUInt32'),
               ]

    def __init__(self):
        self.StatusCode = StatusCode()
        self.AvailableSequenceNumbers = []
        self._freeze = True

    def __str__(self):
        return 'TransferResult(' + 'StatusCode:' + str(self.StatusCode) + ', ' + \
               'AvailableSequenceNumbers:' + str(self.AvailableSequenceNumbers) + ')'

    __repr__ = __str__


class TransferSubscriptionsParameters(FrozenClass):
    '''
    :ivar SubscriptionIds:
    :vartype SubscriptionIds: UInt32
    :ivar SendInitialValues:
    :vartype SendInitialValues: Boolean
    '''

    ua_types = [
        ('SubscriptionIds', 'ListOfUInt32'),
        ('SendInitialValues', 'Boolean'),
               ]

    def __init__(self):
        self.SubscriptionIds = []
        self.SendInitialValues = True
        self._freeze = True

    def __str__(self):
        return 'TransferSubscriptionsParameters(' + 'SubscriptionIds:' + str(self.SubscriptionIds) + ', ' + \
               'SendInitialValues:' + str(self.SendInitialValues) + ')'

    __repr__ = __str__


class TransferSubscriptionsRequest(FrozenClass):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: TransferSubscriptionsParameters
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('RequestHeader', 'RequestHeader'),
        ('Parameters', 'TransferSubscriptionsParameters'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.TransferSubscriptionsRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = TransferSubscriptionsParameters()
        self._freeze = True

    def __str__(self):
        return 'TransferSubscriptionsRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'RequestHeader:' + str(self.RequestHeader) + ', ' + \
               'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class TransferSubscriptionsResult(FrozenClass):
    '''
    :ivar Results:
    :vartype Results: TransferResult
    :ivar DiagnosticInfos:
    :vartype DiagnosticInfos: DiagnosticInfo
    '''

    ua_types = [
        ('Results', 'ListOfTransferResult'),
        ('DiagnosticInfos', 'ListOfDiagnosticInfo'),
               ]

    def __init__(self):
        self.Results = []
        self.DiagnosticInfos = []
        self._freeze = True

    def __str__(self):
        return 'TransferSubscriptionsResult(' + 'Results:' + str(self.Results) + ', ' + \
               'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'

    __repr__ = __str__


class TransferSubscriptionsResponse(FrozenClass):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    :ivar Parameters:
    :vartype Parameters: TransferSubscriptionsResult
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('ResponseHeader', 'ResponseHeader'),
        ('Parameters', 'TransferSubscriptionsResult'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.TransferSubscriptionsResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = TransferSubscriptionsResult()
        self._freeze = True

    def __str__(self):
        return 'TransferSubscriptionsResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
               'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class DeleteSubscriptionsParameters(FrozenClass):
    '''
    :ivar SubscriptionIds:
    :vartype SubscriptionIds: UInt32
    '''

    ua_types = [
        ('SubscriptionIds', 'ListOfUInt32'),
               ]

    def __init__(self):
        self.SubscriptionIds = []
        self._freeze = True

    def __str__(self):
        return 'DeleteSubscriptionsParameters(' + 'SubscriptionIds:' + str(self.SubscriptionIds) + ')'

    __repr__ = __str__


class DeleteSubscriptionsRequest(FrozenClass):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: DeleteSubscriptionsParameters
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('RequestHeader', 'RequestHeader'),
        ('Parameters', 'DeleteSubscriptionsParameters'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.DeleteSubscriptionsRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = DeleteSubscriptionsParameters()
        self._freeze = True

    def __str__(self):
        return 'DeleteSubscriptionsRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'RequestHeader:' + str(self.RequestHeader) + ', ' + \
               'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class DeleteSubscriptionsResponse(FrozenClass):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    :ivar Results:
    :vartype Results: StatusCode
    :ivar DiagnosticInfos:
    :vartype DiagnosticInfos: DiagnosticInfo
    '''

    ua_types = [
        ('TypeId', 'NodeId'),
        ('ResponseHeader', 'ResponseHeader'),
        ('Results', 'ListOfStatusCode'),
        ('DiagnosticInfos', 'ListOfDiagnosticInfo'),
               ]

    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.DeleteSubscriptionsResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Results = []
        self.DiagnosticInfos = []
        self._freeze = True

    def __str__(self):
        return 'DeleteSubscriptionsResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
               'Results:' + str(self.Results) + ', ' + \
               'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'

    __repr__ = __str__


class BuildInfo(FrozenClass):
    '''
    :ivar ProductUri:
    :vartype ProductUri: String
    :ivar ManufacturerName:
    :vartype ManufacturerName: String
    :ivar ProductName:
    :vartype ProductName: String
    :ivar SoftwareVersion:
    :vartype SoftwareVersion: String
    :ivar BuildNumber:
    :vartype BuildNumber: String
    :ivar BuildDate:
    :vartype BuildDate: DateTime
    '''

    ua_types = [
        ('ProductUri', 'String'),
        ('ManufacturerName', 'String'),
        ('ProductName', 'String'),
        ('SoftwareVersion', 'String'),
        ('BuildNumber', 'String'),
        ('BuildDate', 'DateTime'),
               ]

    def __init__(self):
        self.ProductUri = None
        self.ManufacturerName = None
        self.ProductName = None
        self.SoftwareVersion = None
        self.BuildNumber = None
        self.BuildDate = datetime.utcnow()
        self._freeze = True

    def __str__(self):
        return 'BuildInfo(' + 'ProductUri:' + str(self.ProductUri) + ', ' + \
               'ManufacturerName:' + str(self.ManufacturerName) + ', ' + \
               'ProductName:' + str(self.ProductName) + ', ' + \
               'SoftwareVersion:' + str(self.SoftwareVersion) + ', ' + \
               'BuildNumber:' + str(self.BuildNumber) + ', ' + \
               'BuildDate:' + str(self.BuildDate) + ')'

    __repr__ = __str__


class RedundantServerDataType(FrozenClass):
    '''
    :ivar ServerId:
    :vartype ServerId: String
    :ivar ServiceLevel:
    :vartype ServiceLevel: Byte
    :ivar ServerState:
    :vartype ServerState: ServerState
    '''

    ua_types = [
        ('ServerId', 'String'),
        ('ServiceLevel', 'Byte'),
        ('ServerState', 'ServerState'),
               ]

    def __init__(self):
        self.ServerId = None
        self.ServiceLevel = 0
        self.ServerState = ServerState(0)
        self._freeze = True

    def __str__(self):
        return 'RedundantServerDataType(' + 'ServerId:' + str(self.ServerId) + ', ' + \
               'ServiceLevel:' + str(self.ServiceLevel) + ', ' + \
               'ServerState:' + str(self.ServerState) + ')'

    __repr__ = __str__


class EndpointUrlListDataType(FrozenClass):
    '''
    :ivar EndpointUrlList:
    :vartype EndpointUrlList: String
    '''

    ua_types = [
        ('EndpointUrlList', 'ListOfString'),
               ]

    def __init__(self):
        self.EndpointUrlList = []
        self._freeze = True

    def __str__(self):
        return 'EndpointUrlListDataType(' + 'EndpointUrlList:' + str(self.EndpointUrlList) + ')'

    __repr__ = __str__


class NetworkGroupDataType(FrozenClass):
    '''
    :ivar ServerUri:
    :vartype ServerUri: String
    :ivar NetworkPaths:
    :vartype NetworkPaths: EndpointUrlListDataType
    '''

    ua_types = [
        ('ServerUri', 'String'),
        ('NetworkPaths', 'ListOfEndpointUrlListDataType'),
               ]

    def __init__(self):
        self.ServerUri = None
        self.NetworkPaths = []
        self._freeze = True

    def __str__(self):
        return 'NetworkGroupDataType(' + 'ServerUri:' + str(self.ServerUri) + ', ' + \
               'NetworkPaths:' + str(self.NetworkPaths) + ')'

    __repr__ = __str__


class SamplingIntervalDiagnosticsDataType(FrozenClass):
    '''
    :ivar SamplingInterval:
    :vartype SamplingInterval: Double
    :ivar MonitoredItemCount:
    :vartype MonitoredItemCount: UInt32
    :ivar MaxMonitoredItemCount:
    :vartype MaxMonitoredItemCount: UInt32
    :ivar DisabledMonitoredItemCount:
    :vartype DisabledMonitoredItemCount: UInt32
    '''

    ua_types = [
        ('SamplingInterval', 'Double'),
        ('MonitoredItemCount', 'UInt32'),
        ('MaxMonitoredItemCount', 'UInt32'),
        ('DisabledMonitoredItemCount', 'UInt32'),
               ]

    def __init__(self):
        self.SamplingInterval = 0
        self.MonitoredItemCount = 0
        self.MaxMonitoredItemCount = 0
        self.DisabledMonitoredItemCount = 0
        self._freeze = True

    def __str__(self):
        return 'SamplingIntervalDiagnosticsDataType(' + 'SamplingInterval:' + str(self.SamplingInterval) + ', ' + \
               'MonitoredItemCount:' + str(self.MonitoredItemCount) + ', ' + \
               'MaxMonitoredItemCount:' + str(self.MaxMonitoredItemCount) + ', ' + \
               'DisabledMonitoredItemCount:' + str(self.DisabledMonitoredItemCount) + ')'

    __repr__ = __str__


class ServerDiagnosticsSummaryDataType(FrozenClass):
    '''
    :ivar ServerViewCount:
    :vartype ServerViewCount: UInt32
    :ivar CurrentSessionCount:
    :vartype CurrentSessionCount: UInt32
    :ivar CumulatedSessionCount:
    :vartype CumulatedSessionCount: UInt32
    :ivar SecurityRejectedSessionCount:
    :vartype SecurityRejectedSessionCount: UInt32
    :ivar RejectedSessionCount:
    :vartype RejectedSessionCount: UInt32
    :ivar SessionTimeoutCount:
    :vartype SessionTimeoutCount: UInt32
    :ivar SessionAbortCount:
    :vartype SessionAbortCount: UInt32
    :ivar CurrentSubscriptionCount:
    :vartype CurrentSubscriptionCount: UInt32
    :ivar CumulatedSubscriptionCount:
    :vartype CumulatedSubscriptionCount: UInt32
    :ivar PublishingIntervalCount:
    :vartype PublishingIntervalCount: UInt32
    :ivar SecurityRejectedRequestsCount:
    :vartype SecurityRejectedRequestsCount: UInt32
    :ivar RejectedRequestsCount:
    :vartype RejectedRequestsCount: UInt32
    '''

    ua_types = [
        ('ServerViewCount', 'UInt32'),
        ('CurrentSessionCount', 'UInt32'),
        ('CumulatedSessionCount', 'UInt32'),
        ('SecurityRejectedSessionCount', 'UInt32'),
        ('RejectedSessionCount', 'UInt32'),
        ('SessionTimeoutCount', 'UInt32'),
        ('SessionAbortCount', 'UInt32'),
        ('CurrentSubscriptionCount', 'UInt32'),
        ('CumulatedSubscriptionCount', 'UInt32'),
        ('PublishingIntervalCount', 'UInt32'),
        ('SecurityRejectedRequestsCount', 'UInt32'),
        ('RejectedRequestsCount', 'UInt32'),
               ]

    def __init__(self):
        self.ServerViewCount = 0
        self.CurrentSessionCount = 0
        self.CumulatedSessionCount = 0
        self.SecurityRejectedSessionCount = 0
        self.RejectedSessionCount = 0
        self.SessionTimeoutCount = 0
        self.SessionAbortCount = 0
        self.CurrentSubscriptionCount = 0
        self.CumulatedSubscriptionCount = 0
        self.PublishingIntervalCount = 0
        self.SecurityRejectedRequestsCount = 0
        self.RejectedRequestsCount = 0
        self._freeze = True

    def __str__(self):
        return 'ServerDiagnosticsSummaryDataType(' + 'ServerViewCount:' + str(self.ServerViewCount) + ', ' + \
               'CurrentSessionCount:' + str(self.CurrentSessionCount) + ', ' + \
               'CumulatedSessionCount:' + str(self.CumulatedSessionCount) + ', ' + \
               'SecurityRejectedSessionCount:' + str(self.SecurityRejectedSessionCount) + ', ' + \
               'RejectedSessionCount:' + str(self.RejectedSessionCount) + ', ' + \
               'SessionTimeoutCount:' + str(self.SessionTimeoutCount) + ', ' + \
               'SessionAbortCount:' + str(self.SessionAbortCount) + ', ' + \
               'CurrentSubscriptionCount:' + str(self.CurrentSubscriptionCount) + ', ' + \
               'CumulatedSubscriptionCount:' + str(self.CumulatedSubscriptionCount) + ', ' + \
               'PublishingIntervalCount:' + str(self.PublishingIntervalCount) + ', ' + \
               'SecurityRejectedRequestsCount:' + str(self.SecurityRejectedRequestsCount) + ', ' + \
               'RejectedRequestsCount:' + str(self.RejectedRequestsCount) + ')'

    __repr__ = __str__


class ServerStatusDataType(FrozenClass):
    '''
    :ivar StartTime:
    :vartype StartTime: DateTime
    :ivar CurrentTime:
    :vartype CurrentTime: DateTime
    :ivar State:
    :vartype State: ServerState
    :ivar BuildInfo:
    :vartype BuildInfo: BuildInfo
    :ivar SecondsTillShutdown:
    :vartype SecondsTillShutdown: UInt32
    :ivar ShutdownReason:
    :vartype ShutdownReason: LocalizedText
    '''

    ua_types = [
        ('StartTime', 'DateTime'),
        ('CurrentTime', 'DateTime'),
        ('State', 'ServerState'),
        ('BuildInfo', 'BuildInfo'),
        ('SecondsTillShutdown', 'UInt32'),
        ('ShutdownReason', 'LocalizedText'),
               ]

    def __init__(self):
        self.StartTime = datetime.utcnow()
        self.CurrentTime = datetime.utcnow()
        self.State = ServerState(0)
        self.BuildInfo = BuildInfo()
        self.SecondsTillShutdown = 0
        self.ShutdownReason = LocalizedText()
        self._freeze = True

    def __str__(self):
        return 'ServerStatusDataType(' + 'StartTime:' + str(self.StartTime) + ', ' + \
               'CurrentTime:' + str(self.CurrentTime) + ', ' + \
               'State:' + str(self.State) + ', ' + \
               'BuildInfo:' + str(self.BuildInfo) + ', ' + \
               'SecondsTillShutdown:' + str(self.SecondsTillShutdown) + ', ' + \
               'ShutdownReason:' + str(self.ShutdownReason) + ')'

    __repr__ = __str__


class SessionDiagnosticsDataType(FrozenClass):
    '''
    :ivar SessionId:
    :vartype SessionId: NodeId
    :ivar SessionName:
    :vartype SessionName: String
    :ivar ClientDescription:
    :vartype ClientDescription: ApplicationDescription
    :ivar ServerUri:
    :vartype ServerUri: String
    :ivar EndpointUrl:
    :vartype EndpointUrl: String
    :ivar LocaleIds:
    :vartype LocaleIds: String
    :ivar ActualSessionTimeout:
    :vartype ActualSessionTimeout: Double
    :ivar MaxResponseMessageSize:
    :vartype MaxResponseMessageSize: UInt32
    :ivar ClientConnectionTime:
    :vartype ClientConnectionTime: DateTime
    :ivar ClientLastContactTime:
    :vartype ClientLastContactTime: DateTime
    :ivar CurrentSubscriptionsCount:
    :vartype CurrentSubscriptionsCount: UInt32
    :ivar CurrentMonitoredItemsCount:
    :vartype CurrentMonitoredItemsCount: UInt32
    :ivar CurrentPublishRequestsInQueue:
    :vartype CurrentPublishRequestsInQueue: UInt32
    :ivar TotalRequestCount:
    :vartype TotalRequestCount: ServiceCounterDataType
    :ivar UnauthorizedRequestCount:
    :vartype UnauthorizedRequestCount: UInt32
    :ivar ReadCount:
    :vartype ReadCount: ServiceCounterDataType
    :ivar HistoryReadCount:
    :vartype HistoryReadCount: ServiceCounterDataType
    :ivar WriteCount:
    :vartype WriteCount: ServiceCounterDataType
    :ivar HistoryUpdateCount:
    :vartype HistoryUpdateCount: ServiceCounterDataType
    :ivar CallCount:
    :vartype CallCount: ServiceCounterDataType
    :ivar CreateMonitoredItemsCount:
    :vartype CreateMonitoredItemsCount: ServiceCounterDataType
    :ivar ModifyMonitoredItemsCount:
    :vartype ModifyMonitoredItemsCount: ServiceCounterDataType
    :ivar SetMonitoringModeCount:
    :vartype SetMonitoringModeCount: ServiceCounterDataType
    :ivar SetTriggeringCount:
    :vartype SetTriggeringCount: ServiceCounterDataType
    :ivar DeleteMonitoredItemsCount:
    :vartype DeleteMonitoredItemsCount: ServiceCounterDataType
    :ivar CreateSubscriptionCount:
    :vartype CreateSubscriptionCount: ServiceCounterDataType
    :ivar ModifySubscriptionCount:
    :vartype ModifySubscriptionCount: ServiceCounterDataType
    :ivar SetPublishingModeCount:
    :vartype SetPublishingModeCount: ServiceCounterDataType
    :ivar PublishCount:
    :vartype PublishCount: ServiceCounterDataType
    :ivar RepublishCount:
    :vartype RepublishCount: ServiceCounterDataType
    :ivar TransferSubscriptionsCount:
    :vartype TransferSubscriptionsCount: ServiceCounterDataType
    :ivar DeleteSubscriptionsCount:
    :vartype DeleteSubscriptionsCount: ServiceCounterDataType
    :ivar AddNodesCount:
    :vartype AddNodesCount: ServiceCounterDataType
    :ivar AddReferencesCount:
    :vartype AddReferencesCount: ServiceCounterDataType
    :ivar DeleteNodesCount:
    :vartype DeleteNodesCount: ServiceCounterDataType
    :ivar DeleteReferencesCount:
    :vartype DeleteReferencesCount: ServiceCounterDataType
    :ivar BrowseCount:
    :vartype BrowseCount: ServiceCounterDataType
    :ivar BrowseNextCount:
    :vartype BrowseNextCount: ServiceCounterDataType
    :ivar TranslateBrowsePathsToNodeIdsCount:
    :vartype TranslateBrowsePathsToNodeIdsCount: ServiceCounterDataType
    :ivar QueryFirstCount:
    :vartype QueryFirstCount: ServiceCounterDataType
    :ivar QueryNextCount:
    :vartype QueryNextCount: ServiceCounterDataType
    :ivar RegisterNodesCount:
    :vartype RegisterNodesCount: ServiceCounterDataType
    :ivar UnregisterNodesCount:
    :vartype UnregisterNodesCount: ServiceCounterDataType
    '''

    ua_types = [
        ('SessionId', 'NodeId'),
        ('SessionName', 'String'),
        ('ClientDescription', 'ApplicationDescription'),
        ('ServerUri', 'String'),
        ('EndpointUrl', 'String'),
        ('LocaleIds', 'ListOfString'),
        ('ActualSessionTimeout', 'Double'),
        ('MaxResponseMessageSize', 'UInt32'),
        ('ClientConnectionTime', 'DateTime'),
        ('ClientLastContactTime', 'DateTime'),
        ('CurrentSubscriptionsCount', 'UInt32'),
        ('CurrentMonitoredItemsCount', 'UInt32'),
        ('CurrentPublishRequestsInQueue', 'UInt32'),
        ('TotalRequestCount', 'ServiceCounterDataType'),
        ('UnauthorizedRequestCount', 'UInt32'),
        ('ReadCount', 'ServiceCounterDataType'),
        ('HistoryReadCount', 'ServiceCounterDataType'),
        ('WriteCount', 'ServiceCounterDataType'),
        ('HistoryUpdateCount', 'ServiceCounterDataType'),
        ('CallCount', 'ServiceCounterDataType'),
        ('CreateMonitoredItemsCount', 'ServiceCounterDataType'),
        ('ModifyMonitoredItemsCount', 'ServiceCounterDataType'),
        ('SetMonitoringModeCount', 'ServiceCounterDataType'),
        ('SetTriggeringCount', 'ServiceCounterDataType'),
        ('DeleteMonitoredItemsCount', 'ServiceCounterDataType'),
        ('CreateSubscriptionCount', 'ServiceCounterDataType'),
        ('ModifySubscriptionCount', 'ServiceCounterDataType'),
        ('SetPublishingModeCount', 'ServiceCounterDataType'),
        ('PublishCount', 'ServiceCounterDataType'),
        ('RepublishCount', 'ServiceCounterDataType'),
        ('TransferSubscriptionsCount', 'ServiceCounterDataType'),
        ('DeleteSubscriptionsCount', 'ServiceCounterDataType'),
        ('AddNodesCount', 'ServiceCounterDataType'),
        ('AddReferencesCount', 'ServiceCounterDataType'),
        ('DeleteNodesCount', 'ServiceCounterDataType'),
        ('DeleteReferencesCount', 'ServiceCounterDataType'),
        ('BrowseCount', 'ServiceCounterDataType'),
        ('BrowseNextCount', 'ServiceCounterDataType'),
        ('TranslateBrowsePathsToNodeIdsCount', 'ServiceCounterDataType'),
        ('QueryFirstCount', 'ServiceCounterDataType'),
        ('QueryNextCount', 'ServiceCounterDataType'),
        ('RegisterNodesCount', 'ServiceCounterDataType'),
        ('UnregisterNodesCount', 'ServiceCounterDataType'),
               ]

    def __init__(self):
        self.SessionId = NodeId()
        self.SessionName = None
        self.ClientDescription = ApplicationDescription()
        self.ServerUri = None
        self.EndpointUrl = None
        self.LocaleIds = []
        self.ActualSessionTimeout = 0
        self.MaxResponseMessageSize = 0
        self.ClientConnectionTime = datetime.utcnow()
        self.ClientLastContactTime = datetime.utcnow()
        self.CurrentSubscriptionsCount = 0
        self.CurrentMonitoredItemsCount = 0
        self.CurrentPublishRequestsInQueue = 0
        self.TotalRequestCount = ServiceCounterDataType()
        self.UnauthorizedRequestCount = 0
        self.ReadCount = ServiceCounterDataType()
        self.HistoryReadCount = ServiceCounterDataType()
        self.WriteCount = ServiceCounterDataType()
        self.HistoryUpdateCount = ServiceCounterDataType()
        self.CallCount = ServiceCounterDataType()
        self.CreateMonitoredItemsCount = ServiceCounterDataType()
        self.ModifyMonitoredItemsCount = ServiceCounterDataType()
        self.SetMonitoringModeCount = ServiceCounterDataType()
        self.SetTriggeringCount = ServiceCounterDataType()
        self.DeleteMonitoredItemsCount = ServiceCounterDataType()
        self.CreateSubscriptionCount = ServiceCounterDataType()
        self.ModifySubscriptionCount = ServiceCounterDataType()
        self.SetPublishingModeCount = ServiceCounterDataType()
        self.PublishCount = ServiceCounterDataType()
        self.RepublishCount = ServiceCounterDataType()
        self.TransferSubscriptionsCount = ServiceCounterDataType()
        self.DeleteSubscriptionsCount = ServiceCounterDataType()
        self.AddNodesCount = ServiceCounterDataType()
        self.AddReferencesCount = ServiceCounterDataType()
        self.DeleteNodesCount = ServiceCounterDataType()
        self.DeleteReferencesCount = ServiceCounterDataType()
        self.BrowseCount = ServiceCounterDataType()
        self.BrowseNextCount = ServiceCounterDataType()
        self.TranslateBrowsePathsToNodeIdsCount = ServiceCounterDataType()
        self.QueryFirstCount = ServiceCounterDataType()
        self.QueryNextCount = ServiceCounterDataType()
        self.RegisterNodesCount = ServiceCounterDataType()
        self.UnregisterNodesCount = ServiceCounterDataType()
        self._freeze = True

    def __str__(self):
        return 'SessionDiagnosticsDataType(' + 'SessionId:' + str(self.SessionId) + ', ' + \
               'SessionName:' + str(self.SessionName) + ', ' + \
               'ClientDescription:' + str(self.ClientDescription) + ', ' + \
               'ServerUri:' + str(self.ServerUri) + ', ' + \
               'EndpointUrl:' + str(self.EndpointUrl) + ', ' + \
               'LocaleIds:' + str(self.LocaleIds) + ', ' + \
               'ActualSessionTimeout:' + str(self.ActualSessionTimeout) + ', ' + \
               'MaxResponseMessageSize:' + str(self.MaxResponseMessageSize) + ', ' + \
               'ClientConnectionTime:' + str(self.ClientConnectionTime) + ', ' + \
               'ClientLastContactTime:' + str(self.ClientLastContactTime) + ', ' + \
               'CurrentSubscriptionsCount:' + str(self.CurrentSubscriptionsCount) + ', ' + \
               'CurrentMonitoredItemsCount:' + str(self.CurrentMonitoredItemsCount) + ', ' + \
               'CurrentPublishRequestsInQueue:' + str(self.CurrentPublishRequestsInQueue) + ', ' + \
               'TotalRequestCount:' + str(self.TotalRequestCount) + ', ' + \
               'UnauthorizedRequestCount:' + str(self.UnauthorizedRequestCount) + ', ' + \
               'ReadCount:' + str(self.ReadCount) + ', ' + \
               'HistoryReadCount:' + str(self.HistoryReadCount) + ', ' + \
               'WriteCount:' + str(self.WriteCount) + ', ' + \
               'HistoryUpdateCount:' + str(self.HistoryUpdateCount) + ', ' + \
               'CallCount:' + str(self.CallCount) + ', ' + \
               'CreateMonitoredItemsCount:' + str(self.CreateMonitoredItemsCount) + ', ' + \
               'ModifyMonitoredItemsCount:' + str(self.ModifyMonitoredItemsCount) + ', ' + \
               'SetMonitoringModeCount:' + str(self.SetMonitoringModeCount) + ', ' + \
               'SetTriggeringCount:' + str(self.SetTriggeringCount) + ', ' + \
               'DeleteMonitoredItemsCount:' + str(self.DeleteMonitoredItemsCount) + ', ' + \
               'CreateSubscriptionCount:' + str(self.CreateSubscriptionCount) + ', ' + \
               'ModifySubscriptionCount:' + str(self.ModifySubscriptionCount) + ', ' + \
               'SetPublishingModeCount:' + str(self.SetPublishingModeCount) + ', ' + \
               'PublishCount:' + str(self.PublishCount) + ', ' + \
               'RepublishCount:' + str(self.RepublishCount) + ', ' + \
               'TransferSubscriptionsCount:' + str(self.TransferSubscriptionsCount) + ', ' + \
               'DeleteSubscriptionsCount:' + str(self.DeleteSubscriptionsCount) + ', ' + \
               'AddNodesCount:' + str(self.AddNodesCount) + ', ' + \
               'AddReferencesCount:' + str(self.AddReferencesCount) + ', ' + \
               'DeleteNodesCount:' + str(self.DeleteNodesCount) + ', ' + \
               'DeleteReferencesCount:' + str(self.DeleteReferencesCount) + ', ' + \
               'BrowseCount:' + str(self.BrowseCount) + ', ' + \
               'BrowseNextCount:' + str(self.BrowseNextCount) + ', ' + \
               'TranslateBrowsePathsToNodeIdsCount:' + str(self.TranslateBrowsePathsToNodeIdsCount) + ', ' + \
               'QueryFirstCount:' + str(self.QueryFirstCount) + ', ' + \
               'QueryNextCount:' + str(self.QueryNextCount) + ', ' + \
               'RegisterNodesCount:' + str(self.RegisterNodesCount) + ', ' + \
               'UnregisterNodesCount:' + str(self.UnregisterNodesCount) + ')'

    __repr__ = __str__


class SessionSecurityDiagnosticsDataType(FrozenClass):
    '''
    :ivar SessionId:
    :vartype SessionId: NodeId
    :ivar ClientUserIdOfSession:
    :vartype ClientUserIdOfSession: String
    :ivar ClientUserIdHistory:
    :vartype ClientUserIdHistory: String
    :ivar AuthenticationMechanism:
    :vartype AuthenticationMechanism: String
    :ivar Encoding:
    :vartype Encoding: String
    :ivar TransportProtocol:
    :vartype TransportProtocol: String
    :ivar SecurityMode:
    :vartype SecurityMode: MessageSecurityMode
    :ivar SecurityPolicyUri:
    :vartype SecurityPolicyUri: String
    :ivar ClientCertificate:
    :vartype ClientCertificate: ByteString
    '''

    ua_types = [
        ('SessionId', 'NodeId'),
        ('ClientUserIdOfSession', 'String'),
        ('ClientUserIdHistory', 'ListOfString'),
        ('AuthenticationMechanism', 'String'),
        ('Encoding', 'String'),
        ('TransportProtocol', 'String'),
        ('SecurityMode', 'MessageSecurityMode'),
        ('SecurityPolicyUri', 'String'),
        ('ClientCertificate', 'ByteString'),
               ]

    def __init__(self):
        self.SessionId = NodeId()
        self.ClientUserIdOfSession = None
        self.ClientUserIdHistory = []
        self.AuthenticationMechanism = None
        self.Encoding = None
        self.TransportProtocol = None
        self.SecurityMode = MessageSecurityMode(0)
        self.SecurityPolicyUri = None
        self.ClientCertificate = None
        self._freeze = True

    def __str__(self):
        return 'SessionSecurityDiagnosticsDataType(' + 'SessionId:' + str(self.SessionId) + ', ' + \
               'ClientUserIdOfSession:' + str(self.ClientUserIdOfSession) + ', ' + \
               'ClientUserIdHistory:' + str(self.ClientUserIdHistory) + ', ' + \
               'AuthenticationMechanism:' + str(self.AuthenticationMechanism) + ', ' + \
               'Encoding:' + str(self.Encoding) + ', ' + \
               'TransportProtocol:' + str(self.TransportProtocol) + ', ' + \
               'SecurityMode:' + str(self.SecurityMode) + ', ' + \
               'SecurityPolicyUri:' + str(self.SecurityPolicyUri) + ', ' + \
               'ClientCertificate:' + str(self.ClientCertificate) + ')'

    __repr__ = __str__


class ServiceCounterDataType(FrozenClass):
    '''
    :ivar TotalCount:
    :vartype TotalCount: UInt32
    :ivar ErrorCount:
    :vartype ErrorCount: UInt32
    '''

    ua_types = [
        ('TotalCount', 'UInt32'),
        ('ErrorCount', 'UInt32'),
               ]

    def __init__(self):
        self.TotalCount = 0
        self.ErrorCount = 0
        self._freeze = True

    def __str__(self):
        return 'ServiceCounterDataType(' + 'TotalCount:' + str(self.TotalCount) + ', ' + \
               'ErrorCount:' + str(self.ErrorCount) + ')'

    __repr__ = __str__


class StatusResult(FrozenClass):
    '''
    :ivar StatusCode:
    :vartype StatusCode: StatusCode
    :ivar DiagnosticInfo:
    :vartype DiagnosticInfo: DiagnosticInfo
    '''

    ua_types = [
        ('StatusCode', 'StatusCode'),
        ('DiagnosticInfo', 'DiagnosticInfo'),
               ]

    def __init__(self):
        self.StatusCode = StatusCode()
        self.DiagnosticInfo = DiagnosticInfo()
        self._freeze = True

    def __str__(self):
        return 'StatusResult(' + 'StatusCode:' + str(self.StatusCode) + ', ' + \
               'DiagnosticInfo:' + str(self.DiagnosticInfo) + ')'

    __repr__ = __str__


class SubscriptionDiagnosticsDataType(FrozenClass):
    '''
    :ivar SessionId:
    :vartype SessionId: NodeId
    :ivar SubscriptionId:
    :vartype SubscriptionId: UInt32
    :ivar Priority:
    :vartype Priority: Byte
    :ivar PublishingInterval:
    :vartype PublishingInterval: Double
    :ivar MaxKeepAliveCount:
    :vartype MaxKeepAliveCount: UInt32
    :ivar MaxLifetimeCount:
    :vartype MaxLifetimeCount: UInt32
    :ivar MaxNotificationsPerPublish:
    :vartype MaxNotificationsPerPublish: UInt32
    :ivar PublishingEnabled:
    :vartype PublishingEnabled: Boolean
    :ivar ModifyCount:
    :vartype ModifyCount: UInt32
    :ivar EnableCount:
    :vartype EnableCount: UInt32
    :ivar DisableCount:
    :vartype DisableCount: UInt32
    :ivar RepublishRequestCount:
    :vartype RepublishRequestCount: UInt32
    :ivar RepublishMessageRequestCount:
    :vartype RepublishMessageRequestCount: UInt32
    :ivar RepublishMessageCount:
    :vartype RepublishMessageCount: UInt32
    :ivar TransferRequestCount:
    :vartype TransferRequestCount: UInt32
    :ivar TransferredToAltClientCount:
    :vartype TransferredToAltClientCount: UInt32
    :ivar TransferredToSameClientCount:
    :vartype TransferredToSameClientCount: UInt32
    :ivar PublishRequestCount:
    :vartype PublishRequestCount: UInt32
    :ivar DataChangeNotificationsCount:
    :vartype DataChangeNotificationsCount: UInt32
    :ivar EventNotificationsCount:
    :vartype EventNotificationsCount: UInt32
    :ivar NotificationsCount:
    :vartype NotificationsCount: UInt32
    :ivar LatePublishRequestCount:
    :vartype LatePublishRequestCount: UInt32
    :ivar CurrentKeepAliveCount:
    :vartype CurrentKeepAliveCount: UInt32
    :ivar CurrentLifetimeCount:
    :vartype CurrentLifetimeCount: UInt32
    :ivar UnacknowledgedMessageCount:
    :vartype UnacknowledgedMessageCount: UInt32
    :ivar DiscardedMessageCount:
    :vartype DiscardedMessageCount: UInt32
    :ivar MonitoredItemCount:
    :vartype MonitoredItemCount: UInt32
    :ivar DisabledMonitoredItemCount:
    :vartype DisabledMonitoredItemCount: UInt32
    :ivar MonitoringQueueOverflowCount:
    :vartype MonitoringQueueOverflowCount: UInt32
    :ivar NextSequenceNumber:
    :vartype NextSequenceNumber: UInt32
    :ivar EventQueueOverFlowCount:
    :vartype EventQueueOverFlowCount: UInt32
    '''

    ua_types = [
        ('SessionId', 'NodeId'),
        ('SubscriptionId', 'UInt32'),
        ('Priority', 'Byte'),
        ('PublishingInterval', 'Double'),
        ('MaxKeepAliveCount', 'UInt32'),
        ('MaxLifetimeCount', 'UInt32'),
        ('MaxNotificationsPerPublish', 'UInt32'),
        ('PublishingEnabled', 'Boolean'),
        ('ModifyCount', 'UInt32'),
        ('EnableCount', 'UInt32'),
        ('DisableCount', 'UInt32'),
        ('RepublishRequestCount', 'UInt32'),
        ('RepublishMessageRequestCount', 'UInt32'),
        ('RepublishMessageCount', 'UInt32'),
        ('TransferRequestCount', 'UInt32'),
        ('TransferredToAltClientCount', 'UInt32'),
        ('TransferredToSameClientCount', 'UInt32'),
        ('PublishRequestCount', 'UInt32'),
        ('DataChangeNotificationsCount', 'UInt32'),
        ('EventNotificationsCount', 'UInt32'),
        ('NotificationsCount', 'UInt32'),
        ('LatePublishRequestCount', 'UInt32'),
        ('CurrentKeepAliveCount', 'UInt32'),
        ('CurrentLifetimeCount', 'UInt32'),
        ('UnacknowledgedMessageCount', 'UInt32'),
        ('DiscardedMessageCount', 'UInt32'),
        ('MonitoredItemCount', 'UInt32'),
        ('DisabledMonitoredItemCount', 'UInt32'),
        ('MonitoringQueueOverflowCount', 'UInt32'),
        ('NextSequenceNumber', 'UInt32'),
        ('EventQueueOverFlowCount', 'UInt32'),
               ]

    def __init__(self):
        self.SessionId = NodeId()
        self.SubscriptionId = 0
        self.Priority = 0
        self.PublishingInterval = 0
        self.MaxKeepAliveCount = 0
        self.MaxLifetimeCount = 0
        self.MaxNotificationsPerPublish = 0
        self.PublishingEnabled = True
        self.ModifyCount = 0
        self.EnableCount = 0
        self.DisableCount = 0
        self.RepublishRequestCount = 0
        self.RepublishMessageRequestCount = 0
        self.RepublishMessageCount = 0
        self.TransferRequestCount = 0
        self.TransferredToAltClientCount = 0
        self.TransferredToSameClientCount = 0
        self.PublishRequestCount = 0
        self.DataChangeNotificationsCount = 0
        self.EventNotificationsCount = 0
        self.NotificationsCount = 0
        self.LatePublishRequestCount = 0
        self.CurrentKeepAliveCount = 0
        self.CurrentLifetimeCount = 0
        self.UnacknowledgedMessageCount = 0
        self.DiscardedMessageCount = 0
        self.MonitoredItemCount = 0
        self.DisabledMonitoredItemCount = 0
        self.MonitoringQueueOverflowCount = 0
        self.NextSequenceNumber = 0
        self.EventQueueOverFlowCount = 0
        self._freeze = True

    def __str__(self):
        return 'SubscriptionDiagnosticsDataType(' + 'SessionId:' + str(self.SessionId) + ', ' + \
               'SubscriptionId:' + str(self.SubscriptionId) + ', ' + \
               'Priority:' + str(self.Priority) + ', ' + \
               'PublishingInterval:' + str(self.PublishingInterval) + ', ' + \
               'MaxKeepAliveCount:' + str(self.MaxKeepAliveCount) + ', ' + \
               'MaxLifetimeCount:' + str(self.MaxLifetimeCount) + ', ' + \
               'MaxNotificationsPerPublish:' + str(self.MaxNotificationsPerPublish) + ', ' + \
               'PublishingEnabled:' + str(self.PublishingEnabled) + ', ' + \
               'ModifyCount:' + str(self.ModifyCount) + ', ' + \
               'EnableCount:' + str(self.EnableCount) + ', ' + \
               'DisableCount:' + str(self.DisableCount) + ', ' + \
               'RepublishRequestCount:' + str(self.RepublishRequestCount) + ', ' + \
               'RepublishMessageRequestCount:' + str(self.RepublishMessageRequestCount) + ', ' + \
               'RepublishMessageCount:' + str(self.RepublishMessageCount) + ', ' + \
               'TransferRequestCount:' + str(self.TransferRequestCount) + ', ' + \
               'TransferredToAltClientCount:' + str(self.TransferredToAltClientCount) + ', ' + \
               'TransferredToSameClientCount:' + str(self.TransferredToSameClientCount) + ', ' + \
               'PublishRequestCount:' + str(self.PublishRequestCount) + ', ' + \
               'DataChangeNotificationsCount:' + str(self.DataChangeNotificationsCount) + ', ' + \
               'EventNotificationsCount:' + str(self.EventNotificationsCount) + ', ' + \
               'NotificationsCount:' + str(self.NotificationsCount) + ', ' + \
               'LatePublishRequestCount:' + str(self.LatePublishRequestCount) + ', ' + \
               'CurrentKeepAliveCount:' + str(self.CurrentKeepAliveCount) + ', ' + \
               'CurrentLifetimeCount:' + str(self.CurrentLifetimeCount) + ', ' + \
               'UnacknowledgedMessageCount:' + str(self.UnacknowledgedMessageCount) + ', ' + \
               'DiscardedMessageCount:' + str(self.DiscardedMessageCount) + ', ' + \
               'MonitoredItemCount:' + str(self.MonitoredItemCount) + ', ' + \
               'DisabledMonitoredItemCount:' + str(self.DisabledMonitoredItemCount) + ', ' + \
               'MonitoringQueueOverflowCount:' + str(self.MonitoringQueueOverflowCount) + ', ' + \
               'NextSequenceNumber:' + str(self.NextSequenceNumber) + ', ' + \
               'EventQueueOverFlowCount:' + str(self.EventQueueOverFlowCount) + ')'

    __repr__ = __str__


class ModelChangeStructureDataType(FrozenClass):
    '''
    :ivar Affected:
    :vartype Affected: NodeId
    :ivar AffectedType:
    :vartype AffectedType: NodeId
    :ivar Verb:
    :vartype Verb: Byte
    '''

    ua_types = [
        ('Affected', 'NodeId'),
        ('AffectedType', 'NodeId'),
        ('Verb', 'Byte'),
               ]

    def __init__(self):
        self.Affected = NodeId()
        self.AffectedType = NodeId()
        self.Verb = 0
        self._freeze = True

    def __str__(self):
        return 'ModelChangeStructureDataType(' + 'Affected:' + str(self.Affected) + ', ' + \
               'AffectedType:' + str(self.AffectedType) + ', ' + \
               'Verb:' + str(self.Verb) + ')'

    __repr__ = __str__


class SemanticChangeStructureDataType(FrozenClass):
    '''
    :ivar Affected:
    :vartype Affected: NodeId
    :ivar AffectedType:
    :vartype AffectedType: NodeId
    '''

    ua_types = [
        ('Affected', 'NodeId'),
        ('AffectedType', 'NodeId'),
               ]

    def __init__(self):
        self.Affected = NodeId()
        self.AffectedType = NodeId()
        self._freeze = True

    def __str__(self):
        return 'SemanticChangeStructureDataType(' + 'Affected:' + str(self.Affected) + ', ' + \
               'AffectedType:' + str(self.AffectedType) + ')'

    __repr__ = __str__


class Range(FrozenClass):
    '''
    :ivar Low:
    :vartype Low: Double
    :ivar High:
    :vartype High: Double
    '''

    ua_types = [
        ('Low', 'Double'),
        ('High', 'Double'),
               ]

    def __init__(self):
        self.Low = 0
        self.High = 0
        self._freeze = True

    def __str__(self):
        return 'Range(' + 'Low:' + str(self.Low) + ', ' + \
               'High:' + str(self.High) + ')'

    __repr__ = __str__


class EUInformation(FrozenClass):
    '''
    :ivar NamespaceUri:
    :vartype NamespaceUri: String
    :ivar UnitId:
    :vartype UnitId: Int32
    :ivar DisplayName:
    :vartype DisplayName: LocalizedText
    :ivar Description:
    :vartype Description: LocalizedText
    '''

    ua_types = [
        ('NamespaceUri', 'String'),
        ('UnitId', 'Int32'),
        ('DisplayName', 'LocalizedText'),
        ('Description', 'LocalizedText'),
               ]

    def __init__(self):
        self.NamespaceUri = None
        self.UnitId = 0
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self._freeze = True

    def __str__(self):
        return 'EUInformation(' + 'NamespaceUri:' + str(self.NamespaceUri) + ', ' + \
               'UnitId:' + str(self.UnitId) + ', ' + \
               'DisplayName:' + str(self.DisplayName) + ', ' + \
               'Description:' + str(self.Description) + ')'

    __repr__ = __str__


class ComplexNumberType(FrozenClass):
    '''
    :ivar Real:
    :vartype Real: Float
    :ivar Imaginary:
    :vartype Imaginary: Float
    '''

    ua_types = [
        ('Real', 'Float'),
        ('Imaginary', 'Float'),
               ]

    def __init__(self):
        self.Real = 0
        self.Imaginary = 0
        self._freeze = True

    def __str__(self):
        return 'ComplexNumberType(' + 'Real:' + str(self.Real) + ', ' + \
               'Imaginary:' + str(self.Imaginary) + ')'

    __repr__ = __str__


class DoubleComplexNumberType(FrozenClass):
    '''
    :ivar Real:
    :vartype Real: Double
    :ivar Imaginary:
    :vartype Imaginary: Double
    '''

    ua_types = [
        ('Real', 'Double'),
        ('Imaginary', 'Double'),
               ]

    def __init__(self):
        self.Real = 0
        self.Imaginary = 0
        self._freeze = True

    def __str__(self):
        return 'DoubleComplexNumberType(' + 'Real:' + str(self.Real) + ', ' + \
               'Imaginary:' + str(self.Imaginary) + ')'

    __repr__ = __str__


class AxisInformation(FrozenClass):
    '''
    :ivar EngineeringUnits:
    :vartype EngineeringUnits: EUInformation
    :ivar EURange:
    :vartype EURange: Range
    :ivar Title:
    :vartype Title: LocalizedText
    :ivar AxisScaleType:
    :vartype AxisScaleType: AxisScaleEnumeration
    :ivar AxisSteps:
    :vartype AxisSteps: Double
    '''

    ua_types = [
        ('EngineeringUnits', 'EUInformation'),
        ('EURange', 'Range'),
        ('Title', 'LocalizedText'),
        ('AxisScaleType', 'AxisScaleEnumeration'),
        ('AxisSteps', 'ListOfDouble'),
               ]

    def __init__(self):
        self.EngineeringUnits = EUInformation()
        self.EURange = Range()
        self.Title = LocalizedText()
        self.AxisScaleType = AxisScaleEnumeration(0)
        self.AxisSteps = []
        self._freeze = True

    def __str__(self):
        return 'AxisInformation(' + 'EngineeringUnits:' + str(self.EngineeringUnits) + ', ' + \
               'EURange:' + str(self.EURange) + ', ' + \
               'Title:' + str(self.Title) + ', ' + \
               'AxisScaleType:' + str(self.AxisScaleType) + ', ' + \
               'AxisSteps:' + str(self.AxisSteps) + ')'

    __repr__ = __str__


class XVType(FrozenClass):
    '''
    :ivar X:
    :vartype X: Double
    :ivar Value:
    :vartype Value: Float
    '''

    ua_types = [
        ('X', 'Double'),
        ('Value', 'Float'),
               ]

    def __init__(self):
        self.X = 0
        self.Value = 0
        self._freeze = True

    def __str__(self):
        return 'XVType(' + 'X:' + str(self.X) + ', ' + \
               'Value:' + str(self.Value) + ')'

    __repr__ = __str__


class ProgramDiagnosticDataType(FrozenClass):
    '''
    :ivar CreateSessionId:
    :vartype CreateSessionId: NodeId
    :ivar CreateClientName:
    :vartype CreateClientName: String
    :ivar InvocationCreationTime:
    :vartype InvocationCreationTime: DateTime
    :ivar LastTransitionTime:
    :vartype LastTransitionTime: DateTime
    :ivar LastMethodCall:
    :vartype LastMethodCall: String
    :ivar LastMethodSessionId:
    :vartype LastMethodSessionId: NodeId
    :ivar LastMethodInputArguments:
    :vartype LastMethodInputArguments: Argument
    :ivar LastMethodOutputArguments:
    :vartype LastMethodOutputArguments: Argument
    :ivar LastMethodCallTime:
    :vartype LastMethodCallTime: DateTime
    :ivar LastMethodReturnStatus:
    :vartype LastMethodReturnStatus: StatusResult
    '''

    ua_types = [
        ('CreateSessionId', 'NodeId'),
        ('CreateClientName', 'String'),
        ('InvocationCreationTime', 'DateTime'),
        ('LastTransitionTime', 'DateTime'),
        ('LastMethodCall', 'String'),
        ('LastMethodSessionId', 'NodeId'),
        ('LastMethodInputArguments', 'ListOfArgument'),
        ('LastMethodOutputArguments', 'ListOfArgument'),
        ('LastMethodCallTime', 'DateTime'),
        ('LastMethodReturnStatus', 'StatusResult'),
               ]

    def __init__(self):
        self.CreateSessionId = NodeId()
        self.CreateClientName = None
        self.InvocationCreationTime = datetime.utcnow()
        self.LastTransitionTime = datetime.utcnow()
        self.LastMethodCall = None
        self.LastMethodSessionId = NodeId()
        self.LastMethodInputArguments = []
        self.LastMethodOutputArguments = []
        self.LastMethodCallTime = datetime.utcnow()
        self.LastMethodReturnStatus = StatusResult()
        self._freeze = True

    def __str__(self):
        return 'ProgramDiagnosticDataType(' + 'CreateSessionId:' + str(self.CreateSessionId) + ', ' + \
               'CreateClientName:' + str(self.CreateClientName) + ', ' + \
               'InvocationCreationTime:' + str(self.InvocationCreationTime) + ', ' + \
               'LastTransitionTime:' + str(self.LastTransitionTime) + ', ' + \
               'LastMethodCall:' + str(self.LastMethodCall) + ', ' + \
               'LastMethodSessionId:' + str(self.LastMethodSessionId) + ', ' + \
               'LastMethodInputArguments:' + str(self.LastMethodInputArguments) + ', ' + \
               'LastMethodOutputArguments:' + str(self.LastMethodOutputArguments) + ', ' + \
               'LastMethodCallTime:' + str(self.LastMethodCallTime) + ', ' + \
               'LastMethodReturnStatus:' + str(self.LastMethodReturnStatus) + ')'

    __repr__ = __str__


class ProgramDiagnostic2DataType(FrozenClass):
    '''
    :ivar CreateSessionId:
    :vartype CreateSessionId: NodeId
    :ivar CreateClientName:
    :vartype CreateClientName: String
    :ivar InvocationCreationTime:
    :vartype InvocationCreationTime: DateTime
    :ivar LastTransitionTime:
    :vartype LastTransitionTime: DateTime
    :ivar LastMethodCall:
    :vartype LastMethodCall: String
    :ivar LastMethodSessionId:
    :vartype LastMethodSessionId: NodeId
    :ivar LastMethodInputArguments:
    :vartype LastMethodInputArguments: Argument
    :ivar LastMethodOutputArguments:
    :vartype LastMethodOutputArguments: Argument
    :ivar LastMethodInputValues:
    :vartype LastMethodInputValues: Variant
    :ivar LastMethodOutputValues:
    :vartype LastMethodOutputValues: Variant
    :ivar LastMethodCallTime:
    :vartype LastMethodCallTime: DateTime
    :ivar LastMethodReturnStatus:
    :vartype LastMethodReturnStatus: StatusResult
    '''

    ua_types = [
        ('CreateSessionId', 'NodeId'),
        ('CreateClientName', 'String'),
        ('InvocationCreationTime', 'DateTime'),
        ('LastTransitionTime', 'DateTime'),
        ('LastMethodCall', 'String'),
        ('LastMethodSessionId', 'NodeId'),
        ('LastMethodInputArguments', 'ListOfArgument'),
        ('LastMethodOutputArguments', 'ListOfArgument'),
        ('LastMethodInputValues', 'ListOfVariant'),
        ('LastMethodOutputValues', 'ListOfVariant'),
        ('LastMethodCallTime', 'DateTime'),
        ('LastMethodReturnStatus', 'StatusResult'),
               ]

    def __init__(self):
        self.CreateSessionId = NodeId()
        self.CreateClientName = None
        self.InvocationCreationTime = datetime.utcnow()
        self.LastTransitionTime = datetime.utcnow()
        self.LastMethodCall = None
        self.LastMethodSessionId = NodeId()
        self.LastMethodInputArguments = []
        self.LastMethodOutputArguments = []
        self.LastMethodInputValues = []
        self.LastMethodOutputValues = []
        self.LastMethodCallTime = datetime.utcnow()
        self.LastMethodReturnStatus = StatusResult()
        self._freeze = True

    def __str__(self):
        return 'ProgramDiagnostic2DataType(' + 'CreateSessionId:' + str(self.CreateSessionId) + ', ' + \
               'CreateClientName:' + str(self.CreateClientName) + ', ' + \
               'InvocationCreationTime:' + str(self.InvocationCreationTime) + ', ' + \
               'LastTransitionTime:' + str(self.LastTransitionTime) + ', ' + \
               'LastMethodCall:' + str(self.LastMethodCall) + ', ' + \
               'LastMethodSessionId:' + str(self.LastMethodSessionId) + ', ' + \
               'LastMethodInputArguments:' + str(self.LastMethodInputArguments) + ', ' + \
               'LastMethodOutputArguments:' + str(self.LastMethodOutputArguments) + ', ' + \
               'LastMethodInputValues:' + str(self.LastMethodInputValues) + ', ' + \
               'LastMethodOutputValues:' + str(self.LastMethodOutputValues) + ', ' + \
               'LastMethodCallTime:' + str(self.LastMethodCallTime) + ', ' + \
               'LastMethodReturnStatus:' + str(self.LastMethodReturnStatus) + ')'

    __repr__ = __str__


class Annotation(FrozenClass):
    '''
    :ivar Message:
    :vartype Message: String
    :ivar UserName:
    :vartype UserName: String
    :ivar AnnotationTime:
    :vartype AnnotationTime: DateTime
    '''

    ua_types = [
        ('Message', 'String'),
        ('UserName', 'String'),
        ('AnnotationTime', 'DateTime'),
               ]

    def __init__(self):
        self.Message = None
        self.UserName = None
        self.AnnotationTime = datetime.utcnow()
        self._freeze = True

    def __str__(self):
        return 'Annotation(' + 'Message:' + str(self.Message) + ', ' + \
               'UserName:' + str(self.UserName) + ', ' + \
               'AnnotationTime:' + str(self.AnnotationTime) + ')'

    __repr__ = __str__


nid = FourByteNodeId(ObjectIds.KeyValuePair_Encoding_DefaultBinary)
extension_object_classes[nid] = KeyValuePair
extension_object_ids['KeyValuePair'] = nid
nid = FourByteNodeId(ObjectIds.EndpointType_Encoding_DefaultBinary)
extension_object_classes[nid] = EndpointType
extension_object_ids['EndpointType'] = nid
nid = FourByteNodeId(ObjectIds.IdentityMappingRuleType_Encoding_DefaultBinary)
extension_object_classes[nid] = IdentityMappingRuleType
extension_object_ids['IdentityMappingRuleType'] = nid
nid = FourByteNodeId(ObjectIds.TrustListDataType_Encoding_DefaultBinary)
extension_object_classes[nid] = TrustListDataType
extension_object_ids['TrustListDataType'] = nid
nid = FourByteNodeId(ObjectIds.DecimalDataType_Encoding_DefaultBinary)
extension_object_classes[nid] = DecimalDataType
extension_object_ids['DecimalDataType'] = nid
nid = FourByteNodeId(ObjectIds.DataTypeSchemaHeader_Encoding_DefaultBinary)
extension_object_classes[nid] = DataTypeSchemaHeader
extension_object_ids['DataTypeSchemaHeader'] = nid
nid = FourByteNodeId(ObjectIds.DataTypeDescription_Encoding_DefaultBinary)
extension_object_classes[nid] = DataTypeDescription
extension_object_ids['DataTypeDescription'] = nid
nid = FourByteNodeId(ObjectIds.StructureDescription_Encoding_DefaultBinary)
extension_object_classes[nid] = StructureDescription
extension_object_ids['StructureDescription'] = nid
nid = FourByteNodeId(ObjectIds.EnumDescription_Encoding_DefaultBinary)
extension_object_classes[nid] = EnumDescription
extension_object_ids['EnumDescription'] = nid
nid = FourByteNodeId(ObjectIds.SimpleTypeDescription_Encoding_DefaultBinary)
extension_object_classes[nid] = SimpleTypeDescription
extension_object_ids['SimpleTypeDescription'] = nid
nid = FourByteNodeId(ObjectIds.UABinaryFileDataType_Encoding_DefaultBinary)
extension_object_classes[nid] = UABinaryFileDataType
extension_object_ids['UABinaryFileDataType'] = nid
nid = FourByteNodeId(ObjectIds.DataSetMetaDataType_Encoding_DefaultBinary)
extension_object_classes[nid] = DataSetMetaDataType
extension_object_ids['DataSetMetaDataType'] = nid
nid = FourByteNodeId(ObjectIds.FieldMetaData_Encoding_DefaultBinary)
extension_object_classes[nid] = FieldMetaData
extension_object_ids['FieldMetaData'] = nid
nid = FourByteNodeId(ObjectIds.ConfigurationVersionDataType_Encoding_DefaultBinary)
extension_object_classes[nid] = ConfigurationVersionDataType
extension_object_ids['ConfigurationVersionDataType'] = nid
nid = FourByteNodeId(ObjectIds.PublishedDataSetDataType_Encoding_DefaultBinary)
extension_object_classes[nid] = PublishedDataSetDataType
extension_object_ids['PublishedDataSetDataType'] = nid
nid = FourByteNodeId(ObjectIds.PublishedDataSetSourceDataType_Encoding_DefaultBinary)
extension_object_classes[nid] = PublishedDataSetSourceDataType
extension_object_ids['PublishedDataSetSourceDataType'] = nid
nid = FourByteNodeId(ObjectIds.PublishedVariableDataType_Encoding_DefaultBinary)
extension_object_classes[nid] = PublishedVariableDataType
extension_object_ids['PublishedVariableDataType'] = nid
nid = FourByteNodeId(ObjectIds.PublishedDataItemsDataType_Encoding_DefaultBinary)
extension_object_classes[nid] = PublishedDataItemsDataType
extension_object_ids['PublishedDataItemsDataType'] = nid
nid = FourByteNodeId(ObjectIds.PublishedEventsDataType_Encoding_DefaultBinary)
extension_object_classes[nid] = PublishedEventsDataType
extension_object_ids['PublishedEventsDataType'] = nid
nid = FourByteNodeId(ObjectIds.DataSetWriterDataType_Encoding_DefaultBinary)
extension_object_classes[nid] = DataSetWriterDataType
extension_object_ids['DataSetWriterDataType'] = nid
nid = FourByteNodeId(ObjectIds.DataSetWriterTransportDataType_Encoding_DefaultBinary)
extension_object_classes[nid] = DataSetWriterTransportDataType
extension_object_ids['DataSetWriterTransportDataType'] = nid
nid = FourByteNodeId(ObjectIds.DataSetWriterMessageDataType_Encoding_DefaultBinary)
extension_object_classes[nid] = DataSetWriterMessageDataType
extension_object_ids['DataSetWriterMessageDataType'] = nid
nid = FourByteNodeId(ObjectIds.PubSubGroupDataType_Encoding_DefaultBinary)
extension_object_classes[nid] = PubSubGroupDataType
extension_object_ids['PubSubGroupDataType'] = nid
nid = FourByteNodeId(ObjectIds.WriterGroupDataType_Encoding_DefaultBinary)
extension_object_classes[nid] = WriterGroupDataType
extension_object_ids['WriterGroupDataType'] = nid
nid = FourByteNodeId(ObjectIds.WriterGroupTransportDataType_Encoding_DefaultBinary)
extension_object_classes[nid] = WriterGroupTransportDataType
extension_object_ids['WriterGroupTransportDataType'] = nid
nid = FourByteNodeId(ObjectIds.WriterGroupMessageDataType_Encoding_DefaultBinary)
extension_object_classes[nid] = WriterGroupMessageDataType
extension_object_ids['WriterGroupMessageDataType'] = nid
nid = FourByteNodeId(ObjectIds.PubSubConnectionDataType_Encoding_DefaultBinary)
extension_object_classes[nid] = PubSubConnectionDataType
extension_object_ids['PubSubConnectionDataType'] = nid
nid = FourByteNodeId(ObjectIds.ConnectionTransportDataType_Encoding_DefaultBinary)
extension_object_classes[nid] = ConnectionTransportDataType
extension_object_ids['ConnectionTransportDataType'] = nid
nid = FourByteNodeId(ObjectIds.NetworkAddressDataType_Encoding_DefaultBinary)
extension_object_classes[nid] = NetworkAddressDataType
extension_object_ids['NetworkAddressDataType'] = nid
nid = FourByteNodeId(ObjectIds.NetworkAddressUrlDataType_Encoding_DefaultBinary)
extension_object_classes[nid] = NetworkAddressUrlDataType
extension_object_ids['NetworkAddressUrlDataType'] = nid
nid = FourByteNodeId(ObjectIds.ReaderGroupDataType_Encoding_DefaultBinary)
extension_object_classes[nid] = ReaderGroupDataType
extension_object_ids['ReaderGroupDataType'] = nid
nid = FourByteNodeId(ObjectIds.ReaderGroupTransportDataType_Encoding_DefaultBinary)
extension_object_classes[nid] = ReaderGroupTransportDataType
extension_object_ids['ReaderGroupTransportDataType'] = nid
nid = FourByteNodeId(ObjectIds.ReaderGroupMessageDataType_Encoding_DefaultBinary)
extension_object_classes[nid] = ReaderGroupMessageDataType
extension_object_ids['ReaderGroupMessageDataType'] = nid
nid = FourByteNodeId(ObjectIds.DataSetReaderDataType_Encoding_DefaultBinary)
extension_object_classes[nid] = DataSetReaderDataType
extension_object_ids['DataSetReaderDataType'] = nid
nid = FourByteNodeId(ObjectIds.DataSetReaderTransportDataType_Encoding_DefaultBinary)
extension_object_classes[nid] = DataSetReaderTransportDataType
extension_object_ids['DataSetReaderTransportDataType'] = nid
nid = FourByteNodeId(ObjectIds.DataSetReaderMessageDataType_Encoding_DefaultBinary)
extension_object_classes[nid] = DataSetReaderMessageDataType
extension_object_ids['DataSetReaderMessageDataType'] = nid
nid = FourByteNodeId(ObjectIds.SubscribedDataSetDataType_Encoding_DefaultBinary)
extension_object_classes[nid] = SubscribedDataSetDataType
extension_object_ids['SubscribedDataSetDataType'] = nid
nid = FourByteNodeId(ObjectIds.TargetVariablesDataType_Encoding_DefaultBinary)
extension_object_classes[nid] = TargetVariablesDataType
extension_object_ids['TargetVariablesDataType'] = nid
nid = FourByteNodeId(ObjectIds.FieldTargetDataType_Encoding_DefaultBinary)
extension_object_classes[nid] = FieldTargetDataType
extension_object_ids['FieldTargetDataType'] = nid
nid = FourByteNodeId(ObjectIds.SubscribedDataSetMirrorDataType_Encoding_DefaultBinary)
extension_object_classes[nid] = SubscribedDataSetMirrorDataType
extension_object_ids['SubscribedDataSetMirrorDataType'] = nid
nid = FourByteNodeId(ObjectIds.PubSubConfigurationDataType_Encoding_DefaultBinary)
extension_object_classes[nid] = PubSubConfigurationDataType
extension_object_ids['PubSubConfigurationDataType'] = nid
nid = FourByteNodeId(ObjectIds.UadpWriterGroupMessageDataType_Encoding_DefaultBinary)
extension_object_classes[nid] = UadpWriterGroupMessageDataType
extension_object_ids['UadpWriterGroupMessageDataType'] = nid
nid = FourByteNodeId(ObjectIds.UadpDataSetWriterMessageDataType_Encoding_DefaultBinary)
extension_object_classes[nid] = UadpDataSetWriterMessageDataType
extension_object_ids['UadpDataSetWriterMessageDataType'] = nid
nid = FourByteNodeId(ObjectIds.UadpDataSetReaderMessageDataType_Encoding_DefaultBinary)
extension_object_classes[nid] = UadpDataSetReaderMessageDataType
extension_object_ids['UadpDataSetReaderMessageDataType'] = nid
nid = FourByteNodeId(ObjectIds.JsonWriterGroupMessageDataType_Encoding_DefaultBinary)
extension_object_classes[nid] = JsonWriterGroupMessageDataType
extension_object_ids['JsonWriterGroupMessageDataType'] = nid
nid = FourByteNodeId(ObjectIds.JsonDataSetWriterMessageDataType_Encoding_DefaultBinary)
extension_object_classes[nid] = JsonDataSetWriterMessageDataType
extension_object_ids['JsonDataSetWriterMessageDataType'] = nid
nid = FourByteNodeId(ObjectIds.JsonDataSetReaderMessageDataType_Encoding_DefaultBinary)
extension_object_classes[nid] = JsonDataSetReaderMessageDataType
extension_object_ids['JsonDataSetReaderMessageDataType'] = nid
nid = FourByteNodeId(ObjectIds.DatagramConnectionTransportDataType_Encoding_DefaultBinary)
extension_object_classes[nid] = DatagramConnectionTransportDataType
extension_object_ids['DatagramConnectionTransportDataType'] = nid
nid = FourByteNodeId(ObjectIds.DatagramWriterGroupTransportDataType_Encoding_DefaultBinary)
extension_object_classes[nid] = DatagramWriterGroupTransportDataType
extension_object_ids['DatagramWriterGroupTransportDataType'] = nid
nid = FourByteNodeId(ObjectIds.BrokerConnectionTransportDataType_Encoding_DefaultBinary)
extension_object_classes[nid] = BrokerConnectionTransportDataType
extension_object_ids['BrokerConnectionTransportDataType'] = nid
nid = FourByteNodeId(ObjectIds.BrokerWriterGroupTransportDataType_Encoding_DefaultBinary)
extension_object_classes[nid] = BrokerWriterGroupTransportDataType
extension_object_ids['BrokerWriterGroupTransportDataType'] = nid
nid = FourByteNodeId(ObjectIds.BrokerDataSetWriterTransportDataType_Encoding_DefaultBinary)
extension_object_classes[nid] = BrokerDataSetWriterTransportDataType
extension_object_ids['BrokerDataSetWriterTransportDataType'] = nid
nid = FourByteNodeId(ObjectIds.BrokerDataSetReaderTransportDataType_Encoding_DefaultBinary)
extension_object_classes[nid] = BrokerDataSetReaderTransportDataType
extension_object_ids['BrokerDataSetReaderTransportDataType'] = nid
nid = FourByteNodeId(ObjectIds.RolePermissionType_Encoding_DefaultBinary)
extension_object_classes[nid] = RolePermissionType
extension_object_ids['RolePermissionType'] = nid
nid = FourByteNodeId(ObjectIds.StructureField_Encoding_DefaultBinary)
extension_object_classes[nid] = StructureField
extension_object_ids['StructureField'] = nid
nid = FourByteNodeId(ObjectIds.Argument_Encoding_DefaultBinary)
extension_object_classes[nid] = Argument
extension_object_ids['Argument'] = nid
nid = FourByteNodeId(ObjectIds.EnumValueType_Encoding_DefaultBinary)
extension_object_classes[nid] = EnumValueType
extension_object_ids['EnumValueType'] = nid
nid = FourByteNodeId(ObjectIds.EnumField_Encoding_DefaultBinary)
extension_object_classes[nid] = EnumField
extension_object_ids['EnumField'] = nid
nid = FourByteNodeId(ObjectIds.OptionSet_Encoding_DefaultBinary)
extension_object_classes[nid] = OptionSet
extension_object_ids['OptionSet'] = nid
nid = FourByteNodeId(ObjectIds.Union_Encoding_DefaultBinary)
extension_object_classes[nid] = Union
extension_object_ids['Union'] = nid
nid = FourByteNodeId(ObjectIds.TimeZoneDataType_Encoding_DefaultBinary)
extension_object_classes[nid] = TimeZoneDataType
extension_object_ids['TimeZoneDataType'] = nid
nid = FourByteNodeId(ObjectIds.ApplicationDescription_Encoding_DefaultBinary)
extension_object_classes[nid] = ApplicationDescription
extension_object_ids['ApplicationDescription'] = nid
nid = FourByteNodeId(ObjectIds.RequestHeader_Encoding_DefaultBinary)
extension_object_classes[nid] = RequestHeader
extension_object_ids['RequestHeader'] = nid
nid = FourByteNodeId(ObjectIds.ResponseHeader_Encoding_DefaultBinary)
extension_object_classes[nid] = ResponseHeader
extension_object_ids['ResponseHeader'] = nid
nid = FourByteNodeId(ObjectIds.ServiceFault_Encoding_DefaultBinary)
extension_object_classes[nid] = ServiceFault
extension_object_ids['ServiceFault'] = nid
nid = FourByteNodeId(ObjectIds.SessionlessInvokeRequestType_Encoding_DefaultBinary)
extension_object_classes[nid] = SessionlessInvokeRequestType
extension_object_ids['SessionlessInvokeRequestType'] = nid
nid = FourByteNodeId(ObjectIds.SessionlessInvokeResponseType_Encoding_DefaultBinary)
extension_object_classes[nid] = SessionlessInvokeResponseType
extension_object_ids['SessionlessInvokeResponseType'] = nid
nid = FourByteNodeId(ObjectIds.FindServersRequest_Encoding_DefaultBinary)
extension_object_classes[nid] = FindServersRequest
extension_object_ids['FindServersRequest'] = nid
nid = FourByteNodeId(ObjectIds.FindServersResponse_Encoding_DefaultBinary)
extension_object_classes[nid] = FindServersResponse
extension_object_ids['FindServersResponse'] = nid
nid = FourByteNodeId(ObjectIds.ServerOnNetwork_Encoding_DefaultBinary)
extension_object_classes[nid] = ServerOnNetwork
extension_object_ids['ServerOnNetwork'] = nid
nid = FourByteNodeId(ObjectIds.FindServersOnNetworkRequest_Encoding_DefaultBinary)
extension_object_classes[nid] = FindServersOnNetworkRequest
extension_object_ids['FindServersOnNetworkRequest'] = nid
nid = FourByteNodeId(ObjectIds.FindServersOnNetworkResponse_Encoding_DefaultBinary)
extension_object_classes[nid] = FindServersOnNetworkResponse
extension_object_ids['FindServersOnNetworkResponse'] = nid
nid = FourByteNodeId(ObjectIds.UserTokenPolicy_Encoding_DefaultBinary)
extension_object_classes[nid] = UserTokenPolicy
extension_object_ids['UserTokenPolicy'] = nid
nid = FourByteNodeId(ObjectIds.EndpointDescription_Encoding_DefaultBinary)
extension_object_classes[nid] = EndpointDescription
extension_object_ids['EndpointDescription'] = nid
nid = FourByteNodeId(ObjectIds.GetEndpointsRequest_Encoding_DefaultBinary)
extension_object_classes[nid] = GetEndpointsRequest
extension_object_ids['GetEndpointsRequest'] = nid
nid = FourByteNodeId(ObjectIds.GetEndpointsResponse_Encoding_DefaultBinary)
extension_object_classes[nid] = GetEndpointsResponse
extension_object_ids['GetEndpointsResponse'] = nid
nid = FourByteNodeId(ObjectIds.RegisteredServer_Encoding_DefaultBinary)
extension_object_classes[nid] = RegisteredServer
extension_object_ids['RegisteredServer'] = nid
nid = FourByteNodeId(ObjectIds.RegisterServerRequest_Encoding_DefaultBinary)
extension_object_classes[nid] = RegisterServerRequest
extension_object_ids['RegisterServerRequest'] = nid
nid = FourByteNodeId(ObjectIds.RegisterServerResponse_Encoding_DefaultBinary)
extension_object_classes[nid] = RegisterServerResponse
extension_object_ids['RegisterServerResponse'] = nid
nid = FourByteNodeId(ObjectIds.DiscoveryConfiguration_Encoding_DefaultBinary)
extension_object_classes[nid] = DiscoveryConfiguration
extension_object_ids['DiscoveryConfiguration'] = nid
nid = FourByteNodeId(ObjectIds.MdnsDiscoveryConfiguration_Encoding_DefaultBinary)
extension_object_classes[nid] = MdnsDiscoveryConfiguration
extension_object_ids['MdnsDiscoveryConfiguration'] = nid
nid = FourByteNodeId(ObjectIds.RegisterServer2Request_Encoding_DefaultBinary)
extension_object_classes[nid] = RegisterServer2Request
extension_object_ids['RegisterServer2Request'] = nid
nid = FourByteNodeId(ObjectIds.RegisterServer2Response_Encoding_DefaultBinary)
extension_object_classes[nid] = RegisterServer2Response
extension_object_ids['RegisterServer2Response'] = nid
nid = FourByteNodeId(ObjectIds.ChannelSecurityToken_Encoding_DefaultBinary)
extension_object_classes[nid] = ChannelSecurityToken
extension_object_ids['ChannelSecurityToken'] = nid
nid = FourByteNodeId(ObjectIds.OpenSecureChannelRequest_Encoding_DefaultBinary)
extension_object_classes[nid] = OpenSecureChannelRequest
extension_object_ids['OpenSecureChannelRequest'] = nid
nid = FourByteNodeId(ObjectIds.OpenSecureChannelResponse_Encoding_DefaultBinary)
extension_object_classes[nid] = OpenSecureChannelResponse
extension_object_ids['OpenSecureChannelResponse'] = nid
nid = FourByteNodeId(ObjectIds.CloseSecureChannelRequest_Encoding_DefaultBinary)
extension_object_classes[nid] = CloseSecureChannelRequest
extension_object_ids['CloseSecureChannelRequest'] = nid
nid = FourByteNodeId(ObjectIds.CloseSecureChannelResponse_Encoding_DefaultBinary)
extension_object_classes[nid] = CloseSecureChannelResponse
extension_object_ids['CloseSecureChannelResponse'] = nid
nid = FourByteNodeId(ObjectIds.SignedSoftwareCertificate_Encoding_DefaultBinary)
extension_object_classes[nid] = SignedSoftwareCertificate
extension_object_ids['SignedSoftwareCertificate'] = nid
nid = FourByteNodeId(ObjectIds.SignatureData_Encoding_DefaultBinary)
extension_object_classes[nid] = SignatureData
extension_object_ids['SignatureData'] = nid
nid = FourByteNodeId(ObjectIds.CreateSessionRequest_Encoding_DefaultBinary)
extension_object_classes[nid] = CreateSessionRequest
extension_object_ids['CreateSessionRequest'] = nid
nid = FourByteNodeId(ObjectIds.CreateSessionResponse_Encoding_DefaultBinary)
extension_object_classes[nid] = CreateSessionResponse
extension_object_ids['CreateSessionResponse'] = nid
nid = FourByteNodeId(ObjectIds.UserIdentityToken_Encoding_DefaultBinary)
extension_object_classes[nid] = UserIdentityToken
extension_object_ids['UserIdentityToken'] = nid
nid = FourByteNodeId(ObjectIds.AnonymousIdentityToken_Encoding_DefaultBinary)
extension_object_classes[nid] = AnonymousIdentityToken
extension_object_ids['AnonymousIdentityToken'] = nid
nid = FourByteNodeId(ObjectIds.UserNameIdentityToken_Encoding_DefaultBinary)
extension_object_classes[nid] = UserNameIdentityToken
extension_object_ids['UserNameIdentityToken'] = nid
nid = FourByteNodeId(ObjectIds.X509IdentityToken_Encoding_DefaultBinary)
extension_object_classes[nid] = X509IdentityToken
extension_object_ids['X509IdentityToken'] = nid
nid = FourByteNodeId(ObjectIds.IssuedIdentityToken_Encoding_DefaultBinary)
extension_object_classes[nid] = IssuedIdentityToken
extension_object_ids['IssuedIdentityToken'] = nid
nid = FourByteNodeId(ObjectIds.ActivateSessionRequest_Encoding_DefaultBinary)
extension_object_classes[nid] = ActivateSessionRequest
extension_object_ids['ActivateSessionRequest'] = nid
nid = FourByteNodeId(ObjectIds.ActivateSessionResponse_Encoding_DefaultBinary)
extension_object_classes[nid] = ActivateSessionResponse
extension_object_ids['ActivateSessionResponse'] = nid
nid = FourByteNodeId(ObjectIds.CloseSessionRequest_Encoding_DefaultBinary)
extension_object_classes[nid] = CloseSessionRequest
extension_object_ids['CloseSessionRequest'] = nid
nid = FourByteNodeId(ObjectIds.CloseSessionResponse_Encoding_DefaultBinary)
extension_object_classes[nid] = CloseSessionResponse
extension_object_ids['CloseSessionResponse'] = nid
nid = FourByteNodeId(ObjectIds.CancelRequest_Encoding_DefaultBinary)
extension_object_classes[nid] = CancelRequest
extension_object_ids['CancelRequest'] = nid
nid = FourByteNodeId(ObjectIds.CancelResponse_Encoding_DefaultBinary)
extension_object_classes[nid] = CancelResponse
extension_object_ids['CancelResponse'] = nid
nid = FourByteNodeId(ObjectIds.NodeAttributes_Encoding_DefaultBinary)
extension_object_classes[nid] = NodeAttributes
extension_object_ids['NodeAttributes'] = nid
nid = FourByteNodeId(ObjectIds.ObjectAttributes_Encoding_DefaultBinary)
extension_object_classes[nid] = ObjectAttributes
extension_object_ids['ObjectAttributes'] = nid
nid = FourByteNodeId(ObjectIds.VariableAttributes_Encoding_DefaultBinary)
extension_object_classes[nid] = VariableAttributes
extension_object_ids['VariableAttributes'] = nid
nid = FourByteNodeId(ObjectIds.MethodAttributes_Encoding_DefaultBinary)
extension_object_classes[nid] = MethodAttributes
extension_object_ids['MethodAttributes'] = nid
nid = FourByteNodeId(ObjectIds.ObjectTypeAttributes_Encoding_DefaultBinary)
extension_object_classes[nid] = ObjectTypeAttributes
extension_object_ids['ObjectTypeAttributes'] = nid
nid = FourByteNodeId(ObjectIds.VariableTypeAttributes_Encoding_DefaultBinary)
extension_object_classes[nid] = VariableTypeAttributes
extension_object_ids['VariableTypeAttributes'] = nid
nid = FourByteNodeId(ObjectIds.ReferenceTypeAttributes_Encoding_DefaultBinary)
extension_object_classes[nid] = ReferenceTypeAttributes
extension_object_ids['ReferenceTypeAttributes'] = nid
nid = FourByteNodeId(ObjectIds.DataTypeAttributes_Encoding_DefaultBinary)
extension_object_classes[nid] = DataTypeAttributes
extension_object_ids['DataTypeAttributes'] = nid
nid = FourByteNodeId(ObjectIds.ViewAttributes_Encoding_DefaultBinary)
extension_object_classes[nid] = ViewAttributes
extension_object_ids['ViewAttributes'] = nid
nid = FourByteNodeId(ObjectIds.GenericAttributeValue_Encoding_DefaultBinary)
extension_object_classes[nid] = GenericAttributeValue
extension_object_ids['GenericAttributeValue'] = nid
nid = FourByteNodeId(ObjectIds.GenericAttributes_Encoding_DefaultBinary)
extension_object_classes[nid] = GenericAttributes
extension_object_ids['GenericAttributes'] = nid
nid = FourByteNodeId(ObjectIds.AddNodesItem_Encoding_DefaultBinary)
extension_object_classes[nid] = AddNodesItem
extension_object_ids['AddNodesItem'] = nid
nid = FourByteNodeId(ObjectIds.AddNodesResult_Encoding_DefaultBinary)
extension_object_classes[nid] = AddNodesResult
extension_object_ids['AddNodesResult'] = nid
nid = FourByteNodeId(ObjectIds.AddNodesRequest_Encoding_DefaultBinary)
extension_object_classes[nid] = AddNodesRequest
extension_object_ids['AddNodesRequest'] = nid
nid = FourByteNodeId(ObjectIds.AddNodesResponse_Encoding_DefaultBinary)
extension_object_classes[nid] = AddNodesResponse
extension_object_ids['AddNodesResponse'] = nid
nid = FourByteNodeId(ObjectIds.AddReferencesItem_Encoding_DefaultBinary)
extension_object_classes[nid] = AddReferencesItem
extension_object_ids['AddReferencesItem'] = nid
nid = FourByteNodeId(ObjectIds.AddReferencesRequest_Encoding_DefaultBinary)
extension_object_classes[nid] = AddReferencesRequest
extension_object_ids['AddReferencesRequest'] = nid
nid = FourByteNodeId(ObjectIds.AddReferencesResponse_Encoding_DefaultBinary)
extension_object_classes[nid] = AddReferencesResponse
extension_object_ids['AddReferencesResponse'] = nid
nid = FourByteNodeId(ObjectIds.DeleteNodesItem_Encoding_DefaultBinary)
extension_object_classes[nid] = DeleteNodesItem
extension_object_ids['DeleteNodesItem'] = nid
nid = FourByteNodeId(ObjectIds.DeleteNodesRequest_Encoding_DefaultBinary)
extension_object_classes[nid] = DeleteNodesRequest
extension_object_ids['DeleteNodesRequest'] = nid
nid = FourByteNodeId(ObjectIds.DeleteNodesResponse_Encoding_DefaultBinary)
extension_object_classes[nid] = DeleteNodesResponse
extension_object_ids['DeleteNodesResponse'] = nid
nid = FourByteNodeId(ObjectIds.DeleteReferencesItem_Encoding_DefaultBinary)
extension_object_classes[nid] = DeleteReferencesItem
extension_object_ids['DeleteReferencesItem'] = nid
nid = FourByteNodeId(ObjectIds.DeleteReferencesRequest_Encoding_DefaultBinary)
extension_object_classes[nid] = DeleteReferencesRequest
extension_object_ids['DeleteReferencesRequest'] = nid
nid = FourByteNodeId(ObjectIds.DeleteReferencesResponse_Encoding_DefaultBinary)
extension_object_classes[nid] = DeleteReferencesResponse
extension_object_ids['DeleteReferencesResponse'] = nid
nid = FourByteNodeId(ObjectIds.ViewDescription_Encoding_DefaultBinary)
extension_object_classes[nid] = ViewDescription
extension_object_ids['ViewDescription'] = nid
nid = FourByteNodeId(ObjectIds.BrowseDescription_Encoding_DefaultBinary)
extension_object_classes[nid] = BrowseDescription
extension_object_ids['BrowseDescription'] = nid
nid = FourByteNodeId(ObjectIds.ReferenceDescription_Encoding_DefaultBinary)
extension_object_classes[nid] = ReferenceDescription
extension_object_ids['ReferenceDescription'] = nid
nid = FourByteNodeId(ObjectIds.BrowseResult_Encoding_DefaultBinary)
extension_object_classes[nid] = BrowseResult
extension_object_ids['BrowseResult'] = nid
nid = FourByteNodeId(ObjectIds.BrowseRequest_Encoding_DefaultBinary)
extension_object_classes[nid] = BrowseRequest
extension_object_ids['BrowseRequest'] = nid
nid = FourByteNodeId(ObjectIds.BrowseResponse_Encoding_DefaultBinary)
extension_object_classes[nid] = BrowseResponse
extension_object_ids['BrowseResponse'] = nid
nid = FourByteNodeId(ObjectIds.BrowseNextRequest_Encoding_DefaultBinary)
extension_object_classes[nid] = BrowseNextRequest
extension_object_ids['BrowseNextRequest'] = nid
nid = FourByteNodeId(ObjectIds.BrowseNextResponse_Encoding_DefaultBinary)
extension_object_classes[nid] = BrowseNextResponse
extension_object_ids['BrowseNextResponse'] = nid
nid = FourByteNodeId(ObjectIds.RelativePathElement_Encoding_DefaultBinary)
extension_object_classes[nid] = RelativePathElement
extension_object_ids['RelativePathElement'] = nid
nid = FourByteNodeId(ObjectIds.RelativePath_Encoding_DefaultBinary)
extension_object_classes[nid] = RelativePath
extension_object_ids['RelativePath'] = nid
nid = FourByteNodeId(ObjectIds.BrowsePath_Encoding_DefaultBinary)
extension_object_classes[nid] = BrowsePath
extension_object_ids['BrowsePath'] = nid
nid = FourByteNodeId(ObjectIds.BrowsePathTarget_Encoding_DefaultBinary)
extension_object_classes[nid] = BrowsePathTarget
extension_object_ids['BrowsePathTarget'] = nid
nid = FourByteNodeId(ObjectIds.BrowsePathResult_Encoding_DefaultBinary)
extension_object_classes[nid] = BrowsePathResult
extension_object_ids['BrowsePathResult'] = nid
nid = FourByteNodeId(ObjectIds.TranslateBrowsePathsToNodeIdsRequest_Encoding_DefaultBinary)
extension_object_classes[nid] = TranslateBrowsePathsToNodeIdsRequest
extension_object_ids['TranslateBrowsePathsToNodeIdsRequest'] = nid
nid = FourByteNodeId(ObjectIds.TranslateBrowsePathsToNodeIdsResponse_Encoding_DefaultBinary)
extension_object_classes[nid] = TranslateBrowsePathsToNodeIdsResponse
extension_object_ids['TranslateBrowsePathsToNodeIdsResponse'] = nid
nid = FourByteNodeId(ObjectIds.RegisterNodesRequest_Encoding_DefaultBinary)
extension_object_classes[nid] = RegisterNodesRequest
extension_object_ids['RegisterNodesRequest'] = nid
nid = FourByteNodeId(ObjectIds.RegisterNodesResponse_Encoding_DefaultBinary)
extension_object_classes[nid] = RegisterNodesResponse
extension_object_ids['RegisterNodesResponse'] = nid
nid = FourByteNodeId(ObjectIds.UnregisterNodesRequest_Encoding_DefaultBinary)
extension_object_classes[nid] = UnregisterNodesRequest
extension_object_ids['UnregisterNodesRequest'] = nid
nid = FourByteNodeId(ObjectIds.UnregisterNodesResponse_Encoding_DefaultBinary)
extension_object_classes[nid] = UnregisterNodesResponse
extension_object_ids['UnregisterNodesResponse'] = nid
nid = FourByteNodeId(ObjectIds.EndpointConfiguration_Encoding_DefaultBinary)
extension_object_classes[nid] = EndpointConfiguration
extension_object_ids['EndpointConfiguration'] = nid
nid = FourByteNodeId(ObjectIds.QueryDataDescription_Encoding_DefaultBinary)
extension_object_classes[nid] = QueryDataDescription
extension_object_ids['QueryDataDescription'] = nid
nid = FourByteNodeId(ObjectIds.NodeTypeDescription_Encoding_DefaultBinary)
extension_object_classes[nid] = NodeTypeDescription
extension_object_ids['NodeTypeDescription'] = nid
nid = FourByteNodeId(ObjectIds.QueryDataSet_Encoding_DefaultBinary)
extension_object_classes[nid] = QueryDataSet
extension_object_ids['QueryDataSet'] = nid
nid = FourByteNodeId(ObjectIds.NodeReference_Encoding_DefaultBinary)
extension_object_classes[nid] = NodeReference
extension_object_ids['NodeReference'] = nid
nid = FourByteNodeId(ObjectIds.ContentFilterElement_Encoding_DefaultBinary)
extension_object_classes[nid] = ContentFilterElement
extension_object_ids['ContentFilterElement'] = nid
nid = FourByteNodeId(ObjectIds.ContentFilter_Encoding_DefaultBinary)
extension_object_classes[nid] = ContentFilter
extension_object_ids['ContentFilter'] = nid
nid = FourByteNodeId(ObjectIds.ElementOperand_Encoding_DefaultBinary)
extension_object_classes[nid] = ElementOperand
extension_object_ids['ElementOperand'] = nid
nid = FourByteNodeId(ObjectIds.LiteralOperand_Encoding_DefaultBinary)
extension_object_classes[nid] = LiteralOperand
extension_object_ids['LiteralOperand'] = nid
nid = FourByteNodeId(ObjectIds.AttributeOperand_Encoding_DefaultBinary)
extension_object_classes[nid] = AttributeOperand
extension_object_ids['AttributeOperand'] = nid
nid = FourByteNodeId(ObjectIds.SimpleAttributeOperand_Encoding_DefaultBinary)
extension_object_classes[nid] = SimpleAttributeOperand
extension_object_ids['SimpleAttributeOperand'] = nid
nid = FourByteNodeId(ObjectIds.ContentFilterElementResult_Encoding_DefaultBinary)
extension_object_classes[nid] = ContentFilterElementResult
extension_object_ids['ContentFilterElementResult'] = nid
nid = FourByteNodeId(ObjectIds.ContentFilterResult_Encoding_DefaultBinary)
extension_object_classes[nid] = ContentFilterResult
extension_object_ids['ContentFilterResult'] = nid
nid = FourByteNodeId(ObjectIds.ParsingResult_Encoding_DefaultBinary)
extension_object_classes[nid] = ParsingResult
extension_object_ids['ParsingResult'] = nid
nid = FourByteNodeId(ObjectIds.QueryFirstRequest_Encoding_DefaultBinary)
extension_object_classes[nid] = QueryFirstRequest
extension_object_ids['QueryFirstRequest'] = nid
nid = FourByteNodeId(ObjectIds.QueryFirstResponse_Encoding_DefaultBinary)
extension_object_classes[nid] = QueryFirstResponse
extension_object_ids['QueryFirstResponse'] = nid
nid = FourByteNodeId(ObjectIds.QueryNextRequest_Encoding_DefaultBinary)
extension_object_classes[nid] = QueryNextRequest
extension_object_ids['QueryNextRequest'] = nid
nid = FourByteNodeId(ObjectIds.QueryNextResponse_Encoding_DefaultBinary)
extension_object_classes[nid] = QueryNextResponse
extension_object_ids['QueryNextResponse'] = nid
nid = FourByteNodeId(ObjectIds.ReadValueId_Encoding_DefaultBinary)
extension_object_classes[nid] = ReadValueId
extension_object_ids['ReadValueId'] = nid
nid = FourByteNodeId(ObjectIds.ReadRequest_Encoding_DefaultBinary)
extension_object_classes[nid] = ReadRequest
extension_object_ids['ReadRequest'] = nid
nid = FourByteNodeId(ObjectIds.ReadResponse_Encoding_DefaultBinary)
extension_object_classes[nid] = ReadResponse
extension_object_ids['ReadResponse'] = nid
nid = FourByteNodeId(ObjectIds.HistoryReadValueId_Encoding_DefaultBinary)
extension_object_classes[nid] = HistoryReadValueId
extension_object_ids['HistoryReadValueId'] = nid
nid = FourByteNodeId(ObjectIds.HistoryReadResult_Encoding_DefaultBinary)
extension_object_classes[nid] = HistoryReadResult
extension_object_ids['HistoryReadResult'] = nid
nid = FourByteNodeId(ObjectIds.HistoryReadDetails_Encoding_DefaultBinary)
extension_object_classes[nid] = HistoryReadDetails
extension_object_ids['HistoryReadDetails'] = nid
nid = FourByteNodeId(ObjectIds.ReadEventDetails_Encoding_DefaultBinary)
extension_object_classes[nid] = ReadEventDetails
extension_object_ids['ReadEventDetails'] = nid
nid = FourByteNodeId(ObjectIds.ReadRawModifiedDetails_Encoding_DefaultBinary)
extension_object_classes[nid] = ReadRawModifiedDetails
extension_object_ids['ReadRawModifiedDetails'] = nid
nid = FourByteNodeId(ObjectIds.ReadProcessedDetails_Encoding_DefaultBinary)
extension_object_classes[nid] = ReadProcessedDetails
extension_object_ids['ReadProcessedDetails'] = nid
nid = FourByteNodeId(ObjectIds.ReadAtTimeDetails_Encoding_DefaultBinary)
extension_object_classes[nid] = ReadAtTimeDetails
extension_object_ids['ReadAtTimeDetails'] = nid
nid = FourByteNodeId(ObjectIds.HistoryData_Encoding_DefaultBinary)
extension_object_classes[nid] = HistoryData
extension_object_ids['HistoryData'] = nid
nid = FourByteNodeId(ObjectIds.ModificationInfo_Encoding_DefaultBinary)
extension_object_classes[nid] = ModificationInfo
extension_object_ids['ModificationInfo'] = nid
nid = FourByteNodeId(ObjectIds.HistoryModifiedData_Encoding_DefaultBinary)
extension_object_classes[nid] = HistoryModifiedData
extension_object_ids['HistoryModifiedData'] = nid
nid = FourByteNodeId(ObjectIds.HistoryEvent_Encoding_DefaultBinary)
extension_object_classes[nid] = HistoryEvent
extension_object_ids['HistoryEvent'] = nid
nid = FourByteNodeId(ObjectIds.HistoryReadRequest_Encoding_DefaultBinary)
extension_object_classes[nid] = HistoryReadRequest
extension_object_ids['HistoryReadRequest'] = nid
nid = FourByteNodeId(ObjectIds.HistoryReadResponse_Encoding_DefaultBinary)
extension_object_classes[nid] = HistoryReadResponse
extension_object_ids['HistoryReadResponse'] = nid
nid = FourByteNodeId(ObjectIds.WriteValue_Encoding_DefaultBinary)
extension_object_classes[nid] = WriteValue
extension_object_ids['WriteValue'] = nid
nid = FourByteNodeId(ObjectIds.WriteRequest_Encoding_DefaultBinary)
extension_object_classes[nid] = WriteRequest
extension_object_ids['WriteRequest'] = nid
nid = FourByteNodeId(ObjectIds.WriteResponse_Encoding_DefaultBinary)
extension_object_classes[nid] = WriteResponse
extension_object_ids['WriteResponse'] = nid
nid = FourByteNodeId(ObjectIds.HistoryUpdateDetails_Encoding_DefaultBinary)
extension_object_classes[nid] = HistoryUpdateDetails
extension_object_ids['HistoryUpdateDetails'] = nid
nid = FourByteNodeId(ObjectIds.UpdateDataDetails_Encoding_DefaultBinary)
extension_object_classes[nid] = UpdateDataDetails
extension_object_ids['UpdateDataDetails'] = nid
nid = FourByteNodeId(ObjectIds.UpdateStructureDataDetails_Encoding_DefaultBinary)
extension_object_classes[nid] = UpdateStructureDataDetails
extension_object_ids['UpdateStructureDataDetails'] = nid
nid = FourByteNodeId(ObjectIds.UpdateEventDetails_Encoding_DefaultBinary)
extension_object_classes[nid] = UpdateEventDetails
extension_object_ids['UpdateEventDetails'] = nid
nid = FourByteNodeId(ObjectIds.DeleteRawModifiedDetails_Encoding_DefaultBinary)
extension_object_classes[nid] = DeleteRawModifiedDetails
extension_object_ids['DeleteRawModifiedDetails'] = nid
nid = FourByteNodeId(ObjectIds.DeleteAtTimeDetails_Encoding_DefaultBinary)
extension_object_classes[nid] = DeleteAtTimeDetails
extension_object_ids['DeleteAtTimeDetails'] = nid
nid = FourByteNodeId(ObjectIds.DeleteEventDetails_Encoding_DefaultBinary)
extension_object_classes[nid] = DeleteEventDetails
extension_object_ids['DeleteEventDetails'] = nid
nid = FourByteNodeId(ObjectIds.HistoryUpdateResult_Encoding_DefaultBinary)
extension_object_classes[nid] = HistoryUpdateResult
extension_object_ids['HistoryUpdateResult'] = nid
nid = FourByteNodeId(ObjectIds.HistoryUpdateRequest_Encoding_DefaultBinary)
extension_object_classes[nid] = HistoryUpdateRequest
extension_object_ids['HistoryUpdateRequest'] = nid
nid = FourByteNodeId(ObjectIds.HistoryUpdateResponse_Encoding_DefaultBinary)
extension_object_classes[nid] = HistoryUpdateResponse
extension_object_ids['HistoryUpdateResponse'] = nid
nid = FourByteNodeId(ObjectIds.CallMethodRequest_Encoding_DefaultBinary)
extension_object_classes[nid] = CallMethodRequest
extension_object_ids['CallMethodRequest'] = nid
nid = FourByteNodeId(ObjectIds.CallMethodResult_Encoding_DefaultBinary)
extension_object_classes[nid] = CallMethodResult
extension_object_ids['CallMethodResult'] = nid
nid = FourByteNodeId(ObjectIds.CallRequest_Encoding_DefaultBinary)
extension_object_classes[nid] = CallRequest
extension_object_ids['CallRequest'] = nid
nid = FourByteNodeId(ObjectIds.CallResponse_Encoding_DefaultBinary)
extension_object_classes[nid] = CallResponse
extension_object_ids['CallResponse'] = nid
nid = FourByteNodeId(ObjectIds.MonitoringFilter_Encoding_DefaultBinary)
extension_object_classes[nid] = MonitoringFilter
extension_object_ids['MonitoringFilter'] = nid
nid = FourByteNodeId(ObjectIds.DataChangeFilter_Encoding_DefaultBinary)
extension_object_classes[nid] = DataChangeFilter
extension_object_ids['DataChangeFilter'] = nid
nid = FourByteNodeId(ObjectIds.EventFilter_Encoding_DefaultBinary)
extension_object_classes[nid] = EventFilter
extension_object_ids['EventFilter'] = nid
nid = FourByteNodeId(ObjectIds.AggregateConfiguration_Encoding_DefaultBinary)
extension_object_classes[nid] = AggregateConfiguration
extension_object_ids['AggregateConfiguration'] = nid
nid = FourByteNodeId(ObjectIds.AggregateFilter_Encoding_DefaultBinary)
extension_object_classes[nid] = AggregateFilter
extension_object_ids['AggregateFilter'] = nid
nid = FourByteNodeId(ObjectIds.MonitoringFilterResult_Encoding_DefaultBinary)
extension_object_classes[nid] = MonitoringFilterResult
extension_object_ids['MonitoringFilterResult'] = nid
nid = FourByteNodeId(ObjectIds.EventFilterResult_Encoding_DefaultBinary)
extension_object_classes[nid] = EventFilterResult
extension_object_ids['EventFilterResult'] = nid
nid = FourByteNodeId(ObjectIds.AggregateFilterResult_Encoding_DefaultBinary)
extension_object_classes[nid] = AggregateFilterResult
extension_object_ids['AggregateFilterResult'] = nid
nid = FourByteNodeId(ObjectIds.MonitoringParameters_Encoding_DefaultBinary)
extension_object_classes[nid] = MonitoringParameters
extension_object_ids['MonitoringParameters'] = nid
nid = FourByteNodeId(ObjectIds.MonitoredItemCreateRequest_Encoding_DefaultBinary)
extension_object_classes[nid] = MonitoredItemCreateRequest
extension_object_ids['MonitoredItemCreateRequest'] = nid
nid = FourByteNodeId(ObjectIds.MonitoredItemCreateResult_Encoding_DefaultBinary)
extension_object_classes[nid] = MonitoredItemCreateResult
extension_object_ids['MonitoredItemCreateResult'] = nid
nid = FourByteNodeId(ObjectIds.CreateMonitoredItemsRequest_Encoding_DefaultBinary)
extension_object_classes[nid] = CreateMonitoredItemsRequest
extension_object_ids['CreateMonitoredItemsRequest'] = nid
nid = FourByteNodeId(ObjectIds.CreateMonitoredItemsResponse_Encoding_DefaultBinary)
extension_object_classes[nid] = CreateMonitoredItemsResponse
extension_object_ids['CreateMonitoredItemsResponse'] = nid
nid = FourByteNodeId(ObjectIds.MonitoredItemModifyRequest_Encoding_DefaultBinary)
extension_object_classes[nid] = MonitoredItemModifyRequest
extension_object_ids['MonitoredItemModifyRequest'] = nid
nid = FourByteNodeId(ObjectIds.MonitoredItemModifyResult_Encoding_DefaultBinary)
extension_object_classes[nid] = MonitoredItemModifyResult
extension_object_ids['MonitoredItemModifyResult'] = nid
nid = FourByteNodeId(ObjectIds.ModifyMonitoredItemsRequest_Encoding_DefaultBinary)
extension_object_classes[nid] = ModifyMonitoredItemsRequest
extension_object_ids['ModifyMonitoredItemsRequest'] = nid
nid = FourByteNodeId(ObjectIds.ModifyMonitoredItemsResponse_Encoding_DefaultBinary)
extension_object_classes[nid] = ModifyMonitoredItemsResponse
extension_object_ids['ModifyMonitoredItemsResponse'] = nid
nid = FourByteNodeId(ObjectIds.SetMonitoringModeRequest_Encoding_DefaultBinary)
extension_object_classes[nid] = SetMonitoringModeRequest
extension_object_ids['SetMonitoringModeRequest'] = nid
nid = FourByteNodeId(ObjectIds.SetMonitoringModeResponse_Encoding_DefaultBinary)
extension_object_classes[nid] = SetMonitoringModeResponse
extension_object_ids['SetMonitoringModeResponse'] = nid
nid = FourByteNodeId(ObjectIds.SetTriggeringRequest_Encoding_DefaultBinary)
extension_object_classes[nid] = SetTriggeringRequest
extension_object_ids['SetTriggeringRequest'] = nid
nid = FourByteNodeId(ObjectIds.SetTriggeringResponse_Encoding_DefaultBinary)
extension_object_classes[nid] = SetTriggeringResponse
extension_object_ids['SetTriggeringResponse'] = nid
nid = FourByteNodeId(ObjectIds.DeleteMonitoredItemsRequest_Encoding_DefaultBinary)
extension_object_classes[nid] = DeleteMonitoredItemsRequest
extension_object_ids['DeleteMonitoredItemsRequest'] = nid
nid = FourByteNodeId(ObjectIds.DeleteMonitoredItemsResponse_Encoding_DefaultBinary)
extension_object_classes[nid] = DeleteMonitoredItemsResponse
extension_object_ids['DeleteMonitoredItemsResponse'] = nid
nid = FourByteNodeId(ObjectIds.CreateSubscriptionRequest_Encoding_DefaultBinary)
extension_object_classes[nid] = CreateSubscriptionRequest
extension_object_ids['CreateSubscriptionRequest'] = nid
nid = FourByteNodeId(ObjectIds.CreateSubscriptionResponse_Encoding_DefaultBinary)
extension_object_classes[nid] = CreateSubscriptionResponse
extension_object_ids['CreateSubscriptionResponse'] = nid
nid = FourByteNodeId(ObjectIds.ModifySubscriptionRequest_Encoding_DefaultBinary)
extension_object_classes[nid] = ModifySubscriptionRequest
extension_object_ids['ModifySubscriptionRequest'] = nid
nid = FourByteNodeId(ObjectIds.ModifySubscriptionResponse_Encoding_DefaultBinary)
extension_object_classes[nid] = ModifySubscriptionResponse
extension_object_ids['ModifySubscriptionResponse'] = nid
nid = FourByteNodeId(ObjectIds.SetPublishingModeRequest_Encoding_DefaultBinary)
extension_object_classes[nid] = SetPublishingModeRequest
extension_object_ids['SetPublishingModeRequest'] = nid
nid = FourByteNodeId(ObjectIds.SetPublishingModeResponse_Encoding_DefaultBinary)
extension_object_classes[nid] = SetPublishingModeResponse
extension_object_ids['SetPublishingModeResponse'] = nid
nid = FourByteNodeId(ObjectIds.NotificationMessage_Encoding_DefaultBinary)
extension_object_classes[nid] = NotificationMessage
extension_object_ids['NotificationMessage'] = nid
nid = FourByteNodeId(ObjectIds.NotificationData_Encoding_DefaultBinary)
extension_object_classes[nid] = NotificationData
extension_object_ids['NotificationData'] = nid
nid = FourByteNodeId(ObjectIds.DataChangeNotification_Encoding_DefaultBinary)
extension_object_classes[nid] = DataChangeNotification
extension_object_ids['DataChangeNotification'] = nid
nid = FourByteNodeId(ObjectIds.MonitoredItemNotification_Encoding_DefaultBinary)
extension_object_classes[nid] = MonitoredItemNotification
extension_object_ids['MonitoredItemNotification'] = nid
nid = FourByteNodeId(ObjectIds.EventNotificationList_Encoding_DefaultBinary)
extension_object_classes[nid] = EventNotificationList
extension_object_ids['EventNotificationList'] = nid
nid = FourByteNodeId(ObjectIds.EventFieldList_Encoding_DefaultBinary)
extension_object_classes[nid] = EventFieldList
extension_object_ids['EventFieldList'] = nid
nid = FourByteNodeId(ObjectIds.HistoryEventFieldList_Encoding_DefaultBinary)
extension_object_classes[nid] = HistoryEventFieldList
extension_object_ids['HistoryEventFieldList'] = nid
nid = FourByteNodeId(ObjectIds.StatusChangeNotification_Encoding_DefaultBinary)
extension_object_classes[nid] = StatusChangeNotification
extension_object_ids['StatusChangeNotification'] = nid
nid = FourByteNodeId(ObjectIds.SubscriptionAcknowledgement_Encoding_DefaultBinary)
extension_object_classes[nid] = SubscriptionAcknowledgement
extension_object_ids['SubscriptionAcknowledgement'] = nid
nid = FourByteNodeId(ObjectIds.PublishRequest_Encoding_DefaultBinary)
extension_object_classes[nid] = PublishRequest
extension_object_ids['PublishRequest'] = nid
nid = FourByteNodeId(ObjectIds.PublishResponse_Encoding_DefaultBinary)
extension_object_classes[nid] = PublishResponse
extension_object_ids['PublishResponse'] = nid
nid = FourByteNodeId(ObjectIds.RepublishRequest_Encoding_DefaultBinary)
extension_object_classes[nid] = RepublishRequest
extension_object_ids['RepublishRequest'] = nid
nid = FourByteNodeId(ObjectIds.RepublishResponse_Encoding_DefaultBinary)
extension_object_classes[nid] = RepublishResponse
extension_object_ids['RepublishResponse'] = nid
nid = FourByteNodeId(ObjectIds.TransferResult_Encoding_DefaultBinary)
extension_object_classes[nid] = TransferResult
extension_object_ids['TransferResult'] = nid
nid = FourByteNodeId(ObjectIds.TransferSubscriptionsRequest_Encoding_DefaultBinary)
extension_object_classes[nid] = TransferSubscriptionsRequest
extension_object_ids['TransferSubscriptionsRequest'] = nid
nid = FourByteNodeId(ObjectIds.TransferSubscriptionsResponse_Encoding_DefaultBinary)
extension_object_classes[nid] = TransferSubscriptionsResponse
extension_object_ids['TransferSubscriptionsResponse'] = nid
nid = FourByteNodeId(ObjectIds.DeleteSubscriptionsRequest_Encoding_DefaultBinary)
extension_object_classes[nid] = DeleteSubscriptionsRequest
extension_object_ids['DeleteSubscriptionsRequest'] = nid
nid = FourByteNodeId(ObjectIds.DeleteSubscriptionsResponse_Encoding_DefaultBinary)
extension_object_classes[nid] = DeleteSubscriptionsResponse
extension_object_ids['DeleteSubscriptionsResponse'] = nid
nid = FourByteNodeId(ObjectIds.BuildInfo_Encoding_DefaultBinary)
extension_object_classes[nid] = BuildInfo
extension_object_ids['BuildInfo'] = nid
nid = FourByteNodeId(ObjectIds.RedundantServerDataType_Encoding_DefaultBinary)
extension_object_classes[nid] = RedundantServerDataType
extension_object_ids['RedundantServerDataType'] = nid
nid = FourByteNodeId(ObjectIds.EndpointUrlListDataType_Encoding_DefaultBinary)
extension_object_classes[nid] = EndpointUrlListDataType
extension_object_ids['EndpointUrlListDataType'] = nid
nid = FourByteNodeId(ObjectIds.NetworkGroupDataType_Encoding_DefaultBinary)
extension_object_classes[nid] = NetworkGroupDataType
extension_object_ids['NetworkGroupDataType'] = nid
nid = FourByteNodeId(ObjectIds.SamplingIntervalDiagnosticsDataType_Encoding_DefaultBinary)
extension_object_classes[nid] = SamplingIntervalDiagnosticsDataType
extension_object_ids['SamplingIntervalDiagnosticsDataType'] = nid
nid = FourByteNodeId(ObjectIds.ServerDiagnosticsSummaryDataType_Encoding_DefaultBinary)
extension_object_classes[nid] = ServerDiagnosticsSummaryDataType
extension_object_ids['ServerDiagnosticsSummaryDataType'] = nid
nid = FourByteNodeId(ObjectIds.ServerStatusDataType_Encoding_DefaultBinary)
extension_object_classes[nid] = ServerStatusDataType
extension_object_ids['ServerStatusDataType'] = nid
nid = FourByteNodeId(ObjectIds.SessionDiagnosticsDataType_Encoding_DefaultBinary)
extension_object_classes[nid] = SessionDiagnosticsDataType
extension_object_ids['SessionDiagnosticsDataType'] = nid
nid = FourByteNodeId(ObjectIds.SessionSecurityDiagnosticsDataType_Encoding_DefaultBinary)
extension_object_classes[nid] = SessionSecurityDiagnosticsDataType
extension_object_ids['SessionSecurityDiagnosticsDataType'] = nid
nid = FourByteNodeId(ObjectIds.ServiceCounterDataType_Encoding_DefaultBinary)
extension_object_classes[nid] = ServiceCounterDataType
extension_object_ids['ServiceCounterDataType'] = nid
nid = FourByteNodeId(ObjectIds.StatusResult_Encoding_DefaultBinary)
extension_object_classes[nid] = StatusResult
extension_object_ids['StatusResult'] = nid
nid = FourByteNodeId(ObjectIds.SubscriptionDiagnosticsDataType_Encoding_DefaultBinary)
extension_object_classes[nid] = SubscriptionDiagnosticsDataType
extension_object_ids['SubscriptionDiagnosticsDataType'] = nid
nid = FourByteNodeId(ObjectIds.ModelChangeStructureDataType_Encoding_DefaultBinary)
extension_object_classes[nid] = ModelChangeStructureDataType
extension_object_ids['ModelChangeStructureDataType'] = nid
nid = FourByteNodeId(ObjectIds.SemanticChangeStructureDataType_Encoding_DefaultBinary)
extension_object_classes[nid] = SemanticChangeStructureDataType
extension_object_ids['SemanticChangeStructureDataType'] = nid
nid = FourByteNodeId(ObjectIds.Range_Encoding_DefaultBinary)
extension_object_classes[nid] = Range
extension_object_ids['Range'] = nid
nid = FourByteNodeId(ObjectIds.EUInformation_Encoding_DefaultBinary)
extension_object_classes[nid] = EUInformation
extension_object_ids['EUInformation'] = nid
nid = FourByteNodeId(ObjectIds.ComplexNumberType_Encoding_DefaultBinary)
extension_object_classes[nid] = ComplexNumberType
extension_object_ids['ComplexNumberType'] = nid
nid = FourByteNodeId(ObjectIds.DoubleComplexNumberType_Encoding_DefaultBinary)
extension_object_classes[nid] = DoubleComplexNumberType
extension_object_ids['DoubleComplexNumberType'] = nid
nid = FourByteNodeId(ObjectIds.AxisInformation_Encoding_DefaultBinary)
extension_object_classes[nid] = AxisInformation
extension_object_ids['AxisInformation'] = nid
nid = FourByteNodeId(ObjectIds.XVType_Encoding_DefaultBinary)
extension_object_classes[nid] = XVType
extension_object_ids['XVType'] = nid
nid = FourByteNodeId(ObjectIds.ProgramDiagnosticDataType_Encoding_DefaultBinary)
extension_object_classes[nid] = ProgramDiagnosticDataType
extension_object_ids['ProgramDiagnosticDataType'] = nid
nid = FourByteNodeId(ObjectIds.ProgramDiagnostic2DataType_Encoding_DefaultBinary)
extension_object_classes[nid] = ProgramDiagnostic2DataType
extension_object_ids['ProgramDiagnostic2DataType'] = nid
nid = FourByteNodeId(ObjectIds.Annotation_Encoding_DefaultBinary)
extension_object_classes[nid] = Annotation
extension_object_ids['Annotation'] = nid
