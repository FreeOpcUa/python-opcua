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


class XmlElement(object):
    '''
    An XML element encoded as a UTF-8 string.

    :ivar Length:
    :vartype Length: Int32
    :ivar Value:
    :vartype Value: Char
    '''

    __slots__ = [
        "Length",
        "Value",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.Length = 0
        self.Value = []

    def to_binary(self):
        packet = []
        packet.append(uatype_Int32.pack(self.Length))
        packet.append(uatype_Int32.pack(len(self.Value)))
        for fieldname in self.Value:
            packet.append(uatype_Char.pack(fieldname))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return XmlElement(data)

    def _binary_init(self, data):
        self.Length = uatype_Int32.unpack(data.read(4))[0]
        self.Value = unpack_uatype_array('Char', data)

    def __str__(self):
        return 'XmlElement(' + 'Length:' + str(self.Length) + ', ' + \
             'Value:' + str(self.Value) + ')'

    __repr__ = __str__


class DiagnosticInfo(object):
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

    __slots__ = [
        "Encoding",
        "SymbolicId",
        "NamespaceURI",
        "Locale",
        "LocalizedText",
        "AdditionalInfo",
        "InnerStatusCode",
        "InnerDiagnosticInfo",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.Encoding = 0
        self.SymbolicId = 0
        self.NamespaceURI = 0
        self.Locale = 0
        self.LocalizedText = 0
        self.AdditionalInfo = b''
        self.InnerStatusCode = StatusCode()
        self.InnerDiagnosticInfo = None

    def to_binary(self):
        packet = []
        if self.SymbolicId: self.Encoding |= (1 << 0)
        if self.NamespaceURI: self.Encoding |= (1 << 1)
        if self.Locale: self.Encoding |= (1 << 2)
        if self.LocalizedText: self.Encoding |= (1 << 3)
        if self.AdditionalInfo: self.Encoding |= (1 << 4)
        if self.InnerStatusCode: self.Encoding |= (1 << 5)
        if self.InnerDiagnosticInfo: self.Encoding |= (1 << 6)
        packet.append(uatype_UInt8.pack(self.Encoding))
        if self.SymbolicId:
            packet.append(uatype_Int32.pack(self.SymbolicId))
        if self.NamespaceURI:
            packet.append(uatype_Int32.pack(self.NamespaceURI))
        if self.Locale:
            packet.append(uatype_Int32.pack(self.Locale))
        if self.LocalizedText:
            packet.append(uatype_Int32.pack(self.LocalizedText))
        if self.AdditionalInfo:
            packet.append(pack_bytes(self.AdditionalInfo))
        if self.InnerStatusCode:
            packet.append(self.InnerStatusCode.to_binary())
        if self.InnerDiagnosticInfo:
            packet.append(self.InnerDiagnosticInfo.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return DiagnosticInfo(data)

    def _binary_init(self, data):
        self.Encoding = uatype_UInt8.unpack(data.read(1))[0]
        if self.Encoding & (1 << 0):
            self.SymbolicId = uatype_Int32.unpack(data.read(4))[0]
        else:
            self.SymbolicId = 0
        if self.Encoding & (1 << 1):
            self.NamespaceURI = uatype_Int32.unpack(data.read(4))[0]
        else:
            self.NamespaceURI = 0
        if self.Encoding & (1 << 2):
            self.Locale = uatype_Int32.unpack(data.read(4))[0]
        else:
            self.Locale = 0
        if self.Encoding & (1 << 3):
            self.LocalizedText = uatype_Int32.unpack(data.read(4))[0]
        else:
            self.LocalizedText = 0
        if self.Encoding & (1 << 4):
            self.AdditionalInfo = unpack_bytes(data)
        else:
            self.AdditionalInfo = b''
        if self.Encoding & (1 << 5):
            self.InnerStatusCode = StatusCode.from_binary(data)
        else:
            self.InnerStatusCode = StatusCode()
        if self.Encoding & (1 << 6):
            self.InnerDiagnosticInfo = DiagnosticInfo.from_binary(data)
        else:
            self.InnerDiagnosticInfo = None

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


class TrustListDataType(object):
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

    __slots__ = [
        "SpecifiedLists",
        "TrustedCertificates",
        "TrustedCrls",
        "IssuerCertificates",
        "IssuerCrls",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.SpecifiedLists = 0
        self.TrustedCertificates = []
        self.TrustedCrls = []
        self.IssuerCertificates = []
        self.IssuerCrls = []

    def to_binary(self):
        packet = []
        packet.append(uatype_UInt32.pack(self.SpecifiedLists))
        packet.append(uatype_Int32.pack(len(self.TrustedCertificates)))
        for fieldname in self.TrustedCertificates:
            packet.append(pack_bytes(fieldname))
        packet.append(uatype_Int32.pack(len(self.TrustedCrls)))
        for fieldname in self.TrustedCrls:
            packet.append(pack_bytes(fieldname))
        packet.append(uatype_Int32.pack(len(self.IssuerCertificates)))
        for fieldname in self.IssuerCertificates:
            packet.append(pack_bytes(fieldname))
        packet.append(uatype_Int32.pack(len(self.IssuerCrls)))
        for fieldname in self.IssuerCrls:
            packet.append(pack_bytes(fieldname))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return TrustListDataType(data)

    def _binary_init(self, data):
        self.SpecifiedLists = uatype_UInt32.unpack(data.read(4))[0]
        self.TrustedCertificates = unpack_uatype_array('ByteString', data)
        self.TrustedCrls = unpack_uatype_array('ByteString', data)
        self.IssuerCertificates = unpack_uatype_array('ByteString', data)
        self.IssuerCrls = unpack_uatype_array('ByteString', data)

    def __str__(self):
        return 'TrustListDataType(' + 'SpecifiedLists:' + str(self.SpecifiedLists) + ', ' + \
             'TrustedCertificates:' + str(self.TrustedCertificates) + ', ' + \
             'TrustedCrls:' + str(self.TrustedCrls) + ', ' + \
             'IssuerCertificates:' + str(self.IssuerCertificates) + ', ' + \
             'IssuerCrls:' + str(self.IssuerCrls) + ')'

    __repr__ = __str__


class Argument(object):
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

    __slots__ = [
        "Name",
        "DataType",
        "ValueRank",
        "ArrayDimensions",
        "Description",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.Name = ''
        self.DataType = NodeId()
        self.ValueRank = 0
        self.ArrayDimensions = []
        self.Description = LocalizedText()

    def to_binary(self):
        packet = []
        packet.append(pack_string(self.Name))
        packet.append(self.DataType.to_binary())
        packet.append(uatype_Int32.pack(self.ValueRank))
        packet.append(uatype_Int32.pack(len(self.ArrayDimensions)))
        for fieldname in self.ArrayDimensions:
            packet.append(uatype_UInt32.pack(fieldname))
        packet.append(self.Description.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return Argument(data)

    def _binary_init(self, data):
        self.Name = unpack_string(data)
        self.DataType = NodeId.from_binary(data)
        self.ValueRank = uatype_Int32.unpack(data.read(4))[0]
        self.ArrayDimensions = unpack_uatype_array('UInt32', data)
        self.Description = LocalizedText.from_binary(data)

    def __str__(self):
        return 'Argument(' + 'Name:' + str(self.Name) + ', ' + \
             'DataType:' + str(self.DataType) + ', ' + \
             'ValueRank:' + str(self.ValueRank) + ', ' + \
             'ArrayDimensions:' + str(self.ArrayDimensions) + ', ' + \
             'Description:' + str(self.Description) + ')'

    __repr__ = __str__


class EnumValueType(object):
    '''
    A mapping between a value of an enumerated type and a name and description.

    :ivar Value:
    :vartype Value: Int64
    :ivar DisplayName:
    :vartype DisplayName: LocalizedText
    :ivar Description:
    :vartype Description: LocalizedText
    '''

    __slots__ = [
        "Value",
        "DisplayName",
        "Description",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.Value = 0
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()

    def to_binary(self):
        packet = []
        packet.append(uatype_Int64.pack(self.Value))
        packet.append(self.DisplayName.to_binary())
        packet.append(self.Description.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return EnumValueType(data)

    def _binary_init(self, data):
        self.Value = uatype_Int64.unpack(data.read(8))[0]
        self.DisplayName = LocalizedText.from_binary(data)
        self.Description = LocalizedText.from_binary(data)

    def __str__(self):
        return 'EnumValueType(' + 'Value:' + str(self.Value) + ', ' + \
             'DisplayName:' + str(self.DisplayName) + ', ' + \
             'Description:' + str(self.Description) + ')'

    __repr__ = __str__


class OptionSet(object):
    '''
    This abstract Structured DataType is the base DataType for all DataTypes representing a bit mask.

    :ivar Value:
    :vartype Value: ByteString
    :ivar ValidBits:
    :vartype ValidBits: ByteString
    '''

    __slots__ = [
        "Value",
        "ValidBits",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.Value = b''
        self.ValidBits = b''

    def to_binary(self):
        packet = []
        packet.append(pack_bytes(self.Value))
        packet.append(pack_bytes(self.ValidBits))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return OptionSet(data)

    def _binary_init(self, data):
        self.Value = unpack_bytes(data)
        self.ValidBits = unpack_bytes(data)

    def __str__(self):
        return 'OptionSet(' + 'Value:' + str(self.Value) + ', ' + \
             'ValidBits:' + str(self.ValidBits) + ')'

    __repr__ = __str__


class Union(object):
    '''
    This abstract DataType is the base DataType for all union DataTypes.

    '''

    __slots__ = [
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return

    def to_binary(self):
        packet = []
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return Union(data)

    def _binary_init(self, data):
        pass

    def __str__(self):
        return 'Union(' +  + ')'

    __repr__ = __str__


class TimeZoneDataType(object):
    '''
    :ivar Offset:
    :vartype Offset: Int16
    :ivar DaylightSavingInOffset:
    :vartype DaylightSavingInOffset: Boolean
    '''

    __slots__ = [
        "Offset",
        "DaylightSavingInOffset",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.Offset = 0
        self.DaylightSavingInOffset = True

    def to_binary(self):
        packet = []
        packet.append(uatype_Int16.pack(self.Offset))
        packet.append(uatype_Boolean.pack(self.DaylightSavingInOffset))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return TimeZoneDataType(data)

    def _binary_init(self, data):
        self.Offset = uatype_Int16.unpack(data.read(2))[0]
        self.DaylightSavingInOffset = uatype_Boolean.unpack(data.read(1))[0]

    def __str__(self):
        return 'TimeZoneDataType(' + 'Offset:' + str(self.Offset) + ', ' + \
             'DaylightSavingInOffset:' + str(self.DaylightSavingInOffset) + ')'

    __repr__ = __str__


class ApplicationDescription(object):
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

    __slots__ = [
        "ApplicationUri",
        "ProductUri",
        "ApplicationName",
        "ApplicationType",
        "GatewayServerUri",
        "DiscoveryProfileUri",
        "DiscoveryUrls",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.ApplicationUri = ''
        self.ProductUri = ''
        self.ApplicationName = LocalizedText()
        self.ApplicationType = 0
        self.GatewayServerUri = ''
        self.DiscoveryProfileUri = ''
        self.DiscoveryUrls = []

    def to_binary(self):
        packet = []
        packet.append(pack_string(self.ApplicationUri))
        packet.append(pack_string(self.ProductUri))
        packet.append(self.ApplicationName.to_binary())
        packet.append(uatype_UInt32.pack(self.ApplicationType))
        packet.append(pack_string(self.GatewayServerUri))
        packet.append(pack_string(self.DiscoveryProfileUri))
        packet.append(uatype_Int32.pack(len(self.DiscoveryUrls)))
        for fieldname in self.DiscoveryUrls:
            packet.append(pack_string(fieldname))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return ApplicationDescription(data)

    def _binary_init(self, data):
        self.ApplicationUri = unpack_string(data)
        self.ProductUri = unpack_string(data)
        self.ApplicationName = LocalizedText.from_binary(data)
        self.ApplicationType = uatype_UInt32.unpack(data.read(4))[0]
        self.GatewayServerUri = unpack_string(data)
        self.DiscoveryProfileUri = unpack_string(data)
        self.DiscoveryUrls = unpack_uatype_array('String', data)

    def __str__(self):
        return 'ApplicationDescription(' + 'ApplicationUri:' + str(self.ApplicationUri) + ', ' + \
             'ProductUri:' + str(self.ProductUri) + ', ' + \
             'ApplicationName:' + str(self.ApplicationName) + ', ' + \
             'ApplicationType:' + str(self.ApplicationType) + ', ' + \
             'GatewayServerUri:' + str(self.GatewayServerUri) + ', ' + \
             'DiscoveryProfileUri:' + str(self.DiscoveryProfileUri) + ', ' + \
             'DiscoveryUrls:' + str(self.DiscoveryUrls) + ')'

    __repr__ = __str__


class RequestHeader(object):
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

    __slots__ = [
        "AuthenticationToken",
        "Timestamp",
        "RequestHandle",
        "ReturnDiagnostics",
        "AuditEntryId",
        "TimeoutHint",
        "AdditionalHeader",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.AuthenticationToken = NodeId()
        self.Timestamp = datetime.now()
        self.RequestHandle = 0
        self.ReturnDiagnostics = 0
        self.AuditEntryId = ''
        self.TimeoutHint = 0
        self.AdditionalHeader = None

    def to_binary(self):
        packet = []
        packet.append(self.AuthenticationToken.to_binary())
        packet.append(pack_datetime(self.Timestamp))
        packet.append(uatype_UInt32.pack(self.RequestHandle))
        packet.append(uatype_UInt32.pack(self.ReturnDiagnostics))
        packet.append(pack_string(self.AuditEntryId))
        packet.append(uatype_UInt32.pack(self.TimeoutHint))
        packet.append(extensionobject_to_binary(self.AdditionalHeader))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return RequestHeader(data)

    def _binary_init(self, data):
        self.AuthenticationToken = NodeId.from_binary(data)
        self.Timestamp = unpack_datetime(data)
        self.RequestHandle = uatype_UInt32.unpack(data.read(4))[0]
        self.ReturnDiagnostics = uatype_UInt32.unpack(data.read(4))[0]
        self.AuditEntryId = unpack_string(data)
        self.TimeoutHint = uatype_UInt32.unpack(data.read(4))[0]
        self.AdditionalHeader = extensionobject_from_binary(data)

    def __str__(self):
        return 'RequestHeader(' + 'AuthenticationToken:' + str(self.AuthenticationToken) + ', ' + \
             'Timestamp:' + str(self.Timestamp) + ', ' + \
             'RequestHandle:' + str(self.RequestHandle) + ', ' + \
             'ReturnDiagnostics:' + str(self.ReturnDiagnostics) + ', ' + \
             'AuditEntryId:' + str(self.AuditEntryId) + ', ' + \
             'TimeoutHint:' + str(self.TimeoutHint) + ', ' + \
             'AdditionalHeader:' + str(self.AdditionalHeader) + ')'

    __repr__ = __str__


class ResponseHeader(object):
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

    __slots__ = [
        "Timestamp",
        "RequestHandle",
        "ServiceResult",
        "ServiceDiagnostics",
        "StringTable",
        "AdditionalHeader",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.Timestamp = datetime.now()
        self.RequestHandle = 0
        self.ServiceResult = StatusCode()
        self.ServiceDiagnostics = DiagnosticInfo()
        self.StringTable = []
        self.AdditionalHeader = None

    def to_binary(self):
        packet = []
        packet.append(pack_datetime(self.Timestamp))
        packet.append(uatype_UInt32.pack(self.RequestHandle))
        packet.append(self.ServiceResult.to_binary())
        packet.append(self.ServiceDiagnostics.to_binary())
        packet.append(uatype_Int32.pack(len(self.StringTable)))
        for fieldname in self.StringTable:
            packet.append(pack_string(fieldname))
        packet.append(extensionobject_to_binary(self.AdditionalHeader))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return ResponseHeader(data)

    def _binary_init(self, data):
        self.Timestamp = unpack_datetime(data)
        self.RequestHandle = uatype_UInt32.unpack(data.read(4))[0]
        self.ServiceResult = StatusCode.from_binary(data)
        self.ServiceDiagnostics = DiagnosticInfo.from_binary(data)
        self.StringTable = unpack_uatype_array('String', data)
        self.AdditionalHeader = extensionobject_from_binary(data)

    def __str__(self):
        return 'ResponseHeader(' + 'Timestamp:' + str(self.Timestamp) + ', ' + \
             'RequestHandle:' + str(self.RequestHandle) + ', ' + \
             'ServiceResult:' + str(self.ServiceResult) + ', ' + \
             'ServiceDiagnostics:' + str(self.ServiceDiagnostics) + ', ' + \
             'StringTable:' + str(self.StringTable) + ', ' + \
             'AdditionalHeader:' + str(self.AdditionalHeader) + ')'

    __repr__ = __str__


class ServiceFault(object):
    '''
    The response returned by all services when there is a service level error.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    '''

    __slots__ = [
        "TypeId",
        "ResponseHeader",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.ServiceFault_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return ServiceFault(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.ResponseHeader = ResponseHeader.from_binary(data)

    def __str__(self):
        return 'ServiceFault(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'ResponseHeader:' + str(self.ResponseHeader) + ')'

    __repr__ = __str__


class FindServersParameters(object):
    '''
    :ivar EndpointUrl:
    :vartype EndpointUrl: String
    :ivar LocaleIds:
    :vartype LocaleIds: String
    :ivar ServerUris:
    :vartype ServerUris: String
    '''

    __slots__ = [
        "EndpointUrl",
        "LocaleIds",
        "ServerUris",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.EndpointUrl = ''
        self.LocaleIds = []
        self.ServerUris = []

    def to_binary(self):
        packet = []
        packet.append(pack_string(self.EndpointUrl))
        packet.append(uatype_Int32.pack(len(self.LocaleIds)))
        for fieldname in self.LocaleIds:
            packet.append(pack_string(fieldname))
        packet.append(uatype_Int32.pack(len(self.ServerUris)))
        for fieldname in self.ServerUris:
            packet.append(pack_string(fieldname))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return FindServersParameters(data)

    def _binary_init(self, data):
        self.EndpointUrl = unpack_string(data)
        self.LocaleIds = unpack_uatype_array('String', data)
        self.ServerUris = unpack_uatype_array('String', data)

    def __str__(self):
        return 'FindServersParameters(' + 'EndpointUrl:' + str(self.EndpointUrl) + ', ' + \
             'LocaleIds:' + str(self.LocaleIds) + ', ' + \
             'ServerUris:' + str(self.ServerUris) + ')'

    __repr__ = __str__


class FindServersRequest(object):
    '''
    Finds the servers known to the discovery server.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: FindServersParameters
    '''

    __slots__ = [
        "TypeId",
        "RequestHeader",
        "Parameters",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.FindServersRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = FindServersParameters()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return FindServersRequest(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.RequestHeader = RequestHeader.from_binary(data)
        self.Parameters = FindServersParameters.from_binary(data)

    def __str__(self):
        return 'FindServersRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'RequestHeader:' + str(self.RequestHeader) + ', ' + \
             'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class FindServersResponse(object):
    '''
    Finds the servers known to the discovery server.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    :ivar Servers:
    :vartype Servers: ApplicationDescription
    '''

    __slots__ = [
        "TypeId",
        "ResponseHeader",
        "Servers",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.FindServersResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Servers = []

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(uatype_Int32.pack(len(self.Servers)))
        for fieldname in self.Servers:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return FindServersResponse(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.ResponseHeader = ResponseHeader.from_binary(data)
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(ApplicationDescription.from_binary(data))
        self.Servers = array

    def __str__(self):
        return 'FindServersResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
             'Servers:' + str(self.Servers) + ')'

    __repr__ = __str__


class ServerOnNetwork(object):
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

    __slots__ = [
        "RecordId",
        "ServerName",
        "DiscoveryUrl",
        "ServerCapabilities",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.RecordId = 0
        self.ServerName = ''
        self.DiscoveryUrl = ''
        self.ServerCapabilities = []

    def to_binary(self):
        packet = []
        packet.append(uatype_UInt32.pack(self.RecordId))
        packet.append(pack_string(self.ServerName))
        packet.append(pack_string(self.DiscoveryUrl))
        packet.append(uatype_Int32.pack(len(self.ServerCapabilities)))
        for fieldname in self.ServerCapabilities:
            packet.append(pack_string(fieldname))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return ServerOnNetwork(data)

    def _binary_init(self, data):
        self.RecordId = uatype_UInt32.unpack(data.read(4))[0]
        self.ServerName = unpack_string(data)
        self.DiscoveryUrl = unpack_string(data)
        self.ServerCapabilities = unpack_uatype_array('String', data)

    def __str__(self):
        return 'ServerOnNetwork(' + 'RecordId:' + str(self.RecordId) + ', ' + \
             'ServerName:' + str(self.ServerName) + ', ' + \
             'DiscoveryUrl:' + str(self.DiscoveryUrl) + ', ' + \
             'ServerCapabilities:' + str(self.ServerCapabilities) + ')'

    __repr__ = __str__


class FindServersOnNetworkParameters(object):
    '''
    :ivar StartingRecordId:
    :vartype StartingRecordId: UInt32
    :ivar MaxRecordsToReturn:
    :vartype MaxRecordsToReturn: UInt32
    :ivar ServerCapabilityFilter:
    :vartype ServerCapabilityFilter: String
    '''

    __slots__ = [
        "StartingRecordId",
        "MaxRecordsToReturn",
        "ServerCapabilityFilter",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.StartingRecordId = 0
        self.MaxRecordsToReturn = 0
        self.ServerCapabilityFilter = []

    def to_binary(self):
        packet = []
        packet.append(uatype_UInt32.pack(self.StartingRecordId))
        packet.append(uatype_UInt32.pack(self.MaxRecordsToReturn))
        packet.append(uatype_Int32.pack(len(self.ServerCapabilityFilter)))
        for fieldname in self.ServerCapabilityFilter:
            packet.append(pack_string(fieldname))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return FindServersOnNetworkParameters(data)

    def _binary_init(self, data):
        self.StartingRecordId = uatype_UInt32.unpack(data.read(4))[0]
        self.MaxRecordsToReturn = uatype_UInt32.unpack(data.read(4))[0]
        self.ServerCapabilityFilter = unpack_uatype_array('String', data)

    def __str__(self):
        return 'FindServersOnNetworkParameters(' + 'StartingRecordId:' + str(self.StartingRecordId) + ', ' + \
             'MaxRecordsToReturn:' + str(self.MaxRecordsToReturn) + ', ' + \
             'ServerCapabilityFilter:' + str(self.ServerCapabilityFilter) + ')'

    __repr__ = __str__


class FindServersOnNetworkRequest(object):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: FindServersOnNetworkParameters
    '''

    __slots__ = [
        "TypeId",
        "RequestHeader",
        "Parameters",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.FindServersOnNetworkRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = FindServersOnNetworkParameters()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return FindServersOnNetworkRequest(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.RequestHeader = RequestHeader.from_binary(data)
        self.Parameters = FindServersOnNetworkParameters.from_binary(data)

    def __str__(self):
        return 'FindServersOnNetworkRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'RequestHeader:' + str(self.RequestHeader) + ', ' + \
             'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class FindServersOnNetworkResult(object):
    '''
    :ivar LastCounterResetTime:
    :vartype LastCounterResetTime: DateTime
    :ivar Servers:
    :vartype Servers: ServerOnNetwork
    '''

    __slots__ = [
        "LastCounterResetTime",
        "Servers",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.LastCounterResetTime = datetime.now()
        self.Servers = []

    def to_binary(self):
        packet = []
        packet.append(pack_datetime(self.LastCounterResetTime))
        packet.append(uatype_Int32.pack(len(self.Servers)))
        for fieldname in self.Servers:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return FindServersOnNetworkResult(data)

    def _binary_init(self, data):
        self.LastCounterResetTime = unpack_datetime(data)
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(ServerOnNetwork.from_binary(data))
        self.Servers = array

    def __str__(self):
        return 'FindServersOnNetworkResult(' + 'LastCounterResetTime:' + str(self.LastCounterResetTime) + ', ' + \
             'Servers:' + str(self.Servers) + ')'

    __repr__ = __str__


class FindServersOnNetworkResponse(object):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    :ivar Parameters:
    :vartype Parameters: FindServersOnNetworkResult
    '''

    __slots__ = [
        "TypeId",
        "ResponseHeader",
        "Parameters",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.FindServersOnNetworkResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = FindServersOnNetworkResult()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return FindServersOnNetworkResponse(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.ResponseHeader = ResponseHeader.from_binary(data)
        self.Parameters = FindServersOnNetworkResult.from_binary(data)

    def __str__(self):
        return 'FindServersOnNetworkResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
             'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class UserTokenPolicy(object):
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

    __slots__ = [
        "PolicyId",
        "TokenType",
        "IssuedTokenType",
        "IssuerEndpointUrl",
        "SecurityPolicyUri",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.PolicyId = ''
        self.TokenType = 0
        self.IssuedTokenType = ''
        self.IssuerEndpointUrl = ''
        self.SecurityPolicyUri = ''

    def to_binary(self):
        packet = []
        packet.append(pack_string(self.PolicyId))
        packet.append(uatype_UInt32.pack(self.TokenType))
        packet.append(pack_string(self.IssuedTokenType))
        packet.append(pack_string(self.IssuerEndpointUrl))
        packet.append(pack_string(self.SecurityPolicyUri))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return UserTokenPolicy(data)

    def _binary_init(self, data):
        self.PolicyId = unpack_string(data)
        self.TokenType = uatype_UInt32.unpack(data.read(4))[0]
        self.IssuedTokenType = unpack_string(data)
        self.IssuerEndpointUrl = unpack_string(data)
        self.SecurityPolicyUri = unpack_string(data)

    def __str__(self):
        return 'UserTokenPolicy(' + 'PolicyId:' + str(self.PolicyId) + ', ' + \
             'TokenType:' + str(self.TokenType) + ', ' + \
             'IssuedTokenType:' + str(self.IssuedTokenType) + ', ' + \
             'IssuerEndpointUrl:' + str(self.IssuerEndpointUrl) + ', ' + \
             'SecurityPolicyUri:' + str(self.SecurityPolicyUri) + ')'

    __repr__ = __str__


class EndpointDescription(object):
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

    __slots__ = [
        "EndpointUrl",
        "Server",
        "ServerCertificate",
        "SecurityMode",
        "SecurityPolicyUri",
        "UserIdentityTokens",
        "TransportProfileUri",
        "SecurityLevel",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.EndpointUrl = ''
        self.Server = ApplicationDescription()
        self.ServerCertificate = b''
        self.SecurityMode = 0
        self.SecurityPolicyUri = ''
        self.UserIdentityTokens = []
        self.TransportProfileUri = ''
        self.SecurityLevel = 0

    def to_binary(self):
        packet = []
        packet.append(pack_string(self.EndpointUrl))
        packet.append(self.Server.to_binary())
        packet.append(pack_bytes(self.ServerCertificate))
        packet.append(uatype_UInt32.pack(self.SecurityMode))
        packet.append(pack_string(self.SecurityPolicyUri))
        packet.append(uatype_Int32.pack(len(self.UserIdentityTokens)))
        for fieldname in self.UserIdentityTokens:
            packet.append(fieldname.to_binary())
        packet.append(pack_string(self.TransportProfileUri))
        packet.append(uatype_Byte.pack(self.SecurityLevel))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return EndpointDescription(data)

    def _binary_init(self, data):
        self.EndpointUrl = unpack_string(data)
        self.Server = ApplicationDescription.from_binary(data)
        self.ServerCertificate = unpack_bytes(data)
        self.SecurityMode = uatype_UInt32.unpack(data.read(4))[0]
        self.SecurityPolicyUri = unpack_string(data)
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(UserTokenPolicy.from_binary(data))
        self.UserIdentityTokens = array
        self.TransportProfileUri = unpack_string(data)
        self.SecurityLevel = uatype_Byte.unpack(data.read(1))[0]

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


class GetEndpointsParameters(object):
    '''
    :ivar EndpointUrl:
    :vartype EndpointUrl: String
    :ivar LocaleIds:
    :vartype LocaleIds: String
    :ivar ProfileUris:
    :vartype ProfileUris: String
    '''

    __slots__ = [
        "EndpointUrl",
        "LocaleIds",
        "ProfileUris",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.EndpointUrl = ''
        self.LocaleIds = []
        self.ProfileUris = []

    def to_binary(self):
        packet = []
        packet.append(pack_string(self.EndpointUrl))
        packet.append(uatype_Int32.pack(len(self.LocaleIds)))
        for fieldname in self.LocaleIds:
            packet.append(pack_string(fieldname))
        packet.append(uatype_Int32.pack(len(self.ProfileUris)))
        for fieldname in self.ProfileUris:
            packet.append(pack_string(fieldname))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return GetEndpointsParameters(data)

    def _binary_init(self, data):
        self.EndpointUrl = unpack_string(data)
        self.LocaleIds = unpack_uatype_array('String', data)
        self.ProfileUris = unpack_uatype_array('String', data)

    def __str__(self):
        return 'GetEndpointsParameters(' + 'EndpointUrl:' + str(self.EndpointUrl) + ', ' + \
             'LocaleIds:' + str(self.LocaleIds) + ', ' + \
             'ProfileUris:' + str(self.ProfileUris) + ')'

    __repr__ = __str__


class GetEndpointsRequest(object):
    '''
    Gets the endpoints used by the server.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: GetEndpointsParameters
    '''

    __slots__ = [
        "TypeId",
        "RequestHeader",
        "Parameters",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.GetEndpointsRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = GetEndpointsParameters()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return GetEndpointsRequest(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.RequestHeader = RequestHeader.from_binary(data)
        self.Parameters = GetEndpointsParameters.from_binary(data)

    def __str__(self):
        return 'GetEndpointsRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'RequestHeader:' + str(self.RequestHeader) + ', ' + \
             'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class GetEndpointsResponse(object):
    '''
    Gets the endpoints used by the server.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    :ivar Endpoints:
    :vartype Endpoints: EndpointDescription
    '''

    __slots__ = [
        "TypeId",
        "ResponseHeader",
        "Endpoints",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.GetEndpointsResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Endpoints = []

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(uatype_Int32.pack(len(self.Endpoints)))
        for fieldname in self.Endpoints:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return GetEndpointsResponse(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.ResponseHeader = ResponseHeader.from_binary(data)
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(EndpointDescription.from_binary(data))
        self.Endpoints = array

    def __str__(self):
        return 'GetEndpointsResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
             'Endpoints:' + str(self.Endpoints) + ')'

    __repr__ = __str__


class RegisteredServer(object):
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

    __slots__ = [
        "ServerUri",
        "ProductUri",
        "ServerNames",
        "ServerType",
        "GatewayServerUri",
        "DiscoveryUrls",
        "SemaphoreFilePath",
        "IsOnline",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.ServerUri = ''
        self.ProductUri = ''
        self.ServerNames = []
        self.ServerType = 0
        self.GatewayServerUri = ''
        self.DiscoveryUrls = []
        self.SemaphoreFilePath = ''
        self.IsOnline = True

    def to_binary(self):
        packet = []
        packet.append(pack_string(self.ServerUri))
        packet.append(pack_string(self.ProductUri))
        packet.append(uatype_Int32.pack(len(self.ServerNames)))
        for fieldname in self.ServerNames:
            packet.append(fieldname.to_binary())
        packet.append(uatype_UInt32.pack(self.ServerType))
        packet.append(pack_string(self.GatewayServerUri))
        packet.append(uatype_Int32.pack(len(self.DiscoveryUrls)))
        for fieldname in self.DiscoveryUrls:
            packet.append(pack_string(fieldname))
        packet.append(pack_string(self.SemaphoreFilePath))
        packet.append(uatype_Boolean.pack(self.IsOnline))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return RegisteredServer(data)

    def _binary_init(self, data):
        self.ServerUri = unpack_string(data)
        self.ProductUri = unpack_string(data)
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(LocalizedText.from_binary(data))
        self.ServerNames = array
        self.ServerType = uatype_UInt32.unpack(data.read(4))[0]
        self.GatewayServerUri = unpack_string(data)
        self.DiscoveryUrls = unpack_uatype_array('String', data)
        self.SemaphoreFilePath = unpack_string(data)
        self.IsOnline = uatype_Boolean.unpack(data.read(1))[0]

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


class RegisterServerParameters(object):
    '''
    :ivar Server:
    :vartype Server: RegisteredServer
    '''

    __slots__ = [
        "Server",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.Server = RegisteredServer()

    def to_binary(self):
        packet = []
        packet.append(self.Server.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return RegisterServerParameters(data)

    def _binary_init(self, data):
        self.Server = RegisteredServer.from_binary(data)

    def __str__(self):
        return 'RegisterServerParameters(' + 'Server:' + str(self.Server) + ')'

    __repr__ = __str__


class RegisterServerRequest(object):
    '''
    Registers a server with the discovery server.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: RegisterServerParameters
    '''

    __slots__ = [
        "TypeId",
        "RequestHeader",
        "Parameters",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.RegisterServerRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = RegisterServerParameters()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return RegisterServerRequest(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.RequestHeader = RequestHeader.from_binary(data)
        self.Parameters = RegisterServerParameters.from_binary(data)

    def __str__(self):
        return 'RegisterServerRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'RequestHeader:' + str(self.RequestHeader) + ', ' + \
             'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class RegisterServerResponse(object):
    '''
    Registers a server with the discovery server.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    '''

    __slots__ = [
        "TypeId",
        "ResponseHeader",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.RegisterServerResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return RegisterServerResponse(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.ResponseHeader = ResponseHeader.from_binary(data)

    def __str__(self):
        return 'RegisterServerResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'ResponseHeader:' + str(self.ResponseHeader) + ')'

    __repr__ = __str__


class DiscoveryConfiguration(object):
    '''
    A base type for discovery configuration information.

    '''

    __slots__ = [
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return

    def to_binary(self):
        packet = []
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return DiscoveryConfiguration(data)

    def _binary_init(self, data):
        pass

    def __str__(self):
        return 'DiscoveryConfiguration(' +  + ')'

    __repr__ = __str__


class MdnsDiscoveryConfiguration(object):
    '''
    The discovery information needed for mDNS registration.

    :ivar MdnsServerName:
    :vartype MdnsServerName: String
    :ivar ServerCapabilities:
    :vartype ServerCapabilities: String
    '''

    __slots__ = [
        "MdnsServerName",
        "ServerCapabilities",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.MdnsServerName = ''
        self.ServerCapabilities = []

    def to_binary(self):
        packet = []
        packet.append(pack_string(self.MdnsServerName))
        packet.append(uatype_Int32.pack(len(self.ServerCapabilities)))
        for fieldname in self.ServerCapabilities:
            packet.append(pack_string(fieldname))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return MdnsDiscoveryConfiguration(data)

    def _binary_init(self, data):
        self.MdnsServerName = unpack_string(data)
        self.ServerCapabilities = unpack_uatype_array('String', data)

    def __str__(self):
        return 'MdnsDiscoveryConfiguration(' + 'MdnsServerName:' + str(self.MdnsServerName) + ', ' + \
             'ServerCapabilities:' + str(self.ServerCapabilities) + ')'

    __repr__ = __str__


class RegisterServer2Parameters(object):
    '''
    :ivar Server:
    :vartype Server: RegisteredServer
    :ivar DiscoveryConfiguration:
    :vartype DiscoveryConfiguration: ExtensionObject
    '''

    __slots__ = [
        "Server",
        "DiscoveryConfiguration",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.Server = RegisteredServer()
        self.DiscoveryConfiguration = []

    def to_binary(self):
        packet = []
        packet.append(self.Server.to_binary())
        packet.append(uatype_Int32.pack(len(self.DiscoveryConfiguration)))
        for fieldname in self.DiscoveryConfiguration:
            packet.append(extensionobject_to_binary(fieldname))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return RegisterServer2Parameters(data)

    def _binary_init(self, data):
        self.Server = RegisteredServer.from_binary(data)
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(extensionobject_from_binary(data))
        self.DiscoveryConfiguration = array

    def __str__(self):
        return 'RegisterServer2Parameters(' + 'Server:' + str(self.Server) + ', ' + \
             'DiscoveryConfiguration:' + str(self.DiscoveryConfiguration) + ')'

    __repr__ = __str__


class RegisterServer2Request(object):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: RegisterServer2Parameters
    '''

    __slots__ = [
        "TypeId",
        "RequestHeader",
        "Parameters",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.RegisterServer2Request_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = RegisterServer2Parameters()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return RegisterServer2Request(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.RequestHeader = RequestHeader.from_binary(data)
        self.Parameters = RegisterServer2Parameters.from_binary(data)

    def __str__(self):
        return 'RegisterServer2Request(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'RequestHeader:' + str(self.RequestHeader) + ', ' + \
             'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class RegisterServer2Result(object):
    '''
    :ivar ConfigurationResults:
    :vartype ConfigurationResults: StatusCode
    :ivar DiagnosticInfos:
    :vartype DiagnosticInfos: DiagnosticInfo
    '''

    __slots__ = [
        "ConfigurationResults",
        "DiagnosticInfos",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.ConfigurationResults = []
        self.DiagnosticInfos = []

    def to_binary(self):
        packet = []
        packet.append(uatype_Int32.pack(len(self.ConfigurationResults)))
        for fieldname in self.ConfigurationResults:
            packet.append(fieldname.to_binary())
        packet.append(uatype_Int32.pack(len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return RegisterServer2Result(data)

    def _binary_init(self, data):
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(StatusCode.from_binary(data))
        self.ConfigurationResults = array
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(DiagnosticInfo.from_binary(data))
        self.DiagnosticInfos = array

    def __str__(self):
        return 'RegisterServer2Result(' + 'ConfigurationResults:' + str(self.ConfigurationResults) + ', ' + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'

    __repr__ = __str__


class RegisterServer2Response(object):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    :ivar Parameters:
    :vartype Parameters: RegisterServer2Result
    '''

    __slots__ = [
        "TypeId",
        "ResponseHeader",
        "Parameters",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.RegisterServer2Response_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = RegisterServer2Result()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return RegisterServer2Response(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.ResponseHeader = ResponseHeader.from_binary(data)
        self.Parameters = RegisterServer2Result.from_binary(data)

    def __str__(self):
        return 'RegisterServer2Response(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
             'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class ChannelSecurityToken(object):
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

    __slots__ = [
        "ChannelId",
        "TokenId",
        "CreatedAt",
        "RevisedLifetime",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.ChannelId = 0
        self.TokenId = 0
        self.CreatedAt = datetime.now()
        self.RevisedLifetime = 0

    def to_binary(self):
        packet = []
        packet.append(uatype_UInt32.pack(self.ChannelId))
        packet.append(uatype_UInt32.pack(self.TokenId))
        packet.append(pack_datetime(self.CreatedAt))
        packet.append(uatype_UInt32.pack(self.RevisedLifetime))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return ChannelSecurityToken(data)

    def _binary_init(self, data):
        self.ChannelId = uatype_UInt32.unpack(data.read(4))[0]
        self.TokenId = uatype_UInt32.unpack(data.read(4))[0]
        self.CreatedAt = unpack_datetime(data)
        self.RevisedLifetime = uatype_UInt32.unpack(data.read(4))[0]

    def __str__(self):
        return 'ChannelSecurityToken(' + 'ChannelId:' + str(self.ChannelId) + ', ' + \
             'TokenId:' + str(self.TokenId) + ', ' + \
             'CreatedAt:' + str(self.CreatedAt) + ', ' + \
             'RevisedLifetime:' + str(self.RevisedLifetime) + ')'

    __repr__ = __str__


class OpenSecureChannelParameters(object):
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

    __slots__ = [
        "ClientProtocolVersion",
        "RequestType",
        "SecurityMode",
        "ClientNonce",
        "RequestedLifetime",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.ClientProtocolVersion = 0
        self.RequestType = 0
        self.SecurityMode = 0
        self.ClientNonce = b''
        self.RequestedLifetime = 0

    def to_binary(self):
        packet = []
        packet.append(uatype_UInt32.pack(self.ClientProtocolVersion))
        packet.append(uatype_UInt32.pack(self.RequestType))
        packet.append(uatype_UInt32.pack(self.SecurityMode))
        packet.append(pack_bytes(self.ClientNonce))
        packet.append(uatype_UInt32.pack(self.RequestedLifetime))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return OpenSecureChannelParameters(data)

    def _binary_init(self, data):
        self.ClientProtocolVersion = uatype_UInt32.unpack(data.read(4))[0]
        self.RequestType = uatype_UInt32.unpack(data.read(4))[0]
        self.SecurityMode = uatype_UInt32.unpack(data.read(4))[0]
        self.ClientNonce = unpack_bytes(data)
        self.RequestedLifetime = uatype_UInt32.unpack(data.read(4))[0]

    def __str__(self):
        return 'OpenSecureChannelParameters(' + 'ClientProtocolVersion:' + str(self.ClientProtocolVersion) + ', ' + \
             'RequestType:' + str(self.RequestType) + ', ' + \
             'SecurityMode:' + str(self.SecurityMode) + ', ' + \
             'ClientNonce:' + str(self.ClientNonce) + ', ' + \
             'RequestedLifetime:' + str(self.RequestedLifetime) + ')'

    __repr__ = __str__


class OpenSecureChannelRequest(object):
    '''
    Creates a secure channel with a server.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: OpenSecureChannelParameters
    '''

    __slots__ = [
        "TypeId",
        "RequestHeader",
        "Parameters",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.OpenSecureChannelRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = OpenSecureChannelParameters()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return OpenSecureChannelRequest(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.RequestHeader = RequestHeader.from_binary(data)
        self.Parameters = OpenSecureChannelParameters.from_binary(data)

    def __str__(self):
        return 'OpenSecureChannelRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'RequestHeader:' + str(self.RequestHeader) + ', ' + \
             'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class OpenSecureChannelResult(object):
    '''
    :ivar ServerProtocolVersion:
    :vartype ServerProtocolVersion: UInt32
    :ivar SecurityToken:
    :vartype SecurityToken: ChannelSecurityToken
    :ivar ServerNonce:
    :vartype ServerNonce: ByteString
    '''

    __slots__ = [
        "ServerProtocolVersion",
        "SecurityToken",
        "ServerNonce",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.ServerProtocolVersion = 0
        self.SecurityToken = ChannelSecurityToken()
        self.ServerNonce = b''

    def to_binary(self):
        packet = []
        packet.append(uatype_UInt32.pack(self.ServerProtocolVersion))
        packet.append(self.SecurityToken.to_binary())
        packet.append(pack_bytes(self.ServerNonce))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return OpenSecureChannelResult(data)

    def _binary_init(self, data):
        self.ServerProtocolVersion = uatype_UInt32.unpack(data.read(4))[0]
        self.SecurityToken = ChannelSecurityToken.from_binary(data)
        self.ServerNonce = unpack_bytes(data)

    def __str__(self):
        return 'OpenSecureChannelResult(' + 'ServerProtocolVersion:' + str(self.ServerProtocolVersion) + ', ' + \
             'SecurityToken:' + str(self.SecurityToken) + ', ' + \
             'ServerNonce:' + str(self.ServerNonce) + ')'

    __repr__ = __str__


class OpenSecureChannelResponse(object):
    '''
    Creates a secure channel with a server.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    :ivar Parameters:
    :vartype Parameters: OpenSecureChannelResult
    '''

    __slots__ = [
        "TypeId",
        "ResponseHeader",
        "Parameters",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.OpenSecureChannelResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = OpenSecureChannelResult()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return OpenSecureChannelResponse(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.ResponseHeader = ResponseHeader.from_binary(data)
        self.Parameters = OpenSecureChannelResult.from_binary(data)

    def __str__(self):
        return 'OpenSecureChannelResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
             'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class CloseSecureChannelRequest(object):
    '''
    Closes a secure channel.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    '''

    __slots__ = [
        "TypeId",
        "RequestHeader",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.CloseSecureChannelRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return CloseSecureChannelRequest(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.RequestHeader = RequestHeader.from_binary(data)

    def __str__(self):
        return 'CloseSecureChannelRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'RequestHeader:' + str(self.RequestHeader) + ')'

    __repr__ = __str__


class CloseSecureChannelResponse(object):
    '''
    Closes a secure channel.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    '''

    __slots__ = [
        "TypeId",
        "ResponseHeader",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.CloseSecureChannelResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return CloseSecureChannelResponse(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.ResponseHeader = ResponseHeader.from_binary(data)

    def __str__(self):
        return 'CloseSecureChannelResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'ResponseHeader:' + str(self.ResponseHeader) + ')'

    __repr__ = __str__


class SignedSoftwareCertificate(object):
    '''
    A software certificate with a digital signature.

    :ivar CertificateData:
    :vartype CertificateData: ByteString
    :ivar Signature:
    :vartype Signature: ByteString
    '''

    __slots__ = [
        "CertificateData",
        "Signature",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.CertificateData = b''
        self.Signature = b''

    def to_binary(self):
        packet = []
        packet.append(pack_bytes(self.CertificateData))
        packet.append(pack_bytes(self.Signature))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return SignedSoftwareCertificate(data)

    def _binary_init(self, data):
        self.CertificateData = unpack_bytes(data)
        self.Signature = unpack_bytes(data)

    def __str__(self):
        return 'SignedSoftwareCertificate(' + 'CertificateData:' + str(self.CertificateData) + ', ' + \
             'Signature:' + str(self.Signature) + ')'

    __repr__ = __str__


class SignatureData(object):
    '''
    A digital signature.

    :ivar Algorithm:
    :vartype Algorithm: String
    :ivar Signature:
    :vartype Signature: ByteString
    '''

    __slots__ = [
        "Algorithm",
        "Signature",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.Algorithm = ''
        self.Signature = b''

    def to_binary(self):
        packet = []
        packet.append(pack_string(self.Algorithm))
        packet.append(pack_bytes(self.Signature))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return SignatureData(data)

    def _binary_init(self, data):
        self.Algorithm = unpack_string(data)
        self.Signature = unpack_bytes(data)

    def __str__(self):
        return 'SignatureData(' + 'Algorithm:' + str(self.Algorithm) + ', ' + \
             'Signature:' + str(self.Signature) + ')'

    __repr__ = __str__


class CreateSessionParameters(object):
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

    __slots__ = [
        "ClientDescription",
        "ServerUri",
        "EndpointUrl",
        "SessionName",
        "ClientNonce",
        "ClientCertificate",
        "RequestedSessionTimeout",
        "MaxResponseMessageSize",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.ClientDescription = ApplicationDescription()
        self.ServerUri = ''
        self.EndpointUrl = ''
        self.SessionName = ''
        self.ClientNonce = b''
        self.ClientCertificate = b''
        self.RequestedSessionTimeout = 0
        self.MaxResponseMessageSize = 0

    def to_binary(self):
        packet = []
        packet.append(self.ClientDescription.to_binary())
        packet.append(pack_string(self.ServerUri))
        packet.append(pack_string(self.EndpointUrl))
        packet.append(pack_string(self.SessionName))
        packet.append(pack_bytes(self.ClientNonce))
        packet.append(pack_bytes(self.ClientCertificate))
        packet.append(uatype_Double.pack(self.RequestedSessionTimeout))
        packet.append(uatype_UInt32.pack(self.MaxResponseMessageSize))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return CreateSessionParameters(data)

    def _binary_init(self, data):
        self.ClientDescription = ApplicationDescription.from_binary(data)
        self.ServerUri = unpack_string(data)
        self.EndpointUrl = unpack_string(data)
        self.SessionName = unpack_string(data)
        self.ClientNonce = unpack_bytes(data)
        self.ClientCertificate = unpack_bytes(data)
        self.RequestedSessionTimeout = uatype_Double.unpack(data.read(8))[0]
        self.MaxResponseMessageSize = uatype_UInt32.unpack(data.read(4))[0]

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


class CreateSessionRequest(object):
    '''
    Creates a new session with the server.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: CreateSessionParameters
    '''

    __slots__ = [
        "TypeId",
        "RequestHeader",
        "Parameters",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.CreateSessionRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = CreateSessionParameters()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return CreateSessionRequest(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.RequestHeader = RequestHeader.from_binary(data)
        self.Parameters = CreateSessionParameters.from_binary(data)

    def __str__(self):
        return 'CreateSessionRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'RequestHeader:' + str(self.RequestHeader) + ', ' + \
             'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class CreateSessionResult(object):
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

    __slots__ = [
        "SessionId",
        "AuthenticationToken",
        "RevisedSessionTimeout",
        "ServerNonce",
        "ServerCertificate",
        "ServerEndpoints",
        "ServerSoftwareCertificates",
        "ServerSignature",
        "MaxRequestMessageSize",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.SessionId = NodeId()
        self.AuthenticationToken = NodeId()
        self.RevisedSessionTimeout = 0
        self.ServerNonce = b''
        self.ServerCertificate = b''
        self.ServerEndpoints = []
        self.ServerSoftwareCertificates = []
        self.ServerSignature = SignatureData()
        self.MaxRequestMessageSize = 0

    def to_binary(self):
        packet = []
        packet.append(self.SessionId.to_binary())
        packet.append(self.AuthenticationToken.to_binary())
        packet.append(uatype_Double.pack(self.RevisedSessionTimeout))
        packet.append(pack_bytes(self.ServerNonce))
        packet.append(pack_bytes(self.ServerCertificate))
        packet.append(uatype_Int32.pack(len(self.ServerEndpoints)))
        for fieldname in self.ServerEndpoints:
            packet.append(fieldname.to_binary())
        packet.append(uatype_Int32.pack(len(self.ServerSoftwareCertificates)))
        for fieldname in self.ServerSoftwareCertificates:
            packet.append(fieldname.to_binary())
        packet.append(self.ServerSignature.to_binary())
        packet.append(uatype_UInt32.pack(self.MaxRequestMessageSize))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return CreateSessionResult(data)

    def _binary_init(self, data):
        self.SessionId = NodeId.from_binary(data)
        self.AuthenticationToken = NodeId.from_binary(data)
        self.RevisedSessionTimeout = uatype_Double.unpack(data.read(8))[0]
        self.ServerNonce = unpack_bytes(data)
        self.ServerCertificate = unpack_bytes(data)
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(EndpointDescription.from_binary(data))
        self.ServerEndpoints = array
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(SignedSoftwareCertificate.from_binary(data))
        self.ServerSoftwareCertificates = array
        self.ServerSignature = SignatureData.from_binary(data)
        self.MaxRequestMessageSize = uatype_UInt32.unpack(data.read(4))[0]

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


class CreateSessionResponse(object):
    '''
    Creates a new session with the server.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    :ivar Parameters:
    :vartype Parameters: CreateSessionResult
    '''

    __slots__ = [
        "TypeId",
        "ResponseHeader",
        "Parameters",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.CreateSessionResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = CreateSessionResult()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return CreateSessionResponse(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.ResponseHeader = ResponseHeader.from_binary(data)
        self.Parameters = CreateSessionResult.from_binary(data)

    def __str__(self):
        return 'CreateSessionResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
             'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class UserIdentityToken(object):
    '''
    A base type for a user identity token.

    :ivar PolicyId:
    :vartype PolicyId: String
    '''

    __slots__ = [
        "PolicyId",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.PolicyId = ''

    def to_binary(self):
        packet = []
        packet.append(pack_string(self.PolicyId))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return UserIdentityToken(data)

    def _binary_init(self, data):
        self.PolicyId = unpack_string(data)

    def __str__(self):
        return 'UserIdentityToken(' + 'PolicyId:' + str(self.PolicyId) + ')'

    __repr__ = __str__


class AnonymousIdentityToken(object):
    '''
    A token representing an anonymous user.

    :ivar PolicyId:
    :vartype PolicyId: String
    '''

    __slots__ = [
        "PolicyId",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.PolicyId = ''

    def to_binary(self):
        packet = []
        packet.append(pack_string(self.PolicyId))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return AnonymousIdentityToken(data)

    def _binary_init(self, data):
        self.PolicyId = unpack_string(data)

    def __str__(self):
        return 'AnonymousIdentityToken(' + 'PolicyId:' + str(self.PolicyId) + ')'

    __repr__ = __str__


class UserNameIdentityToken(object):
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

    __slots__ = [
        "PolicyId",
        "UserName",
        "Password",
        "EncryptionAlgorithm",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.PolicyId = ''
        self.UserName = ''
        self.Password = b''
        self.EncryptionAlgorithm = ''

    def to_binary(self):
        packet = []
        packet.append(pack_string(self.PolicyId))
        packet.append(pack_string(self.UserName))
        packet.append(pack_bytes(self.Password))
        packet.append(pack_string(self.EncryptionAlgorithm))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return UserNameIdentityToken(data)

    def _binary_init(self, data):
        self.PolicyId = unpack_string(data)
        self.UserName = unpack_string(data)
        self.Password = unpack_bytes(data)
        self.EncryptionAlgorithm = unpack_string(data)

    def __str__(self):
        return 'UserNameIdentityToken(' + 'PolicyId:' + str(self.PolicyId) + ', ' + \
             'UserName:' + str(self.UserName) + ', ' + \
             'Password:' + str(self.Password) + ', ' + \
             'EncryptionAlgorithm:' + str(self.EncryptionAlgorithm) + ')'

    __repr__ = __str__


class X509IdentityToken(object):
    '''
    A token representing a user identified by an X509 certificate.

    :ivar PolicyId:
    :vartype PolicyId: String
    :ivar CertificateData:
    :vartype CertificateData: ByteString
    '''

    __slots__ = [
        "PolicyId",
        "CertificateData",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.PolicyId = ''
        self.CertificateData = b''

    def to_binary(self):
        packet = []
        packet.append(pack_string(self.PolicyId))
        packet.append(pack_bytes(self.CertificateData))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return X509IdentityToken(data)

    def _binary_init(self, data):
        self.PolicyId = unpack_string(data)
        self.CertificateData = unpack_bytes(data)

    def __str__(self):
        return 'X509IdentityToken(' + 'PolicyId:' + str(self.PolicyId) + ', ' + \
             'CertificateData:' + str(self.CertificateData) + ')'

    __repr__ = __str__


class KerberosIdentityToken(object):
    '''
    :ivar PolicyId:
    :vartype PolicyId: String
    :ivar TicketData:
    :vartype TicketData: ByteString
    '''

    __slots__ = [
        "PolicyId",
        "TicketData",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.PolicyId = ''
        self.TicketData = b''

    def to_binary(self):
        packet = []
        packet.append(pack_string(self.PolicyId))
        packet.append(pack_bytes(self.TicketData))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return KerberosIdentityToken(data)

    def _binary_init(self, data):
        self.PolicyId = unpack_string(data)
        self.TicketData = unpack_bytes(data)

    def __str__(self):
        return 'KerberosIdentityToken(' + 'PolicyId:' + str(self.PolicyId) + ', ' + \
             'TicketData:' + str(self.TicketData) + ')'

    __repr__ = __str__


class IssuedIdentityToken(object):
    '''
    A token representing a user identified by a WS-Security XML token.

    :ivar PolicyId:
    :vartype PolicyId: String
    :ivar TokenData:
    :vartype TokenData: ByteString
    :ivar EncryptionAlgorithm:
    :vartype EncryptionAlgorithm: String
    '''

    __slots__ = [
        "PolicyId",
        "TokenData",
        "EncryptionAlgorithm",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.PolicyId = ''
        self.TokenData = b''
        self.EncryptionAlgorithm = ''

    def to_binary(self):
        packet = []
        packet.append(pack_string(self.PolicyId))
        packet.append(pack_bytes(self.TokenData))
        packet.append(pack_string(self.EncryptionAlgorithm))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return IssuedIdentityToken(data)

    def _binary_init(self, data):
        self.PolicyId = unpack_string(data)
        self.TokenData = unpack_bytes(data)
        self.EncryptionAlgorithm = unpack_string(data)

    def __str__(self):
        return 'IssuedIdentityToken(' + 'PolicyId:' + str(self.PolicyId) + ', ' + \
             'TokenData:' + str(self.TokenData) + ', ' + \
             'EncryptionAlgorithm:' + str(self.EncryptionAlgorithm) + ')'

    __repr__ = __str__


class ActivateSessionParameters(object):
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

    __slots__ = [
        "ClientSignature",
        "ClientSoftwareCertificates",
        "LocaleIds",
        "UserIdentityToken",
        "UserTokenSignature",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.ClientSignature = SignatureData()
        self.ClientSoftwareCertificates = []
        self.LocaleIds = []
        self.UserIdentityToken = None
        self.UserTokenSignature = SignatureData()

    def to_binary(self):
        packet = []
        packet.append(self.ClientSignature.to_binary())
        packet.append(uatype_Int32.pack(len(self.ClientSoftwareCertificates)))
        for fieldname in self.ClientSoftwareCertificates:
            packet.append(fieldname.to_binary())
        packet.append(uatype_Int32.pack(len(self.LocaleIds)))
        for fieldname in self.LocaleIds:
            packet.append(pack_string(fieldname))
        packet.append(extensionobject_to_binary(self.UserIdentityToken))
        packet.append(self.UserTokenSignature.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return ActivateSessionParameters(data)

    def _binary_init(self, data):
        self.ClientSignature = SignatureData.from_binary(data)
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(SignedSoftwareCertificate.from_binary(data))
        self.ClientSoftwareCertificates = array
        self.LocaleIds = unpack_uatype_array('String', data)
        self.UserIdentityToken = extensionobject_from_binary(data)
        self.UserTokenSignature = SignatureData.from_binary(data)

    def __str__(self):
        return 'ActivateSessionParameters(' + 'ClientSignature:' + str(self.ClientSignature) + ', ' + \
             'ClientSoftwareCertificates:' + str(self.ClientSoftwareCertificates) + ', ' + \
             'LocaleIds:' + str(self.LocaleIds) + ', ' + \
             'UserIdentityToken:' + str(self.UserIdentityToken) + ', ' + \
             'UserTokenSignature:' + str(self.UserTokenSignature) + ')'

    __repr__ = __str__


class ActivateSessionRequest(object):
    '''
    Activates a session with the server.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: ActivateSessionParameters
    '''

    __slots__ = [
        "TypeId",
        "RequestHeader",
        "Parameters",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.ActivateSessionRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = ActivateSessionParameters()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return ActivateSessionRequest(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.RequestHeader = RequestHeader.from_binary(data)
        self.Parameters = ActivateSessionParameters.from_binary(data)

    def __str__(self):
        return 'ActivateSessionRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'RequestHeader:' + str(self.RequestHeader) + ', ' + \
             'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class ActivateSessionResult(object):
    '''
    :ivar ServerNonce:
    :vartype ServerNonce: ByteString
    :ivar Results:
    :vartype Results: StatusCode
    :ivar DiagnosticInfos:
    :vartype DiagnosticInfos: DiagnosticInfo
    '''

    __slots__ = [
        "ServerNonce",
        "Results",
        "DiagnosticInfos",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.ServerNonce = b''
        self.Results = []
        self.DiagnosticInfos = []

    def to_binary(self):
        packet = []
        packet.append(pack_bytes(self.ServerNonce))
        packet.append(uatype_Int32.pack(len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(uatype_Int32.pack(len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return ActivateSessionResult(data)

    def _binary_init(self, data):
        self.ServerNonce = unpack_bytes(data)
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(StatusCode.from_binary(data))
        self.Results = array
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(DiagnosticInfo.from_binary(data))
        self.DiagnosticInfos = array

    def __str__(self):
        return 'ActivateSessionResult(' + 'ServerNonce:' + str(self.ServerNonce) + ', ' + \
             'Results:' + str(self.Results) + ', ' + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'

    __repr__ = __str__


class ActivateSessionResponse(object):
    '''
    Activates a session with the server.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    :ivar Parameters:
    :vartype Parameters: ActivateSessionResult
    '''

    __slots__ = [
        "TypeId",
        "ResponseHeader",
        "Parameters",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.ActivateSessionResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = ActivateSessionResult()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return ActivateSessionResponse(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.ResponseHeader = ResponseHeader.from_binary(data)
        self.Parameters = ActivateSessionResult.from_binary(data)

    def __str__(self):
        return 'ActivateSessionResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
             'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class CloseSessionRequest(object):
    '''
    Closes a session with the server.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar DeleteSubscriptions:
    :vartype DeleteSubscriptions: Boolean
    '''

    __slots__ = [
        "TypeId",
        "RequestHeader",
        "DeleteSubscriptions",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.CloseSessionRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.DeleteSubscriptions = True

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(uatype_Boolean.pack(self.DeleteSubscriptions))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return CloseSessionRequest(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.RequestHeader = RequestHeader.from_binary(data)
        self.DeleteSubscriptions = uatype_Boolean.unpack(data.read(1))[0]

    def __str__(self):
        return 'CloseSessionRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'RequestHeader:' + str(self.RequestHeader) + ', ' + \
             'DeleteSubscriptions:' + str(self.DeleteSubscriptions) + ')'

    __repr__ = __str__


class CloseSessionResponse(object):
    '''
    Closes a session with the server.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    '''

    __slots__ = [
        "TypeId",
        "ResponseHeader",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.CloseSessionResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return CloseSessionResponse(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.ResponseHeader = ResponseHeader.from_binary(data)

    def __str__(self):
        return 'CloseSessionResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'ResponseHeader:' + str(self.ResponseHeader) + ')'

    __repr__ = __str__


class CancelParameters(object):
    '''
    :ivar RequestHandle:
    :vartype RequestHandle: UInt32
    '''

    __slots__ = [
        "RequestHandle",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.RequestHandle = 0

    def to_binary(self):
        packet = []
        packet.append(uatype_UInt32.pack(self.RequestHandle))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return CancelParameters(data)

    def _binary_init(self, data):
        self.RequestHandle = uatype_UInt32.unpack(data.read(4))[0]

    def __str__(self):
        return 'CancelParameters(' + 'RequestHandle:' + str(self.RequestHandle) + ')'

    __repr__ = __str__


class CancelRequest(object):
    '''
    Cancels an outstanding request.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: CancelParameters
    '''

    __slots__ = [
        "TypeId",
        "RequestHeader",
        "Parameters",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.CancelRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = CancelParameters()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return CancelRequest(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.RequestHeader = RequestHeader.from_binary(data)
        self.Parameters = CancelParameters.from_binary(data)

    def __str__(self):
        return 'CancelRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'RequestHeader:' + str(self.RequestHeader) + ', ' + \
             'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class CancelResult(object):
    '''
    :ivar CancelCount:
    :vartype CancelCount: UInt32
    '''

    __slots__ = [
        "CancelCount",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.CancelCount = 0

    def to_binary(self):
        packet = []
        packet.append(uatype_UInt32.pack(self.CancelCount))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return CancelResult(data)

    def _binary_init(self, data):
        self.CancelCount = uatype_UInt32.unpack(data.read(4))[0]

    def __str__(self):
        return 'CancelResult(' + 'CancelCount:' + str(self.CancelCount) + ')'

    __repr__ = __str__


class CancelResponse(object):
    '''
    Cancels an outstanding request.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    :ivar Parameters:
    :vartype Parameters: CancelResult
    '''

    __slots__ = [
        "TypeId",
        "ResponseHeader",
        "Parameters",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.CancelResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = CancelResult()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return CancelResponse(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.ResponseHeader = ResponseHeader.from_binary(data)
        self.Parameters = CancelResult.from_binary(data)

    def __str__(self):
        return 'CancelResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
             'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class NodeAttributes(object):
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

    __slots__ = [
        "SpecifiedAttributes",
        "DisplayName",
        "Description",
        "WriteMask",
        "UserWriteMask",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.SpecifiedAttributes = 0
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self.UserWriteMask = 0

    def to_binary(self):
        packet = []
        packet.append(uatype_UInt32.pack(self.SpecifiedAttributes))
        packet.append(self.DisplayName.to_binary())
        packet.append(self.Description.to_binary())
        packet.append(uatype_UInt32.pack(self.WriteMask))
        packet.append(uatype_UInt32.pack(self.UserWriteMask))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return NodeAttributes(data)

    def _binary_init(self, data):
        self.SpecifiedAttributes = uatype_UInt32.unpack(data.read(4))[0]
        self.DisplayName = LocalizedText.from_binary(data)
        self.Description = LocalizedText.from_binary(data)
        self.WriteMask = uatype_UInt32.unpack(data.read(4))[0]
        self.UserWriteMask = uatype_UInt32.unpack(data.read(4))[0]

    def __str__(self):
        return 'NodeAttributes(' + 'SpecifiedAttributes:' + str(self.SpecifiedAttributes) + ', ' + \
             'DisplayName:' + str(self.DisplayName) + ', ' + \
             'Description:' + str(self.Description) + ', ' + \
             'WriteMask:' + str(self.WriteMask) + ', ' + \
             'UserWriteMask:' + str(self.UserWriteMask) + ')'

    __repr__ = __str__


class ObjectAttributes(object):
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

    __slots__ = [
        "SpecifiedAttributes",
        "DisplayName",
        "Description",
        "WriteMask",
        "UserWriteMask",
        "EventNotifier",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.SpecifiedAttributes = 0
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self.UserWriteMask = 0
        self.EventNotifier = 0

    def to_binary(self):
        packet = []
        packet.append(uatype_UInt32.pack(self.SpecifiedAttributes))
        packet.append(self.DisplayName.to_binary())
        packet.append(self.Description.to_binary())
        packet.append(uatype_UInt32.pack(self.WriteMask))
        packet.append(uatype_UInt32.pack(self.UserWriteMask))
        packet.append(uatype_Byte.pack(self.EventNotifier))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return ObjectAttributes(data)

    def _binary_init(self, data):
        self.SpecifiedAttributes = uatype_UInt32.unpack(data.read(4))[0]
        self.DisplayName = LocalizedText.from_binary(data)
        self.Description = LocalizedText.from_binary(data)
        self.WriteMask = uatype_UInt32.unpack(data.read(4))[0]
        self.UserWriteMask = uatype_UInt32.unpack(data.read(4))[0]
        self.EventNotifier = uatype_Byte.unpack(data.read(1))[0]

    def __str__(self):
        return 'ObjectAttributes(' + 'SpecifiedAttributes:' + str(self.SpecifiedAttributes) + ', ' + \
             'DisplayName:' + str(self.DisplayName) + ', ' + \
             'Description:' + str(self.Description) + ', ' + \
             'WriteMask:' + str(self.WriteMask) + ', ' + \
             'UserWriteMask:' + str(self.UserWriteMask) + ', ' + \
             'EventNotifier:' + str(self.EventNotifier) + ')'

    __repr__ = __str__


class VariableAttributes(object):
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

    __slots__ = [
        "SpecifiedAttributes",
        "DisplayName",
        "Description",
        "WriteMask",
        "UserWriteMask",
        "Value",
        "DataType",
        "ValueRank",
        "ArrayDimensions",
        "AccessLevel",
        "UserAccessLevel",
        "MinimumSamplingInterval",
        "Historizing",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
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

    def to_binary(self):
        packet = []
        packet.append(uatype_UInt32.pack(self.SpecifiedAttributes))
        packet.append(self.DisplayName.to_binary())
        packet.append(self.Description.to_binary())
        packet.append(uatype_UInt32.pack(self.WriteMask))
        packet.append(uatype_UInt32.pack(self.UserWriteMask))
        packet.append(self.Value.to_binary())
        packet.append(self.DataType.to_binary())
        packet.append(uatype_Int32.pack(self.ValueRank))
        packet.append(uatype_Int32.pack(len(self.ArrayDimensions)))
        for fieldname in self.ArrayDimensions:
            packet.append(uatype_UInt32.pack(fieldname))
        packet.append(uatype_Byte.pack(self.AccessLevel))
        packet.append(uatype_Byte.pack(self.UserAccessLevel))
        packet.append(uatype_Double.pack(self.MinimumSamplingInterval))
        packet.append(uatype_Boolean.pack(self.Historizing))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return VariableAttributes(data)

    def _binary_init(self, data):
        self.SpecifiedAttributes = uatype_UInt32.unpack(data.read(4))[0]
        self.DisplayName = LocalizedText.from_binary(data)
        self.Description = LocalizedText.from_binary(data)
        self.WriteMask = uatype_UInt32.unpack(data.read(4))[0]
        self.UserWriteMask = uatype_UInt32.unpack(data.read(4))[0]
        self.Value = Variant.from_binary(data)
        self.DataType = NodeId.from_binary(data)
        self.ValueRank = uatype_Int32.unpack(data.read(4))[0]
        self.ArrayDimensions = unpack_uatype_array('UInt32', data)
        self.AccessLevel = uatype_Byte.unpack(data.read(1))[0]
        self.UserAccessLevel = uatype_Byte.unpack(data.read(1))[0]
        self.MinimumSamplingInterval = uatype_Double.unpack(data.read(8))[0]
        self.Historizing = uatype_Boolean.unpack(data.read(1))[0]

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


class MethodAttributes(object):
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

    __slots__ = [
        "SpecifiedAttributes",
        "DisplayName",
        "Description",
        "WriteMask",
        "UserWriteMask",
        "Executable",
        "UserExecutable",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.SpecifiedAttributes = 0
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self.UserWriteMask = 0
        self.Executable = True
        self.UserExecutable = True

    def to_binary(self):
        packet = []
        packet.append(uatype_UInt32.pack(self.SpecifiedAttributes))
        packet.append(self.DisplayName.to_binary())
        packet.append(self.Description.to_binary())
        packet.append(uatype_UInt32.pack(self.WriteMask))
        packet.append(uatype_UInt32.pack(self.UserWriteMask))
        packet.append(uatype_Boolean.pack(self.Executable))
        packet.append(uatype_Boolean.pack(self.UserExecutable))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return MethodAttributes(data)

    def _binary_init(self, data):
        self.SpecifiedAttributes = uatype_UInt32.unpack(data.read(4))[0]
        self.DisplayName = LocalizedText.from_binary(data)
        self.Description = LocalizedText.from_binary(data)
        self.WriteMask = uatype_UInt32.unpack(data.read(4))[0]
        self.UserWriteMask = uatype_UInt32.unpack(data.read(4))[0]
        self.Executable = uatype_Boolean.unpack(data.read(1))[0]
        self.UserExecutable = uatype_Boolean.unpack(data.read(1))[0]

    def __str__(self):
        return 'MethodAttributes(' + 'SpecifiedAttributes:' + str(self.SpecifiedAttributes) + ', ' + \
             'DisplayName:' + str(self.DisplayName) + ', ' + \
             'Description:' + str(self.Description) + ', ' + \
             'WriteMask:' + str(self.WriteMask) + ', ' + \
             'UserWriteMask:' + str(self.UserWriteMask) + ', ' + \
             'Executable:' + str(self.Executable) + ', ' + \
             'UserExecutable:' + str(self.UserExecutable) + ')'

    __repr__ = __str__


class ObjectTypeAttributes(object):
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

    __slots__ = [
        "SpecifiedAttributes",
        "DisplayName",
        "Description",
        "WriteMask",
        "UserWriteMask",
        "IsAbstract",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.SpecifiedAttributes = 0
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self.UserWriteMask = 0
        self.IsAbstract = True

    def to_binary(self):
        packet = []
        packet.append(uatype_UInt32.pack(self.SpecifiedAttributes))
        packet.append(self.DisplayName.to_binary())
        packet.append(self.Description.to_binary())
        packet.append(uatype_UInt32.pack(self.WriteMask))
        packet.append(uatype_UInt32.pack(self.UserWriteMask))
        packet.append(uatype_Boolean.pack(self.IsAbstract))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return ObjectTypeAttributes(data)

    def _binary_init(self, data):
        self.SpecifiedAttributes = uatype_UInt32.unpack(data.read(4))[0]
        self.DisplayName = LocalizedText.from_binary(data)
        self.Description = LocalizedText.from_binary(data)
        self.WriteMask = uatype_UInt32.unpack(data.read(4))[0]
        self.UserWriteMask = uatype_UInt32.unpack(data.read(4))[0]
        self.IsAbstract = uatype_Boolean.unpack(data.read(1))[0]

    def __str__(self):
        return 'ObjectTypeAttributes(' + 'SpecifiedAttributes:' + str(self.SpecifiedAttributes) + ', ' + \
             'DisplayName:' + str(self.DisplayName) + ', ' + \
             'Description:' + str(self.Description) + ', ' + \
             'WriteMask:' + str(self.WriteMask) + ', ' + \
             'UserWriteMask:' + str(self.UserWriteMask) + ', ' + \
             'IsAbstract:' + str(self.IsAbstract) + ')'

    __repr__ = __str__


class VariableTypeAttributes(object):
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

    __slots__ = [
        "SpecifiedAttributes",
        "DisplayName",
        "Description",
        "WriteMask",
        "UserWriteMask",
        "Value",
        "DataType",
        "ValueRank",
        "ArrayDimensions",
        "IsAbstract",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
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

    def to_binary(self):
        packet = []
        packet.append(uatype_UInt32.pack(self.SpecifiedAttributes))
        packet.append(self.DisplayName.to_binary())
        packet.append(self.Description.to_binary())
        packet.append(uatype_UInt32.pack(self.WriteMask))
        packet.append(uatype_UInt32.pack(self.UserWriteMask))
        packet.append(self.Value.to_binary())
        packet.append(self.DataType.to_binary())
        packet.append(uatype_Int32.pack(self.ValueRank))
        packet.append(uatype_Int32.pack(len(self.ArrayDimensions)))
        for fieldname in self.ArrayDimensions:
            packet.append(uatype_UInt32.pack(fieldname))
        packet.append(uatype_Boolean.pack(self.IsAbstract))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return VariableTypeAttributes(data)

    def _binary_init(self, data):
        self.SpecifiedAttributes = uatype_UInt32.unpack(data.read(4))[0]
        self.DisplayName = LocalizedText.from_binary(data)
        self.Description = LocalizedText.from_binary(data)
        self.WriteMask = uatype_UInt32.unpack(data.read(4))[0]
        self.UserWriteMask = uatype_UInt32.unpack(data.read(4))[0]
        self.Value = Variant.from_binary(data)
        self.DataType = NodeId.from_binary(data)
        self.ValueRank = uatype_Int32.unpack(data.read(4))[0]
        self.ArrayDimensions = unpack_uatype_array('UInt32', data)
        self.IsAbstract = uatype_Boolean.unpack(data.read(1))[0]

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


class ReferenceTypeAttributes(object):
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

    __slots__ = [
        "SpecifiedAttributes",
        "DisplayName",
        "Description",
        "WriteMask",
        "UserWriteMask",
        "IsAbstract",
        "Symmetric",
        "InverseName",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.SpecifiedAttributes = 0
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self.UserWriteMask = 0
        self.IsAbstract = True
        self.Symmetric = True
        self.InverseName = LocalizedText()

    def to_binary(self):
        packet = []
        packet.append(uatype_UInt32.pack(self.SpecifiedAttributes))
        packet.append(self.DisplayName.to_binary())
        packet.append(self.Description.to_binary())
        packet.append(uatype_UInt32.pack(self.WriteMask))
        packet.append(uatype_UInt32.pack(self.UserWriteMask))
        packet.append(uatype_Boolean.pack(self.IsAbstract))
        packet.append(uatype_Boolean.pack(self.Symmetric))
        packet.append(self.InverseName.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return ReferenceTypeAttributes(data)

    def _binary_init(self, data):
        self.SpecifiedAttributes = uatype_UInt32.unpack(data.read(4))[0]
        self.DisplayName = LocalizedText.from_binary(data)
        self.Description = LocalizedText.from_binary(data)
        self.WriteMask = uatype_UInt32.unpack(data.read(4))[0]
        self.UserWriteMask = uatype_UInt32.unpack(data.read(4))[0]
        self.IsAbstract = uatype_Boolean.unpack(data.read(1))[0]
        self.Symmetric = uatype_Boolean.unpack(data.read(1))[0]
        self.InverseName = LocalizedText.from_binary(data)

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


class DataTypeAttributes(object):
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

    __slots__ = [
        "SpecifiedAttributes",
        "DisplayName",
        "Description",
        "WriteMask",
        "UserWriteMask",
        "IsAbstract",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.SpecifiedAttributes = 0
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self.UserWriteMask = 0
        self.IsAbstract = True

    def to_binary(self):
        packet = []
        packet.append(uatype_UInt32.pack(self.SpecifiedAttributes))
        packet.append(self.DisplayName.to_binary())
        packet.append(self.Description.to_binary())
        packet.append(uatype_UInt32.pack(self.WriteMask))
        packet.append(uatype_UInt32.pack(self.UserWriteMask))
        packet.append(uatype_Boolean.pack(self.IsAbstract))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return DataTypeAttributes(data)

    def _binary_init(self, data):
        self.SpecifiedAttributes = uatype_UInt32.unpack(data.read(4))[0]
        self.DisplayName = LocalizedText.from_binary(data)
        self.Description = LocalizedText.from_binary(data)
        self.WriteMask = uatype_UInt32.unpack(data.read(4))[0]
        self.UserWriteMask = uatype_UInt32.unpack(data.read(4))[0]
        self.IsAbstract = uatype_Boolean.unpack(data.read(1))[0]

    def __str__(self):
        return 'DataTypeAttributes(' + 'SpecifiedAttributes:' + str(self.SpecifiedAttributes) + ', ' + \
             'DisplayName:' + str(self.DisplayName) + ', ' + \
             'Description:' + str(self.Description) + ', ' + \
             'WriteMask:' + str(self.WriteMask) + ', ' + \
             'UserWriteMask:' + str(self.UserWriteMask) + ', ' + \
             'IsAbstract:' + str(self.IsAbstract) + ')'

    __repr__ = __str__


class ViewAttributes(object):
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

    __slots__ = [
        "SpecifiedAttributes",
        "DisplayName",
        "Description",
        "WriteMask",
        "UserWriteMask",
        "ContainsNoLoops",
        "EventNotifier",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.SpecifiedAttributes = 0
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self.UserWriteMask = 0
        self.ContainsNoLoops = True
        self.EventNotifier = 0

    def to_binary(self):
        packet = []
        packet.append(uatype_UInt32.pack(self.SpecifiedAttributes))
        packet.append(self.DisplayName.to_binary())
        packet.append(self.Description.to_binary())
        packet.append(uatype_UInt32.pack(self.WriteMask))
        packet.append(uatype_UInt32.pack(self.UserWriteMask))
        packet.append(uatype_Boolean.pack(self.ContainsNoLoops))
        packet.append(uatype_Byte.pack(self.EventNotifier))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return ViewAttributes(data)

    def _binary_init(self, data):
        self.SpecifiedAttributes = uatype_UInt32.unpack(data.read(4))[0]
        self.DisplayName = LocalizedText.from_binary(data)
        self.Description = LocalizedText.from_binary(data)
        self.WriteMask = uatype_UInt32.unpack(data.read(4))[0]
        self.UserWriteMask = uatype_UInt32.unpack(data.read(4))[0]
        self.ContainsNoLoops = uatype_Boolean.unpack(data.read(1))[0]
        self.EventNotifier = uatype_Byte.unpack(data.read(1))[0]

    def __str__(self):
        return 'ViewAttributes(' + 'SpecifiedAttributes:' + str(self.SpecifiedAttributes) + ', ' + \
             'DisplayName:' + str(self.DisplayName) + ', ' + \
             'Description:' + str(self.Description) + ', ' + \
             'WriteMask:' + str(self.WriteMask) + ', ' + \
             'UserWriteMask:' + str(self.UserWriteMask) + ', ' + \
             'ContainsNoLoops:' + str(self.ContainsNoLoops) + ', ' + \
             'EventNotifier:' + str(self.EventNotifier) + ')'

    __repr__ = __str__


class AddNodesItem(object):
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

    __slots__ = [
        "ParentNodeId",
        "ReferenceTypeId",
        "RequestedNewNodeId",
        "BrowseName",
        "NodeClass",
        "NodeAttributes",
        "TypeDefinition",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.ParentNodeId = ExpandedNodeId()
        self.ReferenceTypeId = NodeId()
        self.RequestedNewNodeId = ExpandedNodeId()
        self.BrowseName = QualifiedName()
        self.NodeClass = 0
        self.NodeAttributes = None
        self.TypeDefinition = ExpandedNodeId()

    def to_binary(self):
        packet = []
        packet.append(self.ParentNodeId.to_binary())
        packet.append(self.ReferenceTypeId.to_binary())
        packet.append(self.RequestedNewNodeId.to_binary())
        packet.append(self.BrowseName.to_binary())
        packet.append(uatype_UInt32.pack(self.NodeClass))
        packet.append(extensionobject_to_binary(self.NodeAttributes))
        packet.append(self.TypeDefinition.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return AddNodesItem(data)

    def _binary_init(self, data):
        self.ParentNodeId = ExpandedNodeId.from_binary(data)
        self.ReferenceTypeId = NodeId.from_binary(data)
        self.RequestedNewNodeId = ExpandedNodeId.from_binary(data)
        self.BrowseName = QualifiedName.from_binary(data)
        self.NodeClass = uatype_UInt32.unpack(data.read(4))[0]
        self.NodeAttributes = extensionobject_from_binary(data)
        self.TypeDefinition = ExpandedNodeId.from_binary(data)

    def __str__(self):
        return 'AddNodesItem(' + 'ParentNodeId:' + str(self.ParentNodeId) + ', ' + \
             'ReferenceTypeId:' + str(self.ReferenceTypeId) + ', ' + \
             'RequestedNewNodeId:' + str(self.RequestedNewNodeId) + ', ' + \
             'BrowseName:' + str(self.BrowseName) + ', ' + \
             'NodeClass:' + str(self.NodeClass) + ', ' + \
             'NodeAttributes:' + str(self.NodeAttributes) + ', ' + \
             'TypeDefinition:' + str(self.TypeDefinition) + ')'

    __repr__ = __str__


class AddNodesResult(object):
    '''
    A result of an add node operation.

    :ivar StatusCode:
    :vartype StatusCode: StatusCode
    :ivar AddedNodeId:
    :vartype AddedNodeId: NodeId
    '''

    __slots__ = [
        "StatusCode",
        "AddedNodeId",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.StatusCode = StatusCode()
        self.AddedNodeId = NodeId()

    def to_binary(self):
        packet = []
        packet.append(self.StatusCode.to_binary())
        packet.append(self.AddedNodeId.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return AddNodesResult(data)

    def _binary_init(self, data):
        self.StatusCode = StatusCode.from_binary(data)
        self.AddedNodeId = NodeId.from_binary(data)

    def __str__(self):
        return 'AddNodesResult(' + 'StatusCode:' + str(self.StatusCode) + ', ' + \
             'AddedNodeId:' + str(self.AddedNodeId) + ')'

    __repr__ = __str__


class AddNodesParameters(object):
    '''
    :ivar NodesToAdd:
    :vartype NodesToAdd: AddNodesItem
    '''

    __slots__ = [
        "NodesToAdd",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.NodesToAdd = []

    def to_binary(self):
        packet = []
        packet.append(uatype_Int32.pack(len(self.NodesToAdd)))
        for fieldname in self.NodesToAdd:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return AddNodesParameters(data)

    def _binary_init(self, data):
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(AddNodesItem.from_binary(data))
        self.NodesToAdd = array

    def __str__(self):
        return 'AddNodesParameters(' + 'NodesToAdd:' + str(self.NodesToAdd) + ')'

    __repr__ = __str__


class AddNodesRequest(object):
    '''
    Adds one or more nodes to the server address space.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: AddNodesParameters
    '''

    __slots__ = [
        "TypeId",
        "RequestHeader",
        "Parameters",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.AddNodesRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = AddNodesParameters()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return AddNodesRequest(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.RequestHeader = RequestHeader.from_binary(data)
        self.Parameters = AddNodesParameters.from_binary(data)

    def __str__(self):
        return 'AddNodesRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'RequestHeader:' + str(self.RequestHeader) + ', ' + \
             'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class AddNodesResponse(object):
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

    __slots__ = [
        "TypeId",
        "ResponseHeader",
        "Results",
        "DiagnosticInfos",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.AddNodesResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Results = []
        self.DiagnosticInfos = []

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(uatype_Int32.pack(len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(uatype_Int32.pack(len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return AddNodesResponse(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.ResponseHeader = ResponseHeader.from_binary(data)
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(AddNodesResult.from_binary(data))
        self.Results = array
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(DiagnosticInfo.from_binary(data))
        self.DiagnosticInfos = array

    def __str__(self):
        return 'AddNodesResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
             'Results:' + str(self.Results) + ', ' + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'

    __repr__ = __str__


class AddReferencesItem(object):
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

    __slots__ = [
        "SourceNodeId",
        "ReferenceTypeId",
        "IsForward",
        "TargetServerUri",
        "TargetNodeId",
        "TargetNodeClass",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.SourceNodeId = NodeId()
        self.ReferenceTypeId = NodeId()
        self.IsForward = True
        self.TargetServerUri = ''
        self.TargetNodeId = ExpandedNodeId()
        self.TargetNodeClass = 0

    def to_binary(self):
        packet = []
        packet.append(self.SourceNodeId.to_binary())
        packet.append(self.ReferenceTypeId.to_binary())
        packet.append(uatype_Boolean.pack(self.IsForward))
        packet.append(pack_string(self.TargetServerUri))
        packet.append(self.TargetNodeId.to_binary())
        packet.append(uatype_UInt32.pack(self.TargetNodeClass))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return AddReferencesItem(data)

    def _binary_init(self, data):
        self.SourceNodeId = NodeId.from_binary(data)
        self.ReferenceTypeId = NodeId.from_binary(data)
        self.IsForward = uatype_Boolean.unpack(data.read(1))[0]
        self.TargetServerUri = unpack_string(data)
        self.TargetNodeId = ExpandedNodeId.from_binary(data)
        self.TargetNodeClass = uatype_UInt32.unpack(data.read(4))[0]

    def __str__(self):
        return 'AddReferencesItem(' + 'SourceNodeId:' + str(self.SourceNodeId) + ', ' + \
             'ReferenceTypeId:' + str(self.ReferenceTypeId) + ', ' + \
             'IsForward:' + str(self.IsForward) + ', ' + \
             'TargetServerUri:' + str(self.TargetServerUri) + ', ' + \
             'TargetNodeId:' + str(self.TargetNodeId) + ', ' + \
             'TargetNodeClass:' + str(self.TargetNodeClass) + ')'

    __repr__ = __str__


class AddReferencesRequest(object):
    '''
    Adds one or more references to the server address space.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar ReferencesToAdd:
    :vartype ReferencesToAdd: AddReferencesItem
    '''

    __slots__ = [
        "TypeId",
        "RequestHeader",
        "ReferencesToAdd",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.AddReferencesRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.ReferencesToAdd = []

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(uatype_Int32.pack(len(self.ReferencesToAdd)))
        for fieldname in self.ReferencesToAdd:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return AddReferencesRequest(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.RequestHeader = RequestHeader.from_binary(data)
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(AddReferencesItem.from_binary(data))
        self.ReferencesToAdd = array

    def __str__(self):
        return 'AddReferencesRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'RequestHeader:' + str(self.RequestHeader) + ', ' + \
             'ReferencesToAdd:' + str(self.ReferencesToAdd) + ')'

    __repr__ = __str__


class AddReferencesResponse(object):
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

    __slots__ = [
        "TypeId",
        "ResponseHeader",
        "Results",
        "DiagnosticInfos",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.AddReferencesResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Results = []
        self.DiagnosticInfos = []

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(uatype_Int32.pack(len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(uatype_Int32.pack(len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return AddReferencesResponse(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.ResponseHeader = ResponseHeader.from_binary(data)
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(StatusCode.from_binary(data))
        self.Results = array
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(DiagnosticInfo.from_binary(data))
        self.DiagnosticInfos = array

    def __str__(self):
        return 'AddReferencesResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
             'Results:' + str(self.Results) + ', ' + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'

    __repr__ = __str__


class DeleteNodesItem(object):
    '''
    A request to delete a node to the server address space.

    :ivar NodeId:
    :vartype NodeId: NodeId
    :ivar DeleteTargetReferences:
    :vartype DeleteTargetReferences: Boolean
    '''

    __slots__ = [
        "NodeId",
        "DeleteTargetReferences",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.NodeId = NodeId()
        self.DeleteTargetReferences = True

    def to_binary(self):
        packet = []
        packet.append(self.NodeId.to_binary())
        packet.append(uatype_Boolean.pack(self.DeleteTargetReferences))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return DeleteNodesItem(data)

    def _binary_init(self, data):
        self.NodeId = NodeId.from_binary(data)
        self.DeleteTargetReferences = uatype_Boolean.unpack(data.read(1))[0]

    def __str__(self):
        return 'DeleteNodesItem(' + 'NodeId:' + str(self.NodeId) + ', ' + \
             'DeleteTargetReferences:' + str(self.DeleteTargetReferences) + ')'

    __repr__ = __str__


class DeleteNodesParameters(object):
    '''
    :ivar NodesToDelete:
    :vartype NodesToDelete: DeleteNodesItem
    '''

    __slots__ = [
        "NodesToDelete",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.NodesToDelete = []

    def to_binary(self):
        packet = []
        packet.append(uatype_Int32.pack(len(self.NodesToDelete)))
        for fieldname in self.NodesToDelete:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return DeleteNodesParameters(data)

    def _binary_init(self, data):
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(DeleteNodesItem.from_binary(data))
        self.NodesToDelete = array

    def __str__(self):
        return 'DeleteNodesParameters(' + 'NodesToDelete:' + str(self.NodesToDelete) + ')'

    __repr__ = __str__


class DeleteNodesRequest(object):
    '''
    Delete one or more nodes from the server address space.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: DeleteNodesParameters
    '''

    __slots__ = [
        "TypeId",
        "RequestHeader",
        "Parameters",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.DeleteNodesRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = DeleteNodesParameters()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return DeleteNodesRequest(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.RequestHeader = RequestHeader.from_binary(data)
        self.Parameters = DeleteNodesParameters.from_binary(data)

    def __str__(self):
        return 'DeleteNodesRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'RequestHeader:' + str(self.RequestHeader) + ', ' + \
             'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class DeleteNodesResult(object):
    '''
    :ivar Results:
    :vartype Results: StatusCode
    :ivar DiagnosticInfos:
    :vartype DiagnosticInfos: DiagnosticInfo
    '''

    __slots__ = [
        "Results",
        "DiagnosticInfos",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.Results = []
        self.DiagnosticInfos = []

    def to_binary(self):
        packet = []
        packet.append(uatype_Int32.pack(len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(uatype_Int32.pack(len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return DeleteNodesResult(data)

    def _binary_init(self, data):
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(StatusCode.from_binary(data))
        self.Results = array
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(DiagnosticInfo.from_binary(data))
        self.DiagnosticInfos = array

    def __str__(self):
        return 'DeleteNodesResult(' + 'Results:' + str(self.Results) + ', ' + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'

    __repr__ = __str__


class DeleteNodesResponse(object):
    '''
    Delete one or more nodes from the server address space.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    :ivar Parameters:
    :vartype Parameters: DeleteNodesResult
    '''

    __slots__ = [
        "TypeId",
        "ResponseHeader",
        "Parameters",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.DeleteNodesResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = DeleteNodesResult()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return DeleteNodesResponse(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.ResponseHeader = ResponseHeader.from_binary(data)
        self.Parameters = DeleteNodesResult.from_binary(data)

    def __str__(self):
        return 'DeleteNodesResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
             'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class DeleteReferencesItem(object):
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

    __slots__ = [
        "SourceNodeId",
        "ReferenceTypeId",
        "IsForward",
        "TargetNodeId",
        "DeleteBidirectional",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.SourceNodeId = NodeId()
        self.ReferenceTypeId = NodeId()
        self.IsForward = True
        self.TargetNodeId = ExpandedNodeId()
        self.DeleteBidirectional = True

    def to_binary(self):
        packet = []
        packet.append(self.SourceNodeId.to_binary())
        packet.append(self.ReferenceTypeId.to_binary())
        packet.append(uatype_Boolean.pack(self.IsForward))
        packet.append(self.TargetNodeId.to_binary())
        packet.append(uatype_Boolean.pack(self.DeleteBidirectional))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return DeleteReferencesItem(data)

    def _binary_init(self, data):
        self.SourceNodeId = NodeId.from_binary(data)
        self.ReferenceTypeId = NodeId.from_binary(data)
        self.IsForward = uatype_Boolean.unpack(data.read(1))[0]
        self.TargetNodeId = ExpandedNodeId.from_binary(data)
        self.DeleteBidirectional = uatype_Boolean.unpack(data.read(1))[0]

    def __str__(self):
        return 'DeleteReferencesItem(' + 'SourceNodeId:' + str(self.SourceNodeId) + ', ' + \
             'ReferenceTypeId:' + str(self.ReferenceTypeId) + ', ' + \
             'IsForward:' + str(self.IsForward) + ', ' + \
             'TargetNodeId:' + str(self.TargetNodeId) + ', ' + \
             'DeleteBidirectional:' + str(self.DeleteBidirectional) + ')'

    __repr__ = __str__


class DeleteReferencesParameters(object):
    '''
    :ivar ReferencesToDelete:
    :vartype ReferencesToDelete: DeleteReferencesItem
    '''

    __slots__ = [
        "ReferencesToDelete",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.ReferencesToDelete = []

    def to_binary(self):
        packet = []
        packet.append(uatype_Int32.pack(len(self.ReferencesToDelete)))
        for fieldname in self.ReferencesToDelete:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return DeleteReferencesParameters(data)

    def _binary_init(self, data):
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(DeleteReferencesItem.from_binary(data))
        self.ReferencesToDelete = array

    def __str__(self):
        return 'DeleteReferencesParameters(' + 'ReferencesToDelete:' + str(self.ReferencesToDelete) + ')'

    __repr__ = __str__


class DeleteReferencesRequest(object):
    '''
    Delete one or more references from the server address space.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: DeleteReferencesParameters
    '''

    __slots__ = [
        "TypeId",
        "RequestHeader",
        "Parameters",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.DeleteReferencesRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = DeleteReferencesParameters()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return DeleteReferencesRequest(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.RequestHeader = RequestHeader.from_binary(data)
        self.Parameters = DeleteReferencesParameters.from_binary(data)

    def __str__(self):
        return 'DeleteReferencesRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'RequestHeader:' + str(self.RequestHeader) + ', ' + \
             'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class DeleteReferencesResult(object):
    '''
    :ivar Results:
    :vartype Results: StatusCode
    :ivar DiagnosticInfos:
    :vartype DiagnosticInfos: DiagnosticInfo
    '''

    __slots__ = [
        "Results",
        "DiagnosticInfos",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.Results = []
        self.DiagnosticInfos = []

    def to_binary(self):
        packet = []
        packet.append(uatype_Int32.pack(len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(uatype_Int32.pack(len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return DeleteReferencesResult(data)

    def _binary_init(self, data):
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(StatusCode.from_binary(data))
        self.Results = array
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(DiagnosticInfo.from_binary(data))
        self.DiagnosticInfos = array

    def __str__(self):
        return 'DeleteReferencesResult(' + 'Results:' + str(self.Results) + ', ' + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'

    __repr__ = __str__


class DeleteReferencesResponse(object):
    '''
    Delete one or more references from the server address space.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    :ivar Parameters:
    :vartype Parameters: DeleteReferencesResult
    '''

    __slots__ = [
        "TypeId",
        "ResponseHeader",
        "Parameters",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.DeleteReferencesResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = DeleteReferencesResult()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return DeleteReferencesResponse(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.ResponseHeader = ResponseHeader.from_binary(data)
        self.Parameters = DeleteReferencesResult.from_binary(data)

    def __str__(self):
        return 'DeleteReferencesResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
             'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class ViewDescription(object):
    '''
    The view to browse.

    :ivar ViewId:
    :vartype ViewId: NodeId
    :ivar Timestamp:
    :vartype Timestamp: DateTime
    :ivar ViewVersion:
    :vartype ViewVersion: UInt32
    '''

    __slots__ = [
        "ViewId",
        "Timestamp",
        "ViewVersion",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.ViewId = NodeId()
        self.Timestamp = datetime.now()
        self.ViewVersion = 0

    def to_binary(self):
        packet = []
        packet.append(self.ViewId.to_binary())
        packet.append(pack_datetime(self.Timestamp))
        packet.append(uatype_UInt32.pack(self.ViewVersion))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return ViewDescription(data)

    def _binary_init(self, data):
        self.ViewId = NodeId.from_binary(data)
        self.Timestamp = unpack_datetime(data)
        self.ViewVersion = uatype_UInt32.unpack(data.read(4))[0]

    def __str__(self):
        return 'ViewDescription(' + 'ViewId:' + str(self.ViewId) + ', ' + \
             'Timestamp:' + str(self.Timestamp) + ', ' + \
             'ViewVersion:' + str(self.ViewVersion) + ')'

    __repr__ = __str__


class BrowseDescription(object):
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

    __slots__ = [
        "NodeId",
        "BrowseDirection",
        "ReferenceTypeId",
        "IncludeSubtypes",
        "NodeClassMask",
        "ResultMask",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.NodeId = NodeId()
        self.BrowseDirection = 0
        self.ReferenceTypeId = NodeId()
        self.IncludeSubtypes = True
        self.NodeClassMask = 0
        self.ResultMask = 0

    def to_binary(self):
        packet = []
        packet.append(self.NodeId.to_binary())
        packet.append(uatype_UInt32.pack(self.BrowseDirection))
        packet.append(self.ReferenceTypeId.to_binary())
        packet.append(uatype_Boolean.pack(self.IncludeSubtypes))
        packet.append(uatype_UInt32.pack(self.NodeClassMask))
        packet.append(uatype_UInt32.pack(self.ResultMask))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return BrowseDescription(data)

    def _binary_init(self, data):
        self.NodeId = NodeId.from_binary(data)
        self.BrowseDirection = uatype_UInt32.unpack(data.read(4))[0]
        self.ReferenceTypeId = NodeId.from_binary(data)
        self.IncludeSubtypes = uatype_Boolean.unpack(data.read(1))[0]
        self.NodeClassMask = uatype_UInt32.unpack(data.read(4))[0]
        self.ResultMask = uatype_UInt32.unpack(data.read(4))[0]

    def __str__(self):
        return 'BrowseDescription(' + 'NodeId:' + str(self.NodeId) + ', ' + \
             'BrowseDirection:' + str(self.BrowseDirection) + ', ' + \
             'ReferenceTypeId:' + str(self.ReferenceTypeId) + ', ' + \
             'IncludeSubtypes:' + str(self.IncludeSubtypes) + ', ' + \
             'NodeClassMask:' + str(self.NodeClassMask) + ', ' + \
             'ResultMask:' + str(self.ResultMask) + ')'

    __repr__ = __str__


class ReferenceDescription(object):
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

    __slots__ = [
        "ReferenceTypeId",
        "IsForward",
        "NodeId",
        "BrowseName",
        "DisplayName",
        "NodeClass",
        "TypeDefinition",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.ReferenceTypeId = NodeId()
        self.IsForward = True
        self.NodeId = ExpandedNodeId()
        self.BrowseName = QualifiedName()
        self.DisplayName = LocalizedText()
        self.NodeClass = 0
        self.TypeDefinition = ExpandedNodeId()

    def to_binary(self):
        packet = []
        packet.append(self.ReferenceTypeId.to_binary())
        packet.append(uatype_Boolean.pack(self.IsForward))
        packet.append(self.NodeId.to_binary())
        packet.append(self.BrowseName.to_binary())
        packet.append(self.DisplayName.to_binary())
        packet.append(uatype_UInt32.pack(self.NodeClass))
        packet.append(self.TypeDefinition.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return ReferenceDescription(data)

    def _binary_init(self, data):
        self.ReferenceTypeId = NodeId.from_binary(data)
        self.IsForward = uatype_Boolean.unpack(data.read(1))[0]
        self.NodeId = ExpandedNodeId.from_binary(data)
        self.BrowseName = QualifiedName.from_binary(data)
        self.DisplayName = LocalizedText.from_binary(data)
        self.NodeClass = uatype_UInt32.unpack(data.read(4))[0]
        self.TypeDefinition = ExpandedNodeId.from_binary(data)

    def __str__(self):
        return 'ReferenceDescription(' + 'ReferenceTypeId:' + str(self.ReferenceTypeId) + ', ' + \
             'IsForward:' + str(self.IsForward) + ', ' + \
             'NodeId:' + str(self.NodeId) + ', ' + \
             'BrowseName:' + str(self.BrowseName) + ', ' + \
             'DisplayName:' + str(self.DisplayName) + ', ' + \
             'NodeClass:' + str(self.NodeClass) + ', ' + \
             'TypeDefinition:' + str(self.TypeDefinition) + ')'

    __repr__ = __str__


class BrowseResult(object):
    '''
    The result of a browse operation.

    :ivar StatusCode:
    :vartype StatusCode: StatusCode
    :ivar ContinuationPoint:
    :vartype ContinuationPoint: ByteString
    :ivar References:
    :vartype References: ReferenceDescription
    '''

    __slots__ = [
        "StatusCode",
        "ContinuationPoint",
        "References",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.StatusCode = StatusCode()
        self.ContinuationPoint = b''
        self.References = []

    def to_binary(self):
        packet = []
        packet.append(self.StatusCode.to_binary())
        packet.append(pack_bytes(self.ContinuationPoint))
        packet.append(uatype_Int32.pack(len(self.References)))
        for fieldname in self.References:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return BrowseResult(data)

    def _binary_init(self, data):
        self.StatusCode = StatusCode.from_binary(data)
        self.ContinuationPoint = unpack_bytes(data)
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(ReferenceDescription.from_binary(data))
        self.References = array

    def __str__(self):
        return 'BrowseResult(' + 'StatusCode:' + str(self.StatusCode) + ', ' + \
             'ContinuationPoint:' + str(self.ContinuationPoint) + ', ' + \
             'References:' + str(self.References) + ')'

    __repr__ = __str__


class BrowseParameters(object):
    '''
    :ivar View:
    :vartype View: ViewDescription
    :ivar RequestedMaxReferencesPerNode:
    :vartype RequestedMaxReferencesPerNode: UInt32
    :ivar NodesToBrowse:
    :vartype NodesToBrowse: BrowseDescription
    '''

    __slots__ = [
        "View",
        "RequestedMaxReferencesPerNode",
        "NodesToBrowse",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.View = ViewDescription()
        self.RequestedMaxReferencesPerNode = 0
        self.NodesToBrowse = []

    def to_binary(self):
        packet = []
        packet.append(self.View.to_binary())
        packet.append(uatype_UInt32.pack(self.RequestedMaxReferencesPerNode))
        packet.append(uatype_Int32.pack(len(self.NodesToBrowse)))
        for fieldname in self.NodesToBrowse:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return BrowseParameters(data)

    def _binary_init(self, data):
        self.View = ViewDescription.from_binary(data)
        self.RequestedMaxReferencesPerNode = uatype_UInt32.unpack(data.read(4))[0]
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(BrowseDescription.from_binary(data))
        self.NodesToBrowse = array

    def __str__(self):
        return 'BrowseParameters(' + 'View:' + str(self.View) + ', ' + \
             'RequestedMaxReferencesPerNode:' + str(self.RequestedMaxReferencesPerNode) + ', ' + \
             'NodesToBrowse:' + str(self.NodesToBrowse) + ')'

    __repr__ = __str__


class BrowseRequest(object):
    '''
    Browse the references for one or more nodes from the server address space.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: BrowseParameters
    '''

    __slots__ = [
        "TypeId",
        "RequestHeader",
        "Parameters",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.BrowseRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = BrowseParameters()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return BrowseRequest(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.RequestHeader = RequestHeader.from_binary(data)
        self.Parameters = BrowseParameters.from_binary(data)

    def __str__(self):
        return 'BrowseRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'RequestHeader:' + str(self.RequestHeader) + ', ' + \
             'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class BrowseResponse(object):
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

    __slots__ = [
        "TypeId",
        "ResponseHeader",
        "Results",
        "DiagnosticInfos",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.BrowseResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Results = []
        self.DiagnosticInfos = []

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(uatype_Int32.pack(len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(uatype_Int32.pack(len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return BrowseResponse(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.ResponseHeader = ResponseHeader.from_binary(data)
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(BrowseResult.from_binary(data))
        self.Results = array
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(DiagnosticInfo.from_binary(data))
        self.DiagnosticInfos = array

    def __str__(self):
        return 'BrowseResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
             'Results:' + str(self.Results) + ', ' + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'

    __repr__ = __str__


class BrowseNextParameters(object):
    '''
    :ivar ReleaseContinuationPoints:
    :vartype ReleaseContinuationPoints: Boolean
    :ivar ContinuationPoints:
    :vartype ContinuationPoints: ByteString
    '''

    __slots__ = [
        "ReleaseContinuationPoints",
        "ContinuationPoints",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.ReleaseContinuationPoints = True
        self.ContinuationPoints = []

    def to_binary(self):
        packet = []
        packet.append(uatype_Boolean.pack(self.ReleaseContinuationPoints))
        packet.append(uatype_Int32.pack(len(self.ContinuationPoints)))
        for fieldname in self.ContinuationPoints:
            packet.append(pack_bytes(fieldname))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return BrowseNextParameters(data)

    def _binary_init(self, data):
        self.ReleaseContinuationPoints = uatype_Boolean.unpack(data.read(1))[0]
        self.ContinuationPoints = unpack_uatype_array('ByteString', data)

    def __str__(self):
        return 'BrowseNextParameters(' + 'ReleaseContinuationPoints:' + str(self.ReleaseContinuationPoints) + ', ' + \
             'ContinuationPoints:' + str(self.ContinuationPoints) + ')'

    __repr__ = __str__


class BrowseNextRequest(object):
    '''
    Continues one or more browse operations.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: BrowseNextParameters
    '''

    __slots__ = [
        "TypeId",
        "RequestHeader",
        "Parameters",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.BrowseNextRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = BrowseNextParameters()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return BrowseNextRequest(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.RequestHeader = RequestHeader.from_binary(data)
        self.Parameters = BrowseNextParameters.from_binary(data)

    def __str__(self):
        return 'BrowseNextRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'RequestHeader:' + str(self.RequestHeader) + ', ' + \
             'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class BrowseNextResult(object):
    '''
    :ivar Results:
    :vartype Results: BrowseResult
    :ivar DiagnosticInfos:
    :vartype DiagnosticInfos: DiagnosticInfo
    '''

    __slots__ = [
        "Results",
        "DiagnosticInfos",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.Results = []
        self.DiagnosticInfos = []

    def to_binary(self):
        packet = []
        packet.append(uatype_Int32.pack(len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(uatype_Int32.pack(len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return BrowseNextResult(data)

    def _binary_init(self, data):
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(BrowseResult.from_binary(data))
        self.Results = array
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(DiagnosticInfo.from_binary(data))
        self.DiagnosticInfos = array

    def __str__(self):
        return 'BrowseNextResult(' + 'Results:' + str(self.Results) + ', ' + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'

    __repr__ = __str__


class BrowseNextResponse(object):
    '''
    Continues one or more browse operations.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    :ivar Parameters:
    :vartype Parameters: BrowseNextResult
    '''

    __slots__ = [
        "TypeId",
        "ResponseHeader",
        "Parameters",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.BrowseNextResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = BrowseNextResult()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return BrowseNextResponse(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.ResponseHeader = ResponseHeader.from_binary(data)
        self.Parameters = BrowseNextResult.from_binary(data)

    def __str__(self):
        return 'BrowseNextResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
             'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class RelativePathElement(object):
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

    __slots__ = [
        "ReferenceTypeId",
        "IsInverse",
        "IncludeSubtypes",
        "TargetName",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.ReferenceTypeId = NodeId()
        self.IsInverse = True
        self.IncludeSubtypes = True
        self.TargetName = QualifiedName()

    def to_binary(self):
        packet = []
        packet.append(self.ReferenceTypeId.to_binary())
        packet.append(uatype_Boolean.pack(self.IsInverse))
        packet.append(uatype_Boolean.pack(self.IncludeSubtypes))
        packet.append(self.TargetName.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return RelativePathElement(data)

    def _binary_init(self, data):
        self.ReferenceTypeId = NodeId.from_binary(data)
        self.IsInverse = uatype_Boolean.unpack(data.read(1))[0]
        self.IncludeSubtypes = uatype_Boolean.unpack(data.read(1))[0]
        self.TargetName = QualifiedName.from_binary(data)

    def __str__(self):
        return 'RelativePathElement(' + 'ReferenceTypeId:' + str(self.ReferenceTypeId) + ', ' + \
             'IsInverse:' + str(self.IsInverse) + ', ' + \
             'IncludeSubtypes:' + str(self.IncludeSubtypes) + ', ' + \
             'TargetName:' + str(self.TargetName) + ')'

    __repr__ = __str__


class RelativePath(object):
    '''
    A relative path constructed from reference types and browse names.

    :ivar Elements:
    :vartype Elements: RelativePathElement
    '''

    __slots__ = [
        "Elements",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.Elements = []

    def to_binary(self):
        packet = []
        packet.append(uatype_Int32.pack(len(self.Elements)))
        for fieldname in self.Elements:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return RelativePath(data)

    def _binary_init(self, data):
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(RelativePathElement.from_binary(data))
        self.Elements = array

    def __str__(self):
        return 'RelativePath(' + 'Elements:' + str(self.Elements) + ')'

    __repr__ = __str__


class BrowsePath(object):
    '''
    A request to translate a path into a node id.

    :ivar StartingNode:
    :vartype StartingNode: NodeId
    :ivar RelativePath:
    :vartype RelativePath: RelativePath
    '''

    __slots__ = [
        "StartingNode",
        "RelativePath",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.StartingNode = NodeId()
        self.RelativePath = RelativePath()

    def to_binary(self):
        packet = []
        packet.append(self.StartingNode.to_binary())
        packet.append(self.RelativePath.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return BrowsePath(data)

    def _binary_init(self, data):
        self.StartingNode = NodeId.from_binary(data)
        self.RelativePath = RelativePath.from_binary(data)

    def __str__(self):
        return 'BrowsePath(' + 'StartingNode:' + str(self.StartingNode) + ', ' + \
             'RelativePath:' + str(self.RelativePath) + ')'

    __repr__ = __str__


class BrowsePathTarget(object):
    '''
    The target of the translated path.

    :ivar TargetId:
    :vartype TargetId: ExpandedNodeId
    :ivar RemainingPathIndex:
    :vartype RemainingPathIndex: UInt32
    '''

    __slots__ = [
        "TargetId",
        "RemainingPathIndex",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TargetId = ExpandedNodeId()
        self.RemainingPathIndex = 0

    def to_binary(self):
        packet = []
        packet.append(self.TargetId.to_binary())
        packet.append(uatype_UInt32.pack(self.RemainingPathIndex))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return BrowsePathTarget(data)

    def _binary_init(self, data):
        self.TargetId = ExpandedNodeId.from_binary(data)
        self.RemainingPathIndex = uatype_UInt32.unpack(data.read(4))[0]

    def __str__(self):
        return 'BrowsePathTarget(' + 'TargetId:' + str(self.TargetId) + ', ' + \
             'RemainingPathIndex:' + str(self.RemainingPathIndex) + ')'

    __repr__ = __str__


class BrowsePathResult(object):
    '''
    The result of a translate opearation.

    :ivar StatusCode:
    :vartype StatusCode: StatusCode
    :ivar Targets:
    :vartype Targets: BrowsePathTarget
    '''

    __slots__ = [
        "StatusCode",
        "Targets",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.StatusCode = StatusCode()
        self.Targets = []

    def to_binary(self):
        packet = []
        packet.append(self.StatusCode.to_binary())
        packet.append(uatype_Int32.pack(len(self.Targets)))
        for fieldname in self.Targets:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return BrowsePathResult(data)

    def _binary_init(self, data):
        self.StatusCode = StatusCode.from_binary(data)
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(BrowsePathTarget.from_binary(data))
        self.Targets = array

    def __str__(self):
        return 'BrowsePathResult(' + 'StatusCode:' + str(self.StatusCode) + ', ' + \
             'Targets:' + str(self.Targets) + ')'

    __repr__ = __str__


class TranslateBrowsePathsToNodeIdsParameters(object):
    '''
    :ivar BrowsePaths:
    :vartype BrowsePaths: BrowsePath
    '''

    __slots__ = [
        "BrowsePaths",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.BrowsePaths = []

    def to_binary(self):
        packet = []
        packet.append(uatype_Int32.pack(len(self.BrowsePaths)))
        for fieldname in self.BrowsePaths:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return TranslateBrowsePathsToNodeIdsParameters(data)

    def _binary_init(self, data):
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(BrowsePath.from_binary(data))
        self.BrowsePaths = array

    def __str__(self):
        return 'TranslateBrowsePathsToNodeIdsParameters(' + 'BrowsePaths:' + str(self.BrowsePaths) + ')'

    __repr__ = __str__


class TranslateBrowsePathsToNodeIdsRequest(object):
    '''
    Translates one or more paths in the server address space.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: TranslateBrowsePathsToNodeIdsParameters
    '''

    __slots__ = [
        "TypeId",
        "RequestHeader",
        "Parameters",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.TranslateBrowsePathsToNodeIdsRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = TranslateBrowsePathsToNodeIdsParameters()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return TranslateBrowsePathsToNodeIdsRequest(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.RequestHeader = RequestHeader.from_binary(data)
        self.Parameters = TranslateBrowsePathsToNodeIdsParameters.from_binary(data)

    def __str__(self):
        return 'TranslateBrowsePathsToNodeIdsRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'RequestHeader:' + str(self.RequestHeader) + ', ' + \
             'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class TranslateBrowsePathsToNodeIdsResponse(object):
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

    __slots__ = [
        "TypeId",
        "ResponseHeader",
        "Results",
        "DiagnosticInfos",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.TranslateBrowsePathsToNodeIdsResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Results = []
        self.DiagnosticInfos = []

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(uatype_Int32.pack(len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(uatype_Int32.pack(len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return TranslateBrowsePathsToNodeIdsResponse(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.ResponseHeader = ResponseHeader.from_binary(data)
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(BrowsePathResult.from_binary(data))
        self.Results = array
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(DiagnosticInfo.from_binary(data))
        self.DiagnosticInfos = array

    def __str__(self):
        return 'TranslateBrowsePathsToNodeIdsResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
             'Results:' + str(self.Results) + ', ' + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'

    __repr__ = __str__


class RegisterNodesParameters(object):
    '''
    :ivar NodesToRegister:
    :vartype NodesToRegister: NodeId
    '''

    __slots__ = [
        "NodesToRegister",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.NodesToRegister = []

    def to_binary(self):
        packet = []
        packet.append(uatype_Int32.pack(len(self.NodesToRegister)))
        for fieldname in self.NodesToRegister:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return RegisterNodesParameters(data)

    def _binary_init(self, data):
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(NodeId.from_binary(data))
        self.NodesToRegister = array

    def __str__(self):
        return 'RegisterNodesParameters(' + 'NodesToRegister:' + str(self.NodesToRegister) + ')'

    __repr__ = __str__


class RegisterNodesRequest(object):
    '''
    Registers one or more nodes for repeated use within a session.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: RegisterNodesParameters
    '''

    __slots__ = [
        "TypeId",
        "RequestHeader",
        "Parameters",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.RegisterNodesRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = RegisterNodesParameters()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return RegisterNodesRequest(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.RequestHeader = RequestHeader.from_binary(data)
        self.Parameters = RegisterNodesParameters.from_binary(data)

    def __str__(self):
        return 'RegisterNodesRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'RequestHeader:' + str(self.RequestHeader) + ', ' + \
             'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class RegisterNodesResult(object):
    '''
    :ivar RegisteredNodeIds:
    :vartype RegisteredNodeIds: NodeId
    '''

    __slots__ = [
        "RegisteredNodeIds",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.RegisteredNodeIds = []

    def to_binary(self):
        packet = []
        packet.append(uatype_Int32.pack(len(self.RegisteredNodeIds)))
        for fieldname in self.RegisteredNodeIds:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return RegisterNodesResult(data)

    def _binary_init(self, data):
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(NodeId.from_binary(data))
        self.RegisteredNodeIds = array

    def __str__(self):
        return 'RegisterNodesResult(' + 'RegisteredNodeIds:' + str(self.RegisteredNodeIds) + ')'

    __repr__ = __str__


class RegisterNodesResponse(object):
    '''
    Registers one or more nodes for repeated use within a session.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    :ivar Parameters:
    :vartype Parameters: RegisterNodesResult
    '''

    __slots__ = [
        "TypeId",
        "ResponseHeader",
        "Parameters",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.RegisterNodesResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = RegisterNodesResult()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return RegisterNodesResponse(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.ResponseHeader = ResponseHeader.from_binary(data)
        self.Parameters = RegisterNodesResult.from_binary(data)

    def __str__(self):
        return 'RegisterNodesResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
             'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class UnregisterNodesParameters(object):
    '''
    :ivar NodesToUnregister:
    :vartype NodesToUnregister: NodeId
    '''

    __slots__ = [
        "NodesToUnregister",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.NodesToUnregister = []

    def to_binary(self):
        packet = []
        packet.append(uatype_Int32.pack(len(self.NodesToUnregister)))
        for fieldname in self.NodesToUnregister:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return UnregisterNodesParameters(data)

    def _binary_init(self, data):
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(NodeId.from_binary(data))
        self.NodesToUnregister = array

    def __str__(self):
        return 'UnregisterNodesParameters(' + 'NodesToUnregister:' + str(self.NodesToUnregister) + ')'

    __repr__ = __str__


class UnregisterNodesRequest(object):
    '''
    Unregisters one or more previously registered nodes.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: UnregisterNodesParameters
    '''

    __slots__ = [
        "TypeId",
        "RequestHeader",
        "Parameters",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.UnregisterNodesRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = UnregisterNodesParameters()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return UnregisterNodesRequest(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.RequestHeader = RequestHeader.from_binary(data)
        self.Parameters = UnregisterNodesParameters.from_binary(data)

    def __str__(self):
        return 'UnregisterNodesRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'RequestHeader:' + str(self.RequestHeader) + ', ' + \
             'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class UnregisterNodesResponse(object):
    '''
    Unregisters one or more previously registered nodes.

    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    '''

    __slots__ = [
        "TypeId",
        "ResponseHeader",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.UnregisterNodesResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return UnregisterNodesResponse(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.ResponseHeader = ResponseHeader.from_binary(data)

    def __str__(self):
        return 'UnregisterNodesResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'ResponseHeader:' + str(self.ResponseHeader) + ')'

    __repr__ = __str__


class EndpointConfiguration(object):
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

    __slots__ = [
        "OperationTimeout",
        "UseBinaryEncoding",
        "MaxStringLength",
        "MaxByteStringLength",
        "MaxArrayLength",
        "MaxMessageSize",
        "MaxBufferSize",
        "ChannelLifetime",
        "SecurityTokenLifetime",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.OperationTimeout = 0
        self.UseBinaryEncoding = True
        self.MaxStringLength = 0
        self.MaxByteStringLength = 0
        self.MaxArrayLength = 0
        self.MaxMessageSize = 0
        self.MaxBufferSize = 0
        self.ChannelLifetime = 0
        self.SecurityTokenLifetime = 0

    def to_binary(self):
        packet = []
        packet.append(uatype_Int32.pack(self.OperationTimeout))
        packet.append(uatype_Boolean.pack(self.UseBinaryEncoding))
        packet.append(uatype_Int32.pack(self.MaxStringLength))
        packet.append(uatype_Int32.pack(self.MaxByteStringLength))
        packet.append(uatype_Int32.pack(self.MaxArrayLength))
        packet.append(uatype_Int32.pack(self.MaxMessageSize))
        packet.append(uatype_Int32.pack(self.MaxBufferSize))
        packet.append(uatype_Int32.pack(self.ChannelLifetime))
        packet.append(uatype_Int32.pack(self.SecurityTokenLifetime))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return EndpointConfiguration(data)

    def _binary_init(self, data):
        self.OperationTimeout = uatype_Int32.unpack(data.read(4))[0]
        self.UseBinaryEncoding = uatype_Boolean.unpack(data.read(1))[0]
        self.MaxStringLength = uatype_Int32.unpack(data.read(4))[0]
        self.MaxByteStringLength = uatype_Int32.unpack(data.read(4))[0]
        self.MaxArrayLength = uatype_Int32.unpack(data.read(4))[0]
        self.MaxMessageSize = uatype_Int32.unpack(data.read(4))[0]
        self.MaxBufferSize = uatype_Int32.unpack(data.read(4))[0]
        self.ChannelLifetime = uatype_Int32.unpack(data.read(4))[0]
        self.SecurityTokenLifetime = uatype_Int32.unpack(data.read(4))[0]

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


class SupportedProfile(object):
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

    __slots__ = [
        "OrganizationUri",
        "ProfileId",
        "ComplianceTool",
        "ComplianceDate",
        "ComplianceLevel",
        "UnsupportedUnitIds",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.OrganizationUri = ''
        self.ProfileId = ''
        self.ComplianceTool = ''
        self.ComplianceDate = datetime.now()
        self.ComplianceLevel = 0
        self.UnsupportedUnitIds = []

    def to_binary(self):
        packet = []
        packet.append(pack_string(self.OrganizationUri))
        packet.append(pack_string(self.ProfileId))
        packet.append(pack_string(self.ComplianceTool))
        packet.append(pack_datetime(self.ComplianceDate))
        packet.append(uatype_UInt32.pack(self.ComplianceLevel))
        packet.append(uatype_Int32.pack(len(self.UnsupportedUnitIds)))
        for fieldname in self.UnsupportedUnitIds:
            packet.append(pack_string(fieldname))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return SupportedProfile(data)

    def _binary_init(self, data):
        self.OrganizationUri = unpack_string(data)
        self.ProfileId = unpack_string(data)
        self.ComplianceTool = unpack_string(data)
        self.ComplianceDate = unpack_datetime(data)
        self.ComplianceLevel = uatype_UInt32.unpack(data.read(4))[0]
        self.UnsupportedUnitIds = unpack_uatype_array('String', data)

    def __str__(self):
        return 'SupportedProfile(' + 'OrganizationUri:' + str(self.OrganizationUri) + ', ' + \
             'ProfileId:' + str(self.ProfileId) + ', ' + \
             'ComplianceTool:' + str(self.ComplianceTool) + ', ' + \
             'ComplianceDate:' + str(self.ComplianceDate) + ', ' + \
             'ComplianceLevel:' + str(self.ComplianceLevel) + ', ' + \
             'UnsupportedUnitIds:' + str(self.UnsupportedUnitIds) + ')'

    __repr__ = __str__


class SoftwareCertificate(object):
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

    __slots__ = [
        "ProductName",
        "ProductUri",
        "VendorName",
        "VendorProductCertificate",
        "SoftwareVersion",
        "BuildNumber",
        "BuildDate",
        "IssuedBy",
        "IssueDate",
        "SupportedProfiles",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
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

    def to_binary(self):
        packet = []
        packet.append(pack_string(self.ProductName))
        packet.append(pack_string(self.ProductUri))
        packet.append(pack_string(self.VendorName))
        packet.append(pack_bytes(self.VendorProductCertificate))
        packet.append(pack_string(self.SoftwareVersion))
        packet.append(pack_string(self.BuildNumber))
        packet.append(pack_datetime(self.BuildDate))
        packet.append(pack_string(self.IssuedBy))
        packet.append(pack_datetime(self.IssueDate))
        packet.append(uatype_Int32.pack(len(self.SupportedProfiles)))
        for fieldname in self.SupportedProfiles:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return SoftwareCertificate(data)

    def _binary_init(self, data):
        self.ProductName = unpack_string(data)
        self.ProductUri = unpack_string(data)
        self.VendorName = unpack_string(data)
        self.VendorProductCertificate = unpack_bytes(data)
        self.SoftwareVersion = unpack_string(data)
        self.BuildNumber = unpack_string(data)
        self.BuildDate = unpack_datetime(data)
        self.IssuedBy = unpack_string(data)
        self.IssueDate = unpack_datetime(data)
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(SupportedProfile.from_binary(data))
        self.SupportedProfiles = array

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


class QueryDataDescription(object):
    '''
    :ivar RelativePath:
    :vartype RelativePath: RelativePath
    :ivar AttributeId:
    :vartype AttributeId: UInt32
    :ivar IndexRange:
    :vartype IndexRange: String
    '''

    __slots__ = [
        "RelativePath",
        "AttributeId",
        "IndexRange",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.RelativePath = RelativePath()
        self.AttributeId = 0
        self.IndexRange = ''

    def to_binary(self):
        packet = []
        packet.append(self.RelativePath.to_binary())
        packet.append(uatype_UInt32.pack(self.AttributeId))
        packet.append(pack_string(self.IndexRange))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return QueryDataDescription(data)

    def _binary_init(self, data):
        self.RelativePath = RelativePath.from_binary(data)
        self.AttributeId = uatype_UInt32.unpack(data.read(4))[0]
        self.IndexRange = unpack_string(data)

    def __str__(self):
        return 'QueryDataDescription(' + 'RelativePath:' + str(self.RelativePath) + ', ' + \
             'AttributeId:' + str(self.AttributeId) + ', ' + \
             'IndexRange:' + str(self.IndexRange) + ')'

    __repr__ = __str__


class NodeTypeDescription(object):
    '''
    :ivar TypeDefinitionNode:
    :vartype TypeDefinitionNode: ExpandedNodeId
    :ivar IncludeSubTypes:
    :vartype IncludeSubTypes: Boolean
    :ivar DataToReturn:
    :vartype DataToReturn: QueryDataDescription
    '''

    __slots__ = [
        "TypeDefinitionNode",
        "IncludeSubTypes",
        "DataToReturn",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeDefinitionNode = ExpandedNodeId()
        self.IncludeSubTypes = True
        self.DataToReturn = []

    def to_binary(self):
        packet = []
        packet.append(self.TypeDefinitionNode.to_binary())
        packet.append(uatype_Boolean.pack(self.IncludeSubTypes))
        packet.append(uatype_Int32.pack(len(self.DataToReturn)))
        for fieldname in self.DataToReturn:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return NodeTypeDescription(data)

    def _binary_init(self, data):
        self.TypeDefinitionNode = ExpandedNodeId.from_binary(data)
        self.IncludeSubTypes = uatype_Boolean.unpack(data.read(1))[0]
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(QueryDataDescription.from_binary(data))
        self.DataToReturn = array

    def __str__(self):
        return 'NodeTypeDescription(' + 'TypeDefinitionNode:' + str(self.TypeDefinitionNode) + ', ' + \
             'IncludeSubTypes:' + str(self.IncludeSubTypes) + ', ' + \
             'DataToReturn:' + str(self.DataToReturn) + ')'

    __repr__ = __str__


class QueryDataSet(object):
    '''
    :ivar NodeId:
    :vartype NodeId: ExpandedNodeId
    :ivar TypeDefinitionNode:
    :vartype TypeDefinitionNode: ExpandedNodeId
    :ivar Values:
    :vartype Values: Variant
    '''

    __slots__ = [
        "NodeId",
        "TypeDefinitionNode",
        "Values",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.NodeId = ExpandedNodeId()
        self.TypeDefinitionNode = ExpandedNodeId()
        self.Values = []

    def to_binary(self):
        packet = []
        packet.append(self.NodeId.to_binary())
        packet.append(self.TypeDefinitionNode.to_binary())
        packet.append(uatype_Int32.pack(len(self.Values)))
        for fieldname in self.Values:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return QueryDataSet(data)

    def _binary_init(self, data):
        self.NodeId = ExpandedNodeId.from_binary(data)
        self.TypeDefinitionNode = ExpandedNodeId.from_binary(data)
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(Variant.from_binary(data))
        self.Values = array

    def __str__(self):
        return 'QueryDataSet(' + 'NodeId:' + str(self.NodeId) + ', ' + \
             'TypeDefinitionNode:' + str(self.TypeDefinitionNode) + ', ' + \
             'Values:' + str(self.Values) + ')'

    __repr__ = __str__


class NodeReference(object):
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

    __slots__ = [
        "NodeId",
        "ReferenceTypeId",
        "IsForward",
        "ReferencedNodeIds",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.NodeId = NodeId()
        self.ReferenceTypeId = NodeId()
        self.IsForward = True
        self.ReferencedNodeIds = []

    def to_binary(self):
        packet = []
        packet.append(self.NodeId.to_binary())
        packet.append(self.ReferenceTypeId.to_binary())
        packet.append(uatype_Boolean.pack(self.IsForward))
        packet.append(uatype_Int32.pack(len(self.ReferencedNodeIds)))
        for fieldname in self.ReferencedNodeIds:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return NodeReference(data)

    def _binary_init(self, data):
        self.NodeId = NodeId.from_binary(data)
        self.ReferenceTypeId = NodeId.from_binary(data)
        self.IsForward = uatype_Boolean.unpack(data.read(1))[0]
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(NodeId.from_binary(data))
        self.ReferencedNodeIds = array

    def __str__(self):
        return 'NodeReference(' + 'NodeId:' + str(self.NodeId) + ', ' + \
             'ReferenceTypeId:' + str(self.ReferenceTypeId) + ', ' + \
             'IsForward:' + str(self.IsForward) + ', ' + \
             'ReferencedNodeIds:' + str(self.ReferencedNodeIds) + ')'

    __repr__ = __str__


class ContentFilterElement(object):
    '''
    :ivar FilterOperator:
    :vartype FilterOperator: FilterOperator
    :ivar FilterOperands:
    :vartype FilterOperands: ExtensionObject
    '''

    __slots__ = [
        "FilterOperator",
        "FilterOperands",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.FilterOperator = 0
        self.FilterOperands = []

    def to_binary(self):
        packet = []
        packet.append(uatype_UInt32.pack(self.FilterOperator))
        packet.append(uatype_Int32.pack(len(self.FilterOperands)))
        for fieldname in self.FilterOperands:
            packet.append(extensionobject_to_binary(fieldname))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return ContentFilterElement(data)

    def _binary_init(self, data):
        self.FilterOperator = uatype_UInt32.unpack(data.read(4))[0]
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(extensionobject_from_binary(data))
        self.FilterOperands = array

    def __str__(self):
        return 'ContentFilterElement(' + 'FilterOperator:' + str(self.FilterOperator) + ', ' + \
             'FilterOperands:' + str(self.FilterOperands) + ')'

    __repr__ = __str__


class ContentFilter(object):
    '''
    :ivar Elements:
    :vartype Elements: ContentFilterElement
    '''

    __slots__ = [
        "Elements",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.Elements = []

    def to_binary(self):
        packet = []
        packet.append(uatype_Int32.pack(len(self.Elements)))
        for fieldname in self.Elements:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return ContentFilter(data)

    def _binary_init(self, data):
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(ContentFilterElement.from_binary(data))
        self.Elements = array

    def __str__(self):
        return 'ContentFilter(' + 'Elements:' + str(self.Elements) + ')'

    __repr__ = __str__


class ElementOperand(object):
    '''
    :ivar Index:
    :vartype Index: UInt32
    '''

    __slots__ = [
        "Index",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.Index = 0

    def to_binary(self):
        packet = []
        packet.append(uatype_UInt32.pack(self.Index))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return ElementOperand(data)

    def _binary_init(self, data):
        self.Index = uatype_UInt32.unpack(data.read(4))[0]

    def __str__(self):
        return 'ElementOperand(' + 'Index:' + str(self.Index) + ')'

    __repr__ = __str__


class LiteralOperand(object):
    '''
    :ivar Value:
    :vartype Value: Variant
    '''

    __slots__ = [
        "Value",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.Value = Variant()

    def to_binary(self):
        packet = []
        packet.append(self.Value.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return LiteralOperand(data)

    def _binary_init(self, data):
        self.Value = Variant.from_binary(data)

    def __str__(self):
        return 'LiteralOperand(' + 'Value:' + str(self.Value) + ')'

    __repr__ = __str__


class AttributeOperand(object):
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

    __slots__ = [
        "NodeId",
        "Alias",
        "BrowsePath",
        "AttributeId",
        "IndexRange",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.NodeId = NodeId()
        self.Alias = ''
        self.BrowsePath = RelativePath()
        self.AttributeId = 0
        self.IndexRange = ''

    def to_binary(self):
        packet = []
        packet.append(self.NodeId.to_binary())
        packet.append(pack_string(self.Alias))
        packet.append(self.BrowsePath.to_binary())
        packet.append(uatype_UInt32.pack(self.AttributeId))
        packet.append(pack_string(self.IndexRange))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return AttributeOperand(data)

    def _binary_init(self, data):
        self.NodeId = NodeId.from_binary(data)
        self.Alias = unpack_string(data)
        self.BrowsePath = RelativePath.from_binary(data)
        self.AttributeId = uatype_UInt32.unpack(data.read(4))[0]
        self.IndexRange = unpack_string(data)

    def __str__(self):
        return 'AttributeOperand(' + 'NodeId:' + str(self.NodeId) + ', ' + \
             'Alias:' + str(self.Alias) + ', ' + \
             'BrowsePath:' + str(self.BrowsePath) + ', ' + \
             'AttributeId:' + str(self.AttributeId) + ', ' + \
             'IndexRange:' + str(self.IndexRange) + ')'

    __repr__ = __str__


class SimpleAttributeOperand(object):
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

    __slots__ = [
        "TypeDefinitionId",
        "BrowsePath",
        "AttributeId",
        "IndexRange",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeDefinitionId = NodeId()
        self.BrowsePath = []
        self.AttributeId = 0
        self.IndexRange = ''

    def to_binary(self):
        packet = []
        packet.append(self.TypeDefinitionId.to_binary())
        packet.append(uatype_Int32.pack(len(self.BrowsePath)))
        for fieldname in self.BrowsePath:
            packet.append(fieldname.to_binary())
        packet.append(uatype_UInt32.pack(self.AttributeId))
        packet.append(pack_string(self.IndexRange))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return SimpleAttributeOperand(data)

    def _binary_init(self, data):
        self.TypeDefinitionId = NodeId.from_binary(data)
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(QualifiedName.from_binary(data))
        self.BrowsePath = array
        self.AttributeId = uatype_UInt32.unpack(data.read(4))[0]
        self.IndexRange = unpack_string(data)

    def __str__(self):
        return 'SimpleAttributeOperand(' + 'TypeDefinitionId:' + str(self.TypeDefinitionId) + ', ' + \
             'BrowsePath:' + str(self.BrowsePath) + ', ' + \
             'AttributeId:' + str(self.AttributeId) + ', ' + \
             'IndexRange:' + str(self.IndexRange) + ')'

    __repr__ = __str__


class ContentFilterElementResult(object):
    '''
    :ivar StatusCode:
    :vartype StatusCode: StatusCode
    :ivar OperandStatusCodes:
    :vartype OperandStatusCodes: StatusCode
    :ivar OperandDiagnosticInfos:
    :vartype OperandDiagnosticInfos: DiagnosticInfo
    '''

    __slots__ = [
        "StatusCode",
        "OperandStatusCodes",
        "OperandDiagnosticInfos",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.StatusCode = StatusCode()
        self.OperandStatusCodes = []
        self.OperandDiagnosticInfos = []

    def to_binary(self):
        packet = []
        packet.append(self.StatusCode.to_binary())
        packet.append(uatype_Int32.pack(len(self.OperandStatusCodes)))
        for fieldname in self.OperandStatusCodes:
            packet.append(fieldname.to_binary())
        packet.append(uatype_Int32.pack(len(self.OperandDiagnosticInfos)))
        for fieldname in self.OperandDiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return ContentFilterElementResult(data)

    def _binary_init(self, data):
        self.StatusCode = StatusCode.from_binary(data)
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(StatusCode.from_binary(data))
        self.OperandStatusCodes = array
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(DiagnosticInfo.from_binary(data))
        self.OperandDiagnosticInfos = array

    def __str__(self):
        return 'ContentFilterElementResult(' + 'StatusCode:' + str(self.StatusCode) + ', ' + \
             'OperandStatusCodes:' + str(self.OperandStatusCodes) + ', ' + \
             'OperandDiagnosticInfos:' + str(self.OperandDiagnosticInfos) + ')'

    __repr__ = __str__


class ContentFilterResult(object):
    '''
    :ivar ElementResults:
    :vartype ElementResults: ContentFilterElementResult
    :ivar ElementDiagnosticInfos:
    :vartype ElementDiagnosticInfos: DiagnosticInfo
    '''

    __slots__ = [
        "ElementResults",
        "ElementDiagnosticInfos",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.ElementResults = []
        self.ElementDiagnosticInfos = []

    def to_binary(self):
        packet = []
        packet.append(uatype_Int32.pack(len(self.ElementResults)))
        for fieldname in self.ElementResults:
            packet.append(fieldname.to_binary())
        packet.append(uatype_Int32.pack(len(self.ElementDiagnosticInfos)))
        for fieldname in self.ElementDiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return ContentFilterResult(data)

    def _binary_init(self, data):
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(ContentFilterElementResult.from_binary(data))
        self.ElementResults = array
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(DiagnosticInfo.from_binary(data))
        self.ElementDiagnosticInfos = array

    def __str__(self):
        return 'ContentFilterResult(' + 'ElementResults:' + str(self.ElementResults) + ', ' + \
             'ElementDiagnosticInfos:' + str(self.ElementDiagnosticInfos) + ')'

    __repr__ = __str__


class ParsingResult(object):
    '''
    :ivar StatusCode:
    :vartype StatusCode: StatusCode
    :ivar DataStatusCodes:
    :vartype DataStatusCodes: StatusCode
    :ivar DataDiagnosticInfos:
    :vartype DataDiagnosticInfos: DiagnosticInfo
    '''

    __slots__ = [
        "StatusCode",
        "DataStatusCodes",
        "DataDiagnosticInfos",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.StatusCode = StatusCode()
        self.DataStatusCodes = []
        self.DataDiagnosticInfos = []

    def to_binary(self):
        packet = []
        packet.append(self.StatusCode.to_binary())
        packet.append(uatype_Int32.pack(len(self.DataStatusCodes)))
        for fieldname in self.DataStatusCodes:
            packet.append(fieldname.to_binary())
        packet.append(uatype_Int32.pack(len(self.DataDiagnosticInfos)))
        for fieldname in self.DataDiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return ParsingResult(data)

    def _binary_init(self, data):
        self.StatusCode = StatusCode.from_binary(data)
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(StatusCode.from_binary(data))
        self.DataStatusCodes = array
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(DiagnosticInfo.from_binary(data))
        self.DataDiagnosticInfos = array

    def __str__(self):
        return 'ParsingResult(' + 'StatusCode:' + str(self.StatusCode) + ', ' + \
             'DataStatusCodes:' + str(self.DataStatusCodes) + ', ' + \
             'DataDiagnosticInfos:' + str(self.DataDiagnosticInfos) + ')'

    __repr__ = __str__


class QueryFirstParameters(object):
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

    __slots__ = [
        "View",
        "NodeTypes",
        "Filter",
        "MaxDataSetsToReturn",
        "MaxReferencesToReturn",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.View = ViewDescription()
        self.NodeTypes = []
        self.Filter = ContentFilter()
        self.MaxDataSetsToReturn = 0
        self.MaxReferencesToReturn = 0

    def to_binary(self):
        packet = []
        packet.append(self.View.to_binary())
        packet.append(uatype_Int32.pack(len(self.NodeTypes)))
        for fieldname in self.NodeTypes:
            packet.append(fieldname.to_binary())
        packet.append(self.Filter.to_binary())
        packet.append(uatype_UInt32.pack(self.MaxDataSetsToReturn))
        packet.append(uatype_UInt32.pack(self.MaxReferencesToReturn))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return QueryFirstParameters(data)

    def _binary_init(self, data):
        self.View = ViewDescription.from_binary(data)
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(NodeTypeDescription.from_binary(data))
        self.NodeTypes = array
        self.Filter = ContentFilter.from_binary(data)
        self.MaxDataSetsToReturn = uatype_UInt32.unpack(data.read(4))[0]
        self.MaxReferencesToReturn = uatype_UInt32.unpack(data.read(4))[0]

    def __str__(self):
        return 'QueryFirstParameters(' + 'View:' + str(self.View) + ', ' + \
             'NodeTypes:' + str(self.NodeTypes) + ', ' + \
             'Filter:' + str(self.Filter) + ', ' + \
             'MaxDataSetsToReturn:' + str(self.MaxDataSetsToReturn) + ', ' + \
             'MaxReferencesToReturn:' + str(self.MaxReferencesToReturn) + ')'

    __repr__ = __str__


class QueryFirstRequest(object):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: QueryFirstParameters
    '''

    __slots__ = [
        "TypeId",
        "RequestHeader",
        "Parameters",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.QueryFirstRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = QueryFirstParameters()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return QueryFirstRequest(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.RequestHeader = RequestHeader.from_binary(data)
        self.Parameters = QueryFirstParameters.from_binary(data)

    def __str__(self):
        return 'QueryFirstRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'RequestHeader:' + str(self.RequestHeader) + ', ' + \
             'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class QueryFirstResult(object):
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

    __slots__ = [
        "QueryDataSets",
        "ContinuationPoint",
        "ParsingResults",
        "DiagnosticInfos",
        "FilterResult",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.QueryDataSets = []
        self.ContinuationPoint = b''
        self.ParsingResults = []
        self.DiagnosticInfos = []
        self.FilterResult = ContentFilterResult()

    def to_binary(self):
        packet = []
        packet.append(uatype_Int32.pack(len(self.QueryDataSets)))
        for fieldname in self.QueryDataSets:
            packet.append(fieldname.to_binary())
        packet.append(pack_bytes(self.ContinuationPoint))
        packet.append(uatype_Int32.pack(len(self.ParsingResults)))
        for fieldname in self.ParsingResults:
            packet.append(fieldname.to_binary())
        packet.append(uatype_Int32.pack(len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        packet.append(self.FilterResult.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return QueryFirstResult(data)

    def _binary_init(self, data):
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(QueryDataSet.from_binary(data))
        self.QueryDataSets = array
        self.ContinuationPoint = unpack_bytes(data)
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(ParsingResult.from_binary(data))
        self.ParsingResults = array
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(DiagnosticInfo.from_binary(data))
        self.DiagnosticInfos = array
        self.FilterResult = ContentFilterResult.from_binary(data)

    def __str__(self):
        return 'QueryFirstResult(' + 'QueryDataSets:' + str(self.QueryDataSets) + ', ' + \
             'ContinuationPoint:' + str(self.ContinuationPoint) + ', ' + \
             'ParsingResults:' + str(self.ParsingResults) + ', ' + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ', ' + \
             'FilterResult:' + str(self.FilterResult) + ')'

    __repr__ = __str__


class QueryFirstResponse(object):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    :ivar Parameters:
    :vartype Parameters: QueryFirstResult
    '''

    __slots__ = [
        "TypeId",
        "ResponseHeader",
        "Parameters",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.QueryFirstResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = QueryFirstResult()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return QueryFirstResponse(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.ResponseHeader = ResponseHeader.from_binary(data)
        self.Parameters = QueryFirstResult.from_binary(data)

    def __str__(self):
        return 'QueryFirstResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
             'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class QueryNextParameters(object):
    '''
    :ivar ReleaseContinuationPoint:
    :vartype ReleaseContinuationPoint: Boolean
    :ivar ContinuationPoint:
    :vartype ContinuationPoint: ByteString
    '''

    __slots__ = [
        "ReleaseContinuationPoint",
        "ContinuationPoint",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.ReleaseContinuationPoint = True
        self.ContinuationPoint = b''

    def to_binary(self):
        packet = []
        packet.append(uatype_Boolean.pack(self.ReleaseContinuationPoint))
        packet.append(pack_bytes(self.ContinuationPoint))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return QueryNextParameters(data)

    def _binary_init(self, data):
        self.ReleaseContinuationPoint = uatype_Boolean.unpack(data.read(1))[0]
        self.ContinuationPoint = unpack_bytes(data)

    def __str__(self):
        return 'QueryNextParameters(' + 'ReleaseContinuationPoint:' + str(self.ReleaseContinuationPoint) + ', ' + \
             'ContinuationPoint:' + str(self.ContinuationPoint) + ')'

    __repr__ = __str__


class QueryNextRequest(object):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: QueryNextParameters
    '''

    __slots__ = [
        "TypeId",
        "RequestHeader",
        "Parameters",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.QueryNextRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = QueryNextParameters()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return QueryNextRequest(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.RequestHeader = RequestHeader.from_binary(data)
        self.Parameters = QueryNextParameters.from_binary(data)

    def __str__(self):
        return 'QueryNextRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'RequestHeader:' + str(self.RequestHeader) + ', ' + \
             'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class QueryNextResult(object):
    '''
    :ivar QueryDataSets:
    :vartype QueryDataSets: QueryDataSet
    :ivar RevisedContinuationPoint:
    :vartype RevisedContinuationPoint: ByteString
    '''

    __slots__ = [
        "QueryDataSets",
        "RevisedContinuationPoint",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.QueryDataSets = []
        self.RevisedContinuationPoint = b''

    def to_binary(self):
        packet = []
        packet.append(uatype_Int32.pack(len(self.QueryDataSets)))
        for fieldname in self.QueryDataSets:
            packet.append(fieldname.to_binary())
        packet.append(pack_bytes(self.RevisedContinuationPoint))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return QueryNextResult(data)

    def _binary_init(self, data):
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(QueryDataSet.from_binary(data))
        self.QueryDataSets = array
        self.RevisedContinuationPoint = unpack_bytes(data)

    def __str__(self):
        return 'QueryNextResult(' + 'QueryDataSets:' + str(self.QueryDataSets) + ', ' + \
             'RevisedContinuationPoint:' + str(self.RevisedContinuationPoint) + ')'

    __repr__ = __str__


class QueryNextResponse(object):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    :ivar Parameters:
    :vartype Parameters: QueryNextResult
    '''

    __slots__ = [
        "TypeId",
        "ResponseHeader",
        "Parameters",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.QueryNextResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = QueryNextResult()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return QueryNextResponse(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.ResponseHeader = ResponseHeader.from_binary(data)
        self.Parameters = QueryNextResult.from_binary(data)

    def __str__(self):
        return 'QueryNextResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
             'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class ReadValueId(object):
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

    __slots__ = [
        "NodeId",
        "AttributeId",
        "IndexRange",
        "DataEncoding",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.NodeId = NodeId()
        self.AttributeId = 0
        self.IndexRange = ''
        self.DataEncoding = QualifiedName()

    def to_binary(self):
        packet = []
        packet.append(self.NodeId.to_binary())
        packet.append(uatype_UInt32.pack(self.AttributeId))
        packet.append(pack_string(self.IndexRange))
        packet.append(self.DataEncoding.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return ReadValueId(data)

    def _binary_init(self, data):
        self.NodeId = NodeId.from_binary(data)
        self.AttributeId = uatype_UInt32.unpack(data.read(4))[0]
        self.IndexRange = unpack_string(data)
        self.DataEncoding = QualifiedName.from_binary(data)

    def __str__(self):
        return 'ReadValueId(' + 'NodeId:' + str(self.NodeId) + ', ' + \
             'AttributeId:' + str(self.AttributeId) + ', ' + \
             'IndexRange:' + str(self.IndexRange) + ', ' + \
             'DataEncoding:' + str(self.DataEncoding) + ')'

    __repr__ = __str__


class ReadParameters(object):
    '''
    :ivar MaxAge:
    :vartype MaxAge: Double
    :ivar TimestampsToReturn:
    :vartype TimestampsToReturn: TimestampsToReturn
    :ivar NodesToRead:
    :vartype NodesToRead: ReadValueId
    '''

    __slots__ = [
        "MaxAge",
        "TimestampsToReturn",
        "NodesToRead",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.MaxAge = 0
        self.TimestampsToReturn = 0
        self.NodesToRead = []

    def to_binary(self):
        packet = []
        packet.append(uatype_Double.pack(self.MaxAge))
        packet.append(uatype_UInt32.pack(self.TimestampsToReturn))
        packet.append(uatype_Int32.pack(len(self.NodesToRead)))
        for fieldname in self.NodesToRead:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return ReadParameters(data)

    def _binary_init(self, data):
        self.MaxAge = uatype_Double.unpack(data.read(8))[0]
        self.TimestampsToReturn = uatype_UInt32.unpack(data.read(4))[0]
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(ReadValueId.from_binary(data))
        self.NodesToRead = array

    def __str__(self):
        return 'ReadParameters(' + 'MaxAge:' + str(self.MaxAge) + ', ' + \
             'TimestampsToReturn:' + str(self.TimestampsToReturn) + ', ' + \
             'NodesToRead:' + str(self.NodesToRead) + ')'

    __repr__ = __str__


class ReadRequest(object):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: ReadParameters
    '''

    __slots__ = [
        "TypeId",
        "RequestHeader",
        "Parameters",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.ReadRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = ReadParameters()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return ReadRequest(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.RequestHeader = RequestHeader.from_binary(data)
        self.Parameters = ReadParameters.from_binary(data)

    def __str__(self):
        return 'ReadRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'RequestHeader:' + str(self.RequestHeader) + ', ' + \
             'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class ReadResponse(object):
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

    __slots__ = [
        "TypeId",
        "ResponseHeader",
        "Results",
        "DiagnosticInfos",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.ReadResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Results = []
        self.DiagnosticInfos = []

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(uatype_Int32.pack(len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(uatype_Int32.pack(len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return ReadResponse(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.ResponseHeader = ResponseHeader.from_binary(data)
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(DataValue.from_binary(data))
        self.Results = array
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(DiagnosticInfo.from_binary(data))
        self.DiagnosticInfos = array

    def __str__(self):
        return 'ReadResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
             'Results:' + str(self.Results) + ', ' + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'

    __repr__ = __str__


class HistoryReadValueId(object):
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

    __slots__ = [
        "NodeId",
        "IndexRange",
        "DataEncoding",
        "ContinuationPoint",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.NodeId = NodeId()
        self.IndexRange = ''
        self.DataEncoding = QualifiedName()
        self.ContinuationPoint = b''

    def to_binary(self):
        packet = []
        packet.append(self.NodeId.to_binary())
        packet.append(pack_string(self.IndexRange))
        packet.append(self.DataEncoding.to_binary())
        packet.append(pack_bytes(self.ContinuationPoint))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return HistoryReadValueId(data)

    def _binary_init(self, data):
        self.NodeId = NodeId.from_binary(data)
        self.IndexRange = unpack_string(data)
        self.DataEncoding = QualifiedName.from_binary(data)
        self.ContinuationPoint = unpack_bytes(data)

    def __str__(self):
        return 'HistoryReadValueId(' + 'NodeId:' + str(self.NodeId) + ', ' + \
             'IndexRange:' + str(self.IndexRange) + ', ' + \
             'DataEncoding:' + str(self.DataEncoding) + ', ' + \
             'ContinuationPoint:' + str(self.ContinuationPoint) + ')'

    __repr__ = __str__


class HistoryReadResult(object):
    '''
    :ivar StatusCode:
    :vartype StatusCode: StatusCode
    :ivar ContinuationPoint:
    :vartype ContinuationPoint: ByteString
    :ivar HistoryData:
    :vartype HistoryData: ExtensionObject
    '''

    __slots__ = [
        "StatusCode",
        "ContinuationPoint",
        "HistoryData",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.StatusCode = StatusCode()
        self.ContinuationPoint = b''
        self.HistoryData = None

    def to_binary(self):
        packet = []
        packet.append(self.StatusCode.to_binary())
        packet.append(pack_bytes(self.ContinuationPoint))
        packet.append(extensionobject_to_binary(self.HistoryData))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return HistoryReadResult(data)

    def _binary_init(self, data):
        self.StatusCode = StatusCode.from_binary(data)
        self.ContinuationPoint = unpack_bytes(data)
        self.HistoryData = extensionobject_from_binary(data)

    def __str__(self):
        return 'HistoryReadResult(' + 'StatusCode:' + str(self.StatusCode) + ', ' + \
             'ContinuationPoint:' + str(self.ContinuationPoint) + ', ' + \
             'HistoryData:' + str(self.HistoryData) + ')'

    __repr__ = __str__


class HistoryReadDetails(object):
    '''
    '''

    __slots__ = [
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return

    def to_binary(self):
        packet = []
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return HistoryReadDetails(data)

    def _binary_init(self, data):
        pass

    def __str__(self):
        return 'HistoryReadDetails(' +  + ')'

    __repr__ = __str__


class ReadEventDetails(object):
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

    __slots__ = [
        "NumValuesPerNode",
        "StartTime",
        "EndTime",
        "Filter",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.NumValuesPerNode = 0
        self.StartTime = datetime.now()
        self.EndTime = datetime.now()
        self.Filter = EventFilter()

    def to_binary(self):
        packet = []
        packet.append(uatype_UInt32.pack(self.NumValuesPerNode))
        packet.append(pack_datetime(self.StartTime))
        packet.append(pack_datetime(self.EndTime))
        packet.append(self.Filter.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return ReadEventDetails(data)

    def _binary_init(self, data):
        self.NumValuesPerNode = uatype_UInt32.unpack(data.read(4))[0]
        self.StartTime = unpack_datetime(data)
        self.EndTime = unpack_datetime(data)
        self.Filter = EventFilter.from_binary(data)

    def __str__(self):
        return 'ReadEventDetails(' + 'NumValuesPerNode:' + str(self.NumValuesPerNode) + ', ' + \
             'StartTime:' + str(self.StartTime) + ', ' + \
             'EndTime:' + str(self.EndTime) + ', ' + \
             'Filter:' + str(self.Filter) + ')'

    __repr__ = __str__


class ReadRawModifiedDetails(object):
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

    __slots__ = [
        "IsReadModified",
        "StartTime",
        "EndTime",
        "NumValuesPerNode",
        "ReturnBounds",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.IsReadModified = True
        self.StartTime = datetime.now()
        self.EndTime = datetime.now()
        self.NumValuesPerNode = 0
        self.ReturnBounds = True

    def to_binary(self):
        packet = []
        packet.append(uatype_Boolean.pack(self.IsReadModified))
        packet.append(pack_datetime(self.StartTime))
        packet.append(pack_datetime(self.EndTime))
        packet.append(uatype_UInt32.pack(self.NumValuesPerNode))
        packet.append(uatype_Boolean.pack(self.ReturnBounds))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return ReadRawModifiedDetails(data)

    def _binary_init(self, data):
        self.IsReadModified = uatype_Boolean.unpack(data.read(1))[0]
        self.StartTime = unpack_datetime(data)
        self.EndTime = unpack_datetime(data)
        self.NumValuesPerNode = uatype_UInt32.unpack(data.read(4))[0]
        self.ReturnBounds = uatype_Boolean.unpack(data.read(1))[0]

    def __str__(self):
        return 'ReadRawModifiedDetails(' + 'IsReadModified:' + str(self.IsReadModified) + ', ' + \
             'StartTime:' + str(self.StartTime) + ', ' + \
             'EndTime:' + str(self.EndTime) + ', ' + \
             'NumValuesPerNode:' + str(self.NumValuesPerNode) + ', ' + \
             'ReturnBounds:' + str(self.ReturnBounds) + ')'

    __repr__ = __str__


class ReadProcessedDetails(object):
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

    __slots__ = [
        "StartTime",
        "EndTime",
        "ProcessingInterval",
        "AggregateType",
        "AggregateConfiguration",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.StartTime = datetime.now()
        self.EndTime = datetime.now()
        self.ProcessingInterval = 0
        self.AggregateType = []
        self.AggregateConfiguration = AggregateConfiguration()

    def to_binary(self):
        packet = []
        packet.append(pack_datetime(self.StartTime))
        packet.append(pack_datetime(self.EndTime))
        packet.append(uatype_Double.pack(self.ProcessingInterval))
        packet.append(uatype_Int32.pack(len(self.AggregateType)))
        for fieldname in self.AggregateType:
            packet.append(fieldname.to_binary())
        packet.append(self.AggregateConfiguration.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return ReadProcessedDetails(data)

    def _binary_init(self, data):
        self.StartTime = unpack_datetime(data)
        self.EndTime = unpack_datetime(data)
        self.ProcessingInterval = uatype_Double.unpack(data.read(8))[0]
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(NodeId.from_binary(data))
        self.AggregateType = array
        self.AggregateConfiguration = AggregateConfiguration.from_binary(data)

    def __str__(self):
        return 'ReadProcessedDetails(' + 'StartTime:' + str(self.StartTime) + ', ' + \
             'EndTime:' + str(self.EndTime) + ', ' + \
             'ProcessingInterval:' + str(self.ProcessingInterval) + ', ' + \
             'AggregateType:' + str(self.AggregateType) + ', ' + \
             'AggregateConfiguration:' + str(self.AggregateConfiguration) + ')'

    __repr__ = __str__


class ReadAtTimeDetails(object):
    '''
    :ivar ReqTimes:
    :vartype ReqTimes: DateTime
    :ivar UseSimpleBounds:
    :vartype UseSimpleBounds: Boolean
    '''

    __slots__ = [
        "ReqTimes",
        "UseSimpleBounds",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.ReqTimes = []
        self.UseSimpleBounds = True

    def to_binary(self):
        packet = []
        packet.append(uatype_Int32.pack(len(self.ReqTimes)))
        for fieldname in self.ReqTimes:
            packet.append(pack_datetime(fieldname))
        packet.append(uatype_Boolean.pack(self.UseSimpleBounds))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return ReadAtTimeDetails(data)

    def _binary_init(self, data):
        self.ReqTimes = unpack_uatype_array('DateTime', data)
        self.UseSimpleBounds = uatype_Boolean.unpack(data.read(1))[0]

    def __str__(self):
        return 'ReadAtTimeDetails(' + 'ReqTimes:' + str(self.ReqTimes) + ', ' + \
             'UseSimpleBounds:' + str(self.UseSimpleBounds) + ')'

    __repr__ = __str__


class HistoryData(object):
    '''
    :ivar DataValues:
    :vartype DataValues: DataValue
    '''

    __slots__ = [
        "DataValues",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.DataValues = []

    def to_binary(self):
        packet = []
        packet.append(uatype_Int32.pack(len(self.DataValues)))
        for fieldname in self.DataValues:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return HistoryData(data)

    def _binary_init(self, data):
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(DataValue.from_binary(data))
        self.DataValues = array

    def __str__(self):
        return 'HistoryData(' + 'DataValues:' + str(self.DataValues) + ')'

    __repr__ = __str__


class ModificationInfo(object):
    '''
    :ivar ModificationTime:
    :vartype ModificationTime: DateTime
    :ivar UpdateType:
    :vartype UpdateType: HistoryUpdateType
    :ivar UserName:
    :vartype UserName: String
    '''

    __slots__ = [
        "ModificationTime",
        "UpdateType",
        "UserName",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.ModificationTime = datetime.now()
        self.UpdateType = 0
        self.UserName = ''

    def to_binary(self):
        packet = []
        packet.append(pack_datetime(self.ModificationTime))
        packet.append(uatype_UInt32.pack(self.UpdateType))
        packet.append(pack_string(self.UserName))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return ModificationInfo(data)

    def _binary_init(self, data):
        self.ModificationTime = unpack_datetime(data)
        self.UpdateType = uatype_UInt32.unpack(data.read(4))[0]
        self.UserName = unpack_string(data)

    def __str__(self):
        return 'ModificationInfo(' + 'ModificationTime:' + str(self.ModificationTime) + ', ' + \
             'UpdateType:' + str(self.UpdateType) + ', ' + \
             'UserName:' + str(self.UserName) + ')'

    __repr__ = __str__


class HistoryModifiedData(object):
    '''
    :ivar DataValues:
    :vartype DataValues: DataValue
    :ivar ModificationInfos:
    :vartype ModificationInfos: ModificationInfo
    '''

    __slots__ = [
        "DataValues",
        "ModificationInfos",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.DataValues = []
        self.ModificationInfos = []

    def to_binary(self):
        packet = []
        packet.append(uatype_Int32.pack(len(self.DataValues)))
        for fieldname in self.DataValues:
            packet.append(fieldname.to_binary())
        packet.append(uatype_Int32.pack(len(self.ModificationInfos)))
        for fieldname in self.ModificationInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return HistoryModifiedData(data)

    def _binary_init(self, data):
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(DataValue.from_binary(data))
        self.DataValues = array
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(ModificationInfo.from_binary(data))
        self.ModificationInfos = array

    def __str__(self):
        return 'HistoryModifiedData(' + 'DataValues:' + str(self.DataValues) + ', ' + \
             'ModificationInfos:' + str(self.ModificationInfos) + ')'

    __repr__ = __str__


class HistoryEvent(object):
    '''
    :ivar Events:
    :vartype Events: HistoryEventFieldList
    '''

    __slots__ = [
        "Events",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.Events = []

    def to_binary(self):
        packet = []
        packet.append(uatype_Int32.pack(len(self.Events)))
        for fieldname in self.Events:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return HistoryEvent(data)

    def _binary_init(self, data):
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(HistoryEventFieldList.from_binary(data))
        self.Events = array

    def __str__(self):
        return 'HistoryEvent(' + 'Events:' + str(self.Events) + ')'

    __repr__ = __str__


class HistoryReadParameters(object):
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

    __slots__ = [
        "HistoryReadDetails",
        "TimestampsToReturn",
        "ReleaseContinuationPoints",
        "NodesToRead",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.HistoryReadDetails = None
        self.TimestampsToReturn = 0
        self.ReleaseContinuationPoints = True
        self.NodesToRead = []

    def to_binary(self):
        packet = []
        packet.append(extensionobject_to_binary(self.HistoryReadDetails))
        packet.append(uatype_UInt32.pack(self.TimestampsToReturn))
        packet.append(uatype_Boolean.pack(self.ReleaseContinuationPoints))
        packet.append(uatype_Int32.pack(len(self.NodesToRead)))
        for fieldname in self.NodesToRead:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return HistoryReadParameters(data)

    def _binary_init(self, data):
        self.HistoryReadDetails = extensionobject_from_binary(data)
        self.TimestampsToReturn = uatype_UInt32.unpack(data.read(4))[0]
        self.ReleaseContinuationPoints = uatype_Boolean.unpack(data.read(1))[0]
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(HistoryReadValueId.from_binary(data))
        self.NodesToRead = array

    def __str__(self):
        return 'HistoryReadParameters(' + 'HistoryReadDetails:' + str(self.HistoryReadDetails) + ', ' + \
             'TimestampsToReturn:' + str(self.TimestampsToReturn) + ', ' + \
             'ReleaseContinuationPoints:' + str(self.ReleaseContinuationPoints) + ', ' + \
             'NodesToRead:' + str(self.NodesToRead) + ')'

    __repr__ = __str__


class HistoryReadRequest(object):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: HistoryReadParameters
    '''

    __slots__ = [
        "TypeId",
        "RequestHeader",
        "Parameters",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.HistoryReadRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = HistoryReadParameters()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return HistoryReadRequest(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.RequestHeader = RequestHeader.from_binary(data)
        self.Parameters = HistoryReadParameters.from_binary(data)

    def __str__(self):
        return 'HistoryReadRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'RequestHeader:' + str(self.RequestHeader) + ', ' + \
             'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class HistoryReadResponse(object):
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

    __slots__ = [
        "TypeId",
        "ResponseHeader",
        "Results",
        "DiagnosticInfos",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.HistoryReadResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Results = []
        self.DiagnosticInfos = []

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(uatype_Int32.pack(len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(uatype_Int32.pack(len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return HistoryReadResponse(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.ResponseHeader = ResponseHeader.from_binary(data)
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(HistoryReadResult.from_binary(data))
        self.Results = array
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(DiagnosticInfo.from_binary(data))
        self.DiagnosticInfos = array

    def __str__(self):
        return 'HistoryReadResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
             'Results:' + str(self.Results) + ', ' + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'

    __repr__ = __str__


class WriteValue(object):
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

    __slots__ = [
        "NodeId",
        "AttributeId",
        "IndexRange",
        "Value",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.NodeId = NodeId()
        self.AttributeId = 0
        self.IndexRange = ''
        self.Value = DataValue()

    def to_binary(self):
        packet = []
        packet.append(self.NodeId.to_binary())
        packet.append(uatype_UInt32.pack(self.AttributeId))
        packet.append(pack_string(self.IndexRange))
        packet.append(self.Value.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return WriteValue(data)

    def _binary_init(self, data):
        self.NodeId = NodeId.from_binary(data)
        self.AttributeId = uatype_UInt32.unpack(data.read(4))[0]
        self.IndexRange = unpack_string(data)
        self.Value = DataValue.from_binary(data)

    def __str__(self):
        return 'WriteValue(' + 'NodeId:' + str(self.NodeId) + ', ' + \
             'AttributeId:' + str(self.AttributeId) + ', ' + \
             'IndexRange:' + str(self.IndexRange) + ', ' + \
             'Value:' + str(self.Value) + ')'

    __repr__ = __str__


class WriteParameters(object):
    '''
    :ivar NodesToWrite:
    :vartype NodesToWrite: WriteValue
    '''

    __slots__ = [
        "NodesToWrite",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.NodesToWrite = []

    def to_binary(self):
        packet = []
        packet.append(uatype_Int32.pack(len(self.NodesToWrite)))
        for fieldname in self.NodesToWrite:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return WriteParameters(data)

    def _binary_init(self, data):
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(WriteValue.from_binary(data))
        self.NodesToWrite = array

    def __str__(self):
        return 'WriteParameters(' + 'NodesToWrite:' + str(self.NodesToWrite) + ')'

    __repr__ = __str__


class WriteRequest(object):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: WriteParameters
    '''

    __slots__ = [
        "TypeId",
        "RequestHeader",
        "Parameters",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.WriteRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = WriteParameters()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return WriteRequest(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.RequestHeader = RequestHeader.from_binary(data)
        self.Parameters = WriteParameters.from_binary(data)

    def __str__(self):
        return 'WriteRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'RequestHeader:' + str(self.RequestHeader) + ', ' + \
             'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class WriteResponse(object):
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

    __slots__ = [
        "TypeId",
        "ResponseHeader",
        "Results",
        "DiagnosticInfos",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.WriteResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Results = []
        self.DiagnosticInfos = []

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(uatype_Int32.pack(len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(uatype_Int32.pack(len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return WriteResponse(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.ResponseHeader = ResponseHeader.from_binary(data)
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(StatusCode.from_binary(data))
        self.Results = array
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(DiagnosticInfo.from_binary(data))
        self.DiagnosticInfos = array

    def __str__(self):
        return 'WriteResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
             'Results:' + str(self.Results) + ', ' + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'

    __repr__ = __str__


class HistoryUpdateDetails(object):
    '''
    :ivar NodeId:
    :vartype NodeId: NodeId
    '''

    __slots__ = [
        "NodeId",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.NodeId = NodeId()

    def to_binary(self):
        packet = []
        packet.append(self.NodeId.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return HistoryUpdateDetails(data)

    def _binary_init(self, data):
        self.NodeId = NodeId.from_binary(data)

    def __str__(self):
        return 'HistoryUpdateDetails(' + 'NodeId:' + str(self.NodeId) + ')'

    __repr__ = __str__


class UpdateDataDetails(object):
    '''
    :ivar NodeId:
    :vartype NodeId: NodeId
    :ivar PerformInsertReplace:
    :vartype PerformInsertReplace: PerformUpdateType
    :ivar UpdateValues:
    :vartype UpdateValues: DataValue
    '''

    __slots__ = [
        "NodeId",
        "PerformInsertReplace",
        "UpdateValues",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.NodeId = NodeId()
        self.PerformInsertReplace = 0
        self.UpdateValues = []

    def to_binary(self):
        packet = []
        packet.append(self.NodeId.to_binary())
        packet.append(uatype_UInt32.pack(self.PerformInsertReplace))
        packet.append(uatype_Int32.pack(len(self.UpdateValues)))
        for fieldname in self.UpdateValues:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return UpdateDataDetails(data)

    def _binary_init(self, data):
        self.NodeId = NodeId.from_binary(data)
        self.PerformInsertReplace = uatype_UInt32.unpack(data.read(4))[0]
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(DataValue.from_binary(data))
        self.UpdateValues = array

    def __str__(self):
        return 'UpdateDataDetails(' + 'NodeId:' + str(self.NodeId) + ', ' + \
             'PerformInsertReplace:' + str(self.PerformInsertReplace) + ', ' + \
             'UpdateValues:' + str(self.UpdateValues) + ')'

    __repr__ = __str__


class UpdateStructureDataDetails(object):
    '''
    :ivar NodeId:
    :vartype NodeId: NodeId
    :ivar PerformInsertReplace:
    :vartype PerformInsertReplace: PerformUpdateType
    :ivar UpdateValues:
    :vartype UpdateValues: DataValue
    '''

    __slots__ = [
        "NodeId",
        "PerformInsertReplace",
        "UpdateValues",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.NodeId = NodeId()
        self.PerformInsertReplace = 0
        self.UpdateValues = []

    def to_binary(self):
        packet = []
        packet.append(self.NodeId.to_binary())
        packet.append(uatype_UInt32.pack(self.PerformInsertReplace))
        packet.append(uatype_Int32.pack(len(self.UpdateValues)))
        for fieldname in self.UpdateValues:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return UpdateStructureDataDetails(data)

    def _binary_init(self, data):
        self.NodeId = NodeId.from_binary(data)
        self.PerformInsertReplace = uatype_UInt32.unpack(data.read(4))[0]
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(DataValue.from_binary(data))
        self.UpdateValues = array

    def __str__(self):
        return 'UpdateStructureDataDetails(' + 'NodeId:' + str(self.NodeId) + ', ' + \
             'PerformInsertReplace:' + str(self.PerformInsertReplace) + ', ' + \
             'UpdateValues:' + str(self.UpdateValues) + ')'

    __repr__ = __str__


class UpdateEventDetails(object):
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

    __slots__ = [
        "NodeId",
        "PerformInsertReplace",
        "Filter",
        "EventData",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.NodeId = NodeId()
        self.PerformInsertReplace = 0
        self.Filter = EventFilter()
        self.EventData = []

    def to_binary(self):
        packet = []
        packet.append(self.NodeId.to_binary())
        packet.append(uatype_UInt32.pack(self.PerformInsertReplace))
        packet.append(self.Filter.to_binary())
        packet.append(uatype_Int32.pack(len(self.EventData)))
        for fieldname in self.EventData:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return UpdateEventDetails(data)

    def _binary_init(self, data):
        self.NodeId = NodeId.from_binary(data)
        self.PerformInsertReplace = uatype_UInt32.unpack(data.read(4))[0]
        self.Filter = EventFilter.from_binary(data)
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(HistoryEventFieldList.from_binary(data))
        self.EventData = array

    def __str__(self):
        return 'UpdateEventDetails(' + 'NodeId:' + str(self.NodeId) + ', ' + \
             'PerformInsertReplace:' + str(self.PerformInsertReplace) + ', ' + \
             'Filter:' + str(self.Filter) + ', ' + \
             'EventData:' + str(self.EventData) + ')'

    __repr__ = __str__


class DeleteRawModifiedDetails(object):
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

    __slots__ = [
        "NodeId",
        "IsDeleteModified",
        "StartTime",
        "EndTime",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.NodeId = NodeId()
        self.IsDeleteModified = True
        self.StartTime = datetime.now()
        self.EndTime = datetime.now()

    def to_binary(self):
        packet = []
        packet.append(self.NodeId.to_binary())
        packet.append(uatype_Boolean.pack(self.IsDeleteModified))
        packet.append(pack_datetime(self.StartTime))
        packet.append(pack_datetime(self.EndTime))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return DeleteRawModifiedDetails(data)

    def _binary_init(self, data):
        self.NodeId = NodeId.from_binary(data)
        self.IsDeleteModified = uatype_Boolean.unpack(data.read(1))[0]
        self.StartTime = unpack_datetime(data)
        self.EndTime = unpack_datetime(data)

    def __str__(self):
        return 'DeleteRawModifiedDetails(' + 'NodeId:' + str(self.NodeId) + ', ' + \
             'IsDeleteModified:' + str(self.IsDeleteModified) + ', ' + \
             'StartTime:' + str(self.StartTime) + ', ' + \
             'EndTime:' + str(self.EndTime) + ')'

    __repr__ = __str__


class DeleteAtTimeDetails(object):
    '''
    :ivar NodeId:
    :vartype NodeId: NodeId
    :ivar ReqTimes:
    :vartype ReqTimes: DateTime
    '''

    __slots__ = [
        "NodeId",
        "ReqTimes",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.NodeId = NodeId()
        self.ReqTimes = []

    def to_binary(self):
        packet = []
        packet.append(self.NodeId.to_binary())
        packet.append(uatype_Int32.pack(len(self.ReqTimes)))
        for fieldname in self.ReqTimes:
            packet.append(pack_datetime(fieldname))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return DeleteAtTimeDetails(data)

    def _binary_init(self, data):
        self.NodeId = NodeId.from_binary(data)
        self.ReqTimes = unpack_uatype_array('DateTime', data)

    def __str__(self):
        return 'DeleteAtTimeDetails(' + 'NodeId:' + str(self.NodeId) + ', ' + \
             'ReqTimes:' + str(self.ReqTimes) + ')'

    __repr__ = __str__


class DeleteEventDetails(object):
    '''
    :ivar NodeId:
    :vartype NodeId: NodeId
    :ivar EventIds:
    :vartype EventIds: ByteString
    '''

    __slots__ = [
        "NodeId",
        "EventIds",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.NodeId = NodeId()
        self.EventIds = []

    def to_binary(self):
        packet = []
        packet.append(self.NodeId.to_binary())
        packet.append(uatype_Int32.pack(len(self.EventIds)))
        for fieldname in self.EventIds:
            packet.append(pack_bytes(fieldname))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return DeleteEventDetails(data)

    def _binary_init(self, data):
        self.NodeId = NodeId.from_binary(data)
        self.EventIds = unpack_uatype_array('ByteString', data)

    def __str__(self):
        return 'DeleteEventDetails(' + 'NodeId:' + str(self.NodeId) + ', ' + \
             'EventIds:' + str(self.EventIds) + ')'

    __repr__ = __str__


class HistoryUpdateResult(object):
    '''
    :ivar StatusCode:
    :vartype StatusCode: StatusCode
    :ivar OperationResults:
    :vartype OperationResults: StatusCode
    :ivar DiagnosticInfos:
    :vartype DiagnosticInfos: DiagnosticInfo
    '''

    __slots__ = [
        "StatusCode",
        "OperationResults",
        "DiagnosticInfos",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.StatusCode = StatusCode()
        self.OperationResults = []
        self.DiagnosticInfos = []

    def to_binary(self):
        packet = []
        packet.append(self.StatusCode.to_binary())
        packet.append(uatype_Int32.pack(len(self.OperationResults)))
        for fieldname in self.OperationResults:
            packet.append(fieldname.to_binary())
        packet.append(uatype_Int32.pack(len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return HistoryUpdateResult(data)

    def _binary_init(self, data):
        self.StatusCode = StatusCode.from_binary(data)
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(StatusCode.from_binary(data))
        self.OperationResults = array
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(DiagnosticInfo.from_binary(data))
        self.DiagnosticInfos = array

    def __str__(self):
        return 'HistoryUpdateResult(' + 'StatusCode:' + str(self.StatusCode) + ', ' + \
             'OperationResults:' + str(self.OperationResults) + ', ' + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'

    __repr__ = __str__


class HistoryUpdateParameters(object):
    '''
    :ivar HistoryUpdateDetails:
    :vartype HistoryUpdateDetails: ExtensionObject
    '''

    __slots__ = [
        "HistoryUpdateDetails",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.HistoryUpdateDetails = []

    def to_binary(self):
        packet = []
        packet.append(uatype_Int32.pack(len(self.HistoryUpdateDetails)))
        for fieldname in self.HistoryUpdateDetails:
            packet.append(extensionobject_to_binary(fieldname))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return HistoryUpdateParameters(data)

    def _binary_init(self, data):
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(extensionobject_from_binary(data))
        self.HistoryUpdateDetails = array

    def __str__(self):
        return 'HistoryUpdateParameters(' + 'HistoryUpdateDetails:' + str(self.HistoryUpdateDetails) + ')'

    __repr__ = __str__


class HistoryUpdateRequest(object):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: HistoryUpdateParameters
    '''

    __slots__ = [
        "TypeId",
        "RequestHeader",
        "Parameters",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.HistoryUpdateRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = HistoryUpdateParameters()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return HistoryUpdateRequest(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.RequestHeader = RequestHeader.from_binary(data)
        self.Parameters = HistoryUpdateParameters.from_binary(data)

    def __str__(self):
        return 'HistoryUpdateRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'RequestHeader:' + str(self.RequestHeader) + ', ' + \
             'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class HistoryUpdateResponse(object):
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

    __slots__ = [
        "TypeId",
        "ResponseHeader",
        "Results",
        "DiagnosticInfos",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.HistoryUpdateResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Results = []
        self.DiagnosticInfos = []

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(uatype_Int32.pack(len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(uatype_Int32.pack(len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return HistoryUpdateResponse(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.ResponseHeader = ResponseHeader.from_binary(data)
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(HistoryUpdateResult.from_binary(data))
        self.Results = array
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(DiagnosticInfo.from_binary(data))
        self.DiagnosticInfos = array

    def __str__(self):
        return 'HistoryUpdateResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
             'Results:' + str(self.Results) + ', ' + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'

    __repr__ = __str__


class CallMethodRequest(object):
    '''
    :ivar ObjectId:
    :vartype ObjectId: NodeId
    :ivar MethodId:
    :vartype MethodId: NodeId
    :ivar InputArguments:
    :vartype InputArguments: Variant
    '''

    __slots__ = [
        "ObjectId",
        "MethodId",
        "InputArguments",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.ObjectId = NodeId()
        self.MethodId = NodeId()
        self.InputArguments = []

    def to_binary(self):
        packet = []
        packet.append(self.ObjectId.to_binary())
        packet.append(self.MethodId.to_binary())
        packet.append(uatype_Int32.pack(len(self.InputArguments)))
        for fieldname in self.InputArguments:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return CallMethodRequest(data)

    def _binary_init(self, data):
        self.ObjectId = NodeId.from_binary(data)
        self.MethodId = NodeId.from_binary(data)
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(Variant.from_binary(data))
        self.InputArguments = array

    def __str__(self):
        return 'CallMethodRequest(' + 'ObjectId:' + str(self.ObjectId) + ', ' + \
             'MethodId:' + str(self.MethodId) + ', ' + \
             'InputArguments:' + str(self.InputArguments) + ')'

    __repr__ = __str__


class CallMethodResult(object):
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

    __slots__ = [
        "StatusCode",
        "InputArgumentResults",
        "InputArgumentDiagnosticInfos",
        "OutputArguments",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.StatusCode = StatusCode()
        self.InputArgumentResults = []
        self.InputArgumentDiagnosticInfos = []
        self.OutputArguments = []

    def to_binary(self):
        packet = []
        packet.append(self.StatusCode.to_binary())
        packet.append(uatype_Int32.pack(len(self.InputArgumentResults)))
        for fieldname in self.InputArgumentResults:
            packet.append(fieldname.to_binary())
        packet.append(uatype_Int32.pack(len(self.InputArgumentDiagnosticInfos)))
        for fieldname in self.InputArgumentDiagnosticInfos:
            packet.append(fieldname.to_binary())
        packet.append(uatype_Int32.pack(len(self.OutputArguments)))
        for fieldname in self.OutputArguments:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return CallMethodResult(data)

    def _binary_init(self, data):
        self.StatusCode = StatusCode.from_binary(data)
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(StatusCode.from_binary(data))
        self.InputArgumentResults = array
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(DiagnosticInfo.from_binary(data))
        self.InputArgumentDiagnosticInfos = array
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(Variant.from_binary(data))
        self.OutputArguments = array

    def __str__(self):
        return 'CallMethodResult(' + 'StatusCode:' + str(self.StatusCode) + ', ' + \
             'InputArgumentResults:' + str(self.InputArgumentResults) + ', ' + \
             'InputArgumentDiagnosticInfos:' + str(self.InputArgumentDiagnosticInfos) + ', ' + \
             'OutputArguments:' + str(self.OutputArguments) + ')'

    __repr__ = __str__


class CallParameters(object):
    '''
    :ivar MethodsToCall:
    :vartype MethodsToCall: CallMethodRequest
    '''

    __slots__ = [
        "MethodsToCall",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.MethodsToCall = []

    def to_binary(self):
        packet = []
        packet.append(uatype_Int32.pack(len(self.MethodsToCall)))
        for fieldname in self.MethodsToCall:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return CallParameters(data)

    def _binary_init(self, data):
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(CallMethodRequest.from_binary(data))
        self.MethodsToCall = array

    def __str__(self):
        return 'CallParameters(' + 'MethodsToCall:' + str(self.MethodsToCall) + ')'

    __repr__ = __str__


class CallRequest(object):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: CallParameters
    '''

    __slots__ = [
        "TypeId",
        "RequestHeader",
        "Parameters",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.CallRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = CallParameters()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return CallRequest(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.RequestHeader = RequestHeader.from_binary(data)
        self.Parameters = CallParameters.from_binary(data)

    def __str__(self):
        return 'CallRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'RequestHeader:' + str(self.RequestHeader) + ', ' + \
             'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class CallResponse(object):
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

    __slots__ = [
        "TypeId",
        "ResponseHeader",
        "Results",
        "DiagnosticInfos",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.CallResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Results = []
        self.DiagnosticInfos = []

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(uatype_Int32.pack(len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(uatype_Int32.pack(len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return CallResponse(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.ResponseHeader = ResponseHeader.from_binary(data)
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(CallMethodResult.from_binary(data))
        self.Results = array
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(DiagnosticInfo.from_binary(data))
        self.DiagnosticInfos = array

    def __str__(self):
        return 'CallResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
             'Results:' + str(self.Results) + ', ' + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'

    __repr__ = __str__


class MonitoringFilter(object):
    '''
    '''

    __slots__ = [
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return

    def to_binary(self):
        packet = []
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return MonitoringFilter(data)

    def _binary_init(self, data):
        pass

    def __str__(self):
        return 'MonitoringFilter(' +  + ')'

    __repr__ = __str__


class DataChangeFilter(object):
    '''
    :ivar Trigger:
    :vartype Trigger: DataChangeTrigger
    :ivar DeadbandType:
    :vartype DeadbandType: UInt32
    :ivar DeadbandValue:
    :vartype DeadbandValue: Double
    '''

    __slots__ = [
        "Trigger",
        "DeadbandType",
        "DeadbandValue",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.Trigger = 0
        self.DeadbandType = 0
        self.DeadbandValue = 0

    def to_binary(self):
        packet = []
        packet.append(uatype_UInt32.pack(self.Trigger))
        packet.append(uatype_UInt32.pack(self.DeadbandType))
        packet.append(uatype_Double.pack(self.DeadbandValue))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return DataChangeFilter(data)

    def _binary_init(self, data):
        self.Trigger = uatype_UInt32.unpack(data.read(4))[0]
        self.DeadbandType = uatype_UInt32.unpack(data.read(4))[0]
        self.DeadbandValue = uatype_Double.unpack(data.read(8))[0]

    def __str__(self):
        return 'DataChangeFilter(' + 'Trigger:' + str(self.Trigger) + ', ' + \
             'DeadbandType:' + str(self.DeadbandType) + ', ' + \
             'DeadbandValue:' + str(self.DeadbandValue) + ')'

    __repr__ = __str__


class EventFilter(object):
    '''
    :ivar SelectClauses:
    :vartype SelectClauses: SimpleAttributeOperand
    :ivar WhereClause:
    :vartype WhereClause: ContentFilter
    '''

    __slots__ = [
        "SelectClauses",
        "WhereClause",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.SelectClauses = []
        self.WhereClause = ContentFilter()

    def to_binary(self):
        packet = []
        packet.append(uatype_Int32.pack(len(self.SelectClauses)))
        for fieldname in self.SelectClauses:
            packet.append(fieldname.to_binary())
        packet.append(self.WhereClause.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return EventFilter(data)

    def _binary_init(self, data):
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(SimpleAttributeOperand.from_binary(data))
        self.SelectClauses = array
        self.WhereClause = ContentFilter.from_binary(data)

    def __str__(self):
        return 'EventFilter(' + 'SelectClauses:' + str(self.SelectClauses) + ', ' + \
             'WhereClause:' + str(self.WhereClause) + ')'

    __repr__ = __str__


class AggregateConfiguration(object):
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

    __slots__ = [
        "UseServerCapabilitiesDefaults",
        "TreatUncertainAsBad",
        "PercentDataBad",
        "PercentDataGood",
        "UseSlopedExtrapolation",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.UseServerCapabilitiesDefaults = True
        self.TreatUncertainAsBad = True
        self.PercentDataBad = 0
        self.PercentDataGood = 0
        self.UseSlopedExtrapolation = True

    def to_binary(self):
        packet = []
        packet.append(uatype_Boolean.pack(self.UseServerCapabilitiesDefaults))
        packet.append(uatype_Boolean.pack(self.TreatUncertainAsBad))
        packet.append(uatype_Byte.pack(self.PercentDataBad))
        packet.append(uatype_Byte.pack(self.PercentDataGood))
        packet.append(uatype_Boolean.pack(self.UseSlopedExtrapolation))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return AggregateConfiguration(data)

    def _binary_init(self, data):
        self.UseServerCapabilitiesDefaults = uatype_Boolean.unpack(data.read(1))[0]
        self.TreatUncertainAsBad = uatype_Boolean.unpack(data.read(1))[0]
        self.PercentDataBad = uatype_Byte.unpack(data.read(1))[0]
        self.PercentDataGood = uatype_Byte.unpack(data.read(1))[0]
        self.UseSlopedExtrapolation = uatype_Boolean.unpack(data.read(1))[0]

    def __str__(self):
        return 'AggregateConfiguration(' + 'UseServerCapabilitiesDefaults:' + str(self.UseServerCapabilitiesDefaults) + ', ' + \
             'TreatUncertainAsBad:' + str(self.TreatUncertainAsBad) + ', ' + \
             'PercentDataBad:' + str(self.PercentDataBad) + ', ' + \
             'PercentDataGood:' + str(self.PercentDataGood) + ', ' + \
             'UseSlopedExtrapolation:' + str(self.UseSlopedExtrapolation) + ')'

    __repr__ = __str__


class AggregateFilter(object):
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

    __slots__ = [
        "StartTime",
        "AggregateType",
        "ProcessingInterval",
        "AggregateConfiguration",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.StartTime = datetime.now()
        self.AggregateType = NodeId()
        self.ProcessingInterval = 0
        self.AggregateConfiguration = AggregateConfiguration()

    def to_binary(self):
        packet = []
        packet.append(pack_datetime(self.StartTime))
        packet.append(self.AggregateType.to_binary())
        packet.append(uatype_Double.pack(self.ProcessingInterval))
        packet.append(self.AggregateConfiguration.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return AggregateFilter(data)

    def _binary_init(self, data):
        self.StartTime = unpack_datetime(data)
        self.AggregateType = NodeId.from_binary(data)
        self.ProcessingInterval = uatype_Double.unpack(data.read(8))[0]
        self.AggregateConfiguration = AggregateConfiguration.from_binary(data)

    def __str__(self):
        return 'AggregateFilter(' + 'StartTime:' + str(self.StartTime) + ', ' + \
             'AggregateType:' + str(self.AggregateType) + ', ' + \
             'ProcessingInterval:' + str(self.ProcessingInterval) + ', ' + \
             'AggregateConfiguration:' + str(self.AggregateConfiguration) + ')'

    __repr__ = __str__


class MonitoringFilterResult(object):
    '''
    '''

    __slots__ = [
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return

    def to_binary(self):
        packet = []
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return MonitoringFilterResult(data)

    def _binary_init(self, data):
        pass

    def __str__(self):
        return 'MonitoringFilterResult(' +  + ')'

    __repr__ = __str__


class EventFilterResult(object):
    '''
    :ivar SelectClauseResults:
    :vartype SelectClauseResults: StatusCode
    :ivar SelectClauseDiagnosticInfos:
    :vartype SelectClauseDiagnosticInfos: DiagnosticInfo
    :ivar WhereClauseResult:
    :vartype WhereClauseResult: ContentFilterResult
    '''

    __slots__ = [
        "SelectClauseResults",
        "SelectClauseDiagnosticInfos",
        "WhereClauseResult",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.SelectClauseResults = []
        self.SelectClauseDiagnosticInfos = []
        self.WhereClauseResult = ContentFilterResult()

    def to_binary(self):
        packet = []
        packet.append(uatype_Int32.pack(len(self.SelectClauseResults)))
        for fieldname in self.SelectClauseResults:
            packet.append(fieldname.to_binary())
        packet.append(uatype_Int32.pack(len(self.SelectClauseDiagnosticInfos)))
        for fieldname in self.SelectClauseDiagnosticInfos:
            packet.append(fieldname.to_binary())
        packet.append(self.WhereClauseResult.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return EventFilterResult(data)

    def _binary_init(self, data):
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(StatusCode.from_binary(data))
        self.SelectClauseResults = array
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(DiagnosticInfo.from_binary(data))
        self.SelectClauseDiagnosticInfos = array
        self.WhereClauseResult = ContentFilterResult.from_binary(data)

    def __str__(self):
        return 'EventFilterResult(' + 'SelectClauseResults:' + str(self.SelectClauseResults) + ', ' + \
             'SelectClauseDiagnosticInfos:' + str(self.SelectClauseDiagnosticInfos) + ', ' + \
             'WhereClauseResult:' + str(self.WhereClauseResult) + ')'

    __repr__ = __str__


class AggregateFilterResult(object):
    '''
    :ivar RevisedStartTime:
    :vartype RevisedStartTime: DateTime
    :ivar RevisedProcessingInterval:
    :vartype RevisedProcessingInterval: Double
    :ivar RevisedAggregateConfiguration:
    :vartype RevisedAggregateConfiguration: AggregateConfiguration
    '''

    __slots__ = [
        "RevisedStartTime",
        "RevisedProcessingInterval",
        "RevisedAggregateConfiguration",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.RevisedStartTime = datetime.now()
        self.RevisedProcessingInterval = 0
        self.RevisedAggregateConfiguration = AggregateConfiguration()

    def to_binary(self):
        packet = []
        packet.append(pack_datetime(self.RevisedStartTime))
        packet.append(uatype_Double.pack(self.RevisedProcessingInterval))
        packet.append(self.RevisedAggregateConfiguration.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return AggregateFilterResult(data)

    def _binary_init(self, data):
        self.RevisedStartTime = unpack_datetime(data)
        self.RevisedProcessingInterval = uatype_Double.unpack(data.read(8))[0]
        self.RevisedAggregateConfiguration = AggregateConfiguration.from_binary(data)

    def __str__(self):
        return 'AggregateFilterResult(' + 'RevisedStartTime:' + str(self.RevisedStartTime) + ', ' + \
             'RevisedProcessingInterval:' + str(self.RevisedProcessingInterval) + ', ' + \
             'RevisedAggregateConfiguration:' + str(self.RevisedAggregateConfiguration) + ')'

    __repr__ = __str__


class MonitoringParameters(object):
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

    __slots__ = [
        "ClientHandle",
        "SamplingInterval",
        "Filter",
        "QueueSize",
        "DiscardOldest",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.ClientHandle = 0
        self.SamplingInterval = 0
        self.Filter = None
        self.QueueSize = 0
        self.DiscardOldest = True

    def to_binary(self):
        packet = []
        packet.append(uatype_UInt32.pack(self.ClientHandle))
        packet.append(uatype_Double.pack(self.SamplingInterval))
        packet.append(extensionobject_to_binary(self.Filter))
        packet.append(uatype_UInt32.pack(self.QueueSize))
        packet.append(uatype_Boolean.pack(self.DiscardOldest))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return MonitoringParameters(data)

    def _binary_init(self, data):
        self.ClientHandle = uatype_UInt32.unpack(data.read(4))[0]
        self.SamplingInterval = uatype_Double.unpack(data.read(8))[0]
        self.Filter = extensionobject_from_binary(data)
        self.QueueSize = uatype_UInt32.unpack(data.read(4))[0]
        self.DiscardOldest = uatype_Boolean.unpack(data.read(1))[0]

    def __str__(self):
        return 'MonitoringParameters(' + 'ClientHandle:' + str(self.ClientHandle) + ', ' + \
             'SamplingInterval:' + str(self.SamplingInterval) + ', ' + \
             'Filter:' + str(self.Filter) + ', ' + \
             'QueueSize:' + str(self.QueueSize) + ', ' + \
             'DiscardOldest:' + str(self.DiscardOldest) + ')'

    __repr__ = __str__


class MonitoredItemCreateRequest(object):
    '''
    :ivar ItemToMonitor:
    :vartype ItemToMonitor: ReadValueId
    :ivar MonitoringMode:
    :vartype MonitoringMode: MonitoringMode
    :ivar RequestedParameters:
    :vartype RequestedParameters: MonitoringParameters
    '''

    __slots__ = [
        "ItemToMonitor",
        "MonitoringMode",
        "RequestedParameters",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.ItemToMonitor = ReadValueId()
        self.MonitoringMode = 0
        self.RequestedParameters = MonitoringParameters()

    def to_binary(self):
        packet = []
        packet.append(self.ItemToMonitor.to_binary())
        packet.append(uatype_UInt32.pack(self.MonitoringMode))
        packet.append(self.RequestedParameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return MonitoredItemCreateRequest(data)

    def _binary_init(self, data):
        self.ItemToMonitor = ReadValueId.from_binary(data)
        self.MonitoringMode = uatype_UInt32.unpack(data.read(4))[0]
        self.RequestedParameters = MonitoringParameters.from_binary(data)

    def __str__(self):
        return 'MonitoredItemCreateRequest(' + 'ItemToMonitor:' + str(self.ItemToMonitor) + ', ' + \
             'MonitoringMode:' + str(self.MonitoringMode) + ', ' + \
             'RequestedParameters:' + str(self.RequestedParameters) + ')'

    __repr__ = __str__


class MonitoredItemCreateResult(object):
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

    __slots__ = [
        "StatusCode",
        "MonitoredItemId",
        "RevisedSamplingInterval",
        "RevisedQueueSize",
        "FilterResult",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.StatusCode = StatusCode()
        self.MonitoredItemId = 0
        self.RevisedSamplingInterval = 0
        self.RevisedQueueSize = 0
        self.FilterResult = None

    def to_binary(self):
        packet = []
        packet.append(self.StatusCode.to_binary())
        packet.append(uatype_UInt32.pack(self.MonitoredItemId))
        packet.append(uatype_Double.pack(self.RevisedSamplingInterval))
        packet.append(uatype_UInt32.pack(self.RevisedQueueSize))
        packet.append(extensionobject_to_binary(self.FilterResult))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return MonitoredItemCreateResult(data)

    def _binary_init(self, data):
        self.StatusCode = StatusCode.from_binary(data)
        self.MonitoredItemId = uatype_UInt32.unpack(data.read(4))[0]
        self.RevisedSamplingInterval = uatype_Double.unpack(data.read(8))[0]
        self.RevisedQueueSize = uatype_UInt32.unpack(data.read(4))[0]
        self.FilterResult = extensionobject_from_binary(data)

    def __str__(self):
        return 'MonitoredItemCreateResult(' + 'StatusCode:' + str(self.StatusCode) + ', ' + \
             'MonitoredItemId:' + str(self.MonitoredItemId) + ', ' + \
             'RevisedSamplingInterval:' + str(self.RevisedSamplingInterval) + ', ' + \
             'RevisedQueueSize:' + str(self.RevisedQueueSize) + ', ' + \
             'FilterResult:' + str(self.FilterResult) + ')'

    __repr__ = __str__


class CreateMonitoredItemsParameters(object):
    '''
    :ivar SubscriptionId:
    :vartype SubscriptionId: UInt32
    :ivar TimestampsToReturn:
    :vartype TimestampsToReturn: TimestampsToReturn
    :ivar ItemsToCreate:
    :vartype ItemsToCreate: MonitoredItemCreateRequest
    '''

    __slots__ = [
        "SubscriptionId",
        "TimestampsToReturn",
        "ItemsToCreate",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.SubscriptionId = 0
        self.TimestampsToReturn = 0
        self.ItemsToCreate = []

    def to_binary(self):
        packet = []
        packet.append(uatype_UInt32.pack(self.SubscriptionId))
        packet.append(uatype_UInt32.pack(self.TimestampsToReturn))
        packet.append(uatype_Int32.pack(len(self.ItemsToCreate)))
        for fieldname in self.ItemsToCreate:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return CreateMonitoredItemsParameters(data)

    def _binary_init(self, data):
        self.SubscriptionId = uatype_UInt32.unpack(data.read(4))[0]
        self.TimestampsToReturn = uatype_UInt32.unpack(data.read(4))[0]
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(MonitoredItemCreateRequest.from_binary(data))
        self.ItemsToCreate = array

    def __str__(self):
        return 'CreateMonitoredItemsParameters(' + 'SubscriptionId:' + str(self.SubscriptionId) + ', ' + \
             'TimestampsToReturn:' + str(self.TimestampsToReturn) + ', ' + \
             'ItemsToCreate:' + str(self.ItemsToCreate) + ')'

    __repr__ = __str__


class CreateMonitoredItemsRequest(object):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: CreateMonitoredItemsParameters
    '''

    __slots__ = [
        "TypeId",
        "RequestHeader",
        "Parameters",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.CreateMonitoredItemsRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = CreateMonitoredItemsParameters()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return CreateMonitoredItemsRequest(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.RequestHeader = RequestHeader.from_binary(data)
        self.Parameters = CreateMonitoredItemsParameters.from_binary(data)

    def __str__(self):
        return 'CreateMonitoredItemsRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'RequestHeader:' + str(self.RequestHeader) + ', ' + \
             'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class CreateMonitoredItemsResponse(object):
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

    __slots__ = [
        "TypeId",
        "ResponseHeader",
        "Results",
        "DiagnosticInfos",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.CreateMonitoredItemsResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Results = []
        self.DiagnosticInfos = []

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(uatype_Int32.pack(len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(uatype_Int32.pack(len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return CreateMonitoredItemsResponse(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.ResponseHeader = ResponseHeader.from_binary(data)
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(MonitoredItemCreateResult.from_binary(data))
        self.Results = array
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(DiagnosticInfo.from_binary(data))
        self.DiagnosticInfos = array

    def __str__(self):
        return 'CreateMonitoredItemsResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
             'Results:' + str(self.Results) + ', ' + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'

    __repr__ = __str__


class MonitoredItemModifyRequest(object):
    '''
    :ivar MonitoredItemId:
    :vartype MonitoredItemId: UInt32
    :ivar RequestedParameters:
    :vartype RequestedParameters: MonitoringParameters
    '''

    __slots__ = [
        "MonitoredItemId",
        "RequestedParameters",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.MonitoredItemId = 0
        self.RequestedParameters = MonitoringParameters()

    def to_binary(self):
        packet = []
        packet.append(uatype_UInt32.pack(self.MonitoredItemId))
        packet.append(self.RequestedParameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return MonitoredItemModifyRequest(data)

    def _binary_init(self, data):
        self.MonitoredItemId = uatype_UInt32.unpack(data.read(4))[0]
        self.RequestedParameters = MonitoringParameters.from_binary(data)

    def __str__(self):
        return 'MonitoredItemModifyRequest(' + 'MonitoredItemId:' + str(self.MonitoredItemId) + ', ' + \
             'RequestedParameters:' + str(self.RequestedParameters) + ')'

    __repr__ = __str__


class MonitoredItemModifyResult(object):
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

    __slots__ = [
        "StatusCode",
        "RevisedSamplingInterval",
        "RevisedQueueSize",
        "FilterResult",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.StatusCode = StatusCode()
        self.RevisedSamplingInterval = 0
        self.RevisedQueueSize = 0
        self.FilterResult = None

    def to_binary(self):
        packet = []
        packet.append(self.StatusCode.to_binary())
        packet.append(uatype_Double.pack(self.RevisedSamplingInterval))
        packet.append(uatype_UInt32.pack(self.RevisedQueueSize))
        packet.append(extensionobject_to_binary(self.FilterResult))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return MonitoredItemModifyResult(data)

    def _binary_init(self, data):
        self.StatusCode = StatusCode.from_binary(data)
        self.RevisedSamplingInterval = uatype_Double.unpack(data.read(8))[0]
        self.RevisedQueueSize = uatype_UInt32.unpack(data.read(4))[0]
        self.FilterResult = extensionobject_from_binary(data)

    def __str__(self):
        return 'MonitoredItemModifyResult(' + 'StatusCode:' + str(self.StatusCode) + ', ' + \
             'RevisedSamplingInterval:' + str(self.RevisedSamplingInterval) + ', ' + \
             'RevisedQueueSize:' + str(self.RevisedQueueSize) + ', ' + \
             'FilterResult:' + str(self.FilterResult) + ')'

    __repr__ = __str__


class ModifyMonitoredItemsParameters(object):
    '''
    :ivar SubscriptionId:
    :vartype SubscriptionId: UInt32
    :ivar TimestampsToReturn:
    :vartype TimestampsToReturn: TimestampsToReturn
    :ivar ItemsToModify:
    :vartype ItemsToModify: MonitoredItemModifyRequest
    '''

    __slots__ = [
        "SubscriptionId",
        "TimestampsToReturn",
        "ItemsToModify",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.SubscriptionId = 0
        self.TimestampsToReturn = 0
        self.ItemsToModify = []

    def to_binary(self):
        packet = []
        packet.append(uatype_UInt32.pack(self.SubscriptionId))
        packet.append(uatype_UInt32.pack(self.TimestampsToReturn))
        packet.append(uatype_Int32.pack(len(self.ItemsToModify)))
        for fieldname in self.ItemsToModify:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return ModifyMonitoredItemsParameters(data)

    def _binary_init(self, data):
        self.SubscriptionId = uatype_UInt32.unpack(data.read(4))[0]
        self.TimestampsToReturn = uatype_UInt32.unpack(data.read(4))[0]
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(MonitoredItemModifyRequest.from_binary(data))
        self.ItemsToModify = array

    def __str__(self):
        return 'ModifyMonitoredItemsParameters(' + 'SubscriptionId:' + str(self.SubscriptionId) + ', ' + \
             'TimestampsToReturn:' + str(self.TimestampsToReturn) + ', ' + \
             'ItemsToModify:' + str(self.ItemsToModify) + ')'

    __repr__ = __str__


class ModifyMonitoredItemsRequest(object):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: ModifyMonitoredItemsParameters
    '''

    __slots__ = [
        "TypeId",
        "RequestHeader",
        "Parameters",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.ModifyMonitoredItemsRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = ModifyMonitoredItemsParameters()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return ModifyMonitoredItemsRequest(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.RequestHeader = RequestHeader.from_binary(data)
        self.Parameters = ModifyMonitoredItemsParameters.from_binary(data)

    def __str__(self):
        return 'ModifyMonitoredItemsRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'RequestHeader:' + str(self.RequestHeader) + ', ' + \
             'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class ModifyMonitoredItemsResponse(object):
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

    __slots__ = [
        "TypeId",
        "ResponseHeader",
        "Results",
        "DiagnosticInfos",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.ModifyMonitoredItemsResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Results = []
        self.DiagnosticInfos = []

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(uatype_Int32.pack(len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(uatype_Int32.pack(len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return ModifyMonitoredItemsResponse(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.ResponseHeader = ResponseHeader.from_binary(data)
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(MonitoredItemModifyResult.from_binary(data))
        self.Results = array
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(DiagnosticInfo.from_binary(data))
        self.DiagnosticInfos = array

    def __str__(self):
        return 'ModifyMonitoredItemsResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
             'Results:' + str(self.Results) + ', ' + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'

    __repr__ = __str__


class SetMonitoringModeParameters(object):
    '''
    :ivar SubscriptionId:
    :vartype SubscriptionId: UInt32
    :ivar MonitoringMode:
    :vartype MonitoringMode: MonitoringMode
    :ivar MonitoredItemIds:
    :vartype MonitoredItemIds: UInt32
    '''

    __slots__ = [
        "SubscriptionId",
        "MonitoringMode",
        "MonitoredItemIds",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.SubscriptionId = 0
        self.MonitoringMode = 0
        self.MonitoredItemIds = []

    def to_binary(self):
        packet = []
        packet.append(uatype_UInt32.pack(self.SubscriptionId))
        packet.append(uatype_UInt32.pack(self.MonitoringMode))
        packet.append(uatype_Int32.pack(len(self.MonitoredItemIds)))
        for fieldname in self.MonitoredItemIds:
            packet.append(uatype_UInt32.pack(fieldname))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return SetMonitoringModeParameters(data)

    def _binary_init(self, data):
        self.SubscriptionId = uatype_UInt32.unpack(data.read(4))[0]
        self.MonitoringMode = uatype_UInt32.unpack(data.read(4))[0]
        self.MonitoredItemIds = unpack_uatype_array('UInt32', data)

    def __str__(self):
        return 'SetMonitoringModeParameters(' + 'SubscriptionId:' + str(self.SubscriptionId) + ', ' + \
             'MonitoringMode:' + str(self.MonitoringMode) + ', ' + \
             'MonitoredItemIds:' + str(self.MonitoredItemIds) + ')'

    __repr__ = __str__


class SetMonitoringModeRequest(object):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: SetMonitoringModeParameters
    '''

    __slots__ = [
        "TypeId",
        "RequestHeader",
        "Parameters",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.SetMonitoringModeRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = SetMonitoringModeParameters()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return SetMonitoringModeRequest(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.RequestHeader = RequestHeader.from_binary(data)
        self.Parameters = SetMonitoringModeParameters.from_binary(data)

    def __str__(self):
        return 'SetMonitoringModeRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'RequestHeader:' + str(self.RequestHeader) + ', ' + \
             'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class SetMonitoringModeResult(object):
    '''
    :ivar Results:
    :vartype Results: StatusCode
    :ivar DiagnosticInfos:
    :vartype DiagnosticInfos: DiagnosticInfo
    '''

    __slots__ = [
        "Results",
        "DiagnosticInfos",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.Results = []
        self.DiagnosticInfos = []

    def to_binary(self):
        packet = []
        packet.append(uatype_Int32.pack(len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(uatype_Int32.pack(len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return SetMonitoringModeResult(data)

    def _binary_init(self, data):
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(StatusCode.from_binary(data))
        self.Results = array
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(DiagnosticInfo.from_binary(data))
        self.DiagnosticInfos = array

    def __str__(self):
        return 'SetMonitoringModeResult(' + 'Results:' + str(self.Results) + ', ' + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'

    __repr__ = __str__


class SetMonitoringModeResponse(object):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    :ivar Parameters:
    :vartype Parameters: SetMonitoringModeResult
    '''

    __slots__ = [
        "TypeId",
        "ResponseHeader",
        "Parameters",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.SetMonitoringModeResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = SetMonitoringModeResult()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return SetMonitoringModeResponse(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.ResponseHeader = ResponseHeader.from_binary(data)
        self.Parameters = SetMonitoringModeResult.from_binary(data)

    def __str__(self):
        return 'SetMonitoringModeResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
             'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class SetTriggeringParameters(object):
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

    __slots__ = [
        "SubscriptionId",
        "TriggeringItemId",
        "LinksToAdd",
        "LinksToRemove",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.SubscriptionId = 0
        self.TriggeringItemId = 0
        self.LinksToAdd = []
        self.LinksToRemove = []

    def to_binary(self):
        packet = []
        packet.append(uatype_UInt32.pack(self.SubscriptionId))
        packet.append(uatype_UInt32.pack(self.TriggeringItemId))
        packet.append(uatype_Int32.pack(len(self.LinksToAdd)))
        for fieldname in self.LinksToAdd:
            packet.append(uatype_UInt32.pack(fieldname))
        packet.append(uatype_Int32.pack(len(self.LinksToRemove)))
        for fieldname in self.LinksToRemove:
            packet.append(uatype_UInt32.pack(fieldname))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return SetTriggeringParameters(data)

    def _binary_init(self, data):
        self.SubscriptionId = uatype_UInt32.unpack(data.read(4))[0]
        self.TriggeringItemId = uatype_UInt32.unpack(data.read(4))[0]
        self.LinksToAdd = unpack_uatype_array('UInt32', data)
        self.LinksToRemove = unpack_uatype_array('UInt32', data)

    def __str__(self):
        return 'SetTriggeringParameters(' + 'SubscriptionId:' + str(self.SubscriptionId) + ', ' + \
             'TriggeringItemId:' + str(self.TriggeringItemId) + ', ' + \
             'LinksToAdd:' + str(self.LinksToAdd) + ', ' + \
             'LinksToRemove:' + str(self.LinksToRemove) + ')'

    __repr__ = __str__


class SetTriggeringRequest(object):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: SetTriggeringParameters
    '''

    __slots__ = [
        "TypeId",
        "RequestHeader",
        "Parameters",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.SetTriggeringRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = SetTriggeringParameters()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return SetTriggeringRequest(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.RequestHeader = RequestHeader.from_binary(data)
        self.Parameters = SetTriggeringParameters.from_binary(data)

    def __str__(self):
        return 'SetTriggeringRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'RequestHeader:' + str(self.RequestHeader) + ', ' + \
             'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class SetTriggeringResult(object):
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

    __slots__ = [
        "AddResults",
        "AddDiagnosticInfos",
        "RemoveResults",
        "RemoveDiagnosticInfos",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.AddResults = []
        self.AddDiagnosticInfos = []
        self.RemoveResults = []
        self.RemoveDiagnosticInfos = []

    def to_binary(self):
        packet = []
        packet.append(uatype_Int32.pack(len(self.AddResults)))
        for fieldname in self.AddResults:
            packet.append(fieldname.to_binary())
        packet.append(uatype_Int32.pack(len(self.AddDiagnosticInfos)))
        for fieldname in self.AddDiagnosticInfos:
            packet.append(fieldname.to_binary())
        packet.append(uatype_Int32.pack(len(self.RemoveResults)))
        for fieldname in self.RemoveResults:
            packet.append(fieldname.to_binary())
        packet.append(uatype_Int32.pack(len(self.RemoveDiagnosticInfos)))
        for fieldname in self.RemoveDiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return SetTriggeringResult(data)

    def _binary_init(self, data):
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(StatusCode.from_binary(data))
        self.AddResults = array
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(DiagnosticInfo.from_binary(data))
        self.AddDiagnosticInfos = array
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(StatusCode.from_binary(data))
        self.RemoveResults = array
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(DiagnosticInfo.from_binary(data))
        self.RemoveDiagnosticInfos = array

    def __str__(self):
        return 'SetTriggeringResult(' + 'AddResults:' + str(self.AddResults) + ', ' + \
             'AddDiagnosticInfos:' + str(self.AddDiagnosticInfos) + ', ' + \
             'RemoveResults:' + str(self.RemoveResults) + ', ' + \
             'RemoveDiagnosticInfos:' + str(self.RemoveDiagnosticInfos) + ')'

    __repr__ = __str__


class SetTriggeringResponse(object):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    :ivar Parameters:
    :vartype Parameters: SetTriggeringResult
    '''

    __slots__ = [
        "TypeId",
        "ResponseHeader",
        "Parameters",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.SetTriggeringResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = SetTriggeringResult()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return SetTriggeringResponse(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.ResponseHeader = ResponseHeader.from_binary(data)
        self.Parameters = SetTriggeringResult.from_binary(data)

    def __str__(self):
        return 'SetTriggeringResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
             'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class DeleteMonitoredItemsParameters(object):
    '''
    :ivar SubscriptionId:
    :vartype SubscriptionId: UInt32
    :ivar MonitoredItemIds:
    :vartype MonitoredItemIds: UInt32
    '''

    __slots__ = [
        "SubscriptionId",
        "MonitoredItemIds",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.SubscriptionId = 0
        self.MonitoredItemIds = []

    def to_binary(self):
        packet = []
        packet.append(uatype_UInt32.pack(self.SubscriptionId))
        packet.append(uatype_Int32.pack(len(self.MonitoredItemIds)))
        for fieldname in self.MonitoredItemIds:
            packet.append(uatype_UInt32.pack(fieldname))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return DeleteMonitoredItemsParameters(data)

    def _binary_init(self, data):
        self.SubscriptionId = uatype_UInt32.unpack(data.read(4))[0]
        self.MonitoredItemIds = unpack_uatype_array('UInt32', data)

    def __str__(self):
        return 'DeleteMonitoredItemsParameters(' + 'SubscriptionId:' + str(self.SubscriptionId) + ', ' + \
             'MonitoredItemIds:' + str(self.MonitoredItemIds) + ')'

    __repr__ = __str__


class DeleteMonitoredItemsRequest(object):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: DeleteMonitoredItemsParameters
    '''

    __slots__ = [
        "TypeId",
        "RequestHeader",
        "Parameters",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.DeleteMonitoredItemsRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = DeleteMonitoredItemsParameters()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return DeleteMonitoredItemsRequest(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.RequestHeader = RequestHeader.from_binary(data)
        self.Parameters = DeleteMonitoredItemsParameters.from_binary(data)

    def __str__(self):
        return 'DeleteMonitoredItemsRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'RequestHeader:' + str(self.RequestHeader) + ', ' + \
             'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class DeleteMonitoredItemsResponse(object):
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

    __slots__ = [
        "TypeId",
        "ResponseHeader",
        "Results",
        "DiagnosticInfos",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.DeleteMonitoredItemsResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Results = []
        self.DiagnosticInfos = []

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(uatype_Int32.pack(len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(uatype_Int32.pack(len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return DeleteMonitoredItemsResponse(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.ResponseHeader = ResponseHeader.from_binary(data)
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(StatusCode.from_binary(data))
        self.Results = array
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(DiagnosticInfo.from_binary(data))
        self.DiagnosticInfos = array

    def __str__(self):
        return 'DeleteMonitoredItemsResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
             'Results:' + str(self.Results) + ', ' + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'

    __repr__ = __str__


class CreateSubscriptionParameters(object):
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

    __slots__ = [
        "RequestedPublishingInterval",
        "RequestedLifetimeCount",
        "RequestedMaxKeepAliveCount",
        "MaxNotificationsPerPublish",
        "PublishingEnabled",
        "Priority",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.RequestedPublishingInterval = 0
        self.RequestedLifetimeCount = 0
        self.RequestedMaxKeepAliveCount = 0
        self.MaxNotificationsPerPublish = 0
        self.PublishingEnabled = True
        self.Priority = 0

    def to_binary(self):
        packet = []
        packet.append(uatype_Double.pack(self.RequestedPublishingInterval))
        packet.append(uatype_UInt32.pack(self.RequestedLifetimeCount))
        packet.append(uatype_UInt32.pack(self.RequestedMaxKeepAliveCount))
        packet.append(uatype_UInt32.pack(self.MaxNotificationsPerPublish))
        packet.append(uatype_Boolean.pack(self.PublishingEnabled))
        packet.append(uatype_Byte.pack(self.Priority))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return CreateSubscriptionParameters(data)

    def _binary_init(self, data):
        self.RequestedPublishingInterval = uatype_Double.unpack(data.read(8))[0]
        self.RequestedLifetimeCount = uatype_UInt32.unpack(data.read(4))[0]
        self.RequestedMaxKeepAliveCount = uatype_UInt32.unpack(data.read(4))[0]
        self.MaxNotificationsPerPublish = uatype_UInt32.unpack(data.read(4))[0]
        self.PublishingEnabled = uatype_Boolean.unpack(data.read(1))[0]
        self.Priority = uatype_Byte.unpack(data.read(1))[0]

    def __str__(self):
        return 'CreateSubscriptionParameters(' + 'RequestedPublishingInterval:' + str(self.RequestedPublishingInterval) + ', ' + \
             'RequestedLifetimeCount:' + str(self.RequestedLifetimeCount) + ', ' + \
             'RequestedMaxKeepAliveCount:' + str(self.RequestedMaxKeepAliveCount) + ', ' + \
             'MaxNotificationsPerPublish:' + str(self.MaxNotificationsPerPublish) + ', ' + \
             'PublishingEnabled:' + str(self.PublishingEnabled) + ', ' + \
             'Priority:' + str(self.Priority) + ')'

    __repr__ = __str__


class CreateSubscriptionRequest(object):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: CreateSubscriptionParameters
    '''

    __slots__ = [
        "TypeId",
        "RequestHeader",
        "Parameters",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.CreateSubscriptionRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = CreateSubscriptionParameters()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return CreateSubscriptionRequest(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.RequestHeader = RequestHeader.from_binary(data)
        self.Parameters = CreateSubscriptionParameters.from_binary(data)

    def __str__(self):
        return 'CreateSubscriptionRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'RequestHeader:' + str(self.RequestHeader) + ', ' + \
             'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class CreateSubscriptionResult(object):
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

    __slots__ = [
        "SubscriptionId",
        "RevisedPublishingInterval",
        "RevisedLifetimeCount",
        "RevisedMaxKeepAliveCount",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.SubscriptionId = 0
        self.RevisedPublishingInterval = 0
        self.RevisedLifetimeCount = 0
        self.RevisedMaxKeepAliveCount = 0

    def to_binary(self):
        packet = []
        packet.append(uatype_UInt32.pack(self.SubscriptionId))
        packet.append(uatype_Double.pack(self.RevisedPublishingInterval))
        packet.append(uatype_UInt32.pack(self.RevisedLifetimeCount))
        packet.append(uatype_UInt32.pack(self.RevisedMaxKeepAliveCount))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return CreateSubscriptionResult(data)

    def _binary_init(self, data):
        self.SubscriptionId = uatype_UInt32.unpack(data.read(4))[0]
        self.RevisedPublishingInterval = uatype_Double.unpack(data.read(8))[0]
        self.RevisedLifetimeCount = uatype_UInt32.unpack(data.read(4))[0]
        self.RevisedMaxKeepAliveCount = uatype_UInt32.unpack(data.read(4))[0]

    def __str__(self):
        return 'CreateSubscriptionResult(' + 'SubscriptionId:' + str(self.SubscriptionId) + ', ' + \
             'RevisedPublishingInterval:' + str(self.RevisedPublishingInterval) + ', ' + \
             'RevisedLifetimeCount:' + str(self.RevisedLifetimeCount) + ', ' + \
             'RevisedMaxKeepAliveCount:' + str(self.RevisedMaxKeepAliveCount) + ')'

    __repr__ = __str__


class CreateSubscriptionResponse(object):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    :ivar Parameters:
    :vartype Parameters: CreateSubscriptionResult
    '''

    __slots__ = [
        "TypeId",
        "ResponseHeader",
        "Parameters",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.CreateSubscriptionResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = CreateSubscriptionResult()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return CreateSubscriptionResponse(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.ResponseHeader = ResponseHeader.from_binary(data)
        self.Parameters = CreateSubscriptionResult.from_binary(data)

    def __str__(self):
        return 'CreateSubscriptionResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
             'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class ModifySubscriptionParameters(object):
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

    __slots__ = [
        "SubscriptionId",
        "RequestedPublishingInterval",
        "RequestedLifetimeCount",
        "RequestedMaxKeepAliveCount",
        "MaxNotificationsPerPublish",
        "Priority",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.SubscriptionId = 0
        self.RequestedPublishingInterval = 0
        self.RequestedLifetimeCount = 0
        self.RequestedMaxKeepAliveCount = 0
        self.MaxNotificationsPerPublish = 0
        self.Priority = 0

    def to_binary(self):
        packet = []
        packet.append(uatype_UInt32.pack(self.SubscriptionId))
        packet.append(uatype_Double.pack(self.RequestedPublishingInterval))
        packet.append(uatype_UInt32.pack(self.RequestedLifetimeCount))
        packet.append(uatype_UInt32.pack(self.RequestedMaxKeepAliveCount))
        packet.append(uatype_UInt32.pack(self.MaxNotificationsPerPublish))
        packet.append(uatype_Byte.pack(self.Priority))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return ModifySubscriptionParameters(data)

    def _binary_init(self, data):
        self.SubscriptionId = uatype_UInt32.unpack(data.read(4))[0]
        self.RequestedPublishingInterval = uatype_Double.unpack(data.read(8))[0]
        self.RequestedLifetimeCount = uatype_UInt32.unpack(data.read(4))[0]
        self.RequestedMaxKeepAliveCount = uatype_UInt32.unpack(data.read(4))[0]
        self.MaxNotificationsPerPublish = uatype_UInt32.unpack(data.read(4))[0]
        self.Priority = uatype_Byte.unpack(data.read(1))[0]

    def __str__(self):
        return 'ModifySubscriptionParameters(' + 'SubscriptionId:' + str(self.SubscriptionId) + ', ' + \
             'RequestedPublishingInterval:' + str(self.RequestedPublishingInterval) + ', ' + \
             'RequestedLifetimeCount:' + str(self.RequestedLifetimeCount) + ', ' + \
             'RequestedMaxKeepAliveCount:' + str(self.RequestedMaxKeepAliveCount) + ', ' + \
             'MaxNotificationsPerPublish:' + str(self.MaxNotificationsPerPublish) + ', ' + \
             'Priority:' + str(self.Priority) + ')'

    __repr__ = __str__


class ModifySubscriptionRequest(object):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: ModifySubscriptionParameters
    '''

    __slots__ = [
        "TypeId",
        "RequestHeader",
        "Parameters",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.ModifySubscriptionRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = ModifySubscriptionParameters()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return ModifySubscriptionRequest(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.RequestHeader = RequestHeader.from_binary(data)
        self.Parameters = ModifySubscriptionParameters.from_binary(data)

    def __str__(self):
        return 'ModifySubscriptionRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'RequestHeader:' + str(self.RequestHeader) + ', ' + \
             'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class ModifySubscriptionResult(object):
    '''
    :ivar RevisedPublishingInterval:
    :vartype RevisedPublishingInterval: Double
    :ivar RevisedLifetimeCount:
    :vartype RevisedLifetimeCount: UInt32
    :ivar RevisedMaxKeepAliveCount:
    :vartype RevisedMaxKeepAliveCount: UInt32
    '''

    __slots__ = [
        "RevisedPublishingInterval",
        "RevisedLifetimeCount",
        "RevisedMaxKeepAliveCount",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.RevisedPublishingInterval = 0
        self.RevisedLifetimeCount = 0
        self.RevisedMaxKeepAliveCount = 0

    def to_binary(self):
        packet = []
        packet.append(uatype_Double.pack(self.RevisedPublishingInterval))
        packet.append(uatype_UInt32.pack(self.RevisedLifetimeCount))
        packet.append(uatype_UInt32.pack(self.RevisedMaxKeepAliveCount))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return ModifySubscriptionResult(data)

    def _binary_init(self, data):
        self.RevisedPublishingInterval = uatype_Double.unpack(data.read(8))[0]
        self.RevisedLifetimeCount = uatype_UInt32.unpack(data.read(4))[0]
        self.RevisedMaxKeepAliveCount = uatype_UInt32.unpack(data.read(4))[0]

    def __str__(self):
        return 'ModifySubscriptionResult(' + 'RevisedPublishingInterval:' + str(self.RevisedPublishingInterval) + ', ' + \
             'RevisedLifetimeCount:' + str(self.RevisedLifetimeCount) + ', ' + \
             'RevisedMaxKeepAliveCount:' + str(self.RevisedMaxKeepAliveCount) + ')'

    __repr__ = __str__


class ModifySubscriptionResponse(object):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    :ivar Parameters:
    :vartype Parameters: ModifySubscriptionResult
    '''

    __slots__ = [
        "TypeId",
        "ResponseHeader",
        "Parameters",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.ModifySubscriptionResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = ModifySubscriptionResult()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return ModifySubscriptionResponse(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.ResponseHeader = ResponseHeader.from_binary(data)
        self.Parameters = ModifySubscriptionResult.from_binary(data)

    def __str__(self):
        return 'ModifySubscriptionResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
             'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class SetPublishingModeParameters(object):
    '''
    :ivar PublishingEnabled:
    :vartype PublishingEnabled: Boolean
    :ivar SubscriptionIds:
    :vartype SubscriptionIds: UInt32
    '''

    __slots__ = [
        "PublishingEnabled",
        "SubscriptionIds",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.PublishingEnabled = True
        self.SubscriptionIds = []

    def to_binary(self):
        packet = []
        packet.append(uatype_Boolean.pack(self.PublishingEnabled))
        packet.append(uatype_Int32.pack(len(self.SubscriptionIds)))
        for fieldname in self.SubscriptionIds:
            packet.append(uatype_UInt32.pack(fieldname))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return SetPublishingModeParameters(data)

    def _binary_init(self, data):
        self.PublishingEnabled = uatype_Boolean.unpack(data.read(1))[0]
        self.SubscriptionIds = unpack_uatype_array('UInt32', data)

    def __str__(self):
        return 'SetPublishingModeParameters(' + 'PublishingEnabled:' + str(self.PublishingEnabled) + ', ' + \
             'SubscriptionIds:' + str(self.SubscriptionIds) + ')'

    __repr__ = __str__


class SetPublishingModeRequest(object):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: SetPublishingModeParameters
    '''

    __slots__ = [
        "TypeId",
        "RequestHeader",
        "Parameters",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.SetPublishingModeRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = SetPublishingModeParameters()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return SetPublishingModeRequest(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.RequestHeader = RequestHeader.from_binary(data)
        self.Parameters = SetPublishingModeParameters.from_binary(data)

    def __str__(self):
        return 'SetPublishingModeRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'RequestHeader:' + str(self.RequestHeader) + ', ' + \
             'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class SetPublishingModeResult(object):
    '''
    :ivar Results:
    :vartype Results: StatusCode
    :ivar DiagnosticInfos:
    :vartype DiagnosticInfos: DiagnosticInfo
    '''

    __slots__ = [
        "Results",
        "DiagnosticInfos",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.Results = []
        self.DiagnosticInfos = []

    def to_binary(self):
        packet = []
        packet.append(uatype_Int32.pack(len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(uatype_Int32.pack(len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return SetPublishingModeResult(data)

    def _binary_init(self, data):
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(StatusCode.from_binary(data))
        self.Results = array
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(DiagnosticInfo.from_binary(data))
        self.DiagnosticInfos = array

    def __str__(self):
        return 'SetPublishingModeResult(' + 'Results:' + str(self.Results) + ', ' + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'

    __repr__ = __str__


class SetPublishingModeResponse(object):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    :ivar Parameters:
    :vartype Parameters: SetPublishingModeResult
    '''

    __slots__ = [
        "TypeId",
        "ResponseHeader",
        "Parameters",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.SetPublishingModeResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = SetPublishingModeResult()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return SetPublishingModeResponse(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.ResponseHeader = ResponseHeader.from_binary(data)
        self.Parameters = SetPublishingModeResult.from_binary(data)

    def __str__(self):
        return 'SetPublishingModeResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
             'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class NotificationMessage(object):
    '''
    :ivar SequenceNumber:
    :vartype SequenceNumber: UInt32
    :ivar PublishTime:
    :vartype PublishTime: DateTime
    :ivar NotificationData:
    :vartype NotificationData: ExtensionObject
    '''

    __slots__ = [
        "SequenceNumber",
        "PublishTime",
        "NotificationData",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.SequenceNumber = 0
        self.PublishTime = datetime.now()
        self.NotificationData = []

    def to_binary(self):
        packet = []
        packet.append(uatype_UInt32.pack(self.SequenceNumber))
        packet.append(pack_datetime(self.PublishTime))
        packet.append(uatype_Int32.pack(len(self.NotificationData)))
        for fieldname in self.NotificationData:
            packet.append(extensionobject_to_binary(fieldname))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return NotificationMessage(data)

    def _binary_init(self, data):
        self.SequenceNumber = uatype_UInt32.unpack(data.read(4))[0]
        self.PublishTime = unpack_datetime(data)
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(extensionobject_from_binary(data))
        self.NotificationData = array

    def __str__(self):
        return 'NotificationMessage(' + 'SequenceNumber:' + str(self.SequenceNumber) + ', ' + \
             'PublishTime:' + str(self.PublishTime) + ', ' + \
             'NotificationData:' + str(self.NotificationData) + ')'

    __repr__ = __str__


class NotificationData(object):
    '''
    '''

    __slots__ = [
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return

    def to_binary(self):
        packet = []
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return NotificationData(data)

    def _binary_init(self, data):
        pass

    def __str__(self):
        return 'NotificationData(' +  + ')'

    __repr__ = __str__


class DataChangeNotification(object):
    '''
    :ivar MonitoredItems:
    :vartype MonitoredItems: MonitoredItemNotification
    :ivar DiagnosticInfos:
    :vartype DiagnosticInfos: DiagnosticInfo
    '''

    __slots__ = [
        "MonitoredItems",
        "DiagnosticInfos",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.MonitoredItems = []
        self.DiagnosticInfos = []

    def to_binary(self):
        packet = []
        packet.append(uatype_Int32.pack(len(self.MonitoredItems)))
        for fieldname in self.MonitoredItems:
            packet.append(fieldname.to_binary())
        packet.append(uatype_Int32.pack(len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return DataChangeNotification(data)

    def _binary_init(self, data):
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(MonitoredItemNotification.from_binary(data))
        self.MonitoredItems = array
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(DiagnosticInfo.from_binary(data))
        self.DiagnosticInfos = array

    def __str__(self):
        return 'DataChangeNotification(' + 'MonitoredItems:' + str(self.MonitoredItems) + ', ' + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'

    __repr__ = __str__


class MonitoredItemNotification(object):
    '''
    :ivar ClientHandle:
    :vartype ClientHandle: UInt32
    :ivar Value:
    :vartype Value: DataValue
    '''

    __slots__ = [
        "ClientHandle",
        "Value",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.ClientHandle = 0
        self.Value = DataValue()

    def to_binary(self):
        packet = []
        packet.append(uatype_UInt32.pack(self.ClientHandle))
        packet.append(self.Value.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return MonitoredItemNotification(data)

    def _binary_init(self, data):
        self.ClientHandle = uatype_UInt32.unpack(data.read(4))[0]
        self.Value = DataValue.from_binary(data)

    def __str__(self):
        return 'MonitoredItemNotification(' + 'ClientHandle:' + str(self.ClientHandle) + ', ' + \
             'Value:' + str(self.Value) + ')'

    __repr__ = __str__


class EventNotificationList(object):
    '''
    :ivar Events:
    :vartype Events: EventFieldList
    '''

    __slots__ = [
        "Events",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.Events = []

    def to_binary(self):
        packet = []
        packet.append(uatype_Int32.pack(len(self.Events)))
        for fieldname in self.Events:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return EventNotificationList(data)

    def _binary_init(self, data):
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(EventFieldList.from_binary(data))
        self.Events = array

    def __str__(self):
        return 'EventNotificationList(' + 'Events:' + str(self.Events) + ')'

    __repr__ = __str__


class EventFieldList(object):
    '''
    :ivar ClientHandle:
    :vartype ClientHandle: UInt32
    :ivar EventFields:
    :vartype EventFields: Variant
    '''

    __slots__ = [
        "ClientHandle",
        "EventFields",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.ClientHandle = 0
        self.EventFields = []

    def to_binary(self):
        packet = []
        packet.append(uatype_UInt32.pack(self.ClientHandle))
        packet.append(uatype_Int32.pack(len(self.EventFields)))
        for fieldname in self.EventFields:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return EventFieldList(data)

    def _binary_init(self, data):
        self.ClientHandle = uatype_UInt32.unpack(data.read(4))[0]
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(Variant.from_binary(data))
        self.EventFields = array

    def __str__(self):
        return 'EventFieldList(' + 'ClientHandle:' + str(self.ClientHandle) + ', ' + \
             'EventFields:' + str(self.EventFields) + ')'

    __repr__ = __str__


class HistoryEventFieldList(object):
    '''
    :ivar EventFields:
    :vartype EventFields: Variant
    '''

    __slots__ = [
        "EventFields",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.EventFields = []

    def to_binary(self):
        packet = []
        packet.append(uatype_Int32.pack(len(self.EventFields)))
        for fieldname in self.EventFields:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return HistoryEventFieldList(data)

    def _binary_init(self, data):
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(Variant.from_binary(data))
        self.EventFields = array

    def __str__(self):
        return 'HistoryEventFieldList(' + 'EventFields:' + str(self.EventFields) + ')'

    __repr__ = __str__


class StatusChangeNotification(object):
    '''
    :ivar Status:
    :vartype Status: StatusCode
    :ivar DiagnosticInfo:
    :vartype DiagnosticInfo: DiagnosticInfo
    '''

    __slots__ = [
        "Status",
        "DiagnosticInfo",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.Status = StatusCode()
        self.DiagnosticInfo = DiagnosticInfo()

    def to_binary(self):
        packet = []
        packet.append(self.Status.to_binary())
        packet.append(self.DiagnosticInfo.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return StatusChangeNotification(data)

    def _binary_init(self, data):
        self.Status = StatusCode.from_binary(data)
        self.DiagnosticInfo = DiagnosticInfo.from_binary(data)

    def __str__(self):
        return 'StatusChangeNotification(' + 'Status:' + str(self.Status) + ', ' + \
             'DiagnosticInfo:' + str(self.DiagnosticInfo) + ')'

    __repr__ = __str__


class SubscriptionAcknowledgement(object):
    '''
    :ivar SubscriptionId:
    :vartype SubscriptionId: UInt32
    :ivar SequenceNumber:
    :vartype SequenceNumber: UInt32
    '''

    __slots__ = [
        "SubscriptionId",
        "SequenceNumber",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.SubscriptionId = 0
        self.SequenceNumber = 0

    def to_binary(self):
        packet = []
        packet.append(uatype_UInt32.pack(self.SubscriptionId))
        packet.append(uatype_UInt32.pack(self.SequenceNumber))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return SubscriptionAcknowledgement(data)

    def _binary_init(self, data):
        self.SubscriptionId = uatype_UInt32.unpack(data.read(4))[0]
        self.SequenceNumber = uatype_UInt32.unpack(data.read(4))[0]

    def __str__(self):
        return 'SubscriptionAcknowledgement(' + 'SubscriptionId:' + str(self.SubscriptionId) + ', ' + \
             'SequenceNumber:' + str(self.SequenceNumber) + ')'

    __repr__ = __str__


class PublishParameters(object):
    '''
    :ivar SubscriptionAcknowledgements:
    :vartype SubscriptionAcknowledgements: SubscriptionAcknowledgement
    '''

    __slots__ = [
        "SubscriptionAcknowledgements",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.SubscriptionAcknowledgements = []

    def to_binary(self):
        packet = []
        packet.append(uatype_Int32.pack(len(self.SubscriptionAcknowledgements)))
        for fieldname in self.SubscriptionAcknowledgements:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return PublishParameters(data)

    def _binary_init(self, data):
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(SubscriptionAcknowledgement.from_binary(data))
        self.SubscriptionAcknowledgements = array

    def __str__(self):
        return 'PublishParameters(' + 'SubscriptionAcknowledgements:' + str(self.SubscriptionAcknowledgements) + ')'

    __repr__ = __str__


class PublishRequest(object):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: PublishParameters
    '''

    __slots__ = [
        "TypeId",
        "RequestHeader",
        "Parameters",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.PublishRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = PublishParameters()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return PublishRequest(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.RequestHeader = RequestHeader.from_binary(data)
        self.Parameters = PublishParameters.from_binary(data)

    def __str__(self):
        return 'PublishRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'RequestHeader:' + str(self.RequestHeader) + ', ' + \
             'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class PublishResult(object):
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

    __slots__ = [
        "SubscriptionId",
        "AvailableSequenceNumbers",
        "MoreNotifications",
        "NotificationMessage",
        "Results",
        "DiagnosticInfos",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.SubscriptionId = 0
        self.AvailableSequenceNumbers = []
        self.MoreNotifications = True
        self.NotificationMessage = NotificationMessage()
        self.Results = []
        self.DiagnosticInfos = []

    def to_binary(self):
        packet = []
        packet.append(uatype_UInt32.pack(self.SubscriptionId))
        packet.append(uatype_Int32.pack(len(self.AvailableSequenceNumbers)))
        for fieldname in self.AvailableSequenceNumbers:
            packet.append(uatype_UInt32.pack(fieldname))
        packet.append(uatype_Boolean.pack(self.MoreNotifications))
        packet.append(self.NotificationMessage.to_binary())
        packet.append(uatype_Int32.pack(len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(uatype_Int32.pack(len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return PublishResult(data)

    def _binary_init(self, data):
        self.SubscriptionId = uatype_UInt32.unpack(data.read(4))[0]
        self.AvailableSequenceNumbers = unpack_uatype_array('UInt32', data)
        self.MoreNotifications = uatype_Boolean.unpack(data.read(1))[0]
        self.NotificationMessage = NotificationMessage.from_binary(data)
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(StatusCode.from_binary(data))
        self.Results = array
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(DiagnosticInfo.from_binary(data))
        self.DiagnosticInfos = array

    def __str__(self):
        return 'PublishResult(' + 'SubscriptionId:' + str(self.SubscriptionId) + ', ' + \
             'AvailableSequenceNumbers:' + str(self.AvailableSequenceNumbers) + ', ' + \
             'MoreNotifications:' + str(self.MoreNotifications) + ', ' + \
             'NotificationMessage:' + str(self.NotificationMessage) + ', ' + \
             'Results:' + str(self.Results) + ', ' + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'

    __repr__ = __str__


class PublishResponse(object):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    :ivar Parameters:
    :vartype Parameters: PublishResult
    '''

    __slots__ = [
        "TypeId",
        "ResponseHeader",
        "Parameters",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.PublishResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = PublishResult()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return PublishResponse(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.ResponseHeader = ResponseHeader.from_binary(data)
        self.Parameters = PublishResult.from_binary(data)

    def __str__(self):
        return 'PublishResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
             'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class RepublishParameters(object):
    '''
    :ivar SubscriptionId:
    :vartype SubscriptionId: UInt32
    :ivar RetransmitSequenceNumber:
    :vartype RetransmitSequenceNumber: UInt32
    '''

    __slots__ = [
        "SubscriptionId",
        "RetransmitSequenceNumber",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.SubscriptionId = 0
        self.RetransmitSequenceNumber = 0

    def to_binary(self):
        packet = []
        packet.append(uatype_UInt32.pack(self.SubscriptionId))
        packet.append(uatype_UInt32.pack(self.RetransmitSequenceNumber))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return RepublishParameters(data)

    def _binary_init(self, data):
        self.SubscriptionId = uatype_UInt32.unpack(data.read(4))[0]
        self.RetransmitSequenceNumber = uatype_UInt32.unpack(data.read(4))[0]

    def __str__(self):
        return 'RepublishParameters(' + 'SubscriptionId:' + str(self.SubscriptionId) + ', ' + \
             'RetransmitSequenceNumber:' + str(self.RetransmitSequenceNumber) + ')'

    __repr__ = __str__


class RepublishRequest(object):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: RepublishParameters
    '''

    __slots__ = [
        "TypeId",
        "RequestHeader",
        "Parameters",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.RepublishRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = RepublishParameters()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return RepublishRequest(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.RequestHeader = RequestHeader.from_binary(data)
        self.Parameters = RepublishParameters.from_binary(data)

    def __str__(self):
        return 'RepublishRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'RequestHeader:' + str(self.RequestHeader) + ', ' + \
             'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class RepublishResponse(object):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    :ivar NotificationMessage:
    :vartype NotificationMessage: NotificationMessage
    '''

    __slots__ = [
        "TypeId",
        "ResponseHeader",
        "NotificationMessage",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.RepublishResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.NotificationMessage = NotificationMessage()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.NotificationMessage.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return RepublishResponse(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.ResponseHeader = ResponseHeader.from_binary(data)
        self.NotificationMessage = NotificationMessage.from_binary(data)

    def __str__(self):
        return 'RepublishResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
             'NotificationMessage:' + str(self.NotificationMessage) + ')'

    __repr__ = __str__


class TransferResult(object):
    '''
    :ivar StatusCode:
    :vartype StatusCode: StatusCode
    :ivar AvailableSequenceNumbers:
    :vartype AvailableSequenceNumbers: UInt32
    '''

    __slots__ = [
        "StatusCode",
        "AvailableSequenceNumbers",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.StatusCode = StatusCode()
        self.AvailableSequenceNumbers = []

    def to_binary(self):
        packet = []
        packet.append(self.StatusCode.to_binary())
        packet.append(uatype_Int32.pack(len(self.AvailableSequenceNumbers)))
        for fieldname in self.AvailableSequenceNumbers:
            packet.append(uatype_UInt32.pack(fieldname))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return TransferResult(data)

    def _binary_init(self, data):
        self.StatusCode = StatusCode.from_binary(data)
        self.AvailableSequenceNumbers = unpack_uatype_array('UInt32', data)

    def __str__(self):
        return 'TransferResult(' + 'StatusCode:' + str(self.StatusCode) + ', ' + \
             'AvailableSequenceNumbers:' + str(self.AvailableSequenceNumbers) + ')'

    __repr__ = __str__


class TransferSubscriptionsParameters(object):
    '''
    :ivar SubscriptionIds:
    :vartype SubscriptionIds: UInt32
    :ivar SendInitialValues:
    :vartype SendInitialValues: Boolean
    '''

    __slots__ = [
        "SubscriptionIds",
        "SendInitialValues",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.SubscriptionIds = []
        self.SendInitialValues = True

    def to_binary(self):
        packet = []
        packet.append(uatype_Int32.pack(len(self.SubscriptionIds)))
        for fieldname in self.SubscriptionIds:
            packet.append(uatype_UInt32.pack(fieldname))
        packet.append(uatype_Boolean.pack(self.SendInitialValues))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return TransferSubscriptionsParameters(data)

    def _binary_init(self, data):
        self.SubscriptionIds = unpack_uatype_array('UInt32', data)
        self.SendInitialValues = uatype_Boolean.unpack(data.read(1))[0]

    def __str__(self):
        return 'TransferSubscriptionsParameters(' + 'SubscriptionIds:' + str(self.SubscriptionIds) + ', ' + \
             'SendInitialValues:' + str(self.SendInitialValues) + ')'

    __repr__ = __str__


class TransferSubscriptionsRequest(object):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: TransferSubscriptionsParameters
    '''

    __slots__ = [
        "TypeId",
        "RequestHeader",
        "Parameters",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.TransferSubscriptionsRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = TransferSubscriptionsParameters()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return TransferSubscriptionsRequest(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.RequestHeader = RequestHeader.from_binary(data)
        self.Parameters = TransferSubscriptionsParameters.from_binary(data)

    def __str__(self):
        return 'TransferSubscriptionsRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'RequestHeader:' + str(self.RequestHeader) + ', ' + \
             'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class TransferSubscriptionsResult(object):
    '''
    :ivar Results:
    :vartype Results: TransferResult
    :ivar DiagnosticInfos:
    :vartype DiagnosticInfos: DiagnosticInfo
    '''

    __slots__ = [
        "Results",
        "DiagnosticInfos",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.Results = []
        self.DiagnosticInfos = []

    def to_binary(self):
        packet = []
        packet.append(uatype_Int32.pack(len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(uatype_Int32.pack(len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return TransferSubscriptionsResult(data)

    def _binary_init(self, data):
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(TransferResult.from_binary(data))
        self.Results = array
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(DiagnosticInfo.from_binary(data))
        self.DiagnosticInfos = array

    def __str__(self):
        return 'TransferSubscriptionsResult(' + 'Results:' + str(self.Results) + ', ' + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'

    __repr__ = __str__


class TransferSubscriptionsResponse(object):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar ResponseHeader:
    :vartype ResponseHeader: ResponseHeader
    :ivar Parameters:
    :vartype Parameters: TransferSubscriptionsResult
    '''

    __slots__ = [
        "TypeId",
        "ResponseHeader",
        "Parameters",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.TransferSubscriptionsResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = TransferSubscriptionsResult()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return TransferSubscriptionsResponse(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.ResponseHeader = ResponseHeader.from_binary(data)
        self.Parameters = TransferSubscriptionsResult.from_binary(data)

    def __str__(self):
        return 'TransferSubscriptionsResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
             'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class DeleteSubscriptionsParameters(object):
    '''
    :ivar SubscriptionIds:
    :vartype SubscriptionIds: UInt32
    '''

    __slots__ = [
        "SubscriptionIds",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.SubscriptionIds = []

    def to_binary(self):
        packet = []
        packet.append(uatype_Int32.pack(len(self.SubscriptionIds)))
        for fieldname in self.SubscriptionIds:
            packet.append(uatype_UInt32.pack(fieldname))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return DeleteSubscriptionsParameters(data)

    def _binary_init(self, data):
        self.SubscriptionIds = unpack_uatype_array('UInt32', data)

    def __str__(self):
        return 'DeleteSubscriptionsParameters(' + 'SubscriptionIds:' + str(self.SubscriptionIds) + ')'

    __repr__ = __str__


class DeleteSubscriptionsRequest(object):
    '''
    :ivar TypeId:
    :vartype TypeId: NodeId
    :ivar RequestHeader:
    :vartype RequestHeader: RequestHeader
    :ivar Parameters:
    :vartype Parameters: DeleteSubscriptionsParameters
    '''

    __slots__ = [
        "TypeId",
        "RequestHeader",
        "Parameters",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.DeleteSubscriptionsRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = DeleteSubscriptionsParameters()

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return DeleteSubscriptionsRequest(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.RequestHeader = RequestHeader.from_binary(data)
        self.Parameters = DeleteSubscriptionsParameters.from_binary(data)

    def __str__(self):
        return 'DeleteSubscriptionsRequest(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'RequestHeader:' + str(self.RequestHeader) + ', ' + \
             'Parameters:' + str(self.Parameters) + ')'

    __repr__ = __str__


class DeleteSubscriptionsResponse(object):
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

    __slots__ = [
        "TypeId",
        "ResponseHeader",
        "Results",
        "DiagnosticInfos",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TypeId = FourByteNodeId(ObjectIds.DeleteSubscriptionsResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Results = []
        self.DiagnosticInfos = []

    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(uatype_Int32.pack(len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(uatype_Int32.pack(len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return DeleteSubscriptionsResponse(data)

    def _binary_init(self, data):
        self.TypeId = NodeId.from_binary(data)
        self.ResponseHeader = ResponseHeader.from_binary(data)
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(StatusCode.from_binary(data))
        self.Results = array
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(DiagnosticInfo.from_binary(data))
        self.DiagnosticInfos = array

    def __str__(self):
        return 'DeleteSubscriptionsResponse(' + 'TypeId:' + str(self.TypeId) + ', ' + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', ' + \
             'Results:' + str(self.Results) + ', ' + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'

    __repr__ = __str__


class BuildInfo(object):
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

    __slots__ = [
        "ProductUri",
        "ManufacturerName",
        "ProductName",
        "SoftwareVersion",
        "BuildNumber",
        "BuildDate",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.ProductUri = ''
        self.ManufacturerName = ''
        self.ProductName = ''
        self.SoftwareVersion = ''
        self.BuildNumber = ''
        self.BuildDate = datetime.now()

    def to_binary(self):
        packet = []
        packet.append(pack_string(self.ProductUri))
        packet.append(pack_string(self.ManufacturerName))
        packet.append(pack_string(self.ProductName))
        packet.append(pack_string(self.SoftwareVersion))
        packet.append(pack_string(self.BuildNumber))
        packet.append(pack_datetime(self.BuildDate))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return BuildInfo(data)

    def _binary_init(self, data):
        self.ProductUri = unpack_string(data)
        self.ManufacturerName = unpack_string(data)
        self.ProductName = unpack_string(data)
        self.SoftwareVersion = unpack_string(data)
        self.BuildNumber = unpack_string(data)
        self.BuildDate = unpack_datetime(data)

    def __str__(self):
        return 'BuildInfo(' + 'ProductUri:' + str(self.ProductUri) + ', ' + \
             'ManufacturerName:' + str(self.ManufacturerName) + ', ' + \
             'ProductName:' + str(self.ProductName) + ', ' + \
             'SoftwareVersion:' + str(self.SoftwareVersion) + ', ' + \
             'BuildNumber:' + str(self.BuildNumber) + ', ' + \
             'BuildDate:' + str(self.BuildDate) + ')'

    __repr__ = __str__


class RedundantServerDataType(object):
    '''
    :ivar ServerId:
    :vartype ServerId: String
    :ivar ServiceLevel:
    :vartype ServiceLevel: Byte
    :ivar ServerState:
    :vartype ServerState: ServerState
    '''

    __slots__ = [
        "ServerId",
        "ServiceLevel",
        "ServerState",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.ServerId = ''
        self.ServiceLevel = 0
        self.ServerState = 0

    def to_binary(self):
        packet = []
        packet.append(pack_string(self.ServerId))
        packet.append(uatype_Byte.pack(self.ServiceLevel))
        packet.append(uatype_UInt32.pack(self.ServerState))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return RedundantServerDataType(data)

    def _binary_init(self, data):
        self.ServerId = unpack_string(data)
        self.ServiceLevel = uatype_Byte.unpack(data.read(1))[0]
        self.ServerState = uatype_UInt32.unpack(data.read(4))[0]

    def __str__(self):
        return 'RedundantServerDataType(' + 'ServerId:' + str(self.ServerId) + ', ' + \
             'ServiceLevel:' + str(self.ServiceLevel) + ', ' + \
             'ServerState:' + str(self.ServerState) + ')'

    __repr__ = __str__


class EndpointUrlListDataType(object):
    '''
    :ivar EndpointUrlList:
    :vartype EndpointUrlList: String
    '''

    __slots__ = [
        "EndpointUrlList",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.EndpointUrlList = []

    def to_binary(self):
        packet = []
        packet.append(uatype_Int32.pack(len(self.EndpointUrlList)))
        for fieldname in self.EndpointUrlList:
            packet.append(pack_string(fieldname))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return EndpointUrlListDataType(data)

    def _binary_init(self, data):
        self.EndpointUrlList = unpack_uatype_array('String', data)

    def __str__(self):
        return 'EndpointUrlListDataType(' + 'EndpointUrlList:' + str(self.EndpointUrlList) + ')'

    __repr__ = __str__


class NetworkGroupDataType(object):
    '''
    :ivar ServerUri:
    :vartype ServerUri: String
    :ivar NetworkPaths:
    :vartype NetworkPaths: EndpointUrlListDataType
    '''

    __slots__ = [
        "ServerUri",
        "NetworkPaths",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.ServerUri = ''
        self.NetworkPaths = []

    def to_binary(self):
        packet = []
        packet.append(pack_string(self.ServerUri))
        packet.append(uatype_Int32.pack(len(self.NetworkPaths)))
        for fieldname in self.NetworkPaths:
            packet.append(fieldname.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return NetworkGroupDataType(data)

    def _binary_init(self, data):
        self.ServerUri = unpack_string(data)
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(EndpointUrlListDataType.from_binary(data))
        self.NetworkPaths = array

    def __str__(self):
        return 'NetworkGroupDataType(' + 'ServerUri:' + str(self.ServerUri) + ', ' + \
             'NetworkPaths:' + str(self.NetworkPaths) + ')'

    __repr__ = __str__


class SamplingIntervalDiagnosticsDataType(object):
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

    __slots__ = [
        "SamplingInterval",
        "MonitoredItemCount",
        "MaxMonitoredItemCount",
        "DisabledMonitoredItemCount",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.SamplingInterval = 0
        self.MonitoredItemCount = 0
        self.MaxMonitoredItemCount = 0
        self.DisabledMonitoredItemCount = 0

    def to_binary(self):
        packet = []
        packet.append(uatype_Double.pack(self.SamplingInterval))
        packet.append(uatype_UInt32.pack(self.MonitoredItemCount))
        packet.append(uatype_UInt32.pack(self.MaxMonitoredItemCount))
        packet.append(uatype_UInt32.pack(self.DisabledMonitoredItemCount))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return SamplingIntervalDiagnosticsDataType(data)

    def _binary_init(self, data):
        self.SamplingInterval = uatype_Double.unpack(data.read(8))[0]
        self.MonitoredItemCount = uatype_UInt32.unpack(data.read(4))[0]
        self.MaxMonitoredItemCount = uatype_UInt32.unpack(data.read(4))[0]
        self.DisabledMonitoredItemCount = uatype_UInt32.unpack(data.read(4))[0]

    def __str__(self):
        return 'SamplingIntervalDiagnosticsDataType(' + 'SamplingInterval:' + str(self.SamplingInterval) + ', ' + \
             'MonitoredItemCount:' + str(self.MonitoredItemCount) + ', ' + \
             'MaxMonitoredItemCount:' + str(self.MaxMonitoredItemCount) + ', ' + \
             'DisabledMonitoredItemCount:' + str(self.DisabledMonitoredItemCount) + ')'

    __repr__ = __str__


class ServerDiagnosticsSummaryDataType(object):
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

    __slots__ = [
        "ServerViewCount",
        "CurrentSessionCount",
        "CumulatedSessionCount",
        "SecurityRejectedSessionCount",
        "RejectedSessionCount",
        "SessionTimeoutCount",
        "SessionAbortCount",
        "CurrentSubscriptionCount",
        "CumulatedSubscriptionCount",
        "PublishingIntervalCount",
        "SecurityRejectedRequestsCount",
        "RejectedRequestsCount",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
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

    def to_binary(self):
        packet = []
        packet.append(uatype_UInt32.pack(self.ServerViewCount))
        packet.append(uatype_UInt32.pack(self.CurrentSessionCount))
        packet.append(uatype_UInt32.pack(self.CumulatedSessionCount))
        packet.append(uatype_UInt32.pack(self.SecurityRejectedSessionCount))
        packet.append(uatype_UInt32.pack(self.RejectedSessionCount))
        packet.append(uatype_UInt32.pack(self.SessionTimeoutCount))
        packet.append(uatype_UInt32.pack(self.SessionAbortCount))
        packet.append(uatype_UInt32.pack(self.CurrentSubscriptionCount))
        packet.append(uatype_UInt32.pack(self.CumulatedSubscriptionCount))
        packet.append(uatype_UInt32.pack(self.PublishingIntervalCount))
        packet.append(uatype_UInt32.pack(self.SecurityRejectedRequestsCount))
        packet.append(uatype_UInt32.pack(self.RejectedRequestsCount))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return ServerDiagnosticsSummaryDataType(data)

    def _binary_init(self, data):
        self.ServerViewCount = uatype_UInt32.unpack(data.read(4))[0]
        self.CurrentSessionCount = uatype_UInt32.unpack(data.read(4))[0]
        self.CumulatedSessionCount = uatype_UInt32.unpack(data.read(4))[0]
        self.SecurityRejectedSessionCount = uatype_UInt32.unpack(data.read(4))[0]
        self.RejectedSessionCount = uatype_UInt32.unpack(data.read(4))[0]
        self.SessionTimeoutCount = uatype_UInt32.unpack(data.read(4))[0]
        self.SessionAbortCount = uatype_UInt32.unpack(data.read(4))[0]
        self.CurrentSubscriptionCount = uatype_UInt32.unpack(data.read(4))[0]
        self.CumulatedSubscriptionCount = uatype_UInt32.unpack(data.read(4))[0]
        self.PublishingIntervalCount = uatype_UInt32.unpack(data.read(4))[0]
        self.SecurityRejectedRequestsCount = uatype_UInt32.unpack(data.read(4))[0]
        self.RejectedRequestsCount = uatype_UInt32.unpack(data.read(4))[0]

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


class ServerStatusDataType(object):
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

    __slots__ = [
        "StartTime",
        "CurrentTime",
        "State",
        "BuildInfo",
        "SecondsTillShutdown",
        "ShutdownReason",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.StartTime = datetime.now()
        self.CurrentTime = datetime.now()
        self.State = 0
        self.BuildInfo = BuildInfo()
        self.SecondsTillShutdown = 0
        self.ShutdownReason = LocalizedText()

    def to_binary(self):
        packet = []
        packet.append(pack_datetime(self.StartTime))
        packet.append(pack_datetime(self.CurrentTime))
        packet.append(uatype_UInt32.pack(self.State))
        packet.append(self.BuildInfo.to_binary())
        packet.append(uatype_UInt32.pack(self.SecondsTillShutdown))
        packet.append(self.ShutdownReason.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return ServerStatusDataType(data)

    def _binary_init(self, data):
        self.StartTime = unpack_datetime(data)
        self.CurrentTime = unpack_datetime(data)
        self.State = uatype_UInt32.unpack(data.read(4))[0]
        self.BuildInfo = BuildInfo.from_binary(data)
        self.SecondsTillShutdown = uatype_UInt32.unpack(data.read(4))[0]
        self.ShutdownReason = LocalizedText.from_binary(data)

    def __str__(self):
        return 'ServerStatusDataType(' + 'StartTime:' + str(self.StartTime) + ', ' + \
             'CurrentTime:' + str(self.CurrentTime) + ', ' + \
             'State:' + str(self.State) + ', ' + \
             'BuildInfo:' + str(self.BuildInfo) + ', ' + \
             'SecondsTillShutdown:' + str(self.SecondsTillShutdown) + ', ' + \
             'ShutdownReason:' + str(self.ShutdownReason) + ')'

    __repr__ = __str__


class SessionDiagnosticsDataType(object):
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

    __slots__ = [
        "SessionId",
        "SessionName",
        "ClientDescription",
        "ServerUri",
        "EndpointUrl",
        "LocaleIds",
        "ActualSessionTimeout",
        "MaxResponseMessageSize",
        "ClientConnectionTime",
        "ClientLastContactTime",
        "CurrentSubscriptionsCount",
        "CurrentMonitoredItemsCount",
        "CurrentPublishRequestsInQueue",
        "TotalRequestCount",
        "UnauthorizedRequestCount",
        "ReadCount",
        "HistoryReadCount",
        "WriteCount",
        "HistoryUpdateCount",
        "CallCount",
        "CreateMonitoredItemsCount",
        "ModifyMonitoredItemsCount",
        "SetMonitoringModeCount",
        "SetTriggeringCount",
        "DeleteMonitoredItemsCount",
        "CreateSubscriptionCount",
        "ModifySubscriptionCount",
        "SetPublishingModeCount",
        "PublishCount",
        "RepublishCount",
        "TransferSubscriptionsCount",
        "DeleteSubscriptionsCount",
        "AddNodesCount",
        "AddReferencesCount",
        "DeleteNodesCount",
        "DeleteReferencesCount",
        "BrowseCount",
        "BrowseNextCount",
        "TranslateBrowsePathsToNodeIdsCount",
        "QueryFirstCount",
        "QueryNextCount",
        "RegisterNodesCount",
        "UnregisterNodesCount",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
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

    def to_binary(self):
        packet = []
        packet.append(self.SessionId.to_binary())
        packet.append(pack_string(self.SessionName))
        packet.append(self.ClientDescription.to_binary())
        packet.append(pack_string(self.ServerUri))
        packet.append(pack_string(self.EndpointUrl))
        packet.append(uatype_Int32.pack(len(self.LocaleIds)))
        for fieldname in self.LocaleIds:
            packet.append(pack_string(fieldname))
        packet.append(uatype_Double.pack(self.ActualSessionTimeout))
        packet.append(uatype_UInt32.pack(self.MaxResponseMessageSize))
        packet.append(pack_datetime(self.ClientConnectionTime))
        packet.append(pack_datetime(self.ClientLastContactTime))
        packet.append(uatype_UInt32.pack(self.CurrentSubscriptionsCount))
        packet.append(uatype_UInt32.pack(self.CurrentMonitoredItemsCount))
        packet.append(uatype_UInt32.pack(self.CurrentPublishRequestsInQueue))
        packet.append(self.TotalRequestCount.to_binary())
        packet.append(uatype_UInt32.pack(self.UnauthorizedRequestCount))
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
        return SessionDiagnosticsDataType(data)

    def _binary_init(self, data):
        self.SessionId = NodeId.from_binary(data)
        self.SessionName = unpack_string(data)
        self.ClientDescription = ApplicationDescription.from_binary(data)
        self.ServerUri = unpack_string(data)
        self.EndpointUrl = unpack_string(data)
        self.LocaleIds = unpack_uatype_array('String', data)
        self.ActualSessionTimeout = uatype_Double.unpack(data.read(8))[0]
        self.MaxResponseMessageSize = uatype_UInt32.unpack(data.read(4))[0]
        self.ClientConnectionTime = unpack_datetime(data)
        self.ClientLastContactTime = unpack_datetime(data)
        self.CurrentSubscriptionsCount = uatype_UInt32.unpack(data.read(4))[0]
        self.CurrentMonitoredItemsCount = uatype_UInt32.unpack(data.read(4))[0]
        self.CurrentPublishRequestsInQueue = uatype_UInt32.unpack(data.read(4))[0]
        self.TotalRequestCount = ServiceCounterDataType.from_binary(data)
        self.UnauthorizedRequestCount = uatype_UInt32.unpack(data.read(4))[0]
        self.ReadCount = ServiceCounterDataType.from_binary(data)
        self.HistoryReadCount = ServiceCounterDataType.from_binary(data)
        self.WriteCount = ServiceCounterDataType.from_binary(data)
        self.HistoryUpdateCount = ServiceCounterDataType.from_binary(data)
        self.CallCount = ServiceCounterDataType.from_binary(data)
        self.CreateMonitoredItemsCount = ServiceCounterDataType.from_binary(data)
        self.ModifyMonitoredItemsCount = ServiceCounterDataType.from_binary(data)
        self.SetMonitoringModeCount = ServiceCounterDataType.from_binary(data)
        self.SetTriggeringCount = ServiceCounterDataType.from_binary(data)
        self.DeleteMonitoredItemsCount = ServiceCounterDataType.from_binary(data)
        self.CreateSubscriptionCount = ServiceCounterDataType.from_binary(data)
        self.ModifySubscriptionCount = ServiceCounterDataType.from_binary(data)
        self.SetPublishingModeCount = ServiceCounterDataType.from_binary(data)
        self.PublishCount = ServiceCounterDataType.from_binary(data)
        self.RepublishCount = ServiceCounterDataType.from_binary(data)
        self.TransferSubscriptionsCount = ServiceCounterDataType.from_binary(data)
        self.DeleteSubscriptionsCount = ServiceCounterDataType.from_binary(data)
        self.AddNodesCount = ServiceCounterDataType.from_binary(data)
        self.AddReferencesCount = ServiceCounterDataType.from_binary(data)
        self.DeleteNodesCount = ServiceCounterDataType.from_binary(data)
        self.DeleteReferencesCount = ServiceCounterDataType.from_binary(data)
        self.BrowseCount = ServiceCounterDataType.from_binary(data)
        self.BrowseNextCount = ServiceCounterDataType.from_binary(data)
        self.TranslateBrowsePathsToNodeIdsCount = ServiceCounterDataType.from_binary(data)
        self.QueryFirstCount = ServiceCounterDataType.from_binary(data)
        self.QueryNextCount = ServiceCounterDataType.from_binary(data)
        self.RegisterNodesCount = ServiceCounterDataType.from_binary(data)
        self.UnregisterNodesCount = ServiceCounterDataType.from_binary(data)

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


class SessionSecurityDiagnosticsDataType(object):
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

    __slots__ = [
        "SessionId",
        "ClientUserIdOfSession",
        "ClientUserIdHistory",
        "AuthenticationMechanism",
        "Encoding",
        "TransportProtocol",
        "SecurityMode",
        "SecurityPolicyUri",
        "ClientCertificate",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.SessionId = NodeId()
        self.ClientUserIdOfSession = ''
        self.ClientUserIdHistory = []
        self.AuthenticationMechanism = ''
        self.Encoding = ''
        self.TransportProtocol = ''
        self.SecurityMode = 0
        self.SecurityPolicyUri = ''
        self.ClientCertificate = b''

    def to_binary(self):
        packet = []
        packet.append(self.SessionId.to_binary())
        packet.append(pack_string(self.ClientUserIdOfSession))
        packet.append(uatype_Int32.pack(len(self.ClientUserIdHistory)))
        for fieldname in self.ClientUserIdHistory:
            packet.append(pack_string(fieldname))
        packet.append(pack_string(self.AuthenticationMechanism))
        packet.append(pack_string(self.Encoding))
        packet.append(pack_string(self.TransportProtocol))
        packet.append(uatype_UInt32.pack(self.SecurityMode))
        packet.append(pack_string(self.SecurityPolicyUri))
        packet.append(pack_bytes(self.ClientCertificate))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return SessionSecurityDiagnosticsDataType(data)

    def _binary_init(self, data):
        self.SessionId = NodeId.from_binary(data)
        self.ClientUserIdOfSession = unpack_string(data)
        self.ClientUserIdHistory = unpack_uatype_array('String', data)
        self.AuthenticationMechanism = unpack_string(data)
        self.Encoding = unpack_string(data)
        self.TransportProtocol = unpack_string(data)
        self.SecurityMode = uatype_UInt32.unpack(data.read(4))[0]
        self.SecurityPolicyUri = unpack_string(data)
        self.ClientCertificate = unpack_bytes(data)

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


class ServiceCounterDataType(object):
    '''
    :ivar TotalCount:
    :vartype TotalCount: UInt32
    :ivar ErrorCount:
    :vartype ErrorCount: UInt32
    '''

    __slots__ = [
        "TotalCount",
        "ErrorCount",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.TotalCount = 0
        self.ErrorCount = 0

    def to_binary(self):
        packet = []
        packet.append(uatype_UInt32.pack(self.TotalCount))
        packet.append(uatype_UInt32.pack(self.ErrorCount))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return ServiceCounterDataType(data)

    def _binary_init(self, data):
        self.TotalCount = uatype_UInt32.unpack(data.read(4))[0]
        self.ErrorCount = uatype_UInt32.unpack(data.read(4))[0]

    def __str__(self):
        return 'ServiceCounterDataType(' + 'TotalCount:' + str(self.TotalCount) + ', ' + \
             'ErrorCount:' + str(self.ErrorCount) + ')'

    __repr__ = __str__


class StatusResult(object):
    '''
    :ivar StatusCode:
    :vartype StatusCode: StatusCode
    :ivar DiagnosticInfo:
    :vartype DiagnosticInfo: DiagnosticInfo
    '''

    __slots__ = [
        "StatusCode",
        "DiagnosticInfo",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.StatusCode = StatusCode()
        self.DiagnosticInfo = DiagnosticInfo()

    def to_binary(self):
        packet = []
        packet.append(self.StatusCode.to_binary())
        packet.append(self.DiagnosticInfo.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return StatusResult(data)

    def _binary_init(self, data):
        self.StatusCode = StatusCode.from_binary(data)
        self.DiagnosticInfo = DiagnosticInfo.from_binary(data)

    def __str__(self):
        return 'StatusResult(' + 'StatusCode:' + str(self.StatusCode) + ', ' + \
             'DiagnosticInfo:' + str(self.DiagnosticInfo) + ')'

    __repr__ = __str__


class SubscriptionDiagnosticsDataType(object):
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

    __slots__ = [
        "SessionId",
        "SubscriptionId",
        "Priority",
        "PublishingInterval",
        "MaxKeepAliveCount",
        "MaxLifetimeCount",
        "MaxNotificationsPerPublish",
        "PublishingEnabled",
        "ModifyCount",
        "EnableCount",
        "DisableCount",
        "RepublishRequestCount",
        "RepublishMessageRequestCount",
        "RepublishMessageCount",
        "TransferRequestCount",
        "TransferredToAltClientCount",
        "TransferredToSameClientCount",
        "PublishRequestCount",
        "DataChangeNotificationsCount",
        "EventNotificationsCount",
        "NotificationsCount",
        "LatePublishRequestCount",
        "CurrentKeepAliveCount",
        "CurrentLifetimeCount",
        "UnacknowledgedMessageCount",
        "DiscardedMessageCount",
        "MonitoredItemCount",
        "DisabledMonitoredItemCount",
        "MonitoringQueueOverflowCount",
        "NextSequenceNumber",
        "EventQueueOverFlowCount",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
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

    def to_binary(self):
        packet = []
        packet.append(self.SessionId.to_binary())
        packet.append(uatype_UInt32.pack(self.SubscriptionId))
        packet.append(uatype_Byte.pack(self.Priority))
        packet.append(uatype_Double.pack(self.PublishingInterval))
        packet.append(uatype_UInt32.pack(self.MaxKeepAliveCount))
        packet.append(uatype_UInt32.pack(self.MaxLifetimeCount))
        packet.append(uatype_UInt32.pack(self.MaxNotificationsPerPublish))
        packet.append(uatype_Boolean.pack(self.PublishingEnabled))
        packet.append(uatype_UInt32.pack(self.ModifyCount))
        packet.append(uatype_UInt32.pack(self.EnableCount))
        packet.append(uatype_UInt32.pack(self.DisableCount))
        packet.append(uatype_UInt32.pack(self.RepublishRequestCount))
        packet.append(uatype_UInt32.pack(self.RepublishMessageRequestCount))
        packet.append(uatype_UInt32.pack(self.RepublishMessageCount))
        packet.append(uatype_UInt32.pack(self.TransferRequestCount))
        packet.append(uatype_UInt32.pack(self.TransferredToAltClientCount))
        packet.append(uatype_UInt32.pack(self.TransferredToSameClientCount))
        packet.append(uatype_UInt32.pack(self.PublishRequestCount))
        packet.append(uatype_UInt32.pack(self.DataChangeNotificationsCount))
        packet.append(uatype_UInt32.pack(self.EventNotificationsCount))
        packet.append(uatype_UInt32.pack(self.NotificationsCount))
        packet.append(uatype_UInt32.pack(self.LatePublishRequestCount))
        packet.append(uatype_UInt32.pack(self.CurrentKeepAliveCount))
        packet.append(uatype_UInt32.pack(self.CurrentLifetimeCount))
        packet.append(uatype_UInt32.pack(self.UnacknowledgedMessageCount))
        packet.append(uatype_UInt32.pack(self.DiscardedMessageCount))
        packet.append(uatype_UInt32.pack(self.MonitoredItemCount))
        packet.append(uatype_UInt32.pack(self.DisabledMonitoredItemCount))
        packet.append(uatype_UInt32.pack(self.MonitoringQueueOverflowCount))
        packet.append(uatype_UInt32.pack(self.NextSequenceNumber))
        packet.append(uatype_UInt32.pack(self.EventQueueOverFlowCount))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return SubscriptionDiagnosticsDataType(data)

    def _binary_init(self, data):
        self.SessionId = NodeId.from_binary(data)
        self.SubscriptionId = uatype_UInt32.unpack(data.read(4))[0]
        self.Priority = uatype_Byte.unpack(data.read(1))[0]
        self.PublishingInterval = uatype_Double.unpack(data.read(8))[0]
        self.MaxKeepAliveCount = uatype_UInt32.unpack(data.read(4))[0]
        self.MaxLifetimeCount = uatype_UInt32.unpack(data.read(4))[0]
        self.MaxNotificationsPerPublish = uatype_UInt32.unpack(data.read(4))[0]
        self.PublishingEnabled = uatype_Boolean.unpack(data.read(1))[0]
        self.ModifyCount = uatype_UInt32.unpack(data.read(4))[0]
        self.EnableCount = uatype_UInt32.unpack(data.read(4))[0]
        self.DisableCount = uatype_UInt32.unpack(data.read(4))[0]
        self.RepublishRequestCount = uatype_UInt32.unpack(data.read(4))[0]
        self.RepublishMessageRequestCount = uatype_UInt32.unpack(data.read(4))[0]
        self.RepublishMessageCount = uatype_UInt32.unpack(data.read(4))[0]
        self.TransferRequestCount = uatype_UInt32.unpack(data.read(4))[0]
        self.TransferredToAltClientCount = uatype_UInt32.unpack(data.read(4))[0]
        self.TransferredToSameClientCount = uatype_UInt32.unpack(data.read(4))[0]
        self.PublishRequestCount = uatype_UInt32.unpack(data.read(4))[0]
        self.DataChangeNotificationsCount = uatype_UInt32.unpack(data.read(4))[0]
        self.EventNotificationsCount = uatype_UInt32.unpack(data.read(4))[0]
        self.NotificationsCount = uatype_UInt32.unpack(data.read(4))[0]
        self.LatePublishRequestCount = uatype_UInt32.unpack(data.read(4))[0]
        self.CurrentKeepAliveCount = uatype_UInt32.unpack(data.read(4))[0]
        self.CurrentLifetimeCount = uatype_UInt32.unpack(data.read(4))[0]
        self.UnacknowledgedMessageCount = uatype_UInt32.unpack(data.read(4))[0]
        self.DiscardedMessageCount = uatype_UInt32.unpack(data.read(4))[0]
        self.MonitoredItemCount = uatype_UInt32.unpack(data.read(4))[0]
        self.DisabledMonitoredItemCount = uatype_UInt32.unpack(data.read(4))[0]
        self.MonitoringQueueOverflowCount = uatype_UInt32.unpack(data.read(4))[0]
        self.NextSequenceNumber = uatype_UInt32.unpack(data.read(4))[0]
        self.EventQueueOverFlowCount = uatype_UInt32.unpack(data.read(4))[0]

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


class ModelChangeStructureDataType(object):
    '''
    :ivar Affected:
    :vartype Affected: NodeId
    :ivar AffectedType:
    :vartype AffectedType: NodeId
    :ivar Verb:
    :vartype Verb: Byte
    '''

    __slots__ = [
        "Affected",
        "AffectedType",
        "Verb",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.Affected = NodeId()
        self.AffectedType = NodeId()
        self.Verb = 0

    def to_binary(self):
        packet = []
        packet.append(self.Affected.to_binary())
        packet.append(self.AffectedType.to_binary())
        packet.append(uatype_Byte.pack(self.Verb))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return ModelChangeStructureDataType(data)

    def _binary_init(self, data):
        self.Affected = NodeId.from_binary(data)
        self.AffectedType = NodeId.from_binary(data)
        self.Verb = uatype_Byte.unpack(data.read(1))[0]

    def __str__(self):
        return 'ModelChangeStructureDataType(' + 'Affected:' + str(self.Affected) + ', ' + \
             'AffectedType:' + str(self.AffectedType) + ', ' + \
             'Verb:' + str(self.Verb) + ')'

    __repr__ = __str__


class SemanticChangeStructureDataType(object):
    '''
    :ivar Affected:
    :vartype Affected: NodeId
    :ivar AffectedType:
    :vartype AffectedType: NodeId
    '''

    __slots__ = [
        "Affected",
        "AffectedType",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.Affected = NodeId()
        self.AffectedType = NodeId()

    def to_binary(self):
        packet = []
        packet.append(self.Affected.to_binary())
        packet.append(self.AffectedType.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return SemanticChangeStructureDataType(data)

    def _binary_init(self, data):
        self.Affected = NodeId.from_binary(data)
        self.AffectedType = NodeId.from_binary(data)

    def __str__(self):
        return 'SemanticChangeStructureDataType(' + 'Affected:' + str(self.Affected) + ', ' + \
             'AffectedType:' + str(self.AffectedType) + ')'

    __repr__ = __str__


class Range(object):
    '''
    :ivar Low:
    :vartype Low: Double
    :ivar High:
    :vartype High: Double
    '''

    __slots__ = [
        "Low",
        "High",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.Low = 0
        self.High = 0

    def to_binary(self):
        packet = []
        packet.append(uatype_Double.pack(self.Low))
        packet.append(uatype_Double.pack(self.High))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return Range(data)

    def _binary_init(self, data):
        self.Low = uatype_Double.unpack(data.read(8))[0]
        self.High = uatype_Double.unpack(data.read(8))[0]

    def __str__(self):
        return 'Range(' + 'Low:' + str(self.Low) + ', ' + \
             'High:' + str(self.High) + ')'

    __repr__ = __str__


class EUInformation(object):
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

    __slots__ = [
        "NamespaceUri",
        "UnitId",
        "DisplayName",
        "Description",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.NamespaceUri = ''
        self.UnitId = 0
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()

    def to_binary(self):
        packet = []
        packet.append(pack_string(self.NamespaceUri))
        packet.append(uatype_Int32.pack(self.UnitId))
        packet.append(self.DisplayName.to_binary())
        packet.append(self.Description.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return EUInformation(data)

    def _binary_init(self, data):
        self.NamespaceUri = unpack_string(data)
        self.UnitId = uatype_Int32.unpack(data.read(4))[0]
        self.DisplayName = LocalizedText.from_binary(data)
        self.Description = LocalizedText.from_binary(data)

    def __str__(self):
        return 'EUInformation(' + 'NamespaceUri:' + str(self.NamespaceUri) + ', ' + \
             'UnitId:' + str(self.UnitId) + ', ' + \
             'DisplayName:' + str(self.DisplayName) + ', ' + \
             'Description:' + str(self.Description) + ')'

    __repr__ = __str__


class ComplexNumberType(object):
    '''
    :ivar Real:
    :vartype Real: Float
    :ivar Imaginary:
    :vartype Imaginary: Float
    '''

    __slots__ = [
        "Real",
        "Imaginary",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.Real = 0
        self.Imaginary = 0

    def to_binary(self):
        packet = []
        packet.append(uatype_Float.pack(self.Real))
        packet.append(uatype_Float.pack(self.Imaginary))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return ComplexNumberType(data)

    def _binary_init(self, data):
        self.Real = uatype_Float.unpack(data.read(4))[0]
        self.Imaginary = uatype_Float.unpack(data.read(4))[0]

    def __str__(self):
        return 'ComplexNumberType(' + 'Real:' + str(self.Real) + ', ' + \
             'Imaginary:' + str(self.Imaginary) + ')'

    __repr__ = __str__


class DoubleComplexNumberType(object):
    '''
    :ivar Real:
    :vartype Real: Double
    :ivar Imaginary:
    :vartype Imaginary: Double
    '''

    __slots__ = [
        "Real",
        "Imaginary",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.Real = 0
        self.Imaginary = 0

    def to_binary(self):
        packet = []
        packet.append(uatype_Double.pack(self.Real))
        packet.append(uatype_Double.pack(self.Imaginary))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return DoubleComplexNumberType(data)

    def _binary_init(self, data):
        self.Real = uatype_Double.unpack(data.read(8))[0]
        self.Imaginary = uatype_Double.unpack(data.read(8))[0]

    def __str__(self):
        return 'DoubleComplexNumberType(' + 'Real:' + str(self.Real) + ', ' + \
             'Imaginary:' + str(self.Imaginary) + ')'

    __repr__ = __str__


class AxisInformation(object):
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

    __slots__ = [
        "EngineeringUnits",
        "EURange",
        "Title",
        "AxisScaleType",
        "AxisSteps",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.EngineeringUnits = EUInformation()
        self.EURange = Range()
        self.Title = LocalizedText()
        self.AxisScaleType = 0
        self.AxisSteps = []

    def to_binary(self):
        packet = []
        packet.append(self.EngineeringUnits.to_binary())
        packet.append(self.EURange.to_binary())
        packet.append(self.Title.to_binary())
        packet.append(uatype_UInt32.pack(self.AxisScaleType))
        packet.append(uatype_Int32.pack(len(self.AxisSteps)))
        for fieldname in self.AxisSteps:
            packet.append(uatype_Double.pack(fieldname))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return AxisInformation(data)

    def _binary_init(self, data):
        self.EngineeringUnits = EUInformation.from_binary(data)
        self.EURange = Range.from_binary(data)
        self.Title = LocalizedText.from_binary(data)
        self.AxisScaleType = uatype_UInt32.unpack(data.read(4))[0]
        self.AxisSteps = unpack_uatype_array('Double', data)

    def __str__(self):
        return 'AxisInformation(' + 'EngineeringUnits:' + str(self.EngineeringUnits) + ', ' + \
             'EURange:' + str(self.EURange) + ', ' + \
             'Title:' + str(self.Title) + ', ' + \
             'AxisScaleType:' + str(self.AxisScaleType) + ', ' + \
             'AxisSteps:' + str(self.AxisSteps) + ')'

    __repr__ = __str__


class XVType(object):
    '''
    :ivar X:
    :vartype X: Double
    :ivar Value:
    :vartype Value: Float
    '''

    __slots__ = [
        "X",
        "Value",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.X = 0
        self.Value = 0

    def to_binary(self):
        packet = []
        packet.append(uatype_Double.pack(self.X))
        packet.append(uatype_Float.pack(self.Value))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return XVType(data)

    def _binary_init(self, data):
        self.X = uatype_Double.unpack(data.read(8))[0]
        self.Value = uatype_Float.unpack(data.read(4))[0]

    def __str__(self):
        return 'XVType(' + 'X:' + str(self.X) + ', ' + \
             'Value:' + str(self.Value) + ')'

    __repr__ = __str__


class ProgramDiagnosticDataType(object):
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

    __slots__ = [
        "CreateSessionId",
        "CreateClientName",
        "InvocationCreationTime",
        "LastTransitionTime",
        "LastMethodCall",
        "LastMethodSessionId",
        "LastMethodInputArguments",
        "LastMethodOutputArguments",
        "LastMethodCallTime",
        "LastMethodReturnStatus",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
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

    def to_binary(self):
        packet = []
        packet.append(self.CreateSessionId.to_binary())
        packet.append(pack_string(self.CreateClientName))
        packet.append(pack_datetime(self.InvocationCreationTime))
        packet.append(pack_datetime(self.LastTransitionTime))
        packet.append(pack_string(self.LastMethodCall))
        packet.append(self.LastMethodSessionId.to_binary())
        packet.append(uatype_Int32.pack(len(self.LastMethodInputArguments)))
        for fieldname in self.LastMethodInputArguments:
            packet.append(fieldname.to_binary())
        packet.append(uatype_Int32.pack(len(self.LastMethodOutputArguments)))
        for fieldname in self.LastMethodOutputArguments:
            packet.append(fieldname.to_binary())
        packet.append(pack_datetime(self.LastMethodCallTime))
        packet.append(self.LastMethodReturnStatus.to_binary())
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return ProgramDiagnosticDataType(data)

    def _binary_init(self, data):
        self.CreateSessionId = NodeId.from_binary(data)
        self.CreateClientName = unpack_string(data)
        self.InvocationCreationTime = unpack_datetime(data)
        self.LastTransitionTime = unpack_datetime(data)
        self.LastMethodCall = unpack_string(data)
        self.LastMethodSessionId = NodeId.from_binary(data)
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(Argument.from_binary(data))
        self.LastMethodInputArguments = array
        length = uatype_Int32.unpack(data.read(4))[0]
        array = []
        if length != -1:
            for _ in range(0, length):
                array.append(Argument.from_binary(data))
        self.LastMethodOutputArguments = array
        self.LastMethodCallTime = unpack_datetime(data)
        self.LastMethodReturnStatus = StatusResult.from_binary(data)

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


class Annotation(object):
    '''
    :ivar Message:
    :vartype Message: String
    :ivar UserName:
    :vartype UserName: String
    :ivar AnnotationTime:
    :vartype AnnotationTime: DateTime
    '''

    __slots__ = [
        "Message",
        "UserName",
        "AnnotationTime",
    ]

    def __init__(self, binary=None):
        if binary is not None:
            self._binary_init(binary)
            return
        self.Message = ''
        self.UserName = ''
        self.AnnotationTime = datetime.now()

    def to_binary(self):
        packet = []
        packet.append(pack_string(self.Message))
        packet.append(pack_string(self.UserName))
        packet.append(pack_datetime(self.AnnotationTime))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        return Annotation(data)

    def _binary_init(self, data):
        self.Message = unpack_string(data)
        self.UserName = unpack_string(data)
        self.AnnotationTime = unpack_datetime(data)

    def __str__(self):
        return 'Annotation(' + 'Message:' + str(self.Message) + ', ' + \
             'UserName:' + str(self.UserName) + ', ' + \
             'AnnotationTime:' + str(self.AnnotationTime) + ')'

    __repr__ = __str__

ExtensionClasses = {
    ObjectIds.TrustListDataType_Encoding_DefaultBinary : TrustListDataType,
    ObjectIds.Argument_Encoding_DefaultBinary : Argument,
    ObjectIds.EnumValueType_Encoding_DefaultBinary : EnumValueType,
    ObjectIds.OptionSet_Encoding_DefaultBinary : OptionSet,
    ObjectIds.Union_Encoding_DefaultBinary : Union,
    ObjectIds.TimeZoneDataType_Encoding_DefaultBinary : TimeZoneDataType,
    ObjectIds.ApplicationDescription_Encoding_DefaultBinary : ApplicationDescription,
    ObjectIds.RequestHeader_Encoding_DefaultBinary : RequestHeader,
    ObjectIds.ResponseHeader_Encoding_DefaultBinary : ResponseHeader,
    ObjectIds.ServiceFault_Encoding_DefaultBinary : ServiceFault,
    ObjectIds.FindServersRequest_Encoding_DefaultBinary : FindServersRequest,
    ObjectIds.FindServersResponse_Encoding_DefaultBinary : FindServersResponse,
    ObjectIds.ServerOnNetwork_Encoding_DefaultBinary : ServerOnNetwork,
    ObjectIds.FindServersOnNetworkRequest_Encoding_DefaultBinary : FindServersOnNetworkRequest,
    ObjectIds.FindServersOnNetworkResponse_Encoding_DefaultBinary : FindServersOnNetworkResponse,
    ObjectIds.UserTokenPolicy_Encoding_DefaultBinary : UserTokenPolicy,
    ObjectIds.EndpointDescription_Encoding_DefaultBinary : EndpointDescription,
    ObjectIds.GetEndpointsRequest_Encoding_DefaultBinary : GetEndpointsRequest,
    ObjectIds.GetEndpointsResponse_Encoding_DefaultBinary : GetEndpointsResponse,
    ObjectIds.RegisteredServer_Encoding_DefaultBinary : RegisteredServer,
    ObjectIds.RegisterServerRequest_Encoding_DefaultBinary : RegisterServerRequest,
    ObjectIds.RegisterServerResponse_Encoding_DefaultBinary : RegisterServerResponse,
    ObjectIds.DiscoveryConfiguration_Encoding_DefaultBinary : DiscoveryConfiguration,
    ObjectIds.MdnsDiscoveryConfiguration_Encoding_DefaultBinary : MdnsDiscoveryConfiguration,
    ObjectIds.RegisterServer2Request_Encoding_DefaultBinary : RegisterServer2Request,
    ObjectIds.RegisterServer2Response_Encoding_DefaultBinary : RegisterServer2Response,
    ObjectIds.ChannelSecurityToken_Encoding_DefaultBinary : ChannelSecurityToken,
    ObjectIds.OpenSecureChannelRequest_Encoding_DefaultBinary : OpenSecureChannelRequest,
    ObjectIds.OpenSecureChannelResponse_Encoding_DefaultBinary : OpenSecureChannelResponse,
    ObjectIds.CloseSecureChannelRequest_Encoding_DefaultBinary : CloseSecureChannelRequest,
    ObjectIds.CloseSecureChannelResponse_Encoding_DefaultBinary : CloseSecureChannelResponse,
    ObjectIds.SignedSoftwareCertificate_Encoding_DefaultBinary : SignedSoftwareCertificate,
    ObjectIds.SignatureData_Encoding_DefaultBinary : SignatureData,
    ObjectIds.CreateSessionRequest_Encoding_DefaultBinary : CreateSessionRequest,
    ObjectIds.CreateSessionResponse_Encoding_DefaultBinary : CreateSessionResponse,
    ObjectIds.UserIdentityToken_Encoding_DefaultBinary : UserIdentityToken,
    ObjectIds.AnonymousIdentityToken_Encoding_DefaultBinary : AnonymousIdentityToken,
    ObjectIds.UserNameIdentityToken_Encoding_DefaultBinary : UserNameIdentityToken,
    ObjectIds.X509IdentityToken_Encoding_DefaultBinary : X509IdentityToken,
    ObjectIds.KerberosIdentityToken_Encoding_DefaultBinary : KerberosIdentityToken,
    ObjectIds.IssuedIdentityToken_Encoding_DefaultBinary : IssuedIdentityToken,
    ObjectIds.ActivateSessionRequest_Encoding_DefaultBinary : ActivateSessionRequest,
    ObjectIds.ActivateSessionResponse_Encoding_DefaultBinary : ActivateSessionResponse,
    ObjectIds.CloseSessionRequest_Encoding_DefaultBinary : CloseSessionRequest,
    ObjectIds.CloseSessionResponse_Encoding_DefaultBinary : CloseSessionResponse,
    ObjectIds.CancelRequest_Encoding_DefaultBinary : CancelRequest,
    ObjectIds.CancelResponse_Encoding_DefaultBinary : CancelResponse,
    ObjectIds.NodeAttributes_Encoding_DefaultBinary : NodeAttributes,
    ObjectIds.ObjectAttributes_Encoding_DefaultBinary : ObjectAttributes,
    ObjectIds.VariableAttributes_Encoding_DefaultBinary : VariableAttributes,
    ObjectIds.MethodAttributes_Encoding_DefaultBinary : MethodAttributes,
    ObjectIds.ObjectTypeAttributes_Encoding_DefaultBinary : ObjectTypeAttributes,
    ObjectIds.VariableTypeAttributes_Encoding_DefaultBinary : VariableTypeAttributes,
    ObjectIds.ReferenceTypeAttributes_Encoding_DefaultBinary : ReferenceTypeAttributes,
    ObjectIds.DataTypeAttributes_Encoding_DefaultBinary : DataTypeAttributes,
    ObjectIds.ViewAttributes_Encoding_DefaultBinary : ViewAttributes,
    ObjectIds.AddNodesItem_Encoding_DefaultBinary : AddNodesItem,
    ObjectIds.AddNodesResult_Encoding_DefaultBinary : AddNodesResult,
    ObjectIds.AddNodesRequest_Encoding_DefaultBinary : AddNodesRequest,
    ObjectIds.AddNodesResponse_Encoding_DefaultBinary : AddNodesResponse,
    ObjectIds.AddReferencesItem_Encoding_DefaultBinary : AddReferencesItem,
    ObjectIds.AddReferencesRequest_Encoding_DefaultBinary : AddReferencesRequest,
    ObjectIds.AddReferencesResponse_Encoding_DefaultBinary : AddReferencesResponse,
    ObjectIds.DeleteNodesItem_Encoding_DefaultBinary : DeleteNodesItem,
    ObjectIds.DeleteNodesRequest_Encoding_DefaultBinary : DeleteNodesRequest,
    ObjectIds.DeleteNodesResponse_Encoding_DefaultBinary : DeleteNodesResponse,
    ObjectIds.DeleteReferencesItem_Encoding_DefaultBinary : DeleteReferencesItem,
    ObjectIds.DeleteReferencesRequest_Encoding_DefaultBinary : DeleteReferencesRequest,
    ObjectIds.DeleteReferencesResponse_Encoding_DefaultBinary : DeleteReferencesResponse,
    ObjectIds.ViewDescription_Encoding_DefaultBinary : ViewDescription,
    ObjectIds.BrowseDescription_Encoding_DefaultBinary : BrowseDescription,
    ObjectIds.ReferenceDescription_Encoding_DefaultBinary : ReferenceDescription,
    ObjectIds.BrowseResult_Encoding_DefaultBinary : BrowseResult,
    ObjectIds.BrowseRequest_Encoding_DefaultBinary : BrowseRequest,
    ObjectIds.BrowseResponse_Encoding_DefaultBinary : BrowseResponse,
    ObjectIds.BrowseNextRequest_Encoding_DefaultBinary : BrowseNextRequest,
    ObjectIds.BrowseNextResponse_Encoding_DefaultBinary : BrowseNextResponse,
    ObjectIds.RelativePathElement_Encoding_DefaultBinary : RelativePathElement,
    ObjectIds.RelativePath_Encoding_DefaultBinary : RelativePath,
    ObjectIds.BrowsePath_Encoding_DefaultBinary : BrowsePath,
    ObjectIds.BrowsePathTarget_Encoding_DefaultBinary : BrowsePathTarget,
    ObjectIds.BrowsePathResult_Encoding_DefaultBinary : BrowsePathResult,
    ObjectIds.TranslateBrowsePathsToNodeIdsRequest_Encoding_DefaultBinary : TranslateBrowsePathsToNodeIdsRequest,
    ObjectIds.TranslateBrowsePathsToNodeIdsResponse_Encoding_DefaultBinary : TranslateBrowsePathsToNodeIdsResponse,
    ObjectIds.RegisterNodesRequest_Encoding_DefaultBinary : RegisterNodesRequest,
    ObjectIds.RegisterNodesResponse_Encoding_DefaultBinary : RegisterNodesResponse,
    ObjectIds.UnregisterNodesRequest_Encoding_DefaultBinary : UnregisterNodesRequest,
    ObjectIds.UnregisterNodesResponse_Encoding_DefaultBinary : UnregisterNodesResponse,
    ObjectIds.EndpointConfiguration_Encoding_DefaultBinary : EndpointConfiguration,
    ObjectIds.SupportedProfile_Encoding_DefaultBinary : SupportedProfile,
    ObjectIds.SoftwareCertificate_Encoding_DefaultBinary : SoftwareCertificate,
    ObjectIds.QueryDataDescription_Encoding_DefaultBinary : QueryDataDescription,
    ObjectIds.NodeTypeDescription_Encoding_DefaultBinary : NodeTypeDescription,
    ObjectIds.QueryDataSet_Encoding_DefaultBinary : QueryDataSet,
    ObjectIds.NodeReference_Encoding_DefaultBinary : NodeReference,
    ObjectIds.ContentFilterElement_Encoding_DefaultBinary : ContentFilterElement,
    ObjectIds.ContentFilter_Encoding_DefaultBinary : ContentFilter,
    ObjectIds.ElementOperand_Encoding_DefaultBinary : ElementOperand,
    ObjectIds.LiteralOperand_Encoding_DefaultBinary : LiteralOperand,
    ObjectIds.AttributeOperand_Encoding_DefaultBinary : AttributeOperand,
    ObjectIds.SimpleAttributeOperand_Encoding_DefaultBinary : SimpleAttributeOperand,
    ObjectIds.ContentFilterElementResult_Encoding_DefaultBinary : ContentFilterElementResult,
    ObjectIds.ContentFilterResult_Encoding_DefaultBinary : ContentFilterResult,
    ObjectIds.ParsingResult_Encoding_DefaultBinary : ParsingResult,
    ObjectIds.QueryFirstRequest_Encoding_DefaultBinary : QueryFirstRequest,
    ObjectIds.QueryFirstResponse_Encoding_DefaultBinary : QueryFirstResponse,
    ObjectIds.QueryNextRequest_Encoding_DefaultBinary : QueryNextRequest,
    ObjectIds.QueryNextResponse_Encoding_DefaultBinary : QueryNextResponse,
    ObjectIds.ReadValueId_Encoding_DefaultBinary : ReadValueId,
    ObjectIds.ReadRequest_Encoding_DefaultBinary : ReadRequest,
    ObjectIds.ReadResponse_Encoding_DefaultBinary : ReadResponse,
    ObjectIds.HistoryReadValueId_Encoding_DefaultBinary : HistoryReadValueId,
    ObjectIds.HistoryReadResult_Encoding_DefaultBinary : HistoryReadResult,
    ObjectIds.HistoryReadDetails_Encoding_DefaultBinary : HistoryReadDetails,
    ObjectIds.ReadEventDetails_Encoding_DefaultBinary : ReadEventDetails,
    ObjectIds.ReadRawModifiedDetails_Encoding_DefaultBinary : ReadRawModifiedDetails,
    ObjectIds.ReadProcessedDetails_Encoding_DefaultBinary : ReadProcessedDetails,
    ObjectIds.ReadAtTimeDetails_Encoding_DefaultBinary : ReadAtTimeDetails,
    ObjectIds.HistoryData_Encoding_DefaultBinary : HistoryData,
    ObjectIds.ModificationInfo_Encoding_DefaultBinary : ModificationInfo,
    ObjectIds.HistoryModifiedData_Encoding_DefaultBinary : HistoryModifiedData,
    ObjectIds.HistoryEvent_Encoding_DefaultBinary : HistoryEvent,
    ObjectIds.HistoryReadRequest_Encoding_DefaultBinary : HistoryReadRequest,
    ObjectIds.HistoryReadResponse_Encoding_DefaultBinary : HistoryReadResponse,
    ObjectIds.WriteValue_Encoding_DefaultBinary : WriteValue,
    ObjectIds.WriteRequest_Encoding_DefaultBinary : WriteRequest,
    ObjectIds.WriteResponse_Encoding_DefaultBinary : WriteResponse,
    ObjectIds.HistoryUpdateDetails_Encoding_DefaultBinary : HistoryUpdateDetails,
    ObjectIds.UpdateDataDetails_Encoding_DefaultBinary : UpdateDataDetails,
    ObjectIds.UpdateStructureDataDetails_Encoding_DefaultBinary : UpdateStructureDataDetails,
    ObjectIds.UpdateEventDetails_Encoding_DefaultBinary : UpdateEventDetails,
    ObjectIds.DeleteRawModifiedDetails_Encoding_DefaultBinary : DeleteRawModifiedDetails,
    ObjectIds.DeleteAtTimeDetails_Encoding_DefaultBinary : DeleteAtTimeDetails,
    ObjectIds.DeleteEventDetails_Encoding_DefaultBinary : DeleteEventDetails,
    ObjectIds.HistoryUpdateResult_Encoding_DefaultBinary : HistoryUpdateResult,
    ObjectIds.HistoryUpdateRequest_Encoding_DefaultBinary : HistoryUpdateRequest,
    ObjectIds.HistoryUpdateResponse_Encoding_DefaultBinary : HistoryUpdateResponse,
    ObjectIds.CallMethodRequest_Encoding_DefaultBinary : CallMethodRequest,
    ObjectIds.CallMethodResult_Encoding_DefaultBinary : CallMethodResult,
    ObjectIds.CallRequest_Encoding_DefaultBinary : CallRequest,
    ObjectIds.CallResponse_Encoding_DefaultBinary : CallResponse,
    ObjectIds.MonitoringFilter_Encoding_DefaultBinary : MonitoringFilter,
    ObjectIds.DataChangeFilter_Encoding_DefaultBinary : DataChangeFilter,
    ObjectIds.EventFilter_Encoding_DefaultBinary : EventFilter,
    ObjectIds.AggregateConfiguration_Encoding_DefaultBinary : AggregateConfiguration,
    ObjectIds.AggregateFilter_Encoding_DefaultBinary : AggregateFilter,
    ObjectIds.MonitoringFilterResult_Encoding_DefaultBinary : MonitoringFilterResult,
    ObjectIds.EventFilterResult_Encoding_DefaultBinary : EventFilterResult,
    ObjectIds.AggregateFilterResult_Encoding_DefaultBinary : AggregateFilterResult,
    ObjectIds.MonitoringParameters_Encoding_DefaultBinary : MonitoringParameters,
    ObjectIds.MonitoredItemCreateRequest_Encoding_DefaultBinary : MonitoredItemCreateRequest,
    ObjectIds.MonitoredItemCreateResult_Encoding_DefaultBinary : MonitoredItemCreateResult,
    ObjectIds.CreateMonitoredItemsRequest_Encoding_DefaultBinary : CreateMonitoredItemsRequest,
    ObjectIds.CreateMonitoredItemsResponse_Encoding_DefaultBinary : CreateMonitoredItemsResponse,
    ObjectIds.MonitoredItemModifyRequest_Encoding_DefaultBinary : MonitoredItemModifyRequest,
    ObjectIds.MonitoredItemModifyResult_Encoding_DefaultBinary : MonitoredItemModifyResult,
    ObjectIds.ModifyMonitoredItemsRequest_Encoding_DefaultBinary : ModifyMonitoredItemsRequest,
    ObjectIds.ModifyMonitoredItemsResponse_Encoding_DefaultBinary : ModifyMonitoredItemsResponse,
    ObjectIds.SetMonitoringModeRequest_Encoding_DefaultBinary : SetMonitoringModeRequest,
    ObjectIds.SetMonitoringModeResponse_Encoding_DefaultBinary : SetMonitoringModeResponse,
    ObjectIds.SetTriggeringRequest_Encoding_DefaultBinary : SetTriggeringRequest,
    ObjectIds.SetTriggeringResponse_Encoding_DefaultBinary : SetTriggeringResponse,
    ObjectIds.DeleteMonitoredItemsRequest_Encoding_DefaultBinary : DeleteMonitoredItemsRequest,
    ObjectIds.DeleteMonitoredItemsResponse_Encoding_DefaultBinary : DeleteMonitoredItemsResponse,
    ObjectIds.CreateSubscriptionRequest_Encoding_DefaultBinary : CreateSubscriptionRequest,
    ObjectIds.CreateSubscriptionResponse_Encoding_DefaultBinary : CreateSubscriptionResponse,
    ObjectIds.ModifySubscriptionRequest_Encoding_DefaultBinary : ModifySubscriptionRequest,
    ObjectIds.ModifySubscriptionResponse_Encoding_DefaultBinary : ModifySubscriptionResponse,
    ObjectIds.SetPublishingModeRequest_Encoding_DefaultBinary : SetPublishingModeRequest,
    ObjectIds.SetPublishingModeResponse_Encoding_DefaultBinary : SetPublishingModeResponse,
    ObjectIds.NotificationMessage_Encoding_DefaultBinary : NotificationMessage,
    ObjectIds.NotificationData_Encoding_DefaultBinary : NotificationData,
    ObjectIds.DataChangeNotification_Encoding_DefaultBinary : DataChangeNotification,
    ObjectIds.MonitoredItemNotification_Encoding_DefaultBinary : MonitoredItemNotification,
    ObjectIds.EventNotificationList_Encoding_DefaultBinary : EventNotificationList,
    ObjectIds.EventFieldList_Encoding_DefaultBinary : EventFieldList,
    ObjectIds.HistoryEventFieldList_Encoding_DefaultBinary : HistoryEventFieldList,
    ObjectIds.StatusChangeNotification_Encoding_DefaultBinary : StatusChangeNotification,
    ObjectIds.SubscriptionAcknowledgement_Encoding_DefaultBinary : SubscriptionAcknowledgement,
    ObjectIds.PublishRequest_Encoding_DefaultBinary : PublishRequest,
    ObjectIds.PublishResponse_Encoding_DefaultBinary : PublishResponse,
    ObjectIds.RepublishRequest_Encoding_DefaultBinary : RepublishRequest,
    ObjectIds.RepublishResponse_Encoding_DefaultBinary : RepublishResponse,
    ObjectIds.TransferResult_Encoding_DefaultBinary : TransferResult,
    ObjectIds.TransferSubscriptionsRequest_Encoding_DefaultBinary : TransferSubscriptionsRequest,
    ObjectIds.TransferSubscriptionsResponse_Encoding_DefaultBinary : TransferSubscriptionsResponse,
    ObjectIds.DeleteSubscriptionsRequest_Encoding_DefaultBinary : DeleteSubscriptionsRequest,
    ObjectIds.DeleteSubscriptionsResponse_Encoding_DefaultBinary : DeleteSubscriptionsResponse,
    ObjectIds.BuildInfo_Encoding_DefaultBinary : BuildInfo,
    ObjectIds.RedundantServerDataType_Encoding_DefaultBinary : RedundantServerDataType,
    ObjectIds.EndpointUrlListDataType_Encoding_DefaultBinary : EndpointUrlListDataType,
    ObjectIds.NetworkGroupDataType_Encoding_DefaultBinary : NetworkGroupDataType,
    ObjectIds.SamplingIntervalDiagnosticsDataType_Encoding_DefaultBinary : SamplingIntervalDiagnosticsDataType,
    ObjectIds.ServerDiagnosticsSummaryDataType_Encoding_DefaultBinary : ServerDiagnosticsSummaryDataType,
    ObjectIds.ServerStatusDataType_Encoding_DefaultBinary : ServerStatusDataType,
    ObjectIds.SessionDiagnosticsDataType_Encoding_DefaultBinary : SessionDiagnosticsDataType,
    ObjectIds.SessionSecurityDiagnosticsDataType_Encoding_DefaultBinary : SessionSecurityDiagnosticsDataType,
    ObjectIds.ServiceCounterDataType_Encoding_DefaultBinary : ServiceCounterDataType,
    ObjectIds.StatusResult_Encoding_DefaultBinary : StatusResult,
    ObjectIds.SubscriptionDiagnosticsDataType_Encoding_DefaultBinary : SubscriptionDiagnosticsDataType,
    ObjectIds.ModelChangeStructureDataType_Encoding_DefaultBinary : ModelChangeStructureDataType,
    ObjectIds.SemanticChangeStructureDataType_Encoding_DefaultBinary : SemanticChangeStructureDataType,
    ObjectIds.Range_Encoding_DefaultBinary : Range,
    ObjectIds.EUInformation_Encoding_DefaultBinary : EUInformation,
    ObjectIds.ComplexNumberType_Encoding_DefaultBinary : ComplexNumberType,
    ObjectIds.DoubleComplexNumberType_Encoding_DefaultBinary : DoubleComplexNumberType,
    ObjectIds.AxisInformation_Encoding_DefaultBinary : AxisInformation,
    ObjectIds.XVType_Encoding_DefaultBinary : XVType,
    ObjectIds.ProgramDiagnosticDataType_Encoding_DefaultBinary : ProgramDiagnosticDataType,
    ObjectIds.Annotation_Encoding_DefaultBinary : Annotation,
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
