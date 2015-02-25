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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            fmt = '<B'
            fmt_size = Encoding
            self.Encoding = struct.unpack(fmt, data.read(fmt_size))[0]
            bodylength = struct.unpack('<i', data.read(4))[0]
            return data
            
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
        def from_binary(self, data):
            fmt = '<i'
            fmt_size = Length
            self.Length = struct.unpack(fmt, data.read(fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    fmt = '<s'
                    fmt_size = Value
                    self.Value = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
class TwoByteNodeId(object):
    def __init__(self):
        self.Identifier = 0
    
    def to_binary(self):
        packet = []
        fmt = '<B'
        packet.append(struct.pack(fmt, self.Identifier))
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            fmt = '<B'
            fmt_size = Identifier
            self.Identifier = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            fmt = '<B'
            fmt_size = NamespaceIndex
            self.NamespaceIndex = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<H'
            fmt_size = Identifier
            self.Identifier = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            fmt = '<H'
            fmt_size = NamespaceIndex
            self.NamespaceIndex = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = Identifier
            self.Identifier = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            fmt = '<H'
            fmt_size = NamespaceIndex
            self.NamespaceIndex = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<s'
            fmt_size = Identifier
            self.Identifier = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            fmt = '<H'
            fmt_size = NamespaceIndex
            self.NamespaceIndex = struct.unpack(fmt, data.read(fmt_size))[0]
            self.Identifier = Guid.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            fmt = '<H'
            fmt_size = NamespaceIndex
            self.NamespaceIndex = struct.unpack(fmt, data.read(fmt_size))[0]
            self.Identifier = ByteString.from_binary(data)
            return data
            
class DiagnosticInfo(object):
    def __init__(self):
        self.Encoding = 0
        self.SymbolicId = 0
        self.NamespaceURI = 0
        self.LocalizedText = 0
        self.AdditionalInfo = b''
        self.InnerStatusCode = StatusCode()
        self.InnerDiagnosticInfo = DiagnosticInfo()
    
    def to_binary(self):
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
        def from_binary(self, data):
            fmt = '<B'
            fmt_size = Encoding
            self.Encoding = struct.unpack(fmt, data.read(fmt_size))[0]
            if self.Encoding & (1 << 0):
                fmt = '<i'
                fmt_size = SymbolicId
                self.SymbolicId = struct.unpack(fmt, data.read(fmt_size))[0]
            if self.Encoding & (1 << 1):
                fmt = '<i'
                fmt_size = NamespaceURI
                self.NamespaceURI = struct.unpack(fmt, data.read(fmt_size))[0]
            if self.Encoding & (1 << 2):
                fmt = '<i'
                fmt_size = LocalizedText
                self.LocalizedText = struct.unpack(fmt, data.read(fmt_size))[0]
            if self.Encoding & (1 << 4):
                fmt = '<s'
                fmt_size = AdditionalInfo
                self.AdditionalInfo = struct.unpack(fmt, data.read(fmt_size))[0]
            if self.Encoding & (1 << 5):
                self.InnerStatusCode = StatusCode.from_binary(data)
            if self.Encoding & (1 << 6):
                self.InnerDiagnosticInfo = DiagnosticInfo.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            fmt = '<i'
            fmt_size = NamespaceIndex
            self.NamespaceIndex = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<s'
            fmt_size = Name
            self.Name = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            fmt = '<B'
            fmt_size = Encoding
            self.Encoding = struct.unpack(fmt, data.read(fmt_size))[0]
            if self.Encoding & (1 << 0):
                fmt = '<s'
                fmt_size = Locale
                self.Locale = struct.unpack(fmt, data.read(fmt_size))[0]
            if self.Encoding & (1 << 1):
                fmt = '<s'
                fmt_size = Text
                self.Text = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            fmt = '<B'
            fmt_size = Encoding
            self.Encoding = struct.unpack(fmt, data.read(fmt_size))[0]
            if self.Encoding & (1 << 0):
                self.Value = Variant.from_binary(data)
            if self.Encoding & (1 << 1):
                self.StatusCode = StatusCode.from_binary(data)
            if self.Encoding & (1 << 2):
                self.SourceTimestamp = DateTime.from_binary(data)
            if self.Encoding & (1 << 3):
                fmt = '<H'
                fmt_size = SourcePicoseconds
                self.SourcePicoseconds = struct.unpack(fmt, data.read(fmt_size))[0]
            if self.Encoding & (1 << 4):
                self.ServerTimestamp = DateTime.from_binary(data)
            if self.Encoding & (1 << 5):
                fmt = '<H'
                fmt_size = ServerPicoseconds
                self.ServerPicoseconds = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        self.Variant = []
    
    def to_binary(self):
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
        def from_binary(self, data):
            fmt = '<B'
            fmt_size = Encoding
            self.Encoding = struct.unpack(fmt, data.read(fmt_size))[0]
            if self.Encoding & (1 << 7):
                fmt = '<i'
                fmt_size = ArrayLength
                self.ArrayLength = struct.unpack(fmt, data.read(fmt_size))[0]
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('<i', data.read(4))[0]
                if length <= -1:
                    for i in range(0, length):
                        fmt = '<?'
                        fmt_size = Boolean
                        self.Boolean = struct.unpack(fmt, data.read(fmt_size))[0]
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('<i', data.read(4))[0]
                if length <= -1:
                    for i in range(0, length):
                        fmt = '<B'
                        fmt_size = SByte
                        self.SByte = struct.unpack(fmt, data.read(fmt_size))[0]
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('<i', data.read(4))[0]
                if length <= -1:
                    for i in range(0, length):
                        fmt = '<B'
                        fmt_size = Byte
                        self.Byte = struct.unpack(fmt, data.read(fmt_size))[0]
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('<i', data.read(4))[0]
                if length <= -1:
                    for i in range(0, length):
                        fmt = '<h'
                        fmt_size = Int16
                        self.Int16 = struct.unpack(fmt, data.read(fmt_size))[0]
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('<i', data.read(4))[0]
                if length <= -1:
                    for i in range(0, length):
                        fmt = '<H'
                        fmt_size = UInt16
                        self.UInt16 = struct.unpack(fmt, data.read(fmt_size))[0]
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('<i', data.read(4))[0]
                if length <= -1:
                    for i in range(0, length):
                        fmt = '<i'
                        fmt_size = Int32
                        self.Int32 = struct.unpack(fmt, data.read(fmt_size))[0]
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('<i', data.read(4))[0]
                if length <= -1:
                    for i in range(0, length):
                        fmt = '<I'
                        fmt_size = UInt32
                        self.UInt32 = struct.unpack(fmt, data.read(fmt_size))[0]
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('<i', data.read(4))[0]
                if length <= -1:
                    for i in range(0, length):
                        fmt = '<q'
                        fmt_size = Int64
                        self.Int64 = struct.unpack(fmt, data.read(fmt_size))[0]
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('<i', data.read(4))[0]
                if length <= -1:
                    for i in range(0, length):
                        fmt = '<Q'
                        fmt_size = UInt64
                        self.UInt64 = struct.unpack(fmt, data.read(fmt_size))[0]
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('<i', data.read(4))[0]
                if length <= -1:
                    for i in range(0, length):
                        fmt = '<f'
                        fmt_size = Float
                        self.Float = struct.unpack(fmt, data.read(fmt_size))[0]
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('<i', data.read(4))[0]
                if length <= -1:
                    for i in range(0, length):
                        fmt = '<d'
                        fmt_size = Double
                        self.Double = struct.unpack(fmt, data.read(fmt_size))[0]
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('<i', data.read(4))[0]
                if length <= -1:
                    for i in range(0, length):
                        slength = struct.unpack('<i', data.red(1))
                        self.String = struct.unpack('<{}s'.format(slength), data.read(slength))
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('<i', data.read(4))[0]
                if length <= -1:
                    for i in range(0, length):
                        self.DateTime = DateTime.from_binary(data)
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('<i', data.read(4))[0]
                if length <= -1:
                    for i in range(0, length):
                        self.Guid = Guid.from_binary(data)
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('<i', data.read(4))[0]
                if length <= -1:
                    for i in range(0, length):
                        self.ByteString = ByteString.from_binary(data)
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('<i', data.read(4))[0]
                if length <= -1:
                    for i in range(0, length):
                        self.XmlElement = XmlElement.from_binary(data)
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('<i', data.read(4))[0]
                if length <= -1:
                    for i in range(0, length):
                        self.NodeId = NodeId.from_binary(data)
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('<i', data.read(4))[0]
                if length <= -1:
                    for i in range(0, length):
                        self.ExpandedNodeId = ExpandedNodeId.from_binary(data)
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('<i', data.read(4))[0]
                if length <= -1:
                    for i in range(0, length):
                        self.StatusCode = StatusCode.from_binary(data)
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('<i', data.read(4))[0]
                if length <= -1:
                    for i in range(0, length):
                        self.DiagnosticInfo = DiagnosticInfo.from_binary(data)
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('<i', data.read(4))[0]
                if length <= -1:
                    for i in range(0, length):
                        self.QualifiedName = QualifiedName.from_binary(data)
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('<i', data.read(4))[0]
                if length <= -1:
                    for i in range(0, length):
                        self.LocalizedText = LocalizedText.from_binary(data)
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('<i', data.read(4))[0]
                if length <= -1:
                    for i in range(0, length):
                        self.ExtensionObject = ExtensionObject.from_binary(data)
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('<i', data.read(4))[0]
                if length <= -1:
                    for i in range(0, length):
                        self.DataValue = DataValue.from_binary(data)
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('<i', data.read(4))[0]
                if length <= -1:
                    for i in range(0, length):
                        self.Variant = Variant.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.NodeId = NodeId.from_binary(data)
            fmt = '<I'
            fmt_size = NodeClass
            self.NodeClass = struct.unpack(fmt, data.read(fmt_size))[0]
            self.BrowseName = QualifiedName.from_binary(data)
            self.DisplayName = LocalizedText.from_binary(data)
            self.Description = LocalizedText.from_binary(data)
            fmt = '<I'
            fmt_size = WriteMask
            self.WriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = UserWriteMask
            self.UserWriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.References = ReferenceNode.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.NodeId = NodeId.from_binary(data)
            fmt = '<I'
            fmt_size = NodeClass
            self.NodeClass = struct.unpack(fmt, data.read(fmt_size))[0]
            self.BrowseName = QualifiedName.from_binary(data)
            self.DisplayName = LocalizedText.from_binary(data)
            self.Description = LocalizedText.from_binary(data)
            fmt = '<I'
            fmt_size = WriteMask
            self.WriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = UserWriteMask
            self.UserWriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.References = ReferenceNode.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.NodeId = NodeId.from_binary(data)
            fmt = '<I'
            fmt_size = NodeClass
            self.NodeClass = struct.unpack(fmt, data.read(fmt_size))[0]
            self.BrowseName = QualifiedName.from_binary(data)
            self.DisplayName = LocalizedText.from_binary(data)
            self.Description = LocalizedText.from_binary(data)
            fmt = '<I'
            fmt_size = WriteMask
            self.WriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = UserWriteMask
            self.UserWriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.References = ReferenceNode.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.NodeId = NodeId.from_binary(data)
            fmt = '<I'
            fmt_size = NodeClass
            self.NodeClass = struct.unpack(fmt, data.read(fmt_size))[0]
            self.BrowseName = QualifiedName.from_binary(data)
            self.DisplayName = LocalizedText.from_binary(data)
            self.Description = LocalizedText.from_binary(data)
            fmt = '<I'
            fmt_size = WriteMask
            self.WriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = UserWriteMask
            self.UserWriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.References = ReferenceNode.from_binary(data)
            fmt = '<B'
            fmt_size = EventNotifier
            self.EventNotifier = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            self.NodeId = NodeId.from_binary(data)
            fmt = '<I'
            fmt_size = NodeClass
            self.NodeClass = struct.unpack(fmt, data.read(fmt_size))[0]
            self.BrowseName = QualifiedName.from_binary(data)
            self.DisplayName = LocalizedText.from_binary(data)
            self.Description = LocalizedText.from_binary(data)
            fmt = '<I'
            fmt_size = WriteMask
            self.WriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = UserWriteMask
            self.UserWriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.References = ReferenceNode.from_binary(data)
            fmt = '<?'
            fmt_size = IsAbstract
            self.IsAbstract = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            self.NodeId = NodeId.from_binary(data)
            fmt = '<I'
            fmt_size = NodeClass
            self.NodeClass = struct.unpack(fmt, data.read(fmt_size))[0]
            self.BrowseName = QualifiedName.from_binary(data)
            self.DisplayName = LocalizedText.from_binary(data)
            self.Description = LocalizedText.from_binary(data)
            fmt = '<I'
            fmt_size = WriteMask
            self.WriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = UserWriteMask
            self.UserWriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.References = ReferenceNode.from_binary(data)
            self.Value = Variant.from_binary(data)
            self.DataType = NodeId.from_binary(data)
            fmt = '<i'
            fmt_size = ValueRank
            self.ValueRank = struct.unpack(fmt, data.read(fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    fmt = '<I'
                    fmt_size = ArrayDimensions
                    self.ArrayDimensions = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<B'
            fmt_size = AccessLevel
            self.AccessLevel = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<B'
            fmt_size = UserAccessLevel
            self.UserAccessLevel = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<d'
            fmt_size = MinimumSamplingInterval
            self.MinimumSamplingInterval = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<?'
            fmt_size = Historizing
            self.Historizing = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            self.NodeId = NodeId.from_binary(data)
            fmt = '<I'
            fmt_size = NodeClass
            self.NodeClass = struct.unpack(fmt, data.read(fmt_size))[0]
            self.BrowseName = QualifiedName.from_binary(data)
            self.DisplayName = LocalizedText.from_binary(data)
            self.Description = LocalizedText.from_binary(data)
            fmt = '<I'
            fmt_size = WriteMask
            self.WriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = UserWriteMask
            self.UserWriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.References = ReferenceNode.from_binary(data)
            self.Value = Variant.from_binary(data)
            self.DataType = NodeId.from_binary(data)
            fmt = '<i'
            fmt_size = ValueRank
            self.ValueRank = struct.unpack(fmt, data.read(fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    fmt = '<I'
                    fmt_size = ArrayDimensions
                    self.ArrayDimensions = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<?'
            fmt_size = IsAbstract
            self.IsAbstract = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            self.NodeId = NodeId.from_binary(data)
            fmt = '<I'
            fmt_size = NodeClass
            self.NodeClass = struct.unpack(fmt, data.read(fmt_size))[0]
            self.BrowseName = QualifiedName.from_binary(data)
            self.DisplayName = LocalizedText.from_binary(data)
            self.Description = LocalizedText.from_binary(data)
            fmt = '<I'
            fmt_size = WriteMask
            self.WriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = UserWriteMask
            self.UserWriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.References = ReferenceNode.from_binary(data)
            fmt = '<?'
            fmt_size = IsAbstract
            self.IsAbstract = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<?'
            fmt_size = Symmetric
            self.Symmetric = struct.unpack(fmt, data.read(fmt_size))[0]
            self.InverseName = LocalizedText.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.NodeId = NodeId.from_binary(data)
            fmt = '<I'
            fmt_size = NodeClass
            self.NodeClass = struct.unpack(fmt, data.read(fmt_size))[0]
            self.BrowseName = QualifiedName.from_binary(data)
            self.DisplayName = LocalizedText.from_binary(data)
            self.Description = LocalizedText.from_binary(data)
            fmt = '<I'
            fmt_size = WriteMask
            self.WriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = UserWriteMask
            self.UserWriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.References = ReferenceNode.from_binary(data)
            fmt = '<?'
            fmt_size = Executable
            self.Executable = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<?'
            fmt_size = UserExecutable
            self.UserExecutable = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            self.NodeId = NodeId.from_binary(data)
            fmt = '<I'
            fmt_size = NodeClass
            self.NodeClass = struct.unpack(fmt, data.read(fmt_size))[0]
            self.BrowseName = QualifiedName.from_binary(data)
            self.DisplayName = LocalizedText.from_binary(data)
            self.Description = LocalizedText.from_binary(data)
            fmt = '<I'
            fmt_size = WriteMask
            self.WriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = UserWriteMask
            self.UserWriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.References = ReferenceNode.from_binary(data)
            fmt = '<?'
            fmt_size = ContainsNoLoops
            self.ContainsNoLoops = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<B'
            fmt_size = EventNotifier
            self.EventNotifier = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            self.NodeId = NodeId.from_binary(data)
            fmt = '<I'
            fmt_size = NodeClass
            self.NodeClass = struct.unpack(fmt, data.read(fmt_size))[0]
            self.BrowseName = QualifiedName.from_binary(data)
            self.DisplayName = LocalizedText.from_binary(data)
            self.Description = LocalizedText.from_binary(data)
            fmt = '<I'
            fmt_size = WriteMask
            self.WriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = UserWriteMask
            self.UserWriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.References = ReferenceNode.from_binary(data)
            fmt = '<?'
            fmt_size = IsAbstract
            self.IsAbstract = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            self.ReferenceTypeId = NodeId.from_binary(data)
            fmt = '<?'
            fmt_size = IsInverse
            self.IsInverse = struct.unpack(fmt, data.read(fmt_size))[0]
            self.TargetId = ExpandedNodeId.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            slength = struct.unpack('<i', data.red(1))
            self.Name = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.DataType = NodeId.from_binary(data)
            fmt = '<i'
            fmt_size = ValueRank
            self.ValueRank = struct.unpack(fmt, data.read(fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    fmt = '<I'
                    fmt_size = ArrayDimensions
                    self.ArrayDimensions = struct.unpack(fmt, data.read(fmt_size))[0]
            self.Description = LocalizedText.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            fmt = '<q'
            fmt_size = Value
            self.Value = struct.unpack(fmt, data.read(fmt_size))[0]
            self.DisplayName = LocalizedText.from_binary(data)
            self.Description = LocalizedText.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            fmt = '<h'
            fmt_size = Offset
            self.Offset = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<?'
            fmt_size = DaylightSavingInOffset
            self.DaylightSavingInOffset = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            slength = struct.unpack('<i', data.red(1))
            self.ApplicationUri = struct.unpack('<{}s'.format(slength), data.read(slength))
            slength = struct.unpack('<i', data.red(1))
            self.ProductUri = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.ApplicationName = LocalizedText.from_binary(data)
            fmt = '<I'
            fmt_size = ApplicationType
            self.ApplicationType = struct.unpack(fmt, data.read(fmt_size))[0]
            slength = struct.unpack('<i', data.red(1))
            self.GatewayServerUri = struct.unpack('<{}s'.format(slength), data.read(slength))
            slength = struct.unpack('<i', data.red(1))
            self.DiscoveryProfileUri = struct.unpack('<{}s'.format(slength), data.read(slength))
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    slength = struct.unpack('<i', data.red(1))
                    self.DiscoveryUrls = struct.unpack('<{}s'.format(slength), data.read(slength))
            return data
            
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
        def from_binary(self, data):
            self.AuthenticationToken = NodeId.from_binary(data)
            self.Timestamp = DateTime.from_binary(data)
            fmt = '<I'
            fmt_size = RequestHandle
            self.RequestHandle = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = ReturnDiagnostics
            self.ReturnDiagnostics = struct.unpack(fmt, data.read(fmt_size))[0]
            slength = struct.unpack('<i', data.red(1))
            self.AuditEntryId = struct.unpack('<{}s'.format(slength), data.read(slength))
            fmt = '<I'
            fmt_size = TimeoutHint
            self.TimeoutHint = struct.unpack(fmt, data.read(fmt_size))[0]
            self.AdditionalHeader = ExtensionObject.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.Timestamp = DateTime.from_binary(data)
            fmt = '<I'
            fmt_size = RequestHandle
            self.RequestHandle = struct.unpack(fmt, data.read(fmt_size))[0]
            self.ServiceResult = StatusCode.from_binary(data)
            self.ServiceDiagnostics = DiagnosticInfo.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    slength = struct.unpack('<i', data.red(1))
                    self.StringTable = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.AdditionalHeader = ExtensionObject.from_binary(data)
            return data
            
class ServiceFault(object):
    def __init__(self):
        self.ResponseHeader = ResponseHeader()
    
    def to_binary(self):
        packet = []
        packet.append(self.ResponseHeader.to_binary())
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.ResponseHeader = ResponseHeader.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            slength = struct.unpack('<i', data.red(1))
            self.EndpointUrl = struct.unpack('<{}s'.format(slength), data.read(slength))
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    slength = struct.unpack('<i', data.red(1))
                    self.LocaleIds = struct.unpack('<{}s'.format(slength), data.read(slength))
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    slength = struct.unpack('<i', data.red(1))
                    self.ServerUris = struct.unpack('<{}s'.format(slength), data.read(slength))
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = FindServersParameters.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.Servers = ApplicationDescription.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            self.Parameters = FindServersResult.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            slength = struct.unpack('<i', data.red(1))
            self.PolicyId = struct.unpack('<{}s'.format(slength), data.read(slength))
            fmt = '<I'
            fmt_size = TokenType
            self.TokenType = struct.unpack(fmt, data.read(fmt_size))[0]
            slength = struct.unpack('<i', data.red(1))
            self.IssuedTokenType = struct.unpack('<{}s'.format(slength), data.read(slength))
            slength = struct.unpack('<i', data.red(1))
            self.IssuerEndpointUrl = struct.unpack('<{}s'.format(slength), data.read(slength))
            slength = struct.unpack('<i', data.red(1))
            self.SecurityPolicyUri = struct.unpack('<{}s'.format(slength), data.read(slength))
            return data
            
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
        def from_binary(self, data):
            slength = struct.unpack('<i', data.red(1))
            self.EndpointUrl = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.Server = ApplicationDescription.from_binary(data)
            self.ServerCertificate = ByteString.from_binary(data)
            fmt = '<I'
            fmt_size = SecurityMode
            self.SecurityMode = struct.unpack(fmt, data.read(fmt_size))[0]
            slength = struct.unpack('<i', data.red(1))
            self.SecurityPolicyUri = struct.unpack('<{}s'.format(slength), data.read(slength))
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.UserIdentityTokens = UserTokenPolicy.from_binary(data)
            slength = struct.unpack('<i', data.red(1))
            self.TransportProfileUri = struct.unpack('<{}s'.format(slength), data.read(slength))
            fmt = '<B'
            fmt_size = SecurityLevel
            self.SecurityLevel = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            slength = struct.unpack('<i', data.red(1))
            self.EndpointUrl = struct.unpack('<{}s'.format(slength), data.read(slength))
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    slength = struct.unpack('<i', data.red(1))
                    self.LocaleIds = struct.unpack('<{}s'.format(slength), data.read(slength))
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    slength = struct.unpack('<i', data.red(1))
                    self.ProfileUris = struct.unpack('<{}s'.format(slength), data.read(slength))
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = GetEndpointsParameters.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.Endpoints = EndpointDescription.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            slength = struct.unpack('<i', data.red(1))
            self.ServerUri = struct.unpack('<{}s'.format(slength), data.read(slength))
            slength = struct.unpack('<i', data.red(1))
            self.ProductUri = struct.unpack('<{}s'.format(slength), data.read(slength))
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.ServerNames = LocalizedText.from_binary(data)
            fmt = '<I'
            fmt_size = ServerType
            self.ServerType = struct.unpack(fmt, data.read(fmt_size))[0]
            slength = struct.unpack('<i', data.red(1))
            self.GatewayServerUri = struct.unpack('<{}s'.format(slength), data.read(slength))
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    slength = struct.unpack('<i', data.red(1))
                    self.DiscoveryUrls = struct.unpack('<{}s'.format(slength), data.read(slength))
            slength = struct.unpack('<i', data.red(1))
            self.SemaphoreFilePath = struct.unpack('<{}s'.format(slength), data.read(slength))
            fmt = '<?'
            fmt_size = IsOnline
            self.IsOnline = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
class RegisterServerParameters(object):
    def __init__(self):
        self.Server = RegisteredServer()
    
    def to_binary(self):
        packet = []
        packet.append(self.Server.to_binary())
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.Server = RegisteredServer.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = RegisterServerParameters.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            fmt = '<I'
            fmt_size = ChannelId
            self.ChannelId = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = TokenId
            self.TokenId = struct.unpack(fmt, data.read(fmt_size))[0]
            self.CreatedAt = DateTime.from_binary(data)
            fmt = '<I'
            fmt_size = RevisedLifetime
            self.RevisedLifetime = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            fmt = '<I'
            fmt_size = ClientProtocolVersion
            self.ClientProtocolVersion = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = RequestType
            self.RequestType = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = SecurityMode
            self.SecurityMode = struct.unpack(fmt, data.read(fmt_size))[0]
            self.ClientNonce = ByteString.from_binary(data)
            fmt = '<I'
            fmt_size = RequestedLifetime
            self.RequestedLifetime = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = OpenSecureChannelParameters.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            fmt = '<I'
            fmt_size = ServerProtocolVersion
            self.ServerProtocolVersion = struct.unpack(fmt, data.read(fmt_size))[0]
            self.SecurityToken = ChannelSecurityToken.from_binary(data)
            self.ServerNonce = ByteString.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            self.Parameters = OpenSecureChannelResult.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.CertificateData = ByteString.from_binary(data)
            self.Signature = ByteString.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            slength = struct.unpack('<i', data.red(1))
            self.Algorithm = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.Signature = ByteString.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.ClientDescription = ApplicationDescription.from_binary(data)
            slength = struct.unpack('<i', data.red(1))
            self.ServerUri = struct.unpack('<{}s'.format(slength), data.read(slength))
            slength = struct.unpack('<i', data.red(1))
            self.EndpointUrl = struct.unpack('<{}s'.format(slength), data.read(slength))
            slength = struct.unpack('<i', data.red(1))
            self.SessionName = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.ClientNonce = ByteString.from_binary(data)
            self.ClientCertificate = ByteString.from_binary(data)
            fmt = '<d'
            fmt_size = RequestedSessionTimeout
            self.RequestedSessionTimeout = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = MaxResponseMessageSize
            self.MaxResponseMessageSize = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = CreateSessionParameters.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.SessionId = NodeId.from_binary(data)
            self.AuthenticationToken = NodeId.from_binary(data)
            fmt = '<d'
            fmt_size = RevisedSessionTimeout
            self.RevisedSessionTimeout = struct.unpack(fmt, data.read(fmt_size))[0]
            self.ServerNonce = ByteString.from_binary(data)
            self.ServerCertificate = ByteString.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.ServerEndpoints = EndpointDescription.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.ServerSoftwareCertificates = SignedSoftwareCertificate.from_binary(data)
            self.ServerSignature = SignatureData.from_binary(data)
            fmt = '<I'
            fmt_size = MaxRequestMessageSize
            self.MaxRequestMessageSize = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            self.Parameters = CreateSessionResult.from_binary(data)
            return data
            
class UserIdentityToken(object):
    def __init__(self):
        self.PolicyId = ''
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.PolicyId)))
        packet.append(struct.pack('<{}s'.format(len(self.PolicyId)), self.PolicyId.encode()))
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            slength = struct.unpack('<i', data.red(1))
            self.PolicyId = struct.unpack('<{}s'.format(slength), data.read(slength))
            return data
            
class AnonymousIdentityToken(object):
    def __init__(self):
        self.PolicyId = ''
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.PolicyId)))
        packet.append(struct.pack('<{}s'.format(len(self.PolicyId)), self.PolicyId.encode()))
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            slength = struct.unpack('<i', data.red(1))
            self.PolicyId = struct.unpack('<{}s'.format(slength), data.read(slength))
            return data
            
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
        def from_binary(self, data):
            slength = struct.unpack('<i', data.red(1))
            self.PolicyId = struct.unpack('<{}s'.format(slength), data.read(slength))
            slength = struct.unpack('<i', data.red(1))
            self.UserName = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.Password = ByteString.from_binary(data)
            slength = struct.unpack('<i', data.red(1))
            self.EncryptionAlgorithm = struct.unpack('<{}s'.format(slength), data.read(slength))
            return data
            
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
        def from_binary(self, data):
            slength = struct.unpack('<i', data.red(1))
            self.PolicyId = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.CertificateData = ByteString.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            slength = struct.unpack('<i', data.red(1))
            self.PolicyId = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.TokenData = ByteString.from_binary(data)
            slength = struct.unpack('<i', data.red(1))
            self.EncryptionAlgorithm = struct.unpack('<{}s'.format(slength), data.read(slength))
            return data
            
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
        def from_binary(self, data):
            self.ClientSignature = SignatureData.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.ClientSoftwareCertificates = SignedSoftwareCertificate.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    slength = struct.unpack('<i', data.red(1))
                    self.LocaleIds = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.UserIdentityToken = ExtensionObject.from_binary(data)
            self.UserTokenSignature = SignatureData.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = ActivateSessionParameters.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.ServerNonce = ByteString.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.Results = StatusCode.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.DiagnosticInfos = DiagnosticInfo.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            self.Parameters = ActivateSessionResult.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            fmt = '<?'
            fmt_size = DeleteSubscriptions
            self.DeleteSubscriptions = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            return data
            
class CancelParameters(object):
    def __init__(self):
        self.RequestHandle = 0
    
    def to_binary(self):
        packet = []
        fmt = '<I'
        packet.append(struct.pack(fmt, self.RequestHandle))
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            fmt = '<I'
            fmt_size = RequestHandle
            self.RequestHandle = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = CancelParameters.from_binary(data)
            return data
            
class CancelResult(object):
    def __init__(self):
        self.CancelCount = 0
    
    def to_binary(self):
        packet = []
        fmt = '<I'
        packet.append(struct.pack(fmt, self.CancelCount))
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            fmt = '<I'
            fmt_size = CancelCount
            self.CancelCount = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            self.Parameters = CancelResult.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            fmt = '<I'
            fmt_size = SpecifiedAttributes
            self.SpecifiedAttributes = struct.unpack(fmt, data.read(fmt_size))[0]
            self.DisplayName = LocalizedText.from_binary(data)
            self.Description = LocalizedText.from_binary(data)
            fmt = '<I'
            fmt_size = WriteMask
            self.WriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = UserWriteMask
            self.UserWriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            fmt = '<I'
            fmt_size = SpecifiedAttributes
            self.SpecifiedAttributes = struct.unpack(fmt, data.read(fmt_size))[0]
            self.DisplayName = LocalizedText.from_binary(data)
            self.Description = LocalizedText.from_binary(data)
            fmt = '<I'
            fmt_size = WriteMask
            self.WriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = UserWriteMask
            self.UserWriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<B'
            fmt_size = EventNotifier
            self.EventNotifier = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            fmt = '<I'
            fmt_size = SpecifiedAttributes
            self.SpecifiedAttributes = struct.unpack(fmt, data.read(fmt_size))[0]
            self.DisplayName = LocalizedText.from_binary(data)
            self.Description = LocalizedText.from_binary(data)
            fmt = '<I'
            fmt_size = WriteMask
            self.WriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = UserWriteMask
            self.UserWriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
            self.Value = Variant.from_binary(data)
            self.DataType = NodeId.from_binary(data)
            fmt = '<i'
            fmt_size = ValueRank
            self.ValueRank = struct.unpack(fmt, data.read(fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    fmt = '<I'
                    fmt_size = ArrayDimensions
                    self.ArrayDimensions = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<B'
            fmt_size = AccessLevel
            self.AccessLevel = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<B'
            fmt_size = UserAccessLevel
            self.UserAccessLevel = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<d'
            fmt_size = MinimumSamplingInterval
            self.MinimumSamplingInterval = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<?'
            fmt_size = Historizing
            self.Historizing = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            fmt = '<I'
            fmt_size = SpecifiedAttributes
            self.SpecifiedAttributes = struct.unpack(fmt, data.read(fmt_size))[0]
            self.DisplayName = LocalizedText.from_binary(data)
            self.Description = LocalizedText.from_binary(data)
            fmt = '<I'
            fmt_size = WriteMask
            self.WriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = UserWriteMask
            self.UserWriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<?'
            fmt_size = Executable
            self.Executable = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<?'
            fmt_size = UserExecutable
            self.UserExecutable = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            fmt = '<I'
            fmt_size = SpecifiedAttributes
            self.SpecifiedAttributes = struct.unpack(fmt, data.read(fmt_size))[0]
            self.DisplayName = LocalizedText.from_binary(data)
            self.Description = LocalizedText.from_binary(data)
            fmt = '<I'
            fmt_size = WriteMask
            self.WriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = UserWriteMask
            self.UserWriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<?'
            fmt_size = IsAbstract
            self.IsAbstract = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            fmt = '<I'
            fmt_size = SpecifiedAttributes
            self.SpecifiedAttributes = struct.unpack(fmt, data.read(fmt_size))[0]
            self.DisplayName = LocalizedText.from_binary(data)
            self.Description = LocalizedText.from_binary(data)
            fmt = '<I'
            fmt_size = WriteMask
            self.WriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = UserWriteMask
            self.UserWriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
            self.Value = Variant.from_binary(data)
            self.DataType = NodeId.from_binary(data)
            fmt = '<i'
            fmt_size = ValueRank
            self.ValueRank = struct.unpack(fmt, data.read(fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    fmt = '<I'
                    fmt_size = ArrayDimensions
                    self.ArrayDimensions = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<?'
            fmt_size = IsAbstract
            self.IsAbstract = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            fmt = '<I'
            fmt_size = SpecifiedAttributes
            self.SpecifiedAttributes = struct.unpack(fmt, data.read(fmt_size))[0]
            self.DisplayName = LocalizedText.from_binary(data)
            self.Description = LocalizedText.from_binary(data)
            fmt = '<I'
            fmt_size = WriteMask
            self.WriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = UserWriteMask
            self.UserWriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<?'
            fmt_size = IsAbstract
            self.IsAbstract = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<?'
            fmt_size = Symmetric
            self.Symmetric = struct.unpack(fmt, data.read(fmt_size))[0]
            self.InverseName = LocalizedText.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            fmt = '<I'
            fmt_size = SpecifiedAttributes
            self.SpecifiedAttributes = struct.unpack(fmt, data.read(fmt_size))[0]
            self.DisplayName = LocalizedText.from_binary(data)
            self.Description = LocalizedText.from_binary(data)
            fmt = '<I'
            fmt_size = WriteMask
            self.WriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = UserWriteMask
            self.UserWriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<?'
            fmt_size = IsAbstract
            self.IsAbstract = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            fmt = '<I'
            fmt_size = SpecifiedAttributes
            self.SpecifiedAttributes = struct.unpack(fmt, data.read(fmt_size))[0]
            self.DisplayName = LocalizedText.from_binary(data)
            self.Description = LocalizedText.from_binary(data)
            fmt = '<I'
            fmt_size = WriteMask
            self.WriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = UserWriteMask
            self.UserWriteMask = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<?'
            fmt_size = ContainsNoLoops
            self.ContainsNoLoops = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<B'
            fmt_size = EventNotifier
            self.EventNotifier = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            self.ParentNodeId = ExpandedNodeId.from_binary(data)
            self.ReferenceTypeId = NodeId.from_binary(data)
            self.RequestedNewNodeId = ExpandedNodeId.from_binary(data)
            self.BrowseName = QualifiedName.from_binary(data)
            fmt = '<I'
            fmt_size = NodeClass
            self.NodeClass = struct.unpack(fmt, data.read(fmt_size))[0]
            self.NodeAttributes = ExtensionObject.from_binary(data)
            self.TypeDefinition = ExpandedNodeId.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.StatusCode = StatusCode.from_binary(data)
            self.AddedNodeId = NodeId.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.NodesToAdd = AddNodesItem.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = AddNodesParameters.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.Results = AddNodesResult.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.DiagnosticInfos = DiagnosticInfo.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.SourceNodeId = NodeId.from_binary(data)
            self.ReferenceTypeId = NodeId.from_binary(data)
            fmt = '<?'
            fmt_size = IsForward
            self.IsForward = struct.unpack(fmt, data.read(fmt_size))[0]
            slength = struct.unpack('<i', data.red(1))
            self.TargetServerUri = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.TargetNodeId = ExpandedNodeId.from_binary(data)
            fmt = '<I'
            fmt_size = TargetNodeClass
            self.TargetNodeClass = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.ReferencesToAdd = AddReferencesItem.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = AddReferencesParameters.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.Results = StatusCode.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.DiagnosticInfos = DiagnosticInfo.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            self.Parameters = AddReferencesResult.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.NodeId = NodeId.from_binary(data)
            fmt = '<?'
            fmt_size = DeleteTargetReferences
            self.DeleteTargetReferences = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.NodesToDelete = DeleteNodesItem.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = DeleteNodesParameters.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.Results = StatusCode.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.DiagnosticInfos = DiagnosticInfo.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            self.Parameters = DeleteNodesResult.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.SourceNodeId = NodeId.from_binary(data)
            self.ReferenceTypeId = NodeId.from_binary(data)
            fmt = '<?'
            fmt_size = IsForward
            self.IsForward = struct.unpack(fmt, data.read(fmt_size))[0]
            self.TargetNodeId = ExpandedNodeId.from_binary(data)
            fmt = '<?'
            fmt_size = DeleteBidirectional
            self.DeleteBidirectional = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.ReferencesToDelete = DeleteReferencesItem.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = DeleteReferencesParameters.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.Results = StatusCode.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.DiagnosticInfos = DiagnosticInfo.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            self.Parameters = DeleteReferencesResult.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.ViewId = NodeId.from_binary(data)
            self.Timestamp = DateTime.from_binary(data)
            fmt = '<I'
            fmt_size = ViewVersion
            self.ViewVersion = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            self.NodeId = NodeId.from_binary(data)
            fmt = '<I'
            fmt_size = BrowseDirection
            self.BrowseDirection = struct.unpack(fmt, data.read(fmt_size))[0]
            self.ReferenceTypeId = NodeId.from_binary(data)
            fmt = '<?'
            fmt_size = IncludeSubtypes
            self.IncludeSubtypes = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = NodeClassMask
            self.NodeClassMask = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = ResultMask
            self.ResultMask = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            self.ReferenceTypeId = NodeId.from_binary(data)
            fmt = '<?'
            fmt_size = IsForward
            self.IsForward = struct.unpack(fmt, data.read(fmt_size))[0]
            self.NodeId = ExpandedNodeId.from_binary(data)
            self.BrowseName = QualifiedName.from_binary(data)
            self.DisplayName = LocalizedText.from_binary(data)
            fmt = '<I'
            fmt_size = NodeClass
            self.NodeClass = struct.unpack(fmt, data.read(fmt_size))[0]
            self.TypeDefinition = ExpandedNodeId.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.StatusCode = StatusCode.from_binary(data)
            self.ContinuationPoint = ByteString.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.References = ReferenceDescription.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.View = ViewDescription.from_binary(data)
            fmt = '<I'
            fmt_size = RequestedMaxReferencesPerNode
            self.RequestedMaxReferencesPerNode = struct.unpack(fmt, data.read(fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.NodesToBrowse = BrowseDescription.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = BrowseParameters.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.Results = BrowseResult.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.DiagnosticInfos = DiagnosticInfo.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            fmt = '<?'
            fmt_size = ReleaseContinuationPoints
            self.ReleaseContinuationPoints = struct.unpack(fmt, data.read(fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.ContinuationPoints = ByteString.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = BrowseNextParameters.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.Results = BrowseResult.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.DiagnosticInfos = DiagnosticInfo.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            self.Parameters = BrowseNextResult.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.ReferenceTypeId = NodeId.from_binary(data)
            fmt = '<?'
            fmt_size = IsInverse
            self.IsInverse = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<?'
            fmt_size = IncludeSubtypes
            self.IncludeSubtypes = struct.unpack(fmt, data.read(fmt_size))[0]
            self.TargetName = QualifiedName.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.Elements = RelativePathElement.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.StartingNode = NodeId.from_binary(data)
            self.RelativePath = RelativePath.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TargetId = ExpandedNodeId.from_binary(data)
            fmt = '<I'
            fmt_size = RemainingPathIndex
            self.RemainingPathIndex = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            self.StatusCode = StatusCode.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.Targets = BrowsePathTarget.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.BrowsePaths = BrowsePath.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = TranslateBrowsePathsToNodeIdsParameters.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.Results = BrowsePathResult.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.DiagnosticInfos = DiagnosticInfo.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            self.Parameters = TranslateBrowsePathsToNodeIdsResult.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.NodesToRegister = NodeId.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = RegisterNodesParameters.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.RegisteredNodeIds = NodeId.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            self.Parameters = RegisterNodesResult.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.NodesToUnregister = NodeId.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = UnregisterNodesParameters.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            fmt = '<i'
            fmt_size = OperationTimeout
            self.OperationTimeout = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<?'
            fmt_size = UseBinaryEncoding
            self.UseBinaryEncoding = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<i'
            fmt_size = MaxStringLength
            self.MaxStringLength = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<i'
            fmt_size = MaxByteStringLength
            self.MaxByteStringLength = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<i'
            fmt_size = MaxArrayLength
            self.MaxArrayLength = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<i'
            fmt_size = MaxMessageSize
            self.MaxMessageSize = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<i'
            fmt_size = MaxBufferSize
            self.MaxBufferSize = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<i'
            fmt_size = ChannelLifetime
            self.ChannelLifetime = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<i'
            fmt_size = SecurityTokenLifetime
            self.SecurityTokenLifetime = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            slength = struct.unpack('<i', data.red(1))
            self.OrganizationUri = struct.unpack('<{}s'.format(slength), data.read(slength))
            slength = struct.unpack('<i', data.red(1))
            self.ProfileId = struct.unpack('<{}s'.format(slength), data.read(slength))
            slength = struct.unpack('<i', data.red(1))
            self.ComplianceTool = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.ComplianceDate = DateTime.from_binary(data)
            fmt = '<I'
            fmt_size = ComplianceLevel
            self.ComplianceLevel = struct.unpack(fmt, data.read(fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    slength = struct.unpack('<i', data.red(1))
                    self.UnsupportedUnitIds = struct.unpack('<{}s'.format(slength), data.read(slength))
            return data
            
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
        def from_binary(self, data):
            slength = struct.unpack('<i', data.red(1))
            self.ProductName = struct.unpack('<{}s'.format(slength), data.read(slength))
            slength = struct.unpack('<i', data.red(1))
            self.ProductUri = struct.unpack('<{}s'.format(slength), data.read(slength))
            slength = struct.unpack('<i', data.red(1))
            self.VendorName = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.VendorProductCertificate = ByteString.from_binary(data)
            slength = struct.unpack('<i', data.red(1))
            self.SoftwareVersion = struct.unpack('<{}s'.format(slength), data.read(slength))
            slength = struct.unpack('<i', data.red(1))
            self.BuildNumber = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.BuildDate = DateTime.from_binary(data)
            slength = struct.unpack('<i', data.red(1))
            self.IssuedBy = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.IssueDate = DateTime.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.SupportedProfiles = SupportedProfile.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.RelativePath = RelativePath.from_binary(data)
            fmt = '<I'
            fmt_size = AttributeId
            self.AttributeId = struct.unpack(fmt, data.read(fmt_size))[0]
            slength = struct.unpack('<i', data.red(1))
            self.IndexRange = struct.unpack('<{}s'.format(slength), data.read(slength))
            return data
            
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
        def from_binary(self, data):
            self.TypeDefinitionNode = ExpandedNodeId.from_binary(data)
            fmt = '<?'
            fmt_size = IncludeSubTypes
            self.IncludeSubTypes = struct.unpack(fmt, data.read(fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.DataToReturn = QueryDataDescription.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.NodeId = ExpandedNodeId.from_binary(data)
            self.TypeDefinitionNode = ExpandedNodeId.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.Values = Variant.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.NodeId = NodeId.from_binary(data)
            self.ReferenceTypeId = NodeId.from_binary(data)
            fmt = '<?'
            fmt_size = IsForward
            self.IsForward = struct.unpack(fmt, data.read(fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.ReferencedNodeIds = NodeId.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            fmt = '<I'
            fmt_size = FilterOperator
            self.FilterOperator = struct.unpack(fmt, data.read(fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.FilterOperands = ExtensionObject.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.Elements = ContentFilterElement.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            fmt = '<B'
            fmt_size = Encoding
            self.Encoding = struct.unpack(fmt, data.read(fmt_size))[0]
            bodylength = struct.unpack('<i', data.read(4))[0]
            fmt = '<I'
            fmt_size = Index
            self.Index = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            fmt = '<B'
            fmt_size = Encoding
            self.Encoding = struct.unpack(fmt, data.read(fmt_size))[0]
            bodylength = struct.unpack('<i', data.read(4))[0]
            self.Value = Variant.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            fmt = '<B'
            fmt_size = Encoding
            self.Encoding = struct.unpack(fmt, data.read(fmt_size))[0]
            bodylength = struct.unpack('<i', data.read(4))[0]
            self.NodeId = NodeId.from_binary(data)
            slength = struct.unpack('<i', data.red(1))
            self.Alias = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.BrowsePath = RelativePath.from_binary(data)
            fmt = '<I'
            fmt_size = AttributeId
            self.AttributeId = struct.unpack(fmt, data.read(fmt_size))[0]
            slength = struct.unpack('<i', data.red(1))
            self.IndexRange = struct.unpack('<{}s'.format(slength), data.read(slength))
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            fmt = '<B'
            fmt_size = Encoding
            self.Encoding = struct.unpack(fmt, data.read(fmt_size))[0]
            bodylength = struct.unpack('<i', data.read(4))[0]
            self.TypeDefinitionId = NodeId.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.BrowsePath = QualifiedName.from_binary(data)
            fmt = '<I'
            fmt_size = AttributeId
            self.AttributeId = struct.unpack(fmt, data.read(fmt_size))[0]
            slength = struct.unpack('<i', data.red(1))
            self.IndexRange = struct.unpack('<{}s'.format(slength), data.read(slength))
            return data
            
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
        def from_binary(self, data):
            self.StatusCode = StatusCode.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.OperandStatusCodes = StatusCode.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.OperandDiagnosticInfos = DiagnosticInfo.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.ElementResults = ContentFilterElementResult.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.ElementDiagnosticInfos = DiagnosticInfo.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.StatusCode = StatusCode.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.DataStatusCodes = StatusCode.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.DataDiagnosticInfos = DiagnosticInfo.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.View = ViewDescription.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.NodeTypes = NodeTypeDescription.from_binary(data)
            self.Filter = ContentFilter.from_binary(data)
            fmt = '<I'
            fmt_size = MaxDataSetsToReturn
            self.MaxDataSetsToReturn = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = MaxReferencesToReturn
            self.MaxReferencesToReturn = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = QueryFirstParameters.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.QueryDataSets = QueryDataSet.from_binary(data)
            self.ContinuationPoint = ByteString.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.ParsingResults = ParsingResult.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.DiagnosticInfos = DiagnosticInfo.from_binary(data)
            self.FilterResult = ContentFilterResult.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            self.Parameters = QueryFirstResult.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            fmt = '<?'
            fmt_size = ReleaseContinuationPoint
            self.ReleaseContinuationPoint = struct.unpack(fmt, data.read(fmt_size))[0]
            self.ContinuationPoint = ByteString.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = QueryNextParameters.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.QueryDataSets = QueryDataSet.from_binary(data)
            self.RevisedContinuationPoint = ByteString.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            self.Parameters = QueryNextResult.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.NodeId = NodeId.from_binary(data)
            fmt = '<I'
            fmt_size = AttributeId
            self.AttributeId = struct.unpack(fmt, data.read(fmt_size))[0]
            slength = struct.unpack('<i', data.red(1))
            self.IndexRange = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.DataEncoding = QualifiedName.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            fmt = '<d'
            fmt_size = MaxAge
            self.MaxAge = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = TimestampsToReturn
            self.TimestampsToReturn = struct.unpack(fmt, data.read(fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.NodesToRead = ReadValueId.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = ReadParameters.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.Results = DataValue.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.DiagnosticInfos = DiagnosticInfo.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            self.Parameters = ReadResult.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.NodeId = NodeId.from_binary(data)
            slength = struct.unpack('<i', data.red(1))
            self.IndexRange = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.DataEncoding = QualifiedName.from_binary(data)
            self.ContinuationPoint = ByteString.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.StatusCode = StatusCode.from_binary(data)
            self.ContinuationPoint = ByteString.from_binary(data)
            self.HistoryData = ExtensionObject.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            fmt = '<B'
            fmt_size = Encoding
            self.Encoding = struct.unpack(fmt, data.read(fmt_size))[0]
            bodylength = struct.unpack('<i', data.read(4))[0]
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            fmt = '<B'
            fmt_size = Encoding
            self.Encoding = struct.unpack(fmt, data.read(fmt_size))[0]
            bodylength = struct.unpack('<i', data.read(4))[0]
            fmt = '<I'
            fmt_size = NumValuesPerNode
            self.NumValuesPerNode = struct.unpack(fmt, data.read(fmt_size))[0]
            self.StartTime = DateTime.from_binary(data)
            self.EndTime = DateTime.from_binary(data)
            self.Filter = EventFilter.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            fmt = '<B'
            fmt_size = Encoding
            self.Encoding = struct.unpack(fmt, data.read(fmt_size))[0]
            bodylength = struct.unpack('<i', data.read(4))[0]
            fmt = '<?'
            fmt_size = IsReadModified
            self.IsReadModified = struct.unpack(fmt, data.read(fmt_size))[0]
            self.StartTime = DateTime.from_binary(data)
            self.EndTime = DateTime.from_binary(data)
            fmt = '<I'
            fmt_size = NumValuesPerNode
            self.NumValuesPerNode = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<?'
            fmt_size = ReturnBounds
            self.ReturnBounds = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            fmt = '<B'
            fmt_size = Encoding
            self.Encoding = struct.unpack(fmt, data.read(fmt_size))[0]
            bodylength = struct.unpack('<i', data.read(4))[0]
            self.StartTime = DateTime.from_binary(data)
            self.EndTime = DateTime.from_binary(data)
            fmt = '<d'
            fmt_size = ProcessingInterval
            self.ProcessingInterval = struct.unpack(fmt, data.read(fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.AggregateType = NodeId.from_binary(data)
            self.AggregateConfiguration = AggregateConfiguration.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            fmt = '<B'
            fmt_size = Encoding
            self.Encoding = struct.unpack(fmt, data.read(fmt_size))[0]
            bodylength = struct.unpack('<i', data.read(4))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.ReqTimes = DateTime.from_binary(data)
            fmt = '<?'
            fmt_size = UseSimpleBounds
            self.UseSimpleBounds = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.DataValues = DataValue.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.ModificationTime = DateTime.from_binary(data)
            fmt = '<I'
            fmt_size = UpdateType
            self.UpdateType = struct.unpack(fmt, data.read(fmt_size))[0]
            slength = struct.unpack('<i', data.red(1))
            self.UserName = struct.unpack('<{}s'.format(slength), data.read(slength))
            return data
            
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
        def from_binary(self, data):
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.DataValues = DataValue.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.ModificationInfos = ModificationInfo.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.Events = HistoryEventFieldList.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.HistoryReadDetails = ExtensionObject.from_binary(data)
            fmt = '<I'
            fmt_size = TimestampsToReturn
            self.TimestampsToReturn = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<?'
            fmt_size = ReleaseContinuationPoints
            self.ReleaseContinuationPoints = struct.unpack(fmt, data.read(fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.NodesToRead = HistoryReadValueId.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = HistoryReadParameters.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.Results = HistoryReadResult.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.DiagnosticInfos = DiagnosticInfo.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.NodeId = NodeId.from_binary(data)
            fmt = '<I'
            fmt_size = AttributeId
            self.AttributeId = struct.unpack(fmt, data.read(fmt_size))[0]
            slength = struct.unpack('<i', data.red(1))
            self.IndexRange = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.Value = DataValue.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.NodesToWrite = WriteValue.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = WriteParameters.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.Results = StatusCode.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.DiagnosticInfos = DiagnosticInfo.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            self.Parameters = WriteResult.from_binary(data)
            return data
            
class HistoryUpdateDetails(object):
    def __init__(self):
        self.NodeId = NodeId()
    
    def to_binary(self):
        packet = []
        packet.append(self.NodeId.to_binary())
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.NodeId = NodeId.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.NodeId = NodeId.from_binary(data)
            fmt = '<I'
            fmt_size = PerformInsertReplace
            self.PerformInsertReplace = struct.unpack(fmt, data.read(fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.UpdateValues = DataValue.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.NodeId = NodeId.from_binary(data)
            fmt = '<I'
            fmt_size = PerformInsertReplace
            self.PerformInsertReplace = struct.unpack(fmt, data.read(fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.UpdateValues = DataValue.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.NodeId = NodeId.from_binary(data)
            fmt = '<I'
            fmt_size = PerformInsertReplace
            self.PerformInsertReplace = struct.unpack(fmt, data.read(fmt_size))[0]
            self.Filter = EventFilter.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.EventData = HistoryEventFieldList.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.NodeId = NodeId.from_binary(data)
            fmt = '<?'
            fmt_size = IsDeleteModified
            self.IsDeleteModified = struct.unpack(fmt, data.read(fmt_size))[0]
            self.StartTime = DateTime.from_binary(data)
            self.EndTime = DateTime.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.NodeId = NodeId.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.ReqTimes = DateTime.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.NodeId = NodeId.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.EventIds = ByteString.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.StatusCode = StatusCode.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.OperationResults = StatusCode.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.DiagnosticInfos = DiagnosticInfo.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.StatusCode = StatusCode.from_binary(data)
            self.EventFilterResult = EventFilterResult.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.HistoryUpdateDetails = ExtensionObject.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = HistoryUpdateParameters.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.Results = HistoryUpdateResult.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.DiagnosticInfos = DiagnosticInfo.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.MethodId = NodeId.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.InputArguments = Variant.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.ObjectId = NodeId.from_binary(data)
            self.Parameters = CallMethodParameters.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.StatusCode = StatusCode.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.InputArgumentResults = StatusCode.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.InputArgumentDiagnosticInfos = DiagnosticInfo.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.OutputArguments = Variant.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.MethodsToCall = CallMethodRequest.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = CallParameters.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.Results = CallMethodResult.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.DiagnosticInfos = DiagnosticInfo.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            self.Parameters = CallResult.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            fmt = '<B'
            fmt_size = Encoding
            self.Encoding = struct.unpack(fmt, data.read(fmt_size))[0]
            bodylength = struct.unpack('<i', data.read(4))[0]
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            fmt = '<B'
            fmt_size = Encoding
            self.Encoding = struct.unpack(fmt, data.read(fmt_size))[0]
            bodylength = struct.unpack('<i', data.read(4))[0]
            fmt = '<I'
            fmt_size = Trigger
            self.Trigger = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = DeadbandType
            self.DeadbandType = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<d'
            fmt_size = DeadbandValue
            self.DeadbandValue = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            fmt = '<B'
            fmt_size = Encoding
            self.Encoding = struct.unpack(fmt, data.read(fmt_size))[0]
            bodylength = struct.unpack('<i', data.read(4))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.SelectClauses = SimpleAttributeOperand.from_binary(data)
            self.WhereClause = ContentFilter.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            fmt = '<?'
            fmt_size = UseServerCapabilitiesDefaults
            self.UseServerCapabilitiesDefaults = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<?'
            fmt_size = TreatUncertainAsBad
            self.TreatUncertainAsBad = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<B'
            fmt_size = PercentDataBad
            self.PercentDataBad = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<B'
            fmt_size = PercentDataGood
            self.PercentDataGood = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<?'
            fmt_size = UseSlopedExtrapolation
            self.UseSlopedExtrapolation = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            fmt = '<B'
            fmt_size = Encoding
            self.Encoding = struct.unpack(fmt, data.read(fmt_size))[0]
            bodylength = struct.unpack('<i', data.read(4))[0]
            self.StartTime = DateTime.from_binary(data)
            self.AggregateType = NodeId.from_binary(data)
            fmt = '<d'
            fmt_size = ProcessingInterval
            self.ProcessingInterval = struct.unpack(fmt, data.read(fmt_size))[0]
            self.AggregateConfiguration = AggregateConfiguration.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            fmt = '<B'
            fmt_size = Encoding
            self.Encoding = struct.unpack(fmt, data.read(fmt_size))[0]
            bodylength = struct.unpack('<i', data.read(4))[0]
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            fmt = '<B'
            fmt_size = Encoding
            self.Encoding = struct.unpack(fmt, data.read(fmt_size))[0]
            bodylength = struct.unpack('<i', data.read(4))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.SelectClauseResults = StatusCode.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.SelectClauseDiagnosticInfos = DiagnosticInfo.from_binary(data)
            self.WhereClauseResult = ContentFilterResult.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            fmt = '<B'
            fmt_size = Encoding
            self.Encoding = struct.unpack(fmt, data.read(fmt_size))[0]
            bodylength = struct.unpack('<i', data.read(4))[0]
            self.RevisedStartTime = DateTime.from_binary(data)
            fmt = '<d'
            fmt_size = RevisedProcessingInterval
            self.RevisedProcessingInterval = struct.unpack(fmt, data.read(fmt_size))[0]
            self.RevisedAggregateConfiguration = AggregateConfiguration.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            fmt = '<I'
            fmt_size = ClientHandle
            self.ClientHandle = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<d'
            fmt_size = SamplingInterval
            self.SamplingInterval = struct.unpack(fmt, data.read(fmt_size))[0]
            self.Filter = ExtensionObject.from_binary(data)
            fmt = '<I'
            fmt_size = QueueSize
            self.QueueSize = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<?'
            fmt_size = DiscardOldest
            self.DiscardOldest = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            fmt = '<I'
            fmt_size = MonitoringMode
            self.MonitoringMode = struct.unpack(fmt, data.read(fmt_size))[0]
            self.RequestedParameters = MonitoringParameters.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.ItemToMonitor = ReadValueId.from_binary(data)
            self.Parameters = MonitoredItemCreateParameters.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.StatusCode = StatusCode.from_binary(data)
            fmt = '<I'
            fmt_size = MonitoredItemId
            self.MonitoredItemId = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<d'
            fmt_size = RevisedSamplingInterval
            self.RevisedSamplingInterval = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = RevisedQueueSize
            self.RevisedQueueSize = struct.unpack(fmt, data.read(fmt_size))[0]
            self.FilterResult = ExtensionObject.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            fmt = '<I'
            fmt_size = SubscriptionId
            self.SubscriptionId = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = TimestampsToReturn
            self.TimestampsToReturn = struct.unpack(fmt, data.read(fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.ItemsToCreate = MonitoredItemCreateRequest.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = CreateMonitoredItemsParameters.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.Results = MonitoredItemCreateResult.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.DiagnosticInfos = DiagnosticInfo.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            self.Parameters = CreateMonitoredItemsResult.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            fmt = '<I'
            fmt_size = MonitoredItemId
            self.MonitoredItemId = struct.unpack(fmt, data.read(fmt_size))[0]
            self.RequestedParameters = MonitoringParameters.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.StatusCode = StatusCode.from_binary(data)
            fmt = '<d'
            fmt_size = RevisedSamplingInterval
            self.RevisedSamplingInterval = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = RevisedQueueSize
            self.RevisedQueueSize = struct.unpack(fmt, data.read(fmt_size))[0]
            self.FilterResult = ExtensionObject.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            fmt = '<I'
            fmt_size = SubscriptionId
            self.SubscriptionId = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = TimestampsToReturn
            self.TimestampsToReturn = struct.unpack(fmt, data.read(fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.ItemsToModify = MonitoredItemModifyRequest.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = ModifyMonitoredItemsParameters.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.Results = MonitoredItemModifyResult.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.DiagnosticInfos = DiagnosticInfo.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            self.Parameters = ModifyMonitoredItemsResult.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            fmt = '<I'
            fmt_size = SubscriptionId
            self.SubscriptionId = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = MonitoringMode
            self.MonitoringMode = struct.unpack(fmt, data.read(fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    fmt = '<I'
                    fmt_size = MonitoredItemIds
                    self.MonitoredItemIds = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = SetMonitoringModeParameters.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.Results = StatusCode.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.DiagnosticInfos = DiagnosticInfo.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            self.Parameters = SetMonitoringModeResult.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            fmt = '<I'
            fmt_size = SubscriptionId
            self.SubscriptionId = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = TriggeringItemId
            self.TriggeringItemId = struct.unpack(fmt, data.read(fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    fmt = '<I'
                    fmt_size = LinksToAdd
                    self.LinksToAdd = struct.unpack(fmt, data.read(fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    fmt = '<I'
                    fmt_size = LinksToRemove
                    self.LinksToRemove = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = SetTriggeringParameters.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.AddResults = StatusCode.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.AddDiagnosticInfos = DiagnosticInfo.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.RemoveResults = StatusCode.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.RemoveDiagnosticInfos = DiagnosticInfo.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            self.Parameters = SetTriggeringResult.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            fmt = '<I'
            fmt_size = SubscriptionId
            self.SubscriptionId = struct.unpack(fmt, data.read(fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    fmt = '<I'
                    fmt_size = MonitoredItemIds
                    self.MonitoredItemIds = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = DeleteMonitoredItemsParameters.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.Results = StatusCode.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.DiagnosticInfos = DiagnosticInfo.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            self.Parameters = DeleteMonitoredItemsResult.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            fmt = '<d'
            fmt_size = RequestedPublishingInterval
            self.RequestedPublishingInterval = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = RequestedLifetimeCount
            self.RequestedLifetimeCount = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = RequestedMaxKeepAliveCount
            self.RequestedMaxKeepAliveCount = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = MaxNotificationsPerPublish
            self.MaxNotificationsPerPublish = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<?'
            fmt_size = PublishingEnabled
            self.PublishingEnabled = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<B'
            fmt_size = Priority
            self.Priority = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = CreateSubscriptionParameters.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            fmt = '<I'
            fmt_size = SubscriptionId
            self.SubscriptionId = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<d'
            fmt_size = RevisedPublishingInterval
            self.RevisedPublishingInterval = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = RevisedLifetimeCount
            self.RevisedLifetimeCount = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = RevisedMaxKeepAliveCount
            self.RevisedMaxKeepAliveCount = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            self.Parameters = CreateSubscriptionResult.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            fmt = '<I'
            fmt_size = SubscriptionId
            self.SubscriptionId = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<d'
            fmt_size = RequestedPublishingInterval
            self.RequestedPublishingInterval = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = RequestedLifetimeCount
            self.RequestedLifetimeCount = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = RequestedMaxKeepAliveCount
            self.RequestedMaxKeepAliveCount = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = MaxNotificationsPerPublish
            self.MaxNotificationsPerPublish = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<B'
            fmt_size = Priority
            self.Priority = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = ModifySubscriptionParameters.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            fmt = '<d'
            fmt_size = RevisedPublishingInterval
            self.RevisedPublishingInterval = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = RevisedLifetimeCount
            self.RevisedLifetimeCount = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = RevisedMaxKeepAliveCount
            self.RevisedMaxKeepAliveCount = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            self.Parameters = ModifySubscriptionResult.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            fmt = '<?'
            fmt_size = PublishingEnabled
            self.PublishingEnabled = struct.unpack(fmt, data.read(fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    fmt = '<I'
                    fmt_size = SubscriptionIds
                    self.SubscriptionIds = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = SetPublishingModeParameters.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.Results = StatusCode.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.DiagnosticInfos = DiagnosticInfo.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            self.Parameters = SetPublishingModeResult.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            fmt = '<I'
            fmt_size = SequenceNumber
            self.SequenceNumber = struct.unpack(fmt, data.read(fmt_size))[0]
            self.PublishTime = DateTime.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.NotificationData = ExtensionObject.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            fmt = '<B'
            fmt_size = Encoding
            self.Encoding = struct.unpack(fmt, data.read(fmt_size))[0]
            bodylength = struct.unpack('<i', data.read(4))[0]
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            fmt = '<B'
            fmt_size = Encoding
            self.Encoding = struct.unpack(fmt, data.read(fmt_size))[0]
            bodylength = struct.unpack('<i', data.read(4))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.MonitoredItems = MonitoredItemNotification.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.DiagnosticInfos = DiagnosticInfo.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            fmt = '<I'
            fmt_size = ClientHandle
            self.ClientHandle = struct.unpack(fmt, data.read(fmt_size))[0]
            self.Value = DataValue.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            fmt = '<B'
            fmt_size = Encoding
            self.Encoding = struct.unpack(fmt, data.read(fmt_size))[0]
            bodylength = struct.unpack('<i', data.read(4))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.Events = EventFieldList.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            fmt = '<I'
            fmt_size = ClientHandle
            self.ClientHandle = struct.unpack(fmt, data.read(fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.EventFields = Variant.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.EventFields = Variant.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            fmt = '<B'
            fmt_size = Encoding
            self.Encoding = struct.unpack(fmt, data.read(fmt_size))[0]
            bodylength = struct.unpack('<i', data.read(4))[0]
            self.Status = StatusCode.from_binary(data)
            self.DiagnosticInfo = DiagnosticInfo.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            fmt = '<I'
            fmt_size = SubscriptionId
            self.SubscriptionId = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = SequenceNumber
            self.SequenceNumber = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.SubscriptionAcknowledgements = SubscriptionAcknowledgement.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = PublishParameters.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            fmt = '<I'
            fmt_size = SubscriptionId
            self.SubscriptionId = struct.unpack(fmt, data.read(fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    fmt = '<I'
                    fmt_size = AvailableSequenceNumbers
                    self.AvailableSequenceNumbers = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<?'
            fmt_size = MoreNotifications
            self.MoreNotifications = struct.unpack(fmt, data.read(fmt_size))[0]
            self.NotificationMessage = NotificationMessage.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.Results = StatusCode.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.DiagnosticInfos = DiagnosticInfo.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            self.Parameters = PublishResult.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            fmt = '<I'
            fmt_size = SubscriptionId
            self.SubscriptionId = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = RetransmitSequenceNumber
            self.RetransmitSequenceNumber = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = RepublishParameters.from_binary(data)
            return data
            
class RepublishResult(object):
    def __init__(self):
        self.NotificationMessage = NotificationMessage()
    
    def to_binary(self):
        packet = []
        packet.append(self.NotificationMessage.to_binary())
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.NotificationMessage = NotificationMessage.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            self.Parameters = RepublishResult.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.StatusCode = StatusCode.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    fmt = '<I'
                    fmt_size = AvailableSequenceNumbers
                    self.AvailableSequenceNumbers = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    fmt = '<I'
                    fmt_size = SubscriptionIds
                    self.SubscriptionIds = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<?'
            fmt_size = SendInitialValues
            self.SendInitialValues = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = TransferSubscriptionsParameters.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.Results = TransferResult.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.DiagnosticInfos = DiagnosticInfo.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            self.Parameters = TransferSubscriptionsResult.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    fmt = '<I'
                    fmt_size = SubscriptionIds
                    self.SubscriptionIds = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = DeleteSubscriptionsParameters.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.Results = StatusCode.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.DiagnosticInfos = DiagnosticInfo.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            self.Parameters = DeleteSubscriptionsResult.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            fmt = '<?'
            fmt_size = Boolean
            self.Boolean = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<B'
            fmt_size = SByte
            self.SByte = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<B'
            fmt_size = Byte
            self.Byte = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<h'
            fmt_size = Int16
            self.Int16 = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<H'
            fmt_size = UInt16
            self.UInt16 = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<i'
            fmt_size = Int32
            self.Int32 = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = UInt32
            self.UInt32 = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<q'
            fmt_size = Int64
            self.Int64 = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<Q'
            fmt_size = UInt64
            self.UInt64 = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<f'
            fmt_size = Float
            self.Float = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<d'
            fmt_size = Double
            self.Double = struct.unpack(fmt, data.read(fmt_size))[0]
            slength = struct.unpack('<i', data.red(1))
            self.String = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.DateTime = DateTime.from_binary(data)
            self.Guid = Guid.from_binary(data)
            self.ByteString = ByteString.from_binary(data)
            self.XmlElement = XmlElement.from_binary(data)
            self.NodeId = NodeId.from_binary(data)
            self.ExpandedNodeId = ExpandedNodeId.from_binary(data)
            self.StatusCode = StatusCode.from_binary(data)
            self.DiagnosticInfo = DiagnosticInfo.from_binary(data)
            self.QualifiedName = QualifiedName.from_binary(data)
            self.LocalizedText = LocalizedText.from_binary(data)
            self.ExtensionObject = ExtensionObject.from_binary(data)
            self.DataValue = DataValue.from_binary(data)
            fmt = '<I'
            fmt_size = EnumeratedValue
            self.EnumeratedValue = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    fmt = '<?'
                    fmt_size = Booleans
                    self.Booleans = struct.unpack(fmt, data.read(fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    fmt = '<B'
                    fmt_size = SBytes
                    self.SBytes = struct.unpack(fmt, data.read(fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    fmt = '<h'
                    fmt_size = Int16s
                    self.Int16s = struct.unpack(fmt, data.read(fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    fmt = '<H'
                    fmt_size = UInt16s
                    self.UInt16s = struct.unpack(fmt, data.read(fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    fmt = '<i'
                    fmt_size = Int32s
                    self.Int32s = struct.unpack(fmt, data.read(fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    fmt = '<I'
                    fmt_size = UInt32s
                    self.UInt32s = struct.unpack(fmt, data.read(fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    fmt = '<q'
                    fmt_size = Int64s
                    self.Int64s = struct.unpack(fmt, data.read(fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    fmt = '<Q'
                    fmt_size = UInt64s
                    self.UInt64s = struct.unpack(fmt, data.read(fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    fmt = '<f'
                    fmt_size = Floats
                    self.Floats = struct.unpack(fmt, data.read(fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    fmt = '<d'
                    fmt_size = Doubles
                    self.Doubles = struct.unpack(fmt, data.read(fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    slength = struct.unpack('<i', data.red(1))
                    self.Strings = struct.unpack('<{}s'.format(slength), data.read(slength))
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.DateTimes = DateTime.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.Guids = Guid.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.ByteStrings = ByteString.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.XmlElements = XmlElement.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.NodeIds = NodeId.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.ExpandedNodeIds = ExpandedNodeId.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.StatusCodes = StatusCode.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.DiagnosticInfos = DiagnosticInfo.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.QualifiedNames = QualifiedName.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.LocalizedTexts = LocalizedText.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.ExtensionObjects = ExtensionObject.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.DataValues = DataValue.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.Variants = Variant.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    fmt = '<I'
                    fmt_size = EnumeratedValues
                    self.EnumeratedValues = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            self.Field1 = ScalarTestType.from_binary(data)
            self.Field2 = ArrayTestType.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            fmt = '<I'
            fmt_size = TestId
            self.TestId = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<i'
            fmt_size = Iteration
            self.Iteration = struct.unpack(fmt, data.read(fmt_size))[0]
            self.Input = Variant.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = TestStackParameters.from_binary(data)
            return data
            
class TestStackResult(object):
    def __init__(self):
        self.Output = Variant()
    
    def to_binary(self):
        packet = []
        packet.append(self.Output.to_binary())
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.Output = Variant.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            self.Parameters = TestStackResult.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            fmt = '<I'
            fmt_size = TestId
            self.TestId = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<i'
            fmt_size = Iteration
            self.Iteration = struct.unpack(fmt, data.read(fmt_size))[0]
            self.Input = CompositeTestType.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = TestStackExParameters.from_binary(data)
            return data
            
class TestStackExResult(object):
    def __init__(self):
        self.Output = CompositeTestType()
    
    def to_binary(self):
        packet = []
        packet.append(self.Output.to_binary())
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.Output = CompositeTestType.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.TypeId = NodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            self.Parameters = TestStackExResult.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            slength = struct.unpack('<i', data.red(1))
            self.ProductUri = struct.unpack('<{}s'.format(slength), data.read(slength))
            slength = struct.unpack('<i', data.red(1))
            self.ManufacturerName = struct.unpack('<{}s'.format(slength), data.read(slength))
            slength = struct.unpack('<i', data.red(1))
            self.ProductName = struct.unpack('<{}s'.format(slength), data.read(slength))
            slength = struct.unpack('<i', data.red(1))
            self.SoftwareVersion = struct.unpack('<{}s'.format(slength), data.read(slength))
            slength = struct.unpack('<i', data.red(1))
            self.BuildNumber = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.BuildDate = DateTime.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            slength = struct.unpack('<i', data.red(1))
            self.ServerId = struct.unpack('<{}s'.format(slength), data.read(slength))
            fmt = '<B'
            fmt_size = ServiceLevel
            self.ServiceLevel = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = ServerState
            self.ServerState = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    slength = struct.unpack('<i', data.red(1))
                    self.EndpointUrlList = struct.unpack('<{}s'.format(slength), data.read(slength))
            return data
            
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
        def from_binary(self, data):
            slength = struct.unpack('<i', data.red(1))
            self.ServerUri = struct.unpack('<{}s'.format(slength), data.read(slength))
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.NetworkPaths = EndpointUrlListDataType.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            fmt = '<d'
            fmt_size = SamplingInterval
            self.SamplingInterval = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = MonitoredItemCount
            self.MonitoredItemCount = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = MaxMonitoredItemCount
            self.MaxMonitoredItemCount = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = DisabledMonitoredItemCount
            self.DisabledMonitoredItemCount = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            fmt = '<I'
            fmt_size = ServerViewCount
            self.ServerViewCount = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = CurrentSessionCount
            self.CurrentSessionCount = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = CumulatedSessionCount
            self.CumulatedSessionCount = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = SecurityRejectedSessionCount
            self.SecurityRejectedSessionCount = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = RejectedSessionCount
            self.RejectedSessionCount = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = SessionTimeoutCount
            self.SessionTimeoutCount = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = SessionAbortCount
            self.SessionAbortCount = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = CurrentSubscriptionCount
            self.CurrentSubscriptionCount = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = CumulatedSubscriptionCount
            self.CumulatedSubscriptionCount = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = PublishingIntervalCount
            self.PublishingIntervalCount = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = SecurityRejectedRequestsCount
            self.SecurityRejectedRequestsCount = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = RejectedRequestsCount
            self.RejectedRequestsCount = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            self.StartTime = DateTime.from_binary(data)
            self.CurrentTime = DateTime.from_binary(data)
            fmt = '<I'
            fmt_size = State
            self.State = struct.unpack(fmt, data.read(fmt_size))[0]
            self.BuildInfo = BuildInfo.from_binary(data)
            fmt = '<I'
            fmt_size = SecondsTillShutdown
            self.SecondsTillShutdown = struct.unpack(fmt, data.read(fmt_size))[0]
            self.ShutdownReason = LocalizedText.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.SessionId = NodeId.from_binary(data)
            slength = struct.unpack('<i', data.red(1))
            self.SessionName = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.ClientDescription = ApplicationDescription.from_binary(data)
            slength = struct.unpack('<i', data.red(1))
            self.ServerUri = struct.unpack('<{}s'.format(slength), data.read(slength))
            slength = struct.unpack('<i', data.red(1))
            self.EndpointUrl = struct.unpack('<{}s'.format(slength), data.read(slength))
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    slength = struct.unpack('<i', data.red(1))
                    self.LocaleIds = struct.unpack('<{}s'.format(slength), data.read(slength))
            fmt = '<d'
            fmt_size = ActualSessionTimeout
            self.ActualSessionTimeout = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = MaxResponseMessageSize
            self.MaxResponseMessageSize = struct.unpack(fmt, data.read(fmt_size))[0]
            self.ClientConnectionTime = DateTime.from_binary(data)
            self.ClientLastContactTime = DateTime.from_binary(data)
            fmt = '<I'
            fmt_size = CurrentSubscriptionsCount
            self.CurrentSubscriptionsCount = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = CurrentMonitoredItemsCount
            self.CurrentMonitoredItemsCount = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = CurrentPublishRequestsInQueue
            self.CurrentPublishRequestsInQueue = struct.unpack(fmt, data.read(fmt_size))[0]
            self.TotalRequestCount = ServiceCounterDataType.from_binary(data)
            fmt = '<I'
            fmt_size = UnauthorizedRequestCount
            self.UnauthorizedRequestCount = struct.unpack(fmt, data.read(fmt_size))[0]
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
            return data
            
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
        def from_binary(self, data):
            self.SessionId = NodeId.from_binary(data)
            slength = struct.unpack('<i', data.red(1))
            self.ClientUserIdOfSession = struct.unpack('<{}s'.format(slength), data.read(slength))
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    slength = struct.unpack('<i', data.red(1))
                    self.ClientUserIdHistory = struct.unpack('<{}s'.format(slength), data.read(slength))
            slength = struct.unpack('<i', data.red(1))
            self.AuthenticationMechanism = struct.unpack('<{}s'.format(slength), data.read(slength))
            slength = struct.unpack('<i', data.red(1))
            self.Encoding = struct.unpack('<{}s'.format(slength), data.read(slength))
            slength = struct.unpack('<i', data.red(1))
            self.TransportProtocol = struct.unpack('<{}s'.format(slength), data.read(slength))
            fmt = '<I'
            fmt_size = SecurityMode
            self.SecurityMode = struct.unpack(fmt, data.read(fmt_size))[0]
            slength = struct.unpack('<i', data.red(1))
            self.SecurityPolicyUri = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.ClientCertificate = ByteString.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            fmt = '<I'
            fmt_size = TotalCount
            self.TotalCount = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = ErrorCount
            self.ErrorCount = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            self.StatusCode = StatusCode.from_binary(data)
            self.DiagnosticInfo = DiagnosticInfo.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            self.SessionId = NodeId.from_binary(data)
            fmt = '<I'
            fmt_size = SubscriptionId
            self.SubscriptionId = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<B'
            fmt_size = Priority
            self.Priority = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<d'
            fmt_size = PublishingInterval
            self.PublishingInterval = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = MaxKeepAliveCount
            self.MaxKeepAliveCount = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = MaxLifetimeCount
            self.MaxLifetimeCount = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = MaxNotificationsPerPublish
            self.MaxNotificationsPerPublish = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<?'
            fmt_size = PublishingEnabled
            self.PublishingEnabled = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = ModifyCount
            self.ModifyCount = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = EnableCount
            self.EnableCount = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = DisableCount
            self.DisableCount = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = RepublishRequestCount
            self.RepublishRequestCount = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = RepublishMessageRequestCount
            self.RepublishMessageRequestCount = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = RepublishMessageCount
            self.RepublishMessageCount = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = TransferRequestCount
            self.TransferRequestCount = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = TransferredToAltClientCount
            self.TransferredToAltClientCount = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = TransferredToSameClientCount
            self.TransferredToSameClientCount = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = PublishRequestCount
            self.PublishRequestCount = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = DataChangeNotificationsCount
            self.DataChangeNotificationsCount = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = EventNotificationsCount
            self.EventNotificationsCount = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = NotificationsCount
            self.NotificationsCount = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = LatePublishRequestCount
            self.LatePublishRequestCount = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = CurrentKeepAliveCount
            self.CurrentKeepAliveCount = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = CurrentLifetimeCount
            self.CurrentLifetimeCount = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = UnacknowledgedMessageCount
            self.UnacknowledgedMessageCount = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = DiscardedMessageCount
            self.DiscardedMessageCount = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = MonitoredItemCount
            self.MonitoredItemCount = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = DisabledMonitoredItemCount
            self.DisabledMonitoredItemCount = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = MonitoringQueueOverflowCount
            self.MonitoringQueueOverflowCount = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = NextSequenceNumber
            self.NextSequenceNumber = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<I'
            fmt_size = EventQueueOverFlowCount
            self.EventQueueOverFlowCount = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            self.Affected = NodeId.from_binary(data)
            self.AffectedType = NodeId.from_binary(data)
            fmt = '<B'
            fmt_size = Verb
            self.Verb = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            self.Affected = NodeId.from_binary(data)
            self.AffectedType = NodeId.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            fmt = '<d'
            fmt_size = Low
            self.Low = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<d'
            fmt_size = High
            self.High = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            slength = struct.unpack('<i', data.red(1))
            self.NamespaceUri = struct.unpack('<{}s'.format(slength), data.read(slength))
            fmt = '<i'
            fmt_size = UnitId
            self.UnitId = struct.unpack(fmt, data.read(fmt_size))[0]
            self.DisplayName = LocalizedText.from_binary(data)
            self.Description = LocalizedText.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            fmt = '<f'
            fmt_size = Real
            self.Real = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<f'
            fmt_size = Imaginary
            self.Imaginary = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            fmt = '<d'
            fmt_size = Real
            self.Real = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<d'
            fmt_size = Imaginary
            self.Imaginary = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            self.EngineeringUnits = EUInformation.from_binary(data)
            self.EURange = Range.from_binary(data)
            self.Title = LocalizedText.from_binary(data)
            fmt = '<I'
            fmt_size = AxisScaleType
            self.AxisScaleType = struct.unpack(fmt, data.read(fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    fmt = '<d'
                    fmt_size = AxisSteps
                    self.AxisSteps = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            fmt = '<d'
            fmt_size = X
            self.X = struct.unpack(fmt, data.read(fmt_size))[0]
            fmt = '<f'
            fmt_size = Value
            self.Value = struct.unpack(fmt, data.read(fmt_size))[0]
            return data
            
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
        def from_binary(self, data):
            self.CreateSessionId = NodeId.from_binary(data)
            slength = struct.unpack('<i', data.red(1))
            self.CreateClientName = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.InvocationCreationTime = DateTime.from_binary(data)
            self.LastTransitionTime = DateTime.from_binary(data)
            slength = struct.unpack('<i', data.red(1))
            self.LastMethodCall = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.LastMethodSessionId = NodeId.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.LastMethodInputArguments = Argument.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.LastMethodOutputArguments = Argument.from_binary(data)
            self.LastMethodCallTime = DateTime.from_binary(data)
            self.LastMethodReturnStatus = StatusResult.from_binary(data)
            return data
            
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
        def from_binary(self, data):
            slength = struct.unpack('<i', data.red(1))
            self.Message = struct.unpack('<{}s'.format(slength), data.read(slength))
            slength = struct.unpack('<i', data.red(1))
            self.UserName = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.AnnotationTime = DateTime.from_binary(data)
            return data
