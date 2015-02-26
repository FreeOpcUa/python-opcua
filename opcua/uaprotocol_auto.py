'''
Autogenerate code from xml spec
'''

import struct

from .uatypes import *
from .object_ids import ObjectIds



class OpenFileMode(object):
    Read = 1
    Write = 2
    EraseExisiting = 4
    Append = 8

class IdType(object):
    Numeric = 0
    String = 1
    Guid = 2
    Opaque = 3

class NodeClass(object):
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
    Server = 0
    Client = 1
    ClientAndServer = 2
    DiscoveryServer = 3

class MessageSecurityMode(object):
    Invalid = 0
    None_ = 1
    Sign = 2
    SignAndEncrypt = 3

class UserTokenType(object):
    Anonymous = 0
    UserName = 1
    Certificate = 2
    IssuedToken = 3

class SecurityTokenRequestType(object):
    Issue = 0
    Renew = 1

class NodeAttributesMask(object):
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
    Forward = 0
    Inverse = 1
    Both = 2

class BrowseResultMask(object):
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
    Untested = 0
    Partial = 1
    SelfTested = 2
    Certified = 3

class FilterOperator(object):
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
    Source = 0
    Server = 1
    Both = 2
    Neither = 3

class HistoryUpdateType(object):
    Insert = 1
    Replace = 2
    Update = 3
    Delete = 4

class PerformUpdateType(object):
    Insert = 1
    Replace = 2
    Update = 3
    Remove = 4

class MonitoringMode(object):
    Disabled = 0
    Sampling = 1
    Reporting = 2

class DataChangeTrigger(object):
    Status = 0
    StatusValue = 1
    StatusValueTimestamp = 2

class DeadbandType(object):
    None_ = 0
    Absolute = 1
    Percent = 2

class EnumeratedTestType(object):
    Red = 1
    Yellow = 4
    Green = 5

class RedundancySupport(object):
    None_ = 0
    Cold = 1
    Warm = 2
    Hot = 3
    Transparent = 4
    HotAndMirrored = 5

class ServerState(object):
    Running = 0
    Failed = 1
    NoConfiguration = 2
    Suspended = 3
    Shutdown = 4
    Test = 5
    CommunicationFault = 6
    Unknown = 7

class ModelChangeStructureVerbMask(object):
    NodeAdded = 1
    NodeDeleted = 2
    ReferenceAdded = 4
    ReferenceDeleted = 8
    DataTypeChanged = 16

class AxisScaleEnumeration(object):
    Linear = 0
    Log = 1
    Ln = 2

class ExceptionDeviationFormat(object):
    AbsoluteValue = 0
    PercentOfRange = 1
    PercentOfValue = 2
    PercentOfEURange = 3
    Unknown = 4

class ExtensionObject(object):
    def __init__(self):
        self.TypeId = NodeId()
        self.Encoding = 0
        self.Body = ByteString()
    
    def to_binary(self):
        packet = []
        if self.Body: self.Encoding |= (1 << 0)
        packet.append(self.TypeId.to_binary())
        fmt = '<B'
        packet.append(struct.pack(fmt, self.Encoding))
        if self.Body: 
            packet.append(self.Body.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ExtensionObject()
        obj.TypeId = NodeId.from_binary(data)
        fmt = '<B'
        fmt_size = 1
        obj.Encoding = struct.unpack(fmt, data.read(fmt_size))[0]
        if obj.Encoding & (1 << 0):
            obj.Body = ByteString.from_binary(data)
        return obj
    
    def __str__(self):
        return 'ExtensionObject(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'Body:' + str(self.Body) + ')'
    
    __repr__ = __str__
    
class XmlElement(object):
    def __init__(self):
        self.Length = 0
        self.Value = []
    
    def to_binary(self):
        packet = []
        fmt = '<i'
        packet.append(struct.pack(fmt, self.Length))
        packet.append(struct.pack('<i', len(self.Value)))
        for i in self.Value:
            fmt = '<s'
            packet.append(struct.pack(fmt, self.Value))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = XmlElement()
        fmt = '<i'
        fmt_size = 4
        obj.Length = struct.unpack(fmt, data.read(fmt_size))[0]
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                fmt = '<s'
                fmt_size = 1
                obj.Value = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'XmlElement(' + 'Length:' + str(self.Length) + ', '  + \
             'Value:' + str(self.Value) + ')'
    
    __repr__ = __str__
    
class TwoByteNodeId(object):
    def __init__(self):
        self.Identifier = 0
    
    def to_binary(self):
        packet = []
        fmt = '<B'
        packet.append(struct.pack(fmt, self.Identifier))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = TwoByteNodeId()
        fmt = '<B'
        fmt_size = 1
        obj.Identifier = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'TwoByteNodeId(' + 'Identifier:' + str(self.Identifier) + ')'
    
    __repr__ = __str__
    
class FourByteNodeId(object):
    def __init__(self):
        self.NamespaceIndex = 0
        self.Identifier = 0
    
    def to_binary(self):
        packet = []
        fmt = '<B'
        packet.append(struct.pack(fmt, self.NamespaceIndex))
        fmt = '<H'
        packet.append(struct.pack(fmt, self.Identifier))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = FourByteNodeId()
        fmt = '<B'
        fmt_size = 1
        obj.NamespaceIndex = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<H'
        fmt_size = 2
        obj.Identifier = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'FourByteNodeId(' + 'NamespaceIndex:' + str(self.NamespaceIndex) + ', '  + \
             'Identifier:' + str(self.Identifier) + ')'
    
    __repr__ = __str__
    
class NumericNodeId(object):
    def __init__(self):
        self.NamespaceIndex = 0
        self.Identifier = 0
    
    def to_binary(self):
        packet = []
        fmt = '<H'
        packet.append(struct.pack(fmt, self.NamespaceIndex))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.Identifier))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = NumericNodeId()
        fmt = '<H'
        fmt_size = 2
        obj.NamespaceIndex = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.Identifier = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'NumericNodeId(' + 'NamespaceIndex:' + str(self.NamespaceIndex) + ', '  + \
             'Identifier:' + str(self.Identifier) + ')'
    
    __repr__ = __str__
    
class StringNodeId(object):
    def __init__(self):
        self.NamespaceIndex = 0
        self.Identifier = b''
    
    def to_binary(self):
        packet = []
        fmt = '<H'
        packet.append(struct.pack(fmt, self.NamespaceIndex))
        fmt = '<s'
        packet.append(struct.pack(fmt, self.Identifier))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = StringNodeId()
        fmt = '<H'
        fmt_size = 2
        obj.NamespaceIndex = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<s'
        fmt_size = 1
        obj.Identifier = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'StringNodeId(' + 'NamespaceIndex:' + str(self.NamespaceIndex) + ', '  + \
             'Identifier:' + str(self.Identifier) + ')'
    
    __repr__ = __str__
    
class GuidNodeId(object):
    def __init__(self):
        self.NamespaceIndex = 0
        self.Identifier = Guid()
    
    def to_binary(self):
        packet = []
        fmt = '<H'
        packet.append(struct.pack(fmt, self.NamespaceIndex))
        packet.append(self.Identifier.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = GuidNodeId()
        fmt = '<H'
        fmt_size = 2
        obj.NamespaceIndex = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.Identifier = Guid.from_binary(data)
        return obj
    
    def __str__(self):
        return 'GuidNodeId(' + 'NamespaceIndex:' + str(self.NamespaceIndex) + ', '  + \
             'Identifier:' + str(self.Identifier) + ')'
    
    __repr__ = __str__
    
class ByteStringNodeId(object):
    def __init__(self):
        self.NamespaceIndex = 0
        self.Identifier = ByteString()
    
    def to_binary(self):
        packet = []
        fmt = '<H'
        packet.append(struct.pack(fmt, self.NamespaceIndex))
        packet.append(self.Identifier.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ByteStringNodeId()
        fmt = '<H'
        fmt_size = 2
        obj.NamespaceIndex = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.Identifier = ByteString.from_binary(data)
        return obj
    
    def __str__(self):
        return 'ByteStringNodeId(' + 'NamespaceIndex:' + str(self.NamespaceIndex) + ', '  + \
             'Identifier:' + str(self.Identifier) + ')'
    
    __repr__ = __str__
    
class DiagnosticInfo(object):
    def __init__(self):
        self.Encoding = 0
        self.SymbolicId = 0
        self.NamespaceURI = 0
        self.LocalizedText = 0
        self.AdditionalInfo = b''
        self.InnerStatusCode = StatusCode()
        self.InnerDiagnosticInfo = None
    
    def to_binary(self):
        if self.InnerDiagnosticInfo is None: self.InnerDiagnosticInfo = DiagnosticInfo()
        packet = []
        if self.SymbolicId: self.Encoding |= (1 << 0)
        if self.NamespaceURI: self.Encoding |= (1 << 1)
        if self.LocalizedText: self.Encoding |= (1 << 2)
        if self.AdditionalInfo: self.Encoding |= (1 << 4)
        if self.InnerStatusCode: self.Encoding |= (1 << 5)
        if self.InnerDiagnosticInfo: self.Encoding |= (1 << 6)
        fmt = '<B'
        packet.append(struct.pack(fmt, self.Encoding))
        if self.SymbolicId: 
            fmt = '<i'
            packet.append(struct.pack(fmt, self.SymbolicId))
        if self.NamespaceURI: 
            fmt = '<i'
            packet.append(struct.pack(fmt, self.NamespaceURI))
        if self.LocalizedText: 
            fmt = '<i'
            packet.append(struct.pack(fmt, self.LocalizedText))
        if self.AdditionalInfo: 
            fmt = '<s'
            packet.append(struct.pack(fmt, self.AdditionalInfo))
        if self.InnerStatusCode: 
            packet.append(self.InnerStatusCode.to_binary())
        if self.InnerDiagnosticInfo: 
            packet.append(self.InnerDiagnosticInfo.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = DiagnosticInfo()
        fmt = '<B'
        fmt_size = 1
        obj.Encoding = struct.unpack(fmt, data.read(fmt_size))[0]
        if obj.Encoding & (1 << 0):
            fmt = '<i'
            fmt_size = 4
            obj.SymbolicId = struct.unpack(fmt, data.read(fmt_size))[0]
        if obj.Encoding & (1 << 1):
            fmt = '<i'
            fmt_size = 4
            obj.NamespaceURI = struct.unpack(fmt, data.read(fmt_size))[0]
        if obj.Encoding & (1 << 2):
            fmt = '<i'
            fmt_size = 4
            obj.LocalizedText = struct.unpack(fmt, data.read(fmt_size))[0]
        if obj.Encoding & (1 << 4):
            fmt = '<s'
            fmt_size = 1
            obj.AdditionalInfo = struct.unpack(fmt, data.read(fmt_size))[0]
        if obj.Encoding & (1 << 5):
            obj.InnerStatusCode = StatusCode.from_binary(data)
        if obj.Encoding & (1 << 6):
            obj.InnerDiagnosticInfo = DiagnosticInfo.from_binary(data)
        return obj
    
    def __str__(self):
        return 'DiagnosticInfo(' + 'Encoding:' + str(self.Encoding) + ', '  + \
             'SymbolicId:' + str(self.SymbolicId) + ', '  + \
             'NamespaceURI:' + str(self.NamespaceURI) + ', '  + \
             'LocalizedText:' + str(self.LocalizedText) + ', '  + \
             'AdditionalInfo:' + str(self.AdditionalInfo) + ', '  + \
             'InnerStatusCode:' + str(self.InnerStatusCode) + ', '  + \
             'InnerDiagnosticInfo:' + str(self.InnerDiagnosticInfo) + ')'
    
    __repr__ = __str__
    
class QualifiedName(object):
    def __init__(self):
        self.NamespaceIndex = 0
        self.Name = b''
    
    def to_binary(self):
        packet = []
        fmt = '<i'
        packet.append(struct.pack(fmt, self.NamespaceIndex))
        fmt = '<s'
        packet.append(struct.pack(fmt, self.Name))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = QualifiedName()
        fmt = '<i'
        fmt_size = 4
        obj.NamespaceIndex = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<s'
        fmt_size = 1
        obj.Name = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'QualifiedName(' + 'NamespaceIndex:' + str(self.NamespaceIndex) + ', '  + \
             'Name:' + str(self.Name) + ')'
    
    __repr__ = __str__
    
class LocalizedText(object):
    def __init__(self):
        self.Encoding = 0
        self.Locale = b''
        self.Text = b''
    
    def to_binary(self):
        packet = []
        if self.Locale: self.Encoding |= (1 << 0)
        if self.Text: self.Encoding |= (1 << 1)
        fmt = '<B'
        packet.append(struct.pack(fmt, self.Encoding))
        if self.Locale: 
            fmt = '<s'
            packet.append(struct.pack(fmt, self.Locale))
        if self.Text: 
            fmt = '<s'
            packet.append(struct.pack(fmt, self.Text))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = LocalizedText()
        fmt = '<B'
        fmt_size = 1
        obj.Encoding = struct.unpack(fmt, data.read(fmt_size))[0]
        if obj.Encoding & (1 << 0):
            fmt = '<s'
            fmt_size = 1
            obj.Locale = struct.unpack(fmt, data.read(fmt_size))[0]
        if obj.Encoding & (1 << 1):
            fmt = '<s'
            fmt_size = 1
            obj.Text = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'LocalizedText(' + 'Encoding:' + str(self.Encoding) + ', '  + \
             'Locale:' + str(self.Locale) + ', '  + \
             'Text:' + str(self.Text) + ')'
    
    __repr__ = __str__
    
class DataValue(object):
    def __init__(self):
        self.Encoding = 0
        self.Value = Variant()
        self.StatusCode = StatusCode()
        self.SourceTimestamp = DateTime()
        self.SourcePicoseconds = 0
        self.ServerTimestamp = DateTime()
        self.ServerPicoseconds = 0
    
    def to_binary(self):
        packet = []
        if self.Value: self.Encoding |= (1 << 0)
        if self.StatusCode: self.Encoding |= (1 << 1)
        if self.SourceTimestamp: self.Encoding |= (1 << 2)
        if self.SourcePicoseconds: self.Encoding |= (1 << 3)
        if self.ServerTimestamp: self.Encoding |= (1 << 4)
        if self.ServerPicoseconds: self.Encoding |= (1 << 5)
        fmt = '<B'
        packet.append(struct.pack(fmt, self.Encoding))
        if self.Value: 
            packet.append(self.Value.to_binary())
        if self.StatusCode: 
            packet.append(self.StatusCode.to_binary())
        if self.SourceTimestamp: 
            packet.append(self.SourceTimestamp.to_binary())
        if self.SourcePicoseconds: 
            fmt = '<H'
            packet.append(struct.pack(fmt, self.SourcePicoseconds))
        if self.ServerTimestamp: 
            packet.append(self.ServerTimestamp.to_binary())
        if self.ServerPicoseconds: 
            fmt = '<H'
            packet.append(struct.pack(fmt, self.ServerPicoseconds))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = DataValue()
        fmt = '<B'
        fmt_size = 1
        obj.Encoding = struct.unpack(fmt, data.read(fmt_size))[0]
        if obj.Encoding & (1 << 0):
            obj.Value = Variant.from_binary(data)
        if obj.Encoding & (1 << 1):
            obj.StatusCode = StatusCode.from_binary(data)
        if obj.Encoding & (1 << 2):
            obj.SourceTimestamp = DateTime.from_binary(data)
        if obj.Encoding & (1 << 3):
            fmt = '<H'
            fmt_size = 2
            obj.SourcePicoseconds = struct.unpack(fmt, data.read(fmt_size))[0]
        if obj.Encoding & (1 << 4):
            obj.ServerTimestamp = DateTime.from_binary(data)
        if obj.Encoding & (1 << 5):
            fmt = '<H'
            fmt_size = 2
            obj.ServerPicoseconds = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'DataValue(' + 'Encoding:' + str(self.Encoding) + ', '  + \
             'Value:' + str(self.Value) + ', '  + \
             'StatusCode:' + str(self.StatusCode) + ', '  + \
             'SourceTimestamp:' + str(self.SourceTimestamp) + ', '  + \
             'SourcePicoseconds:' + str(self.SourcePicoseconds) + ', '  + \
             'ServerTimestamp:' + str(self.ServerTimestamp) + ', '  + \
             'ServerPicoseconds:' + str(self.ServerPicoseconds) + ')'
    
    __repr__ = __str__
    
class Variant(object):
    def __init__(self):
        self.Encoding = 0
        self.ArrayLength = 0
        self.Boolean = []
        self.SByte = []
        self.Byte = []
        self.Int16 = []
        self.UInt16 = []
        self.Int32 = []
        self.UInt32 = []
        self.Int64 = []
        self.UInt64 = []
        self.Float = []
        self.Double = []
        self.String = []
        self.DateTime = []
        self.Guid = []
        self.ByteString = []
        self.XmlElement = []
        self.NodeId = []
        self.ExpandedNodeId = []
        self.StatusCode = []
        self.DiagnosticInfo = []
        self.QualifiedName = []
        self.LocalizedText = []
        self.ExtensionObject = []
        self.DataValue = []
        self.Variant = None
    
    def to_binary(self):
        if self.Variant is None: self.Variant = Variant()
        packet = []
        if self.ArrayLength: self.Encoding |= (1 << 7)
        others = self.Encoding & 0b01111111
        if self.Boolean: self.Encoding = ( 1 | others )
        others = self.Encoding & 0b01111111
        if self.SByte: self.Encoding = ( 2 | others )
        others = self.Encoding & 0b01111111
        if self.Byte: self.Encoding = ( 3 | others )
        others = self.Encoding & 0b01111111
        if self.Int16: self.Encoding = ( 4 | others )
        others = self.Encoding & 0b01111111
        if self.UInt16: self.Encoding = ( 5 | others )
        others = self.Encoding & 0b01111111
        if self.Int32: self.Encoding = ( 6 | others )
        others = self.Encoding & 0b01111111
        if self.UInt32: self.Encoding = ( 7 | others )
        others = self.Encoding & 0b01111111
        if self.Int64: self.Encoding = ( 8 | others )
        others = self.Encoding & 0b01111111
        if self.UInt64: self.Encoding = ( 9 | others )
        others = self.Encoding & 0b01111111
        if self.Float: self.Encoding = ( 10 | others )
        others = self.Encoding & 0b01111111
        if self.Double: self.Encoding = ( 11 | others )
        others = self.Encoding & 0b01111111
        if self.String: self.Encoding = ( 12 | others )
        others = self.Encoding & 0b01111111
        if self.DateTime: self.Encoding = ( 13 | others )
        others = self.Encoding & 0b01111111
        if self.Guid: self.Encoding = ( 14 | others )
        others = self.Encoding & 0b01111111
        if self.ByteString: self.Encoding = ( 15 | others )
        others = self.Encoding & 0b01111111
        if self.XmlElement: self.Encoding = ( 16 | others )
        others = self.Encoding & 0b01111111
        if self.NodeId: self.Encoding = ( 17 | others )
        others = self.Encoding & 0b01111111
        if self.ExpandedNodeId: self.Encoding = ( 18 | others )
        others = self.Encoding & 0b01111111
        if self.StatusCode: self.Encoding = ( 19 | others )
        others = self.Encoding & 0b01111111
        if self.DiagnosticInfo: self.Encoding = ( 20 | others )
        others = self.Encoding & 0b01111111
        if self.QualifiedName: self.Encoding = ( 21 | others )
        others = self.Encoding & 0b01111111
        if self.LocalizedText: self.Encoding = ( 22 | others )
        others = self.Encoding & 0b01111111
        if self.ExtensionObject: self.Encoding = ( 23 | others )
        others = self.Encoding & 0b01111111
        if self.DataValue: self.Encoding = ( 24 | others )
        others = self.Encoding & 0b01111111
        if self.Variant: self.Encoding = ( 25 | others )
        fmt = '<B'
        packet.append(struct.pack(fmt, self.Encoding))
        if self.ArrayLength: 
            fmt = '<i'
            packet.append(struct.pack(fmt, self.ArrayLength))
        if self.Boolean: 
            packet.append(struct.pack('<i', len(self.Boolean)))
            for i in self.Boolean:
                fmt = '<?'
                packet.append(struct.pack(fmt, self.Boolean))
        if self.SByte: 
            packet.append(struct.pack('<i', len(self.SByte)))
            for i in self.SByte:
                fmt = '<B'
                packet.append(struct.pack(fmt, self.SByte))
        if self.Byte: 
            packet.append(struct.pack('<i', len(self.Byte)))
            for i in self.Byte:
                fmt = '<B'
                packet.append(struct.pack(fmt, self.Byte))
        if self.Int16: 
            packet.append(struct.pack('<i', len(self.Int16)))
            for i in self.Int16:
                fmt = '<h'
                packet.append(struct.pack(fmt, self.Int16))
        if self.UInt16: 
            packet.append(struct.pack('<i', len(self.UInt16)))
            for i in self.UInt16:
                fmt = '<H'
                packet.append(struct.pack(fmt, self.UInt16))
        if self.Int32: 
            packet.append(struct.pack('<i', len(self.Int32)))
            for i in self.Int32:
                fmt = '<i'
                packet.append(struct.pack(fmt, self.Int32))
        if self.UInt32: 
            packet.append(struct.pack('<i', len(self.UInt32)))
            for i in self.UInt32:
                fmt = '<I'
                packet.append(struct.pack(fmt, self.UInt32))
        if self.Int64: 
            packet.append(struct.pack('<i', len(self.Int64)))
            for i in self.Int64:
                fmt = '<q'
                packet.append(struct.pack(fmt, self.Int64))
        if self.UInt64: 
            packet.append(struct.pack('<i', len(self.UInt64)))
            for i in self.UInt64:
                fmt = '<Q'
                packet.append(struct.pack(fmt, self.UInt64))
        if self.Float: 
            packet.append(struct.pack('<i', len(self.Float)))
            for i in self.Float:
                fmt = '<f'
                packet.append(struct.pack(fmt, self.Float))
        if self.Double: 
            packet.append(struct.pack('<i', len(self.Double)))
            for i in self.Double:
                fmt = '<d'
                packet.append(struct.pack(fmt, self.Double))
        if self.String: 
            packet.append(struct.pack('<i', len(self.String)))
            for i in self.String:
                packet.append(struct.pack('<i', len(self.String)))
                packet.append(struct.pack('<{}s'.format(len(self.String)), self.String.encode()))
        if self.DateTime: 
            packet.append(struct.pack('<i', len(self.DateTime)))
            for i in self.DateTime:
                packet.append(self.DateTime.to_binary())
        if self.Guid: 
            packet.append(struct.pack('<i', len(self.Guid)))
            for i in self.Guid:
                packet.append(self.Guid.to_binary())
        if self.ByteString: 
            packet.append(struct.pack('<i', len(self.ByteString)))
            for i in self.ByteString:
                packet.append(self.ByteString.to_binary())
        if self.XmlElement: 
            packet.append(struct.pack('<i', len(self.XmlElement)))
            for i in self.XmlElement:
                packet.append(self.XmlElement.to_binary())
        if self.NodeId: 
            packet.append(struct.pack('<i', len(self.NodeId)))
            for i in self.NodeId:
                packet.append(self.NodeId.to_binary())
        if self.ExpandedNodeId: 
            packet.append(struct.pack('<i', len(self.ExpandedNodeId)))
            for i in self.ExpandedNodeId:
                packet.append(self.ExpandedNodeId.to_binary())
        if self.StatusCode: 
            packet.append(struct.pack('<i', len(self.StatusCode)))
            for i in self.StatusCode:
                packet.append(self.StatusCode.to_binary())
        if self.DiagnosticInfo: 
            packet.append(struct.pack('<i', len(self.DiagnosticInfo)))
            for i in self.DiagnosticInfo:
                packet.append(self.DiagnosticInfo.to_binary())
        if self.QualifiedName: 
            packet.append(struct.pack('<i', len(self.QualifiedName)))
            for i in self.QualifiedName:
                packet.append(self.QualifiedName.to_binary())
        if self.LocalizedText: 
            packet.append(struct.pack('<i', len(self.LocalizedText)))
            for i in self.LocalizedText:
                packet.append(self.LocalizedText.to_binary())
        if self.ExtensionObject: 
            packet.append(struct.pack('<i', len(self.ExtensionObject)))
            for i in self.ExtensionObject:
                packet.append(self.ExtensionObject.to_binary())
        if self.DataValue: 
            packet.append(struct.pack('<i', len(self.DataValue)))
            for i in self.DataValue:
                packet.append(self.DataValue.to_binary())
        if self.Variant: 
            packet.append(struct.pack('<i', len(self.Variant)))
            for i in self.Variant:
                packet.append(self.Variant.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = Variant()
        fmt = '<B'
        fmt_size = 1
        obj.Encoding = struct.unpack(fmt, data.read(fmt_size))[0]
        if obj.Encoding & (1 << 7):
            fmt = '<i'
            fmt_size = 4
            obj.ArrayLength = struct.unpack(fmt, data.read(fmt_size))[0]
        val = obj.Encoding & 0b01111111
        if val == 0:
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    fmt = '<?'
                    fmt_size = 1
                    obj.Boolean = struct.unpack(fmt, data.read(fmt_size))[0]
        val = obj.Encoding & 0b01111111
        if val == 0:
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    fmt = '<B'
                    fmt_size = 1
                    obj.SByte = struct.unpack(fmt, data.read(fmt_size))[0]
        val = obj.Encoding & 0b01111111
        if val == 0:
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    fmt = '<B'
                    fmt_size = 1
                    obj.Byte = struct.unpack(fmt, data.read(fmt_size))[0]
        val = obj.Encoding & 0b01111111
        if val == 0:
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    fmt = '<h'
                    fmt_size = 2
                    obj.Int16 = struct.unpack(fmt, data.read(fmt_size))[0]
        val = obj.Encoding & 0b01111111
        if val == 0:
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    fmt = '<H'
                    fmt_size = 2
                    obj.UInt16 = struct.unpack(fmt, data.read(fmt_size))[0]
        val = obj.Encoding & 0b01111111
        if val == 0:
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    fmt = '<i'
                    fmt_size = 4
                    obj.Int32 = struct.unpack(fmt, data.read(fmt_size))[0]
        val = obj.Encoding & 0b01111111
        if val == 0:
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    fmt = '<I'
                    fmt_size = 4
                    obj.UInt32 = struct.unpack(fmt, data.read(fmt_size))[0]
        val = obj.Encoding & 0b01111111
        if val == 0:
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    fmt = '<q'
                    fmt_size = 8
                    obj.Int64 = struct.unpack(fmt, data.read(fmt_size))[0]
        val = obj.Encoding & 0b01111111
        if val == 0:
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    fmt = '<Q'
                    fmt_size = 8
                    obj.UInt64 = struct.unpack(fmt, data.read(fmt_size))[0]
        val = obj.Encoding & 0b01111111
        if val == 0:
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    fmt = '<f'
                    fmt_size = 4
                    obj.Float = struct.unpack(fmt, data.read(fmt_size))[0]
        val = obj.Encoding & 0b01111111
        if val == 0:
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    fmt = '<d'
                    fmt_size = 8
                    obj.Double = struct.unpack(fmt, data.read(fmt_size))[0]
        val = obj.Encoding & 0b01111111
        if val == 0:
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    slength = struct.unpack('<i', data.red(1))
                    obj.String = struct.unpack('<{}s'.format(slength), data.read(slength))
        val = obj.Encoding & 0b01111111
        if val == 0:
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    obj.DateTime = DateTime.from_binary(data)
        val = obj.Encoding & 0b01111111
        if val == 0:
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    obj.Guid = Guid.from_binary(data)
        val = obj.Encoding & 0b01111111
        if val == 0:
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    obj.ByteString = ByteString.from_binary(data)
        val = obj.Encoding & 0b01111111
        if val == 0:
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    obj.XmlElement = XmlElement.from_binary(data)
        val = obj.Encoding & 0b01111111
        if val == 0:
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    obj.NodeId = NodeId.from_binary(data)
        val = obj.Encoding & 0b01111111
        if val == 0:
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    obj.ExpandedNodeId = ExpandedNodeId.from_binary(data)
        val = obj.Encoding & 0b01111111
        if val == 0:
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    obj.StatusCode = StatusCode.from_binary(data)
        val = obj.Encoding & 0b01111111
        if val == 0:
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    obj.DiagnosticInfo = DiagnosticInfo.from_binary(data)
        val = obj.Encoding & 0b01111111
        if val == 0:
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    obj.QualifiedName = QualifiedName.from_binary(data)
        val = obj.Encoding & 0b01111111
        if val == 0:
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    obj.LocalizedText = LocalizedText.from_binary(data)
        val = obj.Encoding & 0b01111111
        if val == 0:
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    obj.ExtensionObject = ExtensionObject.from_binary(data)
        val = obj.Encoding & 0b01111111
        if val == 0:
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    obj.DataValue = DataValue.from_binary(data)
        val = obj.Encoding & 0b01111111
        if val == 0:
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    obj.Variant = Variant.from_binary(data)
        return obj
    
    def __str__(self):
        return 'Variant(' + 'Encoding:' + str(self.Encoding) + ', '  + \
             'ArrayLength:' + str(self.ArrayLength) + ', '  + \
             'Boolean:' + str(self.Boolean) + ', '  + \
             'SByte:' + str(self.SByte) + ', '  + \
             'Byte:' + str(self.Byte) + ', '  + \
             'Int16:' + str(self.Int16) + ', '  + \
             'UInt16:' + str(self.UInt16) + ', '  + \
             'Int32:' + str(self.Int32) + ', '  + \
             'UInt32:' + str(self.UInt32) + ', '  + \
             'Int64:' + str(self.Int64) + ', '  + \
             'UInt64:' + str(self.UInt64) + ', '  + \
             'Float:' + str(self.Float) + ', '  + \
             'Double:' + str(self.Double) + ', '  + \
             'String:' + str(self.String) + ', '  + \
             'DateTime:' + str(self.DateTime) + ', '  + \
             'Guid:' + str(self.Guid) + ', '  + \
             'ByteString:' + str(self.ByteString) + ', '  + \
             'XmlElement:' + str(self.XmlElement) + ', '  + \
             'NodeId:' + str(self.NodeId) + ', '  + \
             'ExpandedNodeId:' + str(self.ExpandedNodeId) + ', '  + \
             'StatusCode:' + str(self.StatusCode) + ', '  + \
             'DiagnosticInfo:' + str(self.DiagnosticInfo) + ', '  + \
             'QualifiedName:' + str(self.QualifiedName) + ', '  + \
             'LocalizedText:' + str(self.LocalizedText) + ', '  + \
             'ExtensionObject:' + str(self.ExtensionObject) + ', '  + \
             'DataValue:' + str(self.DataValue) + ', '  + \
             'Variant:' + str(self.Variant) + ')'
    
    __repr__ = __str__
    
class Node(object):
    def __init__(self):
        self.NodeId = NodeId()
        self.NodeClass = 0
        self.BrowseName = QualifiedName()
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self.UserWriteMask = 0
        self.References = []
    
    def to_binary(self):
        packet = []
        packet.append(self.NodeId.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.NodeClass))
        packet.append(self.BrowseName.to_binary())
        packet.append(self.DisplayName.to_binary())
        packet.append(self.Description.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.WriteMask))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.UserWriteMask))
        packet.append(struct.pack('<i', len(self.References)))
        for i in self.References:
            packet.append(self.References.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = Node()
        obj.NodeId = NodeId.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.NodeClass = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.BrowseName = QualifiedName.from_binary(data)
        obj.DisplayName = LocalizedText.from_binary(data)
        obj.Description = LocalizedText.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.WriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.UserWriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.References = ReferenceNode.from_binary(data)
        return obj
    
    def __str__(self):
        return 'Node(' + 'NodeId:' + str(self.NodeId) + ', '  + \
             'NodeClass:' + str(self.NodeClass) + ', '  + \
             'BrowseName:' + str(self.BrowseName) + ', '  + \
             'DisplayName:' + str(self.DisplayName) + ', '  + \
             'Description:' + str(self.Description) + ', '  + \
             'WriteMask:' + str(self.WriteMask) + ', '  + \
             'UserWriteMask:' + str(self.UserWriteMask) + ', '  + \
             'References:' + str(self.References) + ')'
    
    __repr__ = __str__
    
class InstanceNode(object):
    def __init__(self):
        self.NodeId = NodeId()
        self.NodeClass = 0
        self.BrowseName = QualifiedName()
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self.UserWriteMask = 0
        self.References = []
    
    def to_binary(self):
        packet = []
        packet.append(self.NodeId.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.NodeClass))
        packet.append(self.BrowseName.to_binary())
        packet.append(self.DisplayName.to_binary())
        packet.append(self.Description.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.WriteMask))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.UserWriteMask))
        packet.append(struct.pack('<i', len(self.References)))
        for i in self.References:
            packet.append(self.References.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = InstanceNode()
        obj.NodeId = NodeId.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.NodeClass = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.BrowseName = QualifiedName.from_binary(data)
        obj.DisplayName = LocalizedText.from_binary(data)
        obj.Description = LocalizedText.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.WriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.UserWriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.References = ReferenceNode.from_binary(data)
        return obj
    
    def __str__(self):
        return 'InstanceNode(' + 'NodeId:' + str(self.NodeId) + ', '  + \
             'NodeClass:' + str(self.NodeClass) + ', '  + \
             'BrowseName:' + str(self.BrowseName) + ', '  + \
             'DisplayName:' + str(self.DisplayName) + ', '  + \
             'Description:' + str(self.Description) + ', '  + \
             'WriteMask:' + str(self.WriteMask) + ', '  + \
             'UserWriteMask:' + str(self.UserWriteMask) + ', '  + \
             'References:' + str(self.References) + ')'
    
    __repr__ = __str__
    
class TypeNode(object):
    def __init__(self):
        self.NodeId = NodeId()
        self.NodeClass = 0
        self.BrowseName = QualifiedName()
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self.UserWriteMask = 0
        self.References = []
    
    def to_binary(self):
        packet = []
        packet.append(self.NodeId.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.NodeClass))
        packet.append(self.BrowseName.to_binary())
        packet.append(self.DisplayName.to_binary())
        packet.append(self.Description.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.WriteMask))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.UserWriteMask))
        packet.append(struct.pack('<i', len(self.References)))
        for i in self.References:
            packet.append(self.References.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = TypeNode()
        obj.NodeId = NodeId.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.NodeClass = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.BrowseName = QualifiedName.from_binary(data)
        obj.DisplayName = LocalizedText.from_binary(data)
        obj.Description = LocalizedText.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.WriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.UserWriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.References = ReferenceNode.from_binary(data)
        return obj
    
    def __str__(self):
        return 'TypeNode(' + 'NodeId:' + str(self.NodeId) + ', '  + \
             'NodeClass:' + str(self.NodeClass) + ', '  + \
             'BrowseName:' + str(self.BrowseName) + ', '  + \
             'DisplayName:' + str(self.DisplayName) + ', '  + \
             'Description:' + str(self.Description) + ', '  + \
             'WriteMask:' + str(self.WriteMask) + ', '  + \
             'UserWriteMask:' + str(self.UserWriteMask) + ', '  + \
             'References:' + str(self.References) + ')'
    
    __repr__ = __str__
    
class ObjectNode(object):
    def __init__(self):
        self.NodeId = NodeId()
        self.NodeClass = 0
        self.BrowseName = QualifiedName()
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self.UserWriteMask = 0
        self.References = []
        self.EventNotifier = 0
    
    def to_binary(self):
        packet = []
        packet.append(self.NodeId.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.NodeClass))
        packet.append(self.BrowseName.to_binary())
        packet.append(self.DisplayName.to_binary())
        packet.append(self.Description.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.WriteMask))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.UserWriteMask))
        packet.append(struct.pack('<i', len(self.References)))
        for i in self.References:
            packet.append(self.References.to_binary())
        fmt = '<B'
        packet.append(struct.pack(fmt, self.EventNotifier))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ObjectNode()
        obj.NodeId = NodeId.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.NodeClass = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.BrowseName = QualifiedName.from_binary(data)
        obj.DisplayName = LocalizedText.from_binary(data)
        obj.Description = LocalizedText.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.WriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.UserWriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.References = ReferenceNode.from_binary(data)
        fmt = '<B'
        fmt_size = 1
        obj.EventNotifier = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'ObjectNode(' + 'NodeId:' + str(self.NodeId) + ', '  + \
             'NodeClass:' + str(self.NodeClass) + ', '  + \
             'BrowseName:' + str(self.BrowseName) + ', '  + \
             'DisplayName:' + str(self.DisplayName) + ', '  + \
             'Description:' + str(self.Description) + ', '  + \
             'WriteMask:' + str(self.WriteMask) + ', '  + \
             'UserWriteMask:' + str(self.UserWriteMask) + ', '  + \
             'References:' + str(self.References) + ', '  + \
             'EventNotifier:' + str(self.EventNotifier) + ')'
    
    __repr__ = __str__
    
class ObjectTypeNode(object):
    def __init__(self):
        self.NodeId = NodeId()
        self.NodeClass = 0
        self.BrowseName = QualifiedName()
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self.UserWriteMask = 0
        self.References = []
        self.IsAbstract = 0
    
    def to_binary(self):
        packet = []
        packet.append(self.NodeId.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.NodeClass))
        packet.append(self.BrowseName.to_binary())
        packet.append(self.DisplayName.to_binary())
        packet.append(self.Description.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.WriteMask))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.UserWriteMask))
        packet.append(struct.pack('<i', len(self.References)))
        for i in self.References:
            packet.append(self.References.to_binary())
        fmt = '<?'
        packet.append(struct.pack(fmt, self.IsAbstract))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ObjectTypeNode()
        obj.NodeId = NodeId.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.NodeClass = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.BrowseName = QualifiedName.from_binary(data)
        obj.DisplayName = LocalizedText.from_binary(data)
        obj.Description = LocalizedText.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.WriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.UserWriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.References = ReferenceNode.from_binary(data)
        fmt = '<?'
        fmt_size = 1
        obj.IsAbstract = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'ObjectTypeNode(' + 'NodeId:' + str(self.NodeId) + ', '  + \
             'NodeClass:' + str(self.NodeClass) + ', '  + \
             'BrowseName:' + str(self.BrowseName) + ', '  + \
             'DisplayName:' + str(self.DisplayName) + ', '  + \
             'Description:' + str(self.Description) + ', '  + \
             'WriteMask:' + str(self.WriteMask) + ', '  + \
             'UserWriteMask:' + str(self.UserWriteMask) + ', '  + \
             'References:' + str(self.References) + ', '  + \
             'IsAbstract:' + str(self.IsAbstract) + ')'
    
    __repr__ = __str__
    
class VariableNode(object):
    def __init__(self):
        self.NodeId = NodeId()
        self.NodeClass = 0
        self.BrowseName = QualifiedName()
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self.UserWriteMask = 0
        self.References = []
        self.Value = Variant()
        self.DataType = NodeId()
        self.ValueRank = 0
        self.ArrayDimensions = []
        self.AccessLevel = 0
        self.UserAccessLevel = 0
        self.MinimumSamplingInterval = 0
        self.Historizing = 0
    
    def to_binary(self):
        packet = []
        packet.append(self.NodeId.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.NodeClass))
        packet.append(self.BrowseName.to_binary())
        packet.append(self.DisplayName.to_binary())
        packet.append(self.Description.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.WriteMask))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.UserWriteMask))
        packet.append(struct.pack('<i', len(self.References)))
        for i in self.References:
            packet.append(self.References.to_binary())
        packet.append(self.Value.to_binary())
        packet.append(self.DataType.to_binary())
        fmt = '<i'
        packet.append(struct.pack(fmt, self.ValueRank))
        packet.append(struct.pack('<i', len(self.ArrayDimensions)))
        for i in self.ArrayDimensions:
            fmt = '<I'
            packet.append(struct.pack(fmt, self.ArrayDimensions))
        fmt = '<B'
        packet.append(struct.pack(fmt, self.AccessLevel))
        fmt = '<B'
        packet.append(struct.pack(fmt, self.UserAccessLevel))
        fmt = '<d'
        packet.append(struct.pack(fmt, self.MinimumSamplingInterval))
        fmt = '<?'
        packet.append(struct.pack(fmt, self.Historizing))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = VariableNode()
        obj.NodeId = NodeId.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.NodeClass = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.BrowseName = QualifiedName.from_binary(data)
        obj.DisplayName = LocalizedText.from_binary(data)
        obj.Description = LocalizedText.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.WriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.UserWriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.References = ReferenceNode.from_binary(data)
        obj.Value = Variant.from_binary(data)
        obj.DataType = NodeId.from_binary(data)
        fmt = '<i'
        fmt_size = 4
        obj.ValueRank = struct.unpack(fmt, data.read(fmt_size))[0]
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                fmt = '<I'
                fmt_size = 4
                obj.ArrayDimensions = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<B'
        fmt_size = 1
        obj.AccessLevel = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<B'
        fmt_size = 1
        obj.UserAccessLevel = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<d'
        fmt_size = 8
        obj.MinimumSamplingInterval = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<?'
        fmt_size = 1
        obj.Historizing = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'VariableNode(' + 'NodeId:' + str(self.NodeId) + ', '  + \
             'NodeClass:' + str(self.NodeClass) + ', '  + \
             'BrowseName:' + str(self.BrowseName) + ', '  + \
             'DisplayName:' + str(self.DisplayName) + ', '  + \
             'Description:' + str(self.Description) + ', '  + \
             'WriteMask:' + str(self.WriteMask) + ', '  + \
             'UserWriteMask:' + str(self.UserWriteMask) + ', '  + \
             'References:' + str(self.References) + ', '  + \
             'Value:' + str(self.Value) + ', '  + \
             'DataType:' + str(self.DataType) + ', '  + \
             'ValueRank:' + str(self.ValueRank) + ', '  + \
             'ArrayDimensions:' + str(self.ArrayDimensions) + ', '  + \
             'AccessLevel:' + str(self.AccessLevel) + ', '  + \
             'UserAccessLevel:' + str(self.UserAccessLevel) + ', '  + \
             'MinimumSamplingInterval:' + str(self.MinimumSamplingInterval) + ', '  + \
             'Historizing:' + str(self.Historizing) + ')'
    
    __repr__ = __str__
    
class VariableTypeNode(object):
    def __init__(self):
        self.NodeId = NodeId()
        self.NodeClass = 0
        self.BrowseName = QualifiedName()
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self.UserWriteMask = 0
        self.References = []
        self.Value = Variant()
        self.DataType = NodeId()
        self.ValueRank = 0
        self.ArrayDimensions = []
        self.IsAbstract = 0
    
    def to_binary(self):
        packet = []
        packet.append(self.NodeId.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.NodeClass))
        packet.append(self.BrowseName.to_binary())
        packet.append(self.DisplayName.to_binary())
        packet.append(self.Description.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.WriteMask))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.UserWriteMask))
        packet.append(struct.pack('<i', len(self.References)))
        for i in self.References:
            packet.append(self.References.to_binary())
        packet.append(self.Value.to_binary())
        packet.append(self.DataType.to_binary())
        fmt = '<i'
        packet.append(struct.pack(fmt, self.ValueRank))
        packet.append(struct.pack('<i', len(self.ArrayDimensions)))
        for i in self.ArrayDimensions:
            fmt = '<I'
            packet.append(struct.pack(fmt, self.ArrayDimensions))
        fmt = '<?'
        packet.append(struct.pack(fmt, self.IsAbstract))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = VariableTypeNode()
        obj.NodeId = NodeId.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.NodeClass = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.BrowseName = QualifiedName.from_binary(data)
        obj.DisplayName = LocalizedText.from_binary(data)
        obj.Description = LocalizedText.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.WriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.UserWriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.References = ReferenceNode.from_binary(data)
        obj.Value = Variant.from_binary(data)
        obj.DataType = NodeId.from_binary(data)
        fmt = '<i'
        fmt_size = 4
        obj.ValueRank = struct.unpack(fmt, data.read(fmt_size))[0]
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                fmt = '<I'
                fmt_size = 4
                obj.ArrayDimensions = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<?'
        fmt_size = 1
        obj.IsAbstract = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'VariableTypeNode(' + 'NodeId:' + str(self.NodeId) + ', '  + \
             'NodeClass:' + str(self.NodeClass) + ', '  + \
             'BrowseName:' + str(self.BrowseName) + ', '  + \
             'DisplayName:' + str(self.DisplayName) + ', '  + \
             'Description:' + str(self.Description) + ', '  + \
             'WriteMask:' + str(self.WriteMask) + ', '  + \
             'UserWriteMask:' + str(self.UserWriteMask) + ', '  + \
             'References:' + str(self.References) + ', '  + \
             'Value:' + str(self.Value) + ', '  + \
             'DataType:' + str(self.DataType) + ', '  + \
             'ValueRank:' + str(self.ValueRank) + ', '  + \
             'ArrayDimensions:' + str(self.ArrayDimensions) + ', '  + \
             'IsAbstract:' + str(self.IsAbstract) + ')'
    
    __repr__ = __str__
    
class ReferenceTypeNode(object):
    def __init__(self):
        self.NodeId = NodeId()
        self.NodeClass = 0
        self.BrowseName = QualifiedName()
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self.UserWriteMask = 0
        self.References = []
        self.IsAbstract = 0
        self.Symmetric = 0
        self.InverseName = LocalizedText()
    
    def to_binary(self):
        packet = []
        packet.append(self.NodeId.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.NodeClass))
        packet.append(self.BrowseName.to_binary())
        packet.append(self.DisplayName.to_binary())
        packet.append(self.Description.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.WriteMask))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.UserWriteMask))
        packet.append(struct.pack('<i', len(self.References)))
        for i in self.References:
            packet.append(self.References.to_binary())
        fmt = '<?'
        packet.append(struct.pack(fmt, self.IsAbstract))
        fmt = '<?'
        packet.append(struct.pack(fmt, self.Symmetric))
        packet.append(self.InverseName.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ReferenceTypeNode()
        obj.NodeId = NodeId.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.NodeClass = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.BrowseName = QualifiedName.from_binary(data)
        obj.DisplayName = LocalizedText.from_binary(data)
        obj.Description = LocalizedText.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.WriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.UserWriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.References = ReferenceNode.from_binary(data)
        fmt = '<?'
        fmt_size = 1
        obj.IsAbstract = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<?'
        fmt_size = 1
        obj.Symmetric = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.InverseName = LocalizedText.from_binary(data)
        return obj
    
    def __str__(self):
        return 'ReferenceTypeNode(' + 'NodeId:' + str(self.NodeId) + ', '  + \
             'NodeClass:' + str(self.NodeClass) + ', '  + \
             'BrowseName:' + str(self.BrowseName) + ', '  + \
             'DisplayName:' + str(self.DisplayName) + ', '  + \
             'Description:' + str(self.Description) + ', '  + \
             'WriteMask:' + str(self.WriteMask) + ', '  + \
             'UserWriteMask:' + str(self.UserWriteMask) + ', '  + \
             'References:' + str(self.References) + ', '  + \
             'IsAbstract:' + str(self.IsAbstract) + ', '  + \
             'Symmetric:' + str(self.Symmetric) + ', '  + \
             'InverseName:' + str(self.InverseName) + ')'
    
    __repr__ = __str__
    
class MethodNode(object):
    def __init__(self):
        self.NodeId = NodeId()
        self.NodeClass = 0
        self.BrowseName = QualifiedName()
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self.UserWriteMask = 0
        self.References = []
        self.Executable = 0
        self.UserExecutable = 0
    
    def to_binary(self):
        packet = []
        packet.append(self.NodeId.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.NodeClass))
        packet.append(self.BrowseName.to_binary())
        packet.append(self.DisplayName.to_binary())
        packet.append(self.Description.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.WriteMask))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.UserWriteMask))
        packet.append(struct.pack('<i', len(self.References)))
        for i in self.References:
            packet.append(self.References.to_binary())
        fmt = '<?'
        packet.append(struct.pack(fmt, self.Executable))
        fmt = '<?'
        packet.append(struct.pack(fmt, self.UserExecutable))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = MethodNode()
        obj.NodeId = NodeId.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.NodeClass = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.BrowseName = QualifiedName.from_binary(data)
        obj.DisplayName = LocalizedText.from_binary(data)
        obj.Description = LocalizedText.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.WriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.UserWriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.References = ReferenceNode.from_binary(data)
        fmt = '<?'
        fmt_size = 1
        obj.Executable = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<?'
        fmt_size = 1
        obj.UserExecutable = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'MethodNode(' + 'NodeId:' + str(self.NodeId) + ', '  + \
             'NodeClass:' + str(self.NodeClass) + ', '  + \
             'BrowseName:' + str(self.BrowseName) + ', '  + \
             'DisplayName:' + str(self.DisplayName) + ', '  + \
             'Description:' + str(self.Description) + ', '  + \
             'WriteMask:' + str(self.WriteMask) + ', '  + \
             'UserWriteMask:' + str(self.UserWriteMask) + ', '  + \
             'References:' + str(self.References) + ', '  + \
             'Executable:' + str(self.Executable) + ', '  + \
             'UserExecutable:' + str(self.UserExecutable) + ')'
    
    __repr__ = __str__
    
class ViewNode(object):
    def __init__(self):
        self.NodeId = NodeId()
        self.NodeClass = 0
        self.BrowseName = QualifiedName()
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self.UserWriteMask = 0
        self.References = []
        self.ContainsNoLoops = 0
        self.EventNotifier = 0
    
    def to_binary(self):
        packet = []
        packet.append(self.NodeId.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.NodeClass))
        packet.append(self.BrowseName.to_binary())
        packet.append(self.DisplayName.to_binary())
        packet.append(self.Description.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.WriteMask))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.UserWriteMask))
        packet.append(struct.pack('<i', len(self.References)))
        for i in self.References:
            packet.append(self.References.to_binary())
        fmt = '<?'
        packet.append(struct.pack(fmt, self.ContainsNoLoops))
        fmt = '<B'
        packet.append(struct.pack(fmt, self.EventNotifier))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ViewNode()
        obj.NodeId = NodeId.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.NodeClass = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.BrowseName = QualifiedName.from_binary(data)
        obj.DisplayName = LocalizedText.from_binary(data)
        obj.Description = LocalizedText.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.WriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.UserWriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.References = ReferenceNode.from_binary(data)
        fmt = '<?'
        fmt_size = 1
        obj.ContainsNoLoops = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<B'
        fmt_size = 1
        obj.EventNotifier = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'ViewNode(' + 'NodeId:' + str(self.NodeId) + ', '  + \
             'NodeClass:' + str(self.NodeClass) + ', '  + \
             'BrowseName:' + str(self.BrowseName) + ', '  + \
             'DisplayName:' + str(self.DisplayName) + ', '  + \
             'Description:' + str(self.Description) + ', '  + \
             'WriteMask:' + str(self.WriteMask) + ', '  + \
             'UserWriteMask:' + str(self.UserWriteMask) + ', '  + \
             'References:' + str(self.References) + ', '  + \
             'ContainsNoLoops:' + str(self.ContainsNoLoops) + ', '  + \
             'EventNotifier:' + str(self.EventNotifier) + ')'
    
    __repr__ = __str__
    
class DataTypeNode(object):
    def __init__(self):
        self.NodeId = NodeId()
        self.NodeClass = 0
        self.BrowseName = QualifiedName()
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self.UserWriteMask = 0
        self.References = []
        self.IsAbstract = 0
    
    def to_binary(self):
        packet = []
        packet.append(self.NodeId.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.NodeClass))
        packet.append(self.BrowseName.to_binary())
        packet.append(self.DisplayName.to_binary())
        packet.append(self.Description.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.WriteMask))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.UserWriteMask))
        packet.append(struct.pack('<i', len(self.References)))
        for i in self.References:
            packet.append(self.References.to_binary())
        fmt = '<?'
        packet.append(struct.pack(fmt, self.IsAbstract))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = DataTypeNode()
        obj.NodeId = NodeId.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.NodeClass = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.BrowseName = QualifiedName.from_binary(data)
        obj.DisplayName = LocalizedText.from_binary(data)
        obj.Description = LocalizedText.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.WriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.UserWriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.References = ReferenceNode.from_binary(data)
        fmt = '<?'
        fmt_size = 1
        obj.IsAbstract = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'DataTypeNode(' + 'NodeId:' + str(self.NodeId) + ', '  + \
             'NodeClass:' + str(self.NodeClass) + ', '  + \
             'BrowseName:' + str(self.BrowseName) + ', '  + \
             'DisplayName:' + str(self.DisplayName) + ', '  + \
             'Description:' + str(self.Description) + ', '  + \
             'WriteMask:' + str(self.WriteMask) + ', '  + \
             'UserWriteMask:' + str(self.UserWriteMask) + ', '  + \
             'References:' + str(self.References) + ', '  + \
             'IsAbstract:' + str(self.IsAbstract) + ')'
    
    __repr__ = __str__
    
class ReferenceNode(object):
    def __init__(self):
        self.ReferenceTypeId = NodeId()
        self.IsInverse = 0
        self.TargetId = ExpandedNodeId()
    
    def to_binary(self):
        packet = []
        packet.append(self.ReferenceTypeId.to_binary())
        fmt = '<?'
        packet.append(struct.pack(fmt, self.IsInverse))
        packet.append(self.TargetId.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ReferenceNode()
        obj.ReferenceTypeId = NodeId.from_binary(data)
        fmt = '<?'
        fmt_size = 1
        obj.IsInverse = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.TargetId = ExpandedNodeId.from_binary(data)
        return obj
    
    def __str__(self):
        return 'ReferenceNode(' + 'ReferenceTypeId:' + str(self.ReferenceTypeId) + ', '  + \
             'IsInverse:' + str(self.IsInverse) + ', '  + \
             'TargetId:' + str(self.TargetId) + ')'
    
    __repr__ = __str__
    
class Argument(object):
    def __init__(self):
        self.Name = ''
        self.DataType = NodeId()
        self.ValueRank = 0
        self.ArrayDimensions = []
        self.Description = LocalizedText()
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.Name)))
        packet.append(struct.pack('<{}s'.format(len(self.Name)), self.Name.encode()))
        packet.append(self.DataType.to_binary())
        fmt = '<i'
        packet.append(struct.pack(fmt, self.ValueRank))
        packet.append(struct.pack('<i', len(self.ArrayDimensions)))
        for i in self.ArrayDimensions:
            fmt = '<I'
            packet.append(struct.pack(fmt, self.ArrayDimensions))
        packet.append(self.Description.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = Argument()
        slength = struct.unpack('<i', data.red(1))
        obj.Name = struct.unpack('<{}s'.format(slength), data.read(slength))
        obj.DataType = NodeId.from_binary(data)
        fmt = '<i'
        fmt_size = 4
        obj.ValueRank = struct.unpack(fmt, data.read(fmt_size))[0]
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                fmt = '<I'
                fmt_size = 4
                obj.ArrayDimensions = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.Description = LocalizedText.from_binary(data)
        return obj
    
    def __str__(self):
        return 'Argument(' + 'Name:' + str(self.Name) + ', '  + \
             'DataType:' + str(self.DataType) + ', '  + \
             'ValueRank:' + str(self.ValueRank) + ', '  + \
             'ArrayDimensions:' + str(self.ArrayDimensions) + ', '  + \
             'Description:' + str(self.Description) + ')'
    
    __repr__ = __str__
    
class EnumValueType(object):
    def __init__(self):
        self.Value = 0
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
    
    def to_binary(self):
        packet = []
        fmt = '<q'
        packet.append(struct.pack(fmt, self.Value))
        packet.append(self.DisplayName.to_binary())
        packet.append(self.Description.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = EnumValueType()
        fmt = '<q'
        fmt_size = 8
        obj.Value = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.DisplayName = LocalizedText.from_binary(data)
        obj.Description = LocalizedText.from_binary(data)
        return obj
    
    def __str__(self):
        return 'EnumValueType(' + 'Value:' + str(self.Value) + ', '  + \
             'DisplayName:' + str(self.DisplayName) + ', '  + \
             'Description:' + str(self.Description) + ')'
    
    __repr__ = __str__
    
class TimeZoneDataType(object):
    def __init__(self):
        self.Offset = 0
        self.DaylightSavingInOffset = 0
    
    def to_binary(self):
        packet = []
        fmt = '<h'
        packet.append(struct.pack(fmt, self.Offset))
        fmt = '<?'
        packet.append(struct.pack(fmt, self.DaylightSavingInOffset))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = TimeZoneDataType()
        fmt = '<h'
        fmt_size = 2
        obj.Offset = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<?'
        fmt_size = 1
        obj.DaylightSavingInOffset = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'TimeZoneDataType(' + 'Offset:' + str(self.Offset) + ', '  + \
             'DaylightSavingInOffset:' + str(self.DaylightSavingInOffset) + ')'
    
    __repr__ = __str__
    
class ApplicationDescription(object):
    def __init__(self):
        self.ApplicationUri = ''
        self.ProductUri = ''
        self.ApplicationName = LocalizedText()
        self.ApplicationType = 0
        self.GatewayServerUri = ''
        self.DiscoveryProfileUri = ''
        self.DiscoveryUrls = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.ApplicationUri)))
        packet.append(struct.pack('<{}s'.format(len(self.ApplicationUri)), self.ApplicationUri.encode()))
        packet.append(struct.pack('<i', len(self.ProductUri)))
        packet.append(struct.pack('<{}s'.format(len(self.ProductUri)), self.ProductUri.encode()))
        packet.append(self.ApplicationName.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.ApplicationType))
        packet.append(struct.pack('<i', len(self.GatewayServerUri)))
        packet.append(struct.pack('<{}s'.format(len(self.GatewayServerUri)), self.GatewayServerUri.encode()))
        packet.append(struct.pack('<i', len(self.DiscoveryProfileUri)))
        packet.append(struct.pack('<{}s'.format(len(self.DiscoveryProfileUri)), self.DiscoveryProfileUri.encode()))
        packet.append(struct.pack('<i', len(self.DiscoveryUrls)))
        for i in self.DiscoveryUrls:
            packet.append(struct.pack('<i', len(self.DiscoveryUrls)))
            packet.append(struct.pack('<{}s'.format(len(self.DiscoveryUrls)), self.DiscoveryUrls.encode()))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ApplicationDescription()
        slength = struct.unpack('<i', data.red(1))
        obj.ApplicationUri = struct.unpack('<{}s'.format(slength), data.read(slength))
        slength = struct.unpack('<i', data.red(1))
        obj.ProductUri = struct.unpack('<{}s'.format(slength), data.read(slength))
        obj.ApplicationName = LocalizedText.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.ApplicationType = struct.unpack(fmt, data.read(fmt_size))[0]
        slength = struct.unpack('<i', data.red(1))
        obj.GatewayServerUri = struct.unpack('<{}s'.format(slength), data.read(slength))
        slength = struct.unpack('<i', data.red(1))
        obj.DiscoveryProfileUri = struct.unpack('<{}s'.format(slength), data.read(slength))
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                slength = struct.unpack('<i', data.red(1))
                obj.DiscoveryUrls = struct.unpack('<{}s'.format(slength), data.read(slength))
        return obj
    
    def __str__(self):
        return 'ApplicationDescription(' + 'ApplicationUri:' + str(self.ApplicationUri) + ', '  + \
             'ProductUri:' + str(self.ProductUri) + ', '  + \
             'ApplicationName:' + str(self.ApplicationName) + ', '  + \
             'ApplicationType:' + str(self.ApplicationType) + ', '  + \
             'GatewayServerUri:' + str(self.GatewayServerUri) + ', '  + \
             'DiscoveryProfileUri:' + str(self.DiscoveryProfileUri) + ', '  + \
             'DiscoveryUrls:' + str(self.DiscoveryUrls) + ')'
    
    __repr__ = __str__
    
class RequestHeader(object):
    def __init__(self):
        self.AuthenticationToken = NodeId()
        self.Timestamp = DateTime()
        self.RequestHandle = 0
        self.ReturnDiagnostics = 0
        self.AuditEntryId = ''
        self.TimeoutHint = 0
        self.AdditionalHeader = ExtensionObject()
    
    def to_binary(self):
        packet = []
        packet.append(self.AuthenticationToken.to_binary())
        packet.append(self.Timestamp.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.RequestHandle))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.ReturnDiagnostics))
        packet.append(struct.pack('<i', len(self.AuditEntryId)))
        packet.append(struct.pack('<{}s'.format(len(self.AuditEntryId)), self.AuditEntryId.encode()))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.TimeoutHint))
        packet.append(self.AdditionalHeader.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = RequestHeader()
        obj.AuthenticationToken = NodeId.from_binary(data)
        obj.Timestamp = DateTime.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.RequestHandle = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.ReturnDiagnostics = struct.unpack(fmt, data.read(fmt_size))[0]
        slength = struct.unpack('<i', data.red(1))
        obj.AuditEntryId = struct.unpack('<{}s'.format(slength), data.read(slength))
        fmt = '<I'
        fmt_size = 4
        obj.TimeoutHint = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.AdditionalHeader = ExtensionObject.from_binary(data)
        return obj
    
    def __str__(self):
        return 'RequestHeader(' + 'AuthenticationToken:' + str(self.AuthenticationToken) + ', '  + \
             'Timestamp:' + str(self.Timestamp) + ', '  + \
             'RequestHandle:' + str(self.RequestHandle) + ', '  + \
             'ReturnDiagnostics:' + str(self.ReturnDiagnostics) + ', '  + \
             'AuditEntryId:' + str(self.AuditEntryId) + ', '  + \
             'TimeoutHint:' + str(self.TimeoutHint) + ', '  + \
             'AdditionalHeader:' + str(self.AdditionalHeader) + ')'
    
    __repr__ = __str__
    
class ResponseHeader(object):
    def __init__(self):
        self.Timestamp = DateTime()
        self.RequestHandle = 0
        self.ServiceResult = StatusCode()
        self.ServiceDiagnostics = DiagnosticInfo()
        self.StringTable = []
        self.AdditionalHeader = ExtensionObject()
    
    def to_binary(self):
        packet = []
        packet.append(self.Timestamp.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.RequestHandle))
        packet.append(self.ServiceResult.to_binary())
        packet.append(self.ServiceDiagnostics.to_binary())
        packet.append(struct.pack('<i', len(self.StringTable)))
        for i in self.StringTable:
            packet.append(struct.pack('<i', len(self.StringTable)))
            packet.append(struct.pack('<{}s'.format(len(self.StringTable)), self.StringTable.encode()))
        packet.append(self.AdditionalHeader.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ResponseHeader()
        obj.Timestamp = DateTime.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.RequestHandle = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.ServiceResult = StatusCode.from_binary(data)
        obj.ServiceDiagnostics = DiagnosticInfo.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                slength = struct.unpack('<i', data.red(1))
                obj.StringTable = struct.unpack('<{}s'.format(slength), data.read(slength))
        obj.AdditionalHeader = ExtensionObject.from_binary(data)
        return obj
    
    def __str__(self):
        return 'ResponseHeader(' + 'Timestamp:' + str(self.Timestamp) + ', '  + \
             'RequestHandle:' + str(self.RequestHandle) + ', '  + \
             'ServiceResult:' + str(self.ServiceResult) + ', '  + \
             'ServiceDiagnostics:' + str(self.ServiceDiagnostics) + ', '  + \
             'StringTable:' + str(self.StringTable) + ', '  + \
             'AdditionalHeader:' + str(self.AdditionalHeader) + ')'
    
    __repr__ = __str__
    
class ServiceFault(object):
    def __init__(self):
        self.ResponseHeader = ResponseHeader()
    
    def to_binary(self):
        packet = []
        packet.append(self.ResponseHeader.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ServiceFault()
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        return obj
    
    def __str__(self):
        return 'ServiceFault(' + 'ResponseHeader:' + str(self.ResponseHeader) + ')'
    
    __repr__ = __str__
    
class FindServersParameters(object):
    def __init__(self):
        self.EndpointUrl = ''
        self.LocaleIds = []
        self.ServerUris = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.EndpointUrl)))
        packet.append(struct.pack('<{}s'.format(len(self.EndpointUrl)), self.EndpointUrl.encode()))
        packet.append(struct.pack('<i', len(self.LocaleIds)))
        for i in self.LocaleIds:
            packet.append(struct.pack('<i', len(self.LocaleIds)))
            packet.append(struct.pack('<{}s'.format(len(self.LocaleIds)), self.LocaleIds.encode()))
        packet.append(struct.pack('<i', len(self.ServerUris)))
        for i in self.ServerUris:
            packet.append(struct.pack('<i', len(self.ServerUris)))
            packet.append(struct.pack('<{}s'.format(len(self.ServerUris)), self.ServerUris.encode()))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = FindServersParameters()
        slength = struct.unpack('<i', data.red(1))
        obj.EndpointUrl = struct.unpack('<{}s'.format(slength), data.read(slength))
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                slength = struct.unpack('<i', data.red(1))
                obj.LocaleIds = struct.unpack('<{}s'.format(slength), data.read(slength))
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                slength = struct.unpack('<i', data.red(1))
                obj.ServerUris = struct.unpack('<{}s'.format(slength), data.read(slength))
        return obj
    
    def __str__(self):
        return 'FindServersParameters(' + 'EndpointUrl:' + str(self.EndpointUrl) + ', '  + \
             'LocaleIds:' + str(self.LocaleIds) + ', '  + \
             'ServerUris:' + str(self.ServerUris) + ')'
    
    __repr__ = __str__
    
class FindServersRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.FindServersRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
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
        obj = FindServersRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = FindServersParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'FindServersRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class FindServersResult(object):
    def __init__(self):
        self.Servers = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.Servers)))
        for i in self.Servers:
            packet.append(self.Servers.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = FindServersResult()
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.Servers = ApplicationDescription.from_binary(data)
        return obj
    
    def __str__(self):
        return 'FindServersResult(' + 'Servers:' + str(self.Servers) + ')'
    
    __repr__ = __str__
    
class FindServersResponse(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.FindServersResponse_Encoding_DefaultBinary, NodeIdType.FourByte)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = FindServersResult()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = FindServersResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = FindServersResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'FindServersResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class UserTokenPolicy(object):
    def __init__(self):
        self.PolicyId = ''
        self.TokenType = 0
        self.IssuedTokenType = ''
        self.IssuerEndpointUrl = ''
        self.SecurityPolicyUri = ''
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.PolicyId)))
        packet.append(struct.pack('<{}s'.format(len(self.PolicyId)), self.PolicyId.encode()))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.TokenType))
        packet.append(struct.pack('<i', len(self.IssuedTokenType)))
        packet.append(struct.pack('<{}s'.format(len(self.IssuedTokenType)), self.IssuedTokenType.encode()))
        packet.append(struct.pack('<i', len(self.IssuerEndpointUrl)))
        packet.append(struct.pack('<{}s'.format(len(self.IssuerEndpointUrl)), self.IssuerEndpointUrl.encode()))
        packet.append(struct.pack('<i', len(self.SecurityPolicyUri)))
        packet.append(struct.pack('<{}s'.format(len(self.SecurityPolicyUri)), self.SecurityPolicyUri.encode()))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = UserTokenPolicy()
        slength = struct.unpack('<i', data.red(1))
        obj.PolicyId = struct.unpack('<{}s'.format(slength), data.read(slength))
        fmt = '<I'
        fmt_size = 4
        obj.TokenType = struct.unpack(fmt, data.read(fmt_size))[0]
        slength = struct.unpack('<i', data.red(1))
        obj.IssuedTokenType = struct.unpack('<{}s'.format(slength), data.read(slength))
        slength = struct.unpack('<i', data.red(1))
        obj.IssuerEndpointUrl = struct.unpack('<{}s'.format(slength), data.read(slength))
        slength = struct.unpack('<i', data.red(1))
        obj.SecurityPolicyUri = struct.unpack('<{}s'.format(slength), data.read(slength))
        return obj
    
    def __str__(self):
        return 'UserTokenPolicy(' + 'PolicyId:' + str(self.PolicyId) + ', '  + \
             'TokenType:' + str(self.TokenType) + ', '  + \
             'IssuedTokenType:' + str(self.IssuedTokenType) + ', '  + \
             'IssuerEndpointUrl:' + str(self.IssuerEndpointUrl) + ', '  + \
             'SecurityPolicyUri:' + str(self.SecurityPolicyUri) + ')'
    
    __repr__ = __str__
    
class EndpointDescription(object):
    def __init__(self):
        self.EndpointUrl = ''
        self.Server = ApplicationDescription()
        self.ServerCertificate = ByteString()
        self.SecurityMode = 0
        self.SecurityPolicyUri = ''
        self.UserIdentityTokens = []
        self.TransportProfileUri = ''
        self.SecurityLevel = 0
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.EndpointUrl)))
        packet.append(struct.pack('<{}s'.format(len(self.EndpointUrl)), self.EndpointUrl.encode()))
        packet.append(self.Server.to_binary())
        packet.append(self.ServerCertificate.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.SecurityMode))
        packet.append(struct.pack('<i', len(self.SecurityPolicyUri)))
        packet.append(struct.pack('<{}s'.format(len(self.SecurityPolicyUri)), self.SecurityPolicyUri.encode()))
        packet.append(struct.pack('<i', len(self.UserIdentityTokens)))
        for i in self.UserIdentityTokens:
            packet.append(self.UserIdentityTokens.to_binary())
        packet.append(struct.pack('<i', len(self.TransportProfileUri)))
        packet.append(struct.pack('<{}s'.format(len(self.TransportProfileUri)), self.TransportProfileUri.encode()))
        fmt = '<B'
        packet.append(struct.pack(fmt, self.SecurityLevel))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = EndpointDescription()
        slength = struct.unpack('<i', data.red(1))
        obj.EndpointUrl = struct.unpack('<{}s'.format(slength), data.read(slength))
        obj.Server = ApplicationDescription.from_binary(data)
        obj.ServerCertificate = ByteString.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.SecurityMode = struct.unpack(fmt, data.read(fmt_size))[0]
        slength = struct.unpack('<i', data.red(1))
        obj.SecurityPolicyUri = struct.unpack('<{}s'.format(slength), data.read(slength))
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.UserIdentityTokens = UserTokenPolicy.from_binary(data)
        slength = struct.unpack('<i', data.red(1))
        obj.TransportProfileUri = struct.unpack('<{}s'.format(slength), data.read(slength))
        fmt = '<B'
        fmt_size = 1
        obj.SecurityLevel = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'EndpointDescription(' + 'EndpointUrl:' + str(self.EndpointUrl) + ', '  + \
             'Server:' + str(self.Server) + ', '  + \
             'ServerCertificate:' + str(self.ServerCertificate) + ', '  + \
             'SecurityMode:' + str(self.SecurityMode) + ', '  + \
             'SecurityPolicyUri:' + str(self.SecurityPolicyUri) + ', '  + \
             'UserIdentityTokens:' + str(self.UserIdentityTokens) + ', '  + \
             'TransportProfileUri:' + str(self.TransportProfileUri) + ', '  + \
             'SecurityLevel:' + str(self.SecurityLevel) + ')'
    
    __repr__ = __str__
    
class GetEndpointsParameters(object):
    def __init__(self):
        self.EndpointUrl = ''
        self.LocaleIds = []
        self.ProfileUris = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.EndpointUrl)))
        packet.append(struct.pack('<{}s'.format(len(self.EndpointUrl)), self.EndpointUrl.encode()))
        packet.append(struct.pack('<i', len(self.LocaleIds)))
        for i in self.LocaleIds:
            packet.append(struct.pack('<i', len(self.LocaleIds)))
            packet.append(struct.pack('<{}s'.format(len(self.LocaleIds)), self.LocaleIds.encode()))
        packet.append(struct.pack('<i', len(self.ProfileUris)))
        for i in self.ProfileUris:
            packet.append(struct.pack('<i', len(self.ProfileUris)))
            packet.append(struct.pack('<{}s'.format(len(self.ProfileUris)), self.ProfileUris.encode()))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = GetEndpointsParameters()
        slength = struct.unpack('<i', data.red(1))
        obj.EndpointUrl = struct.unpack('<{}s'.format(slength), data.read(slength))
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                slength = struct.unpack('<i', data.red(1))
                obj.LocaleIds = struct.unpack('<{}s'.format(slength), data.read(slength))
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                slength = struct.unpack('<i', data.red(1))
                obj.ProfileUris = struct.unpack('<{}s'.format(slength), data.read(slength))
        return obj
    
    def __str__(self):
        return 'GetEndpointsParameters(' + 'EndpointUrl:' + str(self.EndpointUrl) + ', '  + \
             'LocaleIds:' + str(self.LocaleIds) + ', '  + \
             'ProfileUris:' + str(self.ProfileUris) + ')'
    
    __repr__ = __str__
    
class GetEndpointsRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.GetEndpointsRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
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
        obj = GetEndpointsRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = GetEndpointsParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'GetEndpointsRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class GetEndpointsResponse(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.GetEndpointsResponse_Encoding_DefaultBinary, NodeIdType.FourByte)
        self.ResponseHeader = ResponseHeader()
        self.Endpoints = []
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(struct.pack('<i', len(self.Endpoints)))
        for i in self.Endpoints:
            packet.append(self.Endpoints.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = GetEndpointsResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.Endpoints = EndpointDescription.from_binary(data)
        return obj
    
    def __str__(self):
        return 'GetEndpointsResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Endpoints:' + str(self.Endpoints) + ')'
    
    __repr__ = __str__
    
class RegisteredServer(object):
    def __init__(self):
        self.ServerUri = ''
        self.ProductUri = ''
        self.ServerNames = []
        self.ServerType = 0
        self.GatewayServerUri = ''
        self.DiscoveryUrls = []
        self.SemaphoreFilePath = ''
        self.IsOnline = 0
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.ServerUri)))
        packet.append(struct.pack('<{}s'.format(len(self.ServerUri)), self.ServerUri.encode()))
        packet.append(struct.pack('<i', len(self.ProductUri)))
        packet.append(struct.pack('<{}s'.format(len(self.ProductUri)), self.ProductUri.encode()))
        packet.append(struct.pack('<i', len(self.ServerNames)))
        for i in self.ServerNames:
            packet.append(self.ServerNames.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.ServerType))
        packet.append(struct.pack('<i', len(self.GatewayServerUri)))
        packet.append(struct.pack('<{}s'.format(len(self.GatewayServerUri)), self.GatewayServerUri.encode()))
        packet.append(struct.pack('<i', len(self.DiscoveryUrls)))
        for i in self.DiscoveryUrls:
            packet.append(struct.pack('<i', len(self.DiscoveryUrls)))
            packet.append(struct.pack('<{}s'.format(len(self.DiscoveryUrls)), self.DiscoveryUrls.encode()))
        packet.append(struct.pack('<i', len(self.SemaphoreFilePath)))
        packet.append(struct.pack('<{}s'.format(len(self.SemaphoreFilePath)), self.SemaphoreFilePath.encode()))
        fmt = '<?'
        packet.append(struct.pack(fmt, self.IsOnline))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = RegisteredServer()
        slength = struct.unpack('<i', data.red(1))
        obj.ServerUri = struct.unpack('<{}s'.format(slength), data.read(slength))
        slength = struct.unpack('<i', data.red(1))
        obj.ProductUri = struct.unpack('<{}s'.format(slength), data.read(slength))
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.ServerNames = LocalizedText.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.ServerType = struct.unpack(fmt, data.read(fmt_size))[0]
        slength = struct.unpack('<i', data.red(1))
        obj.GatewayServerUri = struct.unpack('<{}s'.format(slength), data.read(slength))
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                slength = struct.unpack('<i', data.red(1))
                obj.DiscoveryUrls = struct.unpack('<{}s'.format(slength), data.read(slength))
        slength = struct.unpack('<i', data.red(1))
        obj.SemaphoreFilePath = struct.unpack('<{}s'.format(slength), data.read(slength))
        fmt = '<?'
        fmt_size = 1
        obj.IsOnline = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'RegisteredServer(' + 'ServerUri:' + str(self.ServerUri) + ', '  + \
             'ProductUri:' + str(self.ProductUri) + ', '  + \
             'ServerNames:' + str(self.ServerNames) + ', '  + \
             'ServerType:' + str(self.ServerType) + ', '  + \
             'GatewayServerUri:' + str(self.GatewayServerUri) + ', '  + \
             'DiscoveryUrls:' + str(self.DiscoveryUrls) + ', '  + \
             'SemaphoreFilePath:' + str(self.SemaphoreFilePath) + ', '  + \
             'IsOnline:' + str(self.IsOnline) + ')'
    
    __repr__ = __str__
    
class RegisterServerParameters(object):
    def __init__(self):
        self.Server = RegisteredServer()
    
    def to_binary(self):
        packet = []
        packet.append(self.Server.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = RegisterServerParameters()
        obj.Server = RegisteredServer.from_binary(data)
        return obj
    
    def __str__(self):
        return 'RegisterServerParameters(' + 'Server:' + str(self.Server) + ')'
    
    __repr__ = __str__
    
class RegisterServerRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.RegisterServerRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
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
        obj = RegisterServerRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = RegisterServerParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'RegisterServerRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class RegisterServerResponse(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.RegisterServerResponse_Encoding_DefaultBinary, NodeIdType.FourByte)
        self.ResponseHeader = ResponseHeader()
    
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
        return 'RegisterServerResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ')'
    
    __repr__ = __str__
    
class ChannelSecurityToken(object):
    def __init__(self):
        self.ChannelId = 0
        self.TokenId = 0
        self.CreatedAt = DateTime()
        self.RevisedLifetime = 0
    
    def to_binary(self):
        packet = []
        fmt = '<I'
        packet.append(struct.pack(fmt, self.ChannelId))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.TokenId))
        packet.append(self.CreatedAt.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.RevisedLifetime))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ChannelSecurityToken()
        fmt = '<I'
        fmt_size = 4
        obj.ChannelId = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.TokenId = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.CreatedAt = DateTime.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.RevisedLifetime = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'ChannelSecurityToken(' + 'ChannelId:' + str(self.ChannelId) + ', '  + \
             'TokenId:' + str(self.TokenId) + ', '  + \
             'CreatedAt:' + str(self.CreatedAt) + ', '  + \
             'RevisedLifetime:' + str(self.RevisedLifetime) + ')'
    
    __repr__ = __str__
    
class OpenSecureChannelParameters(object):
    def __init__(self):
        self.ClientProtocolVersion = 0
        self.RequestType = 0
        self.SecurityMode = 0
        self.ClientNonce = ByteString()
        self.RequestedLifetime = 0
    
    def to_binary(self):
        packet = []
        fmt = '<I'
        packet.append(struct.pack(fmt, self.ClientProtocolVersion))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.RequestType))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.SecurityMode))
        packet.append(self.ClientNonce.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.RequestedLifetime))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = OpenSecureChannelParameters()
        fmt = '<I'
        fmt_size = 4
        obj.ClientProtocolVersion = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.RequestType = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.SecurityMode = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.ClientNonce = ByteString.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.RequestedLifetime = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'OpenSecureChannelParameters(' + 'ClientProtocolVersion:' + str(self.ClientProtocolVersion) + ', '  + \
             'RequestType:' + str(self.RequestType) + ', '  + \
             'SecurityMode:' + str(self.SecurityMode) + ', '  + \
             'ClientNonce:' + str(self.ClientNonce) + ', '  + \
             'RequestedLifetime:' + str(self.RequestedLifetime) + ')'
    
    __repr__ = __str__
    
class OpenSecureChannelRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.OpenSecureChannelRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
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
        obj = OpenSecureChannelRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = OpenSecureChannelParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'OpenSecureChannelRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class OpenSecureChannelResult(object):
    def __init__(self):
        self.ServerProtocolVersion = 0
        self.SecurityToken = ChannelSecurityToken()
        self.ServerNonce = ByteString()
    
    def to_binary(self):
        packet = []
        fmt = '<I'
        packet.append(struct.pack(fmt, self.ServerProtocolVersion))
        packet.append(self.SecurityToken.to_binary())
        packet.append(self.ServerNonce.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = OpenSecureChannelResult()
        fmt = '<I'
        fmt_size = 4
        obj.ServerProtocolVersion = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.SecurityToken = ChannelSecurityToken.from_binary(data)
        obj.ServerNonce = ByteString.from_binary(data)
        return obj
    
    def __str__(self):
        return 'OpenSecureChannelResult(' + 'ServerProtocolVersion:' + str(self.ServerProtocolVersion) + ', '  + \
             'SecurityToken:' + str(self.SecurityToken) + ', '  + \
             'ServerNonce:' + str(self.ServerNonce) + ')'
    
    __repr__ = __str__
    
class OpenSecureChannelResponse(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.OpenSecureChannelResponse_Encoding_DefaultBinary, NodeIdType.FourByte)
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
        obj = OpenSecureChannelResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        print(obj.ResponseHeader)
        obj.Parameters = OpenSecureChannelResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'OpenSecureChannelResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class CloseSecureChannelRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.CloseSecureChannelRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
        self.RequestHeader = RequestHeader()
    
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
        return 'CloseSecureChannelRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ')'
    
    __repr__ = __str__
    
class CloseSecureChannelResponse(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.CloseSecureChannelResponse_Encoding_DefaultBinary, NodeIdType.FourByte)
        self.ResponseHeader = ResponseHeader()
    
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
        return 'CloseSecureChannelResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ')'
    
    __repr__ = __str__
    
class SignedSoftwareCertificate(object):
    def __init__(self):
        self.CertificateData = ByteString()
        self.Signature = ByteString()
    
    def to_binary(self):
        packet = []
        packet.append(self.CertificateData.to_binary())
        packet.append(self.Signature.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = SignedSoftwareCertificate()
        obj.CertificateData = ByteString.from_binary(data)
        obj.Signature = ByteString.from_binary(data)
        return obj
    
    def __str__(self):
        return 'SignedSoftwareCertificate(' + 'CertificateData:' + str(self.CertificateData) + ', '  + \
             'Signature:' + str(self.Signature) + ')'
    
    __repr__ = __str__
    
class SignatureData(object):
    def __init__(self):
        self.Algorithm = ''
        self.Signature = ByteString()
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.Algorithm)))
        packet.append(struct.pack('<{}s'.format(len(self.Algorithm)), self.Algorithm.encode()))
        packet.append(self.Signature.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = SignatureData()
        slength = struct.unpack('<i', data.red(1))
        obj.Algorithm = struct.unpack('<{}s'.format(slength), data.read(slength))
        obj.Signature = ByteString.from_binary(data)
        return obj
    
    def __str__(self):
        return 'SignatureData(' + 'Algorithm:' + str(self.Algorithm) + ', '  + \
             'Signature:' + str(self.Signature) + ')'
    
    __repr__ = __str__
    
class CreateSessionParameters(object):
    def __init__(self):
        self.ClientDescription = ApplicationDescription()
        self.ServerUri = ''
        self.EndpointUrl = ''
        self.SessionName = ''
        self.ClientNonce = ByteString()
        self.ClientCertificate = ByteString()
        self.RequestedSessionTimeout = 0
        self.MaxResponseMessageSize = 0
    
    def to_binary(self):
        packet = []
        packet.append(self.ClientDescription.to_binary())
        packet.append(struct.pack('<i', len(self.ServerUri)))
        packet.append(struct.pack('<{}s'.format(len(self.ServerUri)), self.ServerUri.encode()))
        packet.append(struct.pack('<i', len(self.EndpointUrl)))
        packet.append(struct.pack('<{}s'.format(len(self.EndpointUrl)), self.EndpointUrl.encode()))
        packet.append(struct.pack('<i', len(self.SessionName)))
        packet.append(struct.pack('<{}s'.format(len(self.SessionName)), self.SessionName.encode()))
        packet.append(self.ClientNonce.to_binary())
        packet.append(self.ClientCertificate.to_binary())
        fmt = '<d'
        packet.append(struct.pack(fmt, self.RequestedSessionTimeout))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.MaxResponseMessageSize))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = CreateSessionParameters()
        obj.ClientDescription = ApplicationDescription.from_binary(data)
        slength = struct.unpack('<i', data.red(1))
        obj.ServerUri = struct.unpack('<{}s'.format(slength), data.read(slength))
        slength = struct.unpack('<i', data.red(1))
        obj.EndpointUrl = struct.unpack('<{}s'.format(slength), data.read(slength))
        slength = struct.unpack('<i', data.red(1))
        obj.SessionName = struct.unpack('<{}s'.format(slength), data.read(slength))
        obj.ClientNonce = ByteString.from_binary(data)
        obj.ClientCertificate = ByteString.from_binary(data)
        fmt = '<d'
        fmt_size = 8
        obj.RequestedSessionTimeout = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.MaxResponseMessageSize = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'CreateSessionParameters(' + 'ClientDescription:' + str(self.ClientDescription) + ', '  + \
             'ServerUri:' + str(self.ServerUri) + ', '  + \
             'EndpointUrl:' + str(self.EndpointUrl) + ', '  + \
             'SessionName:' + str(self.SessionName) + ', '  + \
             'ClientNonce:' + str(self.ClientNonce) + ', '  + \
             'ClientCertificate:' + str(self.ClientCertificate) + ', '  + \
             'RequestedSessionTimeout:' + str(self.RequestedSessionTimeout) + ', '  + \
             'MaxResponseMessageSize:' + str(self.MaxResponseMessageSize) + ')'
    
    __repr__ = __str__
    
class CreateSessionRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.CreateSessionRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
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
        obj = CreateSessionRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = CreateSessionParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'CreateSessionRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class CreateSessionResult(object):
    def __init__(self):
        self.SessionId = NodeId()
        self.AuthenticationToken = NodeId()
        self.RevisedSessionTimeout = 0
        self.ServerNonce = ByteString()
        self.ServerCertificate = ByteString()
        self.ServerEndpoints = []
        self.ServerSoftwareCertificates = []
        self.ServerSignature = SignatureData()
        self.MaxRequestMessageSize = 0
    
    def to_binary(self):
        packet = []
        packet.append(self.SessionId.to_binary())
        packet.append(self.AuthenticationToken.to_binary())
        fmt = '<d'
        packet.append(struct.pack(fmt, self.RevisedSessionTimeout))
        packet.append(self.ServerNonce.to_binary())
        packet.append(self.ServerCertificate.to_binary())
        packet.append(struct.pack('<i', len(self.ServerEndpoints)))
        for i in self.ServerEndpoints:
            packet.append(self.ServerEndpoints.to_binary())
        packet.append(struct.pack('<i', len(self.ServerSoftwareCertificates)))
        for i in self.ServerSoftwareCertificates:
            packet.append(self.ServerSoftwareCertificates.to_binary())
        packet.append(self.ServerSignature.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.MaxRequestMessageSize))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = CreateSessionResult()
        obj.SessionId = NodeId.from_binary(data)
        obj.AuthenticationToken = NodeId.from_binary(data)
        fmt = '<d'
        fmt_size = 8
        obj.RevisedSessionTimeout = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.ServerNonce = ByteString.from_binary(data)
        obj.ServerCertificate = ByteString.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.ServerEndpoints = EndpointDescription.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.ServerSoftwareCertificates = SignedSoftwareCertificate.from_binary(data)
        obj.ServerSignature = SignatureData.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.MaxRequestMessageSize = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'CreateSessionResult(' + 'SessionId:' + str(self.SessionId) + ', '  + \
             'AuthenticationToken:' + str(self.AuthenticationToken) + ', '  + \
             'RevisedSessionTimeout:' + str(self.RevisedSessionTimeout) + ', '  + \
             'ServerNonce:' + str(self.ServerNonce) + ', '  + \
             'ServerCertificate:' + str(self.ServerCertificate) + ', '  + \
             'ServerEndpoints:' + str(self.ServerEndpoints) + ', '  + \
             'ServerSoftwareCertificates:' + str(self.ServerSoftwareCertificates) + ', '  + \
             'ServerSignature:' + str(self.ServerSignature) + ', '  + \
             'MaxRequestMessageSize:' + str(self.MaxRequestMessageSize) + ')'
    
    __repr__ = __str__
    
class CreateSessionResponse(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.CreateSessionResponse_Encoding_DefaultBinary, NodeIdType.FourByte)
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
        obj = CreateSessionResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = CreateSessionResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'CreateSessionResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class UserIdentityToken(object):
    def __init__(self):
        self.PolicyId = ''
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.PolicyId)))
        packet.append(struct.pack('<{}s'.format(len(self.PolicyId)), self.PolicyId.encode()))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = UserIdentityToken()
        slength = struct.unpack('<i', data.red(1))
        obj.PolicyId = struct.unpack('<{}s'.format(slength), data.read(slength))
        return obj
    
    def __str__(self):
        return 'UserIdentityToken(' + 'PolicyId:' + str(self.PolicyId) + ')'
    
    __repr__ = __str__
    
class AnonymousIdentityToken(object):
    def __init__(self):
        self.PolicyId = ''
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.PolicyId)))
        packet.append(struct.pack('<{}s'.format(len(self.PolicyId)), self.PolicyId.encode()))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = AnonymousIdentityToken()
        slength = struct.unpack('<i', data.red(1))
        obj.PolicyId = struct.unpack('<{}s'.format(slength), data.read(slength))
        return obj
    
    def __str__(self):
        return 'AnonymousIdentityToken(' + 'PolicyId:' + str(self.PolicyId) + ')'
    
    __repr__ = __str__
    
class UserNameIdentityToken(object):
    def __init__(self):
        self.PolicyId = ''
        self.UserName = ''
        self.Password = ByteString()
        self.EncryptionAlgorithm = ''
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.PolicyId)))
        packet.append(struct.pack('<{}s'.format(len(self.PolicyId)), self.PolicyId.encode()))
        packet.append(struct.pack('<i', len(self.UserName)))
        packet.append(struct.pack('<{}s'.format(len(self.UserName)), self.UserName.encode()))
        packet.append(self.Password.to_binary())
        packet.append(struct.pack('<i', len(self.EncryptionAlgorithm)))
        packet.append(struct.pack('<{}s'.format(len(self.EncryptionAlgorithm)), self.EncryptionAlgorithm.encode()))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = UserNameIdentityToken()
        slength = struct.unpack('<i', data.red(1))
        obj.PolicyId = struct.unpack('<{}s'.format(slength), data.read(slength))
        slength = struct.unpack('<i', data.red(1))
        obj.UserName = struct.unpack('<{}s'.format(slength), data.read(slength))
        obj.Password = ByteString.from_binary(data)
        slength = struct.unpack('<i', data.red(1))
        obj.EncryptionAlgorithm = struct.unpack('<{}s'.format(slength), data.read(slength))
        return obj
    
    def __str__(self):
        return 'UserNameIdentityToken(' + 'PolicyId:' + str(self.PolicyId) + ', '  + \
             'UserName:' + str(self.UserName) + ', '  + \
             'Password:' + str(self.Password) + ', '  + \
             'EncryptionAlgorithm:' + str(self.EncryptionAlgorithm) + ')'
    
    __repr__ = __str__
    
class X509IdentityToken(object):
    def __init__(self):
        self.PolicyId = ''
        self.CertificateData = ByteString()
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.PolicyId)))
        packet.append(struct.pack('<{}s'.format(len(self.PolicyId)), self.PolicyId.encode()))
        packet.append(self.CertificateData.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = X509IdentityToken()
        slength = struct.unpack('<i', data.red(1))
        obj.PolicyId = struct.unpack('<{}s'.format(slength), data.read(slength))
        obj.CertificateData = ByteString.from_binary(data)
        return obj
    
    def __str__(self):
        return 'X509IdentityToken(' + 'PolicyId:' + str(self.PolicyId) + ', '  + \
             'CertificateData:' + str(self.CertificateData) + ')'
    
    __repr__ = __str__
    
class IssuedIdentityToken(object):
    def __init__(self):
        self.PolicyId = ''
        self.TokenData = ByteString()
        self.EncryptionAlgorithm = ''
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.PolicyId)))
        packet.append(struct.pack('<{}s'.format(len(self.PolicyId)), self.PolicyId.encode()))
        packet.append(self.TokenData.to_binary())
        packet.append(struct.pack('<i', len(self.EncryptionAlgorithm)))
        packet.append(struct.pack('<{}s'.format(len(self.EncryptionAlgorithm)), self.EncryptionAlgorithm.encode()))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = IssuedIdentityToken()
        slength = struct.unpack('<i', data.red(1))
        obj.PolicyId = struct.unpack('<{}s'.format(slength), data.read(slength))
        obj.TokenData = ByteString.from_binary(data)
        slength = struct.unpack('<i', data.red(1))
        obj.EncryptionAlgorithm = struct.unpack('<{}s'.format(slength), data.read(slength))
        return obj
    
    def __str__(self):
        return 'IssuedIdentityToken(' + 'PolicyId:' + str(self.PolicyId) + ', '  + \
             'TokenData:' + str(self.TokenData) + ', '  + \
             'EncryptionAlgorithm:' + str(self.EncryptionAlgorithm) + ')'
    
    __repr__ = __str__
    
class ActivateSessionParameters(object):
    def __init__(self):
        self.ClientSignature = SignatureData()
        self.ClientSoftwareCertificates = []
        self.LocaleIds = []
        self.UserIdentityToken = ExtensionObject()
        self.UserTokenSignature = SignatureData()
    
    def to_binary(self):
        packet = []
        packet.append(self.ClientSignature.to_binary())
        packet.append(struct.pack('<i', len(self.ClientSoftwareCertificates)))
        for i in self.ClientSoftwareCertificates:
            packet.append(self.ClientSoftwareCertificates.to_binary())
        packet.append(struct.pack('<i', len(self.LocaleIds)))
        for i in self.LocaleIds:
            packet.append(struct.pack('<i', len(self.LocaleIds)))
            packet.append(struct.pack('<{}s'.format(len(self.LocaleIds)), self.LocaleIds.encode()))
        packet.append(self.UserIdentityToken.to_binary())
        packet.append(self.UserTokenSignature.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ActivateSessionParameters()
        obj.ClientSignature = SignatureData.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.ClientSoftwareCertificates = SignedSoftwareCertificate.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                slength = struct.unpack('<i', data.red(1))
                obj.LocaleIds = struct.unpack('<{}s'.format(slength), data.read(slength))
        obj.UserIdentityToken = ExtensionObject.from_binary(data)
        obj.UserTokenSignature = SignatureData.from_binary(data)
        return obj
    
    def __str__(self):
        return 'ActivateSessionParameters(' + 'ClientSignature:' + str(self.ClientSignature) + ', '  + \
             'ClientSoftwareCertificates:' + str(self.ClientSoftwareCertificates) + ', '  + \
             'LocaleIds:' + str(self.LocaleIds) + ', '  + \
             'UserIdentityToken:' + str(self.UserIdentityToken) + ', '  + \
             'UserTokenSignature:' + str(self.UserTokenSignature) + ')'
    
    __repr__ = __str__
    
class ActivateSessionRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.ActivateSessionRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
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
        obj = ActivateSessionRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = ActivateSessionParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'ActivateSessionRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class ActivateSessionResult(object):
    def __init__(self):
        self.ServerNonce = ByteString()
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        packet.append(self.ServerNonce.to_binary())
        packet.append(struct.pack('<i', len(self.Results)))
        for i in self.Results:
            packet.append(self.Results.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for i in self.DiagnosticInfos:
            packet.append(self.DiagnosticInfos.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ActivateSessionResult()
        obj.ServerNonce = ByteString.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.Results = StatusCode.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.DiagnosticInfos = DiagnosticInfo.from_binary(data)
        return obj
    
    def __str__(self):
        return 'ActivateSessionResult(' + 'ServerNonce:' + str(self.ServerNonce) + ', '  + \
             'Results:' + str(self.Results) + ', '  + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'
    
    __repr__ = __str__
    
class ActivateSessionResponse(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.ActivateSessionResponse_Encoding_DefaultBinary, NodeIdType.FourByte)
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
        obj = ActivateSessionResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = ActivateSessionResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'ActivateSessionResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class CloseSessionRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.CloseSessionRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
        self.RequestHeader = RequestHeader()
        self.DeleteSubscriptions = 0
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        fmt = '<?'
        packet.append(struct.pack(fmt, self.DeleteSubscriptions))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = CloseSessionRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        fmt = '<?'
        fmt_size = 1
        obj.DeleteSubscriptions = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'CloseSessionRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'DeleteSubscriptions:' + str(self.DeleteSubscriptions) + ')'
    
    __repr__ = __str__
    
class CloseSessionResponse(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.CloseSessionResponse_Encoding_DefaultBinary, NodeIdType.FourByte)
        self.ResponseHeader = ResponseHeader()
    
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
        return 'CloseSessionResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ')'
    
    __repr__ = __str__
    
class CancelParameters(object):
    def __init__(self):
        self.RequestHandle = 0
    
    def to_binary(self):
        packet = []
        fmt = '<I'
        packet.append(struct.pack(fmt, self.RequestHandle))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = CancelParameters()
        fmt = '<I'
        fmt_size = 4
        obj.RequestHandle = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'CancelParameters(' + 'RequestHandle:' + str(self.RequestHandle) + ')'
    
    __repr__ = __str__
    
class CancelRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.CancelRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
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
        obj = CancelRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = CancelParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'CancelRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class CancelResult(object):
    def __init__(self):
        self.CancelCount = 0
    
    def to_binary(self):
        packet = []
        fmt = '<I'
        packet.append(struct.pack(fmt, self.CancelCount))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = CancelResult()
        fmt = '<I'
        fmt_size = 4
        obj.CancelCount = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'CancelResult(' + 'CancelCount:' + str(self.CancelCount) + ')'
    
    __repr__ = __str__
    
class CancelResponse(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.CancelResponse_Encoding_DefaultBinary, NodeIdType.FourByte)
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
        obj = CancelResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = CancelResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'CancelResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class NodeAttributes(object):
    def __init__(self):
        self.SpecifiedAttributes = 0
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self.UserWriteMask = 0
    
    def to_binary(self):
        packet = []
        fmt = '<I'
        packet.append(struct.pack(fmt, self.SpecifiedAttributes))
        packet.append(self.DisplayName.to_binary())
        packet.append(self.Description.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.WriteMask))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.UserWriteMask))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = NodeAttributes()
        fmt = '<I'
        fmt_size = 4
        obj.SpecifiedAttributes = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.DisplayName = LocalizedText.from_binary(data)
        obj.Description = LocalizedText.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.WriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.UserWriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'NodeAttributes(' + 'SpecifiedAttributes:' + str(self.SpecifiedAttributes) + ', '  + \
             'DisplayName:' + str(self.DisplayName) + ', '  + \
             'Description:' + str(self.Description) + ', '  + \
             'WriteMask:' + str(self.WriteMask) + ', '  + \
             'UserWriteMask:' + str(self.UserWriteMask) + ')'
    
    __repr__ = __str__
    
class ObjectAttributes(object):
    def __init__(self):
        self.SpecifiedAttributes = 0
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self.UserWriteMask = 0
        self.EventNotifier = 0
    
    def to_binary(self):
        packet = []
        fmt = '<I'
        packet.append(struct.pack(fmt, self.SpecifiedAttributes))
        packet.append(self.DisplayName.to_binary())
        packet.append(self.Description.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.WriteMask))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.UserWriteMask))
        fmt = '<B'
        packet.append(struct.pack(fmt, self.EventNotifier))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ObjectAttributes()
        fmt = '<I'
        fmt_size = 4
        obj.SpecifiedAttributes = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.DisplayName = LocalizedText.from_binary(data)
        obj.Description = LocalizedText.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.WriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.UserWriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<B'
        fmt_size = 1
        obj.EventNotifier = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'ObjectAttributes(' + 'SpecifiedAttributes:' + str(self.SpecifiedAttributes) + ', '  + \
             'DisplayName:' + str(self.DisplayName) + ', '  + \
             'Description:' + str(self.Description) + ', '  + \
             'WriteMask:' + str(self.WriteMask) + ', '  + \
             'UserWriteMask:' + str(self.UserWriteMask) + ', '  + \
             'EventNotifier:' + str(self.EventNotifier) + ')'
    
    __repr__ = __str__
    
class VariableAttributes(object):
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
        self.Historizing = 0
    
    def to_binary(self):
        packet = []
        fmt = '<I'
        packet.append(struct.pack(fmt, self.SpecifiedAttributes))
        packet.append(self.DisplayName.to_binary())
        packet.append(self.Description.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.WriteMask))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.UserWriteMask))
        packet.append(self.Value.to_binary())
        packet.append(self.DataType.to_binary())
        fmt = '<i'
        packet.append(struct.pack(fmt, self.ValueRank))
        packet.append(struct.pack('<i', len(self.ArrayDimensions)))
        for i in self.ArrayDimensions:
            fmt = '<I'
            packet.append(struct.pack(fmt, self.ArrayDimensions))
        fmt = '<B'
        packet.append(struct.pack(fmt, self.AccessLevel))
        fmt = '<B'
        packet.append(struct.pack(fmt, self.UserAccessLevel))
        fmt = '<d'
        packet.append(struct.pack(fmt, self.MinimumSamplingInterval))
        fmt = '<?'
        packet.append(struct.pack(fmt, self.Historizing))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = VariableAttributes()
        fmt = '<I'
        fmt_size = 4
        obj.SpecifiedAttributes = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.DisplayName = LocalizedText.from_binary(data)
        obj.Description = LocalizedText.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.WriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.UserWriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.Value = Variant.from_binary(data)
        obj.DataType = NodeId.from_binary(data)
        fmt = '<i'
        fmt_size = 4
        obj.ValueRank = struct.unpack(fmt, data.read(fmt_size))[0]
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                fmt = '<I'
                fmt_size = 4
                obj.ArrayDimensions = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<B'
        fmt_size = 1
        obj.AccessLevel = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<B'
        fmt_size = 1
        obj.UserAccessLevel = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<d'
        fmt_size = 8
        obj.MinimumSamplingInterval = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<?'
        fmt_size = 1
        obj.Historizing = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'VariableAttributes(' + 'SpecifiedAttributes:' + str(self.SpecifiedAttributes) + ', '  + \
             'DisplayName:' + str(self.DisplayName) + ', '  + \
             'Description:' + str(self.Description) + ', '  + \
             'WriteMask:' + str(self.WriteMask) + ', '  + \
             'UserWriteMask:' + str(self.UserWriteMask) + ', '  + \
             'Value:' + str(self.Value) + ', '  + \
             'DataType:' + str(self.DataType) + ', '  + \
             'ValueRank:' + str(self.ValueRank) + ', '  + \
             'ArrayDimensions:' + str(self.ArrayDimensions) + ', '  + \
             'AccessLevel:' + str(self.AccessLevel) + ', '  + \
             'UserAccessLevel:' + str(self.UserAccessLevel) + ', '  + \
             'MinimumSamplingInterval:' + str(self.MinimumSamplingInterval) + ', '  + \
             'Historizing:' + str(self.Historizing) + ')'
    
    __repr__ = __str__
    
class MethodAttributes(object):
    def __init__(self):
        self.SpecifiedAttributes = 0
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self.UserWriteMask = 0
        self.Executable = 0
        self.UserExecutable = 0
    
    def to_binary(self):
        packet = []
        fmt = '<I'
        packet.append(struct.pack(fmt, self.SpecifiedAttributes))
        packet.append(self.DisplayName.to_binary())
        packet.append(self.Description.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.WriteMask))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.UserWriteMask))
        fmt = '<?'
        packet.append(struct.pack(fmt, self.Executable))
        fmt = '<?'
        packet.append(struct.pack(fmt, self.UserExecutable))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = MethodAttributes()
        fmt = '<I'
        fmt_size = 4
        obj.SpecifiedAttributes = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.DisplayName = LocalizedText.from_binary(data)
        obj.Description = LocalizedText.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.WriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.UserWriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<?'
        fmt_size = 1
        obj.Executable = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<?'
        fmt_size = 1
        obj.UserExecutable = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'MethodAttributes(' + 'SpecifiedAttributes:' + str(self.SpecifiedAttributes) + ', '  + \
             'DisplayName:' + str(self.DisplayName) + ', '  + \
             'Description:' + str(self.Description) + ', '  + \
             'WriteMask:' + str(self.WriteMask) + ', '  + \
             'UserWriteMask:' + str(self.UserWriteMask) + ', '  + \
             'Executable:' + str(self.Executable) + ', '  + \
             'UserExecutable:' + str(self.UserExecutable) + ')'
    
    __repr__ = __str__
    
class ObjectTypeAttributes(object):
    def __init__(self):
        self.SpecifiedAttributes = 0
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self.UserWriteMask = 0
        self.IsAbstract = 0
    
    def to_binary(self):
        packet = []
        fmt = '<I'
        packet.append(struct.pack(fmt, self.SpecifiedAttributes))
        packet.append(self.DisplayName.to_binary())
        packet.append(self.Description.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.WriteMask))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.UserWriteMask))
        fmt = '<?'
        packet.append(struct.pack(fmt, self.IsAbstract))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ObjectTypeAttributes()
        fmt = '<I'
        fmt_size = 4
        obj.SpecifiedAttributes = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.DisplayName = LocalizedText.from_binary(data)
        obj.Description = LocalizedText.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.WriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.UserWriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<?'
        fmt_size = 1
        obj.IsAbstract = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'ObjectTypeAttributes(' + 'SpecifiedAttributes:' + str(self.SpecifiedAttributes) + ', '  + \
             'DisplayName:' + str(self.DisplayName) + ', '  + \
             'Description:' + str(self.Description) + ', '  + \
             'WriteMask:' + str(self.WriteMask) + ', '  + \
             'UserWriteMask:' + str(self.UserWriteMask) + ', '  + \
             'IsAbstract:' + str(self.IsAbstract) + ')'
    
    __repr__ = __str__
    
class VariableTypeAttributes(object):
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
        self.IsAbstract = 0
    
    def to_binary(self):
        packet = []
        fmt = '<I'
        packet.append(struct.pack(fmt, self.SpecifiedAttributes))
        packet.append(self.DisplayName.to_binary())
        packet.append(self.Description.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.WriteMask))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.UserWriteMask))
        packet.append(self.Value.to_binary())
        packet.append(self.DataType.to_binary())
        fmt = '<i'
        packet.append(struct.pack(fmt, self.ValueRank))
        packet.append(struct.pack('<i', len(self.ArrayDimensions)))
        for i in self.ArrayDimensions:
            fmt = '<I'
            packet.append(struct.pack(fmt, self.ArrayDimensions))
        fmt = '<?'
        packet.append(struct.pack(fmt, self.IsAbstract))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = VariableTypeAttributes()
        fmt = '<I'
        fmt_size = 4
        obj.SpecifiedAttributes = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.DisplayName = LocalizedText.from_binary(data)
        obj.Description = LocalizedText.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.WriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.UserWriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.Value = Variant.from_binary(data)
        obj.DataType = NodeId.from_binary(data)
        fmt = '<i'
        fmt_size = 4
        obj.ValueRank = struct.unpack(fmt, data.read(fmt_size))[0]
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                fmt = '<I'
                fmt_size = 4
                obj.ArrayDimensions = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<?'
        fmt_size = 1
        obj.IsAbstract = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'VariableTypeAttributes(' + 'SpecifiedAttributes:' + str(self.SpecifiedAttributes) + ', '  + \
             'DisplayName:' + str(self.DisplayName) + ', '  + \
             'Description:' + str(self.Description) + ', '  + \
             'WriteMask:' + str(self.WriteMask) + ', '  + \
             'UserWriteMask:' + str(self.UserWriteMask) + ', '  + \
             'Value:' + str(self.Value) + ', '  + \
             'DataType:' + str(self.DataType) + ', '  + \
             'ValueRank:' + str(self.ValueRank) + ', '  + \
             'ArrayDimensions:' + str(self.ArrayDimensions) + ', '  + \
             'IsAbstract:' + str(self.IsAbstract) + ')'
    
    __repr__ = __str__
    
class ReferenceTypeAttributes(object):
    def __init__(self):
        self.SpecifiedAttributes = 0
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self.UserWriteMask = 0
        self.IsAbstract = 0
        self.Symmetric = 0
        self.InverseName = LocalizedText()
    
    def to_binary(self):
        packet = []
        fmt = '<I'
        packet.append(struct.pack(fmt, self.SpecifiedAttributes))
        packet.append(self.DisplayName.to_binary())
        packet.append(self.Description.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.WriteMask))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.UserWriteMask))
        fmt = '<?'
        packet.append(struct.pack(fmt, self.IsAbstract))
        fmt = '<?'
        packet.append(struct.pack(fmt, self.Symmetric))
        packet.append(self.InverseName.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ReferenceTypeAttributes()
        fmt = '<I'
        fmt_size = 4
        obj.SpecifiedAttributes = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.DisplayName = LocalizedText.from_binary(data)
        obj.Description = LocalizedText.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.WriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.UserWriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<?'
        fmt_size = 1
        obj.IsAbstract = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<?'
        fmt_size = 1
        obj.Symmetric = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.InverseName = LocalizedText.from_binary(data)
        return obj
    
    def __str__(self):
        return 'ReferenceTypeAttributes(' + 'SpecifiedAttributes:' + str(self.SpecifiedAttributes) + ', '  + \
             'DisplayName:' + str(self.DisplayName) + ', '  + \
             'Description:' + str(self.Description) + ', '  + \
             'WriteMask:' + str(self.WriteMask) + ', '  + \
             'UserWriteMask:' + str(self.UserWriteMask) + ', '  + \
             'IsAbstract:' + str(self.IsAbstract) + ', '  + \
             'Symmetric:' + str(self.Symmetric) + ', '  + \
             'InverseName:' + str(self.InverseName) + ')'
    
    __repr__ = __str__
    
class DataTypeAttributes(object):
    def __init__(self):
        self.SpecifiedAttributes = 0
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self.UserWriteMask = 0
        self.IsAbstract = 0
    
    def to_binary(self):
        packet = []
        fmt = '<I'
        packet.append(struct.pack(fmt, self.SpecifiedAttributes))
        packet.append(self.DisplayName.to_binary())
        packet.append(self.Description.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.WriteMask))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.UserWriteMask))
        fmt = '<?'
        packet.append(struct.pack(fmt, self.IsAbstract))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = DataTypeAttributes()
        fmt = '<I'
        fmt_size = 4
        obj.SpecifiedAttributes = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.DisplayName = LocalizedText.from_binary(data)
        obj.Description = LocalizedText.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.WriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.UserWriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<?'
        fmt_size = 1
        obj.IsAbstract = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'DataTypeAttributes(' + 'SpecifiedAttributes:' + str(self.SpecifiedAttributes) + ', '  + \
             'DisplayName:' + str(self.DisplayName) + ', '  + \
             'Description:' + str(self.Description) + ', '  + \
             'WriteMask:' + str(self.WriteMask) + ', '  + \
             'UserWriteMask:' + str(self.UserWriteMask) + ', '  + \
             'IsAbstract:' + str(self.IsAbstract) + ')'
    
    __repr__ = __str__
    
class ViewAttributes(object):
    def __init__(self):
        self.SpecifiedAttributes = 0
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self.UserWriteMask = 0
        self.ContainsNoLoops = 0
        self.EventNotifier = 0
    
    def to_binary(self):
        packet = []
        fmt = '<I'
        packet.append(struct.pack(fmt, self.SpecifiedAttributes))
        packet.append(self.DisplayName.to_binary())
        packet.append(self.Description.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.WriteMask))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.UserWriteMask))
        fmt = '<?'
        packet.append(struct.pack(fmt, self.ContainsNoLoops))
        fmt = '<B'
        packet.append(struct.pack(fmt, self.EventNotifier))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ViewAttributes()
        fmt = '<I'
        fmt_size = 4
        obj.SpecifiedAttributes = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.DisplayName = LocalizedText.from_binary(data)
        obj.Description = LocalizedText.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.WriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.UserWriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<?'
        fmt_size = 1
        obj.ContainsNoLoops = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<B'
        fmt_size = 1
        obj.EventNotifier = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'ViewAttributes(' + 'SpecifiedAttributes:' + str(self.SpecifiedAttributes) + ', '  + \
             'DisplayName:' + str(self.DisplayName) + ', '  + \
             'Description:' + str(self.Description) + ', '  + \
             'WriteMask:' + str(self.WriteMask) + ', '  + \
             'UserWriteMask:' + str(self.UserWriteMask) + ', '  + \
             'ContainsNoLoops:' + str(self.ContainsNoLoops) + ', '  + \
             'EventNotifier:' + str(self.EventNotifier) + ')'
    
    __repr__ = __str__
    
class AddNodesItem(object):
    def __init__(self):
        self.ParentNodeId = ExpandedNodeId()
        self.ReferenceTypeId = NodeId()
        self.RequestedNewNodeId = ExpandedNodeId()
        self.BrowseName = QualifiedName()
        self.NodeClass = 0
        self.NodeAttributes = ExtensionObject()
        self.TypeDefinition = ExpandedNodeId()
    
    def to_binary(self):
        packet = []
        packet.append(self.ParentNodeId.to_binary())
        packet.append(self.ReferenceTypeId.to_binary())
        packet.append(self.RequestedNewNodeId.to_binary())
        packet.append(self.BrowseName.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.NodeClass))
        packet.append(self.NodeAttributes.to_binary())
        packet.append(self.TypeDefinition.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = AddNodesItem()
        obj.ParentNodeId = ExpandedNodeId.from_binary(data)
        obj.ReferenceTypeId = NodeId.from_binary(data)
        obj.RequestedNewNodeId = ExpandedNodeId.from_binary(data)
        obj.BrowseName = QualifiedName.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.NodeClass = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.NodeAttributes = ExtensionObject.from_binary(data)
        obj.TypeDefinition = ExpandedNodeId.from_binary(data)
        return obj
    
    def __str__(self):
        return 'AddNodesItem(' + 'ParentNodeId:' + str(self.ParentNodeId) + ', '  + \
             'ReferenceTypeId:' + str(self.ReferenceTypeId) + ', '  + \
             'RequestedNewNodeId:' + str(self.RequestedNewNodeId) + ', '  + \
             'BrowseName:' + str(self.BrowseName) + ', '  + \
             'NodeClass:' + str(self.NodeClass) + ', '  + \
             'NodeAttributes:' + str(self.NodeAttributes) + ', '  + \
             'TypeDefinition:' + str(self.TypeDefinition) + ')'
    
    __repr__ = __str__
    
class AddNodesResult(object):
    def __init__(self):
        self.StatusCode = StatusCode()
        self.AddedNodeId = NodeId()
    
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
        return 'AddNodesResult(' + 'StatusCode:' + str(self.StatusCode) + ', '  + \
             'AddedNodeId:' + str(self.AddedNodeId) + ')'
    
    __repr__ = __str__
    
class AddNodesParameters(object):
    def __init__(self):
        self.NodesToAdd = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.NodesToAdd)))
        for i in self.NodesToAdd:
            packet.append(self.NodesToAdd.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = AddNodesParameters()
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.NodesToAdd = AddNodesItem.from_binary(data)
        return obj
    
    def __str__(self):
        return 'AddNodesParameters(' + 'NodesToAdd:' + str(self.NodesToAdd) + ')'
    
    __repr__ = __str__
    
class AddNodesRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.AddNodesRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
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
        obj = AddNodesRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = AddNodesParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'AddNodesRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class AddNodesResponse(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.AddNodesResponse_Encoding_DefaultBinary, NodeIdType.FourByte)
        self.ResponseHeader = ResponseHeader()
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(struct.pack('<i', len(self.Results)))
        for i in self.Results:
            packet.append(self.Results.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for i in self.DiagnosticInfos:
            packet.append(self.DiagnosticInfos.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = AddNodesResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.Results = AddNodesResult.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.DiagnosticInfos = DiagnosticInfo.from_binary(data)
        return obj
    
    def __str__(self):
        return 'AddNodesResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Results:' + str(self.Results) + ', '  + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'
    
    __repr__ = __str__
    
class AddReferencesItem(object):
    def __init__(self):
        self.SourceNodeId = NodeId()
        self.ReferenceTypeId = NodeId()
        self.IsForward = 0
        self.TargetServerUri = ''
        self.TargetNodeId = ExpandedNodeId()
        self.TargetNodeClass = 0
    
    def to_binary(self):
        packet = []
        packet.append(self.SourceNodeId.to_binary())
        packet.append(self.ReferenceTypeId.to_binary())
        fmt = '<?'
        packet.append(struct.pack(fmt, self.IsForward))
        packet.append(struct.pack('<i', len(self.TargetServerUri)))
        packet.append(struct.pack('<{}s'.format(len(self.TargetServerUri)), self.TargetServerUri.encode()))
        packet.append(self.TargetNodeId.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.TargetNodeClass))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = AddReferencesItem()
        obj.SourceNodeId = NodeId.from_binary(data)
        obj.ReferenceTypeId = NodeId.from_binary(data)
        fmt = '<?'
        fmt_size = 1
        obj.IsForward = struct.unpack(fmt, data.read(fmt_size))[0]
        slength = struct.unpack('<i', data.red(1))
        obj.TargetServerUri = struct.unpack('<{}s'.format(slength), data.read(slength))
        obj.TargetNodeId = ExpandedNodeId.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.TargetNodeClass = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'AddReferencesItem(' + 'SourceNodeId:' + str(self.SourceNodeId) + ', '  + \
             'ReferenceTypeId:' + str(self.ReferenceTypeId) + ', '  + \
             'IsForward:' + str(self.IsForward) + ', '  + \
             'TargetServerUri:' + str(self.TargetServerUri) + ', '  + \
             'TargetNodeId:' + str(self.TargetNodeId) + ', '  + \
             'TargetNodeClass:' + str(self.TargetNodeClass) + ')'
    
    __repr__ = __str__
    
class AddReferencesParameters(object):
    def __init__(self):
        self.ReferencesToAdd = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.ReferencesToAdd)))
        for i in self.ReferencesToAdd:
            packet.append(self.ReferencesToAdd.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = AddReferencesParameters()
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.ReferencesToAdd = AddReferencesItem.from_binary(data)
        return obj
    
    def __str__(self):
        return 'AddReferencesParameters(' + 'ReferencesToAdd:' + str(self.ReferencesToAdd) + ')'
    
    __repr__ = __str__
    
class AddReferencesRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.AddReferencesRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
        self.RequestHeader = RequestHeader()
        self.Parameters = AddReferencesParameters()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = AddReferencesRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = AddReferencesParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'AddReferencesRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class AddReferencesResult(object):
    def __init__(self):
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.Results)))
        for i in self.Results:
            packet.append(self.Results.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for i in self.DiagnosticInfos:
            packet.append(self.DiagnosticInfos.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = AddReferencesResult()
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.Results = StatusCode.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.DiagnosticInfos = DiagnosticInfo.from_binary(data)
        return obj
    
    def __str__(self):
        return 'AddReferencesResult(' + 'Results:' + str(self.Results) + ', '  + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'
    
    __repr__ = __str__
    
class AddReferencesResponse(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.AddReferencesResponse_Encoding_DefaultBinary, NodeIdType.FourByte)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = AddReferencesResult()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = AddReferencesResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = AddReferencesResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'AddReferencesResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class DeleteNodesItem(object):
    def __init__(self):
        self.NodeId = NodeId()
        self.DeleteTargetReferences = 0
    
    def to_binary(self):
        packet = []
        packet.append(self.NodeId.to_binary())
        fmt = '<?'
        packet.append(struct.pack(fmt, self.DeleteTargetReferences))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = DeleteNodesItem()
        obj.NodeId = NodeId.from_binary(data)
        fmt = '<?'
        fmt_size = 1
        obj.DeleteTargetReferences = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'DeleteNodesItem(' + 'NodeId:' + str(self.NodeId) + ', '  + \
             'DeleteTargetReferences:' + str(self.DeleteTargetReferences) + ')'
    
    __repr__ = __str__
    
class DeleteNodesParameters(object):
    def __init__(self):
        self.NodesToDelete = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.NodesToDelete)))
        for i in self.NodesToDelete:
            packet.append(self.NodesToDelete.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = DeleteNodesParameters()
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.NodesToDelete = DeleteNodesItem.from_binary(data)
        return obj
    
    def __str__(self):
        return 'DeleteNodesParameters(' + 'NodesToDelete:' + str(self.NodesToDelete) + ')'
    
    __repr__ = __str__
    
class DeleteNodesRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.DeleteNodesRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
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
        obj = DeleteNodesRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = DeleteNodesParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'DeleteNodesRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class DeleteNodesResult(object):
    def __init__(self):
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.Results)))
        for i in self.Results:
            packet.append(self.Results.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for i in self.DiagnosticInfos:
            packet.append(self.DiagnosticInfos.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = DeleteNodesResult()
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.Results = StatusCode.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.DiagnosticInfos = DiagnosticInfo.from_binary(data)
        return obj
    
    def __str__(self):
        return 'DeleteNodesResult(' + 'Results:' + str(self.Results) + ', '  + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'
    
    __repr__ = __str__
    
class DeleteNodesResponse(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.DeleteNodesResponse_Encoding_DefaultBinary, NodeIdType.FourByte)
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
        obj = DeleteNodesResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = DeleteNodesResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'DeleteNodesResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class DeleteReferencesItem(object):
    def __init__(self):
        self.SourceNodeId = NodeId()
        self.ReferenceTypeId = NodeId()
        self.IsForward = 0
        self.TargetNodeId = ExpandedNodeId()
        self.DeleteBidirectional = 0
    
    def to_binary(self):
        packet = []
        packet.append(self.SourceNodeId.to_binary())
        packet.append(self.ReferenceTypeId.to_binary())
        fmt = '<?'
        packet.append(struct.pack(fmt, self.IsForward))
        packet.append(self.TargetNodeId.to_binary())
        fmt = '<?'
        packet.append(struct.pack(fmt, self.DeleteBidirectional))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = DeleteReferencesItem()
        obj.SourceNodeId = NodeId.from_binary(data)
        obj.ReferenceTypeId = NodeId.from_binary(data)
        fmt = '<?'
        fmt_size = 1
        obj.IsForward = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.TargetNodeId = ExpandedNodeId.from_binary(data)
        fmt = '<?'
        fmt_size = 1
        obj.DeleteBidirectional = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'DeleteReferencesItem(' + 'SourceNodeId:' + str(self.SourceNodeId) + ', '  + \
             'ReferenceTypeId:' + str(self.ReferenceTypeId) + ', '  + \
             'IsForward:' + str(self.IsForward) + ', '  + \
             'TargetNodeId:' + str(self.TargetNodeId) + ', '  + \
             'DeleteBidirectional:' + str(self.DeleteBidirectional) + ')'
    
    __repr__ = __str__
    
class DeleteReferencesParameters(object):
    def __init__(self):
        self.ReferencesToDelete = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.ReferencesToDelete)))
        for i in self.ReferencesToDelete:
            packet.append(self.ReferencesToDelete.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = DeleteReferencesParameters()
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.ReferencesToDelete = DeleteReferencesItem.from_binary(data)
        return obj
    
    def __str__(self):
        return 'DeleteReferencesParameters(' + 'ReferencesToDelete:' + str(self.ReferencesToDelete) + ')'
    
    __repr__ = __str__
    
class DeleteReferencesRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.DeleteReferencesRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
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
        obj = DeleteReferencesRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = DeleteReferencesParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'DeleteReferencesRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class DeleteReferencesResult(object):
    def __init__(self):
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.Results)))
        for i in self.Results:
            packet.append(self.Results.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for i in self.DiagnosticInfos:
            packet.append(self.DiagnosticInfos.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = DeleteReferencesResult()
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.Results = StatusCode.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.DiagnosticInfos = DiagnosticInfo.from_binary(data)
        return obj
    
    def __str__(self):
        return 'DeleteReferencesResult(' + 'Results:' + str(self.Results) + ', '  + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'
    
    __repr__ = __str__
    
class DeleteReferencesResponse(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.DeleteReferencesResponse_Encoding_DefaultBinary, NodeIdType.FourByte)
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
        obj = DeleteReferencesResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = DeleteReferencesResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'DeleteReferencesResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class ViewDescription(object):
    def __init__(self):
        self.ViewId = NodeId()
        self.Timestamp = DateTime()
        self.ViewVersion = 0
    
    def to_binary(self):
        packet = []
        packet.append(self.ViewId.to_binary())
        packet.append(self.Timestamp.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.ViewVersion))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ViewDescription()
        obj.ViewId = NodeId.from_binary(data)
        obj.Timestamp = DateTime.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.ViewVersion = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'ViewDescription(' + 'ViewId:' + str(self.ViewId) + ', '  + \
             'Timestamp:' + str(self.Timestamp) + ', '  + \
             'ViewVersion:' + str(self.ViewVersion) + ')'
    
    __repr__ = __str__
    
class BrowseDescription(object):
    def __init__(self):
        self.NodeId = NodeId()
        self.BrowseDirection = 0
        self.ReferenceTypeId = NodeId()
        self.IncludeSubtypes = 0
        self.NodeClassMask = 0
        self.ResultMask = 0
    
    def to_binary(self):
        packet = []
        packet.append(self.NodeId.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.BrowseDirection))
        packet.append(self.ReferenceTypeId.to_binary())
        fmt = '<?'
        packet.append(struct.pack(fmt, self.IncludeSubtypes))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.NodeClassMask))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.ResultMask))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = BrowseDescription()
        obj.NodeId = NodeId.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.BrowseDirection = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.ReferenceTypeId = NodeId.from_binary(data)
        fmt = '<?'
        fmt_size = 1
        obj.IncludeSubtypes = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.NodeClassMask = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.ResultMask = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'BrowseDescription(' + 'NodeId:' + str(self.NodeId) + ', '  + \
             'BrowseDirection:' + str(self.BrowseDirection) + ', '  + \
             'ReferenceTypeId:' + str(self.ReferenceTypeId) + ', '  + \
             'IncludeSubtypes:' + str(self.IncludeSubtypes) + ', '  + \
             'NodeClassMask:' + str(self.NodeClassMask) + ', '  + \
             'ResultMask:' + str(self.ResultMask) + ')'
    
    __repr__ = __str__
    
class ReferenceDescription(object):
    def __init__(self):
        self.ReferenceTypeId = NodeId()
        self.IsForward = 0
        self.NodeId = ExpandedNodeId()
        self.BrowseName = QualifiedName()
        self.DisplayName = LocalizedText()
        self.NodeClass = 0
        self.TypeDefinition = ExpandedNodeId()
    
    def to_binary(self):
        packet = []
        packet.append(self.ReferenceTypeId.to_binary())
        fmt = '<?'
        packet.append(struct.pack(fmt, self.IsForward))
        packet.append(self.NodeId.to_binary())
        packet.append(self.BrowseName.to_binary())
        packet.append(self.DisplayName.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.NodeClass))
        packet.append(self.TypeDefinition.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ReferenceDescription()
        obj.ReferenceTypeId = NodeId.from_binary(data)
        fmt = '<?'
        fmt_size = 1
        obj.IsForward = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.NodeId = ExpandedNodeId.from_binary(data)
        obj.BrowseName = QualifiedName.from_binary(data)
        obj.DisplayName = LocalizedText.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.NodeClass = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.TypeDefinition = ExpandedNodeId.from_binary(data)
        return obj
    
    def __str__(self):
        return 'ReferenceDescription(' + 'ReferenceTypeId:' + str(self.ReferenceTypeId) + ', '  + \
             'IsForward:' + str(self.IsForward) + ', '  + \
             'NodeId:' + str(self.NodeId) + ', '  + \
             'BrowseName:' + str(self.BrowseName) + ', '  + \
             'DisplayName:' + str(self.DisplayName) + ', '  + \
             'NodeClass:' + str(self.NodeClass) + ', '  + \
             'TypeDefinition:' + str(self.TypeDefinition) + ')'
    
    __repr__ = __str__
    
class BrowseResult(object):
    def __init__(self):
        self.StatusCode = StatusCode()
        self.ContinuationPoint = ByteString()
        self.References = []
    
    def to_binary(self):
        packet = []
        packet.append(self.StatusCode.to_binary())
        packet.append(self.ContinuationPoint.to_binary())
        packet.append(struct.pack('<i', len(self.References)))
        for i in self.References:
            packet.append(self.References.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = BrowseResult()
        obj.StatusCode = StatusCode.from_binary(data)
        obj.ContinuationPoint = ByteString.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.References = ReferenceDescription.from_binary(data)
        return obj
    
    def __str__(self):
        return 'BrowseResult(' + 'StatusCode:' + str(self.StatusCode) + ', '  + \
             'ContinuationPoint:' + str(self.ContinuationPoint) + ', '  + \
             'References:' + str(self.References) + ')'
    
    __repr__ = __str__
    
class BrowseParameters(object):
    def __init__(self):
        self.View = ViewDescription()
        self.RequestedMaxReferencesPerNode = 0
        self.NodesToBrowse = []
    
    def to_binary(self):
        packet = []
        packet.append(self.View.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.RequestedMaxReferencesPerNode))
        packet.append(struct.pack('<i', len(self.NodesToBrowse)))
        for i in self.NodesToBrowse:
            packet.append(self.NodesToBrowse.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = BrowseParameters()
        obj.View = ViewDescription.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.RequestedMaxReferencesPerNode = struct.unpack(fmt, data.read(fmt_size))[0]
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.NodesToBrowse = BrowseDescription.from_binary(data)
        return obj
    
    def __str__(self):
        return 'BrowseParameters(' + 'View:' + str(self.View) + ', '  + \
             'RequestedMaxReferencesPerNode:' + str(self.RequestedMaxReferencesPerNode) + ', '  + \
             'NodesToBrowse:' + str(self.NodesToBrowse) + ')'
    
    __repr__ = __str__
    
class BrowseRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.BrowseRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
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
        obj = BrowseRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = BrowseParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'BrowseRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class BrowseResponse(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.BrowseResponse_Encoding_DefaultBinary, NodeIdType.FourByte)
        self.ResponseHeader = ResponseHeader()
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(struct.pack('<i', len(self.Results)))
        for i in self.Results:
            packet.append(self.Results.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for i in self.DiagnosticInfos:
            packet.append(self.DiagnosticInfos.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = BrowseResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.Results = BrowseResult.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.DiagnosticInfos = DiagnosticInfo.from_binary(data)
        return obj
    
    def __str__(self):
        return 'BrowseResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Results:' + str(self.Results) + ', '  + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'
    
    __repr__ = __str__
    
class BrowseNextParameters(object):
    def __init__(self):
        self.ReleaseContinuationPoints = 0
        self.ContinuationPoints = []
    
    def to_binary(self):
        packet = []
        fmt = '<?'
        packet.append(struct.pack(fmt, self.ReleaseContinuationPoints))
        packet.append(struct.pack('<i', len(self.ContinuationPoints)))
        for i in self.ContinuationPoints:
            packet.append(self.ContinuationPoints.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = BrowseNextParameters()
        fmt = '<?'
        fmt_size = 1
        obj.ReleaseContinuationPoints = struct.unpack(fmt, data.read(fmt_size))[0]
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.ContinuationPoints = ByteString.from_binary(data)
        return obj
    
    def __str__(self):
        return 'BrowseNextParameters(' + 'ReleaseContinuationPoints:' + str(self.ReleaseContinuationPoints) + ', '  + \
             'ContinuationPoints:' + str(self.ContinuationPoints) + ')'
    
    __repr__ = __str__
    
class BrowseNextRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.BrowseNextRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
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
        obj = BrowseNextRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = BrowseNextParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'BrowseNextRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class BrowseNextResult(object):
    def __init__(self):
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.Results)))
        for i in self.Results:
            packet.append(self.Results.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for i in self.DiagnosticInfos:
            packet.append(self.DiagnosticInfos.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = BrowseNextResult()
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.Results = BrowseResult.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.DiagnosticInfos = DiagnosticInfo.from_binary(data)
        return obj
    
    def __str__(self):
        return 'BrowseNextResult(' + 'Results:' + str(self.Results) + ', '  + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'
    
    __repr__ = __str__
    
class BrowseNextResponse(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.BrowseNextResponse_Encoding_DefaultBinary, NodeIdType.FourByte)
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
        obj = BrowseNextResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = BrowseNextResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'BrowseNextResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class RelativePathElement(object):
    def __init__(self):
        self.ReferenceTypeId = NodeId()
        self.IsInverse = 0
        self.IncludeSubtypes = 0
        self.TargetName = QualifiedName()
    
    def to_binary(self):
        packet = []
        packet.append(self.ReferenceTypeId.to_binary())
        fmt = '<?'
        packet.append(struct.pack(fmt, self.IsInverse))
        fmt = '<?'
        packet.append(struct.pack(fmt, self.IncludeSubtypes))
        packet.append(self.TargetName.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = RelativePathElement()
        obj.ReferenceTypeId = NodeId.from_binary(data)
        fmt = '<?'
        fmt_size = 1
        obj.IsInverse = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<?'
        fmt_size = 1
        obj.IncludeSubtypes = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.TargetName = QualifiedName.from_binary(data)
        return obj
    
    def __str__(self):
        return 'RelativePathElement(' + 'ReferenceTypeId:' + str(self.ReferenceTypeId) + ', '  + \
             'IsInverse:' + str(self.IsInverse) + ', '  + \
             'IncludeSubtypes:' + str(self.IncludeSubtypes) + ', '  + \
             'TargetName:' + str(self.TargetName) + ')'
    
    __repr__ = __str__
    
class RelativePath(object):
    def __init__(self):
        self.Elements = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.Elements)))
        for i in self.Elements:
            packet.append(self.Elements.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = RelativePath()
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.Elements = RelativePathElement.from_binary(data)
        return obj
    
    def __str__(self):
        return 'RelativePath(' + 'Elements:' + str(self.Elements) + ')'
    
    __repr__ = __str__
    
class BrowsePath(object):
    def __init__(self):
        self.StartingNode = NodeId()
        self.RelativePath = RelativePath()
    
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
        return 'BrowsePath(' + 'StartingNode:' + str(self.StartingNode) + ', '  + \
             'RelativePath:' + str(self.RelativePath) + ')'
    
    __repr__ = __str__
    
class BrowsePathTarget(object):
    def __init__(self):
        self.TargetId = ExpandedNodeId()
        self.RemainingPathIndex = 0
    
    def to_binary(self):
        packet = []
        packet.append(self.TargetId.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.RemainingPathIndex))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = BrowsePathTarget()
        obj.TargetId = ExpandedNodeId.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.RemainingPathIndex = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'BrowsePathTarget(' + 'TargetId:' + str(self.TargetId) + ', '  + \
             'RemainingPathIndex:' + str(self.RemainingPathIndex) + ')'
    
    __repr__ = __str__
    
class BrowsePathResult(object):
    def __init__(self):
        self.StatusCode = StatusCode()
        self.Targets = []
    
    def to_binary(self):
        packet = []
        packet.append(self.StatusCode.to_binary())
        packet.append(struct.pack('<i', len(self.Targets)))
        for i in self.Targets:
            packet.append(self.Targets.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = BrowsePathResult()
        obj.StatusCode = StatusCode.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.Targets = BrowsePathTarget.from_binary(data)
        return obj
    
    def __str__(self):
        return 'BrowsePathResult(' + 'StatusCode:' + str(self.StatusCode) + ', '  + \
             'Targets:' + str(self.Targets) + ')'
    
    __repr__ = __str__
    
class TranslateBrowsePathsToNodeIdsParameters(object):
    def __init__(self):
        self.BrowsePaths = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.BrowsePaths)))
        for i in self.BrowsePaths:
            packet.append(self.BrowsePaths.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = TranslateBrowsePathsToNodeIdsParameters()
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.BrowsePaths = BrowsePath.from_binary(data)
        return obj
    
    def __str__(self):
        return 'TranslateBrowsePathsToNodeIdsParameters(' + 'BrowsePaths:' + str(self.BrowsePaths) + ')'
    
    __repr__ = __str__
    
class TranslateBrowsePathsToNodeIdsRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.TranslateBrowsePathsToNodeIdsRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
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
        obj = TranslateBrowsePathsToNodeIdsRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = TranslateBrowsePathsToNodeIdsParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'TranslateBrowsePathsToNodeIdsRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class TranslateBrowsePathsToNodeIdsResult(object):
    def __init__(self):
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.Results)))
        for i in self.Results:
            packet.append(self.Results.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for i in self.DiagnosticInfos:
            packet.append(self.DiagnosticInfos.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = TranslateBrowsePathsToNodeIdsResult()
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.Results = BrowsePathResult.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.DiagnosticInfos = DiagnosticInfo.from_binary(data)
        return obj
    
    def __str__(self):
        return 'TranslateBrowsePathsToNodeIdsResult(' + 'Results:' + str(self.Results) + ', '  + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'
    
    __repr__ = __str__
    
class TranslateBrowsePathsToNodeIdsResponse(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.TranslateBrowsePathsToNodeIdsResponse_Encoding_DefaultBinary, NodeIdType.FourByte)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = TranslateBrowsePathsToNodeIdsResult()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = TranslateBrowsePathsToNodeIdsResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = TranslateBrowsePathsToNodeIdsResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'TranslateBrowsePathsToNodeIdsResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class RegisterNodesParameters(object):
    def __init__(self):
        self.NodesToRegister = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.NodesToRegister)))
        for i in self.NodesToRegister:
            packet.append(self.NodesToRegister.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = RegisterNodesParameters()
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.NodesToRegister = NodeId.from_binary(data)
        return obj
    
    def __str__(self):
        return 'RegisterNodesParameters(' + 'NodesToRegister:' + str(self.NodesToRegister) + ')'
    
    __repr__ = __str__
    
class RegisterNodesRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.RegisterNodesRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
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
        obj = RegisterNodesRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = RegisterNodesParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'RegisterNodesRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class RegisterNodesResult(object):
    def __init__(self):
        self.RegisteredNodeIds = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.RegisteredNodeIds)))
        for i in self.RegisteredNodeIds:
            packet.append(self.RegisteredNodeIds.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = RegisterNodesResult()
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.RegisteredNodeIds = NodeId.from_binary(data)
        return obj
    
    def __str__(self):
        return 'RegisterNodesResult(' + 'RegisteredNodeIds:' + str(self.RegisteredNodeIds) + ')'
    
    __repr__ = __str__
    
class RegisterNodesResponse(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.RegisterNodesResponse_Encoding_DefaultBinary, NodeIdType.FourByte)
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
        obj = RegisterNodesResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = RegisterNodesResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'RegisterNodesResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class UnregisterNodesParameters(object):
    def __init__(self):
        self.NodesToUnregister = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.NodesToUnregister)))
        for i in self.NodesToUnregister:
            packet.append(self.NodesToUnregister.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = UnregisterNodesParameters()
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.NodesToUnregister = NodeId.from_binary(data)
        return obj
    
    def __str__(self):
        return 'UnregisterNodesParameters(' + 'NodesToUnregister:' + str(self.NodesToUnregister) + ')'
    
    __repr__ = __str__
    
class UnregisterNodesRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.UnregisterNodesRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
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
        obj = UnregisterNodesRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = UnregisterNodesParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'UnregisterNodesRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class UnregisterNodesResponse(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.UnregisterNodesResponse_Encoding_DefaultBinary, NodeIdType.FourByte)
        self.ResponseHeader = ResponseHeader()
    
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
        return 'UnregisterNodesResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ')'
    
    __repr__ = __str__
    
class EndpointConfiguration(object):
    def __init__(self):
        self.OperationTimeout = 0
        self.UseBinaryEncoding = 0
        self.MaxStringLength = 0
        self.MaxByteStringLength = 0
        self.MaxArrayLength = 0
        self.MaxMessageSize = 0
        self.MaxBufferSize = 0
        self.ChannelLifetime = 0
        self.SecurityTokenLifetime = 0
    
    def to_binary(self):
        packet = []
        fmt = '<i'
        packet.append(struct.pack(fmt, self.OperationTimeout))
        fmt = '<?'
        packet.append(struct.pack(fmt, self.UseBinaryEncoding))
        fmt = '<i'
        packet.append(struct.pack(fmt, self.MaxStringLength))
        fmt = '<i'
        packet.append(struct.pack(fmt, self.MaxByteStringLength))
        fmt = '<i'
        packet.append(struct.pack(fmt, self.MaxArrayLength))
        fmt = '<i'
        packet.append(struct.pack(fmt, self.MaxMessageSize))
        fmt = '<i'
        packet.append(struct.pack(fmt, self.MaxBufferSize))
        fmt = '<i'
        packet.append(struct.pack(fmt, self.ChannelLifetime))
        fmt = '<i'
        packet.append(struct.pack(fmt, self.SecurityTokenLifetime))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = EndpointConfiguration()
        fmt = '<i'
        fmt_size = 4
        obj.OperationTimeout = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<?'
        fmt_size = 1
        obj.UseBinaryEncoding = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<i'
        fmt_size = 4
        obj.MaxStringLength = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<i'
        fmt_size = 4
        obj.MaxByteStringLength = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<i'
        fmt_size = 4
        obj.MaxArrayLength = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<i'
        fmt_size = 4
        obj.MaxMessageSize = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<i'
        fmt_size = 4
        obj.MaxBufferSize = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<i'
        fmt_size = 4
        obj.ChannelLifetime = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<i'
        fmt_size = 4
        obj.SecurityTokenLifetime = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'EndpointConfiguration(' + 'OperationTimeout:' + str(self.OperationTimeout) + ', '  + \
             'UseBinaryEncoding:' + str(self.UseBinaryEncoding) + ', '  + \
             'MaxStringLength:' + str(self.MaxStringLength) + ', '  + \
             'MaxByteStringLength:' + str(self.MaxByteStringLength) + ', '  + \
             'MaxArrayLength:' + str(self.MaxArrayLength) + ', '  + \
             'MaxMessageSize:' + str(self.MaxMessageSize) + ', '  + \
             'MaxBufferSize:' + str(self.MaxBufferSize) + ', '  + \
             'ChannelLifetime:' + str(self.ChannelLifetime) + ', '  + \
             'SecurityTokenLifetime:' + str(self.SecurityTokenLifetime) + ')'
    
    __repr__ = __str__
    
class SupportedProfile(object):
    def __init__(self):
        self.OrganizationUri = ''
        self.ProfileId = ''
        self.ComplianceTool = ''
        self.ComplianceDate = DateTime()
        self.ComplianceLevel = 0
        self.UnsupportedUnitIds = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.OrganizationUri)))
        packet.append(struct.pack('<{}s'.format(len(self.OrganizationUri)), self.OrganizationUri.encode()))
        packet.append(struct.pack('<i', len(self.ProfileId)))
        packet.append(struct.pack('<{}s'.format(len(self.ProfileId)), self.ProfileId.encode()))
        packet.append(struct.pack('<i', len(self.ComplianceTool)))
        packet.append(struct.pack('<{}s'.format(len(self.ComplianceTool)), self.ComplianceTool.encode()))
        packet.append(self.ComplianceDate.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.ComplianceLevel))
        packet.append(struct.pack('<i', len(self.UnsupportedUnitIds)))
        for i in self.UnsupportedUnitIds:
            packet.append(struct.pack('<i', len(self.UnsupportedUnitIds)))
            packet.append(struct.pack('<{}s'.format(len(self.UnsupportedUnitIds)), self.UnsupportedUnitIds.encode()))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = SupportedProfile()
        slength = struct.unpack('<i', data.red(1))
        obj.OrganizationUri = struct.unpack('<{}s'.format(slength), data.read(slength))
        slength = struct.unpack('<i', data.red(1))
        obj.ProfileId = struct.unpack('<{}s'.format(slength), data.read(slength))
        slength = struct.unpack('<i', data.red(1))
        obj.ComplianceTool = struct.unpack('<{}s'.format(slength), data.read(slength))
        obj.ComplianceDate = DateTime.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.ComplianceLevel = struct.unpack(fmt, data.read(fmt_size))[0]
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                slength = struct.unpack('<i', data.red(1))
                obj.UnsupportedUnitIds = struct.unpack('<{}s'.format(slength), data.read(slength))
        return obj
    
    def __str__(self):
        return 'SupportedProfile(' + 'OrganizationUri:' + str(self.OrganizationUri) + ', '  + \
             'ProfileId:' + str(self.ProfileId) + ', '  + \
             'ComplianceTool:' + str(self.ComplianceTool) + ', '  + \
             'ComplianceDate:' + str(self.ComplianceDate) + ', '  + \
             'ComplianceLevel:' + str(self.ComplianceLevel) + ', '  + \
             'UnsupportedUnitIds:' + str(self.UnsupportedUnitIds) + ')'
    
    __repr__ = __str__
    
class SoftwareCertificate(object):
    def __init__(self):
        self.ProductName = ''
        self.ProductUri = ''
        self.VendorName = ''
        self.VendorProductCertificate = ByteString()
        self.SoftwareVersion = ''
        self.BuildNumber = ''
        self.BuildDate = DateTime()
        self.IssuedBy = ''
        self.IssueDate = DateTime()
        self.SupportedProfiles = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.ProductName)))
        packet.append(struct.pack('<{}s'.format(len(self.ProductName)), self.ProductName.encode()))
        packet.append(struct.pack('<i', len(self.ProductUri)))
        packet.append(struct.pack('<{}s'.format(len(self.ProductUri)), self.ProductUri.encode()))
        packet.append(struct.pack('<i', len(self.VendorName)))
        packet.append(struct.pack('<{}s'.format(len(self.VendorName)), self.VendorName.encode()))
        packet.append(self.VendorProductCertificate.to_binary())
        packet.append(struct.pack('<i', len(self.SoftwareVersion)))
        packet.append(struct.pack('<{}s'.format(len(self.SoftwareVersion)), self.SoftwareVersion.encode()))
        packet.append(struct.pack('<i', len(self.BuildNumber)))
        packet.append(struct.pack('<{}s'.format(len(self.BuildNumber)), self.BuildNumber.encode()))
        packet.append(self.BuildDate.to_binary())
        packet.append(struct.pack('<i', len(self.IssuedBy)))
        packet.append(struct.pack('<{}s'.format(len(self.IssuedBy)), self.IssuedBy.encode()))
        packet.append(self.IssueDate.to_binary())
        packet.append(struct.pack('<i', len(self.SupportedProfiles)))
        for i in self.SupportedProfiles:
            packet.append(self.SupportedProfiles.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = SoftwareCertificate()
        slength = struct.unpack('<i', data.red(1))
        obj.ProductName = struct.unpack('<{}s'.format(slength), data.read(slength))
        slength = struct.unpack('<i', data.red(1))
        obj.ProductUri = struct.unpack('<{}s'.format(slength), data.read(slength))
        slength = struct.unpack('<i', data.red(1))
        obj.VendorName = struct.unpack('<{}s'.format(slength), data.read(slength))
        obj.VendorProductCertificate = ByteString.from_binary(data)
        slength = struct.unpack('<i', data.red(1))
        obj.SoftwareVersion = struct.unpack('<{}s'.format(slength), data.read(slength))
        slength = struct.unpack('<i', data.red(1))
        obj.BuildNumber = struct.unpack('<{}s'.format(slength), data.read(slength))
        obj.BuildDate = DateTime.from_binary(data)
        slength = struct.unpack('<i', data.red(1))
        obj.IssuedBy = struct.unpack('<{}s'.format(slength), data.read(slength))
        obj.IssueDate = DateTime.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.SupportedProfiles = SupportedProfile.from_binary(data)
        return obj
    
    def __str__(self):
        return 'SoftwareCertificate(' + 'ProductName:' + str(self.ProductName) + ', '  + \
             'ProductUri:' + str(self.ProductUri) + ', '  + \
             'VendorName:' + str(self.VendorName) + ', '  + \
             'VendorProductCertificate:' + str(self.VendorProductCertificate) + ', '  + \
             'SoftwareVersion:' + str(self.SoftwareVersion) + ', '  + \
             'BuildNumber:' + str(self.BuildNumber) + ', '  + \
             'BuildDate:' + str(self.BuildDate) + ', '  + \
             'IssuedBy:' + str(self.IssuedBy) + ', '  + \
             'IssueDate:' + str(self.IssueDate) + ', '  + \
             'SupportedProfiles:' + str(self.SupportedProfiles) + ')'
    
    __repr__ = __str__
    
class QueryDataDescription(object):
    def __init__(self):
        self.RelativePath = RelativePath()
        self.AttributeId = 0
        self.IndexRange = ''
    
    def to_binary(self):
        packet = []
        packet.append(self.RelativePath.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.AttributeId))
        packet.append(struct.pack('<i', len(self.IndexRange)))
        packet.append(struct.pack('<{}s'.format(len(self.IndexRange)), self.IndexRange.encode()))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = QueryDataDescription()
        obj.RelativePath = RelativePath.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.AttributeId = struct.unpack(fmt, data.read(fmt_size))[0]
        slength = struct.unpack('<i', data.red(1))
        obj.IndexRange = struct.unpack('<{}s'.format(slength), data.read(slength))
        return obj
    
    def __str__(self):
        return 'QueryDataDescription(' + 'RelativePath:' + str(self.RelativePath) + ', '  + \
             'AttributeId:' + str(self.AttributeId) + ', '  + \
             'IndexRange:' + str(self.IndexRange) + ')'
    
    __repr__ = __str__
    
class NodeTypeDescription(object):
    def __init__(self):
        self.TypeDefinitionNode = ExpandedNodeId()
        self.IncludeSubTypes = 0
        self.DataToReturn = []
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeDefinitionNode.to_binary())
        fmt = '<?'
        packet.append(struct.pack(fmt, self.IncludeSubTypes))
        packet.append(struct.pack('<i', len(self.DataToReturn)))
        for i in self.DataToReturn:
            packet.append(self.DataToReturn.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = NodeTypeDescription()
        obj.TypeDefinitionNode = ExpandedNodeId.from_binary(data)
        fmt = '<?'
        fmt_size = 1
        obj.IncludeSubTypes = struct.unpack(fmt, data.read(fmt_size))[0]
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.DataToReturn = QueryDataDescription.from_binary(data)
        return obj
    
    def __str__(self):
        return 'NodeTypeDescription(' + 'TypeDefinitionNode:' + str(self.TypeDefinitionNode) + ', '  + \
             'IncludeSubTypes:' + str(self.IncludeSubTypes) + ', '  + \
             'DataToReturn:' + str(self.DataToReturn) + ')'
    
    __repr__ = __str__
    
class QueryDataSet(object):
    def __init__(self):
        self.NodeId = ExpandedNodeId()
        self.TypeDefinitionNode = ExpandedNodeId()
        self.Values = []
    
    def to_binary(self):
        packet = []
        packet.append(self.NodeId.to_binary())
        packet.append(self.TypeDefinitionNode.to_binary())
        packet.append(struct.pack('<i', len(self.Values)))
        for i in self.Values:
            packet.append(self.Values.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = QueryDataSet()
        obj.NodeId = ExpandedNodeId.from_binary(data)
        obj.TypeDefinitionNode = ExpandedNodeId.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.Values = Variant.from_binary(data)
        return obj
    
    def __str__(self):
        return 'QueryDataSet(' + 'NodeId:' + str(self.NodeId) + ', '  + \
             'TypeDefinitionNode:' + str(self.TypeDefinitionNode) + ', '  + \
             'Values:' + str(self.Values) + ')'
    
    __repr__ = __str__
    
class NodeReference(object):
    def __init__(self):
        self.NodeId = NodeId()
        self.ReferenceTypeId = NodeId()
        self.IsForward = 0
        self.ReferencedNodeIds = []
    
    def to_binary(self):
        packet = []
        packet.append(self.NodeId.to_binary())
        packet.append(self.ReferenceTypeId.to_binary())
        fmt = '<?'
        packet.append(struct.pack(fmt, self.IsForward))
        packet.append(struct.pack('<i', len(self.ReferencedNodeIds)))
        for i in self.ReferencedNodeIds:
            packet.append(self.ReferencedNodeIds.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = NodeReference()
        obj.NodeId = NodeId.from_binary(data)
        obj.ReferenceTypeId = NodeId.from_binary(data)
        fmt = '<?'
        fmt_size = 1
        obj.IsForward = struct.unpack(fmt, data.read(fmt_size))[0]
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.ReferencedNodeIds = NodeId.from_binary(data)
        return obj
    
    def __str__(self):
        return 'NodeReference(' + 'NodeId:' + str(self.NodeId) + ', '  + \
             'ReferenceTypeId:' + str(self.ReferenceTypeId) + ', '  + \
             'IsForward:' + str(self.IsForward) + ', '  + \
             'ReferencedNodeIds:' + str(self.ReferencedNodeIds) + ')'
    
    __repr__ = __str__
    
class ContentFilterElement(object):
    def __init__(self):
        self.FilterOperator = 0
        self.FilterOperands = []
    
    def to_binary(self):
        packet = []
        fmt = '<I'
        packet.append(struct.pack(fmt, self.FilterOperator))
        packet.append(struct.pack('<i', len(self.FilterOperands)))
        for i in self.FilterOperands:
            packet.append(self.FilterOperands.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ContentFilterElement()
        fmt = '<I'
        fmt_size = 4
        obj.FilterOperator = struct.unpack(fmt, data.read(fmt_size))[0]
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.FilterOperands = ExtensionObject.from_binary(data)
        return obj
    
    def __str__(self):
        return 'ContentFilterElement(' + 'FilterOperator:' + str(self.FilterOperator) + ', '  + \
             'FilterOperands:' + str(self.FilterOperands) + ')'
    
    __repr__ = __str__
    
class ContentFilter(object):
    def __init__(self):
        self.Elements = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.Elements)))
        for i in self.Elements:
            packet.append(self.Elements.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ContentFilter()
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.Elements = ContentFilterElement.from_binary(data)
        return obj
    
    def __str__(self):
        return 'ContentFilter(' + 'Elements:' + str(self.Elements) + ')'
    
    __repr__ = __str__
    
class ElementOperand(object):
    def __init__(self):
        self.TypeId = NodeId()
        self.Encoding = 0
        self.Body = ByteString()
        self.Index = 0
    
    def to_binary(self):
        packet = []
        if self.Body: self.Encoding |= (1 << 0)
        packet.append(self.TypeId.to_binary())
        fmt = '<B'
        packet.append(struct.pack(fmt, self.Encoding))
        if self.Body: 
            packet.append(self.Body.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.Index))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ElementOperand()
        obj.TypeId = NodeId.from_binary(data)
        fmt = '<B'
        fmt_size = 1
        obj.Encoding = struct.unpack(fmt, data.read(fmt_size))[0]
        if obj.Encoding & (1 << 0):
            obj.Body = ByteString.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.Index = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'ElementOperand(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'Body:' + str(self.Body) + ', '  + \
             'Index:' + str(self.Index) + ')'
    
    __repr__ = __str__
    
class LiteralOperand(object):
    def __init__(self):
        self.TypeId = NodeId()
        self.Encoding = 0
        self.Body = ByteString()
        self.Value = Variant()
    
    def to_binary(self):
        packet = []
        if self.Body: self.Encoding |= (1 << 0)
        packet.append(self.TypeId.to_binary())
        fmt = '<B'
        packet.append(struct.pack(fmt, self.Encoding))
        if self.Body: 
            packet.append(self.Body.to_binary())
        packet.append(self.Value.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = LiteralOperand()
        obj.TypeId = NodeId.from_binary(data)
        fmt = '<B'
        fmt_size = 1
        obj.Encoding = struct.unpack(fmt, data.read(fmt_size))[0]
        if obj.Encoding & (1 << 0):
            obj.Body = ByteString.from_binary(data)
        obj.Value = Variant.from_binary(data)
        return obj
    
    def __str__(self):
        return 'LiteralOperand(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'Body:' + str(self.Body) + ', '  + \
             'Value:' + str(self.Value) + ')'
    
    __repr__ = __str__
    
class AttributeOperand(object):
    def __init__(self):
        self.TypeId = NodeId()
        self.Encoding = 0
        self.Body = ByteString()
        self.NodeId = NodeId()
        self.Alias = ''
        self.BrowsePath = RelativePath()
        self.AttributeId = 0
        self.IndexRange = ''
    
    def to_binary(self):
        packet = []
        if self.Body: self.Encoding |= (1 << 0)
        packet.append(self.TypeId.to_binary())
        fmt = '<B'
        packet.append(struct.pack(fmt, self.Encoding))
        if self.Body: 
            packet.append(self.Body.to_binary())
        packet.append(self.NodeId.to_binary())
        packet.append(struct.pack('<i', len(self.Alias)))
        packet.append(struct.pack('<{}s'.format(len(self.Alias)), self.Alias.encode()))
        packet.append(self.BrowsePath.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.AttributeId))
        packet.append(struct.pack('<i', len(self.IndexRange)))
        packet.append(struct.pack('<{}s'.format(len(self.IndexRange)), self.IndexRange.encode()))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = AttributeOperand()
        obj.TypeId = NodeId.from_binary(data)
        fmt = '<B'
        fmt_size = 1
        obj.Encoding = struct.unpack(fmt, data.read(fmt_size))[0]
        if obj.Encoding & (1 << 0):
            obj.Body = ByteString.from_binary(data)
        obj.NodeId = NodeId.from_binary(data)
        slength = struct.unpack('<i', data.red(1))
        obj.Alias = struct.unpack('<{}s'.format(slength), data.read(slength))
        obj.BrowsePath = RelativePath.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.AttributeId = struct.unpack(fmt, data.read(fmt_size))[0]
        slength = struct.unpack('<i', data.red(1))
        obj.IndexRange = struct.unpack('<{}s'.format(slength), data.read(slength))
        return obj
    
    def __str__(self):
        return 'AttributeOperand(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'Body:' + str(self.Body) + ', '  + \
             'NodeId:' + str(self.NodeId) + ', '  + \
             'Alias:' + str(self.Alias) + ', '  + \
             'BrowsePath:' + str(self.BrowsePath) + ', '  + \
             'AttributeId:' + str(self.AttributeId) + ', '  + \
             'IndexRange:' + str(self.IndexRange) + ')'
    
    __repr__ = __str__
    
class SimpleAttributeOperand(object):
    def __init__(self):
        self.TypeId = NodeId()
        self.Encoding = 0
        self.Body = ByteString()
        self.TypeDefinitionId = NodeId()
        self.BrowsePath = []
        self.AttributeId = 0
        self.IndexRange = ''
    
    def to_binary(self):
        packet = []
        if self.Body: self.Encoding |= (1 << 0)
        packet.append(self.TypeId.to_binary())
        fmt = '<B'
        packet.append(struct.pack(fmt, self.Encoding))
        if self.Body: 
            packet.append(self.Body.to_binary())
        packet.append(self.TypeDefinitionId.to_binary())
        packet.append(struct.pack('<i', len(self.BrowsePath)))
        for i in self.BrowsePath:
            packet.append(self.BrowsePath.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.AttributeId))
        packet.append(struct.pack('<i', len(self.IndexRange)))
        packet.append(struct.pack('<{}s'.format(len(self.IndexRange)), self.IndexRange.encode()))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = SimpleAttributeOperand()
        obj.TypeId = NodeId.from_binary(data)
        fmt = '<B'
        fmt_size = 1
        obj.Encoding = struct.unpack(fmt, data.read(fmt_size))[0]
        if obj.Encoding & (1 << 0):
            obj.Body = ByteString.from_binary(data)
        obj.TypeDefinitionId = NodeId.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.BrowsePath = QualifiedName.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.AttributeId = struct.unpack(fmt, data.read(fmt_size))[0]
        slength = struct.unpack('<i', data.red(1))
        obj.IndexRange = struct.unpack('<{}s'.format(slength), data.read(slength))
        return obj
    
    def __str__(self):
        return 'SimpleAttributeOperand(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'Body:' + str(self.Body) + ', '  + \
             'TypeDefinitionId:' + str(self.TypeDefinitionId) + ', '  + \
             'BrowsePath:' + str(self.BrowsePath) + ', '  + \
             'AttributeId:' + str(self.AttributeId) + ', '  + \
             'IndexRange:' + str(self.IndexRange) + ')'
    
    __repr__ = __str__
    
class ContentFilterElementResult(object):
    def __init__(self):
        self.StatusCode = StatusCode()
        self.OperandStatusCodes = []
        self.OperandDiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        packet.append(self.StatusCode.to_binary())
        packet.append(struct.pack('<i', len(self.OperandStatusCodes)))
        for i in self.OperandStatusCodes:
            packet.append(self.OperandStatusCodes.to_binary())
        packet.append(struct.pack('<i', len(self.OperandDiagnosticInfos)))
        for i in self.OperandDiagnosticInfos:
            packet.append(self.OperandDiagnosticInfos.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ContentFilterElementResult()
        obj.StatusCode = StatusCode.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.OperandStatusCodes = StatusCode.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.OperandDiagnosticInfos = DiagnosticInfo.from_binary(data)
        return obj
    
    def __str__(self):
        return 'ContentFilterElementResult(' + 'StatusCode:' + str(self.StatusCode) + ', '  + \
             'OperandStatusCodes:' + str(self.OperandStatusCodes) + ', '  + \
             'OperandDiagnosticInfos:' + str(self.OperandDiagnosticInfos) + ')'
    
    __repr__ = __str__
    
class ContentFilterResult(object):
    def __init__(self):
        self.ElementResults = []
        self.ElementDiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.ElementResults)))
        for i in self.ElementResults:
            packet.append(self.ElementResults.to_binary())
        packet.append(struct.pack('<i', len(self.ElementDiagnosticInfos)))
        for i in self.ElementDiagnosticInfos:
            packet.append(self.ElementDiagnosticInfos.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ContentFilterResult()
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.ElementResults = ContentFilterElementResult.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.ElementDiagnosticInfos = DiagnosticInfo.from_binary(data)
        return obj
    
    def __str__(self):
        return 'ContentFilterResult(' + 'ElementResults:' + str(self.ElementResults) + ', '  + \
             'ElementDiagnosticInfos:' + str(self.ElementDiagnosticInfos) + ')'
    
    __repr__ = __str__
    
class ParsingResult(object):
    def __init__(self):
        self.StatusCode = StatusCode()
        self.DataStatusCodes = []
        self.DataDiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        packet.append(self.StatusCode.to_binary())
        packet.append(struct.pack('<i', len(self.DataStatusCodes)))
        for i in self.DataStatusCodes:
            packet.append(self.DataStatusCodes.to_binary())
        packet.append(struct.pack('<i', len(self.DataDiagnosticInfos)))
        for i in self.DataDiagnosticInfos:
            packet.append(self.DataDiagnosticInfos.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ParsingResult()
        obj.StatusCode = StatusCode.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.DataStatusCodes = StatusCode.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.DataDiagnosticInfos = DiagnosticInfo.from_binary(data)
        return obj
    
    def __str__(self):
        return 'ParsingResult(' + 'StatusCode:' + str(self.StatusCode) + ', '  + \
             'DataStatusCodes:' + str(self.DataStatusCodes) + ', '  + \
             'DataDiagnosticInfos:' + str(self.DataDiagnosticInfos) + ')'
    
    __repr__ = __str__
    
class QueryFirstParameters(object):
    def __init__(self):
        self.View = ViewDescription()
        self.NodeTypes = []
        self.Filter = ContentFilter()
        self.MaxDataSetsToReturn = 0
        self.MaxReferencesToReturn = 0
    
    def to_binary(self):
        packet = []
        packet.append(self.View.to_binary())
        packet.append(struct.pack('<i', len(self.NodeTypes)))
        for i in self.NodeTypes:
            packet.append(self.NodeTypes.to_binary())
        packet.append(self.Filter.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.MaxDataSetsToReturn))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.MaxReferencesToReturn))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = QueryFirstParameters()
        obj.View = ViewDescription.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.NodeTypes = NodeTypeDescription.from_binary(data)
        obj.Filter = ContentFilter.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.MaxDataSetsToReturn = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.MaxReferencesToReturn = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'QueryFirstParameters(' + 'View:' + str(self.View) + ', '  + \
             'NodeTypes:' + str(self.NodeTypes) + ', '  + \
             'Filter:' + str(self.Filter) + ', '  + \
             'MaxDataSetsToReturn:' + str(self.MaxDataSetsToReturn) + ', '  + \
             'MaxReferencesToReturn:' + str(self.MaxReferencesToReturn) + ')'
    
    __repr__ = __str__
    
class QueryFirstRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.QueryFirstRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
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
        obj = QueryFirstRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = QueryFirstParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'QueryFirstRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class QueryFirstResult(object):
    def __init__(self):
        self.QueryDataSets = []
        self.ContinuationPoint = ByteString()
        self.ParsingResults = []
        self.DiagnosticInfos = []
        self.FilterResult = ContentFilterResult()
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.QueryDataSets)))
        for i in self.QueryDataSets:
            packet.append(self.QueryDataSets.to_binary())
        packet.append(self.ContinuationPoint.to_binary())
        packet.append(struct.pack('<i', len(self.ParsingResults)))
        for i in self.ParsingResults:
            packet.append(self.ParsingResults.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for i in self.DiagnosticInfos:
            packet.append(self.DiagnosticInfos.to_binary())
        packet.append(self.FilterResult.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = QueryFirstResult()
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.QueryDataSets = QueryDataSet.from_binary(data)
        obj.ContinuationPoint = ByteString.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.ParsingResults = ParsingResult.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.DiagnosticInfos = DiagnosticInfo.from_binary(data)
        obj.FilterResult = ContentFilterResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'QueryFirstResult(' + 'QueryDataSets:' + str(self.QueryDataSets) + ', '  + \
             'ContinuationPoint:' + str(self.ContinuationPoint) + ', '  + \
             'ParsingResults:' + str(self.ParsingResults) + ', '  + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ', '  + \
             'FilterResult:' + str(self.FilterResult) + ')'
    
    __repr__ = __str__
    
class QueryFirstResponse(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.QueryFirstResponse_Encoding_DefaultBinary, NodeIdType.FourByte)
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
        obj = QueryFirstResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = QueryFirstResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'QueryFirstResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class QueryNextParameters(object):
    def __init__(self):
        self.ReleaseContinuationPoint = 0
        self.ContinuationPoint = ByteString()
    
    def to_binary(self):
        packet = []
        fmt = '<?'
        packet.append(struct.pack(fmt, self.ReleaseContinuationPoint))
        packet.append(self.ContinuationPoint.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = QueryNextParameters()
        fmt = '<?'
        fmt_size = 1
        obj.ReleaseContinuationPoint = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.ContinuationPoint = ByteString.from_binary(data)
        return obj
    
    def __str__(self):
        return 'QueryNextParameters(' + 'ReleaseContinuationPoint:' + str(self.ReleaseContinuationPoint) + ', '  + \
             'ContinuationPoint:' + str(self.ContinuationPoint) + ')'
    
    __repr__ = __str__
    
class QueryNextRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.QueryNextRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
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
        obj = QueryNextRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = QueryNextParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'QueryNextRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class QueryNextResult(object):
    def __init__(self):
        self.QueryDataSets = []
        self.RevisedContinuationPoint = ByteString()
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.QueryDataSets)))
        for i in self.QueryDataSets:
            packet.append(self.QueryDataSets.to_binary())
        packet.append(self.RevisedContinuationPoint.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = QueryNextResult()
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.QueryDataSets = QueryDataSet.from_binary(data)
        obj.RevisedContinuationPoint = ByteString.from_binary(data)
        return obj
    
    def __str__(self):
        return 'QueryNextResult(' + 'QueryDataSets:' + str(self.QueryDataSets) + ', '  + \
             'RevisedContinuationPoint:' + str(self.RevisedContinuationPoint) + ')'
    
    __repr__ = __str__
    
class QueryNextResponse(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.QueryNextResponse_Encoding_DefaultBinary, NodeIdType.FourByte)
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
        obj = QueryNextResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = QueryNextResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'QueryNextResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class ReadValueId(object):
    def __init__(self):
        self.NodeId = NodeId()
        self.AttributeId = 0
        self.IndexRange = ''
        self.DataEncoding = QualifiedName()
    
    def to_binary(self):
        packet = []
        packet.append(self.NodeId.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.AttributeId))
        packet.append(struct.pack('<i', len(self.IndexRange)))
        packet.append(struct.pack('<{}s'.format(len(self.IndexRange)), self.IndexRange.encode()))
        packet.append(self.DataEncoding.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ReadValueId()
        obj.NodeId = NodeId.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.AttributeId = struct.unpack(fmt, data.read(fmt_size))[0]
        slength = struct.unpack('<i', data.red(1))
        obj.IndexRange = struct.unpack('<{}s'.format(slength), data.read(slength))
        obj.DataEncoding = QualifiedName.from_binary(data)
        return obj
    
    def __str__(self):
        return 'ReadValueId(' + 'NodeId:' + str(self.NodeId) + ', '  + \
             'AttributeId:' + str(self.AttributeId) + ', '  + \
             'IndexRange:' + str(self.IndexRange) + ', '  + \
             'DataEncoding:' + str(self.DataEncoding) + ')'
    
    __repr__ = __str__
    
class ReadParameters(object):
    def __init__(self):
        self.MaxAge = 0
        self.TimestampsToReturn = 0
        self.NodesToRead = []
    
    def to_binary(self):
        packet = []
        fmt = '<d'
        packet.append(struct.pack(fmt, self.MaxAge))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.TimestampsToReturn))
        packet.append(struct.pack('<i', len(self.NodesToRead)))
        for i in self.NodesToRead:
            packet.append(self.NodesToRead.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ReadParameters()
        fmt = '<d'
        fmt_size = 8
        obj.MaxAge = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.TimestampsToReturn = struct.unpack(fmt, data.read(fmt_size))[0]
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.NodesToRead = ReadValueId.from_binary(data)
        return obj
    
    def __str__(self):
        return 'ReadParameters(' + 'MaxAge:' + str(self.MaxAge) + ', '  + \
             'TimestampsToReturn:' + str(self.TimestampsToReturn) + ', '  + \
             'NodesToRead:' + str(self.NodesToRead) + ')'
    
    __repr__ = __str__
    
class ReadRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.ReadRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
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
        obj = ReadRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = ReadParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'ReadRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class ReadResult(object):
    def __init__(self):
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.Results)))
        for i in self.Results:
            packet.append(self.Results.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for i in self.DiagnosticInfos:
            packet.append(self.DiagnosticInfos.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ReadResult()
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.Results = DataValue.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.DiagnosticInfos = DiagnosticInfo.from_binary(data)
        return obj
    
    def __str__(self):
        return 'ReadResult(' + 'Results:' + str(self.Results) + ', '  + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'
    
    __repr__ = __str__
    
class ReadResponse(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.ReadResponse_Encoding_DefaultBinary, NodeIdType.FourByte)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = ReadResult()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ReadResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = ReadResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'ReadResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class HistoryReadValueId(object):
    def __init__(self):
        self.NodeId = NodeId()
        self.IndexRange = ''
        self.DataEncoding = QualifiedName()
        self.ContinuationPoint = ByteString()
    
    def to_binary(self):
        packet = []
        packet.append(self.NodeId.to_binary())
        packet.append(struct.pack('<i', len(self.IndexRange)))
        packet.append(struct.pack('<{}s'.format(len(self.IndexRange)), self.IndexRange.encode()))
        packet.append(self.DataEncoding.to_binary())
        packet.append(self.ContinuationPoint.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = HistoryReadValueId()
        obj.NodeId = NodeId.from_binary(data)
        slength = struct.unpack('<i', data.red(1))
        obj.IndexRange = struct.unpack('<{}s'.format(slength), data.read(slength))
        obj.DataEncoding = QualifiedName.from_binary(data)
        obj.ContinuationPoint = ByteString.from_binary(data)
        return obj
    
    def __str__(self):
        return 'HistoryReadValueId(' + 'NodeId:' + str(self.NodeId) + ', '  + \
             'IndexRange:' + str(self.IndexRange) + ', '  + \
             'DataEncoding:' + str(self.DataEncoding) + ', '  + \
             'ContinuationPoint:' + str(self.ContinuationPoint) + ')'
    
    __repr__ = __str__
    
class HistoryReadResult(object):
    def __init__(self):
        self.StatusCode = StatusCode()
        self.ContinuationPoint = ByteString()
        self.HistoryData = ExtensionObject()
    
    def to_binary(self):
        packet = []
        packet.append(self.StatusCode.to_binary())
        packet.append(self.ContinuationPoint.to_binary())
        packet.append(self.HistoryData.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = HistoryReadResult()
        obj.StatusCode = StatusCode.from_binary(data)
        obj.ContinuationPoint = ByteString.from_binary(data)
        obj.HistoryData = ExtensionObject.from_binary(data)
        return obj
    
    def __str__(self):
        return 'HistoryReadResult(' + 'StatusCode:' + str(self.StatusCode) + ', '  + \
             'ContinuationPoint:' + str(self.ContinuationPoint) + ', '  + \
             'HistoryData:' + str(self.HistoryData) + ')'
    
    __repr__ = __str__
    
class HistoryReadDetails(object):
    def __init__(self):
        self.TypeId = NodeId()
        self.Encoding = 0
        self.Body = ByteString()
    
    def to_binary(self):
        packet = []
        if self.Body: self.Encoding |= (1 << 0)
        packet.append(self.TypeId.to_binary())
        fmt = '<B'
        packet.append(struct.pack(fmt, self.Encoding))
        if self.Body: 
            packet.append(self.Body.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = HistoryReadDetails()
        obj.TypeId = NodeId.from_binary(data)
        fmt = '<B'
        fmt_size = 1
        obj.Encoding = struct.unpack(fmt, data.read(fmt_size))[0]
        if obj.Encoding & (1 << 0):
            obj.Body = ByteString.from_binary(data)
        return obj
    
    def __str__(self):
        return 'HistoryReadDetails(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'Body:' + str(self.Body) + ')'
    
    __repr__ = __str__
    
class ReadEventDetails(object):
    def __init__(self):
        self.TypeId = NodeId()
        self.Encoding = 0
        self.Body = ByteString()
        self.NumValuesPerNode = 0
        self.StartTime = DateTime()
        self.EndTime = DateTime()
        self.Filter = EventFilter()
    
    def to_binary(self):
        packet = []
        if self.Body: self.Encoding |= (1 << 0)
        packet.append(self.TypeId.to_binary())
        fmt = '<B'
        packet.append(struct.pack(fmt, self.Encoding))
        if self.Body: 
            packet.append(self.Body.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.NumValuesPerNode))
        packet.append(self.StartTime.to_binary())
        packet.append(self.EndTime.to_binary())
        packet.append(self.Filter.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ReadEventDetails()
        obj.TypeId = NodeId.from_binary(data)
        fmt = '<B'
        fmt_size = 1
        obj.Encoding = struct.unpack(fmt, data.read(fmt_size))[0]
        if obj.Encoding & (1 << 0):
            obj.Body = ByteString.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.NumValuesPerNode = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.StartTime = DateTime.from_binary(data)
        obj.EndTime = DateTime.from_binary(data)
        obj.Filter = EventFilter.from_binary(data)
        return obj
    
    def __str__(self):
        return 'ReadEventDetails(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'Body:' + str(self.Body) + ', '  + \
             'NumValuesPerNode:' + str(self.NumValuesPerNode) + ', '  + \
             'StartTime:' + str(self.StartTime) + ', '  + \
             'EndTime:' + str(self.EndTime) + ', '  + \
             'Filter:' + str(self.Filter) + ')'
    
    __repr__ = __str__
    
class ReadRawModifiedDetails(object):
    def __init__(self):
        self.TypeId = NodeId()
        self.Encoding = 0
        self.Body = ByteString()
        self.IsReadModified = 0
        self.StartTime = DateTime()
        self.EndTime = DateTime()
        self.NumValuesPerNode = 0
        self.ReturnBounds = 0
    
    def to_binary(self):
        packet = []
        if self.Body: self.Encoding |= (1 << 0)
        packet.append(self.TypeId.to_binary())
        fmt = '<B'
        packet.append(struct.pack(fmt, self.Encoding))
        if self.Body: 
            packet.append(self.Body.to_binary())
        fmt = '<?'
        packet.append(struct.pack(fmt, self.IsReadModified))
        packet.append(self.StartTime.to_binary())
        packet.append(self.EndTime.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.NumValuesPerNode))
        fmt = '<?'
        packet.append(struct.pack(fmt, self.ReturnBounds))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ReadRawModifiedDetails()
        obj.TypeId = NodeId.from_binary(data)
        fmt = '<B'
        fmt_size = 1
        obj.Encoding = struct.unpack(fmt, data.read(fmt_size))[0]
        if obj.Encoding & (1 << 0):
            obj.Body = ByteString.from_binary(data)
        fmt = '<?'
        fmt_size = 1
        obj.IsReadModified = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.StartTime = DateTime.from_binary(data)
        obj.EndTime = DateTime.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.NumValuesPerNode = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<?'
        fmt_size = 1
        obj.ReturnBounds = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'ReadRawModifiedDetails(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'Body:' + str(self.Body) + ', '  + \
             'IsReadModified:' + str(self.IsReadModified) + ', '  + \
             'StartTime:' + str(self.StartTime) + ', '  + \
             'EndTime:' + str(self.EndTime) + ', '  + \
             'NumValuesPerNode:' + str(self.NumValuesPerNode) + ', '  + \
             'ReturnBounds:' + str(self.ReturnBounds) + ')'
    
    __repr__ = __str__
    
class ReadProcessedDetails(object):
    def __init__(self):
        self.TypeId = NodeId()
        self.Encoding = 0
        self.Body = ByteString()
        self.StartTime = DateTime()
        self.EndTime = DateTime()
        self.ProcessingInterval = 0
        self.AggregateType = []
        self.AggregateConfiguration = AggregateConfiguration()
    
    def to_binary(self):
        packet = []
        if self.Body: self.Encoding |= (1 << 0)
        packet.append(self.TypeId.to_binary())
        fmt = '<B'
        packet.append(struct.pack(fmt, self.Encoding))
        if self.Body: 
            packet.append(self.Body.to_binary())
        packet.append(self.StartTime.to_binary())
        packet.append(self.EndTime.to_binary())
        fmt = '<d'
        packet.append(struct.pack(fmt, self.ProcessingInterval))
        packet.append(struct.pack('<i', len(self.AggregateType)))
        for i in self.AggregateType:
            packet.append(self.AggregateType.to_binary())
        packet.append(self.AggregateConfiguration.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ReadProcessedDetails()
        obj.TypeId = NodeId.from_binary(data)
        fmt = '<B'
        fmt_size = 1
        obj.Encoding = struct.unpack(fmt, data.read(fmt_size))[0]
        if obj.Encoding & (1 << 0):
            obj.Body = ByteString.from_binary(data)
        obj.StartTime = DateTime.from_binary(data)
        obj.EndTime = DateTime.from_binary(data)
        fmt = '<d'
        fmt_size = 8
        obj.ProcessingInterval = struct.unpack(fmt, data.read(fmt_size))[0]
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.AggregateType = NodeId.from_binary(data)
        obj.AggregateConfiguration = AggregateConfiguration.from_binary(data)
        return obj
    
    def __str__(self):
        return 'ReadProcessedDetails(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'Body:' + str(self.Body) + ', '  + \
             'StartTime:' + str(self.StartTime) + ', '  + \
             'EndTime:' + str(self.EndTime) + ', '  + \
             'ProcessingInterval:' + str(self.ProcessingInterval) + ', '  + \
             'AggregateType:' + str(self.AggregateType) + ', '  + \
             'AggregateConfiguration:' + str(self.AggregateConfiguration) + ')'
    
    __repr__ = __str__
    
class ReadAtTimeDetails(object):
    def __init__(self):
        self.TypeId = NodeId()
        self.Encoding = 0
        self.Body = ByteString()
        self.ReqTimes = []
        self.UseSimpleBounds = 0
    
    def to_binary(self):
        packet = []
        if self.Body: self.Encoding |= (1 << 0)
        packet.append(self.TypeId.to_binary())
        fmt = '<B'
        packet.append(struct.pack(fmt, self.Encoding))
        if self.Body: 
            packet.append(self.Body.to_binary())
        packet.append(struct.pack('<i', len(self.ReqTimes)))
        for i in self.ReqTimes:
            packet.append(self.ReqTimes.to_binary())
        fmt = '<?'
        packet.append(struct.pack(fmt, self.UseSimpleBounds))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ReadAtTimeDetails()
        obj.TypeId = NodeId.from_binary(data)
        fmt = '<B'
        fmt_size = 1
        obj.Encoding = struct.unpack(fmt, data.read(fmt_size))[0]
        if obj.Encoding & (1 << 0):
            obj.Body = ByteString.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.ReqTimes = DateTime.from_binary(data)
        fmt = '<?'
        fmt_size = 1
        obj.UseSimpleBounds = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'ReadAtTimeDetails(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'Body:' + str(self.Body) + ', '  + \
             'ReqTimes:' + str(self.ReqTimes) + ', '  + \
             'UseSimpleBounds:' + str(self.UseSimpleBounds) + ')'
    
    __repr__ = __str__
    
class HistoryData(object):
    def __init__(self):
        self.DataValues = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.DataValues)))
        for i in self.DataValues:
            packet.append(self.DataValues.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = HistoryData()
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.DataValues = DataValue.from_binary(data)
        return obj
    
    def __str__(self):
        return 'HistoryData(' + 'DataValues:' + str(self.DataValues) + ')'
    
    __repr__ = __str__
    
class ModificationInfo(object):
    def __init__(self):
        self.ModificationTime = DateTime()
        self.UpdateType = 0
        self.UserName = ''
    
    def to_binary(self):
        packet = []
        packet.append(self.ModificationTime.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.UpdateType))
        packet.append(struct.pack('<i', len(self.UserName)))
        packet.append(struct.pack('<{}s'.format(len(self.UserName)), self.UserName.encode()))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ModificationInfo()
        obj.ModificationTime = DateTime.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.UpdateType = struct.unpack(fmt, data.read(fmt_size))[0]
        slength = struct.unpack('<i', data.red(1))
        obj.UserName = struct.unpack('<{}s'.format(slength), data.read(slength))
        return obj
    
    def __str__(self):
        return 'ModificationInfo(' + 'ModificationTime:' + str(self.ModificationTime) + ', '  + \
             'UpdateType:' + str(self.UpdateType) + ', '  + \
             'UserName:' + str(self.UserName) + ')'
    
    __repr__ = __str__
    
class HistoryModifiedData(object):
    def __init__(self):
        self.DataValues = []
        self.ModificationInfos = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.DataValues)))
        for i in self.DataValues:
            packet.append(self.DataValues.to_binary())
        packet.append(struct.pack('<i', len(self.ModificationInfos)))
        for i in self.ModificationInfos:
            packet.append(self.ModificationInfos.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = HistoryModifiedData()
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.DataValues = DataValue.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.ModificationInfos = ModificationInfo.from_binary(data)
        return obj
    
    def __str__(self):
        return 'HistoryModifiedData(' + 'DataValues:' + str(self.DataValues) + ', '  + \
             'ModificationInfos:' + str(self.ModificationInfos) + ')'
    
    __repr__ = __str__
    
class HistoryEvent(object):
    def __init__(self):
        self.Events = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.Events)))
        for i in self.Events:
            packet.append(self.Events.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = HistoryEvent()
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.Events = HistoryEventFieldList.from_binary(data)
        return obj
    
    def __str__(self):
        return 'HistoryEvent(' + 'Events:' + str(self.Events) + ')'
    
    __repr__ = __str__
    
class HistoryReadParameters(object):
    def __init__(self):
        self.HistoryReadDetails = ExtensionObject()
        self.TimestampsToReturn = 0
        self.ReleaseContinuationPoints = 0
        self.NodesToRead = []
    
    def to_binary(self):
        packet = []
        packet.append(self.HistoryReadDetails.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.TimestampsToReturn))
        fmt = '<?'
        packet.append(struct.pack(fmt, self.ReleaseContinuationPoints))
        packet.append(struct.pack('<i', len(self.NodesToRead)))
        for i in self.NodesToRead:
            packet.append(self.NodesToRead.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = HistoryReadParameters()
        obj.HistoryReadDetails = ExtensionObject.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.TimestampsToReturn = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<?'
        fmt_size = 1
        obj.ReleaseContinuationPoints = struct.unpack(fmt, data.read(fmt_size))[0]
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.NodesToRead = HistoryReadValueId.from_binary(data)
        return obj
    
    def __str__(self):
        return 'HistoryReadParameters(' + 'HistoryReadDetails:' + str(self.HistoryReadDetails) + ', '  + \
             'TimestampsToReturn:' + str(self.TimestampsToReturn) + ', '  + \
             'ReleaseContinuationPoints:' + str(self.ReleaseContinuationPoints) + ', '  + \
             'NodesToRead:' + str(self.NodesToRead) + ')'
    
    __repr__ = __str__
    
class HistoryReadRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.HistoryReadRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
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
        obj = HistoryReadRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = HistoryReadParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'HistoryReadRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class HistoryReadResponse(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.HistoryReadResponse_Encoding_DefaultBinary, NodeIdType.FourByte)
        self.ResponseHeader = ResponseHeader()
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(struct.pack('<i', len(self.Results)))
        for i in self.Results:
            packet.append(self.Results.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for i in self.DiagnosticInfos:
            packet.append(self.DiagnosticInfos.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = HistoryReadResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.Results = HistoryReadResult.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.DiagnosticInfos = DiagnosticInfo.from_binary(data)
        return obj
    
    def __str__(self):
        return 'HistoryReadResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Results:' + str(self.Results) + ', '  + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'
    
    __repr__ = __str__
    
class WriteValue(object):
    def __init__(self):
        self.NodeId = NodeId()
        self.AttributeId = 0
        self.IndexRange = ''
        self.Value = DataValue()
    
    def to_binary(self):
        packet = []
        packet.append(self.NodeId.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.AttributeId))
        packet.append(struct.pack('<i', len(self.IndexRange)))
        packet.append(struct.pack('<{}s'.format(len(self.IndexRange)), self.IndexRange.encode()))
        packet.append(self.Value.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = WriteValue()
        obj.NodeId = NodeId.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.AttributeId = struct.unpack(fmt, data.read(fmt_size))[0]
        slength = struct.unpack('<i', data.red(1))
        obj.IndexRange = struct.unpack('<{}s'.format(slength), data.read(slength))
        obj.Value = DataValue.from_binary(data)
        return obj
    
    def __str__(self):
        return 'WriteValue(' + 'NodeId:' + str(self.NodeId) + ', '  + \
             'AttributeId:' + str(self.AttributeId) + ', '  + \
             'IndexRange:' + str(self.IndexRange) + ', '  + \
             'Value:' + str(self.Value) + ')'
    
    __repr__ = __str__
    
class WriteParameters(object):
    def __init__(self):
        self.NodesToWrite = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.NodesToWrite)))
        for i in self.NodesToWrite:
            packet.append(self.NodesToWrite.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = WriteParameters()
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.NodesToWrite = WriteValue.from_binary(data)
        return obj
    
    def __str__(self):
        return 'WriteParameters(' + 'NodesToWrite:' + str(self.NodesToWrite) + ')'
    
    __repr__ = __str__
    
class WriteRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.WriteRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
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
        obj = WriteRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = WriteParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'WriteRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class WriteResult(object):
    def __init__(self):
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.Results)))
        for i in self.Results:
            packet.append(self.Results.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for i in self.DiagnosticInfos:
            packet.append(self.DiagnosticInfos.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = WriteResult()
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.Results = StatusCode.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.DiagnosticInfos = DiagnosticInfo.from_binary(data)
        return obj
    
    def __str__(self):
        return 'WriteResult(' + 'Results:' + str(self.Results) + ', '  + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'
    
    __repr__ = __str__
    
class WriteResponse(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.WriteResponse_Encoding_DefaultBinary, NodeIdType.FourByte)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = WriteResult()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = WriteResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = WriteResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'WriteResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class HistoryUpdateDetails(object):
    def __init__(self):
        self.NodeId = NodeId()
    
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
    
class UpdateDataDetails(object):
    def __init__(self):
        self.NodeId = NodeId()
        self.PerformInsertReplace = 0
        self.UpdateValues = []
    
    def to_binary(self):
        packet = []
        packet.append(self.NodeId.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.PerformInsertReplace))
        packet.append(struct.pack('<i', len(self.UpdateValues)))
        for i in self.UpdateValues:
            packet.append(self.UpdateValues.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = UpdateDataDetails()
        obj.NodeId = NodeId.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.PerformInsertReplace = struct.unpack(fmt, data.read(fmt_size))[0]
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.UpdateValues = DataValue.from_binary(data)
        return obj
    
    def __str__(self):
        return 'UpdateDataDetails(' + 'NodeId:' + str(self.NodeId) + ', '  + \
             'PerformInsertReplace:' + str(self.PerformInsertReplace) + ', '  + \
             'UpdateValues:' + str(self.UpdateValues) + ')'
    
    __repr__ = __str__
    
class UpdateStructureDataDetails(object):
    def __init__(self):
        self.NodeId = NodeId()
        self.PerformInsertReplace = 0
        self.UpdateValues = []
    
    def to_binary(self):
        packet = []
        packet.append(self.NodeId.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.PerformInsertReplace))
        packet.append(struct.pack('<i', len(self.UpdateValues)))
        for i in self.UpdateValues:
            packet.append(self.UpdateValues.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = UpdateStructureDataDetails()
        obj.NodeId = NodeId.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.PerformInsertReplace = struct.unpack(fmt, data.read(fmt_size))[0]
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.UpdateValues = DataValue.from_binary(data)
        return obj
    
    def __str__(self):
        return 'UpdateStructureDataDetails(' + 'NodeId:' + str(self.NodeId) + ', '  + \
             'PerformInsertReplace:' + str(self.PerformInsertReplace) + ', '  + \
             'UpdateValues:' + str(self.UpdateValues) + ')'
    
    __repr__ = __str__
    
class UpdateEventDetails(object):
    def __init__(self):
        self.NodeId = NodeId()
        self.PerformInsertReplace = 0
        self.Filter = EventFilter()
        self.EventData = []
    
    def to_binary(self):
        packet = []
        packet.append(self.NodeId.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.PerformInsertReplace))
        packet.append(self.Filter.to_binary())
        packet.append(struct.pack('<i', len(self.EventData)))
        for i in self.EventData:
            packet.append(self.EventData.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = UpdateEventDetails()
        obj.NodeId = NodeId.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.PerformInsertReplace = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.Filter = EventFilter.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.EventData = HistoryEventFieldList.from_binary(data)
        return obj
    
    def __str__(self):
        return 'UpdateEventDetails(' + 'NodeId:' + str(self.NodeId) + ', '  + \
             'PerformInsertReplace:' + str(self.PerformInsertReplace) + ', '  + \
             'Filter:' + str(self.Filter) + ', '  + \
             'EventData:' + str(self.EventData) + ')'
    
    __repr__ = __str__
    
class DeleteRawModifiedDetails(object):
    def __init__(self):
        self.NodeId = NodeId()
        self.IsDeleteModified = 0
        self.StartTime = DateTime()
        self.EndTime = DateTime()
    
    def to_binary(self):
        packet = []
        packet.append(self.NodeId.to_binary())
        fmt = '<?'
        packet.append(struct.pack(fmt, self.IsDeleteModified))
        packet.append(self.StartTime.to_binary())
        packet.append(self.EndTime.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = DeleteRawModifiedDetails()
        obj.NodeId = NodeId.from_binary(data)
        fmt = '<?'
        fmt_size = 1
        obj.IsDeleteModified = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.StartTime = DateTime.from_binary(data)
        obj.EndTime = DateTime.from_binary(data)
        return obj
    
    def __str__(self):
        return 'DeleteRawModifiedDetails(' + 'NodeId:' + str(self.NodeId) + ', '  + \
             'IsDeleteModified:' + str(self.IsDeleteModified) + ', '  + \
             'StartTime:' + str(self.StartTime) + ', '  + \
             'EndTime:' + str(self.EndTime) + ')'
    
    __repr__ = __str__
    
class DeleteAtTimeDetails(object):
    def __init__(self):
        self.NodeId = NodeId()
        self.ReqTimes = []
    
    def to_binary(self):
        packet = []
        packet.append(self.NodeId.to_binary())
        packet.append(struct.pack('<i', len(self.ReqTimes)))
        for i in self.ReqTimes:
            packet.append(self.ReqTimes.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = DeleteAtTimeDetails()
        obj.NodeId = NodeId.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.ReqTimes = DateTime.from_binary(data)
        return obj
    
    def __str__(self):
        return 'DeleteAtTimeDetails(' + 'NodeId:' + str(self.NodeId) + ', '  + \
             'ReqTimes:' + str(self.ReqTimes) + ')'
    
    __repr__ = __str__
    
class DeleteEventDetails(object):
    def __init__(self):
        self.NodeId = NodeId()
        self.EventIds = []
    
    def to_binary(self):
        packet = []
        packet.append(self.NodeId.to_binary())
        packet.append(struct.pack('<i', len(self.EventIds)))
        for i in self.EventIds:
            packet.append(self.EventIds.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = DeleteEventDetails()
        obj.NodeId = NodeId.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.EventIds = ByteString.from_binary(data)
        return obj
    
    def __str__(self):
        return 'DeleteEventDetails(' + 'NodeId:' + str(self.NodeId) + ', '  + \
             'EventIds:' + str(self.EventIds) + ')'
    
    __repr__ = __str__
    
class HistoryUpdateResult(object):
    def __init__(self):
        self.StatusCode = StatusCode()
        self.OperationResults = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        packet.append(self.StatusCode.to_binary())
        packet.append(struct.pack('<i', len(self.OperationResults)))
        for i in self.OperationResults:
            packet.append(self.OperationResults.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for i in self.DiagnosticInfos:
            packet.append(self.DiagnosticInfos.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = HistoryUpdateResult()
        obj.StatusCode = StatusCode.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.OperationResults = StatusCode.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.DiagnosticInfos = DiagnosticInfo.from_binary(data)
        return obj
    
    def __str__(self):
        return 'HistoryUpdateResult(' + 'StatusCode:' + str(self.StatusCode) + ', '  + \
             'OperationResults:' + str(self.OperationResults) + ', '  + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'
    
    __repr__ = __str__
    
class HistoryUpdateEventResult(object):
    def __init__(self):
        self.StatusCode = StatusCode()
        self.EventFilterResult = EventFilterResult()
    
    def to_binary(self):
        packet = []
        packet.append(self.StatusCode.to_binary())
        packet.append(self.EventFilterResult.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = HistoryUpdateEventResult()
        obj.StatusCode = StatusCode.from_binary(data)
        obj.EventFilterResult = EventFilterResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'HistoryUpdateEventResult(' + 'StatusCode:' + str(self.StatusCode) + ', '  + \
             'EventFilterResult:' + str(self.EventFilterResult) + ')'
    
    __repr__ = __str__
    
class HistoryUpdateParameters(object):
    def __init__(self):
        self.HistoryUpdateDetails = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.HistoryUpdateDetails)))
        for i in self.HistoryUpdateDetails:
            packet.append(self.HistoryUpdateDetails.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = HistoryUpdateParameters()
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.HistoryUpdateDetails = ExtensionObject.from_binary(data)
        return obj
    
    def __str__(self):
        return 'HistoryUpdateParameters(' + 'HistoryUpdateDetails:' + str(self.HistoryUpdateDetails) + ')'
    
    __repr__ = __str__
    
class HistoryUpdateRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.HistoryUpdateRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
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
        obj = HistoryUpdateRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = HistoryUpdateParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'HistoryUpdateRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class HistoryUpdateResponse(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.HistoryUpdateResponse_Encoding_DefaultBinary, NodeIdType.FourByte)
        self.ResponseHeader = ResponseHeader()
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(struct.pack('<i', len(self.Results)))
        for i in self.Results:
            packet.append(self.Results.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for i in self.DiagnosticInfos:
            packet.append(self.DiagnosticInfos.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = HistoryUpdateResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.Results = HistoryUpdateResult.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.DiagnosticInfos = DiagnosticInfo.from_binary(data)
        return obj
    
    def __str__(self):
        return 'HistoryUpdateResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Results:' + str(self.Results) + ', '  + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'
    
    __repr__ = __str__
    
class CallMethodParameters(object):
    def __init__(self):
        self.MethodId = NodeId()
        self.InputArguments = []
    
    def to_binary(self):
        packet = []
        packet.append(self.MethodId.to_binary())
        packet.append(struct.pack('<i', len(self.InputArguments)))
        for i in self.InputArguments:
            packet.append(self.InputArguments.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = CallMethodParameters()
        obj.MethodId = NodeId.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.InputArguments = Variant.from_binary(data)
        return obj
    
    def __str__(self):
        return 'CallMethodParameters(' + 'MethodId:' + str(self.MethodId) + ', '  + \
             'InputArguments:' + str(self.InputArguments) + ')'
    
    __repr__ = __str__
    
class CallMethodRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.CallMethodRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
        self.ObjectId = NodeId()
        self.Parameters = CallMethodParameters()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ObjectId.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = CallMethodRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.ObjectId = NodeId.from_binary(data)
        obj.Parameters = CallMethodParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'CallMethodRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ObjectId:' + str(self.ObjectId) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class CallMethodResult(object):
    def __init__(self):
        self.StatusCode = StatusCode()
        self.InputArgumentResults = []
        self.InputArgumentDiagnosticInfos = []
        self.OutputArguments = []
    
    def to_binary(self):
        packet = []
        packet.append(self.StatusCode.to_binary())
        packet.append(struct.pack('<i', len(self.InputArgumentResults)))
        for i in self.InputArgumentResults:
            packet.append(self.InputArgumentResults.to_binary())
        packet.append(struct.pack('<i', len(self.InputArgumentDiagnosticInfos)))
        for i in self.InputArgumentDiagnosticInfos:
            packet.append(self.InputArgumentDiagnosticInfos.to_binary())
        packet.append(struct.pack('<i', len(self.OutputArguments)))
        for i in self.OutputArguments:
            packet.append(self.OutputArguments.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = CallMethodResult()
        obj.StatusCode = StatusCode.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.InputArgumentResults = StatusCode.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.InputArgumentDiagnosticInfos = DiagnosticInfo.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.OutputArguments = Variant.from_binary(data)
        return obj
    
    def __str__(self):
        return 'CallMethodResult(' + 'StatusCode:' + str(self.StatusCode) + ', '  + \
             'InputArgumentResults:' + str(self.InputArgumentResults) + ', '  + \
             'InputArgumentDiagnosticInfos:' + str(self.InputArgumentDiagnosticInfos) + ', '  + \
             'OutputArguments:' + str(self.OutputArguments) + ')'
    
    __repr__ = __str__
    
class CallParameters(object):
    def __init__(self):
        self.MethodsToCall = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.MethodsToCall)))
        for i in self.MethodsToCall:
            packet.append(self.MethodsToCall.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = CallParameters()
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.MethodsToCall = CallMethodRequest.from_binary(data)
        return obj
    
    def __str__(self):
        return 'CallParameters(' + 'MethodsToCall:' + str(self.MethodsToCall) + ')'
    
    __repr__ = __str__
    
class CallRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.CallRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
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
        obj = CallRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = CallParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'CallRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class CallResult(object):
    def __init__(self):
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.Results)))
        for i in self.Results:
            packet.append(self.Results.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for i in self.DiagnosticInfos:
            packet.append(self.DiagnosticInfos.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = CallResult()
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.Results = CallMethodResult.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.DiagnosticInfos = DiagnosticInfo.from_binary(data)
        return obj
    
    def __str__(self):
        return 'CallResult(' + 'Results:' + str(self.Results) + ', '  + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'
    
    __repr__ = __str__
    
class CallResponse(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.CallResponse_Encoding_DefaultBinary, NodeIdType.FourByte)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = CallResult()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = CallResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = CallResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'CallResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class MonitoringFilter(object):
    def __init__(self):
        self.TypeId = NodeId()
        self.Encoding = 0
        self.Body = ByteString()
    
    def to_binary(self):
        packet = []
        if self.Body: self.Encoding |= (1 << 0)
        packet.append(self.TypeId.to_binary())
        fmt = '<B'
        packet.append(struct.pack(fmt, self.Encoding))
        if self.Body: 
            packet.append(self.Body.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = MonitoringFilter()
        obj.TypeId = NodeId.from_binary(data)
        fmt = '<B'
        fmt_size = 1
        obj.Encoding = struct.unpack(fmt, data.read(fmt_size))[0]
        if obj.Encoding & (1 << 0):
            obj.Body = ByteString.from_binary(data)
        return obj
    
    def __str__(self):
        return 'MonitoringFilter(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'Body:' + str(self.Body) + ')'
    
    __repr__ = __str__
    
class DataChangeFilter(object):
    def __init__(self):
        self.TypeId = NodeId()
        self.Encoding = 0
        self.Body = ByteString()
        self.Trigger = 0
        self.DeadbandType = 0
        self.DeadbandValue = 0
    
    def to_binary(self):
        packet = []
        if self.Body: self.Encoding |= (1 << 0)
        packet.append(self.TypeId.to_binary())
        fmt = '<B'
        packet.append(struct.pack(fmt, self.Encoding))
        if self.Body: 
            packet.append(self.Body.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.Trigger))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.DeadbandType))
        fmt = '<d'
        packet.append(struct.pack(fmt, self.DeadbandValue))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = DataChangeFilter()
        obj.TypeId = NodeId.from_binary(data)
        fmt = '<B'
        fmt_size = 1
        obj.Encoding = struct.unpack(fmt, data.read(fmt_size))[0]
        if obj.Encoding & (1 << 0):
            obj.Body = ByteString.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.Trigger = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.DeadbandType = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<d'
        fmt_size = 8
        obj.DeadbandValue = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'DataChangeFilter(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'Body:' + str(self.Body) + ', '  + \
             'Trigger:' + str(self.Trigger) + ', '  + \
             'DeadbandType:' + str(self.DeadbandType) + ', '  + \
             'DeadbandValue:' + str(self.DeadbandValue) + ')'
    
    __repr__ = __str__
    
class EventFilter(object):
    def __init__(self):
        self.TypeId = NodeId()
        self.Encoding = 0
        self.Body = ByteString()
        self.SelectClauses = []
        self.WhereClause = ContentFilter()
    
    def to_binary(self):
        packet = []
        if self.Body: self.Encoding |= (1 << 0)
        packet.append(self.TypeId.to_binary())
        fmt = '<B'
        packet.append(struct.pack(fmt, self.Encoding))
        if self.Body: 
            packet.append(self.Body.to_binary())
        packet.append(struct.pack('<i', len(self.SelectClauses)))
        for i in self.SelectClauses:
            packet.append(self.SelectClauses.to_binary())
        packet.append(self.WhereClause.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = EventFilter()
        obj.TypeId = NodeId.from_binary(data)
        fmt = '<B'
        fmt_size = 1
        obj.Encoding = struct.unpack(fmt, data.read(fmt_size))[0]
        if obj.Encoding & (1 << 0):
            obj.Body = ByteString.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.SelectClauses = SimpleAttributeOperand.from_binary(data)
        obj.WhereClause = ContentFilter.from_binary(data)
        return obj
    
    def __str__(self):
        return 'EventFilter(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'Body:' + str(self.Body) + ', '  + \
             'SelectClauses:' + str(self.SelectClauses) + ', '  + \
             'WhereClause:' + str(self.WhereClause) + ')'
    
    __repr__ = __str__
    
class AggregateConfiguration(object):
    def __init__(self):
        self.UseServerCapabilitiesDefaults = 0
        self.TreatUncertainAsBad = 0
        self.PercentDataBad = 0
        self.PercentDataGood = 0
        self.UseSlopedExtrapolation = 0
    
    def to_binary(self):
        packet = []
        fmt = '<?'
        packet.append(struct.pack(fmt, self.UseServerCapabilitiesDefaults))
        fmt = '<?'
        packet.append(struct.pack(fmt, self.TreatUncertainAsBad))
        fmt = '<B'
        packet.append(struct.pack(fmt, self.PercentDataBad))
        fmt = '<B'
        packet.append(struct.pack(fmt, self.PercentDataGood))
        fmt = '<?'
        packet.append(struct.pack(fmt, self.UseSlopedExtrapolation))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = AggregateConfiguration()
        fmt = '<?'
        fmt_size = 1
        obj.UseServerCapabilitiesDefaults = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<?'
        fmt_size = 1
        obj.TreatUncertainAsBad = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<B'
        fmt_size = 1
        obj.PercentDataBad = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<B'
        fmt_size = 1
        obj.PercentDataGood = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<?'
        fmt_size = 1
        obj.UseSlopedExtrapolation = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'AggregateConfiguration(' + 'UseServerCapabilitiesDefaults:' + str(self.UseServerCapabilitiesDefaults) + ', '  + \
             'TreatUncertainAsBad:' + str(self.TreatUncertainAsBad) + ', '  + \
             'PercentDataBad:' + str(self.PercentDataBad) + ', '  + \
             'PercentDataGood:' + str(self.PercentDataGood) + ', '  + \
             'UseSlopedExtrapolation:' + str(self.UseSlopedExtrapolation) + ')'
    
    __repr__ = __str__
    
class AggregateFilter(object):
    def __init__(self):
        self.TypeId = NodeId()
        self.Encoding = 0
        self.Body = ByteString()
        self.StartTime = DateTime()
        self.AggregateType = NodeId()
        self.ProcessingInterval = 0
        self.AggregateConfiguration = AggregateConfiguration()
    
    def to_binary(self):
        packet = []
        if self.Body: self.Encoding |= (1 << 0)
        packet.append(self.TypeId.to_binary())
        fmt = '<B'
        packet.append(struct.pack(fmt, self.Encoding))
        if self.Body: 
            packet.append(self.Body.to_binary())
        packet.append(self.StartTime.to_binary())
        packet.append(self.AggregateType.to_binary())
        fmt = '<d'
        packet.append(struct.pack(fmt, self.ProcessingInterval))
        packet.append(self.AggregateConfiguration.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = AggregateFilter()
        obj.TypeId = NodeId.from_binary(data)
        fmt = '<B'
        fmt_size = 1
        obj.Encoding = struct.unpack(fmt, data.read(fmt_size))[0]
        if obj.Encoding & (1 << 0):
            obj.Body = ByteString.from_binary(data)
        obj.StartTime = DateTime.from_binary(data)
        obj.AggregateType = NodeId.from_binary(data)
        fmt = '<d'
        fmt_size = 8
        obj.ProcessingInterval = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.AggregateConfiguration = AggregateConfiguration.from_binary(data)
        return obj
    
    def __str__(self):
        return 'AggregateFilter(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'Body:' + str(self.Body) + ', '  + \
             'StartTime:' + str(self.StartTime) + ', '  + \
             'AggregateType:' + str(self.AggregateType) + ', '  + \
             'ProcessingInterval:' + str(self.ProcessingInterval) + ', '  + \
             'AggregateConfiguration:' + str(self.AggregateConfiguration) + ')'
    
    __repr__ = __str__
    
class MonitoringFilterResult(object):
    def __init__(self):
        self.TypeId = NodeId()
        self.Encoding = 0
        self.Body = ByteString()
    
    def to_binary(self):
        packet = []
        if self.Body: self.Encoding |= (1 << 0)
        packet.append(self.TypeId.to_binary())
        fmt = '<B'
        packet.append(struct.pack(fmt, self.Encoding))
        if self.Body: 
            packet.append(self.Body.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = MonitoringFilterResult()
        obj.TypeId = NodeId.from_binary(data)
        fmt = '<B'
        fmt_size = 1
        obj.Encoding = struct.unpack(fmt, data.read(fmt_size))[0]
        if obj.Encoding & (1 << 0):
            obj.Body = ByteString.from_binary(data)
        return obj
    
    def __str__(self):
        return 'MonitoringFilterResult(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'Body:' + str(self.Body) + ')'
    
    __repr__ = __str__
    
class EventFilterResult(object):
    def __init__(self):
        self.TypeId = NodeId()
        self.Encoding = 0
        self.Body = ByteString()
        self.SelectClauseResults = []
        self.SelectClauseDiagnosticInfos = []
        self.WhereClauseResult = ContentFilterResult()
    
    def to_binary(self):
        packet = []
        if self.Body: self.Encoding |= (1 << 0)
        packet.append(self.TypeId.to_binary())
        fmt = '<B'
        packet.append(struct.pack(fmt, self.Encoding))
        if self.Body: 
            packet.append(self.Body.to_binary())
        packet.append(struct.pack('<i', len(self.SelectClauseResults)))
        for i in self.SelectClauseResults:
            packet.append(self.SelectClauseResults.to_binary())
        packet.append(struct.pack('<i', len(self.SelectClauseDiagnosticInfos)))
        for i in self.SelectClauseDiagnosticInfos:
            packet.append(self.SelectClauseDiagnosticInfos.to_binary())
        packet.append(self.WhereClauseResult.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = EventFilterResult()
        obj.TypeId = NodeId.from_binary(data)
        fmt = '<B'
        fmt_size = 1
        obj.Encoding = struct.unpack(fmt, data.read(fmt_size))[0]
        if obj.Encoding & (1 << 0):
            obj.Body = ByteString.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.SelectClauseResults = StatusCode.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.SelectClauseDiagnosticInfos = DiagnosticInfo.from_binary(data)
        obj.WhereClauseResult = ContentFilterResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'EventFilterResult(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'Body:' + str(self.Body) + ', '  + \
             'SelectClauseResults:' + str(self.SelectClauseResults) + ', '  + \
             'SelectClauseDiagnosticInfos:' + str(self.SelectClauseDiagnosticInfos) + ', '  + \
             'WhereClauseResult:' + str(self.WhereClauseResult) + ')'
    
    __repr__ = __str__
    
class AggregateFilterResult(object):
    def __init__(self):
        self.TypeId = NodeId()
        self.Encoding = 0
        self.Body = ByteString()
        self.RevisedStartTime = DateTime()
        self.RevisedProcessingInterval = 0
        self.RevisedAggregateConfiguration = AggregateConfiguration()
    
    def to_binary(self):
        packet = []
        if self.Body: self.Encoding |= (1 << 0)
        packet.append(self.TypeId.to_binary())
        fmt = '<B'
        packet.append(struct.pack(fmt, self.Encoding))
        if self.Body: 
            packet.append(self.Body.to_binary())
        packet.append(self.RevisedStartTime.to_binary())
        fmt = '<d'
        packet.append(struct.pack(fmt, self.RevisedProcessingInterval))
        packet.append(self.RevisedAggregateConfiguration.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = AggregateFilterResult()
        obj.TypeId = NodeId.from_binary(data)
        fmt = '<B'
        fmt_size = 1
        obj.Encoding = struct.unpack(fmt, data.read(fmt_size))[0]
        if obj.Encoding & (1 << 0):
            obj.Body = ByteString.from_binary(data)
        obj.RevisedStartTime = DateTime.from_binary(data)
        fmt = '<d'
        fmt_size = 8
        obj.RevisedProcessingInterval = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.RevisedAggregateConfiguration = AggregateConfiguration.from_binary(data)
        return obj
    
    def __str__(self):
        return 'AggregateFilterResult(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'Body:' + str(self.Body) + ', '  + \
             'RevisedStartTime:' + str(self.RevisedStartTime) + ', '  + \
             'RevisedProcessingInterval:' + str(self.RevisedProcessingInterval) + ', '  + \
             'RevisedAggregateConfiguration:' + str(self.RevisedAggregateConfiguration) + ')'
    
    __repr__ = __str__
    
class MonitoringParameters(object):
    def __init__(self):
        self.ClientHandle = 0
        self.SamplingInterval = 0
        self.Filter = ExtensionObject()
        self.QueueSize = 0
        self.DiscardOldest = 0
    
    def to_binary(self):
        packet = []
        fmt = '<I'
        packet.append(struct.pack(fmt, self.ClientHandle))
        fmt = '<d'
        packet.append(struct.pack(fmt, self.SamplingInterval))
        packet.append(self.Filter.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.QueueSize))
        fmt = '<?'
        packet.append(struct.pack(fmt, self.DiscardOldest))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = MonitoringParameters()
        fmt = '<I'
        fmt_size = 4
        obj.ClientHandle = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<d'
        fmt_size = 8
        obj.SamplingInterval = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.Filter = ExtensionObject.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.QueueSize = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<?'
        fmt_size = 1
        obj.DiscardOldest = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'MonitoringParameters(' + 'ClientHandle:' + str(self.ClientHandle) + ', '  + \
             'SamplingInterval:' + str(self.SamplingInterval) + ', '  + \
             'Filter:' + str(self.Filter) + ', '  + \
             'QueueSize:' + str(self.QueueSize) + ', '  + \
             'DiscardOldest:' + str(self.DiscardOldest) + ')'
    
    __repr__ = __str__
    
class MonitoredItemCreateParameters(object):
    def __init__(self):
        self.MonitoringMode = 0
        self.RequestedParameters = MonitoringParameters()
    
    def to_binary(self):
        packet = []
        fmt = '<I'
        packet.append(struct.pack(fmt, self.MonitoringMode))
        packet.append(self.RequestedParameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = MonitoredItemCreateParameters()
        fmt = '<I'
        fmt_size = 4
        obj.MonitoringMode = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.RequestedParameters = MonitoringParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'MonitoredItemCreateParameters(' + 'MonitoringMode:' + str(self.MonitoringMode) + ', '  + \
             'RequestedParameters:' + str(self.RequestedParameters) + ')'
    
    __repr__ = __str__
    
class MonitoredItemCreateRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.MonitoredItemCreateRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
        self.ItemToMonitor = ReadValueId()
        self.Parameters = MonitoredItemCreateParameters()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ItemToMonitor.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = MonitoredItemCreateRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.ItemToMonitor = ReadValueId.from_binary(data)
        obj.Parameters = MonitoredItemCreateParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'MonitoredItemCreateRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ItemToMonitor:' + str(self.ItemToMonitor) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class MonitoredItemCreateResult(object):
    def __init__(self):
        self.StatusCode = StatusCode()
        self.MonitoredItemId = 0
        self.RevisedSamplingInterval = 0
        self.RevisedQueueSize = 0
        self.FilterResult = ExtensionObject()
    
    def to_binary(self):
        packet = []
        packet.append(self.StatusCode.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.MonitoredItemId))
        fmt = '<d'
        packet.append(struct.pack(fmt, self.RevisedSamplingInterval))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.RevisedQueueSize))
        packet.append(self.FilterResult.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = MonitoredItemCreateResult()
        obj.StatusCode = StatusCode.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.MonitoredItemId = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<d'
        fmt_size = 8
        obj.RevisedSamplingInterval = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.RevisedQueueSize = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.FilterResult = ExtensionObject.from_binary(data)
        return obj
    
    def __str__(self):
        return 'MonitoredItemCreateResult(' + 'StatusCode:' + str(self.StatusCode) + ', '  + \
             'MonitoredItemId:' + str(self.MonitoredItemId) + ', '  + \
             'RevisedSamplingInterval:' + str(self.RevisedSamplingInterval) + ', '  + \
             'RevisedQueueSize:' + str(self.RevisedQueueSize) + ', '  + \
             'FilterResult:' + str(self.FilterResult) + ')'
    
    __repr__ = __str__
    
class CreateMonitoredItemsParameters(object):
    def __init__(self):
        self.SubscriptionId = 0
        self.TimestampsToReturn = 0
        self.ItemsToCreate = []
    
    def to_binary(self):
        packet = []
        fmt = '<I'
        packet.append(struct.pack(fmt, self.SubscriptionId))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.TimestampsToReturn))
        packet.append(struct.pack('<i', len(self.ItemsToCreate)))
        for i in self.ItemsToCreate:
            packet.append(self.ItemsToCreate.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = CreateMonitoredItemsParameters()
        fmt = '<I'
        fmt_size = 4
        obj.SubscriptionId = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.TimestampsToReturn = struct.unpack(fmt, data.read(fmt_size))[0]
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.ItemsToCreate = MonitoredItemCreateRequest.from_binary(data)
        return obj
    
    def __str__(self):
        return 'CreateMonitoredItemsParameters(' + 'SubscriptionId:' + str(self.SubscriptionId) + ', '  + \
             'TimestampsToReturn:' + str(self.TimestampsToReturn) + ', '  + \
             'ItemsToCreate:' + str(self.ItemsToCreate) + ')'
    
    __repr__ = __str__
    
class CreateMonitoredItemsRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.CreateMonitoredItemsRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
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
        obj = CreateMonitoredItemsRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = CreateMonitoredItemsParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'CreateMonitoredItemsRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class CreateMonitoredItemsResult(object):
    def __init__(self):
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.Results)))
        for i in self.Results:
            packet.append(self.Results.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for i in self.DiagnosticInfos:
            packet.append(self.DiagnosticInfos.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = CreateMonitoredItemsResult()
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.Results = MonitoredItemCreateResult.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.DiagnosticInfos = DiagnosticInfo.from_binary(data)
        return obj
    
    def __str__(self):
        return 'CreateMonitoredItemsResult(' + 'Results:' + str(self.Results) + ', '  + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'
    
    __repr__ = __str__
    
class CreateMonitoredItemsResponse(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.CreateMonitoredItemsResponse_Encoding_DefaultBinary, NodeIdType.FourByte)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = CreateMonitoredItemsResult()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = CreateMonitoredItemsResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = CreateMonitoredItemsResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'CreateMonitoredItemsResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class MonitoredItemModifyRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.MonitoredItemModifyRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
        self.MonitoredItemId = 0
        self.RequestedParameters = MonitoringParameters()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.MonitoredItemId))
        packet.append(self.RequestedParameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = MonitoredItemModifyRequest()
        obj.TypeId = NodeId.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.MonitoredItemId = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.RequestedParameters = MonitoringParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'MonitoredItemModifyRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'MonitoredItemId:' + str(self.MonitoredItemId) + ', '  + \
             'RequestedParameters:' + str(self.RequestedParameters) + ')'
    
    __repr__ = __str__
    
class MonitoredItemModifyResult(object):
    def __init__(self):
        self.StatusCode = StatusCode()
        self.RevisedSamplingInterval = 0
        self.RevisedQueueSize = 0
        self.FilterResult = ExtensionObject()
    
    def to_binary(self):
        packet = []
        packet.append(self.StatusCode.to_binary())
        fmt = '<d'
        packet.append(struct.pack(fmt, self.RevisedSamplingInterval))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.RevisedQueueSize))
        packet.append(self.FilterResult.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = MonitoredItemModifyResult()
        obj.StatusCode = StatusCode.from_binary(data)
        fmt = '<d'
        fmt_size = 8
        obj.RevisedSamplingInterval = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.RevisedQueueSize = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.FilterResult = ExtensionObject.from_binary(data)
        return obj
    
    def __str__(self):
        return 'MonitoredItemModifyResult(' + 'StatusCode:' + str(self.StatusCode) + ', '  + \
             'RevisedSamplingInterval:' + str(self.RevisedSamplingInterval) + ', '  + \
             'RevisedQueueSize:' + str(self.RevisedQueueSize) + ', '  + \
             'FilterResult:' + str(self.FilterResult) + ')'
    
    __repr__ = __str__
    
class ModifyMonitoredItemsParameters(object):
    def __init__(self):
        self.SubscriptionId = 0
        self.TimestampsToReturn = 0
        self.ItemsToModify = []
    
    def to_binary(self):
        packet = []
        fmt = '<I'
        packet.append(struct.pack(fmt, self.SubscriptionId))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.TimestampsToReturn))
        packet.append(struct.pack('<i', len(self.ItemsToModify)))
        for i in self.ItemsToModify:
            packet.append(self.ItemsToModify.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ModifyMonitoredItemsParameters()
        fmt = '<I'
        fmt_size = 4
        obj.SubscriptionId = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.TimestampsToReturn = struct.unpack(fmt, data.read(fmt_size))[0]
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.ItemsToModify = MonitoredItemModifyRequest.from_binary(data)
        return obj
    
    def __str__(self):
        return 'ModifyMonitoredItemsParameters(' + 'SubscriptionId:' + str(self.SubscriptionId) + ', '  + \
             'TimestampsToReturn:' + str(self.TimestampsToReturn) + ', '  + \
             'ItemsToModify:' + str(self.ItemsToModify) + ')'
    
    __repr__ = __str__
    
class ModifyMonitoredItemsRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.ModifyMonitoredItemsRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
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
        obj = ModifyMonitoredItemsRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = ModifyMonitoredItemsParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'ModifyMonitoredItemsRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class ModifyMonitoredItemsResult(object):
    def __init__(self):
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.Results)))
        for i in self.Results:
            packet.append(self.Results.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for i in self.DiagnosticInfos:
            packet.append(self.DiagnosticInfos.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ModifyMonitoredItemsResult()
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.Results = MonitoredItemModifyResult.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.DiagnosticInfos = DiagnosticInfo.from_binary(data)
        return obj
    
    def __str__(self):
        return 'ModifyMonitoredItemsResult(' + 'Results:' + str(self.Results) + ', '  + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'
    
    __repr__ = __str__
    
class ModifyMonitoredItemsResponse(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.ModifyMonitoredItemsResponse_Encoding_DefaultBinary, NodeIdType.FourByte)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = ModifyMonitoredItemsResult()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ModifyMonitoredItemsResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = ModifyMonitoredItemsResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'ModifyMonitoredItemsResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class SetMonitoringModeParameters(object):
    def __init__(self):
        self.SubscriptionId = 0
        self.MonitoringMode = 0
        self.MonitoredItemIds = []
    
    def to_binary(self):
        packet = []
        fmt = '<I'
        packet.append(struct.pack(fmt, self.SubscriptionId))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.MonitoringMode))
        packet.append(struct.pack('<i', len(self.MonitoredItemIds)))
        for i in self.MonitoredItemIds:
            fmt = '<I'
            packet.append(struct.pack(fmt, self.MonitoredItemIds))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = SetMonitoringModeParameters()
        fmt = '<I'
        fmt_size = 4
        obj.SubscriptionId = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.MonitoringMode = struct.unpack(fmt, data.read(fmt_size))[0]
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                fmt = '<I'
                fmt_size = 4
                obj.MonitoredItemIds = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'SetMonitoringModeParameters(' + 'SubscriptionId:' + str(self.SubscriptionId) + ', '  + \
             'MonitoringMode:' + str(self.MonitoringMode) + ', '  + \
             'MonitoredItemIds:' + str(self.MonitoredItemIds) + ')'
    
    __repr__ = __str__
    
class SetMonitoringModeRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.SetMonitoringModeRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
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
        obj = SetMonitoringModeRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = SetMonitoringModeParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'SetMonitoringModeRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class SetMonitoringModeResult(object):
    def __init__(self):
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.Results)))
        for i in self.Results:
            packet.append(self.Results.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for i in self.DiagnosticInfos:
            packet.append(self.DiagnosticInfos.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = SetMonitoringModeResult()
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.Results = StatusCode.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.DiagnosticInfos = DiagnosticInfo.from_binary(data)
        return obj
    
    def __str__(self):
        return 'SetMonitoringModeResult(' + 'Results:' + str(self.Results) + ', '  + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'
    
    __repr__ = __str__
    
class SetMonitoringModeResponse(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.SetMonitoringModeResponse_Encoding_DefaultBinary, NodeIdType.FourByte)
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
        obj = SetMonitoringModeResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = SetMonitoringModeResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'SetMonitoringModeResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class SetTriggeringParameters(object):
    def __init__(self):
        self.SubscriptionId = 0
        self.TriggeringItemId = 0
        self.LinksToAdd = []
        self.LinksToRemove = []
    
    def to_binary(self):
        packet = []
        fmt = '<I'
        packet.append(struct.pack(fmt, self.SubscriptionId))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.TriggeringItemId))
        packet.append(struct.pack('<i', len(self.LinksToAdd)))
        for i in self.LinksToAdd:
            fmt = '<I'
            packet.append(struct.pack(fmt, self.LinksToAdd))
        packet.append(struct.pack('<i', len(self.LinksToRemove)))
        for i in self.LinksToRemove:
            fmt = '<I'
            packet.append(struct.pack(fmt, self.LinksToRemove))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = SetTriggeringParameters()
        fmt = '<I'
        fmt_size = 4
        obj.SubscriptionId = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.TriggeringItemId = struct.unpack(fmt, data.read(fmt_size))[0]
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                fmt = '<I'
                fmt_size = 4
                obj.LinksToAdd = struct.unpack(fmt, data.read(fmt_size))[0]
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                fmt = '<I'
                fmt_size = 4
                obj.LinksToRemove = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'SetTriggeringParameters(' + 'SubscriptionId:' + str(self.SubscriptionId) + ', '  + \
             'TriggeringItemId:' + str(self.TriggeringItemId) + ', '  + \
             'LinksToAdd:' + str(self.LinksToAdd) + ', '  + \
             'LinksToRemove:' + str(self.LinksToRemove) + ')'
    
    __repr__ = __str__
    
class SetTriggeringRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.SetTriggeringRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
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
        obj = SetTriggeringRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = SetTriggeringParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'SetTriggeringRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class SetTriggeringResult(object):
    def __init__(self):
        self.AddResults = []
        self.AddDiagnosticInfos = []
        self.RemoveResults = []
        self.RemoveDiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.AddResults)))
        for i in self.AddResults:
            packet.append(self.AddResults.to_binary())
        packet.append(struct.pack('<i', len(self.AddDiagnosticInfos)))
        for i in self.AddDiagnosticInfos:
            packet.append(self.AddDiagnosticInfos.to_binary())
        packet.append(struct.pack('<i', len(self.RemoveResults)))
        for i in self.RemoveResults:
            packet.append(self.RemoveResults.to_binary())
        packet.append(struct.pack('<i', len(self.RemoveDiagnosticInfos)))
        for i in self.RemoveDiagnosticInfos:
            packet.append(self.RemoveDiagnosticInfos.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = SetTriggeringResult()
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.AddResults = StatusCode.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.AddDiagnosticInfos = DiagnosticInfo.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.RemoveResults = StatusCode.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.RemoveDiagnosticInfos = DiagnosticInfo.from_binary(data)
        return obj
    
    def __str__(self):
        return 'SetTriggeringResult(' + 'AddResults:' + str(self.AddResults) + ', '  + \
             'AddDiagnosticInfos:' + str(self.AddDiagnosticInfos) + ', '  + \
             'RemoveResults:' + str(self.RemoveResults) + ', '  + \
             'RemoveDiagnosticInfos:' + str(self.RemoveDiagnosticInfos) + ')'
    
    __repr__ = __str__
    
class SetTriggeringResponse(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.SetTriggeringResponse_Encoding_DefaultBinary, NodeIdType.FourByte)
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
        obj = SetTriggeringResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = SetTriggeringResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'SetTriggeringResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class DeleteMonitoredItemsParameters(object):
    def __init__(self):
        self.SubscriptionId = 0
        self.MonitoredItemIds = []
    
    def to_binary(self):
        packet = []
        fmt = '<I'
        packet.append(struct.pack(fmt, self.SubscriptionId))
        packet.append(struct.pack('<i', len(self.MonitoredItemIds)))
        for i in self.MonitoredItemIds:
            fmt = '<I'
            packet.append(struct.pack(fmt, self.MonitoredItemIds))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = DeleteMonitoredItemsParameters()
        fmt = '<I'
        fmt_size = 4
        obj.SubscriptionId = struct.unpack(fmt, data.read(fmt_size))[0]
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                fmt = '<I'
                fmt_size = 4
                obj.MonitoredItemIds = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'DeleteMonitoredItemsParameters(' + 'SubscriptionId:' + str(self.SubscriptionId) + ', '  + \
             'MonitoredItemIds:' + str(self.MonitoredItemIds) + ')'
    
    __repr__ = __str__
    
class DeleteMonitoredItemsRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.DeleteMonitoredItemsRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
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
        obj = DeleteMonitoredItemsRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = DeleteMonitoredItemsParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'DeleteMonitoredItemsRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class DeleteMonitoredItemsResult(object):
    def __init__(self):
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.Results)))
        for i in self.Results:
            packet.append(self.Results.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for i in self.DiagnosticInfos:
            packet.append(self.DiagnosticInfos.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = DeleteMonitoredItemsResult()
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.Results = StatusCode.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.DiagnosticInfos = DiagnosticInfo.from_binary(data)
        return obj
    
    def __str__(self):
        return 'DeleteMonitoredItemsResult(' + 'Results:' + str(self.Results) + ', '  + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'
    
    __repr__ = __str__
    
class DeleteMonitoredItemsResponse(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.DeleteMonitoredItemsResponse_Encoding_DefaultBinary, NodeIdType.FourByte)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = DeleteMonitoredItemsResult()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = DeleteMonitoredItemsResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = DeleteMonitoredItemsResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'DeleteMonitoredItemsResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class CreateSubscriptionParameters(object):
    def __init__(self):
        self.RequestedPublishingInterval = 0
        self.RequestedLifetimeCount = 0
        self.RequestedMaxKeepAliveCount = 0
        self.MaxNotificationsPerPublish = 0
        self.PublishingEnabled = 0
        self.Priority = 0
    
    def to_binary(self):
        packet = []
        fmt = '<d'
        packet.append(struct.pack(fmt, self.RequestedPublishingInterval))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.RequestedLifetimeCount))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.RequestedMaxKeepAliveCount))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.MaxNotificationsPerPublish))
        fmt = '<?'
        packet.append(struct.pack(fmt, self.PublishingEnabled))
        fmt = '<B'
        packet.append(struct.pack(fmt, self.Priority))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = CreateSubscriptionParameters()
        fmt = '<d'
        fmt_size = 8
        obj.RequestedPublishingInterval = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.RequestedLifetimeCount = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.RequestedMaxKeepAliveCount = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.MaxNotificationsPerPublish = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<?'
        fmt_size = 1
        obj.PublishingEnabled = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<B'
        fmt_size = 1
        obj.Priority = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'CreateSubscriptionParameters(' + 'RequestedPublishingInterval:' + str(self.RequestedPublishingInterval) + ', '  + \
             'RequestedLifetimeCount:' + str(self.RequestedLifetimeCount) + ', '  + \
             'RequestedMaxKeepAliveCount:' + str(self.RequestedMaxKeepAliveCount) + ', '  + \
             'MaxNotificationsPerPublish:' + str(self.MaxNotificationsPerPublish) + ', '  + \
             'PublishingEnabled:' + str(self.PublishingEnabled) + ', '  + \
             'Priority:' + str(self.Priority) + ')'
    
    __repr__ = __str__
    
class CreateSubscriptionRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.CreateSubscriptionRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
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
        obj = CreateSubscriptionRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = CreateSubscriptionParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'CreateSubscriptionRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class CreateSubscriptionResult(object):
    def __init__(self):
        self.SubscriptionId = 0
        self.RevisedPublishingInterval = 0
        self.RevisedLifetimeCount = 0
        self.RevisedMaxKeepAliveCount = 0
    
    def to_binary(self):
        packet = []
        fmt = '<I'
        packet.append(struct.pack(fmt, self.SubscriptionId))
        fmt = '<d'
        packet.append(struct.pack(fmt, self.RevisedPublishingInterval))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.RevisedLifetimeCount))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.RevisedMaxKeepAliveCount))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = CreateSubscriptionResult()
        fmt = '<I'
        fmt_size = 4
        obj.SubscriptionId = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<d'
        fmt_size = 8
        obj.RevisedPublishingInterval = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.RevisedLifetimeCount = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.RevisedMaxKeepAliveCount = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'CreateSubscriptionResult(' + 'SubscriptionId:' + str(self.SubscriptionId) + ', '  + \
             'RevisedPublishingInterval:' + str(self.RevisedPublishingInterval) + ', '  + \
             'RevisedLifetimeCount:' + str(self.RevisedLifetimeCount) + ', '  + \
             'RevisedMaxKeepAliveCount:' + str(self.RevisedMaxKeepAliveCount) + ')'
    
    __repr__ = __str__
    
class CreateSubscriptionResponse(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.CreateSubscriptionResponse_Encoding_DefaultBinary, NodeIdType.FourByte)
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
        obj = CreateSubscriptionResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = CreateSubscriptionResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'CreateSubscriptionResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class ModifySubscriptionParameters(object):
    def __init__(self):
        self.SubscriptionId = 0
        self.RequestedPublishingInterval = 0
        self.RequestedLifetimeCount = 0
        self.RequestedMaxKeepAliveCount = 0
        self.MaxNotificationsPerPublish = 0
        self.Priority = 0
    
    def to_binary(self):
        packet = []
        fmt = '<I'
        packet.append(struct.pack(fmt, self.SubscriptionId))
        fmt = '<d'
        packet.append(struct.pack(fmt, self.RequestedPublishingInterval))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.RequestedLifetimeCount))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.RequestedMaxKeepAliveCount))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.MaxNotificationsPerPublish))
        fmt = '<B'
        packet.append(struct.pack(fmt, self.Priority))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ModifySubscriptionParameters()
        fmt = '<I'
        fmt_size = 4
        obj.SubscriptionId = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<d'
        fmt_size = 8
        obj.RequestedPublishingInterval = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.RequestedLifetimeCount = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.RequestedMaxKeepAliveCount = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.MaxNotificationsPerPublish = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<B'
        fmt_size = 1
        obj.Priority = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'ModifySubscriptionParameters(' + 'SubscriptionId:' + str(self.SubscriptionId) + ', '  + \
             'RequestedPublishingInterval:' + str(self.RequestedPublishingInterval) + ', '  + \
             'RequestedLifetimeCount:' + str(self.RequestedLifetimeCount) + ', '  + \
             'RequestedMaxKeepAliveCount:' + str(self.RequestedMaxKeepAliveCount) + ', '  + \
             'MaxNotificationsPerPublish:' + str(self.MaxNotificationsPerPublish) + ', '  + \
             'Priority:' + str(self.Priority) + ')'
    
    __repr__ = __str__
    
class ModifySubscriptionRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.ModifySubscriptionRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
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
        obj = ModifySubscriptionRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = ModifySubscriptionParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'ModifySubscriptionRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class ModifySubscriptionResult(object):
    def __init__(self):
        self.RevisedPublishingInterval = 0
        self.RevisedLifetimeCount = 0
        self.RevisedMaxKeepAliveCount = 0
    
    def to_binary(self):
        packet = []
        fmt = '<d'
        packet.append(struct.pack(fmt, self.RevisedPublishingInterval))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.RevisedLifetimeCount))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.RevisedMaxKeepAliveCount))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ModifySubscriptionResult()
        fmt = '<d'
        fmt_size = 8
        obj.RevisedPublishingInterval = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.RevisedLifetimeCount = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.RevisedMaxKeepAliveCount = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'ModifySubscriptionResult(' + 'RevisedPublishingInterval:' + str(self.RevisedPublishingInterval) + ', '  + \
             'RevisedLifetimeCount:' + str(self.RevisedLifetimeCount) + ', '  + \
             'RevisedMaxKeepAliveCount:' + str(self.RevisedMaxKeepAliveCount) + ')'
    
    __repr__ = __str__
    
class ModifySubscriptionResponse(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.ModifySubscriptionResponse_Encoding_DefaultBinary, NodeIdType.FourByte)
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
        obj = ModifySubscriptionResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = ModifySubscriptionResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'ModifySubscriptionResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class SetPublishingModeParameters(object):
    def __init__(self):
        self.PublishingEnabled = 0
        self.SubscriptionIds = []
    
    def to_binary(self):
        packet = []
        fmt = '<?'
        packet.append(struct.pack(fmt, self.PublishingEnabled))
        packet.append(struct.pack('<i', len(self.SubscriptionIds)))
        for i in self.SubscriptionIds:
            fmt = '<I'
            packet.append(struct.pack(fmt, self.SubscriptionIds))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = SetPublishingModeParameters()
        fmt = '<?'
        fmt_size = 1
        obj.PublishingEnabled = struct.unpack(fmt, data.read(fmt_size))[0]
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                fmt = '<I'
                fmt_size = 4
                obj.SubscriptionIds = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'SetPublishingModeParameters(' + 'PublishingEnabled:' + str(self.PublishingEnabled) + ', '  + \
             'SubscriptionIds:' + str(self.SubscriptionIds) + ')'
    
    __repr__ = __str__
    
class SetPublishingModeRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.SetPublishingModeRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
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
        obj = SetPublishingModeRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = SetPublishingModeParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'SetPublishingModeRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class SetPublishingModeResult(object):
    def __init__(self):
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.Results)))
        for i in self.Results:
            packet.append(self.Results.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for i in self.DiagnosticInfos:
            packet.append(self.DiagnosticInfos.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = SetPublishingModeResult()
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.Results = StatusCode.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.DiagnosticInfos = DiagnosticInfo.from_binary(data)
        return obj
    
    def __str__(self):
        return 'SetPublishingModeResult(' + 'Results:' + str(self.Results) + ', '  + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'
    
    __repr__ = __str__
    
class SetPublishingModeResponse(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.SetPublishingModeResponse_Encoding_DefaultBinary, NodeIdType.FourByte)
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
        obj = SetPublishingModeResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = SetPublishingModeResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'SetPublishingModeResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class NotificationMessage(object):
    def __init__(self):
        self.SequenceNumber = 0
        self.PublishTime = DateTime()
        self.NotificationData = []
    
    def to_binary(self):
        packet = []
        fmt = '<I'
        packet.append(struct.pack(fmt, self.SequenceNumber))
        packet.append(self.PublishTime.to_binary())
        packet.append(struct.pack('<i', len(self.NotificationData)))
        for i in self.NotificationData:
            packet.append(self.NotificationData.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = NotificationMessage()
        fmt = '<I'
        fmt_size = 4
        obj.SequenceNumber = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.PublishTime = DateTime.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.NotificationData = ExtensionObject.from_binary(data)
        return obj
    
    def __str__(self):
        return 'NotificationMessage(' + 'SequenceNumber:' + str(self.SequenceNumber) + ', '  + \
             'PublishTime:' + str(self.PublishTime) + ', '  + \
             'NotificationData:' + str(self.NotificationData) + ')'
    
    __repr__ = __str__
    
class NotificationData(object):
    def __init__(self):
        self.TypeId = NodeId()
        self.Encoding = 0
        self.Body = ByteString()
    
    def to_binary(self):
        packet = []
        if self.Body: self.Encoding |= (1 << 0)
        packet.append(self.TypeId.to_binary())
        fmt = '<B'
        packet.append(struct.pack(fmt, self.Encoding))
        if self.Body: 
            packet.append(self.Body.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = NotificationData()
        obj.TypeId = NodeId.from_binary(data)
        fmt = '<B'
        fmt_size = 1
        obj.Encoding = struct.unpack(fmt, data.read(fmt_size))[0]
        if obj.Encoding & (1 << 0):
            obj.Body = ByteString.from_binary(data)
        return obj
    
    def __str__(self):
        return 'NotificationData(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'Body:' + str(self.Body) + ')'
    
    __repr__ = __str__
    
class DataChangeNotification(object):
    def __init__(self):
        self.TypeId = NodeId()
        self.Encoding = 0
        self.Body = ByteString()
        self.MonitoredItems = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        if self.Body: self.Encoding |= (1 << 0)
        packet.append(self.TypeId.to_binary())
        fmt = '<B'
        packet.append(struct.pack(fmt, self.Encoding))
        if self.Body: 
            packet.append(self.Body.to_binary())
        packet.append(struct.pack('<i', len(self.MonitoredItems)))
        for i in self.MonitoredItems:
            packet.append(self.MonitoredItems.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for i in self.DiagnosticInfos:
            packet.append(self.DiagnosticInfos.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = DataChangeNotification()
        obj.TypeId = NodeId.from_binary(data)
        fmt = '<B'
        fmt_size = 1
        obj.Encoding = struct.unpack(fmt, data.read(fmt_size))[0]
        if obj.Encoding & (1 << 0):
            obj.Body = ByteString.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.MonitoredItems = MonitoredItemNotification.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.DiagnosticInfos = DiagnosticInfo.from_binary(data)
        return obj
    
    def __str__(self):
        return 'DataChangeNotification(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'Body:' + str(self.Body) + ', '  + \
             'MonitoredItems:' + str(self.MonitoredItems) + ', '  + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'
    
    __repr__ = __str__
    
class MonitoredItemNotification(object):
    def __init__(self):
        self.ClientHandle = 0
        self.Value = DataValue()
    
    def to_binary(self):
        packet = []
        fmt = '<I'
        packet.append(struct.pack(fmt, self.ClientHandle))
        packet.append(self.Value.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = MonitoredItemNotification()
        fmt = '<I'
        fmt_size = 4
        obj.ClientHandle = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.Value = DataValue.from_binary(data)
        return obj
    
    def __str__(self):
        return 'MonitoredItemNotification(' + 'ClientHandle:' + str(self.ClientHandle) + ', '  + \
             'Value:' + str(self.Value) + ')'
    
    __repr__ = __str__
    
class EventNotificationList(object):
    def __init__(self):
        self.TypeId = NodeId()
        self.Encoding = 0
        self.Body = ByteString()
        self.Events = []
    
    def to_binary(self):
        packet = []
        if self.Body: self.Encoding |= (1 << 0)
        packet.append(self.TypeId.to_binary())
        fmt = '<B'
        packet.append(struct.pack(fmt, self.Encoding))
        if self.Body: 
            packet.append(self.Body.to_binary())
        packet.append(struct.pack('<i', len(self.Events)))
        for i in self.Events:
            packet.append(self.Events.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = EventNotificationList()
        obj.TypeId = NodeId.from_binary(data)
        fmt = '<B'
        fmt_size = 1
        obj.Encoding = struct.unpack(fmt, data.read(fmt_size))[0]
        if obj.Encoding & (1 << 0):
            obj.Body = ByteString.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.Events = EventFieldList.from_binary(data)
        return obj
    
    def __str__(self):
        return 'EventNotificationList(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'Body:' + str(self.Body) + ', '  + \
             'Events:' + str(self.Events) + ')'
    
    __repr__ = __str__
    
class EventFieldList(object):
    def __init__(self):
        self.ClientHandle = 0
        self.EventFields = []
    
    def to_binary(self):
        packet = []
        fmt = '<I'
        packet.append(struct.pack(fmt, self.ClientHandle))
        packet.append(struct.pack('<i', len(self.EventFields)))
        for i in self.EventFields:
            packet.append(self.EventFields.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = EventFieldList()
        fmt = '<I'
        fmt_size = 4
        obj.ClientHandle = struct.unpack(fmt, data.read(fmt_size))[0]
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.EventFields = Variant.from_binary(data)
        return obj
    
    def __str__(self):
        return 'EventFieldList(' + 'ClientHandle:' + str(self.ClientHandle) + ', '  + \
             'EventFields:' + str(self.EventFields) + ')'
    
    __repr__ = __str__
    
class HistoryEventFieldList(object):
    def __init__(self):
        self.EventFields = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.EventFields)))
        for i in self.EventFields:
            packet.append(self.EventFields.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = HistoryEventFieldList()
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.EventFields = Variant.from_binary(data)
        return obj
    
    def __str__(self):
        return 'HistoryEventFieldList(' + 'EventFields:' + str(self.EventFields) + ')'
    
    __repr__ = __str__
    
class StatusChangeNotification(object):
    def __init__(self):
        self.TypeId = NodeId()
        self.Encoding = 0
        self.Body = ByteString()
        self.Status = StatusCode()
        self.DiagnosticInfo = DiagnosticInfo()
    
    def to_binary(self):
        packet = []
        if self.Body: self.Encoding |= (1 << 0)
        packet.append(self.TypeId.to_binary())
        fmt = '<B'
        packet.append(struct.pack(fmt, self.Encoding))
        if self.Body: 
            packet.append(self.Body.to_binary())
        packet.append(self.Status.to_binary())
        packet.append(self.DiagnosticInfo.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = StatusChangeNotification()
        obj.TypeId = NodeId.from_binary(data)
        fmt = '<B'
        fmt_size = 1
        obj.Encoding = struct.unpack(fmt, data.read(fmt_size))[0]
        if obj.Encoding & (1 << 0):
            obj.Body = ByteString.from_binary(data)
        obj.Status = StatusCode.from_binary(data)
        obj.DiagnosticInfo = DiagnosticInfo.from_binary(data)
        return obj
    
    def __str__(self):
        return 'StatusChangeNotification(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'Body:' + str(self.Body) + ', '  + \
             'Status:' + str(self.Status) + ', '  + \
             'DiagnosticInfo:' + str(self.DiagnosticInfo) + ')'
    
    __repr__ = __str__
    
class SubscriptionAcknowledgement(object):
    def __init__(self):
        self.SubscriptionId = 0
        self.SequenceNumber = 0
    
    def to_binary(self):
        packet = []
        fmt = '<I'
        packet.append(struct.pack(fmt, self.SubscriptionId))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.SequenceNumber))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = SubscriptionAcknowledgement()
        fmt = '<I'
        fmt_size = 4
        obj.SubscriptionId = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.SequenceNumber = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'SubscriptionAcknowledgement(' + 'SubscriptionId:' + str(self.SubscriptionId) + ', '  + \
             'SequenceNumber:' + str(self.SequenceNumber) + ')'
    
    __repr__ = __str__
    
class PublishParameters(object):
    def __init__(self):
        self.SubscriptionAcknowledgements = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.SubscriptionAcknowledgements)))
        for i in self.SubscriptionAcknowledgements:
            packet.append(self.SubscriptionAcknowledgements.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = PublishParameters()
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.SubscriptionAcknowledgements = SubscriptionAcknowledgement.from_binary(data)
        return obj
    
    def __str__(self):
        return 'PublishParameters(' + 'SubscriptionAcknowledgements:' + str(self.SubscriptionAcknowledgements) + ')'
    
    __repr__ = __str__
    
class PublishRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.PublishRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
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
        obj = PublishRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = PublishParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'PublishRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class PublishResult(object):
    def __init__(self):
        self.SubscriptionId = 0
        self.AvailableSequenceNumbers = []
        self.MoreNotifications = 0
        self.NotificationMessage = NotificationMessage()
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        fmt = '<I'
        packet.append(struct.pack(fmt, self.SubscriptionId))
        packet.append(struct.pack('<i', len(self.AvailableSequenceNumbers)))
        for i in self.AvailableSequenceNumbers:
            fmt = '<I'
            packet.append(struct.pack(fmt, self.AvailableSequenceNumbers))
        fmt = '<?'
        packet.append(struct.pack(fmt, self.MoreNotifications))
        packet.append(self.NotificationMessage.to_binary())
        packet.append(struct.pack('<i', len(self.Results)))
        for i in self.Results:
            packet.append(self.Results.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for i in self.DiagnosticInfos:
            packet.append(self.DiagnosticInfos.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = PublishResult()
        fmt = '<I'
        fmt_size = 4
        obj.SubscriptionId = struct.unpack(fmt, data.read(fmt_size))[0]
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                fmt = '<I'
                fmt_size = 4
                obj.AvailableSequenceNumbers = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<?'
        fmt_size = 1
        obj.MoreNotifications = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.NotificationMessage = NotificationMessage.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.Results = StatusCode.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.DiagnosticInfos = DiagnosticInfo.from_binary(data)
        return obj
    
    def __str__(self):
        return 'PublishResult(' + 'SubscriptionId:' + str(self.SubscriptionId) + ', '  + \
             'AvailableSequenceNumbers:' + str(self.AvailableSequenceNumbers) + ', '  + \
             'MoreNotifications:' + str(self.MoreNotifications) + ', '  + \
             'NotificationMessage:' + str(self.NotificationMessage) + ', '  + \
             'Results:' + str(self.Results) + ', '  + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'
    
    __repr__ = __str__
    
class PublishResponse(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.PublishResponse_Encoding_DefaultBinary, NodeIdType.FourByte)
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
        obj = PublishResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = PublishResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'PublishResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class RepublishParameters(object):
    def __init__(self):
        self.SubscriptionId = 0
        self.RetransmitSequenceNumber = 0
    
    def to_binary(self):
        packet = []
        fmt = '<I'
        packet.append(struct.pack(fmt, self.SubscriptionId))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.RetransmitSequenceNumber))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = RepublishParameters()
        fmt = '<I'
        fmt_size = 4
        obj.SubscriptionId = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.RetransmitSequenceNumber = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'RepublishParameters(' + 'SubscriptionId:' + str(self.SubscriptionId) + ', '  + \
             'RetransmitSequenceNumber:' + str(self.RetransmitSequenceNumber) + ')'
    
    __repr__ = __str__
    
class RepublishRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.RepublishRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
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
        obj = RepublishRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = RepublishParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'RepublishRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class RepublishResult(object):
    def __init__(self):
        self.NotificationMessage = NotificationMessage()
    
    def to_binary(self):
        packet = []
        packet.append(self.NotificationMessage.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = RepublishResult()
        obj.NotificationMessage = NotificationMessage.from_binary(data)
        return obj
    
    def __str__(self):
        return 'RepublishResult(' + 'NotificationMessage:' + str(self.NotificationMessage) + ')'
    
    __repr__ = __str__
    
class RepublishResponse(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.RepublishResponse_Encoding_DefaultBinary, NodeIdType.FourByte)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = RepublishResult()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = RepublishResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = RepublishResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'RepublishResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class TransferResult(object):
    def __init__(self):
        self.StatusCode = StatusCode()
        self.AvailableSequenceNumbers = []
    
    def to_binary(self):
        packet = []
        packet.append(self.StatusCode.to_binary())
        packet.append(struct.pack('<i', len(self.AvailableSequenceNumbers)))
        for i in self.AvailableSequenceNumbers:
            fmt = '<I'
            packet.append(struct.pack(fmt, self.AvailableSequenceNumbers))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = TransferResult()
        obj.StatusCode = StatusCode.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                fmt = '<I'
                fmt_size = 4
                obj.AvailableSequenceNumbers = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'TransferResult(' + 'StatusCode:' + str(self.StatusCode) + ', '  + \
             'AvailableSequenceNumbers:' + str(self.AvailableSequenceNumbers) + ')'
    
    __repr__ = __str__
    
class TransferSubscriptionsParameters(object):
    def __init__(self):
        self.SubscriptionIds = []
        self.SendInitialValues = 0
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.SubscriptionIds)))
        for i in self.SubscriptionIds:
            fmt = '<I'
            packet.append(struct.pack(fmt, self.SubscriptionIds))
        fmt = '<?'
        packet.append(struct.pack(fmt, self.SendInitialValues))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = TransferSubscriptionsParameters()
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                fmt = '<I'
                fmt_size = 4
                obj.SubscriptionIds = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<?'
        fmt_size = 1
        obj.SendInitialValues = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'TransferSubscriptionsParameters(' + 'SubscriptionIds:' + str(self.SubscriptionIds) + ', '  + \
             'SendInitialValues:' + str(self.SendInitialValues) + ')'
    
    __repr__ = __str__
    
class TransferSubscriptionsRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.TransferSubscriptionsRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
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
        obj = TransferSubscriptionsRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = TransferSubscriptionsParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'TransferSubscriptionsRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class TransferSubscriptionsResult(object):
    def __init__(self):
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.Results)))
        for i in self.Results:
            packet.append(self.Results.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for i in self.DiagnosticInfos:
            packet.append(self.DiagnosticInfos.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = TransferSubscriptionsResult()
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.Results = TransferResult.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.DiagnosticInfos = DiagnosticInfo.from_binary(data)
        return obj
    
    def __str__(self):
        return 'TransferSubscriptionsResult(' + 'Results:' + str(self.Results) + ', '  + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'
    
    __repr__ = __str__
    
class TransferSubscriptionsResponse(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.TransferSubscriptionsResponse_Encoding_DefaultBinary, NodeIdType.FourByte)
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
        obj = TransferSubscriptionsResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = TransferSubscriptionsResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'TransferSubscriptionsResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class DeleteSubscriptionsParameters(object):
    def __init__(self):
        self.SubscriptionIds = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.SubscriptionIds)))
        for i in self.SubscriptionIds:
            fmt = '<I'
            packet.append(struct.pack(fmt, self.SubscriptionIds))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = DeleteSubscriptionsParameters()
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                fmt = '<I'
                fmt_size = 4
                obj.SubscriptionIds = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'DeleteSubscriptionsParameters(' + 'SubscriptionIds:' + str(self.SubscriptionIds) + ')'
    
    __repr__ = __str__
    
class DeleteSubscriptionsRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.DeleteSubscriptionsRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
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
        obj = DeleteSubscriptionsRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = DeleteSubscriptionsParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'DeleteSubscriptionsRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class DeleteSubscriptionsResult(object):
    def __init__(self):
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.Results)))
        for i in self.Results:
            packet.append(self.Results.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for i in self.DiagnosticInfos:
            packet.append(self.DiagnosticInfos.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = DeleteSubscriptionsResult()
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.Results = StatusCode.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.DiagnosticInfos = DiagnosticInfo.from_binary(data)
        return obj
    
    def __str__(self):
        return 'DeleteSubscriptionsResult(' + 'Results:' + str(self.Results) + ', '  + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'
    
    __repr__ = __str__
    
class DeleteSubscriptionsResponse(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.DeleteSubscriptionsResponse_Encoding_DefaultBinary, NodeIdType.FourByte)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = DeleteSubscriptionsResult()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = DeleteSubscriptionsResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = DeleteSubscriptionsResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'DeleteSubscriptionsResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class ScalarTestType(object):
    def __init__(self):
        self.Boolean = 0
        self.SByte = SByte()
        self.Byte = 0
        self.Int16 = 0
        self.UInt16 = 0
        self.Int32 = 0
        self.UInt32 = 0
        self.Int64 = 0
        self.UInt64 = 0
        self.Float = 0
        self.Double = 0
        self.String = ''
        self.DateTime = DateTime()
        self.Guid = Guid()
        self.ByteString = ByteString()
        self.XmlElement = XmlElement()
        self.NodeId = NodeId()
        self.ExpandedNodeId = ExpandedNodeId()
        self.StatusCode = StatusCode()
        self.DiagnosticInfo = DiagnosticInfo()
        self.QualifiedName = QualifiedName()
        self.LocalizedText = LocalizedText()
        self.ExtensionObject = ExtensionObject()
        self.DataValue = DataValue()
        self.EnumeratedValue = 0
    
    def to_binary(self):
        packet = []
        fmt = '<?'
        packet.append(struct.pack(fmt, self.Boolean))
        fmt = '<B'
        packet.append(struct.pack(fmt, self.SByte))
        fmt = '<B'
        packet.append(struct.pack(fmt, self.Byte))
        fmt = '<h'
        packet.append(struct.pack(fmt, self.Int16))
        fmt = '<H'
        packet.append(struct.pack(fmt, self.UInt16))
        fmt = '<i'
        packet.append(struct.pack(fmt, self.Int32))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.UInt32))
        fmt = '<q'
        packet.append(struct.pack(fmt, self.Int64))
        fmt = '<Q'
        packet.append(struct.pack(fmt, self.UInt64))
        fmt = '<f'
        packet.append(struct.pack(fmt, self.Float))
        fmt = '<d'
        packet.append(struct.pack(fmt, self.Double))
        packet.append(struct.pack('<i', len(self.String)))
        packet.append(struct.pack('<{}s'.format(len(self.String)), self.String.encode()))
        packet.append(self.DateTime.to_binary())
        packet.append(self.Guid.to_binary())
        packet.append(self.ByteString.to_binary())
        packet.append(self.XmlElement.to_binary())
        packet.append(self.NodeId.to_binary())
        packet.append(self.ExpandedNodeId.to_binary())
        packet.append(self.StatusCode.to_binary())
        packet.append(self.DiagnosticInfo.to_binary())
        packet.append(self.QualifiedName.to_binary())
        packet.append(self.LocalizedText.to_binary())
        packet.append(self.ExtensionObject.to_binary())
        packet.append(self.DataValue.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.EnumeratedValue))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ScalarTestType()
        fmt = '<?'
        fmt_size = 1
        obj.Boolean = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<B'
        fmt_size = 1
        obj.SByte = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<B'
        fmt_size = 1
        obj.Byte = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<h'
        fmt_size = 2
        obj.Int16 = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<H'
        fmt_size = 2
        obj.UInt16 = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<i'
        fmt_size = 4
        obj.Int32 = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.UInt32 = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<q'
        fmt_size = 8
        obj.Int64 = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<Q'
        fmt_size = 8
        obj.UInt64 = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<f'
        fmt_size = 4
        obj.Float = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<d'
        fmt_size = 8
        obj.Double = struct.unpack(fmt, data.read(fmt_size))[0]
        slength = struct.unpack('<i', data.red(1))
        obj.String = struct.unpack('<{}s'.format(slength), data.read(slength))
        obj.DateTime = DateTime.from_binary(data)
        obj.Guid = Guid.from_binary(data)
        obj.ByteString = ByteString.from_binary(data)
        obj.XmlElement = XmlElement.from_binary(data)
        obj.NodeId = NodeId.from_binary(data)
        obj.ExpandedNodeId = ExpandedNodeId.from_binary(data)
        obj.StatusCode = StatusCode.from_binary(data)
        obj.DiagnosticInfo = DiagnosticInfo.from_binary(data)
        obj.QualifiedName = QualifiedName.from_binary(data)
        obj.LocalizedText = LocalizedText.from_binary(data)
        obj.ExtensionObject = ExtensionObject.from_binary(data)
        obj.DataValue = DataValue.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.EnumeratedValue = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'ScalarTestType(' + 'Boolean:' + str(self.Boolean) + ', '  + \
             'SByte:' + str(self.SByte) + ', '  + \
             'Byte:' + str(self.Byte) + ', '  + \
             'Int16:' + str(self.Int16) + ', '  + \
             'UInt16:' + str(self.UInt16) + ', '  + \
             'Int32:' + str(self.Int32) + ', '  + \
             'UInt32:' + str(self.UInt32) + ', '  + \
             'Int64:' + str(self.Int64) + ', '  + \
             'UInt64:' + str(self.UInt64) + ', '  + \
             'Float:' + str(self.Float) + ', '  + \
             'Double:' + str(self.Double) + ', '  + \
             'String:' + str(self.String) + ', '  + \
             'DateTime:' + str(self.DateTime) + ', '  + \
             'Guid:' + str(self.Guid) + ', '  + \
             'ByteString:' + str(self.ByteString) + ', '  + \
             'XmlElement:' + str(self.XmlElement) + ', '  + \
             'NodeId:' + str(self.NodeId) + ', '  + \
             'ExpandedNodeId:' + str(self.ExpandedNodeId) + ', '  + \
             'StatusCode:' + str(self.StatusCode) + ', '  + \
             'DiagnosticInfo:' + str(self.DiagnosticInfo) + ', '  + \
             'QualifiedName:' + str(self.QualifiedName) + ', '  + \
             'LocalizedText:' + str(self.LocalizedText) + ', '  + \
             'ExtensionObject:' + str(self.ExtensionObject) + ', '  + \
             'DataValue:' + str(self.DataValue) + ', '  + \
             'EnumeratedValue:' + str(self.EnumeratedValue) + ')'
    
    __repr__ = __str__
    
class ArrayTestType(object):
    def __init__(self):
        self.Booleans = []
        self.SBytes = []
        self.Int16s = []
        self.UInt16s = []
        self.Int32s = []
        self.UInt32s = []
        self.Int64s = []
        self.UInt64s = []
        self.Floats = []
        self.Doubles = []
        self.Strings = []
        self.DateTimes = []
        self.Guids = []
        self.ByteStrings = []
        self.XmlElements = []
        self.NodeIds = []
        self.ExpandedNodeIds = []
        self.StatusCodes = []
        self.DiagnosticInfos = []
        self.QualifiedNames = []
        self.LocalizedTexts = []
        self.ExtensionObjects = []
        self.DataValues = []
        self.Variants = []
        self.EnumeratedValues = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.Booleans)))
        for i in self.Booleans:
            fmt = '<?'
            packet.append(struct.pack(fmt, self.Booleans))
        packet.append(struct.pack('<i', len(self.SBytes)))
        for i in self.SBytes:
            fmt = '<B'
            packet.append(struct.pack(fmt, self.SBytes))
        packet.append(struct.pack('<i', len(self.Int16s)))
        for i in self.Int16s:
            fmt = '<h'
            packet.append(struct.pack(fmt, self.Int16s))
        packet.append(struct.pack('<i', len(self.UInt16s)))
        for i in self.UInt16s:
            fmt = '<H'
            packet.append(struct.pack(fmt, self.UInt16s))
        packet.append(struct.pack('<i', len(self.Int32s)))
        for i in self.Int32s:
            fmt = '<i'
            packet.append(struct.pack(fmt, self.Int32s))
        packet.append(struct.pack('<i', len(self.UInt32s)))
        for i in self.UInt32s:
            fmt = '<I'
            packet.append(struct.pack(fmt, self.UInt32s))
        packet.append(struct.pack('<i', len(self.Int64s)))
        for i in self.Int64s:
            fmt = '<q'
            packet.append(struct.pack(fmt, self.Int64s))
        packet.append(struct.pack('<i', len(self.UInt64s)))
        for i in self.UInt64s:
            fmt = '<Q'
            packet.append(struct.pack(fmt, self.UInt64s))
        packet.append(struct.pack('<i', len(self.Floats)))
        for i in self.Floats:
            fmt = '<f'
            packet.append(struct.pack(fmt, self.Floats))
        packet.append(struct.pack('<i', len(self.Doubles)))
        for i in self.Doubles:
            fmt = '<d'
            packet.append(struct.pack(fmt, self.Doubles))
        packet.append(struct.pack('<i', len(self.Strings)))
        for i in self.Strings:
            packet.append(struct.pack('<i', len(self.Strings)))
            packet.append(struct.pack('<{}s'.format(len(self.Strings)), self.Strings.encode()))
        packet.append(struct.pack('<i', len(self.DateTimes)))
        for i in self.DateTimes:
            packet.append(self.DateTimes.to_binary())
        packet.append(struct.pack('<i', len(self.Guids)))
        for i in self.Guids:
            packet.append(self.Guids.to_binary())
        packet.append(struct.pack('<i', len(self.ByteStrings)))
        for i in self.ByteStrings:
            packet.append(self.ByteStrings.to_binary())
        packet.append(struct.pack('<i', len(self.XmlElements)))
        for i in self.XmlElements:
            packet.append(self.XmlElements.to_binary())
        packet.append(struct.pack('<i', len(self.NodeIds)))
        for i in self.NodeIds:
            packet.append(self.NodeIds.to_binary())
        packet.append(struct.pack('<i', len(self.ExpandedNodeIds)))
        for i in self.ExpandedNodeIds:
            packet.append(self.ExpandedNodeIds.to_binary())
        packet.append(struct.pack('<i', len(self.StatusCodes)))
        for i in self.StatusCodes:
            packet.append(self.StatusCodes.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for i in self.DiagnosticInfos:
            packet.append(self.DiagnosticInfos.to_binary())
        packet.append(struct.pack('<i', len(self.QualifiedNames)))
        for i in self.QualifiedNames:
            packet.append(self.QualifiedNames.to_binary())
        packet.append(struct.pack('<i', len(self.LocalizedTexts)))
        for i in self.LocalizedTexts:
            packet.append(self.LocalizedTexts.to_binary())
        packet.append(struct.pack('<i', len(self.ExtensionObjects)))
        for i in self.ExtensionObjects:
            packet.append(self.ExtensionObjects.to_binary())
        packet.append(struct.pack('<i', len(self.DataValues)))
        for i in self.DataValues:
            packet.append(self.DataValues.to_binary())
        packet.append(struct.pack('<i', len(self.Variants)))
        for i in self.Variants:
            packet.append(self.Variants.to_binary())
        packet.append(struct.pack('<i', len(self.EnumeratedValues)))
        for i in self.EnumeratedValues:
            fmt = '<I'
            packet.append(struct.pack(fmt, self.EnumeratedValues))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ArrayTestType()
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                fmt = '<?'
                fmt_size = 1
                obj.Booleans = struct.unpack(fmt, data.read(fmt_size))[0]
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                fmt = '<B'
                fmt_size = 1
                obj.SBytes = struct.unpack(fmt, data.read(fmt_size))[0]
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                fmt = '<h'
                fmt_size = 2
                obj.Int16s = struct.unpack(fmt, data.read(fmt_size))[0]
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                fmt = '<H'
                fmt_size = 2
                obj.UInt16s = struct.unpack(fmt, data.read(fmt_size))[0]
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                fmt = '<i'
                fmt_size = 4
                obj.Int32s = struct.unpack(fmt, data.read(fmt_size))[0]
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                fmt = '<I'
                fmt_size = 4
                obj.UInt32s = struct.unpack(fmt, data.read(fmt_size))[0]
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                fmt = '<q'
                fmt_size = 8
                obj.Int64s = struct.unpack(fmt, data.read(fmt_size))[0]
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                fmt = '<Q'
                fmt_size = 8
                obj.UInt64s = struct.unpack(fmt, data.read(fmt_size))[0]
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                fmt = '<f'
                fmt_size = 4
                obj.Floats = struct.unpack(fmt, data.read(fmt_size))[0]
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                fmt = '<d'
                fmt_size = 8
                obj.Doubles = struct.unpack(fmt, data.read(fmt_size))[0]
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                slength = struct.unpack('<i', data.red(1))
                obj.Strings = struct.unpack('<{}s'.format(slength), data.read(slength))
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.DateTimes = DateTime.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.Guids = Guid.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.ByteStrings = ByteString.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.XmlElements = XmlElement.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.NodeIds = NodeId.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.ExpandedNodeIds = ExpandedNodeId.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.StatusCodes = StatusCode.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.DiagnosticInfos = DiagnosticInfo.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.QualifiedNames = QualifiedName.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.LocalizedTexts = LocalizedText.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.ExtensionObjects = ExtensionObject.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.DataValues = DataValue.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.Variants = Variant.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                fmt = '<I'
                fmt_size = 4
                obj.EnumeratedValues = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'ArrayTestType(' + 'Booleans:' + str(self.Booleans) + ', '  + \
             'SBytes:' + str(self.SBytes) + ', '  + \
             'Int16s:' + str(self.Int16s) + ', '  + \
             'UInt16s:' + str(self.UInt16s) + ', '  + \
             'Int32s:' + str(self.Int32s) + ', '  + \
             'UInt32s:' + str(self.UInt32s) + ', '  + \
             'Int64s:' + str(self.Int64s) + ', '  + \
             'UInt64s:' + str(self.UInt64s) + ', '  + \
             'Floats:' + str(self.Floats) + ', '  + \
             'Doubles:' + str(self.Doubles) + ', '  + \
             'Strings:' + str(self.Strings) + ', '  + \
             'DateTimes:' + str(self.DateTimes) + ', '  + \
             'Guids:' + str(self.Guids) + ', '  + \
             'ByteStrings:' + str(self.ByteStrings) + ', '  + \
             'XmlElements:' + str(self.XmlElements) + ', '  + \
             'NodeIds:' + str(self.NodeIds) + ', '  + \
             'ExpandedNodeIds:' + str(self.ExpandedNodeIds) + ', '  + \
             'StatusCodes:' + str(self.StatusCodes) + ', '  + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ', '  + \
             'QualifiedNames:' + str(self.QualifiedNames) + ', '  + \
             'LocalizedTexts:' + str(self.LocalizedTexts) + ', '  + \
             'ExtensionObjects:' + str(self.ExtensionObjects) + ', '  + \
             'DataValues:' + str(self.DataValues) + ', '  + \
             'Variants:' + str(self.Variants) + ', '  + \
             'EnumeratedValues:' + str(self.EnumeratedValues) + ')'
    
    __repr__ = __str__
    
class CompositeTestType(object):
    def __init__(self):
        self.Field1 = ScalarTestType()
        self.Field2 = ArrayTestType()
    
    def to_binary(self):
        packet = []
        packet.append(self.Field1.to_binary())
        packet.append(self.Field2.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = CompositeTestType()
        obj.Field1 = ScalarTestType.from_binary(data)
        obj.Field2 = ArrayTestType.from_binary(data)
        return obj
    
    def __str__(self):
        return 'CompositeTestType(' + 'Field1:' + str(self.Field1) + ', '  + \
             'Field2:' + str(self.Field2) + ')'
    
    __repr__ = __str__
    
class TestStackParameters(object):
    def __init__(self):
        self.TestId = 0
        self.Iteration = 0
        self.Input = Variant()
    
    def to_binary(self):
        packet = []
        fmt = '<I'
        packet.append(struct.pack(fmt, self.TestId))
        fmt = '<i'
        packet.append(struct.pack(fmt, self.Iteration))
        packet.append(self.Input.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = TestStackParameters()
        fmt = '<I'
        fmt_size = 4
        obj.TestId = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<i'
        fmt_size = 4
        obj.Iteration = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.Input = Variant.from_binary(data)
        return obj
    
    def __str__(self):
        return 'TestStackParameters(' + 'TestId:' + str(self.TestId) + ', '  + \
             'Iteration:' + str(self.Iteration) + ', '  + \
             'Input:' + str(self.Input) + ')'
    
    __repr__ = __str__
    
class TestStackRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.TestStackRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
        self.RequestHeader = RequestHeader()
        self.Parameters = TestStackParameters()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = TestStackRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = TestStackParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'TestStackRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class TestStackResult(object):
    def __init__(self):
        self.Output = Variant()
    
    def to_binary(self):
        packet = []
        packet.append(self.Output.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = TestStackResult()
        obj.Output = Variant.from_binary(data)
        return obj
    
    def __str__(self):
        return 'TestStackResult(' + 'Output:' + str(self.Output) + ')'
    
    __repr__ = __str__
    
class TestStackResponse(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.TestStackResponse_Encoding_DefaultBinary, NodeIdType.FourByte)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = TestStackResult()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = TestStackResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = TestStackResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'TestStackResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class TestStackExParameters(object):
    def __init__(self):
        self.TestId = 0
        self.Iteration = 0
        self.Input = CompositeTestType()
    
    def to_binary(self):
        packet = []
        fmt = '<I'
        packet.append(struct.pack(fmt, self.TestId))
        fmt = '<i'
        packet.append(struct.pack(fmt, self.Iteration))
        packet.append(self.Input.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = TestStackExParameters()
        fmt = '<I'
        fmt_size = 4
        obj.TestId = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<i'
        fmt_size = 4
        obj.Iteration = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.Input = CompositeTestType.from_binary(data)
        return obj
    
    def __str__(self):
        return 'TestStackExParameters(' + 'TestId:' + str(self.TestId) + ', '  + \
             'Iteration:' + str(self.Iteration) + ', '  + \
             'Input:' + str(self.Input) + ')'
    
    __repr__ = __str__
    
class TestStackExRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.TestStackExRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
        self.RequestHeader = RequestHeader()
        self.Parameters = TestStackExParameters()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = TestStackExRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = TestStackExParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'TestStackExRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class TestStackExResult(object):
    def __init__(self):
        self.Output = CompositeTestType()
    
    def to_binary(self):
        packet = []
        packet.append(self.Output.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = TestStackExResult()
        obj.Output = CompositeTestType.from_binary(data)
        return obj
    
    def __str__(self):
        return 'TestStackExResult(' + 'Output:' + str(self.Output) + ')'
    
    __repr__ = __str__
    
class TestStackExResponse(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.TestStackExResponse_Encoding_DefaultBinary, NodeIdType.FourByte)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = TestStackExResult()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = TestStackExResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = TestStackExResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'TestStackExResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class BuildInfo(object):
    def __init__(self):
        self.ProductUri = ''
        self.ManufacturerName = ''
        self.ProductName = ''
        self.SoftwareVersion = ''
        self.BuildNumber = ''
        self.BuildDate = DateTime()
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.ProductUri)))
        packet.append(struct.pack('<{}s'.format(len(self.ProductUri)), self.ProductUri.encode()))
        packet.append(struct.pack('<i', len(self.ManufacturerName)))
        packet.append(struct.pack('<{}s'.format(len(self.ManufacturerName)), self.ManufacturerName.encode()))
        packet.append(struct.pack('<i', len(self.ProductName)))
        packet.append(struct.pack('<{}s'.format(len(self.ProductName)), self.ProductName.encode()))
        packet.append(struct.pack('<i', len(self.SoftwareVersion)))
        packet.append(struct.pack('<{}s'.format(len(self.SoftwareVersion)), self.SoftwareVersion.encode()))
        packet.append(struct.pack('<i', len(self.BuildNumber)))
        packet.append(struct.pack('<{}s'.format(len(self.BuildNumber)), self.BuildNumber.encode()))
        packet.append(self.BuildDate.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = BuildInfo()
        slength = struct.unpack('<i', data.red(1))
        obj.ProductUri = struct.unpack('<{}s'.format(slength), data.read(slength))
        slength = struct.unpack('<i', data.red(1))
        obj.ManufacturerName = struct.unpack('<{}s'.format(slength), data.read(slength))
        slength = struct.unpack('<i', data.red(1))
        obj.ProductName = struct.unpack('<{}s'.format(slength), data.read(slength))
        slength = struct.unpack('<i', data.red(1))
        obj.SoftwareVersion = struct.unpack('<{}s'.format(slength), data.read(slength))
        slength = struct.unpack('<i', data.red(1))
        obj.BuildNumber = struct.unpack('<{}s'.format(slength), data.read(slength))
        obj.BuildDate = DateTime.from_binary(data)
        return obj
    
    def __str__(self):
        return 'BuildInfo(' + 'ProductUri:' + str(self.ProductUri) + ', '  + \
             'ManufacturerName:' + str(self.ManufacturerName) + ', '  + \
             'ProductName:' + str(self.ProductName) + ', '  + \
             'SoftwareVersion:' + str(self.SoftwareVersion) + ', '  + \
             'BuildNumber:' + str(self.BuildNumber) + ', '  + \
             'BuildDate:' + str(self.BuildDate) + ')'
    
    __repr__ = __str__
    
class RedundantServerDataType(object):
    def __init__(self):
        self.ServerId = ''
        self.ServiceLevel = 0
        self.ServerState = 0
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.ServerId)))
        packet.append(struct.pack('<{}s'.format(len(self.ServerId)), self.ServerId.encode()))
        fmt = '<B'
        packet.append(struct.pack(fmt, self.ServiceLevel))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.ServerState))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = RedundantServerDataType()
        slength = struct.unpack('<i', data.red(1))
        obj.ServerId = struct.unpack('<{}s'.format(slength), data.read(slength))
        fmt = '<B'
        fmt_size = 1
        obj.ServiceLevel = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.ServerState = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'RedundantServerDataType(' + 'ServerId:' + str(self.ServerId) + ', '  + \
             'ServiceLevel:' + str(self.ServiceLevel) + ', '  + \
             'ServerState:' + str(self.ServerState) + ')'
    
    __repr__ = __str__
    
class EndpointUrlListDataType(object):
    def __init__(self):
        self.EndpointUrlList = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.EndpointUrlList)))
        for i in self.EndpointUrlList:
            packet.append(struct.pack('<i', len(self.EndpointUrlList)))
            packet.append(struct.pack('<{}s'.format(len(self.EndpointUrlList)), self.EndpointUrlList.encode()))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = EndpointUrlListDataType()
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                slength = struct.unpack('<i', data.red(1))
                obj.EndpointUrlList = struct.unpack('<{}s'.format(slength), data.read(slength))
        return obj
    
    def __str__(self):
        return 'EndpointUrlListDataType(' + 'EndpointUrlList:' + str(self.EndpointUrlList) + ')'
    
    __repr__ = __str__
    
class NetworkGroupDataType(object):
    def __init__(self):
        self.ServerUri = ''
        self.NetworkPaths = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.ServerUri)))
        packet.append(struct.pack('<{}s'.format(len(self.ServerUri)), self.ServerUri.encode()))
        packet.append(struct.pack('<i', len(self.NetworkPaths)))
        for i in self.NetworkPaths:
            packet.append(self.NetworkPaths.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = NetworkGroupDataType()
        slength = struct.unpack('<i', data.red(1))
        obj.ServerUri = struct.unpack('<{}s'.format(slength), data.read(slength))
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.NetworkPaths = EndpointUrlListDataType.from_binary(data)
        return obj
    
    def __str__(self):
        return 'NetworkGroupDataType(' + 'ServerUri:' + str(self.ServerUri) + ', '  + \
             'NetworkPaths:' + str(self.NetworkPaths) + ')'
    
    __repr__ = __str__
    
class SamplingIntervalDiagnosticsDataType(object):
    def __init__(self):
        self.SamplingInterval = 0
        self.MonitoredItemCount = 0
        self.MaxMonitoredItemCount = 0
        self.DisabledMonitoredItemCount = 0
    
    def to_binary(self):
        packet = []
        fmt = '<d'
        packet.append(struct.pack(fmt, self.SamplingInterval))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.MonitoredItemCount))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.MaxMonitoredItemCount))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.DisabledMonitoredItemCount))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = SamplingIntervalDiagnosticsDataType()
        fmt = '<d'
        fmt_size = 8
        obj.SamplingInterval = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.MonitoredItemCount = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.MaxMonitoredItemCount = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.DisabledMonitoredItemCount = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'SamplingIntervalDiagnosticsDataType(' + 'SamplingInterval:' + str(self.SamplingInterval) + ', '  + \
             'MonitoredItemCount:' + str(self.MonitoredItemCount) + ', '  + \
             'MaxMonitoredItemCount:' + str(self.MaxMonitoredItemCount) + ', '  + \
             'DisabledMonitoredItemCount:' + str(self.DisabledMonitoredItemCount) + ')'
    
    __repr__ = __str__
    
class ServerDiagnosticsSummaryDataType(object):
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
    
    def to_binary(self):
        packet = []
        fmt = '<I'
        packet.append(struct.pack(fmt, self.ServerViewCount))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.CurrentSessionCount))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.CumulatedSessionCount))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.SecurityRejectedSessionCount))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.RejectedSessionCount))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.SessionTimeoutCount))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.SessionAbortCount))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.CurrentSubscriptionCount))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.CumulatedSubscriptionCount))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.PublishingIntervalCount))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.SecurityRejectedRequestsCount))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.RejectedRequestsCount))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ServerDiagnosticsSummaryDataType()
        fmt = '<I'
        fmt_size = 4
        obj.ServerViewCount = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.CurrentSessionCount = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.CumulatedSessionCount = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.SecurityRejectedSessionCount = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.RejectedSessionCount = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.SessionTimeoutCount = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.SessionAbortCount = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.CurrentSubscriptionCount = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.CumulatedSubscriptionCount = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.PublishingIntervalCount = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.SecurityRejectedRequestsCount = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.RejectedRequestsCount = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'ServerDiagnosticsSummaryDataType(' + 'ServerViewCount:' + str(self.ServerViewCount) + ', '  + \
             'CurrentSessionCount:' + str(self.CurrentSessionCount) + ', '  + \
             'CumulatedSessionCount:' + str(self.CumulatedSessionCount) + ', '  + \
             'SecurityRejectedSessionCount:' + str(self.SecurityRejectedSessionCount) + ', '  + \
             'RejectedSessionCount:' + str(self.RejectedSessionCount) + ', '  + \
             'SessionTimeoutCount:' + str(self.SessionTimeoutCount) + ', '  + \
             'SessionAbortCount:' + str(self.SessionAbortCount) + ', '  + \
             'CurrentSubscriptionCount:' + str(self.CurrentSubscriptionCount) + ', '  + \
             'CumulatedSubscriptionCount:' + str(self.CumulatedSubscriptionCount) + ', '  + \
             'PublishingIntervalCount:' + str(self.PublishingIntervalCount) + ', '  + \
             'SecurityRejectedRequestsCount:' + str(self.SecurityRejectedRequestsCount) + ', '  + \
             'RejectedRequestsCount:' + str(self.RejectedRequestsCount) + ')'
    
    __repr__ = __str__
    
class ServerStatusDataType(object):
    def __init__(self):
        self.StartTime = DateTime()
        self.CurrentTime = DateTime()
        self.State = 0
        self.BuildInfo = BuildInfo()
        self.SecondsTillShutdown = 0
        self.ShutdownReason = LocalizedText()
    
    def to_binary(self):
        packet = []
        packet.append(self.StartTime.to_binary())
        packet.append(self.CurrentTime.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.State))
        packet.append(self.BuildInfo.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.SecondsTillShutdown))
        packet.append(self.ShutdownReason.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ServerStatusDataType()
        obj.StartTime = DateTime.from_binary(data)
        obj.CurrentTime = DateTime.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.State = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.BuildInfo = BuildInfo.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.SecondsTillShutdown = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.ShutdownReason = LocalizedText.from_binary(data)
        return obj
    
    def __str__(self):
        return 'ServerStatusDataType(' + 'StartTime:' + str(self.StartTime) + ', '  + \
             'CurrentTime:' + str(self.CurrentTime) + ', '  + \
             'State:' + str(self.State) + ', '  + \
             'BuildInfo:' + str(self.BuildInfo) + ', '  + \
             'SecondsTillShutdown:' + str(self.SecondsTillShutdown) + ', '  + \
             'ShutdownReason:' + str(self.ShutdownReason) + ')'
    
    __repr__ = __str__
    
class SessionDiagnosticsDataType(object):
    def __init__(self):
        self.SessionId = NodeId()
        self.SessionName = ''
        self.ClientDescription = ApplicationDescription()
        self.ServerUri = ''
        self.EndpointUrl = ''
        self.LocaleIds = []
        self.ActualSessionTimeout = 0
        self.MaxResponseMessageSize = 0
        self.ClientConnectionTime = DateTime()
        self.ClientLastContactTime = DateTime()
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
        packet.append(struct.pack('<i', len(self.SessionName)))
        packet.append(struct.pack('<{}s'.format(len(self.SessionName)), self.SessionName.encode()))
        packet.append(self.ClientDescription.to_binary())
        packet.append(struct.pack('<i', len(self.ServerUri)))
        packet.append(struct.pack('<{}s'.format(len(self.ServerUri)), self.ServerUri.encode()))
        packet.append(struct.pack('<i', len(self.EndpointUrl)))
        packet.append(struct.pack('<{}s'.format(len(self.EndpointUrl)), self.EndpointUrl.encode()))
        packet.append(struct.pack('<i', len(self.LocaleIds)))
        for i in self.LocaleIds:
            packet.append(struct.pack('<i', len(self.LocaleIds)))
            packet.append(struct.pack('<{}s'.format(len(self.LocaleIds)), self.LocaleIds.encode()))
        fmt = '<d'
        packet.append(struct.pack(fmt, self.ActualSessionTimeout))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.MaxResponseMessageSize))
        packet.append(self.ClientConnectionTime.to_binary())
        packet.append(self.ClientLastContactTime.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.CurrentSubscriptionsCount))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.CurrentMonitoredItemsCount))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.CurrentPublishRequestsInQueue))
        packet.append(self.TotalRequestCount.to_binary())
        fmt = '<I'
        packet.append(struct.pack(fmt, self.UnauthorizedRequestCount))
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
        slength = struct.unpack('<i', data.red(1))
        obj.SessionName = struct.unpack('<{}s'.format(slength), data.read(slength))
        obj.ClientDescription = ApplicationDescription.from_binary(data)
        slength = struct.unpack('<i', data.red(1))
        obj.ServerUri = struct.unpack('<{}s'.format(slength), data.read(slength))
        slength = struct.unpack('<i', data.red(1))
        obj.EndpointUrl = struct.unpack('<{}s'.format(slength), data.read(slength))
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                slength = struct.unpack('<i', data.red(1))
                obj.LocaleIds = struct.unpack('<{}s'.format(slength), data.read(slength))
        fmt = '<d'
        fmt_size = 8
        obj.ActualSessionTimeout = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.MaxResponseMessageSize = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.ClientConnectionTime = DateTime.from_binary(data)
        obj.ClientLastContactTime = DateTime.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.CurrentSubscriptionsCount = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.CurrentMonitoredItemsCount = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.CurrentPublishRequestsInQueue = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.TotalRequestCount = ServiceCounterDataType.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.UnauthorizedRequestCount = struct.unpack(fmt, data.read(fmt_size))[0]
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
        return 'SessionDiagnosticsDataType(' + 'SessionId:' + str(self.SessionId) + ', '  + \
             'SessionName:' + str(self.SessionName) + ', '  + \
             'ClientDescription:' + str(self.ClientDescription) + ', '  + \
             'ServerUri:' + str(self.ServerUri) + ', '  + \
             'EndpointUrl:' + str(self.EndpointUrl) + ', '  + \
             'LocaleIds:' + str(self.LocaleIds) + ', '  + \
             'ActualSessionTimeout:' + str(self.ActualSessionTimeout) + ', '  + \
             'MaxResponseMessageSize:' + str(self.MaxResponseMessageSize) + ', '  + \
             'ClientConnectionTime:' + str(self.ClientConnectionTime) + ', '  + \
             'ClientLastContactTime:' + str(self.ClientLastContactTime) + ', '  + \
             'CurrentSubscriptionsCount:' + str(self.CurrentSubscriptionsCount) + ', '  + \
             'CurrentMonitoredItemsCount:' + str(self.CurrentMonitoredItemsCount) + ', '  + \
             'CurrentPublishRequestsInQueue:' + str(self.CurrentPublishRequestsInQueue) + ', '  + \
             'TotalRequestCount:' + str(self.TotalRequestCount) + ', '  + \
             'UnauthorizedRequestCount:' + str(self.UnauthorizedRequestCount) + ', '  + \
             'ReadCount:' + str(self.ReadCount) + ', '  + \
             'HistoryReadCount:' + str(self.HistoryReadCount) + ', '  + \
             'WriteCount:' + str(self.WriteCount) + ', '  + \
             'HistoryUpdateCount:' + str(self.HistoryUpdateCount) + ', '  + \
             'CallCount:' + str(self.CallCount) + ', '  + \
             'CreateMonitoredItemsCount:' + str(self.CreateMonitoredItemsCount) + ', '  + \
             'ModifyMonitoredItemsCount:' + str(self.ModifyMonitoredItemsCount) + ', '  + \
             'SetMonitoringModeCount:' + str(self.SetMonitoringModeCount) + ', '  + \
             'SetTriggeringCount:' + str(self.SetTriggeringCount) + ', '  + \
             'DeleteMonitoredItemsCount:' + str(self.DeleteMonitoredItemsCount) + ', '  + \
             'CreateSubscriptionCount:' + str(self.CreateSubscriptionCount) + ', '  + \
             'ModifySubscriptionCount:' + str(self.ModifySubscriptionCount) + ', '  + \
             'SetPublishingModeCount:' + str(self.SetPublishingModeCount) + ', '  + \
             'PublishCount:' + str(self.PublishCount) + ', '  + \
             'RepublishCount:' + str(self.RepublishCount) + ', '  + \
             'TransferSubscriptionsCount:' + str(self.TransferSubscriptionsCount) + ', '  + \
             'DeleteSubscriptionsCount:' + str(self.DeleteSubscriptionsCount) + ', '  + \
             'AddNodesCount:' + str(self.AddNodesCount) + ', '  + \
             'AddReferencesCount:' + str(self.AddReferencesCount) + ', '  + \
             'DeleteNodesCount:' + str(self.DeleteNodesCount) + ', '  + \
             'DeleteReferencesCount:' + str(self.DeleteReferencesCount) + ', '  + \
             'BrowseCount:' + str(self.BrowseCount) + ', '  + \
             'BrowseNextCount:' + str(self.BrowseNextCount) + ', '  + \
             'TranslateBrowsePathsToNodeIdsCount:' + str(self.TranslateBrowsePathsToNodeIdsCount) + ', '  + \
             'QueryFirstCount:' + str(self.QueryFirstCount) + ', '  + \
             'QueryNextCount:' + str(self.QueryNextCount) + ', '  + \
             'RegisterNodesCount:' + str(self.RegisterNodesCount) + ', '  + \
             'UnregisterNodesCount:' + str(self.UnregisterNodesCount) + ')'
    
    __repr__ = __str__
    
class SessionSecurityDiagnosticsDataType(object):
    def __init__(self):
        self.SessionId = NodeId()
        self.ClientUserIdOfSession = ''
        self.ClientUserIdHistory = []
        self.AuthenticationMechanism = ''
        self.Encoding = ''
        self.TransportProtocol = ''
        self.SecurityMode = 0
        self.SecurityPolicyUri = ''
        self.ClientCertificate = ByteString()
    
    def to_binary(self):
        packet = []
        packet.append(self.SessionId.to_binary())
        packet.append(struct.pack('<i', len(self.ClientUserIdOfSession)))
        packet.append(struct.pack('<{}s'.format(len(self.ClientUserIdOfSession)), self.ClientUserIdOfSession.encode()))
        packet.append(struct.pack('<i', len(self.ClientUserIdHistory)))
        for i in self.ClientUserIdHistory:
            packet.append(struct.pack('<i', len(self.ClientUserIdHistory)))
            packet.append(struct.pack('<{}s'.format(len(self.ClientUserIdHistory)), self.ClientUserIdHistory.encode()))
        packet.append(struct.pack('<i', len(self.AuthenticationMechanism)))
        packet.append(struct.pack('<{}s'.format(len(self.AuthenticationMechanism)), self.AuthenticationMechanism.encode()))
        packet.append(struct.pack('<i', len(self.Encoding)))
        packet.append(struct.pack('<{}s'.format(len(self.Encoding)), self.Encoding.encode()))
        packet.append(struct.pack('<i', len(self.TransportProtocol)))
        packet.append(struct.pack('<{}s'.format(len(self.TransportProtocol)), self.TransportProtocol.encode()))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.SecurityMode))
        packet.append(struct.pack('<i', len(self.SecurityPolicyUri)))
        packet.append(struct.pack('<{}s'.format(len(self.SecurityPolicyUri)), self.SecurityPolicyUri.encode()))
        packet.append(self.ClientCertificate.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = SessionSecurityDiagnosticsDataType()
        obj.SessionId = NodeId.from_binary(data)
        slength = struct.unpack('<i', data.red(1))
        obj.ClientUserIdOfSession = struct.unpack('<{}s'.format(slength), data.read(slength))
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                slength = struct.unpack('<i', data.red(1))
                obj.ClientUserIdHistory = struct.unpack('<{}s'.format(slength), data.read(slength))
        slength = struct.unpack('<i', data.red(1))
        obj.AuthenticationMechanism = struct.unpack('<{}s'.format(slength), data.read(slength))
        slength = struct.unpack('<i', data.red(1))
        obj.Encoding = struct.unpack('<{}s'.format(slength), data.read(slength))
        slength = struct.unpack('<i', data.red(1))
        obj.TransportProtocol = struct.unpack('<{}s'.format(slength), data.read(slength))
        fmt = '<I'
        fmt_size = 4
        obj.SecurityMode = struct.unpack(fmt, data.read(fmt_size))[0]
        slength = struct.unpack('<i', data.red(1))
        obj.SecurityPolicyUri = struct.unpack('<{}s'.format(slength), data.read(slength))
        obj.ClientCertificate = ByteString.from_binary(data)
        return obj
    
    def __str__(self):
        return 'SessionSecurityDiagnosticsDataType(' + 'SessionId:' + str(self.SessionId) + ', '  + \
             'ClientUserIdOfSession:' + str(self.ClientUserIdOfSession) + ', '  + \
             'ClientUserIdHistory:' + str(self.ClientUserIdHistory) + ', '  + \
             'AuthenticationMechanism:' + str(self.AuthenticationMechanism) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'TransportProtocol:' + str(self.TransportProtocol) + ', '  + \
             'SecurityMode:' + str(self.SecurityMode) + ', '  + \
             'SecurityPolicyUri:' + str(self.SecurityPolicyUri) + ', '  + \
             'ClientCertificate:' + str(self.ClientCertificate) + ')'
    
    __repr__ = __str__
    
class ServiceCounterDataType(object):
    def __init__(self):
        self.TotalCount = 0
        self.ErrorCount = 0
    
    def to_binary(self):
        packet = []
        fmt = '<I'
        packet.append(struct.pack(fmt, self.TotalCount))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.ErrorCount))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ServiceCounterDataType()
        fmt = '<I'
        fmt_size = 4
        obj.TotalCount = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.ErrorCount = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'ServiceCounterDataType(' + 'TotalCount:' + str(self.TotalCount) + ', '  + \
             'ErrorCount:' + str(self.ErrorCount) + ')'
    
    __repr__ = __str__
    
class StatusResult(object):
    def __init__(self):
        self.StatusCode = StatusCode()
        self.DiagnosticInfo = DiagnosticInfo()
    
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
        return 'StatusResult(' + 'StatusCode:' + str(self.StatusCode) + ', '  + \
             'DiagnosticInfo:' + str(self.DiagnosticInfo) + ')'
    
    __repr__ = __str__
    
class SubscriptionDiagnosticsDataType(object):
    def __init__(self):
        self.SessionId = NodeId()
        self.SubscriptionId = 0
        self.Priority = 0
        self.PublishingInterval = 0
        self.MaxKeepAliveCount = 0
        self.MaxLifetimeCount = 0
        self.MaxNotificationsPerPublish = 0
        self.PublishingEnabled = 0
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
        fmt = '<I'
        packet.append(struct.pack(fmt, self.SubscriptionId))
        fmt = '<B'
        packet.append(struct.pack(fmt, self.Priority))
        fmt = '<d'
        packet.append(struct.pack(fmt, self.PublishingInterval))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.MaxKeepAliveCount))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.MaxLifetimeCount))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.MaxNotificationsPerPublish))
        fmt = '<?'
        packet.append(struct.pack(fmt, self.PublishingEnabled))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.ModifyCount))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.EnableCount))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.DisableCount))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.RepublishRequestCount))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.RepublishMessageRequestCount))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.RepublishMessageCount))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.TransferRequestCount))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.TransferredToAltClientCount))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.TransferredToSameClientCount))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.PublishRequestCount))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.DataChangeNotificationsCount))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.EventNotificationsCount))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.NotificationsCount))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.LatePublishRequestCount))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.CurrentKeepAliveCount))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.CurrentLifetimeCount))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.UnacknowledgedMessageCount))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.DiscardedMessageCount))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.MonitoredItemCount))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.DisabledMonitoredItemCount))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.MonitoringQueueOverflowCount))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.NextSequenceNumber))
        fmt = '<I'
        packet.append(struct.pack(fmt, self.EventQueueOverFlowCount))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = SubscriptionDiagnosticsDataType()
        obj.SessionId = NodeId.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.SubscriptionId = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<B'
        fmt_size = 1
        obj.Priority = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<d'
        fmt_size = 8
        obj.PublishingInterval = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.MaxKeepAliveCount = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.MaxLifetimeCount = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.MaxNotificationsPerPublish = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<?'
        fmt_size = 1
        obj.PublishingEnabled = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.ModifyCount = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.EnableCount = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.DisableCount = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.RepublishRequestCount = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.RepublishMessageRequestCount = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.RepublishMessageCount = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.TransferRequestCount = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.TransferredToAltClientCount = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.TransferredToSameClientCount = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.PublishRequestCount = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.DataChangeNotificationsCount = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.EventNotificationsCount = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.NotificationsCount = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.LatePublishRequestCount = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.CurrentKeepAliveCount = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.CurrentLifetimeCount = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.UnacknowledgedMessageCount = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.DiscardedMessageCount = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.MonitoredItemCount = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.DisabledMonitoredItemCount = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.MonitoringQueueOverflowCount = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.NextSequenceNumber = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<I'
        fmt_size = 4
        obj.EventQueueOverFlowCount = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'SubscriptionDiagnosticsDataType(' + 'SessionId:' + str(self.SessionId) + ', '  + \
             'SubscriptionId:' + str(self.SubscriptionId) + ', '  + \
             'Priority:' + str(self.Priority) + ', '  + \
             'PublishingInterval:' + str(self.PublishingInterval) + ', '  + \
             'MaxKeepAliveCount:' + str(self.MaxKeepAliveCount) + ', '  + \
             'MaxLifetimeCount:' + str(self.MaxLifetimeCount) + ', '  + \
             'MaxNotificationsPerPublish:' + str(self.MaxNotificationsPerPublish) + ', '  + \
             'PublishingEnabled:' + str(self.PublishingEnabled) + ', '  + \
             'ModifyCount:' + str(self.ModifyCount) + ', '  + \
             'EnableCount:' + str(self.EnableCount) + ', '  + \
             'DisableCount:' + str(self.DisableCount) + ', '  + \
             'RepublishRequestCount:' + str(self.RepublishRequestCount) + ', '  + \
             'RepublishMessageRequestCount:' + str(self.RepublishMessageRequestCount) + ', '  + \
             'RepublishMessageCount:' + str(self.RepublishMessageCount) + ', '  + \
             'TransferRequestCount:' + str(self.TransferRequestCount) + ', '  + \
             'TransferredToAltClientCount:' + str(self.TransferredToAltClientCount) + ', '  + \
             'TransferredToSameClientCount:' + str(self.TransferredToSameClientCount) + ', '  + \
             'PublishRequestCount:' + str(self.PublishRequestCount) + ', '  + \
             'DataChangeNotificationsCount:' + str(self.DataChangeNotificationsCount) + ', '  + \
             'EventNotificationsCount:' + str(self.EventNotificationsCount) + ', '  + \
             'NotificationsCount:' + str(self.NotificationsCount) + ', '  + \
             'LatePublishRequestCount:' + str(self.LatePublishRequestCount) + ', '  + \
             'CurrentKeepAliveCount:' + str(self.CurrentKeepAliveCount) + ', '  + \
             'CurrentLifetimeCount:' + str(self.CurrentLifetimeCount) + ', '  + \
             'UnacknowledgedMessageCount:' + str(self.UnacknowledgedMessageCount) + ', '  + \
             'DiscardedMessageCount:' + str(self.DiscardedMessageCount) + ', '  + \
             'MonitoredItemCount:' + str(self.MonitoredItemCount) + ', '  + \
             'DisabledMonitoredItemCount:' + str(self.DisabledMonitoredItemCount) + ', '  + \
             'MonitoringQueueOverflowCount:' + str(self.MonitoringQueueOverflowCount) + ', '  + \
             'NextSequenceNumber:' + str(self.NextSequenceNumber) + ', '  + \
             'EventQueueOverFlowCount:' + str(self.EventQueueOverFlowCount) + ')'
    
    __repr__ = __str__
    
class ModelChangeStructureDataType(object):
    def __init__(self):
        self.Affected = NodeId()
        self.AffectedType = NodeId()
        self.Verb = 0
    
    def to_binary(self):
        packet = []
        packet.append(self.Affected.to_binary())
        packet.append(self.AffectedType.to_binary())
        fmt = '<B'
        packet.append(struct.pack(fmt, self.Verb))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ModelChangeStructureDataType()
        obj.Affected = NodeId.from_binary(data)
        obj.AffectedType = NodeId.from_binary(data)
        fmt = '<B'
        fmt_size = 1
        obj.Verb = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'ModelChangeStructureDataType(' + 'Affected:' + str(self.Affected) + ', '  + \
             'AffectedType:' + str(self.AffectedType) + ', '  + \
             'Verb:' + str(self.Verb) + ')'
    
    __repr__ = __str__
    
class SemanticChangeStructureDataType(object):
    def __init__(self):
        self.Affected = NodeId()
        self.AffectedType = NodeId()
    
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
        return 'SemanticChangeStructureDataType(' + 'Affected:' + str(self.Affected) + ', '  + \
             'AffectedType:' + str(self.AffectedType) + ')'
    
    __repr__ = __str__
    
class Range(object):
    def __init__(self):
        self.Low = 0
        self.High = 0
    
    def to_binary(self):
        packet = []
        fmt = '<d'
        packet.append(struct.pack(fmt, self.Low))
        fmt = '<d'
        packet.append(struct.pack(fmt, self.High))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = Range()
        fmt = '<d'
        fmt_size = 8
        obj.Low = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<d'
        fmt_size = 8
        obj.High = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'Range(' + 'Low:' + str(self.Low) + ', '  + \
             'High:' + str(self.High) + ')'
    
    __repr__ = __str__
    
class EUInformation(object):
    def __init__(self):
        self.NamespaceUri = ''
        self.UnitId = 0
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.NamespaceUri)))
        packet.append(struct.pack('<{}s'.format(len(self.NamespaceUri)), self.NamespaceUri.encode()))
        fmt = '<i'
        packet.append(struct.pack(fmt, self.UnitId))
        packet.append(self.DisplayName.to_binary())
        packet.append(self.Description.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = EUInformation()
        slength = struct.unpack('<i', data.red(1))
        obj.NamespaceUri = struct.unpack('<{}s'.format(slength), data.read(slength))
        fmt = '<i'
        fmt_size = 4
        obj.UnitId = struct.unpack(fmt, data.read(fmt_size))[0]
        obj.DisplayName = LocalizedText.from_binary(data)
        obj.Description = LocalizedText.from_binary(data)
        return obj
    
    def __str__(self):
        return 'EUInformation(' + 'NamespaceUri:' + str(self.NamespaceUri) + ', '  + \
             'UnitId:' + str(self.UnitId) + ', '  + \
             'DisplayName:' + str(self.DisplayName) + ', '  + \
             'Description:' + str(self.Description) + ')'
    
    __repr__ = __str__
    
class ComplexNumberType(object):
    def __init__(self):
        self.Real = 0
        self.Imaginary = 0
    
    def to_binary(self):
        packet = []
        fmt = '<f'
        packet.append(struct.pack(fmt, self.Real))
        fmt = '<f'
        packet.append(struct.pack(fmt, self.Imaginary))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ComplexNumberType()
        fmt = '<f'
        fmt_size = 4
        obj.Real = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<f'
        fmt_size = 4
        obj.Imaginary = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'ComplexNumberType(' + 'Real:' + str(self.Real) + ', '  + \
             'Imaginary:' + str(self.Imaginary) + ')'
    
    __repr__ = __str__
    
class DoubleComplexNumberType(object):
    def __init__(self):
        self.Real = 0
        self.Imaginary = 0
    
    def to_binary(self):
        packet = []
        fmt = '<d'
        packet.append(struct.pack(fmt, self.Real))
        fmt = '<d'
        packet.append(struct.pack(fmt, self.Imaginary))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = DoubleComplexNumberType()
        fmt = '<d'
        fmt_size = 8
        obj.Real = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<d'
        fmt_size = 8
        obj.Imaginary = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'DoubleComplexNumberType(' + 'Real:' + str(self.Real) + ', '  + \
             'Imaginary:' + str(self.Imaginary) + ')'
    
    __repr__ = __str__
    
class AxisInformation(object):
    def __init__(self):
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
        fmt = '<I'
        packet.append(struct.pack(fmt, self.AxisScaleType))
        packet.append(struct.pack('<i', len(self.AxisSteps)))
        for i in self.AxisSteps:
            fmt = '<d'
            packet.append(struct.pack(fmt, self.AxisSteps))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = AxisInformation()
        obj.EngineeringUnits = EUInformation.from_binary(data)
        obj.EURange = Range.from_binary(data)
        obj.Title = LocalizedText.from_binary(data)
        fmt = '<I'
        fmt_size = 4
        obj.AxisScaleType = struct.unpack(fmt, data.read(fmt_size))[0]
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                fmt = '<d'
                fmt_size = 8
                obj.AxisSteps = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'AxisInformation(' + 'EngineeringUnits:' + str(self.EngineeringUnits) + ', '  + \
             'EURange:' + str(self.EURange) + ', '  + \
             'Title:' + str(self.Title) + ', '  + \
             'AxisScaleType:' + str(self.AxisScaleType) + ', '  + \
             'AxisSteps:' + str(self.AxisSteps) + ')'
    
    __repr__ = __str__
    
class XVType(object):
    def __init__(self):
        self.X = 0
        self.Value = 0
    
    def to_binary(self):
        packet = []
        fmt = '<d'
        packet.append(struct.pack(fmt, self.X))
        fmt = '<f'
        packet.append(struct.pack(fmt, self.Value))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = XVType()
        fmt = '<d'
        fmt_size = 8
        obj.X = struct.unpack(fmt, data.read(fmt_size))[0]
        fmt = '<f'
        fmt_size = 4
        obj.Value = struct.unpack(fmt, data.read(fmt_size))[0]
        return obj
    
    def __str__(self):
        return 'XVType(' + 'X:' + str(self.X) + ', '  + \
             'Value:' + str(self.Value) + ')'
    
    __repr__ = __str__
    
class ProgramDiagnosticDataType(object):
    def __init__(self):
        self.CreateSessionId = NodeId()
        self.CreateClientName = ''
        self.InvocationCreationTime = DateTime()
        self.LastTransitionTime = DateTime()
        self.LastMethodCall = ''
        self.LastMethodSessionId = NodeId()
        self.LastMethodInputArguments = []
        self.LastMethodOutputArguments = []
        self.LastMethodCallTime = DateTime()
        self.LastMethodReturnStatus = StatusResult()
    
    def to_binary(self):
        packet = []
        packet.append(self.CreateSessionId.to_binary())
        packet.append(struct.pack('<i', len(self.CreateClientName)))
        packet.append(struct.pack('<{}s'.format(len(self.CreateClientName)), self.CreateClientName.encode()))
        packet.append(self.InvocationCreationTime.to_binary())
        packet.append(self.LastTransitionTime.to_binary())
        packet.append(struct.pack('<i', len(self.LastMethodCall)))
        packet.append(struct.pack('<{}s'.format(len(self.LastMethodCall)), self.LastMethodCall.encode()))
        packet.append(self.LastMethodSessionId.to_binary())
        packet.append(struct.pack('<i', len(self.LastMethodInputArguments)))
        for i in self.LastMethodInputArguments:
            packet.append(self.LastMethodInputArguments.to_binary())
        packet.append(struct.pack('<i', len(self.LastMethodOutputArguments)))
        for i in self.LastMethodOutputArguments:
            packet.append(self.LastMethodOutputArguments.to_binary())
        packet.append(self.LastMethodCallTime.to_binary())
        packet.append(self.LastMethodReturnStatus.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ProgramDiagnosticDataType()
        obj.CreateSessionId = NodeId.from_binary(data)
        slength = struct.unpack('<i', data.red(1))
        obj.CreateClientName = struct.unpack('<{}s'.format(slength), data.read(slength))
        obj.InvocationCreationTime = DateTime.from_binary(data)
        obj.LastTransitionTime = DateTime.from_binary(data)
        slength = struct.unpack('<i', data.red(1))
        obj.LastMethodCall = struct.unpack('<{}s'.format(slength), data.read(slength))
        obj.LastMethodSessionId = NodeId.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.LastMethodInputArguments = Argument.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length <= -1:
            for i in range(0, length):
                obj.LastMethodOutputArguments = Argument.from_binary(data)
        obj.LastMethodCallTime = DateTime.from_binary(data)
        obj.LastMethodReturnStatus = StatusResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'ProgramDiagnosticDataType(' + 'CreateSessionId:' + str(self.CreateSessionId) + ', '  + \
             'CreateClientName:' + str(self.CreateClientName) + ', '  + \
             'InvocationCreationTime:' + str(self.InvocationCreationTime) + ', '  + \
             'LastTransitionTime:' + str(self.LastTransitionTime) + ', '  + \
             'LastMethodCall:' + str(self.LastMethodCall) + ', '  + \
             'LastMethodSessionId:' + str(self.LastMethodSessionId) + ', '  + \
             'LastMethodInputArguments:' + str(self.LastMethodInputArguments) + ', '  + \
             'LastMethodOutputArguments:' + str(self.LastMethodOutputArguments) + ', '  + \
             'LastMethodCallTime:' + str(self.LastMethodCallTime) + ', '  + \
             'LastMethodReturnStatus:' + str(self.LastMethodReturnStatus) + ')'
    
    __repr__ = __str__
    
class Annotation(object):
    def __init__(self):
        self.Message = ''
        self.UserName = ''
        self.AnnotationTime = DateTime()
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.Message)))
        packet.append(struct.pack('<{}s'.format(len(self.Message)), self.Message.encode()))
        packet.append(struct.pack('<i', len(self.UserName)))
        packet.append(struct.pack('<{}s'.format(len(self.UserName)), self.UserName.encode()))
        packet.append(self.AnnotationTime.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = Annotation()
        slength = struct.unpack('<i', data.red(1))
        obj.Message = struct.unpack('<{}s'.format(slength), data.read(slength))
        slength = struct.unpack('<i', data.red(1))
        obj.UserName = struct.unpack('<{}s'.format(slength), data.read(slength))
        obj.AnnotationTime = DateTime.from_binary(data)
        return obj
    
    def __str__(self):
        return 'Annotation(' + 'Message:' + str(self.Message) + ', '  + \
             'UserName:' + str(self.UserName) + ', '  + \
             'AnnotationTime:' + str(self.AnnotationTime) + ')'
    
    __repr__ = __str__
