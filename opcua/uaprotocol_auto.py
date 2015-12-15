'''
Autogenerate code from xml spec
'''

from datetime import datetime

from opcua.utils import Buffer
from opcua.uatypes import *
from opcua.object_ids import ObjectIds


class NamingRuleType(object):
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


class OpenFileMode(object):
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


class TrustListMasks(object):
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


class IdType(object):
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


class NodeClass(object):
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


class ApplicationType(object):
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


class MessageSecurityMode(object):
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


class UserTokenType(object):
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
    :ivar Kerberos:
    :vartype Kerberos: 4
    '''
    Anonymous = 0
    UserName = 1
    Certificate = 2
    IssuedToken = 3
    Kerberos = 4


class SecurityTokenRequestType(object):
    '''
    Indicates whether a token if being created or renewed.

    :ivar Issue:
    :vartype Issue: 0
    :ivar Renew:
    :vartype Renew: 1
    '''
    Issue = 0
    Renew = 1


class NodeAttributesMask(object):
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
    :ivar All:
    :vartype All: 4194303
    :ivar BaseNode:
    :vartype BaseNode: 1335396
    :ivar Object:
    :vartype Object: 1335524
    :ivar ObjectTypeOrDataType:
    :vartype ObjectTypeOrDataType: 1337444
    :ivar Variable:
    :vartype Variable: 4026999
    :ivar VariableType:
    :vartype VariableType: 3958902
    :ivar Method:
    :vartype Method: 1466724
    :ivar ReferenceType:
    :vartype ReferenceType: 1371236
    :ivar View:
    :vartype View: 1335532
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
    All = 4194303
    BaseNode = 1335396
    Object = 1335524
    ObjectTypeOrDataType = 1337444
    Variable = 4026999
    VariableType = 3958902
    Method = 1466724
    ReferenceType = 1371236
    View = 1335532


class AttributeWriteMask(object):
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


class BrowseDirection(object):
    '''
    The directions of the references to return.

    :ivar Forward:
    :vartype Forward: 0
    :ivar Inverse:
    :vartype Inverse: 1
    :ivar Both:
    :vartype Both: 2
    '''
    Forward = 0
    Inverse = 1
    Both = 2


class BrowseResultMask(object):
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


class ComplianceLevel(object):
    '''
    :ivar Untested:
    :vartype Untested: 0
    :ivar Partial:
    :vartype Partial: 1
    :ivar SelfTested:
    :vartype SelfTested: 2
    :ivar Certified:
    :vartype Certified: 3
    '''
    Untested = 0
    Partial = 1
    SelfTested = 2
    Certified = 3


class FilterOperator(object):
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


class TimestampsToReturn(object):
    '''
    :ivar Source:
    :vartype Source: 0
    :ivar Server:
    :vartype Server: 1
    :ivar Both:
    :vartype Both: 2
    :ivar Neither:
    :vartype Neither: 3
    '''
    Source = 0
    Server = 1
    Both = 2
    Neither = 3


class HistoryUpdateType(object):
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


class PerformUpdateType(object):
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


class MonitoringMode(object):
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


class DataChangeTrigger(object):
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


class DeadbandType(object):
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


class EnumeratedTestType(object):
    '''
    A simple enumerated type used for testing.

    :ivar Red:
    :vartype Red: 1
    :ivar Yellow:
    :vartype Yellow: 4
    :ivar Green:
    :vartype Green: 5
    '''
    Red = 1
    Yellow = 4
    Green = 5


class RedundancySupport(object):
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


class ServerState(object):
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


class ModelChangeStructureVerbMask(object):
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


class AxisScaleEnumeration(object):
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


class ExceptionDeviationFormat(object):
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


class XmlElement(FrozenClass):
    '''
    An XML element encoded as a UTF-8 string.

    :ivar Length:
    :vartype Length: Int32
    :ivar Value:
    :vartype Value: Char
    '''
    def __init__(self):
        self.Length = 0
        self.Value = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('Int32', self.Length))
        packet.append(struct.pack('<i', len(self.Value)))
        for fieldname in self.Value:
            packet.append(pack_uatype('Char', fieldname))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = XmlElement()
        obj.Length = unpack_uatype('Int32', data)
        obj.Value = unpack_uatype_array('Char', data)
        return obj

    def __str__(self):
        return 'XmlElement(' + 'Length:' + str(self.Length) + ', ' + \
               'Value:' + str(self.Value) + ')'

    __repr__ = __str__


class DiagnosticInfo(FrozenClass):
    '''
    A recursive structure containing diagnostic information associated with a status code.

    :ivar Encoding:
    :vartype Encoding: UInt8
    :ivar SymbolicId:
    :vartype SymbolicId: Int32
    :ivar NamespaceURI:
    :vartype NamespaceURI: Int32
    :ivar Locale:
    :vartype Locale: Int32
    :ivar LocalizedText:
    :vartype LocalizedText: Int32
    :ivar AdditionalInfo:
    :vartype AdditionalInfo: CharArray
    :ivar InnerStatusCode:
    :vartype InnerStatusCode: StatusCode
    :ivar InnerDiagnosticInfo:
    :vartype InnerDiagnosticInfo: DiagnosticInfo
    '''
    def __init__(self):
        self.Encoding = 0
        self.SymbolicId = 0
        self.NamespaceURI = 0
        self.Locale = 0
        self.LocalizedText = 0
        self.AdditionalInfo = b''
        self.InnerStatusCode = StatusCode()
        self.InnerDiagnosticInfo = None
        self._freeze()

    def to_binary(self):
        packet = []
        if self.SymbolicId: self.Encoding |= (1 << 0)
        if self.NamespaceURI: self.Encoding |= (1 << 1)
        if self.Locale: self.Encoding |= (1 << 2)
        if self.LocalizedText: self.Encoding |= (1 << 3)
        if self.AdditionalInfo: self.Encoding |= (1 << 4)
        if self.InnerStatusCode: self.Encoding |= (1 << 5)
        if self.InnerDiagnosticInfo: self.Encoding |= (1 << 6)
        packet.append(pack_uatype('UInt8', self.Encoding))
        if self.SymbolicId: 
            packet.append(pack_uatype('Int32', self.SymbolicId))
        if self.NamespaceURI: 
            packet.append(pack_uatype('Int32', self.NamespaceURI))
        if self.Locale: 
            packet.append(pack_uatype('Int32', self.Locale))
        if self.LocalizedText: 
            packet.append(pack_uatype('Int32', self.LocalizedText))
        if self.AdditionalInfo: 
            packet.append(pack_uatype('CharArray', self.AdditionalInfo))
        if self.InnerStatusCode: 
            packet.append(self.InnerStatusCode.to_binary())
        if self.InnerDiagnosticInfo: 
            packet.append(self.InnerDiagnosticInfo.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = DiagnosticInfo()
        obj.Encoding = unpack_uatype('UInt8', data)
        if obj.Encoding & (1 << 0):
            obj.SymbolicId = unpack_uatype('Int32', data)
        if obj.Encoding & (1 << 1):
            obj.NamespaceURI = unpack_uatype('Int32', data)
        if obj.Encoding & (1 << 2):
            obj.Locale = unpack_uatype('Int32', data)
        if obj.Encoding & (1 << 3):
            obj.LocalizedText = unpack_uatype('Int32', data)
        if obj.Encoding & (1 << 4):
            obj.AdditionalInfo = unpack_uatype('CharArray', data)
        if obj.Encoding & (1 << 5):
            obj.InnerStatusCode = StatusCode.from_binary(data)
        if obj.Encoding & (1 << 6):
            obj.InnerDiagnosticInfo = DiagnosticInfo.from_binary(data)
        return obj

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
    def __init__(self):
        self.SpecifiedLists = 0
        self.TrustedCertificates = []
        self.TrustedCrls = []
        self.IssuerCertificates = []
        self.IssuerCrls = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('UInt32', self.SpecifiedLists))
        packet.append(struct.pack('<i', len(self.TrustedCertificates)))
        for fieldname in self.TrustedCertificates:
            packet.append(pack_uatype('ByteString', fieldname))
        packet.append(struct.pack('<i', len(self.TrustedCrls)))
        for fieldname in self.TrustedCrls:
            packet.append(pack_uatype('ByteString', fieldname))
        packet.append(struct.pack('<i', len(self.IssuerCertificates)))
        for fieldname in self.IssuerCertificates:
            packet.append(pack_uatype('ByteString', fieldname))
        packet.append(struct.pack('<i', len(self.IssuerCrls)))
        for fieldname in self.IssuerCrls:
            packet.append(pack_uatype('ByteString', fieldname))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = TrustListDataType()
        obj.SpecifiedLists = unpack_uatype('UInt32', data)
        obj.TrustedCertificates = unpack_uatype_array('ByteString', data)
        obj.TrustedCrls = unpack_uatype_array('ByteString', data)
        obj.IssuerCertificates = unpack_uatype_array('ByteString', data)
        obj.IssuerCrls = unpack_uatype_array('ByteString', data)
        return obj

    def __str__(self):
        return 'TrustListDataType(' + 'SpecifiedLists:' + str(self.SpecifiedLists) + ', ' + \
               'TrustedCertificates:' + str(self.TrustedCertificates) + ', ' + \
               'TrustedCrls:' + str(self.TrustedCrls) + ', ' + \
               'IssuerCertificates:' + str(self.IssuerCertificates) + ', ' + \
               'IssuerCrls:' + str(self.IssuerCrls) + ')'

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
    def __init__(self):
        self.Name = ''
        self.DataType = NodeId()
        self.ValueRank = 0
        self.ArrayDimensions = []
        self.Description = LocalizedText()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('String', self.Name))
        packet.append(self.DataType.to_binary())
        packet.append(pack_uatype('Int32', self.ValueRank))
        packet.append(struct.pack('<i', len(self.ArrayDimensions)))
        for fieldname in self.ArrayDimensions:
            packet.append(pack_uatype('UInt32', fieldname))
        packet.append(self.Description.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = Argument()
        obj.Name = unpack_uatype('String', data)
        obj.DataType = NodeId.from_binary(data)
        obj.ValueRank = unpack_uatype('Int32', data)
        obj.ArrayDimensions = unpack_uatype_array('UInt32', data)
        obj.Description = LocalizedText.from_binary(data)
        return obj

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
    def __init__(self):
        self.Value = 0
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('Int64', self.Value))
        packet.append(self.DisplayName.to_binary())
        packet.append(self.Description.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = EnumValueType()
        obj.Value = unpack_uatype('Int64', data)
        obj.DisplayName = LocalizedText.from_binary(data)
        obj.Description = LocalizedText.from_binary(data)
        return obj

    def __str__(self):
        return 'EnumValueType(' + 'Value:' + str(self.Value) + ', ' + \
               'DisplayName:' + str(self.DisplayName) + ', ' + \
               'Description:' + str(self.Description) + ')'

    __repr__ = __str__


class OptionSet(FrozenClass):
    '''
    This abstract Structured DataType is the base DataType for all DataTypes representing a bit mask.

    :ivar Value:
    :vartype Value: ByteString
    :ivar ValidBits:
    :vartype ValidBits: ByteString
    '''
    def __init__(self):
        self.Value = b''
        self.ValidBits = b''
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('ByteString', self.Value))
        packet.append(pack_uatype('ByteString', self.ValidBits))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = OptionSet()
        obj.Value = unpack_uatype('ByteString', data)
        obj.ValidBits = unpack_uatype('ByteString', data)
        return obj

    def __str__(self):
        return 'OptionSet(' + 'Value:' + str(self.Value) + ', ' + \
               'ValidBits:' + str(self.ValidBits) + ')'

    __repr__ = __str__


class Union(FrozenClass):
    '''
    This abstract DataType is the base DataType for all union DataTypes.

    '''
    def __init__(self):
        self._freeze()

    def to_binary(self):
        packet = []
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = Union()
        return obj

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
    def __init__(self):
        self.Offset = 0
        self.DaylightSavingInOffset = True
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('Int16', self.Offset))
        packet.append(pack_uatype('Boolean', self.DaylightSavingInOffset))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = TimeZoneDataType()
        obj.Offset = unpack_uatype('Int16', data)
        obj.DaylightSavingInOffset = unpack_uatype('Boolean', data)
        return obj

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
    def __init__(self):
        self.ApplicationUri = ''
        self.ProductUri = ''
        self.ApplicationName = LocalizedText()
        self.ApplicationType = 0
        self.GatewayServerUri = ''
        self.DiscoveryProfileUri = ''
        self.DiscoveryUrls = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('String', self.ApplicationUri))
        packet.append(pack_uatype('String', self.ProductUri))
        packet.append(self.ApplicationName.to_binary())
        packet.append(pack_uatype('UInt32', self.ApplicationType))
        packet.append(pack_uatype('String', self.GatewayServerUri))
        packet.append(pack_uatype('String', self.DiscoveryProfileUri))
        packet.append(struct.pack('<i', len(self.DiscoveryUrls)))
        for fieldname in self.DiscoveryUrls:
            packet.append(pack_uatype('String', fieldname))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = ApplicationDescription()
        obj.ApplicationUri = unpack_uatype('String', data)
        obj.ProductUri = unpack_uatype('String', data)
        obj.ApplicationName = LocalizedText.from_binary(data)
        obj.ApplicationType = unpack_uatype('UInt32', data)
        obj.GatewayServerUri = unpack_uatype('String', data)
        obj.DiscoveryProfileUri = unpack_uatype('String', data)
        obj.DiscoveryUrls = unpack_uatype_array('String', data)
        return obj

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
    def __init__(self):
        self.AuthenticationToken = NodeId()
        self.Timestamp = datetime.now()
        self.RequestHandle = 0
        self.ReturnDiagnostics = 0
        self.AuditEntryId = ''
        self.TimeoutHint = 0
        self.AdditionalHeader = None
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.AuthenticationToken.to_binary())
        packet.append(pack_uatype('DateTime', self.Timestamp))
        packet.append(pack_uatype('UInt32', self.RequestHandle))
        packet.append(pack_uatype('UInt32', self.ReturnDiagnostics))
        packet.append(pack_uatype('String', self.AuditEntryId))
        packet.append(pack_uatype('UInt32', self.TimeoutHint))
        packet.append(extensionobject_to_binary(self.AdditionalHeader))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = RequestHeader()
        obj.AuthenticationToken = NodeId.from_binary(data)
        obj.Timestamp = unpack_uatype('DateTime', data)
        obj.RequestHandle = unpack_uatype('UInt32', data)
        obj.ReturnDiagnostics = unpack_uatype('UInt32', data)
        obj.AuditEntryId = unpack_uatype('String', data)
        obj.TimeoutHint = unpack_uatype('UInt32', data)
        obj.AdditionalHeader = extensionobject_from_binary(data)
        return obj

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
    def __init__(self):
        self.Timestamp = datetime.now()
        self.RequestHandle = 0
        self.ServiceResult = StatusCode()
        self.ServiceDiagnostics = DiagnosticInfo()
        self.StringTable = []
        self.AdditionalHeader = None
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('DateTime', self.Timestamp))
        packet.append(pack_uatype('UInt32', self.RequestHandle))
        packet.append(self.ServiceResult.to_binary())
        packet.append(self.ServiceDiagnostics.to_binary())
        packet.append(struct.pack('<i', len(self.StringTable)))
        for fieldname in self.StringTable:
            packet.append(pack_uatype('String', fieldname))
        packet.append(extensionobject_to_binary(self.AdditionalHeader))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = ResponseHeader()
        obj.Timestamp = unpack_uatype('DateTime', data)
        obj.RequestHandle = unpack_uatype('UInt32', data)
        obj.ServiceResult = StatusCode.from_binary(data)
        obj.ServiceDiagnostics = DiagnosticInfo.from_binary(data)
        obj.StringTable = unpack_uatype_array('String', data)
        obj.AdditionalHeader = extensionobject_from_binary(data)
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.ServiceFault_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = ServiceFault()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        return obj

    def __str__(self):
        return 'ServiceFault(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'ResponseHeader:' + str(self.ResponseHeader) + ')'

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
    def __init__(self):
        self.EndpointUrl = ''
        self.LocaleIds = []
        self.ServerUris = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('String', self.EndpointUrl))
        packet.append(struct.pack('<i', len(self.LocaleIds)))
        for fieldname in self.LocaleIds:
            packet.append(pack_uatype('String', fieldname))
        packet.append(struct.pack('<i', len(self.ServerUris)))
        for fieldname in self.ServerUris:
            packet.append(pack_uatype('String', fieldname))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = FindServersParameters()
        obj.EndpointUrl = unpack_uatype('String', data)
        obj.LocaleIds = unpack_uatype_array('String', data)
        obj.ServerUris = unpack_uatype_array('String', data)
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.FindServersRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = FindServersParameters()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = FindServersRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = FindServersParameters.from_binary(data)
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.FindServersResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Servers = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(struct.pack('<i', len(self.Servers)))
        for fieldname in self.Servers:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = FindServersResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.Servers.append(ApplicationDescription.from_binary(data))
        return obj

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
    def __init__(self):
        self.RecordId = 0
        self.ServerName = ''
        self.DiscoveryUrl = ''
        self.ServerCapabilities = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('UInt32', self.RecordId))
        packet.append(pack_uatype('String', self.ServerName))
        packet.append(pack_uatype('String', self.DiscoveryUrl))
        packet.append(struct.pack('<i', len(self.ServerCapabilities)))
        for fieldname in self.ServerCapabilities:
            packet.append(pack_uatype('String', fieldname))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = ServerOnNetwork()
        obj.RecordId = unpack_uatype('UInt32', data)
        obj.ServerName = unpack_uatype('String', data)
        obj.DiscoveryUrl = unpack_uatype('String', data)
        obj.ServerCapabilities = unpack_uatype_array('String', data)
        return obj

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
    def __init__(self):
        self.StartingRecordId = 0
        self.MaxRecordsToReturn = 0
        self.ServerCapabilityFilter = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('UInt32', self.StartingRecordId))
        packet.append(pack_uatype('UInt32', self.MaxRecordsToReturn))
        packet.append(struct.pack('<i', len(self.ServerCapabilityFilter)))
        for fieldname in self.ServerCapabilityFilter:
            packet.append(pack_uatype('String', fieldname))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = FindServersOnNetworkParameters()
        obj.StartingRecordId = unpack_uatype('UInt32', data)
        obj.MaxRecordsToReturn = unpack_uatype('UInt32', data)
        obj.ServerCapabilityFilter = unpack_uatype_array('String', data)
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.FindServersOnNetworkRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = FindServersOnNetworkParameters()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = FindServersOnNetworkRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = FindServersOnNetworkParameters.from_binary(data)
        return obj

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
    def __init__(self):
        self.LastCounterResetTime = datetime.now()
        self.Servers = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('DateTime', self.LastCounterResetTime))
        packet.append(struct.pack('<i', len(self.Servers)))
        for fieldname in self.Servers:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = FindServersOnNetworkResult()
        obj.LastCounterResetTime = unpack_uatype('DateTime', data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.Servers.append(ServerOnNetwork.from_binary(data))
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.FindServersOnNetworkResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = FindServersOnNetworkResult()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = FindServersOnNetworkResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = FindServersOnNetworkResult.from_binary(data)
        return obj

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
    def __init__(self):
        self.PolicyId = ''
        self.TokenType = 0
        self.IssuedTokenType = ''
        self.IssuerEndpointUrl = ''
        self.SecurityPolicyUri = ''
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('String', self.PolicyId))
        packet.append(pack_uatype('UInt32', self.TokenType))
        packet.append(pack_uatype('String', self.IssuedTokenType))
        packet.append(pack_uatype('String', self.IssuerEndpointUrl))
        packet.append(pack_uatype('String', self.SecurityPolicyUri))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = UserTokenPolicy()
        obj.PolicyId = unpack_uatype('String', data)
        obj.TokenType = unpack_uatype('UInt32', data)
        obj.IssuedTokenType = unpack_uatype('String', data)
        obj.IssuerEndpointUrl = unpack_uatype('String', data)
        obj.SecurityPolicyUri = unpack_uatype('String', data)
        return obj

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
    def __init__(self):
        self.EndpointUrl = ''
        self.Server = ApplicationDescription()
        self.ServerCertificate = b''
        self.SecurityMode = 0
        self.SecurityPolicyUri = ''
        self.UserIdentityTokens = []
        self.TransportProfileUri = ''
        self.SecurityLevel = 0
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('String', self.EndpointUrl))
        packet.append(self.Server.to_binary())
        packet.append(pack_uatype('ByteString', self.ServerCertificate))
        packet.append(pack_uatype('UInt32', self.SecurityMode))
        packet.append(pack_uatype('String', self.SecurityPolicyUri))
        packet.append(struct.pack('<i', len(self.UserIdentityTokens)))
        for fieldname in self.UserIdentityTokens:
            packet.append(fieldname.to_binary())
        packet.append(pack_uatype('String', self.TransportProfileUri))
        packet.append(pack_uatype('Byte', self.SecurityLevel))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = EndpointDescription()
        obj.EndpointUrl = unpack_uatype('String', data)
        obj.Server = ApplicationDescription.from_binary(data)
        obj.ServerCertificate = unpack_uatype('ByteString', data)
        obj.SecurityMode = unpack_uatype('UInt32', data)
        obj.SecurityPolicyUri = unpack_uatype('String', data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.UserIdentityTokens.append(UserTokenPolicy.from_binary(data))
        obj.TransportProfileUri = unpack_uatype('String', data)
        obj.SecurityLevel = unpack_uatype('Byte', data)
        return obj

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
    def __init__(self):
        self.EndpointUrl = ''
        self.LocaleIds = []
        self.ProfileUris = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('String', self.EndpointUrl))
        packet.append(struct.pack('<i', len(self.LocaleIds)))
        for fieldname in self.LocaleIds:
            packet.append(pack_uatype('String', fieldname))
        packet.append(struct.pack('<i', len(self.ProfileUris)))
        for fieldname in self.ProfileUris:
            packet.append(pack_uatype('String', fieldname))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = GetEndpointsParameters()
        obj.EndpointUrl = unpack_uatype('String', data)
        obj.LocaleIds = unpack_uatype_array('String', data)
        obj.ProfileUris = unpack_uatype_array('String', data)
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.GetEndpointsRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = GetEndpointsParameters()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = GetEndpointsRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = GetEndpointsParameters.from_binary(data)
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.GetEndpointsResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Endpoints = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(struct.pack('<i', len(self.Endpoints)))
        for fieldname in self.Endpoints:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = GetEndpointsResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.Endpoints.append(EndpointDescription.from_binary(data))
        return obj

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
    def __init__(self):
        self.ServerUri = ''
        self.ProductUri = ''
        self.ServerNames = []
        self.ServerType = 0
        self.GatewayServerUri = ''
        self.DiscoveryUrls = []
        self.SemaphoreFilePath = ''
        self.IsOnline = True
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('String', self.ServerUri))
        packet.append(pack_uatype('String', self.ProductUri))
        packet.append(struct.pack('<i', len(self.ServerNames)))
        for fieldname in self.ServerNames:
            packet.append(fieldname.to_binary())
        packet.append(pack_uatype('UInt32', self.ServerType))
        packet.append(pack_uatype('String', self.GatewayServerUri))
        packet.append(struct.pack('<i', len(self.DiscoveryUrls)))
        for fieldname in self.DiscoveryUrls:
            packet.append(pack_uatype('String', fieldname))
        packet.append(pack_uatype('String', self.SemaphoreFilePath))
        packet.append(pack_uatype('Boolean', self.IsOnline))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = RegisteredServer()
        obj.ServerUri = unpack_uatype('String', data)
        obj.ProductUri = unpack_uatype('String', data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.ServerNames.append(LocalizedText.from_binary(data))
        obj.ServerType = unpack_uatype('UInt32', data)
        obj.GatewayServerUri = unpack_uatype('String', data)
        obj.DiscoveryUrls = unpack_uatype_array('String', data)
        obj.SemaphoreFilePath = unpack_uatype('String', data)
        obj.IsOnline = unpack_uatype('Boolean', data)
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.RegisterServerRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Server = RegisteredServer()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Server.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = RegisterServerRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Server = RegisteredServer.from_binary(data)
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.RegisterServerResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = RegisterServerResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        return obj

    def __str__(self):
        return 'RegisterServerResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'ResponseHeader:' + str(self.ResponseHeader) + ')'

    __repr__ = __str__


class DiscoveryConfiguration(FrozenClass):
    '''
    A base type for discovery configuration information.

    '''
    def __init__(self):
        self._freeze()

    def to_binary(self):
        packet = []
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = DiscoveryConfiguration()
        return obj

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
    def __init__(self):
        self.MdnsServerName = ''
        self.ServerCapabilities = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('String', self.MdnsServerName))
        packet.append(struct.pack('<i', len(self.ServerCapabilities)))
        for fieldname in self.ServerCapabilities:
            packet.append(pack_uatype('String', fieldname))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = MdnsDiscoveryConfiguration()
        obj.MdnsServerName = unpack_uatype('String', data)
        obj.ServerCapabilities = unpack_uatype_array('String', data)
        return obj

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
    def __init__(self):
        self.Server = RegisteredServer()
        self.DiscoveryConfiguration = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.Server.to_binary())
        packet.append(struct.pack('<i', len(self.DiscoveryConfiguration)))
        for fieldname in self.DiscoveryConfiguration:
            packet.append(extensionobject_to_binary(fieldname))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = RegisterServer2Parameters()
        obj.Server = RegisteredServer.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.DiscoveryConfiguration.append(extensionobject_from_binary(data))
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.RegisterServer2Request_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = RegisterServer2Parameters()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = RegisterServer2Request()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = RegisterServer2Parameters.from_binary(data)
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.RegisterServer2Response_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.ConfigurationResults = []
        self.DiagnosticInfos = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(struct.pack('<i', len(self.ConfigurationResults)))
        for fieldname in self.ConfigurationResults:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = RegisterServer2Response()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.ConfigurationResults.append(StatusCode.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.DiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        return obj

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
    def __init__(self):
        self.ChannelId = 0
        self.TokenId = 0
        self.CreatedAt = datetime.now()
        self.RevisedLifetime = 0
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('UInt32', self.ChannelId))
        packet.append(pack_uatype('UInt32', self.TokenId))
        packet.append(pack_uatype('DateTime', self.CreatedAt))
        packet.append(pack_uatype('UInt32', self.RevisedLifetime))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = ChannelSecurityToken()
        obj.ChannelId = unpack_uatype('UInt32', data)
        obj.TokenId = unpack_uatype('UInt32', data)
        obj.CreatedAt = unpack_uatype('DateTime', data)
        obj.RevisedLifetime = unpack_uatype('UInt32', data)
        return obj

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
    def __init__(self):
        self.ClientProtocolVersion = 0
        self.RequestType = 0
        self.SecurityMode = 0
        self.ClientNonce = b''
        self.RequestedLifetime = 0
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('UInt32', self.ClientProtocolVersion))
        packet.append(pack_uatype('UInt32', self.RequestType))
        packet.append(pack_uatype('UInt32', self.SecurityMode))
        packet.append(pack_uatype('ByteString', self.ClientNonce))
        packet.append(pack_uatype('UInt32', self.RequestedLifetime))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = OpenSecureChannelParameters()
        obj.ClientProtocolVersion = unpack_uatype('UInt32', data)
        obj.RequestType = unpack_uatype('UInt32', data)
        obj.SecurityMode = unpack_uatype('UInt32', data)
        obj.ClientNonce = unpack_uatype('ByteString', data)
        obj.RequestedLifetime = unpack_uatype('UInt32', data)
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.OpenSecureChannelRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = OpenSecureChannelParameters()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = OpenSecureChannelRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = OpenSecureChannelParameters.from_binary(data)
        return obj

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
    def __init__(self):
        self.ServerProtocolVersion = 0
        self.SecurityToken = ChannelSecurityToken()
        self.ServerNonce = b''
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('UInt32', self.ServerProtocolVersion))
        packet.append(self.SecurityToken.to_binary())
        packet.append(pack_uatype('ByteString', self.ServerNonce))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = OpenSecureChannelResult()
        obj.ServerProtocolVersion = unpack_uatype('UInt32', data)
        obj.SecurityToken = ChannelSecurityToken.from_binary(data)
        obj.ServerNonce = unpack_uatype('ByteString', data)
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.OpenSecureChannelResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = OpenSecureChannelResult()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = OpenSecureChannelResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = OpenSecureChannelResult.from_binary(data)
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.CloseSecureChannelRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = CloseSecureChannelRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.CloseSecureChannelResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = CloseSecureChannelResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        return obj

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
    def __init__(self):
        self.CertificateData = b''
        self.Signature = b''
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('ByteString', self.CertificateData))
        packet.append(pack_uatype('ByteString', self.Signature))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = SignedSoftwareCertificate()
        obj.CertificateData = unpack_uatype('ByteString', data)
        obj.Signature = unpack_uatype('ByteString', data)
        return obj

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
    def __init__(self):
        self.Algorithm = ''
        self.Signature = b''
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('String', self.Algorithm))
        packet.append(pack_uatype('ByteString', self.Signature))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = SignatureData()
        obj.Algorithm = unpack_uatype('String', data)
        obj.Signature = unpack_uatype('ByteString', data)
        return obj

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
    def __init__(self):
        self.ClientDescription = ApplicationDescription()
        self.ServerUri = ''
        self.EndpointUrl = ''
        self.SessionName = ''
        self.ClientNonce = b''
        self.ClientCertificate = b''
        self.RequestedSessionTimeout = 0
        self.MaxResponseMessageSize = 0
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.ClientDescription.to_binary())
        packet.append(pack_uatype('String', self.ServerUri))
        packet.append(pack_uatype('String', self.EndpointUrl))
        packet.append(pack_uatype('String', self.SessionName))
        packet.append(pack_uatype('ByteString', self.ClientNonce))
        packet.append(pack_uatype('ByteString', self.ClientCertificate))
        packet.append(pack_uatype('Double', self.RequestedSessionTimeout))
        packet.append(pack_uatype('UInt32', self.MaxResponseMessageSize))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = CreateSessionParameters()
        obj.ClientDescription = ApplicationDescription.from_binary(data)
        obj.ServerUri = unpack_uatype('String', data)
        obj.EndpointUrl = unpack_uatype('String', data)
        obj.SessionName = unpack_uatype('String', data)
        obj.ClientNonce = unpack_uatype('ByteString', data)
        obj.ClientCertificate = unpack_uatype('ByteString', data)
        obj.RequestedSessionTimeout = unpack_uatype('Double', data)
        obj.MaxResponseMessageSize = unpack_uatype('UInt32', data)
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.CreateSessionRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = CreateSessionParameters()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = CreateSessionRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = CreateSessionParameters.from_binary(data)
        return obj

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
    def __init__(self):
        self.SessionId = NodeId()
        self.AuthenticationToken = NodeId()
        self.RevisedSessionTimeout = 0
        self.ServerNonce = b''
        self.ServerCertificate = b''
        self.ServerEndpoints = []
        self.ServerSoftwareCertificates = []
        self.ServerSignature = SignatureData()
        self.MaxRequestMessageSize = 0
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.SessionId.to_binary())
        packet.append(self.AuthenticationToken.to_binary())
        packet.append(pack_uatype('Double', self.RevisedSessionTimeout))
        packet.append(pack_uatype('ByteString', self.ServerNonce))
        packet.append(pack_uatype('ByteString', self.ServerCertificate))
        packet.append(struct.pack('<i', len(self.ServerEndpoints)))
        for fieldname in self.ServerEndpoints:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.ServerSoftwareCertificates)))
        for fieldname in self.ServerSoftwareCertificates:
            packet.append(fieldname.to_binary())
        packet.append(self.ServerSignature.to_binary())
        packet.append(pack_uatype('UInt32', self.MaxRequestMessageSize))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = CreateSessionResult()
        obj.SessionId = NodeId.from_binary(data)
        obj.AuthenticationToken = NodeId.from_binary(data)
        obj.RevisedSessionTimeout = unpack_uatype('Double', data)
        obj.ServerNonce = unpack_uatype('ByteString', data)
        obj.ServerCertificate = unpack_uatype('ByteString', data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.ServerEndpoints.append(EndpointDescription.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.ServerSoftwareCertificates.append(SignedSoftwareCertificate.from_binary(data))
        obj.ServerSignature = SignatureData.from_binary(data)
        obj.MaxRequestMessageSize = unpack_uatype('UInt32', data)
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.CreateSessionResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = CreateSessionResult()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = CreateSessionResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = CreateSessionResult.from_binary(data)
        return obj

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
    def __init__(self):
        self.PolicyId = ''
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('String', self.PolicyId))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = UserIdentityToken()
        obj.PolicyId = unpack_uatype('String', data)
        return obj

    def __str__(self):
        return 'UserIdentityToken(' + 'PolicyId:' + str(self.PolicyId) + ')'

    __repr__ = __str__


class AnonymousIdentityToken(FrozenClass):
    '''
    A token representing an anonymous user.

    :ivar PolicyId:
    :vartype PolicyId: String
    '''
    def __init__(self):
        self.PolicyId = ''
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('String', self.PolicyId))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = AnonymousIdentityToken()
        obj.PolicyId = unpack_uatype('String', data)
        return obj

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
    def __init__(self):
        self.PolicyId = ''
        self.UserName = ''
        self.Password = b''
        self.EncryptionAlgorithm = ''
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('String', self.PolicyId))
        packet.append(pack_uatype('String', self.UserName))
        packet.append(pack_uatype('ByteString', self.Password))
        packet.append(pack_uatype('String', self.EncryptionAlgorithm))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = UserNameIdentityToken()
        obj.PolicyId = unpack_uatype('String', data)
        obj.UserName = unpack_uatype('String', data)
        obj.Password = unpack_uatype('ByteString', data)
        obj.EncryptionAlgorithm = unpack_uatype('String', data)
        return obj

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
    def __init__(self):
        self.PolicyId = ''
        self.CertificateData = b''
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('String', self.PolicyId))
        packet.append(pack_uatype('ByteString', self.CertificateData))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = X509IdentityToken()
        obj.PolicyId = unpack_uatype('String', data)
        obj.CertificateData = unpack_uatype('ByteString', data)
        return obj

    def __str__(self):
        return 'X509IdentityToken(' + 'PolicyId:' + str(self.PolicyId) + ', ' + \
               'CertificateData:' + str(self.CertificateData) + ')'

    __repr__ = __str__


class KerberosIdentityToken(FrozenClass):
    '''
    :ivar PolicyId:
    :vartype PolicyId: String
    :ivar TicketData:
    :vartype TicketData: ByteString
    '''
    def __init__(self):
        self.PolicyId = ''
        self.TicketData = b''
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('String', self.PolicyId))
        packet.append(pack_uatype('ByteString', self.TicketData))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = KerberosIdentityToken()
        obj.PolicyId = unpack_uatype('String', data)
        obj.TicketData = unpack_uatype('ByteString', data)
        return obj

    def __str__(self):
        return 'KerberosIdentityToken(' + 'PolicyId:' + str(self.PolicyId) + ', ' + \
               'TicketData:' + str(self.TicketData) + ')'

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
    def __init__(self):
        self.PolicyId = ''
        self.TokenData = b''
        self.EncryptionAlgorithm = ''
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('String', self.PolicyId))
        packet.append(pack_uatype('ByteString', self.TokenData))
        packet.append(pack_uatype('String', self.EncryptionAlgorithm))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = IssuedIdentityToken()
        obj.PolicyId = unpack_uatype('String', data)
        obj.TokenData = unpack_uatype('ByteString', data)
        obj.EncryptionAlgorithm = unpack_uatype('String', data)
        return obj

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
    def __init__(self):
        self.ClientSignature = SignatureData()
        self.ClientSoftwareCertificates = []
        self.LocaleIds = []
        self.UserIdentityToken = None
        self.UserTokenSignature = SignatureData()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.ClientSignature.to_binary())
        packet.append(struct.pack('<i', len(self.ClientSoftwareCertificates)))
        for fieldname in self.ClientSoftwareCertificates:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.LocaleIds)))
        for fieldname in self.LocaleIds:
            packet.append(pack_uatype('String', fieldname))
        packet.append(extensionobject_to_binary(self.UserIdentityToken))
        packet.append(self.UserTokenSignature.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = ActivateSessionParameters()
        obj.ClientSignature = SignatureData.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.ClientSoftwareCertificates.append(SignedSoftwareCertificate.from_binary(data))
        obj.LocaleIds = unpack_uatype_array('String', data)
        obj.UserIdentityToken = extensionobject_from_binary(data)
        obj.UserTokenSignature = SignatureData.from_binary(data)
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.ActivateSessionRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = ActivateSessionParameters()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = ActivateSessionRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = ActivateSessionParameters.from_binary(data)
        return obj

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
    def __init__(self):
        self.ServerNonce = b''
        self.Results = []
        self.DiagnosticInfos = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('ByteString', self.ServerNonce))
        packet.append(struct.pack('<i', len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = ActivateSessionResult()
        obj.ServerNonce = unpack_uatype('ByteString', data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.Results.append(StatusCode.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.DiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.ActivateSessionResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = ActivateSessionResult()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = ActivateSessionResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = ActivateSessionResult.from_binary(data)
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.CloseSessionRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.DeleteSubscriptions = True
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(pack_uatype('Boolean', self.DeleteSubscriptions))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = CloseSessionRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.DeleteSubscriptions = unpack_uatype('Boolean', data)
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.CloseSessionResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = CloseSessionResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        return obj

    def __str__(self):
        return 'CloseSessionResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'ResponseHeader:' + str(self.ResponseHeader) + ')'

    __repr__ = __str__


class CancelParameters(FrozenClass):
    '''
    :ivar RequestHandle:
    :vartype RequestHandle: UInt32
    '''
    def __init__(self):
        self.RequestHandle = 0
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('UInt32', self.RequestHandle))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = CancelParameters()
        obj.RequestHandle = unpack_uatype('UInt32', data)
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.CancelRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = CancelParameters()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = CancelRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = CancelParameters.from_binary(data)
        return obj

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
    def __init__(self):
        self.CancelCount = 0
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('UInt32', self.CancelCount))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = CancelResult()
        obj.CancelCount = unpack_uatype('UInt32', data)
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.CancelResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = CancelResult()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = CancelResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = CancelResult.from_binary(data)
        return obj

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
    def __init__(self):
        self.SpecifiedAttributes = 0
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self.UserWriteMask = 0
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('UInt32', self.SpecifiedAttributes))
        packet.append(self.DisplayName.to_binary())
        packet.append(self.Description.to_binary())
        packet.append(pack_uatype('UInt32', self.WriteMask))
        packet.append(pack_uatype('UInt32', self.UserWriteMask))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = NodeAttributes()
        obj.SpecifiedAttributes = unpack_uatype('UInt32', data)
        obj.DisplayName = LocalizedText.from_binary(data)
        obj.Description = LocalizedText.from_binary(data)
        obj.WriteMask = unpack_uatype('UInt32', data)
        obj.UserWriteMask = unpack_uatype('UInt32', data)
        return obj

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
    def __init__(self):
        self.SpecifiedAttributes = 0
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self.UserWriteMask = 0
        self.EventNotifier = 0
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('UInt32', self.SpecifiedAttributes))
        packet.append(self.DisplayName.to_binary())
        packet.append(self.Description.to_binary())
        packet.append(pack_uatype('UInt32', self.WriteMask))
        packet.append(pack_uatype('UInt32', self.UserWriteMask))
        packet.append(pack_uatype('Byte', self.EventNotifier))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = ObjectAttributes()
        obj.SpecifiedAttributes = unpack_uatype('UInt32', data)
        obj.DisplayName = LocalizedText.from_binary(data)
        obj.Description = LocalizedText.from_binary(data)
        obj.WriteMask = unpack_uatype('UInt32', data)
        obj.UserWriteMask = unpack_uatype('UInt32', data)
        obj.EventNotifier = unpack_uatype('Byte', data)
        return obj

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
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('UInt32', self.SpecifiedAttributes))
        packet.append(self.DisplayName.to_binary())
        packet.append(self.Description.to_binary())
        packet.append(pack_uatype('UInt32', self.WriteMask))
        packet.append(pack_uatype('UInt32', self.UserWriteMask))
        packet.append(self.Value.to_binary())
        packet.append(self.DataType.to_binary())
        packet.append(pack_uatype('Int32', self.ValueRank))
        packet.append(struct.pack('<i', len(self.ArrayDimensions)))
        for fieldname in self.ArrayDimensions:
            packet.append(pack_uatype('UInt32', fieldname))
        packet.append(pack_uatype('Byte', self.AccessLevel))
        packet.append(pack_uatype('Byte', self.UserAccessLevel))
        packet.append(pack_uatype('Double', self.MinimumSamplingInterval))
        packet.append(pack_uatype('Boolean', self.Historizing))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = VariableAttributes()
        obj.SpecifiedAttributes = unpack_uatype('UInt32', data)
        obj.DisplayName = LocalizedText.from_binary(data)
        obj.Description = LocalizedText.from_binary(data)
        obj.WriteMask = unpack_uatype('UInt32', data)
        obj.UserWriteMask = unpack_uatype('UInt32', data)
        obj.Value = Variant.from_binary(data)
        obj.DataType = NodeId.from_binary(data)
        obj.ValueRank = unpack_uatype('Int32', data)
        obj.ArrayDimensions = unpack_uatype_array('UInt32', data)
        obj.AccessLevel = unpack_uatype('Byte', data)
        obj.UserAccessLevel = unpack_uatype('Byte', data)
        obj.MinimumSamplingInterval = unpack_uatype('Double', data)
        obj.Historizing = unpack_uatype('Boolean', data)
        return obj

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
    def __init__(self):
        self.SpecifiedAttributes = 0
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self.UserWriteMask = 0
        self.Executable = True
        self.UserExecutable = True
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('UInt32', self.SpecifiedAttributes))
        packet.append(self.DisplayName.to_binary())
        packet.append(self.Description.to_binary())
        packet.append(pack_uatype('UInt32', self.WriteMask))
        packet.append(pack_uatype('UInt32', self.UserWriteMask))
        packet.append(pack_uatype('Boolean', self.Executable))
        packet.append(pack_uatype('Boolean', self.UserExecutable))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = MethodAttributes()
        obj.SpecifiedAttributes = unpack_uatype('UInt32', data)
        obj.DisplayName = LocalizedText.from_binary(data)
        obj.Description = LocalizedText.from_binary(data)
        obj.WriteMask = unpack_uatype('UInt32', data)
        obj.UserWriteMask = unpack_uatype('UInt32', data)
        obj.Executable = unpack_uatype('Boolean', data)
        obj.UserExecutable = unpack_uatype('Boolean', data)
        return obj

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
    def __init__(self):
        self.SpecifiedAttributes = 0
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self.UserWriteMask = 0
        self.IsAbstract = True
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('UInt32', self.SpecifiedAttributes))
        packet.append(self.DisplayName.to_binary())
        packet.append(self.Description.to_binary())
        packet.append(pack_uatype('UInt32', self.WriteMask))
        packet.append(pack_uatype('UInt32', self.UserWriteMask))
        packet.append(pack_uatype('Boolean', self.IsAbstract))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = ObjectTypeAttributes()
        obj.SpecifiedAttributes = unpack_uatype('UInt32', data)
        obj.DisplayName = LocalizedText.from_binary(data)
        obj.Description = LocalizedText.from_binary(data)
        obj.WriteMask = unpack_uatype('UInt32', data)
        obj.UserWriteMask = unpack_uatype('UInt32', data)
        obj.IsAbstract = unpack_uatype('Boolean', data)
        return obj

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
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('UInt32', self.SpecifiedAttributes))
        packet.append(self.DisplayName.to_binary())
        packet.append(self.Description.to_binary())
        packet.append(pack_uatype('UInt32', self.WriteMask))
        packet.append(pack_uatype('UInt32', self.UserWriteMask))
        packet.append(self.Value.to_binary())
        packet.append(self.DataType.to_binary())
        packet.append(pack_uatype('Int32', self.ValueRank))
        packet.append(struct.pack('<i', len(self.ArrayDimensions)))
        for fieldname in self.ArrayDimensions:
            packet.append(pack_uatype('UInt32', fieldname))
        packet.append(pack_uatype('Boolean', self.IsAbstract))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = VariableTypeAttributes()
        obj.SpecifiedAttributes = unpack_uatype('UInt32', data)
        obj.DisplayName = LocalizedText.from_binary(data)
        obj.Description = LocalizedText.from_binary(data)
        obj.WriteMask = unpack_uatype('UInt32', data)
        obj.UserWriteMask = unpack_uatype('UInt32', data)
        obj.Value = Variant.from_binary(data)
        obj.DataType = NodeId.from_binary(data)
        obj.ValueRank = unpack_uatype('Int32', data)
        obj.ArrayDimensions = unpack_uatype_array('UInt32', data)
        obj.IsAbstract = unpack_uatype('Boolean', data)
        return obj

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
    def __init__(self):
        self.SpecifiedAttributes = 0
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self.UserWriteMask = 0
        self.IsAbstract = True
        self.Symmetric = True
        self.InverseName = LocalizedText()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('UInt32', self.SpecifiedAttributes))
        packet.append(self.DisplayName.to_binary())
        packet.append(self.Description.to_binary())
        packet.append(pack_uatype('UInt32', self.WriteMask))
        packet.append(pack_uatype('UInt32', self.UserWriteMask))
        packet.append(pack_uatype('Boolean', self.IsAbstract))
        packet.append(pack_uatype('Boolean', self.Symmetric))
        packet.append(self.InverseName.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = ReferenceTypeAttributes()
        obj.SpecifiedAttributes = unpack_uatype('UInt32', data)
        obj.DisplayName = LocalizedText.from_binary(data)
        obj.Description = LocalizedText.from_binary(data)
        obj.WriteMask = unpack_uatype('UInt32', data)
        obj.UserWriteMask = unpack_uatype('UInt32', data)
        obj.IsAbstract = unpack_uatype('Boolean', data)
        obj.Symmetric = unpack_uatype('Boolean', data)
        obj.InverseName = LocalizedText.from_binary(data)
        return obj

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
    def __init__(self):
        self.SpecifiedAttributes = 0
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self.UserWriteMask = 0
        self.IsAbstract = True
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('UInt32', self.SpecifiedAttributes))
        packet.append(self.DisplayName.to_binary())
        packet.append(self.Description.to_binary())
        packet.append(pack_uatype('UInt32', self.WriteMask))
        packet.append(pack_uatype('UInt32', self.UserWriteMask))
        packet.append(pack_uatype('Boolean', self.IsAbstract))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = DataTypeAttributes()
        obj.SpecifiedAttributes = unpack_uatype('UInt32', data)
        obj.DisplayName = LocalizedText.from_binary(data)
        obj.Description = LocalizedText.from_binary(data)
        obj.WriteMask = unpack_uatype('UInt32', data)
        obj.UserWriteMask = unpack_uatype('UInt32', data)
        obj.IsAbstract = unpack_uatype('Boolean', data)
        return obj

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
    def __init__(self):
        self.SpecifiedAttributes = 0
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self.UserWriteMask = 0
        self.ContainsNoLoops = True
        self.EventNotifier = 0
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('UInt32', self.SpecifiedAttributes))
        packet.append(self.DisplayName.to_binary())
        packet.append(self.Description.to_binary())
        packet.append(pack_uatype('UInt32', self.WriteMask))
        packet.append(pack_uatype('UInt32', self.UserWriteMask))
        packet.append(pack_uatype('Boolean', self.ContainsNoLoops))
        packet.append(pack_uatype('Byte', self.EventNotifier))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = ViewAttributes()
        obj.SpecifiedAttributes = unpack_uatype('UInt32', data)
        obj.DisplayName = LocalizedText.from_binary(data)
        obj.Description = LocalizedText.from_binary(data)
        obj.WriteMask = unpack_uatype('UInt32', data)
        obj.UserWriteMask = unpack_uatype('UInt32', data)
        obj.ContainsNoLoops = unpack_uatype('Boolean', data)
        obj.EventNotifier = unpack_uatype('Byte', data)
        return obj

    def __str__(self):
        return 'ViewAttributes(' + 'SpecifiedAttributes:' + str(self.SpecifiedAttributes) + ', ' + \
               'DisplayName:' + str(self.DisplayName) + ', ' + \
               'Description:' + str(self.Description) + ', ' + \
               'WriteMask:' + str(self.WriteMask) + ', ' + \
               'UserWriteMask:' + str(self.UserWriteMask) + ', ' + \
               'ContainsNoLoops:' + str(self.ContainsNoLoops) + ', ' + \
               'EventNotifier:' + str(self.EventNotifier) + ')'

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
    def __init__(self):
        self.ParentNodeId = ExpandedNodeId()
        self.ReferenceTypeId = NodeId()
        self.RequestedNewNodeId = ExpandedNodeId()
        self.BrowseName = QualifiedName()
        self.NodeClass = 0
        self.NodeAttributes = None
        self.TypeDefinition = ExpandedNodeId()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.ParentNodeId.to_binary())
        packet.append(self.ReferenceTypeId.to_binary())
        packet.append(self.RequestedNewNodeId.to_binary())
        packet.append(self.BrowseName.to_binary())
        packet.append(pack_uatype('UInt32', self.NodeClass))
        packet.append(extensionobject_to_binary(self.NodeAttributes))
        packet.append(self.TypeDefinition.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = AddNodesItem()
        obj.ParentNodeId = ExpandedNodeId.from_binary(data)
        obj.ReferenceTypeId = NodeId.from_binary(data)
        obj.RequestedNewNodeId = ExpandedNodeId.from_binary(data)
        obj.BrowseName = QualifiedName.from_binary(data)
        obj.NodeClass = unpack_uatype('UInt32', data)
        obj.NodeAttributes = extensionobject_from_binary(data)
        obj.TypeDefinition = ExpandedNodeId.from_binary(data)
        return obj

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
    def __init__(self):
        self.StatusCode = StatusCode()
        self.AddedNodeId = NodeId()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.StatusCode.to_binary())
        packet.append(self.AddedNodeId.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = AddNodesResult()
        obj.StatusCode = StatusCode.from_binary(data)
        obj.AddedNodeId = NodeId.from_binary(data)
        return obj

    def __str__(self):
        return 'AddNodesResult(' + 'StatusCode:' + str(self.StatusCode) + ', ' + \
               'AddedNodeId:' + str(self.AddedNodeId) + ')'

    __repr__ = __str__


class AddNodesParameters(FrozenClass):
    '''
    :ivar NodesToAdd:
    :vartype NodesToAdd: AddNodesItem
    '''
    def __init__(self):
        self.NodesToAdd = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.NodesToAdd)))
        for fieldname in self.NodesToAdd:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = AddNodesParameters()
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.NodesToAdd.append(AddNodesItem.from_binary(data))
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.AddNodesRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = AddNodesParameters()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = AddNodesRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = AddNodesParameters.from_binary(data)
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.AddNodesResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Results = []
        self.DiagnosticInfos = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(struct.pack('<i', len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = AddNodesResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.Results.append(AddNodesResult.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.DiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        return obj

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
    def __init__(self):
        self.SourceNodeId = NodeId()
        self.ReferenceTypeId = NodeId()
        self.IsForward = True
        self.TargetServerUri = ''
        self.TargetNodeId = ExpandedNodeId()
        self.TargetNodeClass = 0
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.SourceNodeId.to_binary())
        packet.append(self.ReferenceTypeId.to_binary())
        packet.append(pack_uatype('Boolean', self.IsForward))
        packet.append(pack_uatype('String', self.TargetServerUri))
        packet.append(self.TargetNodeId.to_binary())
        packet.append(pack_uatype('UInt32', self.TargetNodeClass))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = AddReferencesItem()
        obj.SourceNodeId = NodeId.from_binary(data)
        obj.ReferenceTypeId = NodeId.from_binary(data)
        obj.IsForward = unpack_uatype('Boolean', data)
        obj.TargetServerUri = unpack_uatype('String', data)
        obj.TargetNodeId = ExpandedNodeId.from_binary(data)
        obj.TargetNodeClass = unpack_uatype('UInt32', data)
        return obj

    def __str__(self):
        return 'AddReferencesItem(' + 'SourceNodeId:' + str(self.SourceNodeId) + ', ' + \
               'ReferenceTypeId:' + str(self.ReferenceTypeId) + ', ' + \
               'IsForward:' + str(self.IsForward) + ', ' + \
               'TargetServerUri:' + str(self.TargetServerUri) + ', ' + \
               'TargetNodeId:' + str(self.TargetNodeId) + ', ' + \
               'TargetNodeClass:' + str(self.TargetNodeClass) + ')'

    __repr__ = __str__


class AddReferencesRequest(FrozenClass):
    '''
    Adds one or more references to the server address space.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar ReferencesToAdd:
    :vartype ReferencesToAdd: AddReferencesItem
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.AddReferencesRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.ReferencesToAdd = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(struct.pack('<i', len(self.ReferencesToAdd)))
        for fieldname in self.ReferencesToAdd:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = AddReferencesRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.ReferencesToAdd.append(AddReferencesItem.from_binary(data))
        return obj

    def __str__(self):
        return 'AddReferencesRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'RequestHeader:' + str(self.RequestHeader) + ', ' + \
               'ReferencesToAdd:' + str(self.ReferencesToAdd) + ')'

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.AddReferencesResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Results = []
        self.DiagnosticInfos = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(struct.pack('<i', len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = AddReferencesResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.Results.append(StatusCode.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.DiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        return obj

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
    def __init__(self):
        self.NodeId = NodeId()
        self.DeleteTargetReferences = True
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.NodeId.to_binary())
        packet.append(pack_uatype('Boolean', self.DeleteTargetReferences))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = DeleteNodesItem()
        obj.NodeId = NodeId.from_binary(data)
        obj.DeleteTargetReferences = unpack_uatype('Boolean', data)
        return obj

    def __str__(self):
        return 'DeleteNodesItem(' + 'NodeId:' + str(self.NodeId) + ', ' + \
               'DeleteTargetReferences:' + str(self.DeleteTargetReferences) + ')'

    __repr__ = __str__


class DeleteNodesParameters(FrozenClass):
    '''
    :ivar NodesToDelete:
    :vartype NodesToDelete: DeleteNodesItem
    '''
    def __init__(self):
        self.NodesToDelete = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.NodesToDelete)))
        for fieldname in self.NodesToDelete:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = DeleteNodesParameters()
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.NodesToDelete.append(DeleteNodesItem.from_binary(data))
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.DeleteNodesRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = DeleteNodesParameters()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = DeleteNodesRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = DeleteNodesParameters.from_binary(data)
        return obj

    def __str__(self):
        return 'DeleteNodesRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'RequestHeader:' + str(self.RequestHeader) + ', ' + \
               'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class DeleteNodesResult(FrozenClass):
    '''
    :ivar Results:
    :vartype Results: StatusCode
    :ivar DiagnosticInfos:
    :vartype DiagnosticInfos: DiagnosticInfo
    '''
    def __init__(self):
        self.Results = []
        self.DiagnosticInfos = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = DeleteNodesResult()
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.Results.append(StatusCode.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.DiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        return obj

    def __str__(self):
        return 'DeleteNodesResult(' + 'Results:' + str(self.Results) + ', ' + \
               'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'

    __repr__ = __str__


class DeleteNodesResponse(FrozenClass):
    '''
    Delete one or more nodes from the server address space.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    :ivar Parameters:
    :vartype Parameters: DeleteNodesResult
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.DeleteNodesResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = DeleteNodesResult()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = DeleteNodesResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = DeleteNodesResult.from_binary(data)
        return obj

    def __str__(self):
        return 'DeleteNodesResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
               'Parameters:' + str(self.Parameters) + ')'

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
    def __init__(self):
        self.SourceNodeId = NodeId()
        self.ReferenceTypeId = NodeId()
        self.IsForward = True
        self.TargetNodeId = ExpandedNodeId()
        self.DeleteBidirectional = True
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.SourceNodeId.to_binary())
        packet.append(self.ReferenceTypeId.to_binary())
        packet.append(pack_uatype('Boolean', self.IsForward))
        packet.append(self.TargetNodeId.to_binary())
        packet.append(pack_uatype('Boolean', self.DeleteBidirectional))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = DeleteReferencesItem()
        obj.SourceNodeId = NodeId.from_binary(data)
        obj.ReferenceTypeId = NodeId.from_binary(data)
        obj.IsForward = unpack_uatype('Boolean', data)
        obj.TargetNodeId = ExpandedNodeId.from_binary(data)
        obj.DeleteBidirectional = unpack_uatype('Boolean', data)
        return obj

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
    def __init__(self):
        self.ReferencesToDelete = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.ReferencesToDelete)))
        for fieldname in self.ReferencesToDelete:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = DeleteReferencesParameters()
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.ReferencesToDelete.append(DeleteReferencesItem.from_binary(data))
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.DeleteReferencesRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = DeleteReferencesParameters()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = DeleteReferencesRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = DeleteReferencesParameters.from_binary(data)
        return obj

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
    def __init__(self):
        self.Results = []
        self.DiagnosticInfos = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = DeleteReferencesResult()
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.Results.append(StatusCode.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.DiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.DeleteReferencesResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = DeleteReferencesResult()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = DeleteReferencesResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = DeleteReferencesResult.from_binary(data)
        return obj

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
    def __init__(self):
        self.ViewId = NodeId()
        self.Timestamp = datetime.now()
        self.ViewVersion = 0
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.ViewId.to_binary())
        packet.append(pack_uatype('DateTime', self.Timestamp))
        packet.append(pack_uatype('UInt32', self.ViewVersion))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = ViewDescription()
        obj.ViewId = NodeId.from_binary(data)
        obj.Timestamp = unpack_uatype('DateTime', data)
        obj.ViewVersion = unpack_uatype('UInt32', data)
        return obj

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
    def __init__(self):
        self.NodeId = NodeId()
        self.BrowseDirection = 0
        self.ReferenceTypeId = NodeId()
        self.IncludeSubtypes = True
        self.NodeClassMask = 0
        self.ResultMask = 0
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.NodeId.to_binary())
        packet.append(pack_uatype('UInt32', self.BrowseDirection))
        packet.append(self.ReferenceTypeId.to_binary())
        packet.append(pack_uatype('Boolean', self.IncludeSubtypes))
        packet.append(pack_uatype('UInt32', self.NodeClassMask))
        packet.append(pack_uatype('UInt32', self.ResultMask))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = BrowseDescription()
        obj.NodeId = NodeId.from_binary(data)
        obj.BrowseDirection = unpack_uatype('UInt32', data)
        obj.ReferenceTypeId = NodeId.from_binary(data)
        obj.IncludeSubtypes = unpack_uatype('Boolean', data)
        obj.NodeClassMask = unpack_uatype('UInt32', data)
        obj.ResultMask = unpack_uatype('UInt32', data)
        return obj

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
    def __init__(self):
        self.ReferenceTypeId = NodeId()
        self.IsForward = True
        self.NodeId = ExpandedNodeId()
        self.BrowseName = QualifiedName()
        self.DisplayName = LocalizedText()
        self.NodeClass = 0
        self.TypeDefinition = ExpandedNodeId()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.ReferenceTypeId.to_binary())
        packet.append(pack_uatype('Boolean', self.IsForward))
        packet.append(self.NodeId.to_binary())
        packet.append(self.BrowseName.to_binary())
        packet.append(self.DisplayName.to_binary())
        packet.append(pack_uatype('UInt32', self.NodeClass))
        packet.append(self.TypeDefinition.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = ReferenceDescription()
        obj.ReferenceTypeId = NodeId.from_binary(data)
        obj.IsForward = unpack_uatype('Boolean', data)
        obj.NodeId = ExpandedNodeId.from_binary(data)
        obj.BrowseName = QualifiedName.from_binary(data)
        obj.DisplayName = LocalizedText.from_binary(data)
        obj.NodeClass = unpack_uatype('UInt32', data)
        obj.TypeDefinition = ExpandedNodeId.from_binary(data)
        return obj

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
    def __init__(self):
        self.StatusCode = StatusCode()
        self.ContinuationPoint = b''
        self.References = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.StatusCode.to_binary())
        packet.append(pack_uatype('ByteString', self.ContinuationPoint))
        packet.append(struct.pack('<i', len(self.References)))
        for fieldname in self.References:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = BrowseResult()
        obj.StatusCode = StatusCode.from_binary(data)
        obj.ContinuationPoint = unpack_uatype('ByteString', data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.References.append(ReferenceDescription.from_binary(data))
        return obj

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
    def __init__(self):
        self.View = ViewDescription()
        self.RequestedMaxReferencesPerNode = 0
        self.NodesToBrowse = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.View.to_binary())
        packet.append(pack_uatype('UInt32', self.RequestedMaxReferencesPerNode))
        packet.append(struct.pack('<i', len(self.NodesToBrowse)))
        for fieldname in self.NodesToBrowse:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = BrowseParameters()
        obj.View = ViewDescription.from_binary(data)
        obj.RequestedMaxReferencesPerNode = unpack_uatype('UInt32', data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.NodesToBrowse.append(BrowseDescription.from_binary(data))
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.BrowseRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = BrowseParameters()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = BrowseRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = BrowseParameters.from_binary(data)
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.BrowseResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Results = []
        self.DiagnosticInfos = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(struct.pack('<i', len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = BrowseResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.Results.append(BrowseResult.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.DiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        return obj

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
    def __init__(self):
        self.ReleaseContinuationPoints = True
        self.ContinuationPoints = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('Boolean', self.ReleaseContinuationPoints))
        packet.append(struct.pack('<i', len(self.ContinuationPoints)))
        for fieldname in self.ContinuationPoints:
            packet.append(pack_uatype('ByteString', fieldname))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = BrowseNextParameters()
        obj.ReleaseContinuationPoints = unpack_uatype('Boolean', data)
        obj.ContinuationPoints = unpack_uatype_array('ByteString', data)
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.BrowseNextRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = BrowseNextParameters()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = BrowseNextRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = BrowseNextParameters.from_binary(data)
        return obj

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
    def __init__(self):
        self.Results = []
        self.DiagnosticInfos = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = BrowseNextResult()
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.Results.append(BrowseResult.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.DiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.BrowseNextResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = BrowseNextResult()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = BrowseNextResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = BrowseNextResult.from_binary(data)
        return obj

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
    def __init__(self):
        self.ReferenceTypeId = NodeId()
        self.IsInverse = True
        self.IncludeSubtypes = True
        self.TargetName = QualifiedName()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.ReferenceTypeId.to_binary())
        packet.append(pack_uatype('Boolean', self.IsInverse))
        packet.append(pack_uatype('Boolean', self.IncludeSubtypes))
        packet.append(self.TargetName.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = RelativePathElement()
        obj.ReferenceTypeId = NodeId.from_binary(data)
        obj.IsInverse = unpack_uatype('Boolean', data)
        obj.IncludeSubtypes = unpack_uatype('Boolean', data)
        obj.TargetName = QualifiedName.from_binary(data)
        return obj

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
    def __init__(self):
        self.Elements = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.Elements)))
        for fieldname in self.Elements:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = RelativePath()
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.Elements.append(RelativePathElement.from_binary(data))
        return obj

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
    def __init__(self):
        self.StartingNode = NodeId()
        self.RelativePath = RelativePath()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.StartingNode.to_binary())
        packet.append(self.RelativePath.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = BrowsePath()
        obj.StartingNode = NodeId.from_binary(data)
        obj.RelativePath = RelativePath.from_binary(data)
        return obj

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
    def __init__(self):
        self.TargetId = ExpandedNodeId()
        self.RemainingPathIndex = 0
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TargetId.to_binary())
        packet.append(pack_uatype('UInt32', self.RemainingPathIndex))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = BrowsePathTarget()
        obj.TargetId = ExpandedNodeId.from_binary(data)
        obj.RemainingPathIndex = unpack_uatype('UInt32', data)
        return obj

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
    def __init__(self):
        self.StatusCode = StatusCode()
        self.Targets = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.StatusCode.to_binary())
        packet.append(struct.pack('<i', len(self.Targets)))
        for fieldname in self.Targets:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = BrowsePathResult()
        obj.StatusCode = StatusCode.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.Targets.append(BrowsePathTarget.from_binary(data))
        return obj

    def __str__(self):
        return 'BrowsePathResult(' + 'StatusCode:' + str(self.StatusCode) + ', ' + \
               'Targets:' + str(self.Targets) + ')'

    __repr__ = __str__


class TranslateBrowsePathsToNodeIdsParameters(FrozenClass):
    '''
    :ivar BrowsePaths:
    :vartype BrowsePaths: BrowsePath
    '''
    def __init__(self):
        self.BrowsePaths = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.BrowsePaths)))
        for fieldname in self.BrowsePaths:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = TranslateBrowsePathsToNodeIdsParameters()
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.BrowsePaths.append(BrowsePath.from_binary(data))
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.TranslateBrowsePathsToNodeIdsRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = TranslateBrowsePathsToNodeIdsParameters()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = TranslateBrowsePathsToNodeIdsRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = TranslateBrowsePathsToNodeIdsParameters.from_binary(data)
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.TranslateBrowsePathsToNodeIdsResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Results = []
        self.DiagnosticInfos = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(struct.pack('<i', len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = TranslateBrowsePathsToNodeIdsResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.Results.append(BrowsePathResult.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.DiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        return obj

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
    def __init__(self):
        self.NodesToRegister = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.NodesToRegister)))
        for fieldname in self.NodesToRegister:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = RegisterNodesParameters()
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.NodesToRegister.append(NodeId.from_binary(data))
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.RegisterNodesRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = RegisterNodesParameters()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = RegisterNodesRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = RegisterNodesParameters.from_binary(data)
        return obj

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
    def __init__(self):
        self.RegisteredNodeIds = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.RegisteredNodeIds)))
        for fieldname in self.RegisteredNodeIds:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = RegisterNodesResult()
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.RegisteredNodeIds.append(NodeId.from_binary(data))
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.RegisterNodesResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = RegisterNodesResult()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = RegisterNodesResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = RegisterNodesResult.from_binary(data)
        return obj

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
    def __init__(self):
        self.NodesToUnregister = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.NodesToUnregister)))
        for fieldname in self.NodesToUnregister:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = UnregisterNodesParameters()
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.NodesToUnregister.append(NodeId.from_binary(data))
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.UnregisterNodesRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = UnregisterNodesParameters()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = UnregisterNodesRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = UnregisterNodesParameters.from_binary(data)
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.UnregisterNodesResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = UnregisterNodesResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        return obj

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
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('Int32', self.OperationTimeout))
        packet.append(pack_uatype('Boolean', self.UseBinaryEncoding))
        packet.append(pack_uatype('Int32', self.MaxStringLength))
        packet.append(pack_uatype('Int32', self.MaxByteStringLength))
        packet.append(pack_uatype('Int32', self.MaxArrayLength))
        packet.append(pack_uatype('Int32', self.MaxMessageSize))
        packet.append(pack_uatype('Int32', self.MaxBufferSize))
        packet.append(pack_uatype('Int32', self.ChannelLifetime))
        packet.append(pack_uatype('Int32', self.SecurityTokenLifetime))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = EndpointConfiguration()
        obj.OperationTimeout = unpack_uatype('Int32', data)
        obj.UseBinaryEncoding = unpack_uatype('Boolean', data)
        obj.MaxStringLength = unpack_uatype('Int32', data)
        obj.MaxByteStringLength = unpack_uatype('Int32', data)
        obj.MaxArrayLength = unpack_uatype('Int32', data)
        obj.MaxMessageSize = unpack_uatype('Int32', data)
        obj.MaxBufferSize = unpack_uatype('Int32', data)
        obj.ChannelLifetime = unpack_uatype('Int32', data)
        obj.SecurityTokenLifetime = unpack_uatype('Int32', data)
        return obj

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


class SupportedProfile(FrozenClass):
    '''
    :ivar OrganizationUri:
    :vartype OrganizationUri: String
    :ivar ProfileId:
    :vartype ProfileId: String
    :ivar ComplianceTool:
    :vartype ComplianceTool: String
    :ivar ComplianceDate:
    :vartype ComplianceDate: DateTime
    :ivar ComplianceLevel:
    :vartype ComplianceLevel: ComplianceLevel
    :ivar UnsupportedUnitIds:
    :vartype UnsupportedUnitIds: String
    '''
    def __init__(self):
        self.OrganizationUri = ''
        self.ProfileId = ''
        self.ComplianceTool = ''
        self.ComplianceDate = datetime.now()
        self.ComplianceLevel = 0
        self.UnsupportedUnitIds = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('String', self.OrganizationUri))
        packet.append(pack_uatype('String', self.ProfileId))
        packet.append(pack_uatype('String', self.ComplianceTool))
        packet.append(pack_uatype('DateTime', self.ComplianceDate))
        packet.append(pack_uatype('UInt32', self.ComplianceLevel))
        packet.append(struct.pack('<i', len(self.UnsupportedUnitIds)))
        for fieldname in self.UnsupportedUnitIds:
            packet.append(pack_uatype('String', fieldname))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = SupportedProfile()
        obj.OrganizationUri = unpack_uatype('String', data)
        obj.ProfileId = unpack_uatype('String', data)
        obj.ComplianceTool = unpack_uatype('String', data)
        obj.ComplianceDate = unpack_uatype('DateTime', data)
        obj.ComplianceLevel = unpack_uatype('UInt32', data)
        obj.UnsupportedUnitIds = unpack_uatype_array('String', data)
        return obj

    def __str__(self):
        return 'SupportedProfile(' + 'OrganizationUri:' + str(self.OrganizationUri) + ', ' + \
               'ProfileId:' + str(self.ProfileId) + ', ' + \
               'ComplianceTool:' + str(self.ComplianceTool) + ', ' + \
               'ComplianceDate:' + str(self.ComplianceDate) + ', ' + \
               'ComplianceLevel:' + str(self.ComplianceLevel) + ', ' + \
               'UnsupportedUnitIds:' + str(self.UnsupportedUnitIds) + ')'

    __repr__ = __str__


class SoftwareCertificate(FrozenClass):
    '''
    :ivar ProductName:
    :vartype ProductName: String
    :ivar ProductUri:
    :vartype ProductUri: String
    :ivar VendorName:
    :vartype VendorName: String
    :ivar VendorProductCertificate:
    :vartype VendorProductCertificate: ByteString
    :ivar SoftwareVersion:
    :vartype SoftwareVersion: String
    :ivar BuildNumber:
    :vartype BuildNumber: String
    :ivar BuildDate:
    :vartype BuildDate: DateTime
    :ivar IssuedBy:
    :vartype IssuedBy: String
    :ivar IssueDate:
    :vartype IssueDate: DateTime
    :ivar SupportedProfiles:
    :vartype SupportedProfiles: SupportedProfile
    '''
    def __init__(self):
        self.ProductName = ''
        self.ProductUri = ''
        self.VendorName = ''
        self.VendorProductCertificate = b''
        self.SoftwareVersion = ''
        self.BuildNumber = ''
        self.BuildDate = datetime.now()
        self.IssuedBy = ''
        self.IssueDate = datetime.now()
        self.SupportedProfiles = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('String', self.ProductName))
        packet.append(pack_uatype('String', self.ProductUri))
        packet.append(pack_uatype('String', self.VendorName))
        packet.append(pack_uatype('ByteString', self.VendorProductCertificate))
        packet.append(pack_uatype('String', self.SoftwareVersion))
        packet.append(pack_uatype('String', self.BuildNumber))
        packet.append(pack_uatype('DateTime', self.BuildDate))
        packet.append(pack_uatype('String', self.IssuedBy))
        packet.append(pack_uatype('DateTime', self.IssueDate))
        packet.append(struct.pack('<i', len(self.SupportedProfiles)))
        for fieldname in self.SupportedProfiles:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = SoftwareCertificate()
        obj.ProductName = unpack_uatype('String', data)
        obj.ProductUri = unpack_uatype('String', data)
        obj.VendorName = unpack_uatype('String', data)
        obj.VendorProductCertificate = unpack_uatype('ByteString', data)
        obj.SoftwareVersion = unpack_uatype('String', data)
        obj.BuildNumber = unpack_uatype('String', data)
        obj.BuildDate = unpack_uatype('DateTime', data)
        obj.IssuedBy = unpack_uatype('String', data)
        obj.IssueDate = unpack_uatype('DateTime', data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.SupportedProfiles.append(SupportedProfile.from_binary(data))
        return obj

    def __str__(self):
        return 'SoftwareCertificate(' + 'ProductName:' + str(self.ProductName) + ', ' + \
               'ProductUri:' + str(self.ProductUri) + ', ' + \
               'VendorName:' + str(self.VendorName) + ', ' + \
               'VendorProductCertificate:' + str(self.VendorProductCertificate) + ', ' + \
               'SoftwareVersion:' + str(self.SoftwareVersion) + ', ' + \
               'BuildNumber:' + str(self.BuildNumber) + ', ' + \
               'BuildDate:' + str(self.BuildDate) + ', ' + \
               'IssuedBy:' + str(self.IssuedBy) + ', ' + \
               'IssueDate:' + str(self.IssueDate) + ', ' + \
               'SupportedProfiles:' + str(self.SupportedProfiles) + ')'

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
    def __init__(self):
        self.RelativePath = RelativePath()
        self.AttributeId = 0
        self.IndexRange = ''
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.RelativePath.to_binary())
        packet.append(pack_uatype('UInt32', self.AttributeId))
        packet.append(pack_uatype('String', self.IndexRange))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = QueryDataDescription()
        obj.RelativePath = RelativePath.from_binary(data)
        obj.AttributeId = unpack_uatype('UInt32', data)
        obj.IndexRange = unpack_uatype('String', data)
        return obj

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
    def __init__(self):
        self.TypeDefinitionNode = ExpandedNodeId()
        self.IncludeSubTypes = True
        self.DataToReturn = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeDefinitionNode.to_binary())
        packet.append(pack_uatype('Boolean', self.IncludeSubTypes))
        packet.append(struct.pack('<i', len(self.DataToReturn)))
        for fieldname in self.DataToReturn:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = NodeTypeDescription()
        obj.TypeDefinitionNode = ExpandedNodeId.from_binary(data)
        obj.IncludeSubTypes = unpack_uatype('Boolean', data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.DataToReturn.append(QueryDataDescription.from_binary(data))
        return obj

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
    def __init__(self):
        self.NodeId = ExpandedNodeId()
        self.TypeDefinitionNode = ExpandedNodeId()
        self.Values = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.NodeId.to_binary())
        packet.append(self.TypeDefinitionNode.to_binary())
        packet.append(struct.pack('<i', len(self.Values)))
        for fieldname in self.Values:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = QueryDataSet()
        obj.NodeId = ExpandedNodeId.from_binary(data)
        obj.TypeDefinitionNode = ExpandedNodeId.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.Values.append(Variant.from_binary(data))
        return obj

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
    def __init__(self):
        self.NodeId = NodeId()
        self.ReferenceTypeId = NodeId()
        self.IsForward = True
        self.ReferencedNodeIds = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.NodeId.to_binary())
        packet.append(self.ReferenceTypeId.to_binary())
        packet.append(pack_uatype('Boolean', self.IsForward))
        packet.append(struct.pack('<i', len(self.ReferencedNodeIds)))
        for fieldname in self.ReferencedNodeIds:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = NodeReference()
        obj.NodeId = NodeId.from_binary(data)
        obj.ReferenceTypeId = NodeId.from_binary(data)
        obj.IsForward = unpack_uatype('Boolean', data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.ReferencedNodeIds.append(NodeId.from_binary(data))
        return obj

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
    def __init__(self):
        self.FilterOperator = 0
        self.FilterOperands = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('UInt32', self.FilterOperator))
        packet.append(struct.pack('<i', len(self.FilterOperands)))
        for fieldname in self.FilterOperands:
            packet.append(extensionobject_to_binary(fieldname))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = ContentFilterElement()
        obj.FilterOperator = unpack_uatype('UInt32', data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.FilterOperands.append(extensionobject_from_binary(data))
        return obj

    def __str__(self):
        return 'ContentFilterElement(' + 'FilterOperator:' + str(self.FilterOperator) + ', ' + \
               'FilterOperands:' + str(self.FilterOperands) + ')'

    __repr__ = __str__


class ContentFilter(FrozenClass):
    '''
    :ivar Elements:
    :vartype Elements: ContentFilterElement
    '''
    def __init__(self):
        self.Elements = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.Elements)))
        for fieldname in self.Elements:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = ContentFilter()
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.Elements.append(ContentFilterElement.from_binary(data))
        return obj

    def __str__(self):
        return 'ContentFilter(' + 'Elements:' + str(self.Elements) + ')'

    __repr__ = __str__


class ElementOperand(FrozenClass):
    '''
    :ivar Index:
    :vartype Index: UInt32
    '''
    def __init__(self):
        self.Index = 0
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('UInt32', self.Index))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = ElementOperand()
        obj.Index = unpack_uatype('UInt32', data)
        return obj

    def __str__(self):
        return 'ElementOperand(' + 'Index:' + str(self.Index) + ')'

    __repr__ = __str__


class LiteralOperand(FrozenClass):
    '''
    :ivar Value:
    :vartype Value: Variant
    '''
    def __init__(self):
        self.Value = Variant()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.Value.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = LiteralOperand()
        obj.Value = Variant.from_binary(data)
        return obj

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
    def __init__(self):
        self.NodeId = NodeId()
        self.Alias = ''
        self.BrowsePath = RelativePath()
        self.AttributeId = 0
        self.IndexRange = ''
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.NodeId.to_binary())
        packet.append(pack_uatype('String', self.Alias))
        packet.append(self.BrowsePath.to_binary())
        packet.append(pack_uatype('UInt32', self.AttributeId))
        packet.append(pack_uatype('String', self.IndexRange))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = AttributeOperand()
        obj.NodeId = NodeId.from_binary(data)
        obj.Alias = unpack_uatype('String', data)
        obj.BrowsePath = RelativePath.from_binary(data)
        obj.AttributeId = unpack_uatype('UInt32', data)
        obj.IndexRange = unpack_uatype('String', data)
        return obj

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
    def __init__(self):
        self.TypeDefinitionId = NodeId()
        self.BrowsePath = []
        self.AttributeId = 0
        self.IndexRange = ''
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeDefinitionId.to_binary())
        packet.append(struct.pack('<i', len(self.BrowsePath)))
        for fieldname in self.BrowsePath:
            packet.append(fieldname.to_binary())
        packet.append(pack_uatype('UInt32', self.AttributeId))
        packet.append(pack_uatype('String', self.IndexRange))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = SimpleAttributeOperand()
        obj.TypeDefinitionId = NodeId.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.BrowsePath.append(QualifiedName.from_binary(data))
        obj.AttributeId = unpack_uatype('UInt32', data)
        obj.IndexRange = unpack_uatype('String', data)
        return obj

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
    def __init__(self):
        self.StatusCode = StatusCode()
        self.OperandStatusCodes = []
        self.OperandDiagnosticInfos = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.StatusCode.to_binary())
        packet.append(struct.pack('<i', len(self.OperandStatusCodes)))
        for fieldname in self.OperandStatusCodes:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.OperandDiagnosticInfos)))
        for fieldname in self.OperandDiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = ContentFilterElementResult()
        obj.StatusCode = StatusCode.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.OperandStatusCodes.append(StatusCode.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.OperandDiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        return obj

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
    def __init__(self):
        self.ElementResults = []
        self.ElementDiagnosticInfos = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.ElementResults)))
        for fieldname in self.ElementResults:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.ElementDiagnosticInfos)))
        for fieldname in self.ElementDiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = ContentFilterResult()
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.ElementResults.append(ContentFilterElementResult.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.ElementDiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        return obj

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
    def __init__(self):
        self.StatusCode = StatusCode()
        self.DataStatusCodes = []
        self.DataDiagnosticInfos = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.StatusCode.to_binary())
        packet.append(struct.pack('<i', len(self.DataStatusCodes)))
        for fieldname in self.DataStatusCodes:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.DataDiagnosticInfos)))
        for fieldname in self.DataDiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = ParsingResult()
        obj.StatusCode = StatusCode.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.DataStatusCodes.append(StatusCode.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.DataDiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        return obj

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
    def __init__(self):
        self.View = ViewDescription()
        self.NodeTypes = []
        self.Filter = ContentFilter()
        self.MaxDataSetsToReturn = 0
        self.MaxReferencesToReturn = 0
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.View.to_binary())
        packet.append(struct.pack('<i', len(self.NodeTypes)))
        for fieldname in self.NodeTypes:
            packet.append(fieldname.to_binary())
        packet.append(self.Filter.to_binary())
        packet.append(pack_uatype('UInt32', self.MaxDataSetsToReturn))
        packet.append(pack_uatype('UInt32', self.MaxReferencesToReturn))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = QueryFirstParameters()
        obj.View = ViewDescription.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.NodeTypes.append(NodeTypeDescription.from_binary(data))
        obj.Filter = ContentFilter.from_binary(data)
        obj.MaxDataSetsToReturn = unpack_uatype('UInt32', data)
        obj.MaxReferencesToReturn = unpack_uatype('UInt32', data)
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.QueryFirstRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = QueryFirstParameters()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = QueryFirstRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = QueryFirstParameters.from_binary(data)
        return obj

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
    def __init__(self):
        self.QueryDataSets = []
        self.ContinuationPoint = b''
        self.ParsingResults = []
        self.DiagnosticInfos = []
        self.FilterResult = ContentFilterResult()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.QueryDataSets)))
        for fieldname in self.QueryDataSets:
            packet.append(fieldname.to_binary())
        packet.append(pack_uatype('ByteString', self.ContinuationPoint))
        packet.append(struct.pack('<i', len(self.ParsingResults)))
        for fieldname in self.ParsingResults:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        packet.append(self.FilterResult.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = QueryFirstResult()
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.QueryDataSets.append(QueryDataSet.from_binary(data))
        obj.ContinuationPoint = unpack_uatype('ByteString', data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.ParsingResults.append(ParsingResult.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.DiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        obj.FilterResult = ContentFilterResult.from_binary(data)
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.QueryFirstResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = QueryFirstResult()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = QueryFirstResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = QueryFirstResult.from_binary(data)
        return obj

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
    def __init__(self):
        self.ReleaseContinuationPoint = True
        self.ContinuationPoint = b''
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('Boolean', self.ReleaseContinuationPoint))
        packet.append(pack_uatype('ByteString', self.ContinuationPoint))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = QueryNextParameters()
        obj.ReleaseContinuationPoint = unpack_uatype('Boolean', data)
        obj.ContinuationPoint = unpack_uatype('ByteString', data)
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.QueryNextRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = QueryNextParameters()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = QueryNextRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = QueryNextParameters.from_binary(data)
        return obj

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
    def __init__(self):
        self.QueryDataSets = []
        self.RevisedContinuationPoint = b''
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.QueryDataSets)))
        for fieldname in self.QueryDataSets:
            packet.append(fieldname.to_binary())
        packet.append(pack_uatype('ByteString', self.RevisedContinuationPoint))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = QueryNextResult()
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.QueryDataSets.append(QueryDataSet.from_binary(data))
        obj.RevisedContinuationPoint = unpack_uatype('ByteString', data)
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.QueryNextResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = QueryNextResult()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = QueryNextResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = QueryNextResult.from_binary(data)
        return obj

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
    def __init__(self):
        self.NodeId = NodeId()
        self.AttributeId = 0
        self.IndexRange = ''
        self.DataEncoding = QualifiedName()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.NodeId.to_binary())
        packet.append(pack_uatype('UInt32', self.AttributeId))
        packet.append(pack_uatype('String', self.IndexRange))
        packet.append(self.DataEncoding.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = ReadValueId()
        obj.NodeId = NodeId.from_binary(data)
        obj.AttributeId = unpack_uatype('UInt32', data)
        obj.IndexRange = unpack_uatype('String', data)
        obj.DataEncoding = QualifiedName.from_binary(data)
        return obj

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
    def __init__(self):
        self.MaxAge = 0
        self.TimestampsToReturn = 0
        self.NodesToRead = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('Double', self.MaxAge))
        packet.append(pack_uatype('UInt32', self.TimestampsToReturn))
        packet.append(struct.pack('<i', len(self.NodesToRead)))
        for fieldname in self.NodesToRead:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = ReadParameters()
        obj.MaxAge = unpack_uatype('Double', data)
        obj.TimestampsToReturn = unpack_uatype('UInt32', data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.NodesToRead.append(ReadValueId.from_binary(data))
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.ReadRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = ReadParameters()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = ReadRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = ReadParameters.from_binary(data)
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.ReadResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Results = []
        self.DiagnosticInfos = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(struct.pack('<i', len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = ReadResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.Results.append(DataValue.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.DiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        return obj

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
    def __init__(self):
        self.NodeId = NodeId()
        self.IndexRange = ''
        self.DataEncoding = QualifiedName()
        self.ContinuationPoint = b''
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.NodeId.to_binary())
        packet.append(pack_uatype('String', self.IndexRange))
        packet.append(self.DataEncoding.to_binary())
        packet.append(pack_uatype('ByteString', self.ContinuationPoint))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = HistoryReadValueId()
        obj.NodeId = NodeId.from_binary(data)
        obj.IndexRange = unpack_uatype('String', data)
        obj.DataEncoding = QualifiedName.from_binary(data)
        obj.ContinuationPoint = unpack_uatype('ByteString', data)
        return obj

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
    def __init__(self):
        self.StatusCode = StatusCode()
        self.ContinuationPoint = b''
        self.HistoryData = None
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.StatusCode.to_binary())
        packet.append(pack_uatype('ByteString', self.ContinuationPoint))
        packet.append(extensionobject_to_binary(self.HistoryData))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = HistoryReadResult()
        obj.StatusCode = StatusCode.from_binary(data)
        obj.ContinuationPoint = unpack_uatype('ByteString', data)
        obj.HistoryData = extensionobject_from_binary(data)
        return obj

    def __str__(self):
        return 'HistoryReadResult(' + 'StatusCode:' + str(self.StatusCode) + ', ' + \
               'ContinuationPoint:' + str(self.ContinuationPoint) + ', ' + \
               'HistoryData:' + str(self.HistoryData) + ')'

    __repr__ = __str__


class HistoryReadDetails(FrozenClass):
    '''
    '''
    def __init__(self):
        self._freeze()

    def to_binary(self):
        packet = []
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = HistoryReadDetails()
        return obj

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
    def __init__(self):
        self.NumValuesPerNode = 0
        self.StartTime = datetime.now()
        self.EndTime = datetime.now()
        self.Filter = EventFilter()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('UInt32', self.NumValuesPerNode))
        packet.append(pack_uatype('DateTime', self.StartTime))
        packet.append(pack_uatype('DateTime', self.EndTime))
        packet.append(self.Filter.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = ReadEventDetails()
        obj.NumValuesPerNode = unpack_uatype('UInt32', data)
        obj.StartTime = unpack_uatype('DateTime', data)
        obj.EndTime = unpack_uatype('DateTime', data)
        obj.Filter = EventFilter.from_binary(data)
        return obj

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
    def __init__(self):
        self.IsReadModified = True
        self.StartTime = datetime.now()
        self.EndTime = datetime.now()
        self.NumValuesPerNode = 0
        self.ReturnBounds = True
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('Boolean', self.IsReadModified))
        packet.append(pack_uatype('DateTime', self.StartTime))
        packet.append(pack_uatype('DateTime', self.EndTime))
        packet.append(pack_uatype('UInt32', self.NumValuesPerNode))
        packet.append(pack_uatype('Boolean', self.ReturnBounds))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = ReadRawModifiedDetails()
        obj.IsReadModified = unpack_uatype('Boolean', data)
        obj.StartTime = unpack_uatype('DateTime', data)
        obj.EndTime = unpack_uatype('DateTime', data)
        obj.NumValuesPerNode = unpack_uatype('UInt32', data)
        obj.ReturnBounds = unpack_uatype('Boolean', data)
        return obj

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
    def __init__(self):
        self.StartTime = datetime.now()
        self.EndTime = datetime.now()
        self.ProcessingInterval = 0
        self.AggregateType = []
        self.AggregateConfiguration = AggregateConfiguration()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('DateTime', self.StartTime))
        packet.append(pack_uatype('DateTime', self.EndTime))
        packet.append(pack_uatype('Double', self.ProcessingInterval))
        packet.append(struct.pack('<i', len(self.AggregateType)))
        for fieldname in self.AggregateType:
            packet.append(fieldname.to_binary())
        packet.append(self.AggregateConfiguration.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = ReadProcessedDetails()
        obj.StartTime = unpack_uatype('DateTime', data)
        obj.EndTime = unpack_uatype('DateTime', data)
        obj.ProcessingInterval = unpack_uatype('Double', data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.AggregateType.append(NodeId.from_binary(data))
        obj.AggregateConfiguration = AggregateConfiguration.from_binary(data)
        return obj

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
    def __init__(self):
        self.ReqTimes = []
        self.UseSimpleBounds = True
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.ReqTimes)))
        for fieldname in self.ReqTimes:
            packet.append(pack_uatype('DateTime', fieldname))
        packet.append(pack_uatype('Boolean', self.UseSimpleBounds))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = ReadAtTimeDetails()
        obj.ReqTimes = unpack_uatype_array('DateTime', data)
        obj.UseSimpleBounds = unpack_uatype('Boolean', data)
        return obj

    def __str__(self):
        return 'ReadAtTimeDetails(' + 'ReqTimes:' + str(self.ReqTimes) + ', ' + \
               'UseSimpleBounds:' + str(self.UseSimpleBounds) + ')'

    __repr__ = __str__


class HistoryData(FrozenClass):
    '''
    :ivar DataValues:
    :vartype DataValues: DataValue
    '''
    def __init__(self):
        self.DataValues = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.DataValues)))
        for fieldname in self.DataValues:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = HistoryData()
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.DataValues.append(DataValue.from_binary(data))
        return obj

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
    def __init__(self):
        self.ModificationTime = datetime.now()
        self.UpdateType = 0
        self.UserName = ''
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('DateTime', self.ModificationTime))
        packet.append(pack_uatype('UInt32', self.UpdateType))
        packet.append(pack_uatype('String', self.UserName))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = ModificationInfo()
        obj.ModificationTime = unpack_uatype('DateTime', data)
        obj.UpdateType = unpack_uatype('UInt32', data)
        obj.UserName = unpack_uatype('String', data)
        return obj

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
    def __init__(self):
        self.DataValues = []
        self.ModificationInfos = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.DataValues)))
        for fieldname in self.DataValues:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.ModificationInfos)))
        for fieldname in self.ModificationInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = HistoryModifiedData()
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.DataValues.append(DataValue.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.ModificationInfos.append(ModificationInfo.from_binary(data))
        return obj

    def __str__(self):
        return 'HistoryModifiedData(' + 'DataValues:' + str(self.DataValues) + ', ' + \
               'ModificationInfos:' + str(self.ModificationInfos) + ')'

    __repr__ = __str__


class HistoryEvent(FrozenClass):
    '''
    :ivar Events:
    :vartype Events: HistoryEventFieldList
    '''
    def __init__(self):
        self.Events = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.Events)))
        for fieldname in self.Events:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = HistoryEvent()
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.Events.append(HistoryEventFieldList.from_binary(data))
        return obj

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
    def __init__(self):
        self.HistoryReadDetails = None
        self.TimestampsToReturn = 0
        self.ReleaseContinuationPoints = True
        self.NodesToRead = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(extensionobject_to_binary(self.HistoryReadDetails))
        packet.append(pack_uatype('UInt32', self.TimestampsToReturn))
        packet.append(pack_uatype('Boolean', self.ReleaseContinuationPoints))
        packet.append(struct.pack('<i', len(self.NodesToRead)))
        for fieldname in self.NodesToRead:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = HistoryReadParameters()
        obj.HistoryReadDetails = extensionobject_from_binary(data)
        obj.TimestampsToReturn = unpack_uatype('UInt32', data)
        obj.ReleaseContinuationPoints = unpack_uatype('Boolean', data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.NodesToRead.append(HistoryReadValueId.from_binary(data))
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.HistoryReadRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = HistoryReadParameters()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = HistoryReadRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = HistoryReadParameters.from_binary(data)
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.HistoryReadResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Results = []
        self.DiagnosticInfos = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(struct.pack('<i', len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = HistoryReadResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.Results.append(HistoryReadResult.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.DiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        return obj

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
    def __init__(self):
        self.NodeId = NodeId()
        self.AttributeId = 0
        self.IndexRange = ''
        self.Value = DataValue()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.NodeId.to_binary())
        packet.append(pack_uatype('UInt32', self.AttributeId))
        packet.append(pack_uatype('String', self.IndexRange))
        packet.append(self.Value.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = WriteValue()
        obj.NodeId = NodeId.from_binary(data)
        obj.AttributeId = unpack_uatype('UInt32', data)
        obj.IndexRange = unpack_uatype('String', data)
        obj.Value = DataValue.from_binary(data)
        return obj

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
    def __init__(self):
        self.NodesToWrite = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.NodesToWrite)))
        for fieldname in self.NodesToWrite:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = WriteParameters()
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.NodesToWrite.append(WriteValue.from_binary(data))
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.WriteRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = WriteParameters()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = WriteRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = WriteParameters.from_binary(data)
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.WriteResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Results = []
        self.DiagnosticInfos = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(struct.pack('<i', len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = WriteResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.Results.append(StatusCode.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.DiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        return obj

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
    def __init__(self):
        self.NodeId = NodeId()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.NodeId.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = HistoryUpdateDetails()
        obj.NodeId = NodeId.from_binary(data)
        return obj

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
    def __init__(self):
        self.NodeId = NodeId()
        self.PerformInsertReplace = 0
        self.UpdateValues = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.NodeId.to_binary())
        packet.append(pack_uatype('UInt32', self.PerformInsertReplace))
        packet.append(struct.pack('<i', len(self.UpdateValues)))
        for fieldname in self.UpdateValues:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = UpdateDataDetails()
        obj.NodeId = NodeId.from_binary(data)
        obj.PerformInsertReplace = unpack_uatype('UInt32', data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.UpdateValues.append(DataValue.from_binary(data))
        return obj

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
    def __init__(self):
        self.NodeId = NodeId()
        self.PerformInsertReplace = 0
        self.UpdateValues = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.NodeId.to_binary())
        packet.append(pack_uatype('UInt32', self.PerformInsertReplace))
        packet.append(struct.pack('<i', len(self.UpdateValues)))
        for fieldname in self.UpdateValues:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = UpdateStructureDataDetails()
        obj.NodeId = NodeId.from_binary(data)
        obj.PerformInsertReplace = unpack_uatype('UInt32', data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.UpdateValues.append(DataValue.from_binary(data))
        return obj

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
    def __init__(self):
        self.NodeId = NodeId()
        self.PerformInsertReplace = 0
        self.Filter = EventFilter()
        self.EventData = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.NodeId.to_binary())
        packet.append(pack_uatype('UInt32', self.PerformInsertReplace))
        packet.append(self.Filter.to_binary())
        packet.append(struct.pack('<i', len(self.EventData)))
        for fieldname in self.EventData:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = UpdateEventDetails()
        obj.NodeId = NodeId.from_binary(data)
        obj.PerformInsertReplace = unpack_uatype('UInt32', data)
        obj.Filter = EventFilter.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.EventData.append(HistoryEventFieldList.from_binary(data))
        return obj

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
    def __init__(self):
        self.NodeId = NodeId()
        self.IsDeleteModified = True
        self.StartTime = datetime.now()
        self.EndTime = datetime.now()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.NodeId.to_binary())
        packet.append(pack_uatype('Boolean', self.IsDeleteModified))
        packet.append(pack_uatype('DateTime', self.StartTime))
        packet.append(pack_uatype('DateTime', self.EndTime))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = DeleteRawModifiedDetails()
        obj.NodeId = NodeId.from_binary(data)
        obj.IsDeleteModified = unpack_uatype('Boolean', data)
        obj.StartTime = unpack_uatype('DateTime', data)
        obj.EndTime = unpack_uatype('DateTime', data)
        return obj

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
    def __init__(self):
        self.NodeId = NodeId()
        self.ReqTimes = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.NodeId.to_binary())
        packet.append(struct.pack('<i', len(self.ReqTimes)))
        for fieldname in self.ReqTimes:
            packet.append(pack_uatype('DateTime', fieldname))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = DeleteAtTimeDetails()
        obj.NodeId = NodeId.from_binary(data)
        obj.ReqTimes = unpack_uatype_array('DateTime', data)
        return obj

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
    def __init__(self):
        self.NodeId = NodeId()
        self.EventIds = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.NodeId.to_binary())
        packet.append(struct.pack('<i', len(self.EventIds)))
        for fieldname in self.EventIds:
            packet.append(pack_uatype('ByteString', fieldname))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = DeleteEventDetails()
        obj.NodeId = NodeId.from_binary(data)
        obj.EventIds = unpack_uatype_array('ByteString', data)
        return obj

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
    def __init__(self):
        self.StatusCode = StatusCode()
        self.OperationResults = []
        self.DiagnosticInfos = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.StatusCode.to_binary())
        packet.append(struct.pack('<i', len(self.OperationResults)))
        for fieldname in self.OperationResults:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = HistoryUpdateResult()
        obj.StatusCode = StatusCode.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.OperationResults.append(StatusCode.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.DiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        return obj

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
    def __init__(self):
        self.HistoryUpdateDetails = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.HistoryUpdateDetails)))
        for fieldname in self.HistoryUpdateDetails:
            packet.append(extensionobject_to_binary(fieldname))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = HistoryUpdateParameters()
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.HistoryUpdateDetails.append(extensionobject_from_binary(data))
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.HistoryUpdateRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = HistoryUpdateParameters()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = HistoryUpdateRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = HistoryUpdateParameters.from_binary(data)
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.HistoryUpdateResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Results = []
        self.DiagnosticInfos = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(struct.pack('<i', len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = HistoryUpdateResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.Results.append(HistoryUpdateResult.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.DiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        return obj

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
    def __init__(self):
        self.ObjectId = NodeId()
        self.MethodId = NodeId()
        self.InputArguments = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.ObjectId.to_binary())
        packet.append(self.MethodId.to_binary())
        packet.append(struct.pack('<i', len(self.InputArguments)))
        for fieldname in self.InputArguments:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = CallMethodRequest()
        obj.ObjectId = NodeId.from_binary(data)
        obj.MethodId = NodeId.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.InputArguments.append(Variant.from_binary(data))
        return obj

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
    def __init__(self):
        self.StatusCode = StatusCode()
        self.InputArgumentResults = []
        self.InputArgumentDiagnosticInfos = []
        self.OutputArguments = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.StatusCode.to_binary())
        packet.append(struct.pack('<i', len(self.InputArgumentResults)))
        for fieldname in self.InputArgumentResults:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.InputArgumentDiagnosticInfos)))
        for fieldname in self.InputArgumentDiagnosticInfos:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.OutputArguments)))
        for fieldname in self.OutputArguments:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = CallMethodResult()
        obj.StatusCode = StatusCode.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.InputArgumentResults.append(StatusCode.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.InputArgumentDiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.OutputArguments.append(Variant.from_binary(data))
        return obj

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
    def __init__(self):
        self.MethodsToCall = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.MethodsToCall)))
        for fieldname in self.MethodsToCall:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = CallParameters()
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.MethodsToCall.append(CallMethodRequest.from_binary(data))
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.CallRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = CallParameters()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = CallRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = CallParameters.from_binary(data)
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.CallResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Results = []
        self.DiagnosticInfos = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(struct.pack('<i', len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = CallResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.Results.append(CallMethodResult.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.DiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        return obj

    def __str__(self):
        return 'CallResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
               'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
               'Results:' + str(self.Results) + ', ' + \
               'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'

    __repr__ = __str__


class MonitoringFilter(FrozenClass):
    '''
    '''
    def __init__(self):
        self._freeze()

    def to_binary(self):
        packet = []
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = MonitoringFilter()
        return obj

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
    def __init__(self):
        self.Trigger = 0
        self.DeadbandType = 0
        self.DeadbandValue = 0
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('UInt32', self.Trigger))
        packet.append(pack_uatype('UInt32', self.DeadbandType))
        packet.append(pack_uatype('Double', self.DeadbandValue))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = DataChangeFilter()
        obj.Trigger = unpack_uatype('UInt32', data)
        obj.DeadbandType = unpack_uatype('UInt32', data)
        obj.DeadbandValue = unpack_uatype('Double', data)
        return obj

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
    def __init__(self):
        self.SelectClauses = []
        self.WhereClause = ContentFilter()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.SelectClauses)))
        for fieldname in self.SelectClauses:
            packet.append(fieldname.to_binary())
        packet.append(self.WhereClause.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = EventFilter()
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.SelectClauses.append(SimpleAttributeOperand.from_binary(data))
        obj.WhereClause = ContentFilter.from_binary(data)
        return obj

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
    def __init__(self):
        self.UseServerCapabilitiesDefaults = True
        self.TreatUncertainAsBad = True
        self.PercentDataBad = 0
        self.PercentDataGood = 0
        self.UseSlopedExtrapolation = True
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('Boolean', self.UseServerCapabilitiesDefaults))
        packet.append(pack_uatype('Boolean', self.TreatUncertainAsBad))
        packet.append(pack_uatype('Byte', self.PercentDataBad))
        packet.append(pack_uatype('Byte', self.PercentDataGood))
        packet.append(pack_uatype('Boolean', self.UseSlopedExtrapolation))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = AggregateConfiguration()
        obj.UseServerCapabilitiesDefaults = unpack_uatype('Boolean', data)
        obj.TreatUncertainAsBad = unpack_uatype('Boolean', data)
        obj.PercentDataBad = unpack_uatype('Byte', data)
        obj.PercentDataGood = unpack_uatype('Byte', data)
        obj.UseSlopedExtrapolation = unpack_uatype('Boolean', data)
        return obj

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
    def __init__(self):
        self.StartTime = datetime.now()
        self.AggregateType = NodeId()
        self.ProcessingInterval = 0
        self.AggregateConfiguration = AggregateConfiguration()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('DateTime', self.StartTime))
        packet.append(self.AggregateType.to_binary())
        packet.append(pack_uatype('Double', self.ProcessingInterval))
        packet.append(self.AggregateConfiguration.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = AggregateFilter()
        obj.StartTime = unpack_uatype('DateTime', data)
        obj.AggregateType = NodeId.from_binary(data)
        obj.ProcessingInterval = unpack_uatype('Double', data)
        obj.AggregateConfiguration = AggregateConfiguration.from_binary(data)
        return obj

    def __str__(self):
        return 'AggregateFilter(' + 'StartTime:' + str(self.StartTime) + ', ' + \
               'AggregateType:' + str(self.AggregateType) + ', ' + \
               'ProcessingInterval:' + str(self.ProcessingInterval) + ', ' + \
               'AggregateConfiguration:' + str(self.AggregateConfiguration) + ')'

    __repr__ = __str__


class MonitoringFilterResult(FrozenClass):
    '''
    '''
    def __init__(self):
        self._freeze()

    def to_binary(self):
        packet = []
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = MonitoringFilterResult()
        return obj

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
    def __init__(self):
        self.SelectClauseResults = []
        self.SelectClauseDiagnosticInfos = []
        self.WhereClauseResult = ContentFilterResult()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.SelectClauseResults)))
        for fieldname in self.SelectClauseResults:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.SelectClauseDiagnosticInfos)))
        for fieldname in self.SelectClauseDiagnosticInfos:
            packet.append(fieldname.to_binary())
        packet.append(self.WhereClauseResult.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = EventFilterResult()
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.SelectClauseResults.append(StatusCode.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.SelectClauseDiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        obj.WhereClauseResult = ContentFilterResult.from_binary(data)
        return obj

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
    def __init__(self):
        self.RevisedStartTime = datetime.now()
        self.RevisedProcessingInterval = 0
        self.RevisedAggregateConfiguration = AggregateConfiguration()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('DateTime', self.RevisedStartTime))
        packet.append(pack_uatype('Double', self.RevisedProcessingInterval))
        packet.append(self.RevisedAggregateConfiguration.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = AggregateFilterResult()
        obj.RevisedStartTime = unpack_uatype('DateTime', data)
        obj.RevisedProcessingInterval = unpack_uatype('Double', data)
        obj.RevisedAggregateConfiguration = AggregateConfiguration.from_binary(data)
        return obj

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
    def __init__(self):
        self.ClientHandle = 0
        self.SamplingInterval = 0
        self.Filter = None
        self.QueueSize = 0
        self.DiscardOldest = True
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('UInt32', self.ClientHandle))
        packet.append(pack_uatype('Double', self.SamplingInterval))
        packet.append(extensionobject_to_binary(self.Filter))
        packet.append(pack_uatype('UInt32', self.QueueSize))
        packet.append(pack_uatype('Boolean', self.DiscardOldest))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = MonitoringParameters()
        obj.ClientHandle = unpack_uatype('UInt32', data)
        obj.SamplingInterval = unpack_uatype('Double', data)
        obj.Filter = extensionobject_from_binary(data)
        obj.QueueSize = unpack_uatype('UInt32', data)
        obj.DiscardOldest = unpack_uatype('Boolean', data)
        return obj

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
    def __init__(self):
        self.ItemToMonitor = ReadValueId()
        self.MonitoringMode = 0
        self.RequestedParameters = MonitoringParameters()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.ItemToMonitor.to_binary())
        packet.append(pack_uatype('UInt32', self.MonitoringMode))
        packet.append(self.RequestedParameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = MonitoredItemCreateRequest()
        obj.ItemToMonitor = ReadValueId.from_binary(data)
        obj.MonitoringMode = unpack_uatype('UInt32', data)
        obj.RequestedParameters = MonitoringParameters.from_binary(data)
        return obj

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
    def __init__(self):
        self.StatusCode = StatusCode()
        self.MonitoredItemId = 0
        self.RevisedSamplingInterval = 0
        self.RevisedQueueSize = 0
        self.FilterResult = None
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.StatusCode.to_binary())
        packet.append(pack_uatype('UInt32', self.MonitoredItemId))
        packet.append(pack_uatype('Double', self.RevisedSamplingInterval))
        packet.append(pack_uatype('UInt32', self.RevisedQueueSize))
        packet.append(extensionobject_to_binary(self.FilterResult))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = MonitoredItemCreateResult()
        obj.StatusCode = StatusCode.from_binary(data)
        obj.MonitoredItemId = unpack_uatype('UInt32', data)
        obj.RevisedSamplingInterval = unpack_uatype('Double', data)
        obj.RevisedQueueSize = unpack_uatype('UInt32', data)
        obj.FilterResult = extensionobject_from_binary(data)
        return obj

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
    def __init__(self):
        self.SubscriptionId = 0
        self.TimestampsToReturn = 0
        self.ItemsToCreate = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('UInt32', self.SubscriptionId))
        packet.append(pack_uatype('UInt32', self.TimestampsToReturn))
        packet.append(struct.pack('<i', len(self.ItemsToCreate)))
        for fieldname in self.ItemsToCreate:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = CreateMonitoredItemsParameters()
        obj.SubscriptionId = unpack_uatype('UInt32', data)
        obj.TimestampsToReturn = unpack_uatype('UInt32', data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.ItemsToCreate.append(MonitoredItemCreateRequest.from_binary(data))
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.CreateMonitoredItemsRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = CreateMonitoredItemsParameters()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = CreateMonitoredItemsRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = CreateMonitoredItemsParameters.from_binary(data)
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.CreateMonitoredItemsResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Results = []
        self.DiagnosticInfos = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(struct.pack('<i', len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = CreateMonitoredItemsResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.Results.append(MonitoredItemCreateResult.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.DiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        return obj

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
    def __init__(self):
        self.MonitoredItemId = 0
        self.RequestedParameters = MonitoringParameters()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('UInt32', self.MonitoredItemId))
        packet.append(self.RequestedParameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = MonitoredItemModifyRequest()
        obj.MonitoredItemId = unpack_uatype('UInt32', data)
        obj.RequestedParameters = MonitoringParameters.from_binary(data)
        return obj

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
    def __init__(self):
        self.StatusCode = StatusCode()
        self.RevisedSamplingInterval = 0
        self.RevisedQueueSize = 0
        self.FilterResult = None
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.StatusCode.to_binary())
        packet.append(pack_uatype('Double', self.RevisedSamplingInterval))
        packet.append(pack_uatype('UInt32', self.RevisedQueueSize))
        packet.append(extensionobject_to_binary(self.FilterResult))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = MonitoredItemModifyResult()
        obj.StatusCode = StatusCode.from_binary(data)
        obj.RevisedSamplingInterval = unpack_uatype('Double', data)
        obj.RevisedQueueSize = unpack_uatype('UInt32', data)
        obj.FilterResult = extensionobject_from_binary(data)
        return obj

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
    def __init__(self):
        self.SubscriptionId = 0
        self.TimestampsToReturn = 0
        self.ItemsToModify = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('UInt32', self.SubscriptionId))
        packet.append(pack_uatype('UInt32', self.TimestampsToReturn))
        packet.append(struct.pack('<i', len(self.ItemsToModify)))
        for fieldname in self.ItemsToModify:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = ModifyMonitoredItemsParameters()
        obj.SubscriptionId = unpack_uatype('UInt32', data)
        obj.TimestampsToReturn = unpack_uatype('UInt32', data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.ItemsToModify.append(MonitoredItemModifyRequest.from_binary(data))
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.ModifyMonitoredItemsRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = ModifyMonitoredItemsParameters()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = ModifyMonitoredItemsRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = ModifyMonitoredItemsParameters.from_binary(data)
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.ModifyMonitoredItemsResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Results = []
        self.DiagnosticInfos = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(struct.pack('<i', len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = ModifyMonitoredItemsResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.Results.append(MonitoredItemModifyResult.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.DiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        return obj

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
    def __init__(self):
        self.SubscriptionId = 0
        self.MonitoringMode = 0
        self.MonitoredItemIds = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('UInt32', self.SubscriptionId))
        packet.append(pack_uatype('UInt32', self.MonitoringMode))
        packet.append(struct.pack('<i', len(self.MonitoredItemIds)))
        for fieldname in self.MonitoredItemIds:
            packet.append(pack_uatype('UInt32', fieldname))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = SetMonitoringModeParameters()
        obj.SubscriptionId = unpack_uatype('UInt32', data)
        obj.MonitoringMode = unpack_uatype('UInt32', data)
        obj.MonitoredItemIds = unpack_uatype_array('UInt32', data)
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.SetMonitoringModeRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = SetMonitoringModeParameters()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = SetMonitoringModeRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = SetMonitoringModeParameters.from_binary(data)
        return obj

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
    def __init__(self):
        self.Results = []
        self.DiagnosticInfos = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = SetMonitoringModeResult()
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.Results.append(StatusCode.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.DiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.SetMonitoringModeResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = SetMonitoringModeResult()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = SetMonitoringModeResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = SetMonitoringModeResult.from_binary(data)
        return obj

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
    def __init__(self):
        self.SubscriptionId = 0
        self.TriggeringItemId = 0
        self.LinksToAdd = []
        self.LinksToRemove = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('UInt32', self.SubscriptionId))
        packet.append(pack_uatype('UInt32', self.TriggeringItemId))
        packet.append(struct.pack('<i', len(self.LinksToAdd)))
        for fieldname in self.LinksToAdd:
            packet.append(pack_uatype('UInt32', fieldname))
        packet.append(struct.pack('<i', len(self.LinksToRemove)))
        for fieldname in self.LinksToRemove:
            packet.append(pack_uatype('UInt32', fieldname))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = SetTriggeringParameters()
        obj.SubscriptionId = unpack_uatype('UInt32', data)
        obj.TriggeringItemId = unpack_uatype('UInt32', data)
        obj.LinksToAdd = unpack_uatype_array('UInt32', data)
        obj.LinksToRemove = unpack_uatype_array('UInt32', data)
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.SetTriggeringRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = SetTriggeringParameters()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = SetTriggeringRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = SetTriggeringParameters.from_binary(data)
        return obj

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
    def __init__(self):
        self.AddResults = []
        self.AddDiagnosticInfos = []
        self.RemoveResults = []
        self.RemoveDiagnosticInfos = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.AddResults)))
        for fieldname in self.AddResults:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.AddDiagnosticInfos)))
        for fieldname in self.AddDiagnosticInfos:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.RemoveResults)))
        for fieldname in self.RemoveResults:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.RemoveDiagnosticInfos)))
        for fieldname in self.RemoveDiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = SetTriggeringResult()
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.AddResults.append(StatusCode.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.AddDiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.RemoveResults.append(StatusCode.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.RemoveDiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.SetTriggeringResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = SetTriggeringResult()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = SetTriggeringResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = SetTriggeringResult.from_binary(data)
        return obj

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
    def __init__(self):
        self.SubscriptionId = 0
        self.MonitoredItemIds = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('UInt32', self.SubscriptionId))
        packet.append(struct.pack('<i', len(self.MonitoredItemIds)))
        for fieldname in self.MonitoredItemIds:
            packet.append(pack_uatype('UInt32', fieldname))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = DeleteMonitoredItemsParameters()
        obj.SubscriptionId = unpack_uatype('UInt32', data)
        obj.MonitoredItemIds = unpack_uatype_array('UInt32', data)
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.DeleteMonitoredItemsRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = DeleteMonitoredItemsParameters()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = DeleteMonitoredItemsRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = DeleteMonitoredItemsParameters.from_binary(data)
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.DeleteMonitoredItemsResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Results = []
        self.DiagnosticInfos = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(struct.pack('<i', len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = DeleteMonitoredItemsResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.Results.append(StatusCode.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.DiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        return obj

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
    def __init__(self):
        self.RequestedPublishingInterval = 0
        self.RequestedLifetimeCount = 0
        self.RequestedMaxKeepAliveCount = 0
        self.MaxNotificationsPerPublish = 0
        self.PublishingEnabled = True
        self.Priority = 0
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('Double', self.RequestedPublishingInterval))
        packet.append(pack_uatype('UInt32', self.RequestedLifetimeCount))
        packet.append(pack_uatype('UInt32', self.RequestedMaxKeepAliveCount))
        packet.append(pack_uatype('UInt32', self.MaxNotificationsPerPublish))
        packet.append(pack_uatype('Boolean', self.PublishingEnabled))
        packet.append(pack_uatype('Byte', self.Priority))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = CreateSubscriptionParameters()
        obj.RequestedPublishingInterval = unpack_uatype('Double', data)
        obj.RequestedLifetimeCount = unpack_uatype('UInt32', data)
        obj.RequestedMaxKeepAliveCount = unpack_uatype('UInt32', data)
        obj.MaxNotificationsPerPublish = unpack_uatype('UInt32', data)
        obj.PublishingEnabled = unpack_uatype('Boolean', data)
        obj.Priority = unpack_uatype('Byte', data)
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.CreateSubscriptionRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = CreateSubscriptionParameters()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = CreateSubscriptionRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = CreateSubscriptionParameters.from_binary(data)
        return obj

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
    def __init__(self):
        self.SubscriptionId = 0
        self.RevisedPublishingInterval = 0
        self.RevisedLifetimeCount = 0
        self.RevisedMaxKeepAliveCount = 0
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('UInt32', self.SubscriptionId))
        packet.append(pack_uatype('Double', self.RevisedPublishingInterval))
        packet.append(pack_uatype('UInt32', self.RevisedLifetimeCount))
        packet.append(pack_uatype('UInt32', self.RevisedMaxKeepAliveCount))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = CreateSubscriptionResult()
        obj.SubscriptionId = unpack_uatype('UInt32', data)
        obj.RevisedPublishingInterval = unpack_uatype('Double', data)
        obj.RevisedLifetimeCount = unpack_uatype('UInt32', data)
        obj.RevisedMaxKeepAliveCount = unpack_uatype('UInt32', data)
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.CreateSubscriptionResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = CreateSubscriptionResult()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = CreateSubscriptionResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = CreateSubscriptionResult.from_binary(data)
        return obj

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
    def __init__(self):
        self.SubscriptionId = 0
        self.RequestedPublishingInterval = 0
        self.RequestedLifetimeCount = 0
        self.RequestedMaxKeepAliveCount = 0
        self.MaxNotificationsPerPublish = 0
        self.Priority = 0
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('UInt32', self.SubscriptionId))
        packet.append(pack_uatype('Double', self.RequestedPublishingInterval))
        packet.append(pack_uatype('UInt32', self.RequestedLifetimeCount))
        packet.append(pack_uatype('UInt32', self.RequestedMaxKeepAliveCount))
        packet.append(pack_uatype('UInt32', self.MaxNotificationsPerPublish))
        packet.append(pack_uatype('Byte', self.Priority))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = ModifySubscriptionParameters()
        obj.SubscriptionId = unpack_uatype('UInt32', data)
        obj.RequestedPublishingInterval = unpack_uatype('Double', data)
        obj.RequestedLifetimeCount = unpack_uatype('UInt32', data)
        obj.RequestedMaxKeepAliveCount = unpack_uatype('UInt32', data)
        obj.MaxNotificationsPerPublish = unpack_uatype('UInt32', data)
        obj.Priority = unpack_uatype('Byte', data)
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.ModifySubscriptionRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = ModifySubscriptionParameters()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = ModifySubscriptionRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = ModifySubscriptionParameters.from_binary(data)
        return obj

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
    def __init__(self):
        self.RevisedPublishingInterval = 0
        self.RevisedLifetimeCount = 0
        self.RevisedMaxKeepAliveCount = 0
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('Double', self.RevisedPublishingInterval))
        packet.append(pack_uatype('UInt32', self.RevisedLifetimeCount))
        packet.append(pack_uatype('UInt32', self.RevisedMaxKeepAliveCount))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = ModifySubscriptionResult()
        obj.RevisedPublishingInterval = unpack_uatype('Double', data)
        obj.RevisedLifetimeCount = unpack_uatype('UInt32', data)
        obj.RevisedMaxKeepAliveCount = unpack_uatype('UInt32', data)
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.ModifySubscriptionResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = ModifySubscriptionResult()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = ModifySubscriptionResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = ModifySubscriptionResult.from_binary(data)
        return obj

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
    def __init__(self):
        self.PublishingEnabled = True
        self.SubscriptionIds = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('Boolean', self.PublishingEnabled))
        packet.append(struct.pack('<i', len(self.SubscriptionIds)))
        for fieldname in self.SubscriptionIds:
            packet.append(pack_uatype('UInt32', fieldname))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = SetPublishingModeParameters()
        obj.PublishingEnabled = unpack_uatype('Boolean', data)
        obj.SubscriptionIds = unpack_uatype_array('UInt32', data)
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.SetPublishingModeRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = SetPublishingModeParameters()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = SetPublishingModeRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = SetPublishingModeParameters.from_binary(data)
        return obj

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
    def __init__(self):
        self.Results = []
        self.DiagnosticInfos = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = SetPublishingModeResult()
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.Results.append(StatusCode.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.DiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.SetPublishingModeResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = SetPublishingModeResult()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = SetPublishingModeResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = SetPublishingModeResult.from_binary(data)
        return obj

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
    def __init__(self):
        self.SequenceNumber = 0
        self.PublishTime = datetime.now()
        self.NotificationData = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('UInt32', self.SequenceNumber))
        packet.append(pack_uatype('DateTime', self.PublishTime))
        packet.append(struct.pack('<i', len(self.NotificationData)))
        for fieldname in self.NotificationData:
            packet.append(extensionobject_to_binary(fieldname))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = NotificationMessage()
        obj.SequenceNumber = unpack_uatype('UInt32', data)
        obj.PublishTime = unpack_uatype('DateTime', data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.NotificationData.append(extensionobject_from_binary(data))
        return obj

    def __str__(self):
        return 'NotificationMessage(' + 'SequenceNumber:' + str(self.SequenceNumber) + ', ' + \
               'PublishTime:' + str(self.PublishTime) + ', ' + \
               'NotificationData:' + str(self.NotificationData) + ')'

    __repr__ = __str__


class NotificationData(FrozenClass):
    '''
    '''
    def __init__(self):
        self._freeze()

    def to_binary(self):
        packet = []
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = NotificationData()
        return obj

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
    def __init__(self):
        self.MonitoredItems = []
        self.DiagnosticInfos = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.MonitoredItems)))
        for fieldname in self.MonitoredItems:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = DataChangeNotification()
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.MonitoredItems.append(MonitoredItemNotification.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.DiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        return obj

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
    def __init__(self):
        self.ClientHandle = 0
        self.Value = DataValue()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('UInt32', self.ClientHandle))
        packet.append(self.Value.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = MonitoredItemNotification()
        obj.ClientHandle = unpack_uatype('UInt32', data)
        obj.Value = DataValue.from_binary(data)
        return obj

    def __str__(self):
        return 'MonitoredItemNotification(' + 'ClientHandle:' + str(self.ClientHandle) + ', ' + \
               'Value:' + str(self.Value) + ')'

    __repr__ = __str__


class EventNotificationList(FrozenClass):
    '''
    :ivar Events:
    :vartype Events: EventFieldList
    '''
    def __init__(self):
        self.Events = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.Events)))
        for fieldname in self.Events:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = EventNotificationList()
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.Events.append(EventFieldList.from_binary(data))
        return obj

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
    def __init__(self):
        self.ClientHandle = 0
        self.EventFields = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('UInt32', self.ClientHandle))
        packet.append(struct.pack('<i', len(self.EventFields)))
        for fieldname in self.EventFields:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = EventFieldList()
        obj.ClientHandle = unpack_uatype('UInt32', data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.EventFields.append(Variant.from_binary(data))
        return obj

    def __str__(self):
        return 'EventFieldList(' + 'ClientHandle:' + str(self.ClientHandle) + ', ' + \
               'EventFields:' + str(self.EventFields) + ')'

    __repr__ = __str__


class HistoryEventFieldList(FrozenClass):
    '''
    :ivar EventFields:
    :vartype EventFields: Variant
    '''
    def __init__(self):
        self.EventFields = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.EventFields)))
        for fieldname in self.EventFields:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = HistoryEventFieldList()
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.EventFields.append(Variant.from_binary(data))
        return obj

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
    def __init__(self):
        self.Status = StatusCode()
        self.DiagnosticInfo = DiagnosticInfo()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.Status.to_binary())
        packet.append(self.DiagnosticInfo.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = StatusChangeNotification()
        obj.Status = StatusCode.from_binary(data)
        obj.DiagnosticInfo = DiagnosticInfo.from_binary(data)
        return obj

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
    def __init__(self):
        self.SubscriptionId = 0
        self.SequenceNumber = 0
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('UInt32', self.SubscriptionId))
        packet.append(pack_uatype('UInt32', self.SequenceNumber))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = SubscriptionAcknowledgement()
        obj.SubscriptionId = unpack_uatype('UInt32', data)
        obj.SequenceNumber = unpack_uatype('UInt32', data)
        return obj

    def __str__(self):
        return 'SubscriptionAcknowledgement(' + 'SubscriptionId:' + str(self.SubscriptionId) + ', ' + \
               'SequenceNumber:' + str(self.SequenceNumber) + ')'

    __repr__ = __str__


class PublishParameters(FrozenClass):
    '''
    :ivar SubscriptionAcknowledgements:
    :vartype SubscriptionAcknowledgements: SubscriptionAcknowledgement
    '''
    def __init__(self):
        self.SubscriptionAcknowledgements = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.SubscriptionAcknowledgements)))
        for fieldname in self.SubscriptionAcknowledgements:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = PublishParameters()
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.SubscriptionAcknowledgements.append(SubscriptionAcknowledgement.from_binary(data))
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.PublishRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = PublishParameters()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = PublishRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = PublishParameters.from_binary(data)
        return obj

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
    def __init__(self):
        self.SubscriptionId = 0
        self.AvailableSequenceNumbers = []
        self.MoreNotifications = True
        self.NotificationMessage = NotificationMessage()
        self.Results = []
        self.DiagnosticInfos = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('UInt32', self.SubscriptionId))
        packet.append(struct.pack('<i', len(self.AvailableSequenceNumbers)))
        for fieldname in self.AvailableSequenceNumbers:
            packet.append(pack_uatype('UInt32', fieldname))
        packet.append(pack_uatype('Boolean', self.MoreNotifications))
        packet.append(self.NotificationMessage.to_binary())
        packet.append(struct.pack('<i', len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = PublishResult()
        obj.SubscriptionId = unpack_uatype('UInt32', data)
        obj.AvailableSequenceNumbers = unpack_uatype_array('UInt32', data)
        obj.MoreNotifications = unpack_uatype('Boolean', data)
        obj.NotificationMessage = NotificationMessage.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.Results.append(StatusCode.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.DiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.PublishResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = PublishResult()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = PublishResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = PublishResult.from_binary(data)
        return obj

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
    def __init__(self):
        self.SubscriptionId = 0
        self.RetransmitSequenceNumber = 0
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('UInt32', self.SubscriptionId))
        packet.append(pack_uatype('UInt32', self.RetransmitSequenceNumber))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = RepublishParameters()
        obj.SubscriptionId = unpack_uatype('UInt32', data)
        obj.RetransmitSequenceNumber = unpack_uatype('UInt32', data)
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.RepublishRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = RepublishParameters()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = RepublishRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = RepublishParameters.from_binary(data)
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.RepublishResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.NotificationMessage = NotificationMessage()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.NotificationMessage.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = RepublishResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.NotificationMessage = NotificationMessage.from_binary(data)
        return obj

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
    def __init__(self):
        self.StatusCode = StatusCode()
        self.AvailableSequenceNumbers = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.StatusCode.to_binary())
        packet.append(struct.pack('<i', len(self.AvailableSequenceNumbers)))
        for fieldname in self.AvailableSequenceNumbers:
            packet.append(pack_uatype('UInt32', fieldname))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = TransferResult()
        obj.StatusCode = StatusCode.from_binary(data)
        obj.AvailableSequenceNumbers = unpack_uatype_array('UInt32', data)
        return obj

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
    def __init__(self):
        self.SubscriptionIds = []
        self.SendInitialValues = True
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.SubscriptionIds)))
        for fieldname in self.SubscriptionIds:
            packet.append(pack_uatype('UInt32', fieldname))
        packet.append(pack_uatype('Boolean', self.SendInitialValues))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = TransferSubscriptionsParameters()
        obj.SubscriptionIds = unpack_uatype_array('UInt32', data)
        obj.SendInitialValues = unpack_uatype('Boolean', data)
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.TransferSubscriptionsRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = TransferSubscriptionsParameters()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = TransferSubscriptionsRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = TransferSubscriptionsParameters.from_binary(data)
        return obj

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
    def __init__(self):
        self.Results = []
        self.DiagnosticInfos = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = TransferSubscriptionsResult()
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.Results.append(TransferResult.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.DiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.TransferSubscriptionsResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = TransferSubscriptionsResult()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = TransferSubscriptionsResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = TransferSubscriptionsResult.from_binary(data)
        return obj

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
    def __init__(self):
        self.SubscriptionIds = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.SubscriptionIds)))
        for fieldname in self.SubscriptionIds:
            packet.append(pack_uatype('UInt32', fieldname))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = DeleteSubscriptionsParameters()
        obj.SubscriptionIds = unpack_uatype_array('UInt32', data)
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.DeleteSubscriptionsRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = DeleteSubscriptionsParameters()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = DeleteSubscriptionsRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = DeleteSubscriptionsParameters.from_binary(data)
        return obj

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
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.DeleteSubscriptionsResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Results = []
        self.DiagnosticInfos = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(struct.pack('<i', len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = DeleteSubscriptionsResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.Results.append(StatusCode.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.DiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        return obj

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
    def __init__(self):
        self.ProductUri = ''
        self.ManufacturerName = ''
        self.ProductName = ''
        self.SoftwareVersion = ''
        self.BuildNumber = ''
        self.BuildDate = datetime.now()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('String', self.ProductUri))
        packet.append(pack_uatype('String', self.ManufacturerName))
        packet.append(pack_uatype('String', self.ProductName))
        packet.append(pack_uatype('String', self.SoftwareVersion))
        packet.append(pack_uatype('String', self.BuildNumber))
        packet.append(pack_uatype('DateTime', self.BuildDate))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = BuildInfo()
        obj.ProductUri = unpack_uatype('String', data)
        obj.ManufacturerName = unpack_uatype('String', data)
        obj.ProductName = unpack_uatype('String', data)
        obj.SoftwareVersion = unpack_uatype('String', data)
        obj.BuildNumber = unpack_uatype('String', data)
        obj.BuildDate = unpack_uatype('DateTime', data)
        return obj

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
    def __init__(self):
        self.ServerId = ''
        self.ServiceLevel = 0
        self.ServerState = 0
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('String', self.ServerId))
        packet.append(pack_uatype('Byte', self.ServiceLevel))
        packet.append(pack_uatype('UInt32', self.ServerState))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = RedundantServerDataType()
        obj.ServerId = unpack_uatype('String', data)
        obj.ServiceLevel = unpack_uatype('Byte', data)
        obj.ServerState = unpack_uatype('UInt32', data)
        return obj

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
    def __init__(self):
        self.EndpointUrlList = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.EndpointUrlList)))
        for fieldname in self.EndpointUrlList:
            packet.append(pack_uatype('String', fieldname))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = EndpointUrlListDataType()
        obj.EndpointUrlList = unpack_uatype_array('String', data)
        return obj

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
    def __init__(self):
        self.ServerUri = ''
        self.NetworkPaths = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('String', self.ServerUri))
        packet.append(struct.pack('<i', len(self.NetworkPaths)))
        for fieldname in self.NetworkPaths:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = NetworkGroupDataType()
        obj.ServerUri = unpack_uatype('String', data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.NetworkPaths.append(EndpointUrlListDataType.from_binary(data))
        return obj

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
    def __init__(self):
        self.SamplingInterval = 0
        self.MonitoredItemCount = 0
        self.MaxMonitoredItemCount = 0
        self.DisabledMonitoredItemCount = 0
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('Double', self.SamplingInterval))
        packet.append(pack_uatype('UInt32', self.MonitoredItemCount))
        packet.append(pack_uatype('UInt32', self.MaxMonitoredItemCount))
        packet.append(pack_uatype('UInt32', self.DisabledMonitoredItemCount))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = SamplingIntervalDiagnosticsDataType()
        obj.SamplingInterval = unpack_uatype('Double', data)
        obj.MonitoredItemCount = unpack_uatype('UInt32', data)
        obj.MaxMonitoredItemCount = unpack_uatype('UInt32', data)
        obj.DisabledMonitoredItemCount = unpack_uatype('UInt32', data)
        return obj

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
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('UInt32', self.ServerViewCount))
        packet.append(pack_uatype('UInt32', self.CurrentSessionCount))
        packet.append(pack_uatype('UInt32', self.CumulatedSessionCount))
        packet.append(pack_uatype('UInt32', self.SecurityRejectedSessionCount))
        packet.append(pack_uatype('UInt32', self.RejectedSessionCount))
        packet.append(pack_uatype('UInt32', self.SessionTimeoutCount))
        packet.append(pack_uatype('UInt32', self.SessionAbortCount))
        packet.append(pack_uatype('UInt32', self.CurrentSubscriptionCount))
        packet.append(pack_uatype('UInt32', self.CumulatedSubscriptionCount))
        packet.append(pack_uatype('UInt32', self.PublishingIntervalCount))
        packet.append(pack_uatype('UInt32', self.SecurityRejectedRequestsCount))
        packet.append(pack_uatype('UInt32', self.RejectedRequestsCount))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = ServerDiagnosticsSummaryDataType()
        obj.ServerViewCount = unpack_uatype('UInt32', data)
        obj.CurrentSessionCount = unpack_uatype('UInt32', data)
        obj.CumulatedSessionCount = unpack_uatype('UInt32', data)
        obj.SecurityRejectedSessionCount = unpack_uatype('UInt32', data)
        obj.RejectedSessionCount = unpack_uatype('UInt32', data)
        obj.SessionTimeoutCount = unpack_uatype('UInt32', data)
        obj.SessionAbortCount = unpack_uatype('UInt32', data)
        obj.CurrentSubscriptionCount = unpack_uatype('UInt32', data)
        obj.CumulatedSubscriptionCount = unpack_uatype('UInt32', data)
        obj.PublishingIntervalCount = unpack_uatype('UInt32', data)
        obj.SecurityRejectedRequestsCount = unpack_uatype('UInt32', data)
        obj.RejectedRequestsCount = unpack_uatype('UInt32', data)
        return obj

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
    def __init__(self):
        self.StartTime = datetime.now()
        self.CurrentTime = datetime.now()
        self.State = 0
        self.BuildInfo = BuildInfo()
        self.SecondsTillShutdown = 0
        self.ShutdownReason = LocalizedText()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('DateTime', self.StartTime))
        packet.append(pack_uatype('DateTime', self.CurrentTime))
        packet.append(pack_uatype('UInt32', self.State))
        packet.append(self.BuildInfo.to_binary())
        packet.append(pack_uatype('UInt32', self.SecondsTillShutdown))
        packet.append(self.ShutdownReason.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = ServerStatusDataType()
        obj.StartTime = unpack_uatype('DateTime', data)
        obj.CurrentTime = unpack_uatype('DateTime', data)
        obj.State = unpack_uatype('UInt32', data)
        obj.BuildInfo = BuildInfo.from_binary(data)
        obj.SecondsTillShutdown = unpack_uatype('UInt32', data)
        obj.ShutdownReason = LocalizedText.from_binary(data)
        return obj

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
    def __init__(self):
        self.SessionId = NodeId()
        self.SessionName = ''
        self.ClientDescription = ApplicationDescription()
        self.ServerUri = ''
        self.EndpointUrl = ''
        self.LocaleIds = []
        self.ActualSessionTimeout = 0
        self.MaxResponseMessageSize = 0
        self.ClientConnectionTime = datetime.now()
        self.ClientLastContactTime = datetime.now()
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
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.SessionId.to_binary())
        packet.append(pack_uatype('String', self.SessionName))
        packet.append(self.ClientDescription.to_binary())
        packet.append(pack_uatype('String', self.ServerUri))
        packet.append(pack_uatype('String', self.EndpointUrl))
        packet.append(struct.pack('<i', len(self.LocaleIds)))
        for fieldname in self.LocaleIds:
            packet.append(pack_uatype('String', fieldname))
        packet.append(pack_uatype('Double', self.ActualSessionTimeout))
        packet.append(pack_uatype('UInt32', self.MaxResponseMessageSize))
        packet.append(pack_uatype('DateTime', self.ClientConnectionTime))
        packet.append(pack_uatype('DateTime', self.ClientLastContactTime))
        packet.append(pack_uatype('UInt32', self.CurrentSubscriptionsCount))
        packet.append(pack_uatype('UInt32', self.CurrentMonitoredItemsCount))
        packet.append(pack_uatype('UInt32', self.CurrentPublishRequestsInQueue))
        packet.append(self.TotalRequestCount.to_binary())
        packet.append(pack_uatype('UInt32', self.UnauthorizedRequestCount))
        packet.append(self.ReadCount.to_binary())
        packet.append(self.HistoryReadCount.to_binary())
        packet.append(self.WriteCount.to_binary())
        packet.append(self.HistoryUpdateCount.to_binary())
        packet.append(self.CallCount.to_binary())
        packet.append(self.CreateMonitoredItemsCount.to_binary())
        packet.append(self.ModifyMonitoredItemsCount.to_binary())
        packet.append(self.SetMonitoringModeCount.to_binary())
        packet.append(self.SetTriggeringCount.to_binary())
        packet.append(self.DeleteMonitoredItemsCount.to_binary())
        packet.append(self.CreateSubscriptionCount.to_binary())
        packet.append(self.ModifySubscriptionCount.to_binary())
        packet.append(self.SetPublishingModeCount.to_binary())
        packet.append(self.PublishCount.to_binary())
        packet.append(self.RepublishCount.to_binary())
        packet.append(self.TransferSubscriptionsCount.to_binary())
        packet.append(self.DeleteSubscriptionsCount.to_binary())
        packet.append(self.AddNodesCount.to_binary())
        packet.append(self.AddReferencesCount.to_binary())
        packet.append(self.DeleteNodesCount.to_binary())
        packet.append(self.DeleteReferencesCount.to_binary())
        packet.append(self.BrowseCount.to_binary())
        packet.append(self.BrowseNextCount.to_binary())
        packet.append(self.TranslateBrowsePathsToNodeIdsCount.to_binary())
        packet.append(self.QueryFirstCount.to_binary())
        packet.append(self.QueryNextCount.to_binary())
        packet.append(self.RegisterNodesCount.to_binary())
        packet.append(self.UnregisterNodesCount.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = SessionDiagnosticsDataType()
        obj.SessionId = NodeId.from_binary(data)
        obj.SessionName = unpack_uatype('String', data)
        obj.ClientDescription = ApplicationDescription.from_binary(data)
        obj.ServerUri = unpack_uatype('String', data)
        obj.EndpointUrl = unpack_uatype('String', data)
        obj.LocaleIds = unpack_uatype_array('String', data)
        obj.ActualSessionTimeout = unpack_uatype('Double', data)
        obj.MaxResponseMessageSize = unpack_uatype('UInt32', data)
        obj.ClientConnectionTime = unpack_uatype('DateTime', data)
        obj.ClientLastContactTime = unpack_uatype('DateTime', data)
        obj.CurrentSubscriptionsCount = unpack_uatype('UInt32', data)
        obj.CurrentMonitoredItemsCount = unpack_uatype('UInt32', data)
        obj.CurrentPublishRequestsInQueue = unpack_uatype('UInt32', data)
        obj.TotalRequestCount = ServiceCounterDataType.from_binary(data)
        obj.UnauthorizedRequestCount = unpack_uatype('UInt32', data)
        obj.ReadCount = ServiceCounterDataType.from_binary(data)
        obj.HistoryReadCount = ServiceCounterDataType.from_binary(data)
        obj.WriteCount = ServiceCounterDataType.from_binary(data)
        obj.HistoryUpdateCount = ServiceCounterDataType.from_binary(data)
        obj.CallCount = ServiceCounterDataType.from_binary(data)
        obj.CreateMonitoredItemsCount = ServiceCounterDataType.from_binary(data)
        obj.ModifyMonitoredItemsCount = ServiceCounterDataType.from_binary(data)
        obj.SetMonitoringModeCount = ServiceCounterDataType.from_binary(data)
        obj.SetTriggeringCount = ServiceCounterDataType.from_binary(data)
        obj.DeleteMonitoredItemsCount = ServiceCounterDataType.from_binary(data)
        obj.CreateSubscriptionCount = ServiceCounterDataType.from_binary(data)
        obj.ModifySubscriptionCount = ServiceCounterDataType.from_binary(data)
        obj.SetPublishingModeCount = ServiceCounterDataType.from_binary(data)
        obj.PublishCount = ServiceCounterDataType.from_binary(data)
        obj.RepublishCount = ServiceCounterDataType.from_binary(data)
        obj.TransferSubscriptionsCount = ServiceCounterDataType.from_binary(data)
        obj.DeleteSubscriptionsCount = ServiceCounterDataType.from_binary(data)
        obj.AddNodesCount = ServiceCounterDataType.from_binary(data)
        obj.AddReferencesCount = ServiceCounterDataType.from_binary(data)
        obj.DeleteNodesCount = ServiceCounterDataType.from_binary(data)
        obj.DeleteReferencesCount = ServiceCounterDataType.from_binary(data)
        obj.BrowseCount = ServiceCounterDataType.from_binary(data)
        obj.BrowseNextCount = ServiceCounterDataType.from_binary(data)
        obj.TranslateBrowsePathsToNodeIdsCount = ServiceCounterDataType.from_binary(data)
        obj.QueryFirstCount = ServiceCounterDataType.from_binary(data)
        obj.QueryNextCount = ServiceCounterDataType.from_binary(data)
        obj.RegisterNodesCount = ServiceCounterDataType.from_binary(data)
        obj.UnregisterNodesCount = ServiceCounterDataType.from_binary(data)
        return obj

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
    def __init__(self):
        self.SessionId = NodeId()
        self.ClientUserIdOfSession = ''
        self.ClientUserIdHistory = []
        self.AuthenticationMechanism = ''
        self.Encoding = ''
        self.TransportProtocol = ''
        self.SecurityMode = 0
        self.SecurityPolicyUri = ''
        self.ClientCertificate = b''
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.SessionId.to_binary())
        packet.append(pack_uatype('String', self.ClientUserIdOfSession))
        packet.append(struct.pack('<i', len(self.ClientUserIdHistory)))
        for fieldname in self.ClientUserIdHistory:
            packet.append(pack_uatype('String', fieldname))
        packet.append(pack_uatype('String', self.AuthenticationMechanism))
        packet.append(pack_uatype('String', self.Encoding))
        packet.append(pack_uatype('String', self.TransportProtocol))
        packet.append(pack_uatype('UInt32', self.SecurityMode))
        packet.append(pack_uatype('String', self.SecurityPolicyUri))
        packet.append(pack_uatype('ByteString', self.ClientCertificate))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = SessionSecurityDiagnosticsDataType()
        obj.SessionId = NodeId.from_binary(data)
        obj.ClientUserIdOfSession = unpack_uatype('String', data)
        obj.ClientUserIdHistory = unpack_uatype_array('String', data)
        obj.AuthenticationMechanism = unpack_uatype('String', data)
        obj.Encoding = unpack_uatype('String', data)
        obj.TransportProtocol = unpack_uatype('String', data)
        obj.SecurityMode = unpack_uatype('UInt32', data)
        obj.SecurityPolicyUri = unpack_uatype('String', data)
        obj.ClientCertificate = unpack_uatype('ByteString', data)
        return obj

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
    def __init__(self):
        self.TotalCount = 0
        self.ErrorCount = 0
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('UInt32', self.TotalCount))
        packet.append(pack_uatype('UInt32', self.ErrorCount))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = ServiceCounterDataType()
        obj.TotalCount = unpack_uatype('UInt32', data)
        obj.ErrorCount = unpack_uatype('UInt32', data)
        return obj

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
    def __init__(self):
        self.StatusCode = StatusCode()
        self.DiagnosticInfo = DiagnosticInfo()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.StatusCode.to_binary())
        packet.append(self.DiagnosticInfo.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = StatusResult()
        obj.StatusCode = StatusCode.from_binary(data)
        obj.DiagnosticInfo = DiagnosticInfo.from_binary(data)
        return obj

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
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.SessionId.to_binary())
        packet.append(pack_uatype('UInt32', self.SubscriptionId))
        packet.append(pack_uatype('Byte', self.Priority))
        packet.append(pack_uatype('Double', self.PublishingInterval))
        packet.append(pack_uatype('UInt32', self.MaxKeepAliveCount))
        packet.append(pack_uatype('UInt32', self.MaxLifetimeCount))
        packet.append(pack_uatype('UInt32', self.MaxNotificationsPerPublish))
        packet.append(pack_uatype('Boolean', self.PublishingEnabled))
        packet.append(pack_uatype('UInt32', self.ModifyCount))
        packet.append(pack_uatype('UInt32', self.EnableCount))
        packet.append(pack_uatype('UInt32', self.DisableCount))
        packet.append(pack_uatype('UInt32', self.RepublishRequestCount))
        packet.append(pack_uatype('UInt32', self.RepublishMessageRequestCount))
        packet.append(pack_uatype('UInt32', self.RepublishMessageCount))
        packet.append(pack_uatype('UInt32', self.TransferRequestCount))
        packet.append(pack_uatype('UInt32', self.TransferredToAltClientCount))
        packet.append(pack_uatype('UInt32', self.TransferredToSameClientCount))
        packet.append(pack_uatype('UInt32', self.PublishRequestCount))
        packet.append(pack_uatype('UInt32', self.DataChangeNotificationsCount))
        packet.append(pack_uatype('UInt32', self.EventNotificationsCount))
        packet.append(pack_uatype('UInt32', self.NotificationsCount))
        packet.append(pack_uatype('UInt32', self.LatePublishRequestCount))
        packet.append(pack_uatype('UInt32', self.CurrentKeepAliveCount))
        packet.append(pack_uatype('UInt32', self.CurrentLifetimeCount))
        packet.append(pack_uatype('UInt32', self.UnacknowledgedMessageCount))
        packet.append(pack_uatype('UInt32', self.DiscardedMessageCount))
        packet.append(pack_uatype('UInt32', self.MonitoredItemCount))
        packet.append(pack_uatype('UInt32', self.DisabledMonitoredItemCount))
        packet.append(pack_uatype('UInt32', self.MonitoringQueueOverflowCount))
        packet.append(pack_uatype('UInt32', self.NextSequenceNumber))
        packet.append(pack_uatype('UInt32', self.EventQueueOverFlowCount))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = SubscriptionDiagnosticsDataType()
        obj.SessionId = NodeId.from_binary(data)
        obj.SubscriptionId = unpack_uatype('UInt32', data)
        obj.Priority = unpack_uatype('Byte', data)
        obj.PublishingInterval = unpack_uatype('Double', data)
        obj.MaxKeepAliveCount = unpack_uatype('UInt32', data)
        obj.MaxLifetimeCount = unpack_uatype('UInt32', data)
        obj.MaxNotificationsPerPublish = unpack_uatype('UInt32', data)
        obj.PublishingEnabled = unpack_uatype('Boolean', data)
        obj.ModifyCount = unpack_uatype('UInt32', data)
        obj.EnableCount = unpack_uatype('UInt32', data)
        obj.DisableCount = unpack_uatype('UInt32', data)
        obj.RepublishRequestCount = unpack_uatype('UInt32', data)
        obj.RepublishMessageRequestCount = unpack_uatype('UInt32', data)
        obj.RepublishMessageCount = unpack_uatype('UInt32', data)
        obj.TransferRequestCount = unpack_uatype('UInt32', data)
        obj.TransferredToAltClientCount = unpack_uatype('UInt32', data)
        obj.TransferredToSameClientCount = unpack_uatype('UInt32', data)
        obj.PublishRequestCount = unpack_uatype('UInt32', data)
        obj.DataChangeNotificationsCount = unpack_uatype('UInt32', data)
        obj.EventNotificationsCount = unpack_uatype('UInt32', data)
        obj.NotificationsCount = unpack_uatype('UInt32', data)
        obj.LatePublishRequestCount = unpack_uatype('UInt32', data)
        obj.CurrentKeepAliveCount = unpack_uatype('UInt32', data)
        obj.CurrentLifetimeCount = unpack_uatype('UInt32', data)
        obj.UnacknowledgedMessageCount = unpack_uatype('UInt32', data)
        obj.DiscardedMessageCount = unpack_uatype('UInt32', data)
        obj.MonitoredItemCount = unpack_uatype('UInt32', data)
        obj.DisabledMonitoredItemCount = unpack_uatype('UInt32', data)
        obj.MonitoringQueueOverflowCount = unpack_uatype('UInt32', data)
        obj.NextSequenceNumber = unpack_uatype('UInt32', data)
        obj.EventQueueOverFlowCount = unpack_uatype('UInt32', data)
        return obj

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
    def __init__(self):
        self.Affected = NodeId()
        self.AffectedType = NodeId()
        self.Verb = 0
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.Affected.to_binary())
        packet.append(self.AffectedType.to_binary())
        packet.append(pack_uatype('Byte', self.Verb))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = ModelChangeStructureDataType()
        obj.Affected = NodeId.from_binary(data)
        obj.AffectedType = NodeId.from_binary(data)
        obj.Verb = unpack_uatype('Byte', data)
        return obj

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
    def __init__(self):
        self.Affected = NodeId()
        self.AffectedType = NodeId()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.Affected.to_binary())
        packet.append(self.AffectedType.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = SemanticChangeStructureDataType()
        obj.Affected = NodeId.from_binary(data)
        obj.AffectedType = NodeId.from_binary(data)
        return obj

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
    def __init__(self):
        self.Low = 0
        self.High = 0
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('Double', self.Low))
        packet.append(pack_uatype('Double', self.High))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = Range()
        obj.Low = unpack_uatype('Double', data)
        obj.High = unpack_uatype('Double', data)
        return obj

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
    def __init__(self):
        self.NamespaceUri = ''
        self.UnitId = 0
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('String', self.NamespaceUri))
        packet.append(pack_uatype('Int32', self.UnitId))
        packet.append(self.DisplayName.to_binary())
        packet.append(self.Description.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = EUInformation()
        obj.NamespaceUri = unpack_uatype('String', data)
        obj.UnitId = unpack_uatype('Int32', data)
        obj.DisplayName = LocalizedText.from_binary(data)
        obj.Description = LocalizedText.from_binary(data)
        return obj

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
    def __init__(self):
        self.Real = 0
        self.Imaginary = 0
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('Float', self.Real))
        packet.append(pack_uatype('Float', self.Imaginary))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = ComplexNumberType()
        obj.Real = unpack_uatype('Float', data)
        obj.Imaginary = unpack_uatype('Float', data)
        return obj

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
    def __init__(self):
        self.Real = 0
        self.Imaginary = 0
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('Double', self.Real))
        packet.append(pack_uatype('Double', self.Imaginary))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = DoubleComplexNumberType()
        obj.Real = unpack_uatype('Double', data)
        obj.Imaginary = unpack_uatype('Double', data)
        return obj

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
    def __init__(self):
        self.EngineeringUnits = EUInformation()
        self.EURange = Range()
        self.Title = LocalizedText()
        self.AxisScaleType = 0
        self.AxisSteps = []
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.EngineeringUnits.to_binary())
        packet.append(self.EURange.to_binary())
        packet.append(self.Title.to_binary())
        packet.append(pack_uatype('UInt32', self.AxisScaleType))
        packet.append(struct.pack('<i', len(self.AxisSteps)))
        for fieldname in self.AxisSteps:
            packet.append(pack_uatype('Double', fieldname))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = AxisInformation()
        obj.EngineeringUnits = EUInformation.from_binary(data)
        obj.EURange = Range.from_binary(data)
        obj.Title = LocalizedText.from_binary(data)
        obj.AxisScaleType = unpack_uatype('UInt32', data)
        obj.AxisSteps = unpack_uatype_array('Double', data)
        return obj

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
    def __init__(self):
        self.X = 0
        self.Value = 0
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('Double', self.X))
        packet.append(pack_uatype('Float', self.Value))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = XVType()
        obj.X = unpack_uatype('Double', data)
        obj.Value = unpack_uatype('Float', data)
        return obj

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
    def __init__(self):
        self.CreateSessionId = NodeId()
        self.CreateClientName = ''
        self.InvocationCreationTime = datetime.now()
        self.LastTransitionTime = datetime.now()
        self.LastMethodCall = ''
        self.LastMethodSessionId = NodeId()
        self.LastMethodInputArguments = []
        self.LastMethodOutputArguments = []
        self.LastMethodCallTime = datetime.now()
        self.LastMethodReturnStatus = StatusResult()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(self.CreateSessionId.to_binary())
        packet.append(pack_uatype('String', self.CreateClientName))
        packet.append(pack_uatype('DateTime', self.InvocationCreationTime))
        packet.append(pack_uatype('DateTime', self.LastTransitionTime))
        packet.append(pack_uatype('String', self.LastMethodCall))
        packet.append(self.LastMethodSessionId.to_binary())
        packet.append(struct.pack('<i', len(self.LastMethodInputArguments)))
        for fieldname in self.LastMethodInputArguments:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.LastMethodOutputArguments)))
        for fieldname in self.LastMethodOutputArguments:
            packet.append(fieldname.to_binary())
        packet.append(pack_uatype('DateTime', self.LastMethodCallTime))
        packet.append(self.LastMethodReturnStatus.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = ProgramDiagnosticDataType()
        obj.CreateSessionId = NodeId.from_binary(data)
        obj.CreateClientName = unpack_uatype('String', data)
        obj.InvocationCreationTime = unpack_uatype('DateTime', data)
        obj.LastTransitionTime = unpack_uatype('DateTime', data)
        obj.LastMethodCall = unpack_uatype('String', data)
        obj.LastMethodSessionId = NodeId.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.LastMethodInputArguments.append(Argument.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for _ in range(0, length):
                obj.LastMethodOutputArguments.append(Argument.from_binary(data))
        obj.LastMethodCallTime = unpack_uatype('DateTime', data)
        obj.LastMethodReturnStatus = StatusResult.from_binary(data)
        return obj

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


class Annotation(FrozenClass):
    '''
    :ivar Message:
    :vartype Message: String
    :ivar UserName:
    :vartype UserName: String
    :ivar AnnotationTime:
    :vartype AnnotationTime: DateTime
    '''
    def __init__(self):
        self.Message = ''
        self.UserName = ''
        self.AnnotationTime = datetime.now()
        self._freeze()

    def to_binary(self):
        packet = []
        packet.append(pack_uatype('String', self.Message))
        packet.append(pack_uatype('String', self.UserName))
        packet.append(pack_uatype('DateTime', self.AnnotationTime))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        obj = Annotation()
        obj.Message = unpack_uatype('String', data)
        obj.UserName = unpack_uatype('String', data)
        obj.AnnotationTime = unpack_uatype('DateTime', data)
        return obj

    def __str__(self):
        return 'Annotation(' + 'Message:' + str(self.Message) + ', ' + \
               'UserName:' + str(self.UserName) + ', ' + \
               'AnnotationTime:' + str(self.AnnotationTime) + ')'

    __repr__ = __str__


ExtensionClasses = {
    ObjectIds.TrustListDataType_Encoding_DefaultBinary: TrustListDataType,
    ObjectIds.Argument_Encoding_DefaultBinary: Argument,
    ObjectIds.EnumValueType_Encoding_DefaultBinary: EnumValueType,
    ObjectIds.OptionSet_Encoding_DefaultBinary: OptionSet,
    ObjectIds.Union_Encoding_DefaultBinary: Union,
    ObjectIds.TimeZoneDataType_Encoding_DefaultBinary: TimeZoneDataType,
    ObjectIds.ApplicationDescription_Encoding_DefaultBinary: ApplicationDescription,
    ObjectIds.RequestHeader_Encoding_DefaultBinary: RequestHeader,
    ObjectIds.ResponseHeader_Encoding_DefaultBinary: ResponseHeader,
    ObjectIds.ServiceFault_Encoding_DefaultBinary: ServiceFault,
    ObjectIds.FindServersRequest_Encoding_DefaultBinary: FindServersRequest,
    ObjectIds.FindServersResponse_Encoding_DefaultBinary: FindServersResponse,
    ObjectIds.ServerOnNetwork_Encoding_DefaultBinary: ServerOnNetwork,
    ObjectIds.FindServersOnNetworkRequest_Encoding_DefaultBinary: FindServersOnNetworkRequest,
    ObjectIds.FindServersOnNetworkResponse_Encoding_DefaultBinary: FindServersOnNetworkResponse,
    ObjectIds.UserTokenPolicy_Encoding_DefaultBinary: UserTokenPolicy,
    ObjectIds.EndpointDescription_Encoding_DefaultBinary: EndpointDescription,
    ObjectIds.GetEndpointsRequest_Encoding_DefaultBinary: GetEndpointsRequest,
    ObjectIds.GetEndpointsResponse_Encoding_DefaultBinary: GetEndpointsResponse,
    ObjectIds.RegisteredServer_Encoding_DefaultBinary: RegisteredServer,
    ObjectIds.RegisterServerRequest_Encoding_DefaultBinary: RegisterServerRequest,
    ObjectIds.RegisterServerResponse_Encoding_DefaultBinary: RegisterServerResponse,
    ObjectIds.DiscoveryConfiguration_Encoding_DefaultBinary: DiscoveryConfiguration,
    ObjectIds.MdnsDiscoveryConfiguration_Encoding_DefaultBinary: MdnsDiscoveryConfiguration,
    ObjectIds.RegisterServer2Request_Encoding_DefaultBinary: RegisterServer2Request,
    ObjectIds.RegisterServer2Response_Encoding_DefaultBinary: RegisterServer2Response,
    ObjectIds.ChannelSecurityToken_Encoding_DefaultBinary: ChannelSecurityToken,
    ObjectIds.OpenSecureChannelRequest_Encoding_DefaultBinary: OpenSecureChannelRequest,
    ObjectIds.OpenSecureChannelResponse_Encoding_DefaultBinary: OpenSecureChannelResponse,
    ObjectIds.CloseSecureChannelRequest_Encoding_DefaultBinary: CloseSecureChannelRequest,
    ObjectIds.CloseSecureChannelResponse_Encoding_DefaultBinary: CloseSecureChannelResponse,
    ObjectIds.SignedSoftwareCertificate_Encoding_DefaultBinary: SignedSoftwareCertificate,
    ObjectIds.SignatureData_Encoding_DefaultBinary: SignatureData,
    ObjectIds.CreateSessionRequest_Encoding_DefaultBinary: CreateSessionRequest,
    ObjectIds.CreateSessionResponse_Encoding_DefaultBinary: CreateSessionResponse,
    ObjectIds.UserIdentityToken_Encoding_DefaultBinary: UserIdentityToken,
    ObjectIds.AnonymousIdentityToken_Encoding_DefaultBinary: AnonymousIdentityToken,
    ObjectIds.UserNameIdentityToken_Encoding_DefaultBinary: UserNameIdentityToken,
    ObjectIds.X509IdentityToken_Encoding_DefaultBinary: X509IdentityToken,
    ObjectIds.KerberosIdentityToken_Encoding_DefaultBinary: KerberosIdentityToken,
    ObjectIds.IssuedIdentityToken_Encoding_DefaultBinary: IssuedIdentityToken,
    ObjectIds.ActivateSessionRequest_Encoding_DefaultBinary: ActivateSessionRequest,
    ObjectIds.ActivateSessionResponse_Encoding_DefaultBinary: ActivateSessionResponse,
    ObjectIds.CloseSessionRequest_Encoding_DefaultBinary: CloseSessionRequest,
    ObjectIds.CloseSessionResponse_Encoding_DefaultBinary: CloseSessionResponse,
    ObjectIds.CancelRequest_Encoding_DefaultBinary: CancelRequest,
    ObjectIds.CancelResponse_Encoding_DefaultBinary: CancelResponse,
    ObjectIds.NodeAttributes_Encoding_DefaultBinary: NodeAttributes,
    ObjectIds.ObjectAttributes_Encoding_DefaultBinary: ObjectAttributes,
    ObjectIds.VariableAttributes_Encoding_DefaultBinary: VariableAttributes,
    ObjectIds.MethodAttributes_Encoding_DefaultBinary: MethodAttributes,
    ObjectIds.ObjectTypeAttributes_Encoding_DefaultBinary: ObjectTypeAttributes,
    ObjectIds.VariableTypeAttributes_Encoding_DefaultBinary: VariableTypeAttributes,
    ObjectIds.ReferenceTypeAttributes_Encoding_DefaultBinary: ReferenceTypeAttributes,
    ObjectIds.DataTypeAttributes_Encoding_DefaultBinary: DataTypeAttributes,
    ObjectIds.ViewAttributes_Encoding_DefaultBinary: ViewAttributes,
    ObjectIds.AddNodesItem_Encoding_DefaultBinary: AddNodesItem,
    ObjectIds.AddNodesResult_Encoding_DefaultBinary: AddNodesResult,
    ObjectIds.AddNodesRequest_Encoding_DefaultBinary: AddNodesRequest,
    ObjectIds.AddNodesResponse_Encoding_DefaultBinary: AddNodesResponse,
    ObjectIds.AddReferencesItem_Encoding_DefaultBinary: AddReferencesItem,
    ObjectIds.AddReferencesRequest_Encoding_DefaultBinary: AddReferencesRequest,
    ObjectIds.AddReferencesResponse_Encoding_DefaultBinary: AddReferencesResponse,
    ObjectIds.DeleteNodesItem_Encoding_DefaultBinary: DeleteNodesItem,
    ObjectIds.DeleteNodesRequest_Encoding_DefaultBinary: DeleteNodesRequest,
    ObjectIds.DeleteNodesResponse_Encoding_DefaultBinary: DeleteNodesResponse,
    ObjectIds.DeleteReferencesItem_Encoding_DefaultBinary: DeleteReferencesItem,
    ObjectIds.DeleteReferencesRequest_Encoding_DefaultBinary: DeleteReferencesRequest,
    ObjectIds.DeleteReferencesResponse_Encoding_DefaultBinary: DeleteReferencesResponse,
    ObjectIds.ViewDescription_Encoding_DefaultBinary: ViewDescription,
    ObjectIds.BrowseDescription_Encoding_DefaultBinary: BrowseDescription,
    ObjectIds.ReferenceDescription_Encoding_DefaultBinary: ReferenceDescription,
    ObjectIds.BrowseResult_Encoding_DefaultBinary: BrowseResult,
    ObjectIds.BrowseRequest_Encoding_DefaultBinary: BrowseRequest,
    ObjectIds.BrowseResponse_Encoding_DefaultBinary: BrowseResponse,
    ObjectIds.BrowseNextRequest_Encoding_DefaultBinary: BrowseNextRequest,
    ObjectIds.BrowseNextResponse_Encoding_DefaultBinary: BrowseNextResponse,
    ObjectIds.RelativePathElement_Encoding_DefaultBinary: RelativePathElement,
    ObjectIds.RelativePath_Encoding_DefaultBinary: RelativePath,
    ObjectIds.BrowsePath_Encoding_DefaultBinary: BrowsePath,
    ObjectIds.BrowsePathTarget_Encoding_DefaultBinary: BrowsePathTarget,
    ObjectIds.BrowsePathResult_Encoding_DefaultBinary: BrowsePathResult,
    ObjectIds.TranslateBrowsePathsToNodeIdsRequest_Encoding_DefaultBinary: TranslateBrowsePathsToNodeIdsRequest,
    ObjectIds.TranslateBrowsePathsToNodeIdsResponse_Encoding_DefaultBinary: TranslateBrowsePathsToNodeIdsResponse,
    ObjectIds.RegisterNodesRequest_Encoding_DefaultBinary: RegisterNodesRequest,
    ObjectIds.RegisterNodesResponse_Encoding_DefaultBinary: RegisterNodesResponse,
    ObjectIds.UnregisterNodesRequest_Encoding_DefaultBinary: UnregisterNodesRequest,
    ObjectIds.UnregisterNodesResponse_Encoding_DefaultBinary: UnregisterNodesResponse,
    ObjectIds.EndpointConfiguration_Encoding_DefaultBinary: EndpointConfiguration,
    ObjectIds.SupportedProfile_Encoding_DefaultBinary: SupportedProfile,
    ObjectIds.SoftwareCertificate_Encoding_DefaultBinary: SoftwareCertificate,
    ObjectIds.QueryDataDescription_Encoding_DefaultBinary: QueryDataDescription,
    ObjectIds.NodeTypeDescription_Encoding_DefaultBinary: NodeTypeDescription,
    ObjectIds.QueryDataSet_Encoding_DefaultBinary: QueryDataSet,
    ObjectIds.NodeReference_Encoding_DefaultBinary: NodeReference,
    ObjectIds.ContentFilterElement_Encoding_DefaultBinary: ContentFilterElement,
    ObjectIds.ContentFilter_Encoding_DefaultBinary: ContentFilter,
    ObjectIds.ElementOperand_Encoding_DefaultBinary: ElementOperand,
    ObjectIds.LiteralOperand_Encoding_DefaultBinary: LiteralOperand,
    ObjectIds.AttributeOperand_Encoding_DefaultBinary: AttributeOperand,
    ObjectIds.SimpleAttributeOperand_Encoding_DefaultBinary: SimpleAttributeOperand,
    ObjectIds.ContentFilterElementResult_Encoding_DefaultBinary: ContentFilterElementResult,
    ObjectIds.ContentFilterResult_Encoding_DefaultBinary: ContentFilterResult,
    ObjectIds.ParsingResult_Encoding_DefaultBinary: ParsingResult,
    ObjectIds.QueryFirstRequest_Encoding_DefaultBinary: QueryFirstRequest,
    ObjectIds.QueryFirstResponse_Encoding_DefaultBinary: QueryFirstResponse,
    ObjectIds.QueryNextRequest_Encoding_DefaultBinary: QueryNextRequest,
    ObjectIds.QueryNextResponse_Encoding_DefaultBinary: QueryNextResponse,
    ObjectIds.ReadValueId_Encoding_DefaultBinary: ReadValueId,
    ObjectIds.ReadRequest_Encoding_DefaultBinary: ReadRequest,
    ObjectIds.ReadResponse_Encoding_DefaultBinary: ReadResponse,
    ObjectIds.HistoryReadValueId_Encoding_DefaultBinary: HistoryReadValueId,
    ObjectIds.HistoryReadResult_Encoding_DefaultBinary: HistoryReadResult,
    ObjectIds.HistoryReadDetails_Encoding_DefaultBinary: HistoryReadDetails,
    ObjectIds.ReadEventDetails_Encoding_DefaultBinary: ReadEventDetails,
    ObjectIds.ReadRawModifiedDetails_Encoding_DefaultBinary: ReadRawModifiedDetails,
    ObjectIds.ReadProcessedDetails_Encoding_DefaultBinary: ReadProcessedDetails,
    ObjectIds.ReadAtTimeDetails_Encoding_DefaultBinary: ReadAtTimeDetails,
    ObjectIds.HistoryData_Encoding_DefaultBinary: HistoryData,
    ObjectIds.ModificationInfo_Encoding_DefaultBinary: ModificationInfo,
    ObjectIds.HistoryModifiedData_Encoding_DefaultBinary: HistoryModifiedData,
    ObjectIds.HistoryEvent_Encoding_DefaultBinary: HistoryEvent,
    ObjectIds.HistoryReadRequest_Encoding_DefaultBinary: HistoryReadRequest,
    ObjectIds.HistoryReadResponse_Encoding_DefaultBinary: HistoryReadResponse,
    ObjectIds.WriteValue_Encoding_DefaultBinary: WriteValue,
    ObjectIds.WriteRequest_Encoding_DefaultBinary: WriteRequest,
    ObjectIds.WriteResponse_Encoding_DefaultBinary: WriteResponse,
    ObjectIds.HistoryUpdateDetails_Encoding_DefaultBinary: HistoryUpdateDetails,
    ObjectIds.UpdateDataDetails_Encoding_DefaultBinary: UpdateDataDetails,
    ObjectIds.UpdateStructureDataDetails_Encoding_DefaultBinary: UpdateStructureDataDetails,
    ObjectIds.UpdateEventDetails_Encoding_DefaultBinary: UpdateEventDetails,
    ObjectIds.DeleteRawModifiedDetails_Encoding_DefaultBinary: DeleteRawModifiedDetails,
    ObjectIds.DeleteAtTimeDetails_Encoding_DefaultBinary: DeleteAtTimeDetails,
    ObjectIds.DeleteEventDetails_Encoding_DefaultBinary: DeleteEventDetails,
    ObjectIds.HistoryUpdateResult_Encoding_DefaultBinary: HistoryUpdateResult,
    ObjectIds.HistoryUpdateRequest_Encoding_DefaultBinary: HistoryUpdateRequest,
    ObjectIds.HistoryUpdateResponse_Encoding_DefaultBinary: HistoryUpdateResponse,
    ObjectIds.CallMethodRequest_Encoding_DefaultBinary: CallMethodRequest,
    ObjectIds.CallMethodResult_Encoding_DefaultBinary: CallMethodResult,
    ObjectIds.CallRequest_Encoding_DefaultBinary: CallRequest,
    ObjectIds.CallResponse_Encoding_DefaultBinary: CallResponse,
    ObjectIds.MonitoringFilter_Encoding_DefaultBinary: MonitoringFilter,
    ObjectIds.DataChangeFilter_Encoding_DefaultBinary: DataChangeFilter,
    ObjectIds.EventFilter_Encoding_DefaultBinary: EventFilter,
    ObjectIds.AggregateConfiguration_Encoding_DefaultBinary: AggregateConfiguration,
    ObjectIds.AggregateFilter_Encoding_DefaultBinary: AggregateFilter,
    ObjectIds.MonitoringFilterResult_Encoding_DefaultBinary: MonitoringFilterResult,
    ObjectIds.EventFilterResult_Encoding_DefaultBinary: EventFilterResult,
    ObjectIds.AggregateFilterResult_Encoding_DefaultBinary: AggregateFilterResult,
    ObjectIds.MonitoringParameters_Encoding_DefaultBinary: MonitoringParameters,
    ObjectIds.MonitoredItemCreateRequest_Encoding_DefaultBinary: MonitoredItemCreateRequest,
    ObjectIds.MonitoredItemCreateResult_Encoding_DefaultBinary: MonitoredItemCreateResult,
    ObjectIds.CreateMonitoredItemsRequest_Encoding_DefaultBinary: CreateMonitoredItemsRequest,
    ObjectIds.CreateMonitoredItemsResponse_Encoding_DefaultBinary: CreateMonitoredItemsResponse,
    ObjectIds.MonitoredItemModifyRequest_Encoding_DefaultBinary: MonitoredItemModifyRequest,
    ObjectIds.MonitoredItemModifyResult_Encoding_DefaultBinary: MonitoredItemModifyResult,
    ObjectIds.ModifyMonitoredItemsRequest_Encoding_DefaultBinary: ModifyMonitoredItemsRequest,
    ObjectIds.ModifyMonitoredItemsResponse_Encoding_DefaultBinary: ModifyMonitoredItemsResponse,
    ObjectIds.SetMonitoringModeRequest_Encoding_DefaultBinary: SetMonitoringModeRequest,
    ObjectIds.SetMonitoringModeResponse_Encoding_DefaultBinary: SetMonitoringModeResponse,
    ObjectIds.SetTriggeringRequest_Encoding_DefaultBinary: SetTriggeringRequest,
    ObjectIds.SetTriggeringResponse_Encoding_DefaultBinary: SetTriggeringResponse,
    ObjectIds.DeleteMonitoredItemsRequest_Encoding_DefaultBinary: DeleteMonitoredItemsRequest,
    ObjectIds.DeleteMonitoredItemsResponse_Encoding_DefaultBinary: DeleteMonitoredItemsResponse,
    ObjectIds.CreateSubscriptionRequest_Encoding_DefaultBinary: CreateSubscriptionRequest,
    ObjectIds.CreateSubscriptionResponse_Encoding_DefaultBinary: CreateSubscriptionResponse,
    ObjectIds.ModifySubscriptionRequest_Encoding_DefaultBinary: ModifySubscriptionRequest,
    ObjectIds.ModifySubscriptionResponse_Encoding_DefaultBinary: ModifySubscriptionResponse,
    ObjectIds.SetPublishingModeRequest_Encoding_DefaultBinary: SetPublishingModeRequest,
    ObjectIds.SetPublishingModeResponse_Encoding_DefaultBinary: SetPublishingModeResponse,
    ObjectIds.NotificationMessage_Encoding_DefaultBinary: NotificationMessage,
    ObjectIds.NotificationData_Encoding_DefaultBinary: NotificationData,
    ObjectIds.DataChangeNotification_Encoding_DefaultBinary: DataChangeNotification,
    ObjectIds.MonitoredItemNotification_Encoding_DefaultBinary: MonitoredItemNotification,
    ObjectIds.EventNotificationList_Encoding_DefaultBinary: EventNotificationList,
    ObjectIds.EventFieldList_Encoding_DefaultBinary: EventFieldList,
    ObjectIds.HistoryEventFieldList_Encoding_DefaultBinary: HistoryEventFieldList,
    ObjectIds.StatusChangeNotification_Encoding_DefaultBinary: StatusChangeNotification,
    ObjectIds.SubscriptionAcknowledgement_Encoding_DefaultBinary: SubscriptionAcknowledgement,
    ObjectIds.PublishRequest_Encoding_DefaultBinary: PublishRequest,
    ObjectIds.PublishResponse_Encoding_DefaultBinary: PublishResponse,
    ObjectIds.RepublishRequest_Encoding_DefaultBinary: RepublishRequest,
    ObjectIds.RepublishResponse_Encoding_DefaultBinary: RepublishResponse,
    ObjectIds.TransferResult_Encoding_DefaultBinary: TransferResult,
    ObjectIds.TransferSubscriptionsRequest_Encoding_DefaultBinary: TransferSubscriptionsRequest,
    ObjectIds.TransferSubscriptionsResponse_Encoding_DefaultBinary: TransferSubscriptionsResponse,
    ObjectIds.DeleteSubscriptionsRequest_Encoding_DefaultBinary: DeleteSubscriptionsRequest,
    ObjectIds.DeleteSubscriptionsResponse_Encoding_DefaultBinary: DeleteSubscriptionsResponse,
    ObjectIds.BuildInfo_Encoding_DefaultBinary: BuildInfo,
    ObjectIds.RedundantServerDataType_Encoding_DefaultBinary: RedundantServerDataType,
    ObjectIds.EndpointUrlListDataType_Encoding_DefaultBinary: EndpointUrlListDataType,
    ObjectIds.NetworkGroupDataType_Encoding_DefaultBinary: NetworkGroupDataType,
    ObjectIds.SamplingIntervalDiagnosticsDataType_Encoding_DefaultBinary: SamplingIntervalDiagnosticsDataType,
    ObjectIds.ServerDiagnosticsSummaryDataType_Encoding_DefaultBinary: ServerDiagnosticsSummaryDataType,
    ObjectIds.ServerStatusDataType_Encoding_DefaultBinary: ServerStatusDataType,
    ObjectIds.SessionDiagnosticsDataType_Encoding_DefaultBinary: SessionDiagnosticsDataType,
    ObjectIds.SessionSecurityDiagnosticsDataType_Encoding_DefaultBinary: SessionSecurityDiagnosticsDataType,
    ObjectIds.ServiceCounterDataType_Encoding_DefaultBinary: ServiceCounterDataType,
    ObjectIds.StatusResult_Encoding_DefaultBinary: StatusResult,
    ObjectIds.SubscriptionDiagnosticsDataType_Encoding_DefaultBinary: SubscriptionDiagnosticsDataType,
    ObjectIds.ModelChangeStructureDataType_Encoding_DefaultBinary: ModelChangeStructureDataType,
    ObjectIds.SemanticChangeStructureDataType_Encoding_DefaultBinary: SemanticChangeStructureDataType,
    ObjectIds.Range_Encoding_DefaultBinary: Range,
    ObjectIds.EUInformation_Encoding_DefaultBinary: EUInformation,
    ObjectIds.ComplexNumberType_Encoding_DefaultBinary: ComplexNumberType,
    ObjectIds.DoubleComplexNumberType_Encoding_DefaultBinary: DoubleComplexNumberType,
    ObjectIds.AxisInformation_Encoding_DefaultBinary: AxisInformation,
    ObjectIds.XVType_Encoding_DefaultBinary: XVType,
    ObjectIds.ProgramDiagnosticDataType_Encoding_DefaultBinary: ProgramDiagnosticDataType,
    ObjectIds.Annotation_Encoding_DefaultBinary: Annotation,
}


def extensionobject_from_binary(data):
    """
    Convert binary-coded ExtensionObject to a Python object.
    Returns an object, or None if TypeId is zero
    """
    TypeId = NodeId.from_binary(data)
    Encoding = unpack_uatype('UInt8', data)
    if Encoding & (1 << 0):
        Body = unpack_uatype('ByteString', data)
    if TypeId.Identifier == 0:
        return None
    klass = ExtensionClasses[TypeId.Identifier]
    return klass.from_binary(Buffer(Body))


def extensionobject_to_binary(obj):
    """
    Convert Python object to binary-coded ExtensionObject.
    If obj is None, convert to empty ExtensionObject (TypeId = 0, no Body).
    Returns a binary string
    """
    TypeId = NodeId()
    Encoding = 0
    Body = None
    if obj is not None:
        TypeId = FourByteNodeId(getattr(ObjectIds, "{}_Encoding_DefaultBinary".format(obj.__class__.__name__)))
        Encoding |= (1 << 0)
        Body = obj.to_binary()
    packet = []
    packet.append(TypeId.to_binary())
    packet.append(pack_uatype('UInt8', Encoding))
    if Body:
        packet.append(pack_uatype('ByteString', Body))
    return b''.join(packet)
