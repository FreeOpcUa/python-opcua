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

class XmlElement(object):
    def __init__(self):
        self.Length = 0
        self._Length_fmt = '<i'
        self._Length_fmt_size = 4
        self.Value = []
        self._Value_fmt = '<s'
        self._Value_fmt_size = 1
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack(self._Length_fmt, self.Length))
        tmp.append(struct.pack('<i', len(self.Value)))
        for i in Value:
            tmp.append(struct.pack(self._Value_fmt, self.Value))
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.Length = struct.unpack(self._Length_fmt, data.read(self._Length_fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.Value = struct.unpack(self._Value_fmt, data.read(self._Value_fmt_size))[0]
            return data
            
class TwoByteNodeId(object):
    def __init__(self):
        self.Identifier = 0
        self._Identifier_fmt = '<B'
        self._Identifier_fmt_size = 1
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack(self._Identifier_fmt, self.Identifier))
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.Identifier = struct.unpack(self._Identifier_fmt, data.read(self._Identifier_fmt_size))[0]
            return data
            
class FourByteNodeId(object):
    def __init__(self):
        self.NamespaceIndex = 0
        self._NamespaceIndex_fmt = '<B'
        self._NamespaceIndex_fmt_size = 1
        self.Identifier = 0
        self._Identifier_fmt = '<H'
        self._Identifier_fmt_size = 2
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack(self._NamespaceIndex_fmt, self.NamespaceIndex))
        tmp.append(struct.pack(self._Identifier_fmt, self.Identifier))
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.NamespaceIndex = struct.unpack(self._NamespaceIndex_fmt, data.read(self._NamespaceIndex_fmt_size))[0]
            self.Identifier = struct.unpack(self._Identifier_fmt, data.read(self._Identifier_fmt_size))[0]
            return data
            
class NumericNodeId(object):
    def __init__(self):
        self.NamespaceIndex = 0
        self._NamespaceIndex_fmt = '<H'
        self._NamespaceIndex_fmt_size = 2
        self.Identifier = 0
        self._Identifier_fmt = '<I'
        self._Identifier_fmt_size = 4
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack(self._NamespaceIndex_fmt, self.NamespaceIndex))
        tmp.append(struct.pack(self._Identifier_fmt, self.Identifier))
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.NamespaceIndex = struct.unpack(self._NamespaceIndex_fmt, data.read(self._NamespaceIndex_fmt_size))[0]
            self.Identifier = struct.unpack(self._Identifier_fmt, data.read(self._Identifier_fmt_size))[0]
            return data
            
class StringNodeId(object):
    def __init__(self):
        self.NamespaceIndex = 0
        self._NamespaceIndex_fmt = '<H'
        self._NamespaceIndex_fmt_size = 2
        self.Identifier = b''
        self._Identifier_fmt = '<s'
        self._Identifier_fmt_size = 1
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack(self._NamespaceIndex_fmt, self.NamespaceIndex))
        tmp.append(struct.pack(self._Identifier_fmt, self.Identifier))
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.NamespaceIndex = struct.unpack(self._NamespaceIndex_fmt, data.read(self._NamespaceIndex_fmt_size))[0]
            self.Identifier = struct.unpack(self._Identifier_fmt, data.read(self._Identifier_fmt_size))[0]
            return data
            
class GuidNodeId(object):
    def __init__(self):
        self.NamespaceIndex = 0
        self._NamespaceIndex_fmt = '<H'
        self._NamespaceIndex_fmt_size = 2
        self.Identifier = Guid()
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack(self._NamespaceIndex_fmt, self.NamespaceIndex))
        tmp.append(self.Identifier.to_binary())
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.NamespaceIndex = struct.unpack(self._NamespaceIndex_fmt, data.read(self._NamespaceIndex_fmt_size))[0]
            self.Identifier = Guid.from_binary(data)
            return data
            
class ByteStringNodeId(object):
    def __init__(self):
        self.NamespaceIndex = 0
        self._NamespaceIndex_fmt = '<H'
        self._NamespaceIndex_fmt_size = 2
        self.Identifier = ByteString()
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack(self._NamespaceIndex_fmt, self.NamespaceIndex))
        tmp.append(self.Identifier.to_binary())
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.NamespaceIndex = struct.unpack(self._NamespaceIndex_fmt, data.read(self._NamespaceIndex_fmt_size))[0]
            self.Identifier = ByteString.from_binary(data)
            return data
            
class DiagnosticInfo(object):
    def __init__(self):
        self.Encoding = 0
        self._Encoding_fmt = '<B'
        self._Encoding_fmt_size = 1
        self.SymbolicId = 0
        self._SymbolicId_fmt = '<i'
        self._SymbolicId_fmt_size = 4
        self.NamespaceURI = 0
        self._NamespaceURI_fmt = '<i'
        self._NamespaceURI_fmt_size = 4
        self.LocalizedText = 0
        self._LocalizedText_fmt = '<i'
        self._LocalizedText_fmt_size = 4
        self.AdditionalInfo = b''
        self._AdditionalInfo_fmt = '<s'
        self._AdditionalInfo_fmt_size = 1
        self.InnerStatusCode = StatusCode()
        self.InnerDiagnosticInfo = DiagnosticInfo()
    
    def to_binary(self):
        packet = []
        tmp = packet
        if self.SymbolicId: self.Encoding |= (value << 0)
        if self.NamespaceURI: self.Encoding |= (value << 1)
        if self.LocalizedText: self.Encoding |= (value << 2)
        if self.AdditionalInfo: self.Encoding |= (value << 4)
        if self.InnerStatusCode: self.Encoding |= (value << 5)
        if self.InnerDiagnosticInfo: self.Encoding |= (value << 6)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.SymbolicId: 
            tmp.append(struct.pack(self._SymbolicId_fmt, self.SymbolicId))
        if self.NamespaceURI: 
            tmp.append(struct.pack(self._NamespaceURI_fmt, self.NamespaceURI))
        if self.LocalizedText: 
            tmp.append(struct.pack(self._LocalizedText_fmt, self.LocalizedText))
        if self.AdditionalInfo: 
            tmp.append(struct.pack(self._AdditionalInfo_fmt, self.AdditionalInfo))
        if self.InnerStatusCode: 
            tmp.append(self.InnerStatusCode.to_binary())
        if self.InnerDiagnosticInfo: 
            tmp.append(self.InnerDiagnosticInfo.to_binary())
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))[0]
            if self.Encoding & (1 << 0):
                self.SymbolicId = struct.unpack(self._SymbolicId_fmt, data.read(self._SymbolicId_fmt_size))[0]
            if self.Encoding & (1 << 1):
                self.NamespaceURI = struct.unpack(self._NamespaceURI_fmt, data.read(self._NamespaceURI_fmt_size))[0]
            if self.Encoding & (1 << 2):
                self.LocalizedText = struct.unpack(self._LocalizedText_fmt, data.read(self._LocalizedText_fmt_size))[0]
            if self.Encoding & (1 << 4):
                self.AdditionalInfo = struct.unpack(self._AdditionalInfo_fmt, data.read(self._AdditionalInfo_fmt_size))[0]
            if self.Encoding & (1 << 5):
                self.InnerStatusCode = StatusCode.from_binary(data)
            if self.Encoding & (1 << 6):
                self.InnerDiagnosticInfo = DiagnosticInfo.from_binary(data)
            return data
            
class QualifiedName(object):
    def __init__(self):
        self.NamespaceIndex = 0
        self._NamespaceIndex_fmt = '<i'
        self._NamespaceIndex_fmt_size = 4
        self.Name = b''
        self._Name_fmt = '<s'
        self._Name_fmt_size = 1
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack(self._NamespaceIndex_fmt, self.NamespaceIndex))
        tmp.append(struct.pack(self._Name_fmt, self.Name))
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.NamespaceIndex = struct.unpack(self._NamespaceIndex_fmt, data.read(self._NamespaceIndex_fmt_size))[0]
            self.Name = struct.unpack(self._Name_fmt, data.read(self._Name_fmt_size))[0]
            return data
            
class LocalizedText(object):
    def __init__(self):
        self.Encoding = 0
        self._Encoding_fmt = '<B'
        self._Encoding_fmt_size = 1
        self.Locale = b''
        self._Locale_fmt = '<s'
        self._Locale_fmt_size = 1
        self.Text = b''
        self._Text_fmt = '<s'
        self._Text_fmt_size = 1
    
    def to_binary(self):
        packet = []
        tmp = packet
        if self.Locale: self.Encoding |= (value << 0)
        if self.Text: self.Encoding |= (value << 1)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.Locale: 
            tmp.append(struct.pack(self._Locale_fmt, self.Locale))
        if self.Text: 
            tmp.append(struct.pack(self._Text_fmt, self.Text))
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))[0]
            if self.Encoding & (1 << 0):
                self.Locale = struct.unpack(self._Locale_fmt, data.read(self._Locale_fmt_size))[0]
            if self.Encoding & (1 << 1):
                self.Text = struct.unpack(self._Text_fmt, data.read(self._Text_fmt_size))[0]
            return data
            
class DataValue(object):
    def __init__(self):
        self.Encoding = 0
        self._Encoding_fmt = '<B'
        self._Encoding_fmt_size = 1
        self.Value = Variant()
        self.StatusCode = StatusCode()
        self.SourceTimestamp = 0
        self.SourcePicoseconds = 0
        self._SourcePicoseconds_fmt = '<H'
        self._SourcePicoseconds_fmt_size = 2
        self.ServerTimestamp = 0
        self.ServerPicoseconds = 0
        self._ServerPicoseconds_fmt = '<H'
        self._ServerPicoseconds_fmt_size = 2
    
    def to_binary(self):
        packet = []
        tmp = packet
        if self.Value: self.Encoding |= (value << 0)
        if self.StatusCode: self.Encoding |= (value << 1)
        if self.SourceTimestamp: self.Encoding |= (value << 2)
        if self.SourcePicoseconds: self.Encoding |= (value << 3)
        if self.ServerTimestamp: self.Encoding |= (value << 4)
        if self.ServerPicoseconds: self.Encoding |= (value << 5)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.Value: 
            tmp.append(self.Value.to_binary())
        if self.StatusCode: 
            tmp.append(self.StatusCode.to_binary())
        if self.SourceTimestamp: 
            tmp.append(self.SourceTimestamp.to_binary())
        if self.SourcePicoseconds: 
            tmp.append(struct.pack(self._SourcePicoseconds_fmt, self.SourcePicoseconds))
        if self.ServerTimestamp: 
            tmp.append(self.ServerTimestamp.to_binary())
        if self.ServerPicoseconds: 
            tmp.append(struct.pack(self._ServerPicoseconds_fmt, self.ServerPicoseconds))
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))[0]
            if self.Encoding & (1 << 0):
                self.Value = Variant.from_binary(data)
            if self.Encoding & (1 << 1):
                self.StatusCode = StatusCode.from_binary(data)
            if self.Encoding & (1 << 2):
                self.SourceTimestamp = DateTime.from_binary(data)
            if self.Encoding & (1 << 3):
                self.SourcePicoseconds = struct.unpack(self._SourcePicoseconds_fmt, data.read(self._SourcePicoseconds_fmt_size))[0]
            if self.Encoding & (1 << 4):
                self.ServerTimestamp = DateTime.from_binary(data)
            if self.Encoding & (1 << 5):
                self.ServerPicoseconds = struct.unpack(self._ServerPicoseconds_fmt, data.read(self._ServerPicoseconds_fmt_size))[0]
            return data
            
class ExtensionObject(object):
    def __init__(self):
        self.Encoding = 0
        self._Encoding_fmt = '<B'
        self._Encoding_fmt_size = 1
        self.TypeId = ExpandedNodeId()
        self.Body = []
        self._Body_fmt = '<B'
        self._Body_fmt_size = 1
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        tmp.append(self.TypeId.to_binary())
        tmp = packet
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))[0]
            self.TypeId = ExpandedNodeId.from_binary(data)
            bodylength = struct.unpack('<i', data.read(4))[0]
            return data
            
class Variant(object):
    def __init__(self):
        self.Encoding = 0
        self._Encoding_fmt = '<B'
        self._Encoding_fmt_size = 1
        self.ArrayLength = 0
        self._ArrayLength_fmt = '<i'
        self._ArrayLength_fmt_size = 4
        self.Boolean = []
        self._Boolean_fmt = '<?'
        self._Boolean_fmt_size = 1
        self.SByte = []
        self._SByte_fmt = '<B'
        self._SByte_fmt_size = 1
        self.Byte = []
        self._Byte_fmt = '<B'
        self._Byte_fmt_size = 1
        self.Int16 = []
        self._Int16_fmt = '<h'
        self._Int16_fmt_size = 2
        self.UInt16 = []
        self._UInt16_fmt = '<H'
        self._UInt16_fmt_size = 2
        self.Int32 = []
        self._Int32_fmt = '<i'
        self._Int32_fmt_size = 4
        self.UInt32 = []
        self._UInt32_fmt = '<I'
        self._UInt32_fmt_size = 4
        self.Int64 = []
        self._Int64_fmt = '<q'
        self._Int64_fmt_size = 8
        self.UInt64 = []
        self._UInt64_fmt = '<Q'
        self._UInt64_fmt_size = 8
        self.Float = []
        self._Float_fmt = '<f'
        self._Float_fmt_size = 4
        self.Double = []
        self._Double_fmt = '<d'
        self._Double_fmt_size = 8
        self.String = []
        self._String_fmt = '<s'
        self._String_fmt_size = 1
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
        tmp = packet
        if self.ArrayLength: self.Encoding |= (value << 7)
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
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.ArrayLength: 
            tmp.append(struct.pack(self._ArrayLength_fmt, self.ArrayLength))
        if self.Boolean: 
            tmp.append(struct.pack('<i', len(self.Boolean)))
            for i in Boolean:
                tmp.append(struct.pack(self._Boolean_fmt, self.Boolean))
        if self.SByte: 
            tmp.append(struct.pack('<i', len(self.SByte)))
            for i in SByte:
                tmp.append(struct.pack(self._SByte_fmt, self.SByte))
        if self.Byte: 
            tmp.append(struct.pack('<i', len(self.Byte)))
            for i in Byte:
                tmp.append(struct.pack(self._Byte_fmt, self.Byte))
        if self.Int16: 
            tmp.append(struct.pack('<i', len(self.Int16)))
            for i in Int16:
                tmp.append(struct.pack(self._Int16_fmt, self.Int16))
        if self.UInt16: 
            tmp.append(struct.pack('<i', len(self.UInt16)))
            for i in UInt16:
                tmp.append(struct.pack(self._UInt16_fmt, self.UInt16))
        if self.Int32: 
            tmp.append(struct.pack('<i', len(self.Int32)))
            for i in Int32:
                tmp.append(struct.pack(self._Int32_fmt, self.Int32))
        if self.UInt32: 
            tmp.append(struct.pack('<i', len(self.UInt32)))
            for i in UInt32:
                tmp.append(struct.pack(self._UInt32_fmt, self.UInt32))
        if self.Int64: 
            tmp.append(struct.pack('<i', len(self.Int64)))
            for i in Int64:
                tmp.append(struct.pack(self._Int64_fmt, self.Int64))
        if self.UInt64: 
            tmp.append(struct.pack('<i', len(self.UInt64)))
            for i in UInt64:
                tmp.append(struct.pack(self._UInt64_fmt, self.UInt64))
        if self.Float: 
            tmp.append(struct.pack('<i', len(self.Float)))
            for i in Float:
                tmp.append(struct.pack(self._Float_fmt, self.Float))
        if self.Double: 
            tmp.append(struct.pack('<i', len(self.Double)))
            for i in Double:
                tmp.append(struct.pack(self._Double_fmt, self.Double))
        if self.String: 
            tmp.append(struct.pack('<i', len(self.String)))
            for i in String:
                tmp.append(struct.pack('<i', len(self.String)))
                tmp.append(struct.pack('<{}s'.format(len(self.String)), self.String.encode()))
        if self.DateTime: 
            tmp.append(struct.pack('<i', len(self.DateTime)))
            for i in DateTime:
                tmp.append(self.DateTime.to_binary())
        if self.Guid: 
            tmp.append(struct.pack('<i', len(self.Guid)))
            for i in Guid:
                tmp.append(self.Guid.to_binary())
        if self.ByteString: 
            tmp.append(struct.pack('<i', len(self.ByteString)))
            for i in ByteString:
                tmp.append(self.ByteString.to_binary())
        if self.XmlElement: 
            tmp.append(struct.pack('<i', len(self.XmlElement)))
            for i in XmlElement:
                tmp.append(self.XmlElement.to_binary())
        if self.NodeId: 
            tmp.append(struct.pack('<i', len(self.NodeId)))
            for i in NodeId:
                tmp.append(self.NodeId.to_binary())
        if self.ExpandedNodeId: 
            tmp.append(struct.pack('<i', len(self.ExpandedNodeId)))
            for i in ExpandedNodeId:
                tmp.append(self.ExpandedNodeId.to_binary())
        if self.StatusCode: 
            tmp.append(struct.pack('<i', len(self.StatusCode)))
            for i in StatusCode:
                tmp.append(self.StatusCode.to_binary())
        if self.DiagnosticInfo: 
            tmp.append(struct.pack('<i', len(self.DiagnosticInfo)))
            for i in DiagnosticInfo:
                tmp.append(self.DiagnosticInfo.to_binary())
        if self.QualifiedName: 
            tmp.append(struct.pack('<i', len(self.QualifiedName)))
            for i in QualifiedName:
                tmp.append(self.QualifiedName.to_binary())
        if self.LocalizedText: 
            tmp.append(struct.pack('<i', len(self.LocalizedText)))
            for i in LocalizedText:
                tmp.append(self.LocalizedText.to_binary())
        if self.ExtensionObject: 
            tmp.append(struct.pack('<i', len(self.ExtensionObject)))
            for i in ExtensionObject:
                tmp.append(self.ExtensionObject.to_binary())
        if self.DataValue: 
            tmp.append(struct.pack('<i', len(self.DataValue)))
            for i in DataValue:
                tmp.append(self.DataValue.to_binary())
        if self.Variant: 
            tmp.append(struct.pack('<i', len(self.Variant)))
            for i in Variant:
                tmp.append(self.Variant.to_binary())
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))[0]
            if self.Encoding & (1 << 7):
                self.ArrayLength = struct.unpack(self._ArrayLength_fmt, data.read(self._ArrayLength_fmt_size))[0]
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('<i', data.read(4))[0]
                if length <= -1:
                    for i in range(0, length):
                        self.Boolean = struct.unpack(self._Boolean_fmt, data.read(self._Boolean_fmt_size))[0]
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('<i', data.read(4))[0]
                if length <= -1:
                    for i in range(0, length):
                        self.SByte = struct.unpack(self._SByte_fmt, data.read(self._SByte_fmt_size))[0]
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('<i', data.read(4))[0]
                if length <= -1:
                    for i in range(0, length):
                        self.Byte = struct.unpack(self._Byte_fmt, data.read(self._Byte_fmt_size))[0]
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('<i', data.read(4))[0]
                if length <= -1:
                    for i in range(0, length):
                        self.Int16 = struct.unpack(self._Int16_fmt, data.read(self._Int16_fmt_size))[0]
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('<i', data.read(4))[0]
                if length <= -1:
                    for i in range(0, length):
                        self.UInt16 = struct.unpack(self._UInt16_fmt, data.read(self._UInt16_fmt_size))[0]
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('<i', data.read(4))[0]
                if length <= -1:
                    for i in range(0, length):
                        self.Int32 = struct.unpack(self._Int32_fmt, data.read(self._Int32_fmt_size))[0]
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('<i', data.read(4))[0]
                if length <= -1:
                    for i in range(0, length):
                        self.UInt32 = struct.unpack(self._UInt32_fmt, data.read(self._UInt32_fmt_size))[0]
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('<i', data.read(4))[0]
                if length <= -1:
                    for i in range(0, length):
                        self.Int64 = struct.unpack(self._Int64_fmt, data.read(self._Int64_fmt_size))[0]
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('<i', data.read(4))[0]
                if length <= -1:
                    for i in range(0, length):
                        self.UInt64 = struct.unpack(self._UInt64_fmt, data.read(self._UInt64_fmt_size))[0]
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('<i', data.read(4))[0]
                if length <= -1:
                    for i in range(0, length):
                        self.Float = struct.unpack(self._Float_fmt, data.read(self._Float_fmt_size))[0]
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('<i', data.read(4))[0]
                if length <= -1:
                    for i in range(0, length):
                        self.Double = struct.unpack(self._Double_fmt, data.read(self._Double_fmt_size))[0]
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('<i', data.read(4))[0]
                if length <= -1:
                    for i in range(0, length):
                        slength = struct.unpack('<i', data.red(1))
                        self.String = struct.unpack('<{}s'.format(slength), data.read(slength))
                        self.String = struct.unpack(self._String_fmt, data.read(self._String_fmt_size))[0]
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
        self.TypeId = ExpandedNodeId()
        self.NodeId = NodeId()
        self.NodeClass = 0
        self._NodeClass_fmt = '<I'
        self._NodeClass_fmt_size = 4
        self.BrowseName = QualifiedName()
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self._WriteMask_fmt = '<I'
        self._WriteMask_fmt_size = 4
        self.UserWriteMask = 0
        self._UserWriteMask_fmt = '<I'
        self._UserWriteMask_fmt_size = 4
        self.References = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.NodeId.to_binary())
        tmp.append(struct.pack(self._NodeClass_fmt, self.NodeClass))
        tmp.append(self.BrowseName.to_binary())
        tmp.append(self.DisplayName.to_binary())
        tmp.append(self.Description.to_binary())
        tmp.append(struct.pack(self._WriteMask_fmt, self.WriteMask))
        tmp.append(struct.pack(self._UserWriteMask_fmt, self.UserWriteMask))
        tmp.append(struct.pack('<i', len(self.References)))
        for i in References:
            tmp.append(self.References.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.NodeId = NodeId.from_binary(data)
            self.NodeClass = struct.unpack(self._NodeClass_fmt, data.read(self._NodeClass_fmt_size))[0]
            self.BrowseName = QualifiedName.from_binary(data)
            self.DisplayName = LocalizedText.from_binary(data)
            self.Description = LocalizedText.from_binary(data)
            self.WriteMask = struct.unpack(self._WriteMask_fmt, data.read(self._WriteMask_fmt_size))[0]
            self.UserWriteMask = struct.unpack(self._UserWriteMask_fmt, data.read(self._UserWriteMask_fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.References = ReferenceNode.from_binary(data)
            return data
            
class InstanceNode(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.NodeId = NodeId()
        self.NodeClass = 0
        self._NodeClass_fmt = '<I'
        self._NodeClass_fmt_size = 4
        self.BrowseName = QualifiedName()
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self._WriteMask_fmt = '<I'
        self._WriteMask_fmt_size = 4
        self.UserWriteMask = 0
        self._UserWriteMask_fmt = '<I'
        self._UserWriteMask_fmt_size = 4
        self.References = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.NodeId.to_binary())
        tmp.append(struct.pack(self._NodeClass_fmt, self.NodeClass))
        tmp.append(self.BrowseName.to_binary())
        tmp.append(self.DisplayName.to_binary())
        tmp.append(self.Description.to_binary())
        tmp.append(struct.pack(self._WriteMask_fmt, self.WriteMask))
        tmp.append(struct.pack(self._UserWriteMask_fmt, self.UserWriteMask))
        tmp.append(struct.pack('<i', len(self.References)))
        for i in References:
            tmp.append(self.References.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.NodeId = NodeId.from_binary(data)
            self.NodeClass = struct.unpack(self._NodeClass_fmt, data.read(self._NodeClass_fmt_size))[0]
            self.BrowseName = QualifiedName.from_binary(data)
            self.DisplayName = LocalizedText.from_binary(data)
            self.Description = LocalizedText.from_binary(data)
            self.WriteMask = struct.unpack(self._WriteMask_fmt, data.read(self._WriteMask_fmt_size))[0]
            self.UserWriteMask = struct.unpack(self._UserWriteMask_fmt, data.read(self._UserWriteMask_fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.References = ReferenceNode.from_binary(data)
            return data
            
class TypeNode(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.NodeId = NodeId()
        self.NodeClass = 0
        self._NodeClass_fmt = '<I'
        self._NodeClass_fmt_size = 4
        self.BrowseName = QualifiedName()
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self._WriteMask_fmt = '<I'
        self._WriteMask_fmt_size = 4
        self.UserWriteMask = 0
        self._UserWriteMask_fmt = '<I'
        self._UserWriteMask_fmt_size = 4
        self.References = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.NodeId.to_binary())
        tmp.append(struct.pack(self._NodeClass_fmt, self.NodeClass))
        tmp.append(self.BrowseName.to_binary())
        tmp.append(self.DisplayName.to_binary())
        tmp.append(self.Description.to_binary())
        tmp.append(struct.pack(self._WriteMask_fmt, self.WriteMask))
        tmp.append(struct.pack(self._UserWriteMask_fmt, self.UserWriteMask))
        tmp.append(struct.pack('<i', len(self.References)))
        for i in References:
            tmp.append(self.References.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.NodeId = NodeId.from_binary(data)
            self.NodeClass = struct.unpack(self._NodeClass_fmt, data.read(self._NodeClass_fmt_size))[0]
            self.BrowseName = QualifiedName.from_binary(data)
            self.DisplayName = LocalizedText.from_binary(data)
            self.Description = LocalizedText.from_binary(data)
            self.WriteMask = struct.unpack(self._WriteMask_fmt, data.read(self._WriteMask_fmt_size))[0]
            self.UserWriteMask = struct.unpack(self._UserWriteMask_fmt, data.read(self._UserWriteMask_fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.References = ReferenceNode.from_binary(data)
            return data
            
class ObjectNode(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.NodeId = NodeId()
        self.NodeClass = 0
        self._NodeClass_fmt = '<I'
        self._NodeClass_fmt_size = 4
        self.BrowseName = QualifiedName()
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self._WriteMask_fmt = '<I'
        self._WriteMask_fmt_size = 4
        self.UserWriteMask = 0
        self._UserWriteMask_fmt = '<I'
        self._UserWriteMask_fmt_size = 4
        self.References = []
        self.EventNotifier = 0
        self._EventNotifier_fmt = '<B'
        self._EventNotifier_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.NodeId.to_binary())
        tmp.append(struct.pack(self._NodeClass_fmt, self.NodeClass))
        tmp.append(self.BrowseName.to_binary())
        tmp.append(self.DisplayName.to_binary())
        tmp.append(self.Description.to_binary())
        tmp.append(struct.pack(self._WriteMask_fmt, self.WriteMask))
        tmp.append(struct.pack(self._UserWriteMask_fmt, self.UserWriteMask))
        tmp.append(struct.pack('<i', len(self.References)))
        for i in References:
            tmp.append(self.References.to_binary())
        tmp.append(struct.pack(self._EventNotifier_fmt, self.EventNotifier))
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.NodeId = NodeId.from_binary(data)
            self.NodeClass = struct.unpack(self._NodeClass_fmt, data.read(self._NodeClass_fmt_size))[0]
            self.BrowseName = QualifiedName.from_binary(data)
            self.DisplayName = LocalizedText.from_binary(data)
            self.Description = LocalizedText.from_binary(data)
            self.WriteMask = struct.unpack(self._WriteMask_fmt, data.read(self._WriteMask_fmt_size))[0]
            self.UserWriteMask = struct.unpack(self._UserWriteMask_fmt, data.read(self._UserWriteMask_fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.References = ReferenceNode.from_binary(data)
            self.EventNotifier = struct.unpack(self._EventNotifier_fmt, data.read(self._EventNotifier_fmt_size))[0]
            return data
            
class ObjectTypeNode(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.NodeId = NodeId()
        self.NodeClass = 0
        self._NodeClass_fmt = '<I'
        self._NodeClass_fmt_size = 4
        self.BrowseName = QualifiedName()
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self._WriteMask_fmt = '<I'
        self._WriteMask_fmt_size = 4
        self.UserWriteMask = 0
        self._UserWriteMask_fmt = '<I'
        self._UserWriteMask_fmt_size = 4
        self.References = []
        self.IsAbstract = 0
        self._IsAbstract_fmt = '<?'
        self._IsAbstract_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.NodeId.to_binary())
        tmp.append(struct.pack(self._NodeClass_fmt, self.NodeClass))
        tmp.append(self.BrowseName.to_binary())
        tmp.append(self.DisplayName.to_binary())
        tmp.append(self.Description.to_binary())
        tmp.append(struct.pack(self._WriteMask_fmt, self.WriteMask))
        tmp.append(struct.pack(self._UserWriteMask_fmt, self.UserWriteMask))
        tmp.append(struct.pack('<i', len(self.References)))
        for i in References:
            tmp.append(self.References.to_binary())
        tmp.append(struct.pack(self._IsAbstract_fmt, self.IsAbstract))
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.NodeId = NodeId.from_binary(data)
            self.NodeClass = struct.unpack(self._NodeClass_fmt, data.read(self._NodeClass_fmt_size))[0]
            self.BrowseName = QualifiedName.from_binary(data)
            self.DisplayName = LocalizedText.from_binary(data)
            self.Description = LocalizedText.from_binary(data)
            self.WriteMask = struct.unpack(self._WriteMask_fmt, data.read(self._WriteMask_fmt_size))[0]
            self.UserWriteMask = struct.unpack(self._UserWriteMask_fmt, data.read(self._UserWriteMask_fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.References = ReferenceNode.from_binary(data)
            self.IsAbstract = struct.unpack(self._IsAbstract_fmt, data.read(self._IsAbstract_fmt_size))[0]
            return data
            
class VariableNode(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.NodeId = NodeId()
        self.NodeClass = 0
        self._NodeClass_fmt = '<I'
        self._NodeClass_fmt_size = 4
        self.BrowseName = QualifiedName()
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self._WriteMask_fmt = '<I'
        self._WriteMask_fmt_size = 4
        self.UserWriteMask = 0
        self._UserWriteMask_fmt = '<I'
        self._UserWriteMask_fmt_size = 4
        self.References = []
        self.Value = Variant()
        self.DataType = NodeId()
        self.ValueRank = 0
        self._ValueRank_fmt = '<i'
        self._ValueRank_fmt_size = 4
        self.ArrayDimensions = []
        self._ArrayDimensions_fmt = '<I'
        self._ArrayDimensions_fmt_size = 4
        self.AccessLevel = 0
        self._AccessLevel_fmt = '<B'
        self._AccessLevel_fmt_size = 1
        self.UserAccessLevel = 0
        self._UserAccessLevel_fmt = '<B'
        self._UserAccessLevel_fmt_size = 1
        self.MinimumSamplingInterval = 0
        self._MinimumSamplingInterval_fmt = '<d'
        self._MinimumSamplingInterval_fmt_size = 8
        self.Historizing = 0
        self._Historizing_fmt = '<?'
        self._Historizing_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.NodeId.to_binary())
        tmp.append(struct.pack(self._NodeClass_fmt, self.NodeClass))
        tmp.append(self.BrowseName.to_binary())
        tmp.append(self.DisplayName.to_binary())
        tmp.append(self.Description.to_binary())
        tmp.append(struct.pack(self._WriteMask_fmt, self.WriteMask))
        tmp.append(struct.pack(self._UserWriteMask_fmt, self.UserWriteMask))
        tmp.append(struct.pack('<i', len(self.References)))
        for i in References:
            tmp.append(self.References.to_binary())
        tmp.append(self.Value.to_binary())
        tmp.append(self.DataType.to_binary())
        tmp.append(struct.pack(self._ValueRank_fmt, self.ValueRank))
        tmp.append(struct.pack('<i', len(self.ArrayDimensions)))
        for i in ArrayDimensions:
            tmp.append(struct.pack(self._ArrayDimensions_fmt, self.ArrayDimensions))
        tmp.append(struct.pack(self._AccessLevel_fmt, self.AccessLevel))
        tmp.append(struct.pack(self._UserAccessLevel_fmt, self.UserAccessLevel))
        tmp.append(struct.pack(self._MinimumSamplingInterval_fmt, self.MinimumSamplingInterval))
        tmp.append(struct.pack(self._Historizing_fmt, self.Historizing))
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.NodeId = NodeId.from_binary(data)
            self.NodeClass = struct.unpack(self._NodeClass_fmt, data.read(self._NodeClass_fmt_size))[0]
            self.BrowseName = QualifiedName.from_binary(data)
            self.DisplayName = LocalizedText.from_binary(data)
            self.Description = LocalizedText.from_binary(data)
            self.WriteMask = struct.unpack(self._WriteMask_fmt, data.read(self._WriteMask_fmt_size))[0]
            self.UserWriteMask = struct.unpack(self._UserWriteMask_fmt, data.read(self._UserWriteMask_fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.References = ReferenceNode.from_binary(data)
            self.Value = Variant.from_binary(data)
            self.DataType = NodeId.from_binary(data)
            self.ValueRank = struct.unpack(self._ValueRank_fmt, data.read(self._ValueRank_fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.ArrayDimensions = struct.unpack(self._ArrayDimensions_fmt, data.read(self._ArrayDimensions_fmt_size))[0]
            self.AccessLevel = struct.unpack(self._AccessLevel_fmt, data.read(self._AccessLevel_fmt_size))[0]
            self.UserAccessLevel = struct.unpack(self._UserAccessLevel_fmt, data.read(self._UserAccessLevel_fmt_size))[0]
            self.MinimumSamplingInterval = struct.unpack(self._MinimumSamplingInterval_fmt, data.read(self._MinimumSamplingInterval_fmt_size))[0]
            self.Historizing = struct.unpack(self._Historizing_fmt, data.read(self._Historizing_fmt_size))[0]
            return data
            
class VariableTypeNode(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.NodeId = NodeId()
        self.NodeClass = 0
        self._NodeClass_fmt = '<I'
        self._NodeClass_fmt_size = 4
        self.BrowseName = QualifiedName()
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self._WriteMask_fmt = '<I'
        self._WriteMask_fmt_size = 4
        self.UserWriteMask = 0
        self._UserWriteMask_fmt = '<I'
        self._UserWriteMask_fmt_size = 4
        self.References = []
        self.Value = Variant()
        self.DataType = NodeId()
        self.ValueRank = 0
        self._ValueRank_fmt = '<i'
        self._ValueRank_fmt_size = 4
        self.ArrayDimensions = []
        self._ArrayDimensions_fmt = '<I'
        self._ArrayDimensions_fmt_size = 4
        self.IsAbstract = 0
        self._IsAbstract_fmt = '<?'
        self._IsAbstract_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.NodeId.to_binary())
        tmp.append(struct.pack(self._NodeClass_fmt, self.NodeClass))
        tmp.append(self.BrowseName.to_binary())
        tmp.append(self.DisplayName.to_binary())
        tmp.append(self.Description.to_binary())
        tmp.append(struct.pack(self._WriteMask_fmt, self.WriteMask))
        tmp.append(struct.pack(self._UserWriteMask_fmt, self.UserWriteMask))
        tmp.append(struct.pack('<i', len(self.References)))
        for i in References:
            tmp.append(self.References.to_binary())
        tmp.append(self.Value.to_binary())
        tmp.append(self.DataType.to_binary())
        tmp.append(struct.pack(self._ValueRank_fmt, self.ValueRank))
        tmp.append(struct.pack('<i', len(self.ArrayDimensions)))
        for i in ArrayDimensions:
            tmp.append(struct.pack(self._ArrayDimensions_fmt, self.ArrayDimensions))
        tmp.append(struct.pack(self._IsAbstract_fmt, self.IsAbstract))
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.NodeId = NodeId.from_binary(data)
            self.NodeClass = struct.unpack(self._NodeClass_fmt, data.read(self._NodeClass_fmt_size))[0]
            self.BrowseName = QualifiedName.from_binary(data)
            self.DisplayName = LocalizedText.from_binary(data)
            self.Description = LocalizedText.from_binary(data)
            self.WriteMask = struct.unpack(self._WriteMask_fmt, data.read(self._WriteMask_fmt_size))[0]
            self.UserWriteMask = struct.unpack(self._UserWriteMask_fmt, data.read(self._UserWriteMask_fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.References = ReferenceNode.from_binary(data)
            self.Value = Variant.from_binary(data)
            self.DataType = NodeId.from_binary(data)
            self.ValueRank = struct.unpack(self._ValueRank_fmt, data.read(self._ValueRank_fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.ArrayDimensions = struct.unpack(self._ArrayDimensions_fmt, data.read(self._ArrayDimensions_fmt_size))[0]
            self.IsAbstract = struct.unpack(self._IsAbstract_fmt, data.read(self._IsAbstract_fmt_size))[0]
            return data
            
class ReferenceTypeNode(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.NodeId = NodeId()
        self.NodeClass = 0
        self._NodeClass_fmt = '<I'
        self._NodeClass_fmt_size = 4
        self.BrowseName = QualifiedName()
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self._WriteMask_fmt = '<I'
        self._WriteMask_fmt_size = 4
        self.UserWriteMask = 0
        self._UserWriteMask_fmt = '<I'
        self._UserWriteMask_fmt_size = 4
        self.References = []
        self.IsAbstract = 0
        self._IsAbstract_fmt = '<?'
        self._IsAbstract_fmt_size = 1
        self.Symmetric = 0
        self._Symmetric_fmt = '<?'
        self._Symmetric_fmt_size = 1
        self.InverseName = LocalizedText()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.NodeId.to_binary())
        tmp.append(struct.pack(self._NodeClass_fmt, self.NodeClass))
        tmp.append(self.BrowseName.to_binary())
        tmp.append(self.DisplayName.to_binary())
        tmp.append(self.Description.to_binary())
        tmp.append(struct.pack(self._WriteMask_fmt, self.WriteMask))
        tmp.append(struct.pack(self._UserWriteMask_fmt, self.UserWriteMask))
        tmp.append(struct.pack('<i', len(self.References)))
        for i in References:
            tmp.append(self.References.to_binary())
        tmp.append(struct.pack(self._IsAbstract_fmt, self.IsAbstract))
        tmp.append(struct.pack(self._Symmetric_fmt, self.Symmetric))
        tmp.append(self.InverseName.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.NodeId = NodeId.from_binary(data)
            self.NodeClass = struct.unpack(self._NodeClass_fmt, data.read(self._NodeClass_fmt_size))[0]
            self.BrowseName = QualifiedName.from_binary(data)
            self.DisplayName = LocalizedText.from_binary(data)
            self.Description = LocalizedText.from_binary(data)
            self.WriteMask = struct.unpack(self._WriteMask_fmt, data.read(self._WriteMask_fmt_size))[0]
            self.UserWriteMask = struct.unpack(self._UserWriteMask_fmt, data.read(self._UserWriteMask_fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.References = ReferenceNode.from_binary(data)
            self.IsAbstract = struct.unpack(self._IsAbstract_fmt, data.read(self._IsAbstract_fmt_size))[0]
            self.Symmetric = struct.unpack(self._Symmetric_fmt, data.read(self._Symmetric_fmt_size))[0]
            self.InverseName = LocalizedText.from_binary(data)
            return data
            
class MethodNode(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.NodeId = NodeId()
        self.NodeClass = 0
        self._NodeClass_fmt = '<I'
        self._NodeClass_fmt_size = 4
        self.BrowseName = QualifiedName()
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self._WriteMask_fmt = '<I'
        self._WriteMask_fmt_size = 4
        self.UserWriteMask = 0
        self._UserWriteMask_fmt = '<I'
        self._UserWriteMask_fmt_size = 4
        self.References = []
        self.Executable = 0
        self._Executable_fmt = '<?'
        self._Executable_fmt_size = 1
        self.UserExecutable = 0
        self._UserExecutable_fmt = '<?'
        self._UserExecutable_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.NodeId.to_binary())
        tmp.append(struct.pack(self._NodeClass_fmt, self.NodeClass))
        tmp.append(self.BrowseName.to_binary())
        tmp.append(self.DisplayName.to_binary())
        tmp.append(self.Description.to_binary())
        tmp.append(struct.pack(self._WriteMask_fmt, self.WriteMask))
        tmp.append(struct.pack(self._UserWriteMask_fmt, self.UserWriteMask))
        tmp.append(struct.pack('<i', len(self.References)))
        for i in References:
            tmp.append(self.References.to_binary())
        tmp.append(struct.pack(self._Executable_fmt, self.Executable))
        tmp.append(struct.pack(self._UserExecutable_fmt, self.UserExecutable))
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.NodeId = NodeId.from_binary(data)
            self.NodeClass = struct.unpack(self._NodeClass_fmt, data.read(self._NodeClass_fmt_size))[0]
            self.BrowseName = QualifiedName.from_binary(data)
            self.DisplayName = LocalizedText.from_binary(data)
            self.Description = LocalizedText.from_binary(data)
            self.WriteMask = struct.unpack(self._WriteMask_fmt, data.read(self._WriteMask_fmt_size))[0]
            self.UserWriteMask = struct.unpack(self._UserWriteMask_fmt, data.read(self._UserWriteMask_fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.References = ReferenceNode.from_binary(data)
            self.Executable = struct.unpack(self._Executable_fmt, data.read(self._Executable_fmt_size))[0]
            self.UserExecutable = struct.unpack(self._UserExecutable_fmt, data.read(self._UserExecutable_fmt_size))[0]
            return data
            
class ViewNode(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.NodeId = NodeId()
        self.NodeClass = 0
        self._NodeClass_fmt = '<I'
        self._NodeClass_fmt_size = 4
        self.BrowseName = QualifiedName()
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self._WriteMask_fmt = '<I'
        self._WriteMask_fmt_size = 4
        self.UserWriteMask = 0
        self._UserWriteMask_fmt = '<I'
        self._UserWriteMask_fmt_size = 4
        self.References = []
        self.ContainsNoLoops = 0
        self._ContainsNoLoops_fmt = '<?'
        self._ContainsNoLoops_fmt_size = 1
        self.EventNotifier = 0
        self._EventNotifier_fmt = '<B'
        self._EventNotifier_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.NodeId.to_binary())
        tmp.append(struct.pack(self._NodeClass_fmt, self.NodeClass))
        tmp.append(self.BrowseName.to_binary())
        tmp.append(self.DisplayName.to_binary())
        tmp.append(self.Description.to_binary())
        tmp.append(struct.pack(self._WriteMask_fmt, self.WriteMask))
        tmp.append(struct.pack(self._UserWriteMask_fmt, self.UserWriteMask))
        tmp.append(struct.pack('<i', len(self.References)))
        for i in References:
            tmp.append(self.References.to_binary())
        tmp.append(struct.pack(self._ContainsNoLoops_fmt, self.ContainsNoLoops))
        tmp.append(struct.pack(self._EventNotifier_fmt, self.EventNotifier))
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.NodeId = NodeId.from_binary(data)
            self.NodeClass = struct.unpack(self._NodeClass_fmt, data.read(self._NodeClass_fmt_size))[0]
            self.BrowseName = QualifiedName.from_binary(data)
            self.DisplayName = LocalizedText.from_binary(data)
            self.Description = LocalizedText.from_binary(data)
            self.WriteMask = struct.unpack(self._WriteMask_fmt, data.read(self._WriteMask_fmt_size))[0]
            self.UserWriteMask = struct.unpack(self._UserWriteMask_fmt, data.read(self._UserWriteMask_fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.References = ReferenceNode.from_binary(data)
            self.ContainsNoLoops = struct.unpack(self._ContainsNoLoops_fmt, data.read(self._ContainsNoLoops_fmt_size))[0]
            self.EventNotifier = struct.unpack(self._EventNotifier_fmt, data.read(self._EventNotifier_fmt_size))[0]
            return data
            
class DataTypeNode(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.NodeId = NodeId()
        self.NodeClass = 0
        self._NodeClass_fmt = '<I'
        self._NodeClass_fmt_size = 4
        self.BrowseName = QualifiedName()
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self._WriteMask_fmt = '<I'
        self._WriteMask_fmt_size = 4
        self.UserWriteMask = 0
        self._UserWriteMask_fmt = '<I'
        self._UserWriteMask_fmt_size = 4
        self.References = []
        self.IsAbstract = 0
        self._IsAbstract_fmt = '<?'
        self._IsAbstract_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.NodeId.to_binary())
        tmp.append(struct.pack(self._NodeClass_fmt, self.NodeClass))
        tmp.append(self.BrowseName.to_binary())
        tmp.append(self.DisplayName.to_binary())
        tmp.append(self.Description.to_binary())
        tmp.append(struct.pack(self._WriteMask_fmt, self.WriteMask))
        tmp.append(struct.pack(self._UserWriteMask_fmt, self.UserWriteMask))
        tmp.append(struct.pack('<i', len(self.References)))
        for i in References:
            tmp.append(self.References.to_binary())
        tmp.append(struct.pack(self._IsAbstract_fmt, self.IsAbstract))
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.NodeId = NodeId.from_binary(data)
            self.NodeClass = struct.unpack(self._NodeClass_fmt, data.read(self._NodeClass_fmt_size))[0]
            self.BrowseName = QualifiedName.from_binary(data)
            self.DisplayName = LocalizedText.from_binary(data)
            self.Description = LocalizedText.from_binary(data)
            self.WriteMask = struct.unpack(self._WriteMask_fmt, data.read(self._WriteMask_fmt_size))[0]
            self.UserWriteMask = struct.unpack(self._UserWriteMask_fmt, data.read(self._UserWriteMask_fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.References = ReferenceNode.from_binary(data)
            self.IsAbstract = struct.unpack(self._IsAbstract_fmt, data.read(self._IsAbstract_fmt_size))[0]
            return data
            
class ReferenceNode(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.ReferenceTypeId = NodeId()
        self.IsInverse = 0
        self._IsInverse_fmt = '<?'
        self._IsInverse_fmt_size = 1
        self.TargetId = ExpandedNodeId()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.ReferenceTypeId.to_binary())
        tmp.append(struct.pack(self._IsInverse_fmt, self.IsInverse))
        tmp.append(self.TargetId.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.ReferenceTypeId = NodeId.from_binary(data)
            self.IsInverse = struct.unpack(self._IsInverse_fmt, data.read(self._IsInverse_fmt_size))[0]
            self.TargetId = ExpandedNodeId.from_binary(data)
            return data
            
class Argument(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.Name = ''
        self._Name_fmt = '<s'
        self._Name_fmt_size = 1
        self.DataType = NodeId()
        self.ValueRank = 0
        self._ValueRank_fmt = '<i'
        self._ValueRank_fmt_size = 4
        self.ArrayDimensions = []
        self._ArrayDimensions_fmt = '<I'
        self._ArrayDimensions_fmt_size = 4
        self.Description = LocalizedText()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack('<i', len(self.Name)))
        tmp.append(struct.pack('<{}s'.format(len(self.Name)), self.Name.encode()))
        tmp.append(self.DataType.to_binary())
        tmp.append(struct.pack(self._ValueRank_fmt, self.ValueRank))
        tmp.append(struct.pack('<i', len(self.ArrayDimensions)))
        for i in ArrayDimensions:
            tmp.append(struct.pack(self._ArrayDimensions_fmt, self.ArrayDimensions))
        tmp.append(self.Description.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            slength = struct.unpack('<i', data.red(1))
            self.Name = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.Name = struct.unpack(self._Name_fmt, data.read(self._Name_fmt_size))[0]
            self.DataType = NodeId.from_binary(data)
            self.ValueRank = struct.unpack(self._ValueRank_fmt, data.read(self._ValueRank_fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.ArrayDimensions = struct.unpack(self._ArrayDimensions_fmt, data.read(self._ArrayDimensions_fmt_size))[0]
            self.Description = LocalizedText.from_binary(data)
            return data
            
class EnumValueType(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.Value = 0
        self._Value_fmt = '<q'
        self._Value_fmt_size = 8
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack(self._Value_fmt, self.Value))
        tmp.append(self.DisplayName.to_binary())
        tmp.append(self.Description.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.Value = struct.unpack(self._Value_fmt, data.read(self._Value_fmt_size))[0]
            self.DisplayName = LocalizedText.from_binary(data)
            self.Description = LocalizedText.from_binary(data)
            return data
            
class TimeZoneDataType(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.Offset = 0
        self._Offset_fmt = '<h'
        self._Offset_fmt_size = 2
        self.DaylightSavingInOffset = 0
        self._DaylightSavingInOffset_fmt = '<?'
        self._DaylightSavingInOffset_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack(self._Offset_fmt, self.Offset))
        tmp.append(struct.pack(self._DaylightSavingInOffset_fmt, self.DaylightSavingInOffset))
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.Offset = struct.unpack(self._Offset_fmt, data.read(self._Offset_fmt_size))[0]
            self.DaylightSavingInOffset = struct.unpack(self._DaylightSavingInOffset_fmt, data.read(self._DaylightSavingInOffset_fmt_size))[0]
            return data
            
class ApplicationDescription(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.ApplicationUri = ''
        self._ApplicationUri_fmt = '<s'
        self._ApplicationUri_fmt_size = 1
        self.ProductUri = ''
        self._ProductUri_fmt = '<s'
        self._ProductUri_fmt_size = 1
        self.ApplicationName = LocalizedText()
        self.ApplicationType = 0
        self._ApplicationType_fmt = '<I'
        self._ApplicationType_fmt_size = 4
        self.GatewayServerUri = ''
        self._GatewayServerUri_fmt = '<s'
        self._GatewayServerUri_fmt_size = 1
        self.DiscoveryProfileUri = ''
        self._DiscoveryProfileUri_fmt = '<s'
        self._DiscoveryProfileUri_fmt_size = 1
        self.DiscoveryUrls = []
        self._DiscoveryUrls_fmt = '<s'
        self._DiscoveryUrls_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack('<i', len(self.ApplicationUri)))
        tmp.append(struct.pack('<{}s'.format(len(self.ApplicationUri)), self.ApplicationUri.encode()))
        tmp.append(struct.pack('<i', len(self.ProductUri)))
        tmp.append(struct.pack('<{}s'.format(len(self.ProductUri)), self.ProductUri.encode()))
        tmp.append(self.ApplicationName.to_binary())
        tmp.append(struct.pack(self._ApplicationType_fmt, self.ApplicationType))
        tmp.append(struct.pack('<i', len(self.GatewayServerUri)))
        tmp.append(struct.pack('<{}s'.format(len(self.GatewayServerUri)), self.GatewayServerUri.encode()))
        tmp.append(struct.pack('<i', len(self.DiscoveryProfileUri)))
        tmp.append(struct.pack('<{}s'.format(len(self.DiscoveryProfileUri)), self.DiscoveryProfileUri.encode()))
        tmp.append(struct.pack('<i', len(self.DiscoveryUrls)))
        for i in DiscoveryUrls:
            tmp.append(struct.pack('<i', len(self.DiscoveryUrls)))
            tmp.append(struct.pack('<{}s'.format(len(self.DiscoveryUrls)), self.DiscoveryUrls.encode()))
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            slength = struct.unpack('<i', data.red(1))
            self.ApplicationUri = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.ApplicationUri = struct.unpack(self._ApplicationUri_fmt, data.read(self._ApplicationUri_fmt_size))[0]
            slength = struct.unpack('<i', data.red(1))
            self.ProductUri = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.ProductUri = struct.unpack(self._ProductUri_fmt, data.read(self._ProductUri_fmt_size))[0]
            self.ApplicationName = LocalizedText.from_binary(data)
            self.ApplicationType = struct.unpack(self._ApplicationType_fmt, data.read(self._ApplicationType_fmt_size))[0]
            slength = struct.unpack('<i', data.red(1))
            self.GatewayServerUri = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.GatewayServerUri = struct.unpack(self._GatewayServerUri_fmt, data.read(self._GatewayServerUri_fmt_size))[0]
            slength = struct.unpack('<i', data.red(1))
            self.DiscoveryProfileUri = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.DiscoveryProfileUri = struct.unpack(self._DiscoveryProfileUri_fmt, data.read(self._DiscoveryProfileUri_fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    slength = struct.unpack('<i', data.red(1))
                    self.DiscoveryUrls = struct.unpack('<{}s'.format(slength), data.read(slength))
                    self.DiscoveryUrls = struct.unpack(self._DiscoveryUrls_fmt, data.read(self._DiscoveryUrls_fmt_size))[0]
            return data
            
class RequestHeader(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.AuthenticationToken = NodeId()
        self.Timestamp = 0
        self.RequestHandle = 0
        self._RequestHandle_fmt = '<I'
        self._RequestHandle_fmt_size = 4
        self.ReturnDiagnostics = 0
        self._ReturnDiagnostics_fmt = '<I'
        self._ReturnDiagnostics_fmt_size = 4
        self.AuditEntryId = ''
        self._AuditEntryId_fmt = '<s'
        self._AuditEntryId_fmt_size = 1
        self.TimeoutHint = 0
        self._TimeoutHint_fmt = '<I'
        self._TimeoutHint_fmt_size = 4
        self.AdditionalHeader = ExtensionObject()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.AuthenticationToken.to_binary())
        tmp.append(self.Timestamp.to_binary())
        tmp.append(struct.pack(self._RequestHandle_fmt, self.RequestHandle))
        tmp.append(struct.pack(self._ReturnDiagnostics_fmt, self.ReturnDiagnostics))
        tmp.append(struct.pack('<i', len(self.AuditEntryId)))
        tmp.append(struct.pack('<{}s'.format(len(self.AuditEntryId)), self.AuditEntryId.encode()))
        tmp.append(struct.pack(self._TimeoutHint_fmt, self.TimeoutHint))
        tmp.append(self.AdditionalHeader.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.AuthenticationToken = NodeId.from_binary(data)
            self.Timestamp = DateTime.from_binary(data)
            self.RequestHandle = struct.unpack(self._RequestHandle_fmt, data.read(self._RequestHandle_fmt_size))[0]
            self.ReturnDiagnostics = struct.unpack(self._ReturnDiagnostics_fmt, data.read(self._ReturnDiagnostics_fmt_size))[0]
            slength = struct.unpack('<i', data.red(1))
            self.AuditEntryId = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.AuditEntryId = struct.unpack(self._AuditEntryId_fmt, data.read(self._AuditEntryId_fmt_size))[0]
            self.TimeoutHint = struct.unpack(self._TimeoutHint_fmt, data.read(self._TimeoutHint_fmt_size))[0]
            self.AdditionalHeader = ExtensionObject.from_binary(data)
            return data
            
class ResponseHeader(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.Timestamp = 0
        self.RequestHandle = 0
        self._RequestHandle_fmt = '<I'
        self._RequestHandle_fmt_size = 4
        self.ServiceResult = StatusCode()
        self.ServiceDiagnostics = DiagnosticInfo()
        self.StringTable = []
        self._StringTable_fmt = '<s'
        self._StringTable_fmt_size = 1
        self.AdditionalHeader = ExtensionObject()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.Timestamp.to_binary())
        tmp.append(struct.pack(self._RequestHandle_fmt, self.RequestHandle))
        tmp.append(self.ServiceResult.to_binary())
        tmp.append(self.ServiceDiagnostics.to_binary())
        tmp.append(struct.pack('<i', len(self.StringTable)))
        for i in StringTable:
            tmp.append(struct.pack('<i', len(self.StringTable)))
            tmp.append(struct.pack('<{}s'.format(len(self.StringTable)), self.StringTable.encode()))
        tmp.append(self.AdditionalHeader.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.Timestamp = DateTime.from_binary(data)
            self.RequestHandle = struct.unpack(self._RequestHandle_fmt, data.read(self._RequestHandle_fmt_size))[0]
            self.ServiceResult = StatusCode.from_binary(data)
            self.ServiceDiagnostics = DiagnosticInfo.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    slength = struct.unpack('<i', data.red(1))
                    self.StringTable = struct.unpack('<{}s'.format(slength), data.read(slength))
                    self.StringTable = struct.unpack(self._StringTable_fmt, data.read(self._StringTable_fmt_size))[0]
            self.AdditionalHeader = ExtensionObject.from_binary(data)
            return data
            
class ServiceFault(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.ResponseHeader = ResponseHeader()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.ResponseHeader.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            return data
            
class FindServersParameters(object):
    def __init__(self):
        self.EndpointUrl = ''
        self._EndpointUrl_fmt = '<s'
        self._EndpointUrl_fmt_size = 1
        self.LocaleIds = []
        self._LocaleIds_fmt = '<s'
        self._LocaleIds_fmt_size = 1
        self.ServerUris = []
        self._ServerUris_fmt = '<s'
        self._ServerUris_fmt_size = 1
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack('<i', len(self.EndpointUrl)))
        tmp.append(struct.pack('<{}s'.format(len(self.EndpointUrl)), self.EndpointUrl.encode()))
        tmp.append(struct.pack('<i', len(self.LocaleIds)))
        for i in LocaleIds:
            tmp.append(struct.pack('<i', len(self.LocaleIds)))
            tmp.append(struct.pack('<{}s'.format(len(self.LocaleIds)), self.LocaleIds.encode()))
        tmp.append(struct.pack('<i', len(self.ServerUris)))
        for i in ServerUris:
            tmp.append(struct.pack('<i', len(self.ServerUris)))
            tmp.append(struct.pack('<{}s'.format(len(self.ServerUris)), self.ServerUris.encode()))
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            slength = struct.unpack('<i', data.red(1))
            self.EndpointUrl = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.EndpointUrl = struct.unpack(self._EndpointUrl_fmt, data.read(self._EndpointUrl_fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    slength = struct.unpack('<i', data.red(1))
                    self.LocaleIds = struct.unpack('<{}s'.format(slength), data.read(slength))
                    self.LocaleIds = struct.unpack(self._LocaleIds_fmt, data.read(self._LocaleIds_fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    slength = struct.unpack('<i', data.red(1))
                    self.ServerUris = struct.unpack('<{}s'.format(slength), data.read(slength))
                    self.ServerUris = struct.unpack(self._ServerUris_fmt, data.read(self._ServerUris_fmt_size))[0]
            return data
            
class FindServersRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.FindServersRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
        self.RequestHeader = RequestHeader()
        self.Parameters = FindServersParameters()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = FindServersParameters.from_binary(data)
            return data
            
class FindServersResult(object):
    def __init__(self):
        self.Servers = []
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack('<i', len(self.Servers)))
        for i in Servers:
            tmp.append(self.Servers.to_binary())
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
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            self.Parameters = FindServersResult.from_binary(data)
            return data
            
class UserTokenPolicy(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.PolicyId = ''
        self._PolicyId_fmt = '<s'
        self._PolicyId_fmt_size = 1
        self.TokenType = UserTokenType()
        self.IssuedTokenType = ''
        self._IssuedTokenType_fmt = '<s'
        self._IssuedTokenType_fmt_size = 1
        self.IssuerEndpointUrl = ''
        self._IssuerEndpointUrl_fmt = '<s'
        self._IssuerEndpointUrl_fmt_size = 1
        self.SecurityPolicyUri = ''
        self._SecurityPolicyUri_fmt = '<s'
        self._SecurityPolicyUri_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack('<i', len(self.PolicyId)))
        tmp.append(struct.pack('<{}s'.format(len(self.PolicyId)), self.PolicyId.encode()))
        tmp.append(self.TokenType.to_binary())
        tmp.append(struct.pack('<i', len(self.IssuedTokenType)))
        tmp.append(struct.pack('<{}s'.format(len(self.IssuedTokenType)), self.IssuedTokenType.encode()))
        tmp.append(struct.pack('<i', len(self.IssuerEndpointUrl)))
        tmp.append(struct.pack('<{}s'.format(len(self.IssuerEndpointUrl)), self.IssuerEndpointUrl.encode()))
        tmp.append(struct.pack('<i', len(self.SecurityPolicyUri)))
        tmp.append(struct.pack('<{}s'.format(len(self.SecurityPolicyUri)), self.SecurityPolicyUri.encode()))
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            slength = struct.unpack('<i', data.red(1))
            self.PolicyId = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.PolicyId = struct.unpack(self._PolicyId_fmt, data.read(self._PolicyId_fmt_size))[0]
            self.TokenType = UserTokenType.from_binary(data)
            slength = struct.unpack('<i', data.red(1))
            self.IssuedTokenType = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.IssuedTokenType = struct.unpack(self._IssuedTokenType_fmt, data.read(self._IssuedTokenType_fmt_size))[0]
            slength = struct.unpack('<i', data.red(1))
            self.IssuerEndpointUrl = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.IssuerEndpointUrl = struct.unpack(self._IssuerEndpointUrl_fmt, data.read(self._IssuerEndpointUrl_fmt_size))[0]
            slength = struct.unpack('<i', data.red(1))
            self.SecurityPolicyUri = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.SecurityPolicyUri = struct.unpack(self._SecurityPolicyUri_fmt, data.read(self._SecurityPolicyUri_fmt_size))[0]
            return data
            
class EndpointDescription(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.EndpointUrl = ''
        self._EndpointUrl_fmt = '<s'
        self._EndpointUrl_fmt_size = 1
        self.Server = ApplicationDescription()
        self.ServerCertificate = ByteString()
        self.SecurityMode = MessageSecurityMode()
        self.SecurityPolicyUri = ''
        self._SecurityPolicyUri_fmt = '<s'
        self._SecurityPolicyUri_fmt_size = 1
        self.UserIdentityTokens = []
        self.TransportProfileUri = ''
        self._TransportProfileUri_fmt = '<s'
        self._TransportProfileUri_fmt_size = 1
        self.SecurityLevel = 0
        self._SecurityLevel_fmt = '<B'
        self._SecurityLevel_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack('<i', len(self.EndpointUrl)))
        tmp.append(struct.pack('<{}s'.format(len(self.EndpointUrl)), self.EndpointUrl.encode()))
        tmp.append(self.Server.to_binary())
        tmp.append(self.ServerCertificate.to_binary())
        tmp.append(self.SecurityMode.to_binary())
        tmp.append(struct.pack('<i', len(self.SecurityPolicyUri)))
        tmp.append(struct.pack('<{}s'.format(len(self.SecurityPolicyUri)), self.SecurityPolicyUri.encode()))
        tmp.append(struct.pack('<i', len(self.UserIdentityTokens)))
        for i in UserIdentityTokens:
            tmp.append(self.UserIdentityTokens.to_binary())
        tmp.append(struct.pack('<i', len(self.TransportProfileUri)))
        tmp.append(struct.pack('<{}s'.format(len(self.TransportProfileUri)), self.TransportProfileUri.encode()))
        tmp.append(struct.pack(self._SecurityLevel_fmt, self.SecurityLevel))
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            slength = struct.unpack('<i', data.red(1))
            self.EndpointUrl = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.EndpointUrl = struct.unpack(self._EndpointUrl_fmt, data.read(self._EndpointUrl_fmt_size))[0]
            self.Server = ApplicationDescription.from_binary(data)
            self.ServerCertificate = ByteString.from_binary(data)
            self.SecurityMode = MessageSecurityMode.from_binary(data)
            slength = struct.unpack('<i', data.red(1))
            self.SecurityPolicyUri = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.SecurityPolicyUri = struct.unpack(self._SecurityPolicyUri_fmt, data.read(self._SecurityPolicyUri_fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.UserIdentityTokens = UserTokenPolicy.from_binary(data)
            slength = struct.unpack('<i', data.red(1))
            self.TransportProfileUri = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.TransportProfileUri = struct.unpack(self._TransportProfileUri_fmt, data.read(self._TransportProfileUri_fmt_size))[0]
            self.SecurityLevel = struct.unpack(self._SecurityLevel_fmt, data.read(self._SecurityLevel_fmt_size))[0]
            return data
            
class GetEndpointsParameters(object):
    def __init__(self):
        self.EndpointUrl = ''
        self._EndpointUrl_fmt = '<s'
        self._EndpointUrl_fmt_size = 1
        self.LocaleIds = []
        self._LocaleIds_fmt = '<s'
        self._LocaleIds_fmt_size = 1
        self.ProfileUris = []
        self._ProfileUris_fmt = '<s'
        self._ProfileUris_fmt_size = 1
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack('<i', len(self.EndpointUrl)))
        tmp.append(struct.pack('<{}s'.format(len(self.EndpointUrl)), self.EndpointUrl.encode()))
        tmp.append(struct.pack('<i', len(self.LocaleIds)))
        for i in LocaleIds:
            tmp.append(struct.pack('<i', len(self.LocaleIds)))
            tmp.append(struct.pack('<{}s'.format(len(self.LocaleIds)), self.LocaleIds.encode()))
        tmp.append(struct.pack('<i', len(self.ProfileUris)))
        for i in ProfileUris:
            tmp.append(struct.pack('<i', len(self.ProfileUris)))
            tmp.append(struct.pack('<{}s'.format(len(self.ProfileUris)), self.ProfileUris.encode()))
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            slength = struct.unpack('<i', data.red(1))
            self.EndpointUrl = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.EndpointUrl = struct.unpack(self._EndpointUrl_fmt, data.read(self._EndpointUrl_fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    slength = struct.unpack('<i', data.red(1))
                    self.LocaleIds = struct.unpack('<{}s'.format(slength), data.read(slength))
                    self.LocaleIds = struct.unpack(self._LocaleIds_fmt, data.read(self._LocaleIds_fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    slength = struct.unpack('<i', data.red(1))
                    self.ProfileUris = struct.unpack('<{}s'.format(slength), data.read(slength))
                    self.ProfileUris = struct.unpack(self._ProfileUris_fmt, data.read(self._ProfileUris_fmt_size))[0]
            return data
            
class GetEndpointsRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.GetEndpointsRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
        self.RequestHeader = RequestHeader()
        self.Parameters = GetEndpointsParameters()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
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
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(struct.pack('<i', len(self.Endpoints)))
        for i in Endpoints:
            tmp.append(self.Endpoints.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.Endpoints = EndpointDescription.from_binary(data)
            return data
            
class RegisteredServer(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.ServerUri = ''
        self._ServerUri_fmt = '<s'
        self._ServerUri_fmt_size = 1
        self.ProductUri = ''
        self._ProductUri_fmt = '<s'
        self._ProductUri_fmt_size = 1
        self.ServerNames = []
        self.ServerType = ApplicationType()
        self.GatewayServerUri = ''
        self._GatewayServerUri_fmt = '<s'
        self._GatewayServerUri_fmt_size = 1
        self.DiscoveryUrls = []
        self._DiscoveryUrls_fmt = '<s'
        self._DiscoveryUrls_fmt_size = 1
        self.SemaphoreFilePath = ''
        self._SemaphoreFilePath_fmt = '<s'
        self._SemaphoreFilePath_fmt_size = 1
        self.IsOnline = 0
        self._IsOnline_fmt = '<?'
        self._IsOnline_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack('<i', len(self.ServerUri)))
        tmp.append(struct.pack('<{}s'.format(len(self.ServerUri)), self.ServerUri.encode()))
        tmp.append(struct.pack('<i', len(self.ProductUri)))
        tmp.append(struct.pack('<{}s'.format(len(self.ProductUri)), self.ProductUri.encode()))
        tmp.append(struct.pack('<i', len(self.ServerNames)))
        for i in ServerNames:
            tmp.append(self.ServerNames.to_binary())
        tmp.append(self.ServerType.to_binary())
        tmp.append(struct.pack('<i', len(self.GatewayServerUri)))
        tmp.append(struct.pack('<{}s'.format(len(self.GatewayServerUri)), self.GatewayServerUri.encode()))
        tmp.append(struct.pack('<i', len(self.DiscoveryUrls)))
        for i in DiscoveryUrls:
            tmp.append(struct.pack('<i', len(self.DiscoveryUrls)))
            tmp.append(struct.pack('<{}s'.format(len(self.DiscoveryUrls)), self.DiscoveryUrls.encode()))
        tmp.append(struct.pack('<i', len(self.SemaphoreFilePath)))
        tmp.append(struct.pack('<{}s'.format(len(self.SemaphoreFilePath)), self.SemaphoreFilePath.encode()))
        tmp.append(struct.pack(self._IsOnline_fmt, self.IsOnline))
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            slength = struct.unpack('<i', data.red(1))
            self.ServerUri = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.ServerUri = struct.unpack(self._ServerUri_fmt, data.read(self._ServerUri_fmt_size))[0]
            slength = struct.unpack('<i', data.red(1))
            self.ProductUri = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.ProductUri = struct.unpack(self._ProductUri_fmt, data.read(self._ProductUri_fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.ServerNames = LocalizedText.from_binary(data)
            self.ServerType = ApplicationType.from_binary(data)
            slength = struct.unpack('<i', data.red(1))
            self.GatewayServerUri = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.GatewayServerUri = struct.unpack(self._GatewayServerUri_fmt, data.read(self._GatewayServerUri_fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    slength = struct.unpack('<i', data.red(1))
                    self.DiscoveryUrls = struct.unpack('<{}s'.format(slength), data.read(slength))
                    self.DiscoveryUrls = struct.unpack(self._DiscoveryUrls_fmt, data.read(self._DiscoveryUrls_fmt_size))[0]
            slength = struct.unpack('<i', data.red(1))
            self.SemaphoreFilePath = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.SemaphoreFilePath = struct.unpack(self._SemaphoreFilePath_fmt, data.read(self._SemaphoreFilePath_fmt_size))[0]
            self.IsOnline = struct.unpack(self._IsOnline_fmt, data.read(self._IsOnline_fmt_size))[0]
            return data
            
class RegisterServerParameters(object):
    def __init__(self):
        self.Server = RegisteredServer()
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(self.Server.to_binary())
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
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = RegisterServerParameters.from_binary(data)
            return data
            
class RegisterServerResponse(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.RegisterServerResponse_Encoding_DefaultBinary, NodeIdType.FourByte)
        self.ResponseHeader = ResponseHeader()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.ResponseHeader.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            return data
            
class ChannelSecurityToken(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.ChannelId = 0
        self._ChannelId_fmt = '<I'
        self._ChannelId_fmt_size = 4
        self.TokenId = 0
        self._TokenId_fmt = '<I'
        self._TokenId_fmt_size = 4
        self.CreatedAt = 0
        self.RevisedLifetime = 0
        self._RevisedLifetime_fmt = '<I'
        self._RevisedLifetime_fmt_size = 4
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack(self._ChannelId_fmt, self.ChannelId))
        tmp.append(struct.pack(self._TokenId_fmt, self.TokenId))
        tmp.append(self.CreatedAt.to_binary())
        tmp.append(struct.pack(self._RevisedLifetime_fmt, self.RevisedLifetime))
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.ChannelId = struct.unpack(self._ChannelId_fmt, data.read(self._ChannelId_fmt_size))[0]
            self.TokenId = struct.unpack(self._TokenId_fmt, data.read(self._TokenId_fmt_size))[0]
            self.CreatedAt = DateTime.from_binary(data)
            self.RevisedLifetime = struct.unpack(self._RevisedLifetime_fmt, data.read(self._RevisedLifetime_fmt_size))[0]
            return data
            
class OpenSecureChannelParameters(object):
    def __init__(self):
        self.ClientProtocolVersion = 0
        self._ClientProtocolVersion_fmt = '<I'
        self._ClientProtocolVersion_fmt_size = 4
        self.RequestType = SecurityTokenRequestType()
        self.SecurityMode = MessageSecurityMode()
        self.ClientNonce = ByteString()
        self.RequestedLifetime = 0
        self._RequestedLifetime_fmt = '<I'
        self._RequestedLifetime_fmt_size = 4
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack(self._ClientProtocolVersion_fmt, self.ClientProtocolVersion))
        tmp.append(self.RequestType.to_binary())
        tmp.append(self.SecurityMode.to_binary())
        tmp.append(self.ClientNonce.to_binary())
        tmp.append(struct.pack(self._RequestedLifetime_fmt, self.RequestedLifetime))
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.ClientProtocolVersion = struct.unpack(self._ClientProtocolVersion_fmt, data.read(self._ClientProtocolVersion_fmt_size))[0]
            self.RequestType = SecurityTokenRequestType.from_binary(data)
            self.SecurityMode = MessageSecurityMode.from_binary(data)
            self.ClientNonce = ByteString.from_binary(data)
            self.RequestedLifetime = struct.unpack(self._RequestedLifetime_fmt, data.read(self._RequestedLifetime_fmt_size))[0]
            return data
            
class OpenSecureChannelRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.OpenSecureChannelRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
        self.RequestHeader = RequestHeader()
        self.Parameters = OpenSecureChannelParameters()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = OpenSecureChannelParameters.from_binary(data)
            return data
            
class OpenSecureChannelResult(object):
    def __init__(self):
        self.ServerProtocolVersion = 0
        self._ServerProtocolVersion_fmt = '<I'
        self._ServerProtocolVersion_fmt_size = 4
        self.SecurityToken = ChannelSecurityToken()
        self.ServerNonce = ByteString()
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack(self._ServerProtocolVersion_fmt, self.ServerProtocolVersion))
        tmp.append(self.SecurityToken.to_binary())
        tmp.append(self.ServerNonce.to_binary())
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.ServerProtocolVersion = struct.unpack(self._ServerProtocolVersion_fmt, data.read(self._ServerProtocolVersion_fmt_size))[0]
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
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            self.Parameters = OpenSecureChannelResult.from_binary(data)
            return data
            
class CloseSecureChannelRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.CloseSecureChannelRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
        self.RequestHeader = RequestHeader()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.RequestHeader.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            return data
            
class CloseSecureChannelResponse(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.CloseSecureChannelResponse_Encoding_DefaultBinary, NodeIdType.FourByte)
        self.ResponseHeader = ResponseHeader()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.ResponseHeader.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            return data
            
class SignedSoftwareCertificate(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.CertificateData = ByteString()
        self.Signature = ByteString()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.CertificateData.to_binary())
        tmp.append(self.Signature.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.CertificateData = ByteString.from_binary(data)
            self.Signature = ByteString.from_binary(data)
            return data
            
class SignatureData(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.Algorithm = ''
        self._Algorithm_fmt = '<s'
        self._Algorithm_fmt_size = 1
        self.Signature = ByteString()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack('<i', len(self.Algorithm)))
        tmp.append(struct.pack('<{}s'.format(len(self.Algorithm)), self.Algorithm.encode()))
        tmp.append(self.Signature.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            slength = struct.unpack('<i', data.red(1))
            self.Algorithm = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.Algorithm = struct.unpack(self._Algorithm_fmt, data.read(self._Algorithm_fmt_size))[0]
            self.Signature = ByteString.from_binary(data)
            return data
            
class CreateSessionParameters(object):
    def __init__(self):
        self.ClientDescription = ApplicationDescription()
        self.ServerUri = ''
        self._ServerUri_fmt = '<s'
        self._ServerUri_fmt_size = 1
        self.EndpointUrl = ''
        self._EndpointUrl_fmt = '<s'
        self._EndpointUrl_fmt_size = 1
        self.SessionName = ''
        self._SessionName_fmt = '<s'
        self._SessionName_fmt_size = 1
        self.ClientNonce = ByteString()
        self.ClientCertificate = ByteString()
        self.RequestedSessionTimeout = 0
        self._RequestedSessionTimeout_fmt = '<d'
        self._RequestedSessionTimeout_fmt_size = 8
        self.MaxResponseMessageSize = 0
        self._MaxResponseMessageSize_fmt = '<I'
        self._MaxResponseMessageSize_fmt_size = 4
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(self.ClientDescription.to_binary())
        tmp.append(struct.pack('<i', len(self.ServerUri)))
        tmp.append(struct.pack('<{}s'.format(len(self.ServerUri)), self.ServerUri.encode()))
        tmp.append(struct.pack('<i', len(self.EndpointUrl)))
        tmp.append(struct.pack('<{}s'.format(len(self.EndpointUrl)), self.EndpointUrl.encode()))
        tmp.append(struct.pack('<i', len(self.SessionName)))
        tmp.append(struct.pack('<{}s'.format(len(self.SessionName)), self.SessionName.encode()))
        tmp.append(self.ClientNonce.to_binary())
        tmp.append(self.ClientCertificate.to_binary())
        tmp.append(struct.pack(self._RequestedSessionTimeout_fmt, self.RequestedSessionTimeout))
        tmp.append(struct.pack(self._MaxResponseMessageSize_fmt, self.MaxResponseMessageSize))
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.ClientDescription = ApplicationDescription.from_binary(data)
            slength = struct.unpack('<i', data.red(1))
            self.ServerUri = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.ServerUri = struct.unpack(self._ServerUri_fmt, data.read(self._ServerUri_fmt_size))[0]
            slength = struct.unpack('<i', data.red(1))
            self.EndpointUrl = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.EndpointUrl = struct.unpack(self._EndpointUrl_fmt, data.read(self._EndpointUrl_fmt_size))[0]
            slength = struct.unpack('<i', data.red(1))
            self.SessionName = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.SessionName = struct.unpack(self._SessionName_fmt, data.read(self._SessionName_fmt_size))[0]
            self.ClientNonce = ByteString.from_binary(data)
            self.ClientCertificate = ByteString.from_binary(data)
            self.RequestedSessionTimeout = struct.unpack(self._RequestedSessionTimeout_fmt, data.read(self._RequestedSessionTimeout_fmt_size))[0]
            self.MaxResponseMessageSize = struct.unpack(self._MaxResponseMessageSize_fmt, data.read(self._MaxResponseMessageSize_fmt_size))[0]
            return data
            
class CreateSessionRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.CreateSessionRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
        self.RequestHeader = RequestHeader()
        self.Parameters = CreateSessionParameters()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = CreateSessionParameters.from_binary(data)
            return data
            
class CreateSessionResult(object):
    def __init__(self):
        self.SessionId = NodeId()
        self.AuthenticationToken = NodeId()
        self.RevisedSessionTimeout = 0
        self._RevisedSessionTimeout_fmt = '<d'
        self._RevisedSessionTimeout_fmt_size = 8
        self.ServerNonce = ByteString()
        self.ServerCertificate = ByteString()
        self.ServerEndpoints = []
        self.ServerSoftwareCertificates = []
        self.ServerSignature = SignatureData()
        self.MaxRequestMessageSize = 0
        self._MaxRequestMessageSize_fmt = '<I'
        self._MaxRequestMessageSize_fmt_size = 4
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(self.SessionId.to_binary())
        tmp.append(self.AuthenticationToken.to_binary())
        tmp.append(struct.pack(self._RevisedSessionTimeout_fmt, self.RevisedSessionTimeout))
        tmp.append(self.ServerNonce.to_binary())
        tmp.append(self.ServerCertificate.to_binary())
        tmp.append(struct.pack('<i', len(self.ServerEndpoints)))
        for i in ServerEndpoints:
            tmp.append(self.ServerEndpoints.to_binary())
        tmp.append(struct.pack('<i', len(self.ServerSoftwareCertificates)))
        for i in ServerSoftwareCertificates:
            tmp.append(self.ServerSoftwareCertificates.to_binary())
        tmp.append(self.ServerSignature.to_binary())
        tmp.append(struct.pack(self._MaxRequestMessageSize_fmt, self.MaxRequestMessageSize))
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.SessionId = NodeId.from_binary(data)
            self.AuthenticationToken = NodeId.from_binary(data)
            self.RevisedSessionTimeout = struct.unpack(self._RevisedSessionTimeout_fmt, data.read(self._RevisedSessionTimeout_fmt_size))[0]
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
            self.MaxRequestMessageSize = struct.unpack(self._MaxRequestMessageSize_fmt, data.read(self._MaxRequestMessageSize_fmt_size))[0]
            return data
            
class CreateSessionResponse(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.CreateSessionResponse_Encoding_DefaultBinary, NodeIdType.FourByte)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = CreateSessionResult()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            self.Parameters = CreateSessionResult.from_binary(data)
            return data
            
class UserIdentityToken(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.PolicyId = ''
        self._PolicyId_fmt = '<s'
        self._PolicyId_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack('<i', len(self.PolicyId)))
        tmp.append(struct.pack('<{}s'.format(len(self.PolicyId)), self.PolicyId.encode()))
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            slength = struct.unpack('<i', data.red(1))
            self.PolicyId = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.PolicyId = struct.unpack(self._PolicyId_fmt, data.read(self._PolicyId_fmt_size))[0]
            return data
            
class AnonymousIdentityToken(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.PolicyId = ''
        self._PolicyId_fmt = '<s'
        self._PolicyId_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack('<i', len(self.PolicyId)))
        tmp.append(struct.pack('<{}s'.format(len(self.PolicyId)), self.PolicyId.encode()))
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            slength = struct.unpack('<i', data.red(1))
            self.PolicyId = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.PolicyId = struct.unpack(self._PolicyId_fmt, data.read(self._PolicyId_fmt_size))[0]
            return data
            
class UserNameIdentityToken(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.PolicyId = ''
        self._PolicyId_fmt = '<s'
        self._PolicyId_fmt_size = 1
        self.UserName = ''
        self._UserName_fmt = '<s'
        self._UserName_fmt_size = 1
        self.Password = ByteString()
        self.EncryptionAlgorithm = ''
        self._EncryptionAlgorithm_fmt = '<s'
        self._EncryptionAlgorithm_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack('<i', len(self.PolicyId)))
        tmp.append(struct.pack('<{}s'.format(len(self.PolicyId)), self.PolicyId.encode()))
        tmp.append(struct.pack('<i', len(self.UserName)))
        tmp.append(struct.pack('<{}s'.format(len(self.UserName)), self.UserName.encode()))
        tmp.append(self.Password.to_binary())
        tmp.append(struct.pack('<i', len(self.EncryptionAlgorithm)))
        tmp.append(struct.pack('<{}s'.format(len(self.EncryptionAlgorithm)), self.EncryptionAlgorithm.encode()))
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            slength = struct.unpack('<i', data.red(1))
            self.PolicyId = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.PolicyId = struct.unpack(self._PolicyId_fmt, data.read(self._PolicyId_fmt_size))[0]
            slength = struct.unpack('<i', data.red(1))
            self.UserName = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.UserName = struct.unpack(self._UserName_fmt, data.read(self._UserName_fmt_size))[0]
            self.Password = ByteString.from_binary(data)
            slength = struct.unpack('<i', data.red(1))
            self.EncryptionAlgorithm = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.EncryptionAlgorithm = struct.unpack(self._EncryptionAlgorithm_fmt, data.read(self._EncryptionAlgorithm_fmt_size))[0]
            return data
            
class X509IdentityToken(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.PolicyId = ''
        self._PolicyId_fmt = '<s'
        self._PolicyId_fmt_size = 1
        self.CertificateData = ByteString()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack('<i', len(self.PolicyId)))
        tmp.append(struct.pack('<{}s'.format(len(self.PolicyId)), self.PolicyId.encode()))
        tmp.append(self.CertificateData.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            slength = struct.unpack('<i', data.red(1))
            self.PolicyId = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.PolicyId = struct.unpack(self._PolicyId_fmt, data.read(self._PolicyId_fmt_size))[0]
            self.CertificateData = ByteString.from_binary(data)
            return data
            
class IssuedIdentityToken(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.PolicyId = ''
        self._PolicyId_fmt = '<s'
        self._PolicyId_fmt_size = 1
        self.TokenData = ByteString()
        self.EncryptionAlgorithm = ''
        self._EncryptionAlgorithm_fmt = '<s'
        self._EncryptionAlgorithm_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack('<i', len(self.PolicyId)))
        tmp.append(struct.pack('<{}s'.format(len(self.PolicyId)), self.PolicyId.encode()))
        tmp.append(self.TokenData.to_binary())
        tmp.append(struct.pack('<i', len(self.EncryptionAlgorithm)))
        tmp.append(struct.pack('<{}s'.format(len(self.EncryptionAlgorithm)), self.EncryptionAlgorithm.encode()))
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            slength = struct.unpack('<i', data.red(1))
            self.PolicyId = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.PolicyId = struct.unpack(self._PolicyId_fmt, data.read(self._PolicyId_fmt_size))[0]
            self.TokenData = ByteString.from_binary(data)
            slength = struct.unpack('<i', data.red(1))
            self.EncryptionAlgorithm = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.EncryptionAlgorithm = struct.unpack(self._EncryptionAlgorithm_fmt, data.read(self._EncryptionAlgorithm_fmt_size))[0]
            return data
            
class ActivateSessionParameters(object):
    def __init__(self):
        self.ClientSignature = SignatureData()
        self.ClientSoftwareCertificates = []
        self.LocaleIds = []
        self._LocaleIds_fmt = '<s'
        self._LocaleIds_fmt_size = 1
        self.UserIdentityToken = ExtensionObject()
        self.UserTokenSignature = SignatureData()
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(self.ClientSignature.to_binary())
        tmp.append(struct.pack('<i', len(self.ClientSoftwareCertificates)))
        for i in ClientSoftwareCertificates:
            tmp.append(self.ClientSoftwareCertificates.to_binary())
        tmp.append(struct.pack('<i', len(self.LocaleIds)))
        for i in LocaleIds:
            tmp.append(struct.pack('<i', len(self.LocaleIds)))
            tmp.append(struct.pack('<{}s'.format(len(self.LocaleIds)), self.LocaleIds.encode()))
        tmp.append(self.UserIdentityToken.to_binary())
        tmp.append(self.UserTokenSignature.to_binary())
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
                    self.LocaleIds = struct.unpack(self._LocaleIds_fmt, data.read(self._LocaleIds_fmt_size))[0]
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
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
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
        tmp = packet
        tmp.append(self.ServerNonce.to_binary())
        tmp.append(struct.pack('<i', len(self.Results)))
        for i in Results:
            tmp.append(self.Results.to_binary())
        tmp.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for i in DiagnosticInfos:
            tmp.append(self.DiagnosticInfos.to_binary())
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
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            self.Parameters = ActivateSessionResult.from_binary(data)
            return data
            
class CloseSessionRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.CloseSessionRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
        self.RequestHeader = RequestHeader()
        self.DeleteSubscriptions = 0
        self._DeleteSubscriptions_fmt = '<?'
        self._DeleteSubscriptions_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(struct.pack(self._DeleteSubscriptions_fmt, self.DeleteSubscriptions))
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.DeleteSubscriptions = struct.unpack(self._DeleteSubscriptions_fmt, data.read(self._DeleteSubscriptions_fmt_size))[0]
            return data
            
class CloseSessionResponse(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.CloseSessionResponse_Encoding_DefaultBinary, NodeIdType.FourByte)
        self.ResponseHeader = ResponseHeader()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.ResponseHeader.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            return data
            
class CancelParameters(object):
    def __init__(self):
        self.RequestHandle = 0
        self._RequestHandle_fmt = '<I'
        self._RequestHandle_fmt_size = 4
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack(self._RequestHandle_fmt, self.RequestHandle))
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.RequestHandle = struct.unpack(self._RequestHandle_fmt, data.read(self._RequestHandle_fmt_size))[0]
            return data
            
class CancelRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.CancelRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
        self.RequestHeader = RequestHeader()
        self.Parameters = CancelParameters()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = CancelParameters.from_binary(data)
            return data
            
class CancelResult(object):
    def __init__(self):
        self.CancelCount = 0
        self._CancelCount_fmt = '<I'
        self._CancelCount_fmt_size = 4
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack(self._CancelCount_fmt, self.CancelCount))
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.CancelCount = struct.unpack(self._CancelCount_fmt, data.read(self._CancelCount_fmt_size))[0]
            return data
            
class CancelResponse(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.CancelResponse_Encoding_DefaultBinary, NodeIdType.FourByte)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = CancelResult()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            self.Parameters = CancelResult.from_binary(data)
            return data
            
class NodeAttributes(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.SpecifiedAttributes = 0
        self._SpecifiedAttributes_fmt = '<I'
        self._SpecifiedAttributes_fmt_size = 4
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self._WriteMask_fmt = '<I'
        self._WriteMask_fmt_size = 4
        self.UserWriteMask = 0
        self._UserWriteMask_fmt = '<I'
        self._UserWriteMask_fmt_size = 4
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack(self._SpecifiedAttributes_fmt, self.SpecifiedAttributes))
        tmp.append(self.DisplayName.to_binary())
        tmp.append(self.Description.to_binary())
        tmp.append(struct.pack(self._WriteMask_fmt, self.WriteMask))
        tmp.append(struct.pack(self._UserWriteMask_fmt, self.UserWriteMask))
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.SpecifiedAttributes = struct.unpack(self._SpecifiedAttributes_fmt, data.read(self._SpecifiedAttributes_fmt_size))[0]
            self.DisplayName = LocalizedText.from_binary(data)
            self.Description = LocalizedText.from_binary(data)
            self.WriteMask = struct.unpack(self._WriteMask_fmt, data.read(self._WriteMask_fmt_size))[0]
            self.UserWriteMask = struct.unpack(self._UserWriteMask_fmt, data.read(self._UserWriteMask_fmt_size))[0]
            return data
            
class ObjectAttributes(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.SpecifiedAttributes = 0
        self._SpecifiedAttributes_fmt = '<I'
        self._SpecifiedAttributes_fmt_size = 4
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self._WriteMask_fmt = '<I'
        self._WriteMask_fmt_size = 4
        self.UserWriteMask = 0
        self._UserWriteMask_fmt = '<I'
        self._UserWriteMask_fmt_size = 4
        self.EventNotifier = 0
        self._EventNotifier_fmt = '<B'
        self._EventNotifier_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack(self._SpecifiedAttributes_fmt, self.SpecifiedAttributes))
        tmp.append(self.DisplayName.to_binary())
        tmp.append(self.Description.to_binary())
        tmp.append(struct.pack(self._WriteMask_fmt, self.WriteMask))
        tmp.append(struct.pack(self._UserWriteMask_fmt, self.UserWriteMask))
        tmp.append(struct.pack(self._EventNotifier_fmt, self.EventNotifier))
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.SpecifiedAttributes = struct.unpack(self._SpecifiedAttributes_fmt, data.read(self._SpecifiedAttributes_fmt_size))[0]
            self.DisplayName = LocalizedText.from_binary(data)
            self.Description = LocalizedText.from_binary(data)
            self.WriteMask = struct.unpack(self._WriteMask_fmt, data.read(self._WriteMask_fmt_size))[0]
            self.UserWriteMask = struct.unpack(self._UserWriteMask_fmt, data.read(self._UserWriteMask_fmt_size))[0]
            self.EventNotifier = struct.unpack(self._EventNotifier_fmt, data.read(self._EventNotifier_fmt_size))[0]
            return data
            
class VariableAttributes(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.SpecifiedAttributes = 0
        self._SpecifiedAttributes_fmt = '<I'
        self._SpecifiedAttributes_fmt_size = 4
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self._WriteMask_fmt = '<I'
        self._WriteMask_fmt_size = 4
        self.UserWriteMask = 0
        self._UserWriteMask_fmt = '<I'
        self._UserWriteMask_fmt_size = 4
        self.Value = Variant()
        self.DataType = NodeId()
        self.ValueRank = 0
        self._ValueRank_fmt = '<i'
        self._ValueRank_fmt_size = 4
        self.ArrayDimensions = []
        self._ArrayDimensions_fmt = '<I'
        self._ArrayDimensions_fmt_size = 4
        self.AccessLevel = 0
        self._AccessLevel_fmt = '<B'
        self._AccessLevel_fmt_size = 1
        self.UserAccessLevel = 0
        self._UserAccessLevel_fmt = '<B'
        self._UserAccessLevel_fmt_size = 1
        self.MinimumSamplingInterval = 0
        self._MinimumSamplingInterval_fmt = '<d'
        self._MinimumSamplingInterval_fmt_size = 8
        self.Historizing = 0
        self._Historizing_fmt = '<?'
        self._Historizing_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack(self._SpecifiedAttributes_fmt, self.SpecifiedAttributes))
        tmp.append(self.DisplayName.to_binary())
        tmp.append(self.Description.to_binary())
        tmp.append(struct.pack(self._WriteMask_fmt, self.WriteMask))
        tmp.append(struct.pack(self._UserWriteMask_fmt, self.UserWriteMask))
        tmp.append(self.Value.to_binary())
        tmp.append(self.DataType.to_binary())
        tmp.append(struct.pack(self._ValueRank_fmt, self.ValueRank))
        tmp.append(struct.pack('<i', len(self.ArrayDimensions)))
        for i in ArrayDimensions:
            tmp.append(struct.pack(self._ArrayDimensions_fmt, self.ArrayDimensions))
        tmp.append(struct.pack(self._AccessLevel_fmt, self.AccessLevel))
        tmp.append(struct.pack(self._UserAccessLevel_fmt, self.UserAccessLevel))
        tmp.append(struct.pack(self._MinimumSamplingInterval_fmt, self.MinimumSamplingInterval))
        tmp.append(struct.pack(self._Historizing_fmt, self.Historizing))
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.SpecifiedAttributes = struct.unpack(self._SpecifiedAttributes_fmt, data.read(self._SpecifiedAttributes_fmt_size))[0]
            self.DisplayName = LocalizedText.from_binary(data)
            self.Description = LocalizedText.from_binary(data)
            self.WriteMask = struct.unpack(self._WriteMask_fmt, data.read(self._WriteMask_fmt_size))[0]
            self.UserWriteMask = struct.unpack(self._UserWriteMask_fmt, data.read(self._UserWriteMask_fmt_size))[0]
            self.Value = Variant.from_binary(data)
            self.DataType = NodeId.from_binary(data)
            self.ValueRank = struct.unpack(self._ValueRank_fmt, data.read(self._ValueRank_fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.ArrayDimensions = struct.unpack(self._ArrayDimensions_fmt, data.read(self._ArrayDimensions_fmt_size))[0]
            self.AccessLevel = struct.unpack(self._AccessLevel_fmt, data.read(self._AccessLevel_fmt_size))[0]
            self.UserAccessLevel = struct.unpack(self._UserAccessLevel_fmt, data.read(self._UserAccessLevel_fmt_size))[0]
            self.MinimumSamplingInterval = struct.unpack(self._MinimumSamplingInterval_fmt, data.read(self._MinimumSamplingInterval_fmt_size))[0]
            self.Historizing = struct.unpack(self._Historizing_fmt, data.read(self._Historizing_fmt_size))[0]
            return data
            
class MethodAttributes(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.SpecifiedAttributes = 0
        self._SpecifiedAttributes_fmt = '<I'
        self._SpecifiedAttributes_fmt_size = 4
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self._WriteMask_fmt = '<I'
        self._WriteMask_fmt_size = 4
        self.UserWriteMask = 0
        self._UserWriteMask_fmt = '<I'
        self._UserWriteMask_fmt_size = 4
        self.Executable = 0
        self._Executable_fmt = '<?'
        self._Executable_fmt_size = 1
        self.UserExecutable = 0
        self._UserExecutable_fmt = '<?'
        self._UserExecutable_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack(self._SpecifiedAttributes_fmt, self.SpecifiedAttributes))
        tmp.append(self.DisplayName.to_binary())
        tmp.append(self.Description.to_binary())
        tmp.append(struct.pack(self._WriteMask_fmt, self.WriteMask))
        tmp.append(struct.pack(self._UserWriteMask_fmt, self.UserWriteMask))
        tmp.append(struct.pack(self._Executable_fmt, self.Executable))
        tmp.append(struct.pack(self._UserExecutable_fmt, self.UserExecutable))
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.SpecifiedAttributes = struct.unpack(self._SpecifiedAttributes_fmt, data.read(self._SpecifiedAttributes_fmt_size))[0]
            self.DisplayName = LocalizedText.from_binary(data)
            self.Description = LocalizedText.from_binary(data)
            self.WriteMask = struct.unpack(self._WriteMask_fmt, data.read(self._WriteMask_fmt_size))[0]
            self.UserWriteMask = struct.unpack(self._UserWriteMask_fmt, data.read(self._UserWriteMask_fmt_size))[0]
            self.Executable = struct.unpack(self._Executable_fmt, data.read(self._Executable_fmt_size))[0]
            self.UserExecutable = struct.unpack(self._UserExecutable_fmt, data.read(self._UserExecutable_fmt_size))[0]
            return data
            
class ObjectTypeAttributes(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.SpecifiedAttributes = 0
        self._SpecifiedAttributes_fmt = '<I'
        self._SpecifiedAttributes_fmt_size = 4
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self._WriteMask_fmt = '<I'
        self._WriteMask_fmt_size = 4
        self.UserWriteMask = 0
        self._UserWriteMask_fmt = '<I'
        self._UserWriteMask_fmt_size = 4
        self.IsAbstract = 0
        self._IsAbstract_fmt = '<?'
        self._IsAbstract_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack(self._SpecifiedAttributes_fmt, self.SpecifiedAttributes))
        tmp.append(self.DisplayName.to_binary())
        tmp.append(self.Description.to_binary())
        tmp.append(struct.pack(self._WriteMask_fmt, self.WriteMask))
        tmp.append(struct.pack(self._UserWriteMask_fmt, self.UserWriteMask))
        tmp.append(struct.pack(self._IsAbstract_fmt, self.IsAbstract))
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.SpecifiedAttributes = struct.unpack(self._SpecifiedAttributes_fmt, data.read(self._SpecifiedAttributes_fmt_size))[0]
            self.DisplayName = LocalizedText.from_binary(data)
            self.Description = LocalizedText.from_binary(data)
            self.WriteMask = struct.unpack(self._WriteMask_fmt, data.read(self._WriteMask_fmt_size))[0]
            self.UserWriteMask = struct.unpack(self._UserWriteMask_fmt, data.read(self._UserWriteMask_fmt_size))[0]
            self.IsAbstract = struct.unpack(self._IsAbstract_fmt, data.read(self._IsAbstract_fmt_size))[0]
            return data
            
class VariableTypeAttributes(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.SpecifiedAttributes = 0
        self._SpecifiedAttributes_fmt = '<I'
        self._SpecifiedAttributes_fmt_size = 4
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self._WriteMask_fmt = '<I'
        self._WriteMask_fmt_size = 4
        self.UserWriteMask = 0
        self._UserWriteMask_fmt = '<I'
        self._UserWriteMask_fmt_size = 4
        self.Value = Variant()
        self.DataType = NodeId()
        self.ValueRank = 0
        self._ValueRank_fmt = '<i'
        self._ValueRank_fmt_size = 4
        self.ArrayDimensions = []
        self._ArrayDimensions_fmt = '<I'
        self._ArrayDimensions_fmt_size = 4
        self.IsAbstract = 0
        self._IsAbstract_fmt = '<?'
        self._IsAbstract_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack(self._SpecifiedAttributes_fmt, self.SpecifiedAttributes))
        tmp.append(self.DisplayName.to_binary())
        tmp.append(self.Description.to_binary())
        tmp.append(struct.pack(self._WriteMask_fmt, self.WriteMask))
        tmp.append(struct.pack(self._UserWriteMask_fmt, self.UserWriteMask))
        tmp.append(self.Value.to_binary())
        tmp.append(self.DataType.to_binary())
        tmp.append(struct.pack(self._ValueRank_fmt, self.ValueRank))
        tmp.append(struct.pack('<i', len(self.ArrayDimensions)))
        for i in ArrayDimensions:
            tmp.append(struct.pack(self._ArrayDimensions_fmt, self.ArrayDimensions))
        tmp.append(struct.pack(self._IsAbstract_fmt, self.IsAbstract))
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.SpecifiedAttributes = struct.unpack(self._SpecifiedAttributes_fmt, data.read(self._SpecifiedAttributes_fmt_size))[0]
            self.DisplayName = LocalizedText.from_binary(data)
            self.Description = LocalizedText.from_binary(data)
            self.WriteMask = struct.unpack(self._WriteMask_fmt, data.read(self._WriteMask_fmt_size))[0]
            self.UserWriteMask = struct.unpack(self._UserWriteMask_fmt, data.read(self._UserWriteMask_fmt_size))[0]
            self.Value = Variant.from_binary(data)
            self.DataType = NodeId.from_binary(data)
            self.ValueRank = struct.unpack(self._ValueRank_fmt, data.read(self._ValueRank_fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.ArrayDimensions = struct.unpack(self._ArrayDimensions_fmt, data.read(self._ArrayDimensions_fmt_size))[0]
            self.IsAbstract = struct.unpack(self._IsAbstract_fmt, data.read(self._IsAbstract_fmt_size))[0]
            return data
            
class ReferenceTypeAttributes(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.SpecifiedAttributes = 0
        self._SpecifiedAttributes_fmt = '<I'
        self._SpecifiedAttributes_fmt_size = 4
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self._WriteMask_fmt = '<I'
        self._WriteMask_fmt_size = 4
        self.UserWriteMask = 0
        self._UserWriteMask_fmt = '<I'
        self._UserWriteMask_fmt_size = 4
        self.IsAbstract = 0
        self._IsAbstract_fmt = '<?'
        self._IsAbstract_fmt_size = 1
        self.Symmetric = 0
        self._Symmetric_fmt = '<?'
        self._Symmetric_fmt_size = 1
        self.InverseName = LocalizedText()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack(self._SpecifiedAttributes_fmt, self.SpecifiedAttributes))
        tmp.append(self.DisplayName.to_binary())
        tmp.append(self.Description.to_binary())
        tmp.append(struct.pack(self._WriteMask_fmt, self.WriteMask))
        tmp.append(struct.pack(self._UserWriteMask_fmt, self.UserWriteMask))
        tmp.append(struct.pack(self._IsAbstract_fmt, self.IsAbstract))
        tmp.append(struct.pack(self._Symmetric_fmt, self.Symmetric))
        tmp.append(self.InverseName.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.SpecifiedAttributes = struct.unpack(self._SpecifiedAttributes_fmt, data.read(self._SpecifiedAttributes_fmt_size))[0]
            self.DisplayName = LocalizedText.from_binary(data)
            self.Description = LocalizedText.from_binary(data)
            self.WriteMask = struct.unpack(self._WriteMask_fmt, data.read(self._WriteMask_fmt_size))[0]
            self.UserWriteMask = struct.unpack(self._UserWriteMask_fmt, data.read(self._UserWriteMask_fmt_size))[0]
            self.IsAbstract = struct.unpack(self._IsAbstract_fmt, data.read(self._IsAbstract_fmt_size))[0]
            self.Symmetric = struct.unpack(self._Symmetric_fmt, data.read(self._Symmetric_fmt_size))[0]
            self.InverseName = LocalizedText.from_binary(data)
            return data
            
class DataTypeAttributes(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.SpecifiedAttributes = 0
        self._SpecifiedAttributes_fmt = '<I'
        self._SpecifiedAttributes_fmt_size = 4
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self._WriteMask_fmt = '<I'
        self._WriteMask_fmt_size = 4
        self.UserWriteMask = 0
        self._UserWriteMask_fmt = '<I'
        self._UserWriteMask_fmt_size = 4
        self.IsAbstract = 0
        self._IsAbstract_fmt = '<?'
        self._IsAbstract_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack(self._SpecifiedAttributes_fmt, self.SpecifiedAttributes))
        tmp.append(self.DisplayName.to_binary())
        tmp.append(self.Description.to_binary())
        tmp.append(struct.pack(self._WriteMask_fmt, self.WriteMask))
        tmp.append(struct.pack(self._UserWriteMask_fmt, self.UserWriteMask))
        tmp.append(struct.pack(self._IsAbstract_fmt, self.IsAbstract))
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.SpecifiedAttributes = struct.unpack(self._SpecifiedAttributes_fmt, data.read(self._SpecifiedAttributes_fmt_size))[0]
            self.DisplayName = LocalizedText.from_binary(data)
            self.Description = LocalizedText.from_binary(data)
            self.WriteMask = struct.unpack(self._WriteMask_fmt, data.read(self._WriteMask_fmt_size))[0]
            self.UserWriteMask = struct.unpack(self._UserWriteMask_fmt, data.read(self._UserWriteMask_fmt_size))[0]
            self.IsAbstract = struct.unpack(self._IsAbstract_fmt, data.read(self._IsAbstract_fmt_size))[0]
            return data
            
class ViewAttributes(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.SpecifiedAttributes = 0
        self._SpecifiedAttributes_fmt = '<I'
        self._SpecifiedAttributes_fmt_size = 4
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self._WriteMask_fmt = '<I'
        self._WriteMask_fmt_size = 4
        self.UserWriteMask = 0
        self._UserWriteMask_fmt = '<I'
        self._UserWriteMask_fmt_size = 4
        self.ContainsNoLoops = 0
        self._ContainsNoLoops_fmt = '<?'
        self._ContainsNoLoops_fmt_size = 1
        self.EventNotifier = 0
        self._EventNotifier_fmt = '<B'
        self._EventNotifier_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack(self._SpecifiedAttributes_fmt, self.SpecifiedAttributes))
        tmp.append(self.DisplayName.to_binary())
        tmp.append(self.Description.to_binary())
        tmp.append(struct.pack(self._WriteMask_fmt, self.WriteMask))
        tmp.append(struct.pack(self._UserWriteMask_fmt, self.UserWriteMask))
        tmp.append(struct.pack(self._ContainsNoLoops_fmt, self.ContainsNoLoops))
        tmp.append(struct.pack(self._EventNotifier_fmt, self.EventNotifier))
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.SpecifiedAttributes = struct.unpack(self._SpecifiedAttributes_fmt, data.read(self._SpecifiedAttributes_fmt_size))[0]
            self.DisplayName = LocalizedText.from_binary(data)
            self.Description = LocalizedText.from_binary(data)
            self.WriteMask = struct.unpack(self._WriteMask_fmt, data.read(self._WriteMask_fmt_size))[0]
            self.UserWriteMask = struct.unpack(self._UserWriteMask_fmt, data.read(self._UserWriteMask_fmt_size))[0]
            self.ContainsNoLoops = struct.unpack(self._ContainsNoLoops_fmt, data.read(self._ContainsNoLoops_fmt_size))[0]
            self.EventNotifier = struct.unpack(self._EventNotifier_fmt, data.read(self._EventNotifier_fmt_size))[0]
            return data
            
class AddNodesItem(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.ParentNodeId = ExpandedNodeId()
        self.ReferenceTypeId = NodeId()
        self.RequestedNewNodeId = ExpandedNodeId()
        self.BrowseName = QualifiedName()
        self.NodeClass = 0
        self._NodeClass_fmt = '<I'
        self._NodeClass_fmt_size = 4
        self.NodeAttributes = ExtensionObject()
        self.TypeDefinition = ExpandedNodeId()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.ParentNodeId.to_binary())
        tmp.append(self.ReferenceTypeId.to_binary())
        tmp.append(self.RequestedNewNodeId.to_binary())
        tmp.append(self.BrowseName.to_binary())
        tmp.append(struct.pack(self._NodeClass_fmt, self.NodeClass))
        tmp.append(self.NodeAttributes.to_binary())
        tmp.append(self.TypeDefinition.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.ParentNodeId = ExpandedNodeId.from_binary(data)
            self.ReferenceTypeId = NodeId.from_binary(data)
            self.RequestedNewNodeId = ExpandedNodeId.from_binary(data)
            self.BrowseName = QualifiedName.from_binary(data)
            self.NodeClass = struct.unpack(self._NodeClass_fmt, data.read(self._NodeClass_fmt_size))[0]
            self.NodeAttributes = ExtensionObject.from_binary(data)
            self.TypeDefinition = ExpandedNodeId.from_binary(data)
            return data
            
class AddNodesResult(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.StatusCode = StatusCode()
        self.AddedNodeId = NodeId()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.StatusCode.to_binary())
        tmp.append(self.AddedNodeId.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.StatusCode = StatusCode.from_binary(data)
            self.AddedNodeId = NodeId.from_binary(data)
            return data
            
class AddNodesParameters(object):
    def __init__(self):
        self.NodesToAdd = []
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack('<i', len(self.NodesToAdd)))
        for i in NodesToAdd:
            tmp.append(self.NodesToAdd.to_binary())
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
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
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
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(struct.pack('<i', len(self.Results)))
        for i in Results:
            tmp.append(self.Results.to_binary())
        tmp.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for i in DiagnosticInfos:
            tmp.append(self.DiagnosticInfos.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
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
        self.TypeId = ExpandedNodeId()
        self.SourceNodeId = NodeId()
        self.ReferenceTypeId = NodeId()
        self.IsForward = 0
        self._IsForward_fmt = '<?'
        self._IsForward_fmt_size = 1
        self.TargetServerUri = ''
        self._TargetServerUri_fmt = '<s'
        self._TargetServerUri_fmt_size = 1
        self.TargetNodeId = ExpandedNodeId()
        self.TargetNodeClass = NodeClass()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.SourceNodeId.to_binary())
        tmp.append(self.ReferenceTypeId.to_binary())
        tmp.append(struct.pack(self._IsForward_fmt, self.IsForward))
        tmp.append(struct.pack('<i', len(self.TargetServerUri)))
        tmp.append(struct.pack('<{}s'.format(len(self.TargetServerUri)), self.TargetServerUri.encode()))
        tmp.append(self.TargetNodeId.to_binary())
        tmp.append(self.TargetNodeClass.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.SourceNodeId = NodeId.from_binary(data)
            self.ReferenceTypeId = NodeId.from_binary(data)
            self.IsForward = struct.unpack(self._IsForward_fmt, data.read(self._IsForward_fmt_size))[0]
            slength = struct.unpack('<i', data.red(1))
            self.TargetServerUri = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.TargetServerUri = struct.unpack(self._TargetServerUri_fmt, data.read(self._TargetServerUri_fmt_size))[0]
            self.TargetNodeId = ExpandedNodeId.from_binary(data)
            self.TargetNodeClass = NodeClass.from_binary(data)
            return data
            
class AddReferencesParameters(object):
    def __init__(self):
        self.ReferencesToAdd = []
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack('<i', len(self.ReferencesToAdd)))
        for i in ReferencesToAdd:
            tmp.append(self.ReferencesToAdd.to_binary())
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
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = AddReferencesParameters.from_binary(data)
            return data
            
class AddReferencesResult(object):
    def __init__(self):
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack('<i', len(self.Results)))
        for i in Results:
            tmp.append(self.Results.to_binary())
        tmp.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for i in DiagnosticInfos:
            tmp.append(self.DiagnosticInfos.to_binary())
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
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            self.Parameters = AddReferencesResult.from_binary(data)
            return data
            
class DeleteNodesItem(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.NodeId = NodeId()
        self.DeleteTargetReferences = 0
        self._DeleteTargetReferences_fmt = '<?'
        self._DeleteTargetReferences_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.NodeId.to_binary())
        tmp.append(struct.pack(self._DeleteTargetReferences_fmt, self.DeleteTargetReferences))
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.NodeId = NodeId.from_binary(data)
            self.DeleteTargetReferences = struct.unpack(self._DeleteTargetReferences_fmt, data.read(self._DeleteTargetReferences_fmt_size))[0]
            return data
            
class DeleteNodesParameters(object):
    def __init__(self):
        self.NodesToDelete = []
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack('<i', len(self.NodesToDelete)))
        for i in NodesToDelete:
            tmp.append(self.NodesToDelete.to_binary())
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
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = DeleteNodesParameters.from_binary(data)
            return data
            
class DeleteNodesResult(object):
    def __init__(self):
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack('<i', len(self.Results)))
        for i in Results:
            tmp.append(self.Results.to_binary())
        tmp.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for i in DiagnosticInfos:
            tmp.append(self.DiagnosticInfos.to_binary())
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
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            self.Parameters = DeleteNodesResult.from_binary(data)
            return data
            
class DeleteReferencesItem(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.SourceNodeId = NodeId()
        self.ReferenceTypeId = NodeId()
        self.IsForward = 0
        self._IsForward_fmt = '<?'
        self._IsForward_fmt_size = 1
        self.TargetNodeId = ExpandedNodeId()
        self.DeleteBidirectional = 0
        self._DeleteBidirectional_fmt = '<?'
        self._DeleteBidirectional_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.SourceNodeId.to_binary())
        tmp.append(self.ReferenceTypeId.to_binary())
        tmp.append(struct.pack(self._IsForward_fmt, self.IsForward))
        tmp.append(self.TargetNodeId.to_binary())
        tmp.append(struct.pack(self._DeleteBidirectional_fmt, self.DeleteBidirectional))
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.SourceNodeId = NodeId.from_binary(data)
            self.ReferenceTypeId = NodeId.from_binary(data)
            self.IsForward = struct.unpack(self._IsForward_fmt, data.read(self._IsForward_fmt_size))[0]
            self.TargetNodeId = ExpandedNodeId.from_binary(data)
            self.DeleteBidirectional = struct.unpack(self._DeleteBidirectional_fmt, data.read(self._DeleteBidirectional_fmt_size))[0]
            return data
            
class DeleteReferencesParameters(object):
    def __init__(self):
        self.ReferencesToDelete = []
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack('<i', len(self.ReferencesToDelete)))
        for i in ReferencesToDelete:
            tmp.append(self.ReferencesToDelete.to_binary())
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
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = DeleteReferencesParameters.from_binary(data)
            return data
            
class DeleteReferencesResult(object):
    def __init__(self):
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack('<i', len(self.Results)))
        for i in Results:
            tmp.append(self.Results.to_binary())
        tmp.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for i in DiagnosticInfos:
            tmp.append(self.DiagnosticInfos.to_binary())
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
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            self.Parameters = DeleteReferencesResult.from_binary(data)
            return data
            
class ViewDescription(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.ViewId = NodeId()
        self.Timestamp = 0
        self.ViewVersion = 0
        self._ViewVersion_fmt = '<I'
        self._ViewVersion_fmt_size = 4
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.ViewId.to_binary())
        tmp.append(self.Timestamp.to_binary())
        tmp.append(struct.pack(self._ViewVersion_fmt, self.ViewVersion))
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.ViewId = NodeId.from_binary(data)
            self.Timestamp = DateTime.from_binary(data)
            self.ViewVersion = struct.unpack(self._ViewVersion_fmt, data.read(self._ViewVersion_fmt_size))[0]
            return data
            
class BrowseDescription(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.NodeId = NodeId()
        self.BrowseDirection = 0
        self._BrowseDirection_fmt = '<I'
        self._BrowseDirection_fmt_size = 4
        self.ReferenceTypeId = NodeId()
        self.IncludeSubtypes = 0
        self._IncludeSubtypes_fmt = '<?'
        self._IncludeSubtypes_fmt_size = 1
        self.NodeClassMask = 0
        self._NodeClassMask_fmt = '<I'
        self._NodeClassMask_fmt_size = 4
        self.ResultMask = 0
        self._ResultMask_fmt = '<I'
        self._ResultMask_fmt_size = 4
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.NodeId.to_binary())
        tmp.append(struct.pack(self._BrowseDirection_fmt, self.BrowseDirection))
        tmp.append(self.ReferenceTypeId.to_binary())
        tmp.append(struct.pack(self._IncludeSubtypes_fmt, self.IncludeSubtypes))
        tmp.append(struct.pack(self._NodeClassMask_fmt, self.NodeClassMask))
        tmp.append(struct.pack(self._ResultMask_fmt, self.ResultMask))
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.NodeId = NodeId.from_binary(data)
            self.BrowseDirection = struct.unpack(self._BrowseDirection_fmt, data.read(self._BrowseDirection_fmt_size))[0]
            self.ReferenceTypeId = NodeId.from_binary(data)
            self.IncludeSubtypes = struct.unpack(self._IncludeSubtypes_fmt, data.read(self._IncludeSubtypes_fmt_size))[0]
            self.NodeClassMask = struct.unpack(self._NodeClassMask_fmt, data.read(self._NodeClassMask_fmt_size))[0]
            self.ResultMask = struct.unpack(self._ResultMask_fmt, data.read(self._ResultMask_fmt_size))[0]
            return data
            
class ReferenceDescription(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.ReferenceTypeId = NodeId()
        self.IsForward = 0
        self._IsForward_fmt = '<?'
        self._IsForward_fmt_size = 1
        self.NodeId = ExpandedNodeId()
        self.BrowseName = QualifiedName()
        self.DisplayName = LocalizedText()
        self.NodeClass = 0
        self._NodeClass_fmt = '<I'
        self._NodeClass_fmt_size = 4
        self.TypeDefinition = ExpandedNodeId()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.ReferenceTypeId.to_binary())
        tmp.append(struct.pack(self._IsForward_fmt, self.IsForward))
        tmp.append(self.NodeId.to_binary())
        tmp.append(self.BrowseName.to_binary())
        tmp.append(self.DisplayName.to_binary())
        tmp.append(struct.pack(self._NodeClass_fmt, self.NodeClass))
        tmp.append(self.TypeDefinition.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.ReferenceTypeId = NodeId.from_binary(data)
            self.IsForward = struct.unpack(self._IsForward_fmt, data.read(self._IsForward_fmt_size))[0]
            self.NodeId = ExpandedNodeId.from_binary(data)
            self.BrowseName = QualifiedName.from_binary(data)
            self.DisplayName = LocalizedText.from_binary(data)
            self.NodeClass = struct.unpack(self._NodeClass_fmt, data.read(self._NodeClass_fmt_size))[0]
            self.TypeDefinition = ExpandedNodeId.from_binary(data)
            return data
            
class BrowseResult(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.StatusCode = StatusCode()
        self.ContinuationPoint = ByteString()
        self.References = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.StatusCode.to_binary())
        tmp.append(self.ContinuationPoint.to_binary())
        tmp.append(struct.pack('<i', len(self.References)))
        for i in References:
            tmp.append(self.References.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
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
        self._RequestedMaxReferencesPerNode_fmt = '<I'
        self._RequestedMaxReferencesPerNode_fmt_size = 4
        self.NodesToBrowse = []
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(self.View.to_binary())
        tmp.append(struct.pack(self._RequestedMaxReferencesPerNode_fmt, self.RequestedMaxReferencesPerNode))
        tmp.append(struct.pack('<i', len(self.NodesToBrowse)))
        for i in NodesToBrowse:
            tmp.append(self.NodesToBrowse.to_binary())
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.View = ViewDescription.from_binary(data)
            self.RequestedMaxReferencesPerNode = struct.unpack(self._RequestedMaxReferencesPerNode_fmt, data.read(self._RequestedMaxReferencesPerNode_fmt_size))[0]
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
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
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
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(struct.pack('<i', len(self.Results)))
        for i in Results:
            tmp.append(self.Results.to_binary())
        tmp.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for i in DiagnosticInfos:
            tmp.append(self.DiagnosticInfos.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
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
        self._ReleaseContinuationPoints_fmt = '<?'
        self._ReleaseContinuationPoints_fmt_size = 1
        self.ContinuationPoints = []
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack(self._ReleaseContinuationPoints_fmt, self.ReleaseContinuationPoints))
        tmp.append(struct.pack('<i', len(self.ContinuationPoints)))
        for i in ContinuationPoints:
            tmp.append(self.ContinuationPoints.to_binary())
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.ReleaseContinuationPoints = struct.unpack(self._ReleaseContinuationPoints_fmt, data.read(self._ReleaseContinuationPoints_fmt_size))[0]
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
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = BrowseNextParameters.from_binary(data)
            return data
            
class BrowseNextResult(object):
    def __init__(self):
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack('<i', len(self.Results)))
        for i in Results:
            tmp.append(self.Results.to_binary())
        tmp.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for i in DiagnosticInfos:
            tmp.append(self.DiagnosticInfos.to_binary())
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
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            self.Parameters = BrowseNextResult.from_binary(data)
            return data
            
class RelativePathElement(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.ReferenceTypeId = NodeId()
        self.IsInverse = 0
        self._IsInverse_fmt = '<?'
        self._IsInverse_fmt_size = 1
        self.IncludeSubtypes = 0
        self._IncludeSubtypes_fmt = '<?'
        self._IncludeSubtypes_fmt_size = 1
        self.TargetName = QualifiedName()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.ReferenceTypeId.to_binary())
        tmp.append(struct.pack(self._IsInverse_fmt, self.IsInverse))
        tmp.append(struct.pack(self._IncludeSubtypes_fmt, self.IncludeSubtypes))
        tmp.append(self.TargetName.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.ReferenceTypeId = NodeId.from_binary(data)
            self.IsInverse = struct.unpack(self._IsInverse_fmt, data.read(self._IsInverse_fmt_size))[0]
            self.IncludeSubtypes = struct.unpack(self._IncludeSubtypes_fmt, data.read(self._IncludeSubtypes_fmt_size))[0]
            self.TargetName = QualifiedName.from_binary(data)
            return data
            
class RelativePath(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.Elements = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack('<i', len(self.Elements)))
        for i in Elements:
            tmp.append(self.Elements.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.Elements = RelativePathElement.from_binary(data)
            return data
            
class BrowsePath(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.StartingNode = NodeId()
        self.RelativePath = RelativePath()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.StartingNode.to_binary())
        tmp.append(self.RelativePath.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.StartingNode = NodeId.from_binary(data)
            self.RelativePath = RelativePath.from_binary(data)
            return data
            
class BrowsePathTarget(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.TargetId = ExpandedNodeId()
        self.RemainingPathIndex = 0
        self._RemainingPathIndex_fmt = '<I'
        self._RemainingPathIndex_fmt_size = 4
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.TargetId.to_binary())
        tmp.append(struct.pack(self._RemainingPathIndex_fmt, self.RemainingPathIndex))
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.TargetId = ExpandedNodeId.from_binary(data)
            self.RemainingPathIndex = struct.unpack(self._RemainingPathIndex_fmt, data.read(self._RemainingPathIndex_fmt_size))[0]
            return data
            
class BrowsePathResult(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.StatusCode = StatusCode()
        self.Targets = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.StatusCode.to_binary())
        tmp.append(struct.pack('<i', len(self.Targets)))
        for i in Targets:
            tmp.append(self.Targets.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
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
        tmp = packet
        tmp.append(struct.pack('<i', len(self.BrowsePaths)))
        for i in BrowsePaths:
            tmp.append(self.BrowsePaths.to_binary())
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
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = TranslateBrowsePathsToNodeIdsParameters.from_binary(data)
            return data
            
class TranslateBrowsePathsToNodeIdsResult(object):
    def __init__(self):
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack('<i', len(self.Results)))
        for i in Results:
            tmp.append(self.Results.to_binary())
        tmp.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for i in DiagnosticInfos:
            tmp.append(self.DiagnosticInfos.to_binary())
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
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            self.Parameters = TranslateBrowsePathsToNodeIdsResult.from_binary(data)
            return data
            
class RegisterNodesParameters(object):
    def __init__(self):
        self.NodesToRegister = []
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack('<i', len(self.NodesToRegister)))
        for i in NodesToRegister:
            tmp.append(self.NodesToRegister.to_binary())
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
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = RegisterNodesParameters.from_binary(data)
            return data
            
class RegisterNodesResult(object):
    def __init__(self):
        self.RegisteredNodeIds = []
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack('<i', len(self.RegisteredNodeIds)))
        for i in RegisteredNodeIds:
            tmp.append(self.RegisteredNodeIds.to_binary())
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
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            self.Parameters = RegisterNodesResult.from_binary(data)
            return data
            
class UnregisterNodesParameters(object):
    def __init__(self):
        self.NodesToUnregister = []
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack('<i', len(self.NodesToUnregister)))
        for i in NodesToUnregister:
            tmp.append(self.NodesToUnregister.to_binary())
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
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = UnregisterNodesParameters.from_binary(data)
            return data
            
class UnregisterNodesResponse(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.UnregisterNodesResponse_Encoding_DefaultBinary, NodeIdType.FourByte)
        self.ResponseHeader = ResponseHeader()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.ResponseHeader.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            return data
            
class EndpointConfiguration(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.OperationTimeout = 0
        self._OperationTimeout_fmt = '<i'
        self._OperationTimeout_fmt_size = 4
        self.UseBinaryEncoding = 0
        self._UseBinaryEncoding_fmt = '<?'
        self._UseBinaryEncoding_fmt_size = 1
        self.MaxStringLength = 0
        self._MaxStringLength_fmt = '<i'
        self._MaxStringLength_fmt_size = 4
        self.MaxByteStringLength = 0
        self._MaxByteStringLength_fmt = '<i'
        self._MaxByteStringLength_fmt_size = 4
        self.MaxArrayLength = 0
        self._MaxArrayLength_fmt = '<i'
        self._MaxArrayLength_fmt_size = 4
        self.MaxMessageSize = 0
        self._MaxMessageSize_fmt = '<i'
        self._MaxMessageSize_fmt_size = 4
        self.MaxBufferSize = 0
        self._MaxBufferSize_fmt = '<i'
        self._MaxBufferSize_fmt_size = 4
        self.ChannelLifetime = 0
        self._ChannelLifetime_fmt = '<i'
        self._ChannelLifetime_fmt_size = 4
        self.SecurityTokenLifetime = 0
        self._SecurityTokenLifetime_fmt = '<i'
        self._SecurityTokenLifetime_fmt_size = 4
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack(self._OperationTimeout_fmt, self.OperationTimeout))
        tmp.append(struct.pack(self._UseBinaryEncoding_fmt, self.UseBinaryEncoding))
        tmp.append(struct.pack(self._MaxStringLength_fmt, self.MaxStringLength))
        tmp.append(struct.pack(self._MaxByteStringLength_fmt, self.MaxByteStringLength))
        tmp.append(struct.pack(self._MaxArrayLength_fmt, self.MaxArrayLength))
        tmp.append(struct.pack(self._MaxMessageSize_fmt, self.MaxMessageSize))
        tmp.append(struct.pack(self._MaxBufferSize_fmt, self.MaxBufferSize))
        tmp.append(struct.pack(self._ChannelLifetime_fmt, self.ChannelLifetime))
        tmp.append(struct.pack(self._SecurityTokenLifetime_fmt, self.SecurityTokenLifetime))
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.OperationTimeout = struct.unpack(self._OperationTimeout_fmt, data.read(self._OperationTimeout_fmt_size))[0]
            self.UseBinaryEncoding = struct.unpack(self._UseBinaryEncoding_fmt, data.read(self._UseBinaryEncoding_fmt_size))[0]
            self.MaxStringLength = struct.unpack(self._MaxStringLength_fmt, data.read(self._MaxStringLength_fmt_size))[0]
            self.MaxByteStringLength = struct.unpack(self._MaxByteStringLength_fmt, data.read(self._MaxByteStringLength_fmt_size))[0]
            self.MaxArrayLength = struct.unpack(self._MaxArrayLength_fmt, data.read(self._MaxArrayLength_fmt_size))[0]
            self.MaxMessageSize = struct.unpack(self._MaxMessageSize_fmt, data.read(self._MaxMessageSize_fmt_size))[0]
            self.MaxBufferSize = struct.unpack(self._MaxBufferSize_fmt, data.read(self._MaxBufferSize_fmt_size))[0]
            self.ChannelLifetime = struct.unpack(self._ChannelLifetime_fmt, data.read(self._ChannelLifetime_fmt_size))[0]
            self.SecurityTokenLifetime = struct.unpack(self._SecurityTokenLifetime_fmt, data.read(self._SecurityTokenLifetime_fmt_size))[0]
            return data
            
class SupportedProfile(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.OrganizationUri = ''
        self._OrganizationUri_fmt = '<s'
        self._OrganizationUri_fmt_size = 1
        self.ProfileId = ''
        self._ProfileId_fmt = '<s'
        self._ProfileId_fmt_size = 1
        self.ComplianceTool = ''
        self._ComplianceTool_fmt = '<s'
        self._ComplianceTool_fmt_size = 1
        self.ComplianceDate = 0
        self.ComplianceLevel = 0
        self._ComplianceLevel_fmt = '<I'
        self._ComplianceLevel_fmt_size = 4
        self.UnsupportedUnitIds = []
        self._UnsupportedUnitIds_fmt = '<s'
        self._UnsupportedUnitIds_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack('<i', len(self.OrganizationUri)))
        tmp.append(struct.pack('<{}s'.format(len(self.OrganizationUri)), self.OrganizationUri.encode()))
        tmp.append(struct.pack('<i', len(self.ProfileId)))
        tmp.append(struct.pack('<{}s'.format(len(self.ProfileId)), self.ProfileId.encode()))
        tmp.append(struct.pack('<i', len(self.ComplianceTool)))
        tmp.append(struct.pack('<{}s'.format(len(self.ComplianceTool)), self.ComplianceTool.encode()))
        tmp.append(self.ComplianceDate.to_binary())
        tmp.append(struct.pack(self._ComplianceLevel_fmt, self.ComplianceLevel))
        tmp.append(struct.pack('<i', len(self.UnsupportedUnitIds)))
        for i in UnsupportedUnitIds:
            tmp.append(struct.pack('<i', len(self.UnsupportedUnitIds)))
            tmp.append(struct.pack('<{}s'.format(len(self.UnsupportedUnitIds)), self.UnsupportedUnitIds.encode()))
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            slength = struct.unpack('<i', data.red(1))
            self.OrganizationUri = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.OrganizationUri = struct.unpack(self._OrganizationUri_fmt, data.read(self._OrganizationUri_fmt_size))[0]
            slength = struct.unpack('<i', data.red(1))
            self.ProfileId = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.ProfileId = struct.unpack(self._ProfileId_fmt, data.read(self._ProfileId_fmt_size))[0]
            slength = struct.unpack('<i', data.red(1))
            self.ComplianceTool = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.ComplianceTool = struct.unpack(self._ComplianceTool_fmt, data.read(self._ComplianceTool_fmt_size))[0]
            self.ComplianceDate = DateTime.from_binary(data)
            self.ComplianceLevel = struct.unpack(self._ComplianceLevel_fmt, data.read(self._ComplianceLevel_fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    slength = struct.unpack('<i', data.red(1))
                    self.UnsupportedUnitIds = struct.unpack('<{}s'.format(slength), data.read(slength))
                    self.UnsupportedUnitIds = struct.unpack(self._UnsupportedUnitIds_fmt, data.read(self._UnsupportedUnitIds_fmt_size))[0]
            return data
            
class SoftwareCertificate(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.ProductName = ''
        self._ProductName_fmt = '<s'
        self._ProductName_fmt_size = 1
        self.ProductUri = ''
        self._ProductUri_fmt = '<s'
        self._ProductUri_fmt_size = 1
        self.VendorName = ''
        self._VendorName_fmt = '<s'
        self._VendorName_fmt_size = 1
        self.VendorProductCertificate = ByteString()
        self.SoftwareVersion = ''
        self._SoftwareVersion_fmt = '<s'
        self._SoftwareVersion_fmt_size = 1
        self.BuildNumber = ''
        self._BuildNumber_fmt = '<s'
        self._BuildNumber_fmt_size = 1
        self.BuildDate = 0
        self.IssuedBy = ''
        self._IssuedBy_fmt = '<s'
        self._IssuedBy_fmt_size = 1
        self.IssueDate = 0
        self.SupportedProfiles = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack('<i', len(self.ProductName)))
        tmp.append(struct.pack('<{}s'.format(len(self.ProductName)), self.ProductName.encode()))
        tmp.append(struct.pack('<i', len(self.ProductUri)))
        tmp.append(struct.pack('<{}s'.format(len(self.ProductUri)), self.ProductUri.encode()))
        tmp.append(struct.pack('<i', len(self.VendorName)))
        tmp.append(struct.pack('<{}s'.format(len(self.VendorName)), self.VendorName.encode()))
        tmp.append(self.VendorProductCertificate.to_binary())
        tmp.append(struct.pack('<i', len(self.SoftwareVersion)))
        tmp.append(struct.pack('<{}s'.format(len(self.SoftwareVersion)), self.SoftwareVersion.encode()))
        tmp.append(struct.pack('<i', len(self.BuildNumber)))
        tmp.append(struct.pack('<{}s'.format(len(self.BuildNumber)), self.BuildNumber.encode()))
        tmp.append(self.BuildDate.to_binary())
        tmp.append(struct.pack('<i', len(self.IssuedBy)))
        tmp.append(struct.pack('<{}s'.format(len(self.IssuedBy)), self.IssuedBy.encode()))
        tmp.append(self.IssueDate.to_binary())
        tmp.append(struct.pack('<i', len(self.SupportedProfiles)))
        for i in SupportedProfiles:
            tmp.append(self.SupportedProfiles.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            slength = struct.unpack('<i', data.red(1))
            self.ProductName = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.ProductName = struct.unpack(self._ProductName_fmt, data.read(self._ProductName_fmt_size))[0]
            slength = struct.unpack('<i', data.red(1))
            self.ProductUri = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.ProductUri = struct.unpack(self._ProductUri_fmt, data.read(self._ProductUri_fmt_size))[0]
            slength = struct.unpack('<i', data.red(1))
            self.VendorName = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.VendorName = struct.unpack(self._VendorName_fmt, data.read(self._VendorName_fmt_size))[0]
            self.VendorProductCertificate = ByteString.from_binary(data)
            slength = struct.unpack('<i', data.red(1))
            self.SoftwareVersion = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.SoftwareVersion = struct.unpack(self._SoftwareVersion_fmt, data.read(self._SoftwareVersion_fmt_size))[0]
            slength = struct.unpack('<i', data.red(1))
            self.BuildNumber = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.BuildNumber = struct.unpack(self._BuildNumber_fmt, data.read(self._BuildNumber_fmt_size))[0]
            self.BuildDate = DateTime.from_binary(data)
            slength = struct.unpack('<i', data.red(1))
            self.IssuedBy = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.IssuedBy = struct.unpack(self._IssuedBy_fmt, data.read(self._IssuedBy_fmt_size))[0]
            self.IssueDate = DateTime.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.SupportedProfiles = SupportedProfile.from_binary(data)
            return data
            
class QueryDataDescription(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.RelativePath = RelativePath()
        self.AttributeId = 0
        self._AttributeId_fmt = '<I'
        self._AttributeId_fmt_size = 4
        self.IndexRange = ''
        self._IndexRange_fmt = '<s'
        self._IndexRange_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.RelativePath.to_binary())
        tmp.append(struct.pack(self._AttributeId_fmt, self.AttributeId))
        tmp.append(struct.pack('<i', len(self.IndexRange)))
        tmp.append(struct.pack('<{}s'.format(len(self.IndexRange)), self.IndexRange.encode()))
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.RelativePath = RelativePath.from_binary(data)
            self.AttributeId = struct.unpack(self._AttributeId_fmt, data.read(self._AttributeId_fmt_size))[0]
            slength = struct.unpack('<i', data.red(1))
            self.IndexRange = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.IndexRange = struct.unpack(self._IndexRange_fmt, data.read(self._IndexRange_fmt_size))[0]
            return data
            
class NodeTypeDescription(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.TypeDefinitionNode = ExpandedNodeId()
        self.IncludeSubTypes = 0
        self._IncludeSubTypes_fmt = '<?'
        self._IncludeSubTypes_fmt_size = 1
        self.DataToReturn = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.TypeDefinitionNode.to_binary())
        tmp.append(struct.pack(self._IncludeSubTypes_fmt, self.IncludeSubTypes))
        tmp.append(struct.pack('<i', len(self.DataToReturn)))
        for i in DataToReturn:
            tmp.append(self.DataToReturn.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.TypeDefinitionNode = ExpandedNodeId.from_binary(data)
            self.IncludeSubTypes = struct.unpack(self._IncludeSubTypes_fmt, data.read(self._IncludeSubTypes_fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.DataToReturn = QueryDataDescription.from_binary(data)
            return data
            
class QueryDataSet(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.NodeId = ExpandedNodeId()
        self.TypeDefinitionNode = ExpandedNodeId()
        self.Values = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.NodeId.to_binary())
        tmp.append(self.TypeDefinitionNode.to_binary())
        tmp.append(struct.pack('<i', len(self.Values)))
        for i in Values:
            tmp.append(self.Values.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.NodeId = ExpandedNodeId.from_binary(data)
            self.TypeDefinitionNode = ExpandedNodeId.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.Values = Variant.from_binary(data)
            return data
            
class NodeReference(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.NodeId = NodeId()
        self.ReferenceTypeId = NodeId()
        self.IsForward = 0
        self._IsForward_fmt = '<?'
        self._IsForward_fmt_size = 1
        self.ReferencedNodeIds = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.NodeId.to_binary())
        tmp.append(self.ReferenceTypeId.to_binary())
        tmp.append(struct.pack(self._IsForward_fmt, self.IsForward))
        tmp.append(struct.pack('<i', len(self.ReferencedNodeIds)))
        for i in ReferencedNodeIds:
            tmp.append(self.ReferencedNodeIds.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.NodeId = NodeId.from_binary(data)
            self.ReferenceTypeId = NodeId.from_binary(data)
            self.IsForward = struct.unpack(self._IsForward_fmt, data.read(self._IsForward_fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.ReferencedNodeIds = NodeId.from_binary(data)
            return data
            
class ContentFilterElement(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.FilterOperator = 0
        self._FilterOperator_fmt = '<I'
        self._FilterOperator_fmt_size = 4
        self.FilterOperands = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack(self._FilterOperator_fmt, self.FilterOperator))
        tmp.append(struct.pack('<i', len(self.FilterOperands)))
        for i in FilterOperands:
            tmp.append(self.FilterOperands.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.FilterOperator = struct.unpack(self._FilterOperator_fmt, data.read(self._FilterOperator_fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.FilterOperands = ExtensionObject.from_binary(data)
            return data
            
class ContentFilter(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.Elements = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack('<i', len(self.Elements)))
        for i in Elements:
            tmp.append(self.Elements.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.Elements = ContentFilterElement.from_binary(data)
            return data
            
class FilterOperand(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            return data
            
class ElementOperand(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.Index = 0
        self._Index_fmt = '<I'
        self._Index_fmt_size = 4
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack(self._Index_fmt, self.Index))
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.Index = struct.unpack(self._Index_fmt, data.read(self._Index_fmt_size))[0]
            return data
            
class LiteralOperand(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.Value = Variant()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.Value.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.Value = Variant.from_binary(data)
            return data
            
class AttributeOperand(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.NodeId = NodeId()
        self.Alias = ''
        self._Alias_fmt = '<s'
        self._Alias_fmt_size = 1
        self.BrowsePath = RelativePath()
        self.AttributeId = 0
        self._AttributeId_fmt = '<I'
        self._AttributeId_fmt_size = 4
        self.IndexRange = ''
        self._IndexRange_fmt = '<s'
        self._IndexRange_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.NodeId.to_binary())
        tmp.append(struct.pack('<i', len(self.Alias)))
        tmp.append(struct.pack('<{}s'.format(len(self.Alias)), self.Alias.encode()))
        tmp.append(self.BrowsePath.to_binary())
        tmp.append(struct.pack(self._AttributeId_fmt, self.AttributeId))
        tmp.append(struct.pack('<i', len(self.IndexRange)))
        tmp.append(struct.pack('<{}s'.format(len(self.IndexRange)), self.IndexRange.encode()))
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.NodeId = NodeId.from_binary(data)
            slength = struct.unpack('<i', data.red(1))
            self.Alias = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.Alias = struct.unpack(self._Alias_fmt, data.read(self._Alias_fmt_size))[0]
            self.BrowsePath = RelativePath.from_binary(data)
            self.AttributeId = struct.unpack(self._AttributeId_fmt, data.read(self._AttributeId_fmt_size))[0]
            slength = struct.unpack('<i', data.red(1))
            self.IndexRange = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.IndexRange = struct.unpack(self._IndexRange_fmt, data.read(self._IndexRange_fmt_size))[0]
            return data
            
class SimpleAttributeOperand(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.TypeDefinitionId = NodeId()
        self.BrowsePath = []
        self.AttributeId = 0
        self._AttributeId_fmt = '<I'
        self._AttributeId_fmt_size = 4
        self.IndexRange = ''
        self._IndexRange_fmt = '<s'
        self._IndexRange_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.TypeDefinitionId.to_binary())
        tmp.append(struct.pack('<i', len(self.BrowsePath)))
        for i in BrowsePath:
            tmp.append(self.BrowsePath.to_binary())
        tmp.append(struct.pack(self._AttributeId_fmt, self.AttributeId))
        tmp.append(struct.pack('<i', len(self.IndexRange)))
        tmp.append(struct.pack('<{}s'.format(len(self.IndexRange)), self.IndexRange.encode()))
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.TypeDefinitionId = NodeId.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.BrowsePath = QualifiedName.from_binary(data)
            self.AttributeId = struct.unpack(self._AttributeId_fmt, data.read(self._AttributeId_fmt_size))[0]
            slength = struct.unpack('<i', data.red(1))
            self.IndexRange = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.IndexRange = struct.unpack(self._IndexRange_fmt, data.read(self._IndexRange_fmt_size))[0]
            return data
            
class ContentFilterElementResult(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.StatusCode = StatusCode()
        self.OperandStatusCodes = []
        self.OperandDiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.StatusCode.to_binary())
        tmp.append(struct.pack('<i', len(self.OperandStatusCodes)))
        for i in OperandStatusCodes:
            tmp.append(self.OperandStatusCodes.to_binary())
        tmp.append(struct.pack('<i', len(self.OperandDiagnosticInfos)))
        for i in OperandDiagnosticInfos:
            tmp.append(self.OperandDiagnosticInfos.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
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
        self.TypeId = ExpandedNodeId()
        self.ElementResults = []
        self.ElementDiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack('<i', len(self.ElementResults)))
        for i in ElementResults:
            tmp.append(self.ElementResults.to_binary())
        tmp.append(struct.pack('<i', len(self.ElementDiagnosticInfos)))
        for i in ElementDiagnosticInfos:
            tmp.append(self.ElementDiagnosticInfos.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
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
        self.TypeId = ExpandedNodeId()
        self.StatusCode = StatusCode()
        self.DataStatusCodes = []
        self.DataDiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.StatusCode.to_binary())
        tmp.append(struct.pack('<i', len(self.DataStatusCodes)))
        for i in DataStatusCodes:
            tmp.append(self.DataStatusCodes.to_binary())
        tmp.append(struct.pack('<i', len(self.DataDiagnosticInfos)))
        for i in DataDiagnosticInfos:
            tmp.append(self.DataDiagnosticInfos.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
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
        self._MaxDataSetsToReturn_fmt = '<I'
        self._MaxDataSetsToReturn_fmt_size = 4
        self.MaxReferencesToReturn = 0
        self._MaxReferencesToReturn_fmt = '<I'
        self._MaxReferencesToReturn_fmt_size = 4
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(self.View.to_binary())
        tmp.append(struct.pack('<i', len(self.NodeTypes)))
        for i in NodeTypes:
            tmp.append(self.NodeTypes.to_binary())
        tmp.append(self.Filter.to_binary())
        tmp.append(struct.pack(self._MaxDataSetsToReturn_fmt, self.MaxDataSetsToReturn))
        tmp.append(struct.pack(self._MaxReferencesToReturn_fmt, self.MaxReferencesToReturn))
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.View = ViewDescription.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.NodeTypes = NodeTypeDescription.from_binary(data)
            self.Filter = ContentFilter.from_binary(data)
            self.MaxDataSetsToReturn = struct.unpack(self._MaxDataSetsToReturn_fmt, data.read(self._MaxDataSetsToReturn_fmt_size))[0]
            self.MaxReferencesToReturn = struct.unpack(self._MaxReferencesToReturn_fmt, data.read(self._MaxReferencesToReturn_fmt_size))[0]
            return data
            
class QueryFirstRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.QueryFirstRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
        self.RequestHeader = RequestHeader()
        self.Parameters = QueryFirstParameters()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
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
        tmp = packet
        tmp.append(struct.pack('<i', len(self.QueryDataSets)))
        for i in QueryDataSets:
            tmp.append(self.QueryDataSets.to_binary())
        tmp.append(self.ContinuationPoint.to_binary())
        tmp.append(struct.pack('<i', len(self.ParsingResults)))
        for i in ParsingResults:
            tmp.append(self.ParsingResults.to_binary())
        tmp.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for i in DiagnosticInfos:
            tmp.append(self.DiagnosticInfos.to_binary())
        tmp.append(self.FilterResult.to_binary())
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
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            self.Parameters = QueryFirstResult.from_binary(data)
            return data
            
class QueryNextParameters(object):
    def __init__(self):
        self.ReleaseContinuationPoint = 0
        self._ReleaseContinuationPoint_fmt = '<?'
        self._ReleaseContinuationPoint_fmt_size = 1
        self.ContinuationPoint = ByteString()
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack(self._ReleaseContinuationPoint_fmt, self.ReleaseContinuationPoint))
        tmp.append(self.ContinuationPoint.to_binary())
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.ReleaseContinuationPoint = struct.unpack(self._ReleaseContinuationPoint_fmt, data.read(self._ReleaseContinuationPoint_fmt_size))[0]
            self.ContinuationPoint = ByteString.from_binary(data)
            return data
            
class QueryNextRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.QueryNextRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
        self.RequestHeader = RequestHeader()
        self.Parameters = QueryNextParameters()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = QueryNextParameters.from_binary(data)
            return data
            
class QueryNextResult(object):
    def __init__(self):
        self.QueryDataSets = []
        self.RevisedContinuationPoint = ByteString()
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack('<i', len(self.QueryDataSets)))
        for i in QueryDataSets:
            tmp.append(self.QueryDataSets.to_binary())
        tmp.append(self.RevisedContinuationPoint.to_binary())
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
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            self.Parameters = QueryNextResult.from_binary(data)
            return data
            
class ReadValueId(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.NodeId = NodeId()
        self.AttributeId = 0
        self._AttributeId_fmt = '<I'
        self._AttributeId_fmt_size = 4
        self.IndexRange = ''
        self._IndexRange_fmt = '<s'
        self._IndexRange_fmt_size = 1
        self.DataEncoding = QualifiedName()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.NodeId.to_binary())
        tmp.append(struct.pack(self._AttributeId_fmt, self.AttributeId))
        tmp.append(struct.pack('<i', len(self.IndexRange)))
        tmp.append(struct.pack('<{}s'.format(len(self.IndexRange)), self.IndexRange.encode()))
        tmp.append(self.DataEncoding.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.NodeId = NodeId.from_binary(data)
            self.AttributeId = struct.unpack(self._AttributeId_fmt, data.read(self._AttributeId_fmt_size))[0]
            slength = struct.unpack('<i', data.red(1))
            self.IndexRange = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.IndexRange = struct.unpack(self._IndexRange_fmt, data.read(self._IndexRange_fmt_size))[0]
            self.DataEncoding = QualifiedName.from_binary(data)
            return data
            
class ReadParameters(object):
    def __init__(self):
        self.MaxAge = 0
        self._MaxAge_fmt = '<d'
        self._MaxAge_fmt_size = 8
        self.TimestampsToReturn = 0
        self._TimestampsToReturn_fmt = '<I'
        self._TimestampsToReturn_fmt_size = 4
        self.NodesToRead = []
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack(self._MaxAge_fmt, self.MaxAge))
        tmp.append(struct.pack(self._TimestampsToReturn_fmt, self.TimestampsToReturn))
        tmp.append(struct.pack('<i', len(self.NodesToRead)))
        for i in NodesToRead:
            tmp.append(self.NodesToRead.to_binary())
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.MaxAge = struct.unpack(self._MaxAge_fmt, data.read(self._MaxAge_fmt_size))[0]
            self.TimestampsToReturn = struct.unpack(self._TimestampsToReturn_fmt, data.read(self._TimestampsToReturn_fmt_size))[0]
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
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = ReadParameters.from_binary(data)
            return data
            
class ReadResult(object):
    def __init__(self):
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack('<i', len(self.Results)))
        for i in Results:
            tmp.append(self.Results.to_binary())
        tmp.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for i in DiagnosticInfos:
            tmp.append(self.DiagnosticInfos.to_binary())
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
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            self.Parameters = ReadResult.from_binary(data)
            return data
            
class HistoryReadValueId(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.NodeId = NodeId()
        self.IndexRange = ''
        self._IndexRange_fmt = '<s'
        self._IndexRange_fmt_size = 1
        self.DataEncoding = QualifiedName()
        self.ContinuationPoint = ByteString()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.NodeId.to_binary())
        tmp.append(struct.pack('<i', len(self.IndexRange)))
        tmp.append(struct.pack('<{}s'.format(len(self.IndexRange)), self.IndexRange.encode()))
        tmp.append(self.DataEncoding.to_binary())
        tmp.append(self.ContinuationPoint.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.NodeId = NodeId.from_binary(data)
            slength = struct.unpack('<i', data.red(1))
            self.IndexRange = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.IndexRange = struct.unpack(self._IndexRange_fmt, data.read(self._IndexRange_fmt_size))[0]
            self.DataEncoding = QualifiedName.from_binary(data)
            self.ContinuationPoint = ByteString.from_binary(data)
            return data
            
class HistoryReadResult(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.StatusCode = StatusCode()
        self.ContinuationPoint = ByteString()
        self.HistoryData = ExtensionObject()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.StatusCode.to_binary())
        tmp.append(self.ContinuationPoint.to_binary())
        tmp.append(self.HistoryData.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.StatusCode = StatusCode.from_binary(data)
            self.ContinuationPoint = ByteString.from_binary(data)
            self.HistoryData = ExtensionObject.from_binary(data)
            return data
            
class HistoryReadDetails(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            return data
            
class ReadEventDetails(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.NumValuesPerNode = 0
        self._NumValuesPerNode_fmt = '<I'
        self._NumValuesPerNode_fmt_size = 4
        self.StartTime = 0
        self.EndTime = 0
        self.Filter = EventFilter()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack(self._NumValuesPerNode_fmt, self.NumValuesPerNode))
        tmp.append(self.StartTime.to_binary())
        tmp.append(self.EndTime.to_binary())
        tmp.append(self.Filter.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.NumValuesPerNode = struct.unpack(self._NumValuesPerNode_fmt, data.read(self._NumValuesPerNode_fmt_size))[0]
            self.StartTime = DateTime.from_binary(data)
            self.EndTime = DateTime.from_binary(data)
            self.Filter = EventFilter.from_binary(data)
            return data
            
class ReadRawModifiedDetails(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.IsReadModified = 0
        self._IsReadModified_fmt = '<?'
        self._IsReadModified_fmt_size = 1
        self.StartTime = 0
        self.EndTime = 0
        self.NumValuesPerNode = 0
        self._NumValuesPerNode_fmt = '<I'
        self._NumValuesPerNode_fmt_size = 4
        self.ReturnBounds = 0
        self._ReturnBounds_fmt = '<?'
        self._ReturnBounds_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack(self._IsReadModified_fmt, self.IsReadModified))
        tmp.append(self.StartTime.to_binary())
        tmp.append(self.EndTime.to_binary())
        tmp.append(struct.pack(self._NumValuesPerNode_fmt, self.NumValuesPerNode))
        tmp.append(struct.pack(self._ReturnBounds_fmt, self.ReturnBounds))
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.IsReadModified = struct.unpack(self._IsReadModified_fmt, data.read(self._IsReadModified_fmt_size))[0]
            self.StartTime = DateTime.from_binary(data)
            self.EndTime = DateTime.from_binary(data)
            self.NumValuesPerNode = struct.unpack(self._NumValuesPerNode_fmt, data.read(self._NumValuesPerNode_fmt_size))[0]
            self.ReturnBounds = struct.unpack(self._ReturnBounds_fmt, data.read(self._ReturnBounds_fmt_size))[0]
            return data
            
class ReadProcessedDetails(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.StartTime = 0
        self.EndTime = 0
        self.ProcessingInterval = 0
        self._ProcessingInterval_fmt = '<d'
        self._ProcessingInterval_fmt_size = 8
        self.AggregateType = []
        self.AggregateConfiguration = AggregateConfiguration()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.StartTime.to_binary())
        tmp.append(self.EndTime.to_binary())
        tmp.append(struct.pack(self._ProcessingInterval_fmt, self.ProcessingInterval))
        tmp.append(struct.pack('<i', len(self.AggregateType)))
        for i in AggregateType:
            tmp.append(self.AggregateType.to_binary())
        tmp.append(self.AggregateConfiguration.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.StartTime = DateTime.from_binary(data)
            self.EndTime = DateTime.from_binary(data)
            self.ProcessingInterval = struct.unpack(self._ProcessingInterval_fmt, data.read(self._ProcessingInterval_fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.AggregateType = NodeId.from_binary(data)
            self.AggregateConfiguration = AggregateConfiguration.from_binary(data)
            return data
            
class ReadAtTimeDetails(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.ReqTimes = []
        self.UseSimpleBounds = 0
        self._UseSimpleBounds_fmt = '<?'
        self._UseSimpleBounds_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack('<i', len(self.ReqTimes)))
        for i in ReqTimes:
            tmp.append(self.ReqTimes.to_binary())
        tmp.append(struct.pack(self._UseSimpleBounds_fmt, self.UseSimpleBounds))
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.ReqTimes = DateTime.from_binary(data)
            self.UseSimpleBounds = struct.unpack(self._UseSimpleBounds_fmt, data.read(self._UseSimpleBounds_fmt_size))[0]
            return data
            
class HistoryData(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.DataValues = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack('<i', len(self.DataValues)))
        for i in DataValues:
            tmp.append(self.DataValues.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.DataValues = DataValue.from_binary(data)
            return data
            
class ModificationInfo(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.ModificationTime = 0
        self.UpdateType = HistoryUpdateType()
        self.UserName = ''
        self._UserName_fmt = '<s'
        self._UserName_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.ModificationTime.to_binary())
        tmp.append(self.UpdateType.to_binary())
        tmp.append(struct.pack('<i', len(self.UserName)))
        tmp.append(struct.pack('<{}s'.format(len(self.UserName)), self.UserName.encode()))
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.ModificationTime = DateTime.from_binary(data)
            self.UpdateType = HistoryUpdateType.from_binary(data)
            slength = struct.unpack('<i', data.red(1))
            self.UserName = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.UserName = struct.unpack(self._UserName_fmt, data.read(self._UserName_fmt_size))[0]
            return data
            
class HistoryModifiedData(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.DataValues = []
        self.ModificationInfos = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack('<i', len(self.DataValues)))
        for i in DataValues:
            tmp.append(self.DataValues.to_binary())
        tmp.append(struct.pack('<i', len(self.ModificationInfos)))
        for i in ModificationInfos:
            tmp.append(self.ModificationInfos.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
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
        self.TypeId = ExpandedNodeId()
        self.Events = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack('<i', len(self.Events)))
        for i in Events:
            tmp.append(self.Events.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.Events = HistoryEventFieldList.from_binary(data)
            return data
            
class HistoryReadParameters(object):
    def __init__(self):
        self.HistoryReadDetails = ExtensionObject()
        self.TimestampsToReturn = 0
        self._TimestampsToReturn_fmt = '<I'
        self._TimestampsToReturn_fmt_size = 4
        self.ReleaseContinuationPoints = 0
        self._ReleaseContinuationPoints_fmt = '<?'
        self._ReleaseContinuationPoints_fmt_size = 1
        self.NodesToRead = []
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(self.HistoryReadDetails.to_binary())
        tmp.append(struct.pack(self._TimestampsToReturn_fmt, self.TimestampsToReturn))
        tmp.append(struct.pack(self._ReleaseContinuationPoints_fmt, self.ReleaseContinuationPoints))
        tmp.append(struct.pack('<i', len(self.NodesToRead)))
        for i in NodesToRead:
            tmp.append(self.NodesToRead.to_binary())
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.HistoryReadDetails = ExtensionObject.from_binary(data)
            self.TimestampsToReturn = struct.unpack(self._TimestampsToReturn_fmt, data.read(self._TimestampsToReturn_fmt_size))[0]
            self.ReleaseContinuationPoints = struct.unpack(self._ReleaseContinuationPoints_fmt, data.read(self._ReleaseContinuationPoints_fmt_size))[0]
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
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
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
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(struct.pack('<i', len(self.Results)))
        for i in Results:
            tmp.append(self.Results.to_binary())
        tmp.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for i in DiagnosticInfos:
            tmp.append(self.DiagnosticInfos.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
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
        self.TypeId = ExpandedNodeId()
        self.NodeId = NodeId()
        self.AttributeId = 0
        self._AttributeId_fmt = '<I'
        self._AttributeId_fmt_size = 4
        self.IndexRange = ''
        self._IndexRange_fmt = '<s'
        self._IndexRange_fmt_size = 1
        self.Value = DataValue()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.NodeId.to_binary())
        tmp.append(struct.pack(self._AttributeId_fmt, self.AttributeId))
        tmp.append(struct.pack('<i', len(self.IndexRange)))
        tmp.append(struct.pack('<{}s'.format(len(self.IndexRange)), self.IndexRange.encode()))
        tmp.append(self.Value.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.NodeId = NodeId.from_binary(data)
            self.AttributeId = struct.unpack(self._AttributeId_fmt, data.read(self._AttributeId_fmt_size))[0]
            slength = struct.unpack('<i', data.red(1))
            self.IndexRange = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.IndexRange = struct.unpack(self._IndexRange_fmt, data.read(self._IndexRange_fmt_size))[0]
            self.Value = DataValue.from_binary(data)
            return data
            
class WriteParameters(object):
    def __init__(self):
        self.NodesToWrite = []
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack('<i', len(self.NodesToWrite)))
        for i in NodesToWrite:
            tmp.append(self.NodesToWrite.to_binary())
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
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = WriteParameters.from_binary(data)
            return data
            
class WriteResult(object):
    def __init__(self):
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack('<i', len(self.Results)))
        for i in Results:
            tmp.append(self.Results.to_binary())
        tmp.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for i in DiagnosticInfos:
            tmp.append(self.DiagnosticInfos.to_binary())
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
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            self.Parameters = WriteResult.from_binary(data)
            return data
            
class HistoryUpdateDetails(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.NodeId = NodeId()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.NodeId.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.NodeId = NodeId.from_binary(data)
            return data
            
class UpdateDataDetails(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.NodeId = NodeId()
        self.PerformInsertReplace = PerformUpdateType()
        self.UpdateValues = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.NodeId.to_binary())
        tmp.append(self.PerformInsertReplace.to_binary())
        tmp.append(struct.pack('<i', len(self.UpdateValues)))
        for i in UpdateValues:
            tmp.append(self.UpdateValues.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.NodeId = NodeId.from_binary(data)
            self.PerformInsertReplace = PerformUpdateType.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.UpdateValues = DataValue.from_binary(data)
            return data
            
class UpdateStructureDataDetails(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.NodeId = NodeId()
        self.PerformInsertReplace = PerformUpdateType()
        self.UpdateValues = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.NodeId.to_binary())
        tmp.append(self.PerformInsertReplace.to_binary())
        tmp.append(struct.pack('<i', len(self.UpdateValues)))
        for i in UpdateValues:
            tmp.append(self.UpdateValues.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.NodeId = NodeId.from_binary(data)
            self.PerformInsertReplace = PerformUpdateType.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.UpdateValues = DataValue.from_binary(data)
            return data
            
class UpdateEventDetails(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.NodeId = NodeId()
        self.PerformInsertReplace = PerformUpdateType()
        self.Filter = EventFilter()
        self.EventData = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.NodeId.to_binary())
        tmp.append(self.PerformInsertReplace.to_binary())
        tmp.append(self.Filter.to_binary())
        tmp.append(struct.pack('<i', len(self.EventData)))
        for i in EventData:
            tmp.append(self.EventData.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.NodeId = NodeId.from_binary(data)
            self.PerformInsertReplace = PerformUpdateType.from_binary(data)
            self.Filter = EventFilter.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.EventData = HistoryEventFieldList.from_binary(data)
            return data
            
class DeleteRawModifiedDetails(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.NodeId = NodeId()
        self.IsDeleteModified = 0
        self._IsDeleteModified_fmt = '<?'
        self._IsDeleteModified_fmt_size = 1
        self.StartTime = 0
        self.EndTime = 0
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.NodeId.to_binary())
        tmp.append(struct.pack(self._IsDeleteModified_fmt, self.IsDeleteModified))
        tmp.append(self.StartTime.to_binary())
        tmp.append(self.EndTime.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.NodeId = NodeId.from_binary(data)
            self.IsDeleteModified = struct.unpack(self._IsDeleteModified_fmt, data.read(self._IsDeleteModified_fmt_size))[0]
            self.StartTime = DateTime.from_binary(data)
            self.EndTime = DateTime.from_binary(data)
            return data
            
class DeleteAtTimeDetails(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.NodeId = NodeId()
        self.ReqTimes = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.NodeId.to_binary())
        tmp.append(struct.pack('<i', len(self.ReqTimes)))
        for i in ReqTimes:
            tmp.append(self.ReqTimes.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.NodeId = NodeId.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.ReqTimes = DateTime.from_binary(data)
            return data
            
class DeleteEventDetails(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.NodeId = NodeId()
        self.EventIds = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.NodeId.to_binary())
        tmp.append(struct.pack('<i', len(self.EventIds)))
        for i in EventIds:
            tmp.append(self.EventIds.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.NodeId = NodeId.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.EventIds = ByteString.from_binary(data)
            return data
            
class HistoryUpdateResult(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.StatusCode = StatusCode()
        self.OperationResults = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.StatusCode.to_binary())
        tmp.append(struct.pack('<i', len(self.OperationResults)))
        for i in OperationResults:
            tmp.append(self.OperationResults.to_binary())
        tmp.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for i in DiagnosticInfos:
            tmp.append(self.DiagnosticInfos.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
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
        self.TypeId = ExpandedNodeId()
        self.StatusCode = StatusCode()
        self.EventFilterResult = EventFilterResult()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.StatusCode.to_binary())
        tmp.append(self.EventFilterResult.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.StatusCode = StatusCode.from_binary(data)
            self.EventFilterResult = EventFilterResult.from_binary(data)
            return data
            
class HistoryUpdateParameters(object):
    def __init__(self):
        self.HistoryUpdateDetails = []
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack('<i', len(self.HistoryUpdateDetails)))
        for i in HistoryUpdateDetails:
            tmp.append(self.HistoryUpdateDetails.to_binary())
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
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
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
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(struct.pack('<i', len(self.Results)))
        for i in Results:
            tmp.append(self.Results.to_binary())
        tmp.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for i in DiagnosticInfos:
            tmp.append(self.DiagnosticInfos.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
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
        tmp = packet
        tmp.append(self.MethodId.to_binary())
        tmp.append(struct.pack('<i', len(self.InputArguments)))
        for i in InputArguments:
            tmp.append(self.InputArguments.to_binary())
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
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.ObjectId.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.ObjectId = NodeId.from_binary(data)
            self.Parameters = CallMethodParameters.from_binary(data)
            return data
            
class CallMethodResult(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.StatusCode = StatusCode()
        self.InputArgumentResults = []
        self.InputArgumentDiagnosticInfos = []
        self.OutputArguments = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.StatusCode.to_binary())
        tmp.append(struct.pack('<i', len(self.InputArgumentResults)))
        for i in InputArgumentResults:
            tmp.append(self.InputArgumentResults.to_binary())
        tmp.append(struct.pack('<i', len(self.InputArgumentDiagnosticInfos)))
        for i in InputArgumentDiagnosticInfos:
            tmp.append(self.InputArgumentDiagnosticInfos.to_binary())
        tmp.append(struct.pack('<i', len(self.OutputArguments)))
        for i in OutputArguments:
            tmp.append(self.OutputArguments.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
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
        tmp = packet
        tmp.append(struct.pack('<i', len(self.MethodsToCall)))
        for i in MethodsToCall:
            tmp.append(self.MethodsToCall.to_binary())
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
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = CallParameters.from_binary(data)
            return data
            
class CallResult(object):
    def __init__(self):
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack('<i', len(self.Results)))
        for i in Results:
            tmp.append(self.Results.to_binary())
        tmp.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for i in DiagnosticInfos:
            tmp.append(self.DiagnosticInfos.to_binary())
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
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            self.Parameters = CallResult.from_binary(data)
            return data
            
class MonitoringFilter(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            return data
            
class DataChangeFilter(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.Trigger = DataChangeTrigger()
        self.DeadbandType = 0
        self._DeadbandType_fmt = '<I'
        self._DeadbandType_fmt_size = 4
        self.DeadbandValue = 0
        self._DeadbandValue_fmt = '<d'
        self._DeadbandValue_fmt_size = 8
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.Trigger.to_binary())
        tmp.append(struct.pack(self._DeadbandType_fmt, self.DeadbandType))
        tmp.append(struct.pack(self._DeadbandValue_fmt, self.DeadbandValue))
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.Trigger = DataChangeTrigger.from_binary(data)
            self.DeadbandType = struct.unpack(self._DeadbandType_fmt, data.read(self._DeadbandType_fmt_size))[0]
            self.DeadbandValue = struct.unpack(self._DeadbandValue_fmt, data.read(self._DeadbandValue_fmt_size))[0]
            return data
            
class EventFilter(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.SelectClauses = []
        self.WhereClause = ContentFilter()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack('<i', len(self.SelectClauses)))
        for i in SelectClauses:
            tmp.append(self.SelectClauses.to_binary())
        tmp.append(self.WhereClause.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.SelectClauses = SimpleAttributeOperand.from_binary(data)
            self.WhereClause = ContentFilter.from_binary(data)
            return data
            
class AggregateConfiguration(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.UseServerCapabilitiesDefaults = 0
        self._UseServerCapabilitiesDefaults_fmt = '<?'
        self._UseServerCapabilitiesDefaults_fmt_size = 1
        self.TreatUncertainAsBad = 0
        self._TreatUncertainAsBad_fmt = '<?'
        self._TreatUncertainAsBad_fmt_size = 1
        self.PercentDataBad = 0
        self._PercentDataBad_fmt = '<B'
        self._PercentDataBad_fmt_size = 1
        self.PercentDataGood = 0
        self._PercentDataGood_fmt = '<B'
        self._PercentDataGood_fmt_size = 1
        self.UseSlopedExtrapolation = 0
        self._UseSlopedExtrapolation_fmt = '<?'
        self._UseSlopedExtrapolation_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack(self._UseServerCapabilitiesDefaults_fmt, self.UseServerCapabilitiesDefaults))
        tmp.append(struct.pack(self._TreatUncertainAsBad_fmt, self.TreatUncertainAsBad))
        tmp.append(struct.pack(self._PercentDataBad_fmt, self.PercentDataBad))
        tmp.append(struct.pack(self._PercentDataGood_fmt, self.PercentDataGood))
        tmp.append(struct.pack(self._UseSlopedExtrapolation_fmt, self.UseSlopedExtrapolation))
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.UseServerCapabilitiesDefaults = struct.unpack(self._UseServerCapabilitiesDefaults_fmt, data.read(self._UseServerCapabilitiesDefaults_fmt_size))[0]
            self.TreatUncertainAsBad = struct.unpack(self._TreatUncertainAsBad_fmt, data.read(self._TreatUncertainAsBad_fmt_size))[0]
            self.PercentDataBad = struct.unpack(self._PercentDataBad_fmt, data.read(self._PercentDataBad_fmt_size))[0]
            self.PercentDataGood = struct.unpack(self._PercentDataGood_fmt, data.read(self._PercentDataGood_fmt_size))[0]
            self.UseSlopedExtrapolation = struct.unpack(self._UseSlopedExtrapolation_fmt, data.read(self._UseSlopedExtrapolation_fmt_size))[0]
            return data
            
class AggregateFilter(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.StartTime = 0
        self.AggregateType = NodeId()
        self.ProcessingInterval = 0
        self._ProcessingInterval_fmt = '<d'
        self._ProcessingInterval_fmt_size = 8
        self.AggregateConfiguration = AggregateConfiguration()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.StartTime.to_binary())
        tmp.append(self.AggregateType.to_binary())
        tmp.append(struct.pack(self._ProcessingInterval_fmt, self.ProcessingInterval))
        tmp.append(self.AggregateConfiguration.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.StartTime = DateTime.from_binary(data)
            self.AggregateType = NodeId.from_binary(data)
            self.ProcessingInterval = struct.unpack(self._ProcessingInterval_fmt, data.read(self._ProcessingInterval_fmt_size))[0]
            self.AggregateConfiguration = AggregateConfiguration.from_binary(data)
            return data
            
class MonitoringFilterResult(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            return data
            
class EventFilterResult(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.SelectClauseResults = []
        self.SelectClauseDiagnosticInfos = []
        self.WhereClauseResult = ContentFilterResult()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack('<i', len(self.SelectClauseResults)))
        for i in SelectClauseResults:
            tmp.append(self.SelectClauseResults.to_binary())
        tmp.append(struct.pack('<i', len(self.SelectClauseDiagnosticInfos)))
        for i in SelectClauseDiagnosticInfos:
            tmp.append(self.SelectClauseDiagnosticInfos.to_binary())
        tmp.append(self.WhereClauseResult.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
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
        self.TypeId = ExpandedNodeId()
        self.RevisedStartTime = 0
        self.RevisedProcessingInterval = 0
        self._RevisedProcessingInterval_fmt = '<d'
        self._RevisedProcessingInterval_fmt_size = 8
        self.RevisedAggregateConfiguration = AggregateConfiguration()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.RevisedStartTime.to_binary())
        tmp.append(struct.pack(self._RevisedProcessingInterval_fmt, self.RevisedProcessingInterval))
        tmp.append(self.RevisedAggregateConfiguration.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.RevisedStartTime = DateTime.from_binary(data)
            self.RevisedProcessingInterval = struct.unpack(self._RevisedProcessingInterval_fmt, data.read(self._RevisedProcessingInterval_fmt_size))[0]
            self.RevisedAggregateConfiguration = AggregateConfiguration.from_binary(data)
            return data
            
class MonitoringParameters(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.ClientHandle = 0
        self._ClientHandle_fmt = '<I'
        self._ClientHandle_fmt_size = 4
        self.SamplingInterval = 0
        self._SamplingInterval_fmt = '<d'
        self._SamplingInterval_fmt_size = 8
        self.Filter = ExtensionObject()
        self.QueueSize = 0
        self._QueueSize_fmt = '<I'
        self._QueueSize_fmt_size = 4
        self.DiscardOldest = 0
        self._DiscardOldest_fmt = '<?'
        self._DiscardOldest_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack(self._ClientHandle_fmt, self.ClientHandle))
        tmp.append(struct.pack(self._SamplingInterval_fmt, self.SamplingInterval))
        tmp.append(self.Filter.to_binary())
        tmp.append(struct.pack(self._QueueSize_fmt, self.QueueSize))
        tmp.append(struct.pack(self._DiscardOldest_fmt, self.DiscardOldest))
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.ClientHandle = struct.unpack(self._ClientHandle_fmt, data.read(self._ClientHandle_fmt_size))[0]
            self.SamplingInterval = struct.unpack(self._SamplingInterval_fmt, data.read(self._SamplingInterval_fmt_size))[0]
            self.Filter = ExtensionObject.from_binary(data)
            self.QueueSize = struct.unpack(self._QueueSize_fmt, data.read(self._QueueSize_fmt_size))[0]
            self.DiscardOldest = struct.unpack(self._DiscardOldest_fmt, data.read(self._DiscardOldest_fmt_size))[0]
            return data
            
class MonitoredItemCreateParameters(object):
    def __init__(self):
        self.MonitoringMode = 0
        self._MonitoringMode_fmt = '<I'
        self._MonitoringMode_fmt_size = 4
        self.RequestedParameters = MonitoringParameters()
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack(self._MonitoringMode_fmt, self.MonitoringMode))
        tmp.append(self.RequestedParameters.to_binary())
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.MonitoringMode = struct.unpack(self._MonitoringMode_fmt, data.read(self._MonitoringMode_fmt_size))[0]
            self.RequestedParameters = MonitoringParameters.from_binary(data)
            return data
            
class MonitoredItemCreateRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.MonitoredItemCreateRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
        self.ItemToMonitor = ReadValueId()
        self.Parameters = MonitoredItemCreateParameters()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.ItemToMonitor.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.ItemToMonitor = ReadValueId.from_binary(data)
            self.Parameters = MonitoredItemCreateParameters.from_binary(data)
            return data
            
class MonitoredItemCreateResult(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.StatusCode = StatusCode()
        self.MonitoredItemId = 0
        self._MonitoredItemId_fmt = '<I'
        self._MonitoredItemId_fmt_size = 4
        self.RevisedSamplingInterval = 0
        self._RevisedSamplingInterval_fmt = '<d'
        self._RevisedSamplingInterval_fmt_size = 8
        self.RevisedQueueSize = 0
        self._RevisedQueueSize_fmt = '<I'
        self._RevisedQueueSize_fmt_size = 4
        self.FilterResult = ExtensionObject()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.StatusCode.to_binary())
        tmp.append(struct.pack(self._MonitoredItemId_fmt, self.MonitoredItemId))
        tmp.append(struct.pack(self._RevisedSamplingInterval_fmt, self.RevisedSamplingInterval))
        tmp.append(struct.pack(self._RevisedQueueSize_fmt, self.RevisedQueueSize))
        tmp.append(self.FilterResult.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.StatusCode = StatusCode.from_binary(data)
            self.MonitoredItemId = struct.unpack(self._MonitoredItemId_fmt, data.read(self._MonitoredItemId_fmt_size))[0]
            self.RevisedSamplingInterval = struct.unpack(self._RevisedSamplingInterval_fmt, data.read(self._RevisedSamplingInterval_fmt_size))[0]
            self.RevisedQueueSize = struct.unpack(self._RevisedQueueSize_fmt, data.read(self._RevisedQueueSize_fmt_size))[0]
            self.FilterResult = ExtensionObject.from_binary(data)
            return data
            
class CreateMonitoredItemsParameters(object):
    def __init__(self):
        self.SubscriptionId = 0
        self._SubscriptionId_fmt = '<I'
        self._SubscriptionId_fmt_size = 4
        self.TimestampsToReturn = 0
        self._TimestampsToReturn_fmt = '<I'
        self._TimestampsToReturn_fmt_size = 4
        self.ItemsToCreate = []
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack(self._SubscriptionId_fmt, self.SubscriptionId))
        tmp.append(struct.pack(self._TimestampsToReturn_fmt, self.TimestampsToReturn))
        tmp.append(struct.pack('<i', len(self.ItemsToCreate)))
        for i in ItemsToCreate:
            tmp.append(self.ItemsToCreate.to_binary())
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.SubscriptionId = struct.unpack(self._SubscriptionId_fmt, data.read(self._SubscriptionId_fmt_size))[0]
            self.TimestampsToReturn = struct.unpack(self._TimestampsToReturn_fmt, data.read(self._TimestampsToReturn_fmt_size))[0]
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
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = CreateMonitoredItemsParameters.from_binary(data)
            return data
            
class CreateMonitoredItemsResult(object):
    def __init__(self):
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack('<i', len(self.Results)))
        for i in Results:
            tmp.append(self.Results.to_binary())
        tmp.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for i in DiagnosticInfos:
            tmp.append(self.DiagnosticInfos.to_binary())
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
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            self.Parameters = CreateMonitoredItemsResult.from_binary(data)
            return data
            
class MonitoredItemModifyRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.MonitoredItemModifyRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
        self.MonitoredItemId = 0
        self._MonitoredItemId_fmt = '<I'
        self._MonitoredItemId_fmt_size = 4
        self.RequestedParameters = MonitoringParameters()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack(self._MonitoredItemId_fmt, self.MonitoredItemId))
        tmp.append(self.RequestedParameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.MonitoredItemId = struct.unpack(self._MonitoredItemId_fmt, data.read(self._MonitoredItemId_fmt_size))[0]
            self.RequestedParameters = MonitoringParameters.from_binary(data)
            return data
            
class MonitoredItemModifyResult(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.StatusCode = StatusCode()
        self.RevisedSamplingInterval = 0
        self._RevisedSamplingInterval_fmt = '<d'
        self._RevisedSamplingInterval_fmt_size = 8
        self.RevisedQueueSize = 0
        self._RevisedQueueSize_fmt = '<I'
        self._RevisedQueueSize_fmt_size = 4
        self.FilterResult = ExtensionObject()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.StatusCode.to_binary())
        tmp.append(struct.pack(self._RevisedSamplingInterval_fmt, self.RevisedSamplingInterval))
        tmp.append(struct.pack(self._RevisedQueueSize_fmt, self.RevisedQueueSize))
        tmp.append(self.FilterResult.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.StatusCode = StatusCode.from_binary(data)
            self.RevisedSamplingInterval = struct.unpack(self._RevisedSamplingInterval_fmt, data.read(self._RevisedSamplingInterval_fmt_size))[0]
            self.RevisedQueueSize = struct.unpack(self._RevisedQueueSize_fmt, data.read(self._RevisedQueueSize_fmt_size))[0]
            self.FilterResult = ExtensionObject.from_binary(data)
            return data
            
class ModifyMonitoredItemsParameters(object):
    def __init__(self):
        self.SubscriptionId = 0
        self._SubscriptionId_fmt = '<I'
        self._SubscriptionId_fmt_size = 4
        self.TimestampsToReturn = 0
        self._TimestampsToReturn_fmt = '<I'
        self._TimestampsToReturn_fmt_size = 4
        self.ItemsToModify = []
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack(self._SubscriptionId_fmt, self.SubscriptionId))
        tmp.append(struct.pack(self._TimestampsToReturn_fmt, self.TimestampsToReturn))
        tmp.append(struct.pack('<i', len(self.ItemsToModify)))
        for i in ItemsToModify:
            tmp.append(self.ItemsToModify.to_binary())
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.SubscriptionId = struct.unpack(self._SubscriptionId_fmt, data.read(self._SubscriptionId_fmt_size))[0]
            self.TimestampsToReturn = struct.unpack(self._TimestampsToReturn_fmt, data.read(self._TimestampsToReturn_fmt_size))[0]
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
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = ModifyMonitoredItemsParameters.from_binary(data)
            return data
            
class ModifyMonitoredItemsResult(object):
    def __init__(self):
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack('<i', len(self.Results)))
        for i in Results:
            tmp.append(self.Results.to_binary())
        tmp.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for i in DiagnosticInfos:
            tmp.append(self.DiagnosticInfos.to_binary())
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
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            self.Parameters = ModifyMonitoredItemsResult.from_binary(data)
            return data
            
class SetMonitoringModeParameters(object):
    def __init__(self):
        self.SubscriptionId = 0
        self._SubscriptionId_fmt = '<I'
        self._SubscriptionId_fmt_size = 4
        self.MonitoringMode = 0
        self._MonitoringMode_fmt = '<I'
        self._MonitoringMode_fmt_size = 4
        self.MonitoredItemIds = []
        self._MonitoredItemIds_fmt = '<I'
        self._MonitoredItemIds_fmt_size = 4
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack(self._SubscriptionId_fmt, self.SubscriptionId))
        tmp.append(struct.pack(self._MonitoringMode_fmt, self.MonitoringMode))
        tmp.append(struct.pack('<i', len(self.MonitoredItemIds)))
        for i in MonitoredItemIds:
            tmp.append(struct.pack(self._MonitoredItemIds_fmt, self.MonitoredItemIds))
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.SubscriptionId = struct.unpack(self._SubscriptionId_fmt, data.read(self._SubscriptionId_fmt_size))[0]
            self.MonitoringMode = struct.unpack(self._MonitoringMode_fmt, data.read(self._MonitoringMode_fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.MonitoredItemIds = struct.unpack(self._MonitoredItemIds_fmt, data.read(self._MonitoredItemIds_fmt_size))[0]
            return data
            
class SetMonitoringModeRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.SetMonitoringModeRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
        self.RequestHeader = RequestHeader()
        self.Parameters = SetMonitoringModeParameters()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = SetMonitoringModeParameters.from_binary(data)
            return data
            
class SetMonitoringModeResult(object):
    def __init__(self):
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack('<i', len(self.Results)))
        for i in Results:
            tmp.append(self.Results.to_binary())
        tmp.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for i in DiagnosticInfos:
            tmp.append(self.DiagnosticInfos.to_binary())
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
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            self.Parameters = SetMonitoringModeResult.from_binary(data)
            return data
            
class SetTriggeringParameters(object):
    def __init__(self):
        self.SubscriptionId = 0
        self._SubscriptionId_fmt = '<I'
        self._SubscriptionId_fmt_size = 4
        self.TriggeringItemId = 0
        self._TriggeringItemId_fmt = '<I'
        self._TriggeringItemId_fmt_size = 4
        self.LinksToAdd = []
        self._LinksToAdd_fmt = '<I'
        self._LinksToAdd_fmt_size = 4
        self.LinksToRemove = []
        self._LinksToRemove_fmt = '<I'
        self._LinksToRemove_fmt_size = 4
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack(self._SubscriptionId_fmt, self.SubscriptionId))
        tmp.append(struct.pack(self._TriggeringItemId_fmt, self.TriggeringItemId))
        tmp.append(struct.pack('<i', len(self.LinksToAdd)))
        for i in LinksToAdd:
            tmp.append(struct.pack(self._LinksToAdd_fmt, self.LinksToAdd))
        tmp.append(struct.pack('<i', len(self.LinksToRemove)))
        for i in LinksToRemove:
            tmp.append(struct.pack(self._LinksToRemove_fmt, self.LinksToRemove))
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.SubscriptionId = struct.unpack(self._SubscriptionId_fmt, data.read(self._SubscriptionId_fmt_size))[0]
            self.TriggeringItemId = struct.unpack(self._TriggeringItemId_fmt, data.read(self._TriggeringItemId_fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.LinksToAdd = struct.unpack(self._LinksToAdd_fmt, data.read(self._LinksToAdd_fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.LinksToRemove = struct.unpack(self._LinksToRemove_fmt, data.read(self._LinksToRemove_fmt_size))[0]
            return data
            
class SetTriggeringRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.SetTriggeringRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
        self.RequestHeader = RequestHeader()
        self.Parameters = SetTriggeringParameters()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
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
        tmp = packet
        tmp.append(struct.pack('<i', len(self.AddResults)))
        for i in AddResults:
            tmp.append(self.AddResults.to_binary())
        tmp.append(struct.pack('<i', len(self.AddDiagnosticInfos)))
        for i in AddDiagnosticInfos:
            tmp.append(self.AddDiagnosticInfos.to_binary())
        tmp.append(struct.pack('<i', len(self.RemoveResults)))
        for i in RemoveResults:
            tmp.append(self.RemoveResults.to_binary())
        tmp.append(struct.pack('<i', len(self.RemoveDiagnosticInfos)))
        for i in RemoveDiagnosticInfos:
            tmp.append(self.RemoveDiagnosticInfos.to_binary())
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
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            self.Parameters = SetTriggeringResult.from_binary(data)
            return data
            
class DeleteMonitoredItemsParameters(object):
    def __init__(self):
        self.SubscriptionId = 0
        self._SubscriptionId_fmt = '<I'
        self._SubscriptionId_fmt_size = 4
        self.MonitoredItemIds = []
        self._MonitoredItemIds_fmt = '<I'
        self._MonitoredItemIds_fmt_size = 4
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack(self._SubscriptionId_fmt, self.SubscriptionId))
        tmp.append(struct.pack('<i', len(self.MonitoredItemIds)))
        for i in MonitoredItemIds:
            tmp.append(struct.pack(self._MonitoredItemIds_fmt, self.MonitoredItemIds))
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.SubscriptionId = struct.unpack(self._SubscriptionId_fmt, data.read(self._SubscriptionId_fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.MonitoredItemIds = struct.unpack(self._MonitoredItemIds_fmt, data.read(self._MonitoredItemIds_fmt_size))[0]
            return data
            
class DeleteMonitoredItemsRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.DeleteMonitoredItemsRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
        self.RequestHeader = RequestHeader()
        self.Parameters = DeleteMonitoredItemsParameters()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = DeleteMonitoredItemsParameters.from_binary(data)
            return data
            
class DeleteMonitoredItemsResult(object):
    def __init__(self):
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack('<i', len(self.Results)))
        for i in Results:
            tmp.append(self.Results.to_binary())
        tmp.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for i in DiagnosticInfos:
            tmp.append(self.DiagnosticInfos.to_binary())
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
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            self.Parameters = DeleteMonitoredItemsResult.from_binary(data)
            return data
            
class CreateSubscriptionParameters(object):
    def __init__(self):
        self.RequestedPublishingInterval = 0
        self._RequestedPublishingInterval_fmt = '<d'
        self._RequestedPublishingInterval_fmt_size = 8
        self.RequestedLifetimeCount = 0
        self._RequestedLifetimeCount_fmt = '<I'
        self._RequestedLifetimeCount_fmt_size = 4
        self.RequestedMaxKeepAliveCount = 0
        self._RequestedMaxKeepAliveCount_fmt = '<I'
        self._RequestedMaxKeepAliveCount_fmt_size = 4
        self.MaxNotificationsPerPublish = 0
        self._MaxNotificationsPerPublish_fmt = '<I'
        self._MaxNotificationsPerPublish_fmt_size = 4
        self.PublishingEnabled = 0
        self._PublishingEnabled_fmt = '<?'
        self._PublishingEnabled_fmt_size = 1
        self.Priority = 0
        self._Priority_fmt = '<B'
        self._Priority_fmt_size = 1
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack(self._RequestedPublishingInterval_fmt, self.RequestedPublishingInterval))
        tmp.append(struct.pack(self._RequestedLifetimeCount_fmt, self.RequestedLifetimeCount))
        tmp.append(struct.pack(self._RequestedMaxKeepAliveCount_fmt, self.RequestedMaxKeepAliveCount))
        tmp.append(struct.pack(self._MaxNotificationsPerPublish_fmt, self.MaxNotificationsPerPublish))
        tmp.append(struct.pack(self._PublishingEnabled_fmt, self.PublishingEnabled))
        tmp.append(struct.pack(self._Priority_fmt, self.Priority))
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.RequestedPublishingInterval = struct.unpack(self._RequestedPublishingInterval_fmt, data.read(self._RequestedPublishingInterval_fmt_size))[0]
            self.RequestedLifetimeCount = struct.unpack(self._RequestedLifetimeCount_fmt, data.read(self._RequestedLifetimeCount_fmt_size))[0]
            self.RequestedMaxKeepAliveCount = struct.unpack(self._RequestedMaxKeepAliveCount_fmt, data.read(self._RequestedMaxKeepAliveCount_fmt_size))[0]
            self.MaxNotificationsPerPublish = struct.unpack(self._MaxNotificationsPerPublish_fmt, data.read(self._MaxNotificationsPerPublish_fmt_size))[0]
            self.PublishingEnabled = struct.unpack(self._PublishingEnabled_fmt, data.read(self._PublishingEnabled_fmt_size))[0]
            self.Priority = struct.unpack(self._Priority_fmt, data.read(self._Priority_fmt_size))[0]
            return data
            
class CreateSubscriptionRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.CreateSubscriptionRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
        self.RequestHeader = RequestHeader()
        self.Parameters = CreateSubscriptionParameters()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = CreateSubscriptionParameters.from_binary(data)
            return data
            
class CreateSubscriptionResult(object):
    def __init__(self):
        self.SubscriptionId = 0
        self._SubscriptionId_fmt = '<I'
        self._SubscriptionId_fmt_size = 4
        self.RevisedPublishingInterval = 0
        self._RevisedPublishingInterval_fmt = '<d'
        self._RevisedPublishingInterval_fmt_size = 8
        self.RevisedLifetimeCount = 0
        self._RevisedLifetimeCount_fmt = '<I'
        self._RevisedLifetimeCount_fmt_size = 4
        self.RevisedMaxKeepAliveCount = 0
        self._RevisedMaxKeepAliveCount_fmt = '<I'
        self._RevisedMaxKeepAliveCount_fmt_size = 4
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack(self._SubscriptionId_fmt, self.SubscriptionId))
        tmp.append(struct.pack(self._RevisedPublishingInterval_fmt, self.RevisedPublishingInterval))
        tmp.append(struct.pack(self._RevisedLifetimeCount_fmt, self.RevisedLifetimeCount))
        tmp.append(struct.pack(self._RevisedMaxKeepAliveCount_fmt, self.RevisedMaxKeepAliveCount))
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.SubscriptionId = struct.unpack(self._SubscriptionId_fmt, data.read(self._SubscriptionId_fmt_size))[0]
            self.RevisedPublishingInterval = struct.unpack(self._RevisedPublishingInterval_fmt, data.read(self._RevisedPublishingInterval_fmt_size))[0]
            self.RevisedLifetimeCount = struct.unpack(self._RevisedLifetimeCount_fmt, data.read(self._RevisedLifetimeCount_fmt_size))[0]
            self.RevisedMaxKeepAliveCount = struct.unpack(self._RevisedMaxKeepAliveCount_fmt, data.read(self._RevisedMaxKeepAliveCount_fmt_size))[0]
            return data
            
class CreateSubscriptionResponse(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.CreateSubscriptionResponse_Encoding_DefaultBinary, NodeIdType.FourByte)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = CreateSubscriptionResult()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            self.Parameters = CreateSubscriptionResult.from_binary(data)
            return data
            
class ModifySubscriptionParameters(object):
    def __init__(self):
        self.SubscriptionId = 0
        self._SubscriptionId_fmt = '<I'
        self._SubscriptionId_fmt_size = 4
        self.RequestedPublishingInterval = 0
        self._RequestedPublishingInterval_fmt = '<d'
        self._RequestedPublishingInterval_fmt_size = 8
        self.RequestedLifetimeCount = 0
        self._RequestedLifetimeCount_fmt = '<I'
        self._RequestedLifetimeCount_fmt_size = 4
        self.RequestedMaxKeepAliveCount = 0
        self._RequestedMaxKeepAliveCount_fmt = '<I'
        self._RequestedMaxKeepAliveCount_fmt_size = 4
        self.MaxNotificationsPerPublish = 0
        self._MaxNotificationsPerPublish_fmt = '<I'
        self._MaxNotificationsPerPublish_fmt_size = 4
        self.Priority = 0
        self._Priority_fmt = '<B'
        self._Priority_fmt_size = 1
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack(self._SubscriptionId_fmt, self.SubscriptionId))
        tmp.append(struct.pack(self._RequestedPublishingInterval_fmt, self.RequestedPublishingInterval))
        tmp.append(struct.pack(self._RequestedLifetimeCount_fmt, self.RequestedLifetimeCount))
        tmp.append(struct.pack(self._RequestedMaxKeepAliveCount_fmt, self.RequestedMaxKeepAliveCount))
        tmp.append(struct.pack(self._MaxNotificationsPerPublish_fmt, self.MaxNotificationsPerPublish))
        tmp.append(struct.pack(self._Priority_fmt, self.Priority))
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.SubscriptionId = struct.unpack(self._SubscriptionId_fmt, data.read(self._SubscriptionId_fmt_size))[0]
            self.RequestedPublishingInterval = struct.unpack(self._RequestedPublishingInterval_fmt, data.read(self._RequestedPublishingInterval_fmt_size))[0]
            self.RequestedLifetimeCount = struct.unpack(self._RequestedLifetimeCount_fmt, data.read(self._RequestedLifetimeCount_fmt_size))[0]
            self.RequestedMaxKeepAliveCount = struct.unpack(self._RequestedMaxKeepAliveCount_fmt, data.read(self._RequestedMaxKeepAliveCount_fmt_size))[0]
            self.MaxNotificationsPerPublish = struct.unpack(self._MaxNotificationsPerPublish_fmt, data.read(self._MaxNotificationsPerPublish_fmt_size))[0]
            self.Priority = struct.unpack(self._Priority_fmt, data.read(self._Priority_fmt_size))[0]
            return data
            
class ModifySubscriptionRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.ModifySubscriptionRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
        self.RequestHeader = RequestHeader()
        self.Parameters = ModifySubscriptionParameters()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = ModifySubscriptionParameters.from_binary(data)
            return data
            
class ModifySubscriptionResult(object):
    def __init__(self):
        self.RevisedPublishingInterval = 0
        self._RevisedPublishingInterval_fmt = '<d'
        self._RevisedPublishingInterval_fmt_size = 8
        self.RevisedLifetimeCount = 0
        self._RevisedLifetimeCount_fmt = '<I'
        self._RevisedLifetimeCount_fmt_size = 4
        self.RevisedMaxKeepAliveCount = 0
        self._RevisedMaxKeepAliveCount_fmt = '<I'
        self._RevisedMaxKeepAliveCount_fmt_size = 4
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack(self._RevisedPublishingInterval_fmt, self.RevisedPublishingInterval))
        tmp.append(struct.pack(self._RevisedLifetimeCount_fmt, self.RevisedLifetimeCount))
        tmp.append(struct.pack(self._RevisedMaxKeepAliveCount_fmt, self.RevisedMaxKeepAliveCount))
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.RevisedPublishingInterval = struct.unpack(self._RevisedPublishingInterval_fmt, data.read(self._RevisedPublishingInterval_fmt_size))[0]
            self.RevisedLifetimeCount = struct.unpack(self._RevisedLifetimeCount_fmt, data.read(self._RevisedLifetimeCount_fmt_size))[0]
            self.RevisedMaxKeepAliveCount = struct.unpack(self._RevisedMaxKeepAliveCount_fmt, data.read(self._RevisedMaxKeepAliveCount_fmt_size))[0]
            return data
            
class ModifySubscriptionResponse(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.ModifySubscriptionResponse_Encoding_DefaultBinary, NodeIdType.FourByte)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = ModifySubscriptionResult()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            self.Parameters = ModifySubscriptionResult.from_binary(data)
            return data
            
class SetPublishingModeParameters(object):
    def __init__(self):
        self.PublishingEnabled = 0
        self._PublishingEnabled_fmt = '<?'
        self._PublishingEnabled_fmt_size = 1
        self.SubscriptionIds = []
        self._SubscriptionIds_fmt = '<I'
        self._SubscriptionIds_fmt_size = 4
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack(self._PublishingEnabled_fmt, self.PublishingEnabled))
        tmp.append(struct.pack('<i', len(self.SubscriptionIds)))
        for i in SubscriptionIds:
            tmp.append(struct.pack(self._SubscriptionIds_fmt, self.SubscriptionIds))
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.PublishingEnabled = struct.unpack(self._PublishingEnabled_fmt, data.read(self._PublishingEnabled_fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.SubscriptionIds = struct.unpack(self._SubscriptionIds_fmt, data.read(self._SubscriptionIds_fmt_size))[0]
            return data
            
class SetPublishingModeRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.SetPublishingModeRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
        self.RequestHeader = RequestHeader()
        self.Parameters = SetPublishingModeParameters()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = SetPublishingModeParameters.from_binary(data)
            return data
            
class SetPublishingModeResult(object):
    def __init__(self):
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack('<i', len(self.Results)))
        for i in Results:
            tmp.append(self.Results.to_binary())
        tmp.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for i in DiagnosticInfos:
            tmp.append(self.DiagnosticInfos.to_binary())
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
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            self.Parameters = SetPublishingModeResult.from_binary(data)
            return data
            
class NotificationMessage(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.SequenceNumber = 0
        self._SequenceNumber_fmt = '<I'
        self._SequenceNumber_fmt_size = 4
        self.PublishTime = 0
        self.NotificationData = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack(self._SequenceNumber_fmt, self.SequenceNumber))
        tmp.append(self.PublishTime.to_binary())
        tmp.append(struct.pack('<i', len(self.NotificationData)))
        for i in NotificationData:
            tmp.append(self.NotificationData.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.SequenceNumber = struct.unpack(self._SequenceNumber_fmt, data.read(self._SequenceNumber_fmt_size))[0]
            self.PublishTime = DateTime.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.NotificationData = ExtensionObject.from_binary(data)
            return data
            
class NotificationData(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            return data
            
class DataChangeNotification(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.MonitoredItems = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack('<i', len(self.MonitoredItems)))
        for i in MonitoredItems:
            tmp.append(self.MonitoredItems.to_binary())
        tmp.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for i in DiagnosticInfos:
            tmp.append(self.DiagnosticInfos.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
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
        self.TypeId = ExpandedNodeId()
        self.ClientHandle = 0
        self._ClientHandle_fmt = '<I'
        self._ClientHandle_fmt_size = 4
        self.Value = DataValue()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack(self._ClientHandle_fmt, self.ClientHandle))
        tmp.append(self.Value.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.ClientHandle = struct.unpack(self._ClientHandle_fmt, data.read(self._ClientHandle_fmt_size))[0]
            self.Value = DataValue.from_binary(data)
            return data
            
class EventNotificationList(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.Events = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack('<i', len(self.Events)))
        for i in Events:
            tmp.append(self.Events.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.Events = EventFieldList.from_binary(data)
            return data
            
class EventFieldList(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.ClientHandle = 0
        self._ClientHandle_fmt = '<I'
        self._ClientHandle_fmt_size = 4
        self.EventFields = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack(self._ClientHandle_fmt, self.ClientHandle))
        tmp.append(struct.pack('<i', len(self.EventFields)))
        for i in EventFields:
            tmp.append(self.EventFields.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.ClientHandle = struct.unpack(self._ClientHandle_fmt, data.read(self._ClientHandle_fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.EventFields = Variant.from_binary(data)
            return data
            
class HistoryEventFieldList(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.EventFields = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack('<i', len(self.EventFields)))
        for i in EventFields:
            tmp.append(self.EventFields.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.EventFields = Variant.from_binary(data)
            return data
            
class StatusChangeNotification(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.Status = StatusCode()
        self.DiagnosticInfo = DiagnosticInfo()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.Status.to_binary())
        tmp.append(self.DiagnosticInfo.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.Status = StatusCode.from_binary(data)
            self.DiagnosticInfo = DiagnosticInfo.from_binary(data)
            return data
            
class SubscriptionAcknowledgement(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.SubscriptionId = 0
        self._SubscriptionId_fmt = '<I'
        self._SubscriptionId_fmt_size = 4
        self.SequenceNumber = 0
        self._SequenceNumber_fmt = '<I'
        self._SequenceNumber_fmt_size = 4
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack(self._SubscriptionId_fmt, self.SubscriptionId))
        tmp.append(struct.pack(self._SequenceNumber_fmt, self.SequenceNumber))
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.SubscriptionId = struct.unpack(self._SubscriptionId_fmt, data.read(self._SubscriptionId_fmt_size))[0]
            self.SequenceNumber = struct.unpack(self._SequenceNumber_fmt, data.read(self._SequenceNumber_fmt_size))[0]
            return data
            
class PublishParameters(object):
    def __init__(self):
        self.SubscriptionAcknowledgements = []
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack('<i', len(self.SubscriptionAcknowledgements)))
        for i in SubscriptionAcknowledgements:
            tmp.append(self.SubscriptionAcknowledgements.to_binary())
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
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = PublishParameters.from_binary(data)
            return data
            
class PublishResult(object):
    def __init__(self):
        self.SubscriptionId = 0
        self._SubscriptionId_fmt = '<I'
        self._SubscriptionId_fmt_size = 4
        self.AvailableSequenceNumbers = []
        self._AvailableSequenceNumbers_fmt = '<I'
        self._AvailableSequenceNumbers_fmt_size = 4
        self.MoreNotifications = 0
        self._MoreNotifications_fmt = '<?'
        self._MoreNotifications_fmt_size = 1
        self.NotificationMessage = NotificationMessage()
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack(self._SubscriptionId_fmt, self.SubscriptionId))
        tmp.append(struct.pack('<i', len(self.AvailableSequenceNumbers)))
        for i in AvailableSequenceNumbers:
            tmp.append(struct.pack(self._AvailableSequenceNumbers_fmt, self.AvailableSequenceNumbers))
        tmp.append(struct.pack(self._MoreNotifications_fmt, self.MoreNotifications))
        tmp.append(self.NotificationMessage.to_binary())
        tmp.append(struct.pack('<i', len(self.Results)))
        for i in Results:
            tmp.append(self.Results.to_binary())
        tmp.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for i in DiagnosticInfos:
            tmp.append(self.DiagnosticInfos.to_binary())
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.SubscriptionId = struct.unpack(self._SubscriptionId_fmt, data.read(self._SubscriptionId_fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.AvailableSequenceNumbers = struct.unpack(self._AvailableSequenceNumbers_fmt, data.read(self._AvailableSequenceNumbers_fmt_size))[0]
            self.MoreNotifications = struct.unpack(self._MoreNotifications_fmt, data.read(self._MoreNotifications_fmt_size))[0]
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
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            self.Parameters = PublishResult.from_binary(data)
            return data
            
class RepublishParameters(object):
    def __init__(self):
        self.SubscriptionId = 0
        self._SubscriptionId_fmt = '<I'
        self._SubscriptionId_fmt_size = 4
        self.RetransmitSequenceNumber = 0
        self._RetransmitSequenceNumber_fmt = '<I'
        self._RetransmitSequenceNumber_fmt_size = 4
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack(self._SubscriptionId_fmt, self.SubscriptionId))
        tmp.append(struct.pack(self._RetransmitSequenceNumber_fmt, self.RetransmitSequenceNumber))
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.SubscriptionId = struct.unpack(self._SubscriptionId_fmt, data.read(self._SubscriptionId_fmt_size))[0]
            self.RetransmitSequenceNumber = struct.unpack(self._RetransmitSequenceNumber_fmt, data.read(self._RetransmitSequenceNumber_fmt_size))[0]
            return data
            
class RepublishRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.RepublishRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
        self.RequestHeader = RequestHeader()
        self.Parameters = RepublishParameters()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = RepublishParameters.from_binary(data)
            return data
            
class RepublishResult(object):
    def __init__(self):
        self.NotificationMessage = NotificationMessage()
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(self.NotificationMessage.to_binary())
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
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            self.Parameters = RepublishResult.from_binary(data)
            return data
            
class TransferResult(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.StatusCode = StatusCode()
        self.AvailableSequenceNumbers = []
        self._AvailableSequenceNumbers_fmt = '<I'
        self._AvailableSequenceNumbers_fmt_size = 4
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.StatusCode.to_binary())
        tmp.append(struct.pack('<i', len(self.AvailableSequenceNumbers)))
        for i in AvailableSequenceNumbers:
            tmp.append(struct.pack(self._AvailableSequenceNumbers_fmt, self.AvailableSequenceNumbers))
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.StatusCode = StatusCode.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.AvailableSequenceNumbers = struct.unpack(self._AvailableSequenceNumbers_fmt, data.read(self._AvailableSequenceNumbers_fmt_size))[0]
            return data
            
class TransferSubscriptionsParameters(object):
    def __init__(self):
        self.SubscriptionIds = []
        self._SubscriptionIds_fmt = '<I'
        self._SubscriptionIds_fmt_size = 4
        self.SendInitialValues = 0
        self._SendInitialValues_fmt = '<?'
        self._SendInitialValues_fmt_size = 1
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack('<i', len(self.SubscriptionIds)))
        for i in SubscriptionIds:
            tmp.append(struct.pack(self._SubscriptionIds_fmt, self.SubscriptionIds))
        tmp.append(struct.pack(self._SendInitialValues_fmt, self.SendInitialValues))
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.SubscriptionIds = struct.unpack(self._SubscriptionIds_fmt, data.read(self._SubscriptionIds_fmt_size))[0]
            self.SendInitialValues = struct.unpack(self._SendInitialValues_fmt, data.read(self._SendInitialValues_fmt_size))[0]
            return data
            
class TransferSubscriptionsRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.TransferSubscriptionsRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
        self.RequestHeader = RequestHeader()
        self.Parameters = TransferSubscriptionsParameters()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = TransferSubscriptionsParameters.from_binary(data)
            return data
            
class TransferSubscriptionsResult(object):
    def __init__(self):
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack('<i', len(self.Results)))
        for i in Results:
            tmp.append(self.Results.to_binary())
        tmp.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for i in DiagnosticInfos:
            tmp.append(self.DiagnosticInfos.to_binary())
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
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            self.Parameters = TransferSubscriptionsResult.from_binary(data)
            return data
            
class DeleteSubscriptionsParameters(object):
    def __init__(self):
        self.SubscriptionIds = []
        self._SubscriptionIds_fmt = '<I'
        self._SubscriptionIds_fmt_size = 4
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack('<i', len(self.SubscriptionIds)))
        for i in SubscriptionIds:
            tmp.append(struct.pack(self._SubscriptionIds_fmt, self.SubscriptionIds))
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.SubscriptionIds = struct.unpack(self._SubscriptionIds_fmt, data.read(self._SubscriptionIds_fmt_size))[0]
            return data
            
class DeleteSubscriptionsRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.DeleteSubscriptionsRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
        self.RequestHeader = RequestHeader()
        self.Parameters = DeleteSubscriptionsParameters()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = DeleteSubscriptionsParameters.from_binary(data)
            return data
            
class DeleteSubscriptionsResult(object):
    def __init__(self):
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack('<i', len(self.Results)))
        for i in Results:
            tmp.append(self.Results.to_binary())
        tmp.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for i in DiagnosticInfos:
            tmp.append(self.DiagnosticInfos.to_binary())
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
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            self.Parameters = DeleteSubscriptionsResult.from_binary(data)
            return data
            
class ScalarTestType(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.Boolean = 0
        self._Boolean_fmt = '<?'
        self._Boolean_fmt_size = 1
        self.SByte = SByte()
        self._SByte_fmt = '<B'
        self._SByte_fmt_size = 1
        self.Byte = 0
        self._Byte_fmt = '<B'
        self._Byte_fmt_size = 1
        self.Int16 = 0
        self._Int16_fmt = '<h'
        self._Int16_fmt_size = 2
        self.UInt16 = 0
        self._UInt16_fmt = '<H'
        self._UInt16_fmt_size = 2
        self.Int32 = 0
        self._Int32_fmt = '<i'
        self._Int32_fmt_size = 4
        self.UInt32 = 0
        self._UInt32_fmt = '<I'
        self._UInt32_fmt_size = 4
        self.Int64 = 0
        self._Int64_fmt = '<q'
        self._Int64_fmt_size = 8
        self.UInt64 = 0
        self._UInt64_fmt = '<Q'
        self._UInt64_fmt_size = 8
        self.Float = 0
        self._Float_fmt = '<f'
        self._Float_fmt_size = 4
        self.Double = 0
        self._Double_fmt = '<d'
        self._Double_fmt_size = 8
        self.String = ''
        self._String_fmt = '<s'
        self._String_fmt_size = 1
        self.DateTime = 0
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
        self.EnumeratedValue = EnumeratedTestType()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack(self._Boolean_fmt, self.Boolean))
        tmp.append(struct.pack(self._SByte_fmt, self.SByte))
        tmp.append(struct.pack(self._Byte_fmt, self.Byte))
        tmp.append(struct.pack(self._Int16_fmt, self.Int16))
        tmp.append(struct.pack(self._UInt16_fmt, self.UInt16))
        tmp.append(struct.pack(self._Int32_fmt, self.Int32))
        tmp.append(struct.pack(self._UInt32_fmt, self.UInt32))
        tmp.append(struct.pack(self._Int64_fmt, self.Int64))
        tmp.append(struct.pack(self._UInt64_fmt, self.UInt64))
        tmp.append(struct.pack(self._Float_fmt, self.Float))
        tmp.append(struct.pack(self._Double_fmt, self.Double))
        tmp.append(struct.pack('<i', len(self.String)))
        tmp.append(struct.pack('<{}s'.format(len(self.String)), self.String.encode()))
        tmp.append(self.DateTime.to_binary())
        tmp.append(self.Guid.to_binary())
        tmp.append(self.ByteString.to_binary())
        tmp.append(self.XmlElement.to_binary())
        tmp.append(self.NodeId.to_binary())
        tmp.append(self.ExpandedNodeId.to_binary())
        tmp.append(self.StatusCode.to_binary())
        tmp.append(self.DiagnosticInfo.to_binary())
        tmp.append(self.QualifiedName.to_binary())
        tmp.append(self.LocalizedText.to_binary())
        tmp.append(self.ExtensionObject.to_binary())
        tmp.append(self.DataValue.to_binary())
        tmp.append(self.EnumeratedValue.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.Boolean = struct.unpack(self._Boolean_fmt, data.read(self._Boolean_fmt_size))[0]
            self.SByte = struct.unpack(self._SByte_fmt, data.read(self._SByte_fmt_size))[0]
            self.Byte = struct.unpack(self._Byte_fmt, data.read(self._Byte_fmt_size))[0]
            self.Int16 = struct.unpack(self._Int16_fmt, data.read(self._Int16_fmt_size))[0]
            self.UInt16 = struct.unpack(self._UInt16_fmt, data.read(self._UInt16_fmt_size))[0]
            self.Int32 = struct.unpack(self._Int32_fmt, data.read(self._Int32_fmt_size))[0]
            self.UInt32 = struct.unpack(self._UInt32_fmt, data.read(self._UInt32_fmt_size))[0]
            self.Int64 = struct.unpack(self._Int64_fmt, data.read(self._Int64_fmt_size))[0]
            self.UInt64 = struct.unpack(self._UInt64_fmt, data.read(self._UInt64_fmt_size))[0]
            self.Float = struct.unpack(self._Float_fmt, data.read(self._Float_fmt_size))[0]
            self.Double = struct.unpack(self._Double_fmt, data.read(self._Double_fmt_size))[0]
            slength = struct.unpack('<i', data.red(1))
            self.String = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.String = struct.unpack(self._String_fmt, data.read(self._String_fmt_size))[0]
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
            self.EnumeratedValue = EnumeratedTestType.from_binary(data)
            return data
            
class ArrayTestType(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.Booleans = []
        self._Booleans_fmt = '<?'
        self._Booleans_fmt_size = 1
        self.SBytes = []
        self._SBytes_fmt = '<B'
        self._SBytes_fmt_size = 1
        self.Int16s = []
        self._Int16s_fmt = '<h'
        self._Int16s_fmt_size = 2
        self.UInt16s = []
        self._UInt16s_fmt = '<H'
        self._UInt16s_fmt_size = 2
        self.Int32s = []
        self._Int32s_fmt = '<i'
        self._Int32s_fmt_size = 4
        self.UInt32s = []
        self._UInt32s_fmt = '<I'
        self._UInt32s_fmt_size = 4
        self.Int64s = []
        self._Int64s_fmt = '<q'
        self._Int64s_fmt_size = 8
        self.UInt64s = []
        self._UInt64s_fmt = '<Q'
        self._UInt64s_fmt_size = 8
        self.Floats = []
        self._Floats_fmt = '<f'
        self._Floats_fmt_size = 4
        self.Doubles = []
        self._Doubles_fmt = '<d'
        self._Doubles_fmt_size = 8
        self.Strings = []
        self._Strings_fmt = '<s'
        self._Strings_fmt_size = 1
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
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack('<i', len(self.Booleans)))
        for i in Booleans:
            tmp.append(struct.pack(self._Booleans_fmt, self.Booleans))
        tmp.append(struct.pack('<i', len(self.SBytes)))
        for i in SBytes:
            tmp.append(struct.pack(self._SBytes_fmt, self.SBytes))
        tmp.append(struct.pack('<i', len(self.Int16s)))
        for i in Int16s:
            tmp.append(struct.pack(self._Int16s_fmt, self.Int16s))
        tmp.append(struct.pack('<i', len(self.UInt16s)))
        for i in UInt16s:
            tmp.append(struct.pack(self._UInt16s_fmt, self.UInt16s))
        tmp.append(struct.pack('<i', len(self.Int32s)))
        for i in Int32s:
            tmp.append(struct.pack(self._Int32s_fmt, self.Int32s))
        tmp.append(struct.pack('<i', len(self.UInt32s)))
        for i in UInt32s:
            tmp.append(struct.pack(self._UInt32s_fmt, self.UInt32s))
        tmp.append(struct.pack('<i', len(self.Int64s)))
        for i in Int64s:
            tmp.append(struct.pack(self._Int64s_fmt, self.Int64s))
        tmp.append(struct.pack('<i', len(self.UInt64s)))
        for i in UInt64s:
            tmp.append(struct.pack(self._UInt64s_fmt, self.UInt64s))
        tmp.append(struct.pack('<i', len(self.Floats)))
        for i in Floats:
            tmp.append(struct.pack(self._Floats_fmt, self.Floats))
        tmp.append(struct.pack('<i', len(self.Doubles)))
        for i in Doubles:
            tmp.append(struct.pack(self._Doubles_fmt, self.Doubles))
        tmp.append(struct.pack('<i', len(self.Strings)))
        for i in Strings:
            tmp.append(struct.pack('<i', len(self.Strings)))
            tmp.append(struct.pack('<{}s'.format(len(self.Strings)), self.Strings.encode()))
        tmp.append(struct.pack('<i', len(self.DateTimes)))
        for i in DateTimes:
            tmp.append(self.DateTimes.to_binary())
        tmp.append(struct.pack('<i', len(self.Guids)))
        for i in Guids:
            tmp.append(self.Guids.to_binary())
        tmp.append(struct.pack('<i', len(self.ByteStrings)))
        for i in ByteStrings:
            tmp.append(self.ByteStrings.to_binary())
        tmp.append(struct.pack('<i', len(self.XmlElements)))
        for i in XmlElements:
            tmp.append(self.XmlElements.to_binary())
        tmp.append(struct.pack('<i', len(self.NodeIds)))
        for i in NodeIds:
            tmp.append(self.NodeIds.to_binary())
        tmp.append(struct.pack('<i', len(self.ExpandedNodeIds)))
        for i in ExpandedNodeIds:
            tmp.append(self.ExpandedNodeIds.to_binary())
        tmp.append(struct.pack('<i', len(self.StatusCodes)))
        for i in StatusCodes:
            tmp.append(self.StatusCodes.to_binary())
        tmp.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for i in DiagnosticInfos:
            tmp.append(self.DiagnosticInfos.to_binary())
        tmp.append(struct.pack('<i', len(self.QualifiedNames)))
        for i in QualifiedNames:
            tmp.append(self.QualifiedNames.to_binary())
        tmp.append(struct.pack('<i', len(self.LocalizedTexts)))
        for i in LocalizedTexts:
            tmp.append(self.LocalizedTexts.to_binary())
        tmp.append(struct.pack('<i', len(self.ExtensionObjects)))
        for i in ExtensionObjects:
            tmp.append(self.ExtensionObjects.to_binary())
        tmp.append(struct.pack('<i', len(self.DataValues)))
        for i in DataValues:
            tmp.append(self.DataValues.to_binary())
        tmp.append(struct.pack('<i', len(self.Variants)))
        for i in Variants:
            tmp.append(self.Variants.to_binary())
        tmp.append(struct.pack('<i', len(self.EnumeratedValues)))
        for i in EnumeratedValues:
            tmp.append(self.EnumeratedValues.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.Booleans = struct.unpack(self._Booleans_fmt, data.read(self._Booleans_fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.SBytes = struct.unpack(self._SBytes_fmt, data.read(self._SBytes_fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.Int16s = struct.unpack(self._Int16s_fmt, data.read(self._Int16s_fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.UInt16s = struct.unpack(self._UInt16s_fmt, data.read(self._UInt16s_fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.Int32s = struct.unpack(self._Int32s_fmt, data.read(self._Int32s_fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.UInt32s = struct.unpack(self._UInt32s_fmt, data.read(self._UInt32s_fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.Int64s = struct.unpack(self._Int64s_fmt, data.read(self._Int64s_fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.UInt64s = struct.unpack(self._UInt64s_fmt, data.read(self._UInt64s_fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.Floats = struct.unpack(self._Floats_fmt, data.read(self._Floats_fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.Doubles = struct.unpack(self._Doubles_fmt, data.read(self._Doubles_fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    slength = struct.unpack('<i', data.red(1))
                    self.Strings = struct.unpack('<{}s'.format(slength), data.read(slength))
                    self.Strings = struct.unpack(self._Strings_fmt, data.read(self._Strings_fmt_size))[0]
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
                    self.EnumeratedValues = EnumeratedTestType.from_binary(data)
            return data
            
class CompositeTestType(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.Field1 = ScalarTestType()
        self.Field2 = ArrayTestType()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.Field1.to_binary())
        tmp.append(self.Field2.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.Field1 = ScalarTestType.from_binary(data)
            self.Field2 = ArrayTestType.from_binary(data)
            return data
            
class TestStackParameters(object):
    def __init__(self):
        self.TestId = 0
        self._TestId_fmt = '<I'
        self._TestId_fmt_size = 4
        self.Iteration = 0
        self._Iteration_fmt = '<i'
        self._Iteration_fmt_size = 4
        self.Input = Variant()
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack(self._TestId_fmt, self.TestId))
        tmp.append(struct.pack(self._Iteration_fmt, self.Iteration))
        tmp.append(self.Input.to_binary())
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TestId = struct.unpack(self._TestId_fmt, data.read(self._TestId_fmt_size))[0]
            self.Iteration = struct.unpack(self._Iteration_fmt, data.read(self._Iteration_fmt_size))[0]
            self.Input = Variant.from_binary(data)
            return data
            
class TestStackRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.TestStackRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
        self.RequestHeader = RequestHeader()
        self.Parameters = TestStackParameters()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = TestStackParameters.from_binary(data)
            return data
            
class TestStackResult(object):
    def __init__(self):
        self.Output = Variant()
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(self.Output.to_binary())
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
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            self.Parameters = TestStackResult.from_binary(data)
            return data
            
class TestStackExParameters(object):
    def __init__(self):
        self.TestId = 0
        self._TestId_fmt = '<I'
        self._TestId_fmt_size = 4
        self.Iteration = 0
        self._Iteration_fmt = '<i'
        self._Iteration_fmt_size = 4
        self.Input = CompositeTestType()
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack(self._TestId_fmt, self.TestId))
        tmp.append(struct.pack(self._Iteration_fmt, self.Iteration))
        tmp.append(self.Input.to_binary())
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TestId = struct.unpack(self._TestId_fmt, data.read(self._TestId_fmt_size))[0]
            self.Iteration = struct.unpack(self._Iteration_fmt, data.read(self._Iteration_fmt_size))[0]
            self.Input = CompositeTestType.from_binary(data)
            return data
            
class TestStackExRequest(object):
    def __init__(self):
        self.TypeId = NodeId(0, ObjectIds.TestStackExRequest_Encoding_DefaultBinary, NodeIdType.FourByte)
        self.RequestHeader = RequestHeader()
        self.Parameters = TestStackExParameters()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.RequestHeader = RequestHeader.from_binary(data)
            self.Parameters = TestStackExParameters.from_binary(data)
            return data
            
class TestStackExResult(object):
    def __init__(self):
        self.Output = CompositeTestType()
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(self.Output.to_binary())
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
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(self.Parameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.ResponseHeader = ResponseHeader.from_binary(data)
            self.Parameters = TestStackExResult.from_binary(data)
            return data
            
class BuildInfo(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.ProductUri = ''
        self._ProductUri_fmt = '<s'
        self._ProductUri_fmt_size = 1
        self.ManufacturerName = ''
        self._ManufacturerName_fmt = '<s'
        self._ManufacturerName_fmt_size = 1
        self.ProductName = ''
        self._ProductName_fmt = '<s'
        self._ProductName_fmt_size = 1
        self.SoftwareVersion = ''
        self._SoftwareVersion_fmt = '<s'
        self._SoftwareVersion_fmt_size = 1
        self.BuildNumber = ''
        self._BuildNumber_fmt = '<s'
        self._BuildNumber_fmt_size = 1
        self.BuildDate = 0
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack('<i', len(self.ProductUri)))
        tmp.append(struct.pack('<{}s'.format(len(self.ProductUri)), self.ProductUri.encode()))
        tmp.append(struct.pack('<i', len(self.ManufacturerName)))
        tmp.append(struct.pack('<{}s'.format(len(self.ManufacturerName)), self.ManufacturerName.encode()))
        tmp.append(struct.pack('<i', len(self.ProductName)))
        tmp.append(struct.pack('<{}s'.format(len(self.ProductName)), self.ProductName.encode()))
        tmp.append(struct.pack('<i', len(self.SoftwareVersion)))
        tmp.append(struct.pack('<{}s'.format(len(self.SoftwareVersion)), self.SoftwareVersion.encode()))
        tmp.append(struct.pack('<i', len(self.BuildNumber)))
        tmp.append(struct.pack('<{}s'.format(len(self.BuildNumber)), self.BuildNumber.encode()))
        tmp.append(self.BuildDate.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            slength = struct.unpack('<i', data.red(1))
            self.ProductUri = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.ProductUri = struct.unpack(self._ProductUri_fmt, data.read(self._ProductUri_fmt_size))[0]
            slength = struct.unpack('<i', data.red(1))
            self.ManufacturerName = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.ManufacturerName = struct.unpack(self._ManufacturerName_fmt, data.read(self._ManufacturerName_fmt_size))[0]
            slength = struct.unpack('<i', data.red(1))
            self.ProductName = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.ProductName = struct.unpack(self._ProductName_fmt, data.read(self._ProductName_fmt_size))[0]
            slength = struct.unpack('<i', data.red(1))
            self.SoftwareVersion = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.SoftwareVersion = struct.unpack(self._SoftwareVersion_fmt, data.read(self._SoftwareVersion_fmt_size))[0]
            slength = struct.unpack('<i', data.red(1))
            self.BuildNumber = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.BuildNumber = struct.unpack(self._BuildNumber_fmt, data.read(self._BuildNumber_fmt_size))[0]
            self.BuildDate = DateTime.from_binary(data)
            return data
            
class RedundantServerDataType(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.ServerId = ''
        self._ServerId_fmt = '<s'
        self._ServerId_fmt_size = 1
        self.ServiceLevel = 0
        self._ServiceLevel_fmt = '<B'
        self._ServiceLevel_fmt_size = 1
        self.ServerState = 0
        self._ServerState_fmt = '<I'
        self._ServerState_fmt_size = 4
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack('<i', len(self.ServerId)))
        tmp.append(struct.pack('<{}s'.format(len(self.ServerId)), self.ServerId.encode()))
        tmp.append(struct.pack(self._ServiceLevel_fmt, self.ServiceLevel))
        tmp.append(struct.pack(self._ServerState_fmt, self.ServerState))
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            slength = struct.unpack('<i', data.red(1))
            self.ServerId = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.ServerId = struct.unpack(self._ServerId_fmt, data.read(self._ServerId_fmt_size))[0]
            self.ServiceLevel = struct.unpack(self._ServiceLevel_fmt, data.read(self._ServiceLevel_fmt_size))[0]
            self.ServerState = struct.unpack(self._ServerState_fmt, data.read(self._ServerState_fmt_size))[0]
            return data
            
class EndpointUrlListDataType(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.EndpointUrlList = []
        self._EndpointUrlList_fmt = '<s'
        self._EndpointUrlList_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack('<i', len(self.EndpointUrlList)))
        for i in EndpointUrlList:
            tmp.append(struct.pack('<i', len(self.EndpointUrlList)))
            tmp.append(struct.pack('<{}s'.format(len(self.EndpointUrlList)), self.EndpointUrlList.encode()))
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    slength = struct.unpack('<i', data.red(1))
                    self.EndpointUrlList = struct.unpack('<{}s'.format(slength), data.read(slength))
                    self.EndpointUrlList = struct.unpack(self._EndpointUrlList_fmt, data.read(self._EndpointUrlList_fmt_size))[0]
            return data
            
class NetworkGroupDataType(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.ServerUri = ''
        self._ServerUri_fmt = '<s'
        self._ServerUri_fmt_size = 1
        self.NetworkPaths = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack('<i', len(self.ServerUri)))
        tmp.append(struct.pack('<{}s'.format(len(self.ServerUri)), self.ServerUri.encode()))
        tmp.append(struct.pack('<i', len(self.NetworkPaths)))
        for i in NetworkPaths:
            tmp.append(self.NetworkPaths.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            slength = struct.unpack('<i', data.red(1))
            self.ServerUri = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.ServerUri = struct.unpack(self._ServerUri_fmt, data.read(self._ServerUri_fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.NetworkPaths = EndpointUrlListDataType.from_binary(data)
            return data
            
class SamplingIntervalDiagnosticsDataType(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.SamplingInterval = 0
        self._SamplingInterval_fmt = '<d'
        self._SamplingInterval_fmt_size = 8
        self.MonitoredItemCount = 0
        self._MonitoredItemCount_fmt = '<I'
        self._MonitoredItemCount_fmt_size = 4
        self.MaxMonitoredItemCount = 0
        self._MaxMonitoredItemCount_fmt = '<I'
        self._MaxMonitoredItemCount_fmt_size = 4
        self.DisabledMonitoredItemCount = 0
        self._DisabledMonitoredItemCount_fmt = '<I'
        self._DisabledMonitoredItemCount_fmt_size = 4
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack(self._SamplingInterval_fmt, self.SamplingInterval))
        tmp.append(struct.pack(self._MonitoredItemCount_fmt, self.MonitoredItemCount))
        tmp.append(struct.pack(self._MaxMonitoredItemCount_fmt, self.MaxMonitoredItemCount))
        tmp.append(struct.pack(self._DisabledMonitoredItemCount_fmt, self.DisabledMonitoredItemCount))
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.SamplingInterval = struct.unpack(self._SamplingInterval_fmt, data.read(self._SamplingInterval_fmt_size))[0]
            self.MonitoredItemCount = struct.unpack(self._MonitoredItemCount_fmt, data.read(self._MonitoredItemCount_fmt_size))[0]
            self.MaxMonitoredItemCount = struct.unpack(self._MaxMonitoredItemCount_fmt, data.read(self._MaxMonitoredItemCount_fmt_size))[0]
            self.DisabledMonitoredItemCount = struct.unpack(self._DisabledMonitoredItemCount_fmt, data.read(self._DisabledMonitoredItemCount_fmt_size))[0]
            return data
            
class ServerDiagnosticsSummaryDataType(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.ServerViewCount = 0
        self._ServerViewCount_fmt = '<I'
        self._ServerViewCount_fmt_size = 4
        self.CurrentSessionCount = 0
        self._CurrentSessionCount_fmt = '<I'
        self._CurrentSessionCount_fmt_size = 4
        self.CumulatedSessionCount = 0
        self._CumulatedSessionCount_fmt = '<I'
        self._CumulatedSessionCount_fmt_size = 4
        self.SecurityRejectedSessionCount = 0
        self._SecurityRejectedSessionCount_fmt = '<I'
        self._SecurityRejectedSessionCount_fmt_size = 4
        self.RejectedSessionCount = 0
        self._RejectedSessionCount_fmt = '<I'
        self._RejectedSessionCount_fmt_size = 4
        self.SessionTimeoutCount = 0
        self._SessionTimeoutCount_fmt = '<I'
        self._SessionTimeoutCount_fmt_size = 4
        self.SessionAbortCount = 0
        self._SessionAbortCount_fmt = '<I'
        self._SessionAbortCount_fmt_size = 4
        self.CurrentSubscriptionCount = 0
        self._CurrentSubscriptionCount_fmt = '<I'
        self._CurrentSubscriptionCount_fmt_size = 4
        self.CumulatedSubscriptionCount = 0
        self._CumulatedSubscriptionCount_fmt = '<I'
        self._CumulatedSubscriptionCount_fmt_size = 4
        self.PublishingIntervalCount = 0
        self._PublishingIntervalCount_fmt = '<I'
        self._PublishingIntervalCount_fmt_size = 4
        self.SecurityRejectedRequestsCount = 0
        self._SecurityRejectedRequestsCount_fmt = '<I'
        self._SecurityRejectedRequestsCount_fmt_size = 4
        self.RejectedRequestsCount = 0
        self._RejectedRequestsCount_fmt = '<I'
        self._RejectedRequestsCount_fmt_size = 4
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack(self._ServerViewCount_fmt, self.ServerViewCount))
        tmp.append(struct.pack(self._CurrentSessionCount_fmt, self.CurrentSessionCount))
        tmp.append(struct.pack(self._CumulatedSessionCount_fmt, self.CumulatedSessionCount))
        tmp.append(struct.pack(self._SecurityRejectedSessionCount_fmt, self.SecurityRejectedSessionCount))
        tmp.append(struct.pack(self._RejectedSessionCount_fmt, self.RejectedSessionCount))
        tmp.append(struct.pack(self._SessionTimeoutCount_fmt, self.SessionTimeoutCount))
        tmp.append(struct.pack(self._SessionAbortCount_fmt, self.SessionAbortCount))
        tmp.append(struct.pack(self._CurrentSubscriptionCount_fmt, self.CurrentSubscriptionCount))
        tmp.append(struct.pack(self._CumulatedSubscriptionCount_fmt, self.CumulatedSubscriptionCount))
        tmp.append(struct.pack(self._PublishingIntervalCount_fmt, self.PublishingIntervalCount))
        tmp.append(struct.pack(self._SecurityRejectedRequestsCount_fmt, self.SecurityRejectedRequestsCount))
        tmp.append(struct.pack(self._RejectedRequestsCount_fmt, self.RejectedRequestsCount))
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.ServerViewCount = struct.unpack(self._ServerViewCount_fmt, data.read(self._ServerViewCount_fmt_size))[0]
            self.CurrentSessionCount = struct.unpack(self._CurrentSessionCount_fmt, data.read(self._CurrentSessionCount_fmt_size))[0]
            self.CumulatedSessionCount = struct.unpack(self._CumulatedSessionCount_fmt, data.read(self._CumulatedSessionCount_fmt_size))[0]
            self.SecurityRejectedSessionCount = struct.unpack(self._SecurityRejectedSessionCount_fmt, data.read(self._SecurityRejectedSessionCount_fmt_size))[0]
            self.RejectedSessionCount = struct.unpack(self._RejectedSessionCount_fmt, data.read(self._RejectedSessionCount_fmt_size))[0]
            self.SessionTimeoutCount = struct.unpack(self._SessionTimeoutCount_fmt, data.read(self._SessionTimeoutCount_fmt_size))[0]
            self.SessionAbortCount = struct.unpack(self._SessionAbortCount_fmt, data.read(self._SessionAbortCount_fmt_size))[0]
            self.CurrentSubscriptionCount = struct.unpack(self._CurrentSubscriptionCount_fmt, data.read(self._CurrentSubscriptionCount_fmt_size))[0]
            self.CumulatedSubscriptionCount = struct.unpack(self._CumulatedSubscriptionCount_fmt, data.read(self._CumulatedSubscriptionCount_fmt_size))[0]
            self.PublishingIntervalCount = struct.unpack(self._PublishingIntervalCount_fmt, data.read(self._PublishingIntervalCount_fmt_size))[0]
            self.SecurityRejectedRequestsCount = struct.unpack(self._SecurityRejectedRequestsCount_fmt, data.read(self._SecurityRejectedRequestsCount_fmt_size))[0]
            self.RejectedRequestsCount = struct.unpack(self._RejectedRequestsCount_fmt, data.read(self._RejectedRequestsCount_fmt_size))[0]
            return data
            
class ServerStatusDataType(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.StartTime = 0
        self.CurrentTime = 0
        self.State = ServerState()
        self.BuildInfo = BuildInfo()
        self.SecondsTillShutdown = 0
        self._SecondsTillShutdown_fmt = '<I'
        self._SecondsTillShutdown_fmt_size = 4
        self.ShutdownReason = LocalizedText()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.StartTime.to_binary())
        tmp.append(self.CurrentTime.to_binary())
        tmp.append(self.State.to_binary())
        tmp.append(self.BuildInfo.to_binary())
        tmp.append(struct.pack(self._SecondsTillShutdown_fmt, self.SecondsTillShutdown))
        tmp.append(self.ShutdownReason.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.StartTime = DateTime.from_binary(data)
            self.CurrentTime = DateTime.from_binary(data)
            self.State = ServerState.from_binary(data)
            self.BuildInfo = BuildInfo.from_binary(data)
            self.SecondsTillShutdown = struct.unpack(self._SecondsTillShutdown_fmt, data.read(self._SecondsTillShutdown_fmt_size))[0]
            self.ShutdownReason = LocalizedText.from_binary(data)
            return data
            
class SessionDiagnosticsDataType(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.SessionId = NodeId()
        self.SessionName = ''
        self._SessionName_fmt = '<s'
        self._SessionName_fmt_size = 1
        self.ClientDescription = ApplicationDescription()
        self.ServerUri = ''
        self._ServerUri_fmt = '<s'
        self._ServerUri_fmt_size = 1
        self.EndpointUrl = ''
        self._EndpointUrl_fmt = '<s'
        self._EndpointUrl_fmt_size = 1
        self.LocaleIds = []
        self._LocaleIds_fmt = '<s'
        self._LocaleIds_fmt_size = 1
        self.ActualSessionTimeout = 0
        self._ActualSessionTimeout_fmt = '<d'
        self._ActualSessionTimeout_fmt_size = 8
        self.MaxResponseMessageSize = 0
        self._MaxResponseMessageSize_fmt = '<I'
        self._MaxResponseMessageSize_fmt_size = 4
        self.ClientConnectionTime = 0
        self.ClientLastContactTime = 0
        self.CurrentSubscriptionsCount = 0
        self._CurrentSubscriptionsCount_fmt = '<I'
        self._CurrentSubscriptionsCount_fmt_size = 4
        self.CurrentMonitoredItemsCount = 0
        self._CurrentMonitoredItemsCount_fmt = '<I'
        self._CurrentMonitoredItemsCount_fmt_size = 4
        self.CurrentPublishRequestsInQueue = 0
        self._CurrentPublishRequestsInQueue_fmt = '<I'
        self._CurrentPublishRequestsInQueue_fmt_size = 4
        self.TotalRequestCount = ServiceCounterDataType()
        self.UnauthorizedRequestCount = 0
        self._UnauthorizedRequestCount_fmt = '<I'
        self._UnauthorizedRequestCount_fmt_size = 4
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
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.SessionId.to_binary())
        tmp.append(struct.pack('<i', len(self.SessionName)))
        tmp.append(struct.pack('<{}s'.format(len(self.SessionName)), self.SessionName.encode()))
        tmp.append(self.ClientDescription.to_binary())
        tmp.append(struct.pack('<i', len(self.ServerUri)))
        tmp.append(struct.pack('<{}s'.format(len(self.ServerUri)), self.ServerUri.encode()))
        tmp.append(struct.pack('<i', len(self.EndpointUrl)))
        tmp.append(struct.pack('<{}s'.format(len(self.EndpointUrl)), self.EndpointUrl.encode()))
        tmp.append(struct.pack('<i', len(self.LocaleIds)))
        for i in LocaleIds:
            tmp.append(struct.pack('<i', len(self.LocaleIds)))
            tmp.append(struct.pack('<{}s'.format(len(self.LocaleIds)), self.LocaleIds.encode()))
        tmp.append(struct.pack(self._ActualSessionTimeout_fmt, self.ActualSessionTimeout))
        tmp.append(struct.pack(self._MaxResponseMessageSize_fmt, self.MaxResponseMessageSize))
        tmp.append(self.ClientConnectionTime.to_binary())
        tmp.append(self.ClientLastContactTime.to_binary())
        tmp.append(struct.pack(self._CurrentSubscriptionsCount_fmt, self.CurrentSubscriptionsCount))
        tmp.append(struct.pack(self._CurrentMonitoredItemsCount_fmt, self.CurrentMonitoredItemsCount))
        tmp.append(struct.pack(self._CurrentPublishRequestsInQueue_fmt, self.CurrentPublishRequestsInQueue))
        tmp.append(self.TotalRequestCount.to_binary())
        tmp.append(struct.pack(self._UnauthorizedRequestCount_fmt, self.UnauthorizedRequestCount))
        tmp.append(self.ReadCount.to_binary())
        tmp.append(self.HistoryReadCount.to_binary())
        tmp.append(self.WriteCount.to_binary())
        tmp.append(self.HistoryUpdateCount.to_binary())
        tmp.append(self.CallCount.to_binary())
        tmp.append(self.CreateMonitoredItemsCount.to_binary())
        tmp.append(self.ModifyMonitoredItemsCount.to_binary())
        tmp.append(self.SetMonitoringModeCount.to_binary())
        tmp.append(self.SetTriggeringCount.to_binary())
        tmp.append(self.DeleteMonitoredItemsCount.to_binary())
        tmp.append(self.CreateSubscriptionCount.to_binary())
        tmp.append(self.ModifySubscriptionCount.to_binary())
        tmp.append(self.SetPublishingModeCount.to_binary())
        tmp.append(self.PublishCount.to_binary())
        tmp.append(self.RepublishCount.to_binary())
        tmp.append(self.TransferSubscriptionsCount.to_binary())
        tmp.append(self.DeleteSubscriptionsCount.to_binary())
        tmp.append(self.AddNodesCount.to_binary())
        tmp.append(self.AddReferencesCount.to_binary())
        tmp.append(self.DeleteNodesCount.to_binary())
        tmp.append(self.DeleteReferencesCount.to_binary())
        tmp.append(self.BrowseCount.to_binary())
        tmp.append(self.BrowseNextCount.to_binary())
        tmp.append(self.TranslateBrowsePathsToNodeIdsCount.to_binary())
        tmp.append(self.QueryFirstCount.to_binary())
        tmp.append(self.QueryNextCount.to_binary())
        tmp.append(self.RegisterNodesCount.to_binary())
        tmp.append(self.UnregisterNodesCount.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.SessionId = NodeId.from_binary(data)
            slength = struct.unpack('<i', data.red(1))
            self.SessionName = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.SessionName = struct.unpack(self._SessionName_fmt, data.read(self._SessionName_fmt_size))[0]
            self.ClientDescription = ApplicationDescription.from_binary(data)
            slength = struct.unpack('<i', data.red(1))
            self.ServerUri = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.ServerUri = struct.unpack(self._ServerUri_fmt, data.read(self._ServerUri_fmt_size))[0]
            slength = struct.unpack('<i', data.red(1))
            self.EndpointUrl = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.EndpointUrl = struct.unpack(self._EndpointUrl_fmt, data.read(self._EndpointUrl_fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    slength = struct.unpack('<i', data.red(1))
                    self.LocaleIds = struct.unpack('<{}s'.format(slength), data.read(slength))
                    self.LocaleIds = struct.unpack(self._LocaleIds_fmt, data.read(self._LocaleIds_fmt_size))[0]
            self.ActualSessionTimeout = struct.unpack(self._ActualSessionTimeout_fmt, data.read(self._ActualSessionTimeout_fmt_size))[0]
            self.MaxResponseMessageSize = struct.unpack(self._MaxResponseMessageSize_fmt, data.read(self._MaxResponseMessageSize_fmt_size))[0]
            self.ClientConnectionTime = DateTime.from_binary(data)
            self.ClientLastContactTime = DateTime.from_binary(data)
            self.CurrentSubscriptionsCount = struct.unpack(self._CurrentSubscriptionsCount_fmt, data.read(self._CurrentSubscriptionsCount_fmt_size))[0]
            self.CurrentMonitoredItemsCount = struct.unpack(self._CurrentMonitoredItemsCount_fmt, data.read(self._CurrentMonitoredItemsCount_fmt_size))[0]
            self.CurrentPublishRequestsInQueue = struct.unpack(self._CurrentPublishRequestsInQueue_fmt, data.read(self._CurrentPublishRequestsInQueue_fmt_size))[0]
            self.TotalRequestCount = ServiceCounterDataType.from_binary(data)
            self.UnauthorizedRequestCount = struct.unpack(self._UnauthorizedRequestCount_fmt, data.read(self._UnauthorizedRequestCount_fmt_size))[0]
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
        self.TypeId = ExpandedNodeId()
        self.SessionId = NodeId()
        self.ClientUserIdOfSession = ''
        self._ClientUserIdOfSession_fmt = '<s'
        self._ClientUserIdOfSession_fmt_size = 1
        self.ClientUserIdHistory = []
        self._ClientUserIdHistory_fmt = '<s'
        self._ClientUserIdHistory_fmt_size = 1
        self.AuthenticationMechanism = ''
        self._AuthenticationMechanism_fmt = '<s'
        self._AuthenticationMechanism_fmt_size = 1
        self.Encoding = ''
        self._Encoding_fmt = '<s'
        self._Encoding_fmt_size = 1
        self.TransportProtocol = ''
        self._TransportProtocol_fmt = '<s'
        self._TransportProtocol_fmt_size = 1
        self.SecurityMode = MessageSecurityMode()
        self.SecurityPolicyUri = ''
        self._SecurityPolicyUri_fmt = '<s'
        self._SecurityPolicyUri_fmt_size = 1
        self.ClientCertificate = ByteString()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.SessionId.to_binary())
        tmp.append(struct.pack('<i', len(self.ClientUserIdOfSession)))
        tmp.append(struct.pack('<{}s'.format(len(self.ClientUserIdOfSession)), self.ClientUserIdOfSession.encode()))
        tmp.append(struct.pack('<i', len(self.ClientUserIdHistory)))
        for i in ClientUserIdHistory:
            tmp.append(struct.pack('<i', len(self.ClientUserIdHistory)))
            tmp.append(struct.pack('<{}s'.format(len(self.ClientUserIdHistory)), self.ClientUserIdHistory.encode()))
        tmp.append(struct.pack('<i', len(self.AuthenticationMechanism)))
        tmp.append(struct.pack('<{}s'.format(len(self.AuthenticationMechanism)), self.AuthenticationMechanism.encode()))
        tmp.append(struct.pack('<i', len(self.Encoding)))
        tmp.append(struct.pack('<{}s'.format(len(self.Encoding)), self.Encoding.encode()))
        tmp.append(struct.pack('<i', len(self.TransportProtocol)))
        tmp.append(struct.pack('<{}s'.format(len(self.TransportProtocol)), self.TransportProtocol.encode()))
        tmp.append(self.SecurityMode.to_binary())
        tmp.append(struct.pack('<i', len(self.SecurityPolicyUri)))
        tmp.append(struct.pack('<{}s'.format(len(self.SecurityPolicyUri)), self.SecurityPolicyUri.encode()))
        tmp.append(self.ClientCertificate.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.SessionId = NodeId.from_binary(data)
            slength = struct.unpack('<i', data.red(1))
            self.ClientUserIdOfSession = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.ClientUserIdOfSession = struct.unpack(self._ClientUserIdOfSession_fmt, data.read(self._ClientUserIdOfSession_fmt_size))[0]
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    slength = struct.unpack('<i', data.red(1))
                    self.ClientUserIdHistory = struct.unpack('<{}s'.format(slength), data.read(slength))
                    self.ClientUserIdHistory = struct.unpack(self._ClientUserIdHistory_fmt, data.read(self._ClientUserIdHistory_fmt_size))[0]
            slength = struct.unpack('<i', data.red(1))
            self.AuthenticationMechanism = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.AuthenticationMechanism = struct.unpack(self._AuthenticationMechanism_fmt, data.read(self._AuthenticationMechanism_fmt_size))[0]
            slength = struct.unpack('<i', data.red(1))
            self.Encoding = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))[0]
            slength = struct.unpack('<i', data.red(1))
            self.TransportProtocol = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.TransportProtocol = struct.unpack(self._TransportProtocol_fmt, data.read(self._TransportProtocol_fmt_size))[0]
            self.SecurityMode = MessageSecurityMode.from_binary(data)
            slength = struct.unpack('<i', data.red(1))
            self.SecurityPolicyUri = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.SecurityPolicyUri = struct.unpack(self._SecurityPolicyUri_fmt, data.read(self._SecurityPolicyUri_fmt_size))[0]
            self.ClientCertificate = ByteString.from_binary(data)
            return data
            
class ServiceCounterDataType(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.TotalCount = 0
        self._TotalCount_fmt = '<I'
        self._TotalCount_fmt_size = 4
        self.ErrorCount = 0
        self._ErrorCount_fmt = '<I'
        self._ErrorCount_fmt_size = 4
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack(self._TotalCount_fmt, self.TotalCount))
        tmp.append(struct.pack(self._ErrorCount_fmt, self.ErrorCount))
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.TotalCount = struct.unpack(self._TotalCount_fmt, data.read(self._TotalCount_fmt_size))[0]
            self.ErrorCount = struct.unpack(self._ErrorCount_fmt, data.read(self._ErrorCount_fmt_size))[0]
            return data
            
class StatusResult(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.StatusCode = StatusCode()
        self.DiagnosticInfo = DiagnosticInfo()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.StatusCode.to_binary())
        tmp.append(self.DiagnosticInfo.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.StatusCode = StatusCode.from_binary(data)
            self.DiagnosticInfo = DiagnosticInfo.from_binary(data)
            return data
            
class SubscriptionDiagnosticsDataType(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.SessionId = NodeId()
        self.SubscriptionId = 0
        self._SubscriptionId_fmt = '<I'
        self._SubscriptionId_fmt_size = 4
        self.Priority = 0
        self._Priority_fmt = '<B'
        self._Priority_fmt_size = 1
        self.PublishingInterval = 0
        self._PublishingInterval_fmt = '<d'
        self._PublishingInterval_fmt_size = 8
        self.MaxKeepAliveCount = 0
        self._MaxKeepAliveCount_fmt = '<I'
        self._MaxKeepAliveCount_fmt_size = 4
        self.MaxLifetimeCount = 0
        self._MaxLifetimeCount_fmt = '<I'
        self._MaxLifetimeCount_fmt_size = 4
        self.MaxNotificationsPerPublish = 0
        self._MaxNotificationsPerPublish_fmt = '<I'
        self._MaxNotificationsPerPublish_fmt_size = 4
        self.PublishingEnabled = 0
        self._PublishingEnabled_fmt = '<?'
        self._PublishingEnabled_fmt_size = 1
        self.ModifyCount = 0
        self._ModifyCount_fmt = '<I'
        self._ModifyCount_fmt_size = 4
        self.EnableCount = 0
        self._EnableCount_fmt = '<I'
        self._EnableCount_fmt_size = 4
        self.DisableCount = 0
        self._DisableCount_fmt = '<I'
        self._DisableCount_fmt_size = 4
        self.RepublishRequestCount = 0
        self._RepublishRequestCount_fmt = '<I'
        self._RepublishRequestCount_fmt_size = 4
        self.RepublishMessageRequestCount = 0
        self._RepublishMessageRequestCount_fmt = '<I'
        self._RepublishMessageRequestCount_fmt_size = 4
        self.RepublishMessageCount = 0
        self._RepublishMessageCount_fmt = '<I'
        self._RepublishMessageCount_fmt_size = 4
        self.TransferRequestCount = 0
        self._TransferRequestCount_fmt = '<I'
        self._TransferRequestCount_fmt_size = 4
        self.TransferredToAltClientCount = 0
        self._TransferredToAltClientCount_fmt = '<I'
        self._TransferredToAltClientCount_fmt_size = 4
        self.TransferredToSameClientCount = 0
        self._TransferredToSameClientCount_fmt = '<I'
        self._TransferredToSameClientCount_fmt_size = 4
        self.PublishRequestCount = 0
        self._PublishRequestCount_fmt = '<I'
        self._PublishRequestCount_fmt_size = 4
        self.DataChangeNotificationsCount = 0
        self._DataChangeNotificationsCount_fmt = '<I'
        self._DataChangeNotificationsCount_fmt_size = 4
        self.EventNotificationsCount = 0
        self._EventNotificationsCount_fmt = '<I'
        self._EventNotificationsCount_fmt_size = 4
        self.NotificationsCount = 0
        self._NotificationsCount_fmt = '<I'
        self._NotificationsCount_fmt_size = 4
        self.LatePublishRequestCount = 0
        self._LatePublishRequestCount_fmt = '<I'
        self._LatePublishRequestCount_fmt_size = 4
        self.CurrentKeepAliveCount = 0
        self._CurrentKeepAliveCount_fmt = '<I'
        self._CurrentKeepAliveCount_fmt_size = 4
        self.CurrentLifetimeCount = 0
        self._CurrentLifetimeCount_fmt = '<I'
        self._CurrentLifetimeCount_fmt_size = 4
        self.UnacknowledgedMessageCount = 0
        self._UnacknowledgedMessageCount_fmt = '<I'
        self._UnacknowledgedMessageCount_fmt_size = 4
        self.DiscardedMessageCount = 0
        self._DiscardedMessageCount_fmt = '<I'
        self._DiscardedMessageCount_fmt_size = 4
        self.MonitoredItemCount = 0
        self._MonitoredItemCount_fmt = '<I'
        self._MonitoredItemCount_fmt_size = 4
        self.DisabledMonitoredItemCount = 0
        self._DisabledMonitoredItemCount_fmt = '<I'
        self._DisabledMonitoredItemCount_fmt_size = 4
        self.MonitoringQueueOverflowCount = 0
        self._MonitoringQueueOverflowCount_fmt = '<I'
        self._MonitoringQueueOverflowCount_fmt_size = 4
        self.NextSequenceNumber = 0
        self._NextSequenceNumber_fmt = '<I'
        self._NextSequenceNumber_fmt_size = 4
        self.EventQueueOverFlowCount = 0
        self._EventQueueOverFlowCount_fmt = '<I'
        self._EventQueueOverFlowCount_fmt_size = 4
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.SessionId.to_binary())
        tmp.append(struct.pack(self._SubscriptionId_fmt, self.SubscriptionId))
        tmp.append(struct.pack(self._Priority_fmt, self.Priority))
        tmp.append(struct.pack(self._PublishingInterval_fmt, self.PublishingInterval))
        tmp.append(struct.pack(self._MaxKeepAliveCount_fmt, self.MaxKeepAliveCount))
        tmp.append(struct.pack(self._MaxLifetimeCount_fmt, self.MaxLifetimeCount))
        tmp.append(struct.pack(self._MaxNotificationsPerPublish_fmt, self.MaxNotificationsPerPublish))
        tmp.append(struct.pack(self._PublishingEnabled_fmt, self.PublishingEnabled))
        tmp.append(struct.pack(self._ModifyCount_fmt, self.ModifyCount))
        tmp.append(struct.pack(self._EnableCount_fmt, self.EnableCount))
        tmp.append(struct.pack(self._DisableCount_fmt, self.DisableCount))
        tmp.append(struct.pack(self._RepublishRequestCount_fmt, self.RepublishRequestCount))
        tmp.append(struct.pack(self._RepublishMessageRequestCount_fmt, self.RepublishMessageRequestCount))
        tmp.append(struct.pack(self._RepublishMessageCount_fmt, self.RepublishMessageCount))
        tmp.append(struct.pack(self._TransferRequestCount_fmt, self.TransferRequestCount))
        tmp.append(struct.pack(self._TransferredToAltClientCount_fmt, self.TransferredToAltClientCount))
        tmp.append(struct.pack(self._TransferredToSameClientCount_fmt, self.TransferredToSameClientCount))
        tmp.append(struct.pack(self._PublishRequestCount_fmt, self.PublishRequestCount))
        tmp.append(struct.pack(self._DataChangeNotificationsCount_fmt, self.DataChangeNotificationsCount))
        tmp.append(struct.pack(self._EventNotificationsCount_fmt, self.EventNotificationsCount))
        tmp.append(struct.pack(self._NotificationsCount_fmt, self.NotificationsCount))
        tmp.append(struct.pack(self._LatePublishRequestCount_fmt, self.LatePublishRequestCount))
        tmp.append(struct.pack(self._CurrentKeepAliveCount_fmt, self.CurrentKeepAliveCount))
        tmp.append(struct.pack(self._CurrentLifetimeCount_fmt, self.CurrentLifetimeCount))
        tmp.append(struct.pack(self._UnacknowledgedMessageCount_fmt, self.UnacknowledgedMessageCount))
        tmp.append(struct.pack(self._DiscardedMessageCount_fmt, self.DiscardedMessageCount))
        tmp.append(struct.pack(self._MonitoredItemCount_fmt, self.MonitoredItemCount))
        tmp.append(struct.pack(self._DisabledMonitoredItemCount_fmt, self.DisabledMonitoredItemCount))
        tmp.append(struct.pack(self._MonitoringQueueOverflowCount_fmt, self.MonitoringQueueOverflowCount))
        tmp.append(struct.pack(self._NextSequenceNumber_fmt, self.NextSequenceNumber))
        tmp.append(struct.pack(self._EventQueueOverFlowCount_fmt, self.EventQueueOverFlowCount))
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.SessionId = NodeId.from_binary(data)
            self.SubscriptionId = struct.unpack(self._SubscriptionId_fmt, data.read(self._SubscriptionId_fmt_size))[0]
            self.Priority = struct.unpack(self._Priority_fmt, data.read(self._Priority_fmt_size))[0]
            self.PublishingInterval = struct.unpack(self._PublishingInterval_fmt, data.read(self._PublishingInterval_fmt_size))[0]
            self.MaxKeepAliveCount = struct.unpack(self._MaxKeepAliveCount_fmt, data.read(self._MaxKeepAliveCount_fmt_size))[0]
            self.MaxLifetimeCount = struct.unpack(self._MaxLifetimeCount_fmt, data.read(self._MaxLifetimeCount_fmt_size))[0]
            self.MaxNotificationsPerPublish = struct.unpack(self._MaxNotificationsPerPublish_fmt, data.read(self._MaxNotificationsPerPublish_fmt_size))[0]
            self.PublishingEnabled = struct.unpack(self._PublishingEnabled_fmt, data.read(self._PublishingEnabled_fmt_size))[0]
            self.ModifyCount = struct.unpack(self._ModifyCount_fmt, data.read(self._ModifyCount_fmt_size))[0]
            self.EnableCount = struct.unpack(self._EnableCount_fmt, data.read(self._EnableCount_fmt_size))[0]
            self.DisableCount = struct.unpack(self._DisableCount_fmt, data.read(self._DisableCount_fmt_size))[0]
            self.RepublishRequestCount = struct.unpack(self._RepublishRequestCount_fmt, data.read(self._RepublishRequestCount_fmt_size))[0]
            self.RepublishMessageRequestCount = struct.unpack(self._RepublishMessageRequestCount_fmt, data.read(self._RepublishMessageRequestCount_fmt_size))[0]
            self.RepublishMessageCount = struct.unpack(self._RepublishMessageCount_fmt, data.read(self._RepublishMessageCount_fmt_size))[0]
            self.TransferRequestCount = struct.unpack(self._TransferRequestCount_fmt, data.read(self._TransferRequestCount_fmt_size))[0]
            self.TransferredToAltClientCount = struct.unpack(self._TransferredToAltClientCount_fmt, data.read(self._TransferredToAltClientCount_fmt_size))[0]
            self.TransferredToSameClientCount = struct.unpack(self._TransferredToSameClientCount_fmt, data.read(self._TransferredToSameClientCount_fmt_size))[0]
            self.PublishRequestCount = struct.unpack(self._PublishRequestCount_fmt, data.read(self._PublishRequestCount_fmt_size))[0]
            self.DataChangeNotificationsCount = struct.unpack(self._DataChangeNotificationsCount_fmt, data.read(self._DataChangeNotificationsCount_fmt_size))[0]
            self.EventNotificationsCount = struct.unpack(self._EventNotificationsCount_fmt, data.read(self._EventNotificationsCount_fmt_size))[0]
            self.NotificationsCount = struct.unpack(self._NotificationsCount_fmt, data.read(self._NotificationsCount_fmt_size))[0]
            self.LatePublishRequestCount = struct.unpack(self._LatePublishRequestCount_fmt, data.read(self._LatePublishRequestCount_fmt_size))[0]
            self.CurrentKeepAliveCount = struct.unpack(self._CurrentKeepAliveCount_fmt, data.read(self._CurrentKeepAliveCount_fmt_size))[0]
            self.CurrentLifetimeCount = struct.unpack(self._CurrentLifetimeCount_fmt, data.read(self._CurrentLifetimeCount_fmt_size))[0]
            self.UnacknowledgedMessageCount = struct.unpack(self._UnacknowledgedMessageCount_fmt, data.read(self._UnacknowledgedMessageCount_fmt_size))[0]
            self.DiscardedMessageCount = struct.unpack(self._DiscardedMessageCount_fmt, data.read(self._DiscardedMessageCount_fmt_size))[0]
            self.MonitoredItemCount = struct.unpack(self._MonitoredItemCount_fmt, data.read(self._MonitoredItemCount_fmt_size))[0]
            self.DisabledMonitoredItemCount = struct.unpack(self._DisabledMonitoredItemCount_fmt, data.read(self._DisabledMonitoredItemCount_fmt_size))[0]
            self.MonitoringQueueOverflowCount = struct.unpack(self._MonitoringQueueOverflowCount_fmt, data.read(self._MonitoringQueueOverflowCount_fmt_size))[0]
            self.NextSequenceNumber = struct.unpack(self._NextSequenceNumber_fmt, data.read(self._NextSequenceNumber_fmt_size))[0]
            self.EventQueueOverFlowCount = struct.unpack(self._EventQueueOverFlowCount_fmt, data.read(self._EventQueueOverFlowCount_fmt_size))[0]
            return data
            
class ModelChangeStructureDataType(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.Affected = NodeId()
        self.AffectedType = NodeId()
        self.Verb = 0
        self._Verb_fmt = '<B'
        self._Verb_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.Affected.to_binary())
        tmp.append(self.AffectedType.to_binary())
        tmp.append(struct.pack(self._Verb_fmt, self.Verb))
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.Affected = NodeId.from_binary(data)
            self.AffectedType = NodeId.from_binary(data)
            self.Verb = struct.unpack(self._Verb_fmt, data.read(self._Verb_fmt_size))[0]
            return data
            
class SemanticChangeStructureDataType(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.Affected = NodeId()
        self.AffectedType = NodeId()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.Affected.to_binary())
        tmp.append(self.AffectedType.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.Affected = NodeId.from_binary(data)
            self.AffectedType = NodeId.from_binary(data)
            return data
            
class Range(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.Low = 0
        self._Low_fmt = '<d'
        self._Low_fmt_size = 8
        self.High = 0
        self._High_fmt = '<d'
        self._High_fmt_size = 8
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack(self._Low_fmt, self.Low))
        tmp.append(struct.pack(self._High_fmt, self.High))
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.Low = struct.unpack(self._Low_fmt, data.read(self._Low_fmt_size))[0]
            self.High = struct.unpack(self._High_fmt, data.read(self._High_fmt_size))[0]
            return data
            
class EUInformation(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.NamespaceUri = ''
        self._NamespaceUri_fmt = '<s'
        self._NamespaceUri_fmt_size = 1
        self.UnitId = 0
        self._UnitId_fmt = '<i'
        self._UnitId_fmt_size = 4
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack('<i', len(self.NamespaceUri)))
        tmp.append(struct.pack('<{}s'.format(len(self.NamespaceUri)), self.NamespaceUri.encode()))
        tmp.append(struct.pack(self._UnitId_fmt, self.UnitId))
        tmp.append(self.DisplayName.to_binary())
        tmp.append(self.Description.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            slength = struct.unpack('<i', data.red(1))
            self.NamespaceUri = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.NamespaceUri = struct.unpack(self._NamespaceUri_fmt, data.read(self._NamespaceUri_fmt_size))[0]
            self.UnitId = struct.unpack(self._UnitId_fmt, data.read(self._UnitId_fmt_size))[0]
            self.DisplayName = LocalizedText.from_binary(data)
            self.Description = LocalizedText.from_binary(data)
            return data
            
class ComplexNumberType(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.Real = 0
        self._Real_fmt = '<f'
        self._Real_fmt_size = 4
        self.Imaginary = 0
        self._Imaginary_fmt = '<f'
        self._Imaginary_fmt_size = 4
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack(self._Real_fmt, self.Real))
        tmp.append(struct.pack(self._Imaginary_fmt, self.Imaginary))
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.Real = struct.unpack(self._Real_fmt, data.read(self._Real_fmt_size))[0]
            self.Imaginary = struct.unpack(self._Imaginary_fmt, data.read(self._Imaginary_fmt_size))[0]
            return data
            
class DoubleComplexNumberType(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.Real = 0
        self._Real_fmt = '<d'
        self._Real_fmt_size = 8
        self.Imaginary = 0
        self._Imaginary_fmt = '<d'
        self._Imaginary_fmt_size = 8
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack(self._Real_fmt, self.Real))
        tmp.append(struct.pack(self._Imaginary_fmt, self.Imaginary))
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.Real = struct.unpack(self._Real_fmt, data.read(self._Real_fmt_size))[0]
            self.Imaginary = struct.unpack(self._Imaginary_fmt, data.read(self._Imaginary_fmt_size))[0]
            return data
            
class AxisInformation(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.EngineeringUnits = EUInformation()
        self.EURange = Range()
        self.Title = LocalizedText()
        self.AxisScaleType = AxisScaleEnumeration()
        self.AxisSteps = []
        self._AxisSteps_fmt = '<d'
        self._AxisSteps_fmt_size = 8
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.EngineeringUnits.to_binary())
        tmp.append(self.EURange.to_binary())
        tmp.append(self.Title.to_binary())
        tmp.append(self.AxisScaleType.to_binary())
        tmp.append(struct.pack('<i', len(self.AxisSteps)))
        for i in AxisSteps:
            tmp.append(struct.pack(self._AxisSteps_fmt, self.AxisSteps))
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.EngineeringUnits = EUInformation.from_binary(data)
            self.EURange = Range.from_binary(data)
            self.Title = LocalizedText.from_binary(data)
            self.AxisScaleType = AxisScaleEnumeration.from_binary(data)
            length = struct.unpack('<i', data.read(4))[0]
            if length <= -1:
                for i in range(0, length):
                    self.AxisSteps = struct.unpack(self._AxisSteps_fmt, data.read(self._AxisSteps_fmt_size))[0]
            return data
            
class XVType(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.X = 0
        self._X_fmt = '<d'
        self._X_fmt_size = 8
        self.Value = 0
        self._Value_fmt = '<f'
        self._Value_fmt_size = 4
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack(self._X_fmt, self.X))
        tmp.append(struct.pack(self._Value_fmt, self.Value))
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.X = struct.unpack(self._X_fmt, data.read(self._X_fmt_size))[0]
            self.Value = struct.unpack(self._Value_fmt, data.read(self._Value_fmt_size))[0]
            return data
            
class ProgramDiagnosticDataType(object):
    def __init__(self):
        self.TypeId = ExpandedNodeId()
        self.CreateSessionId = NodeId()
        self.CreateClientName = ''
        self._CreateClientName_fmt = '<s'
        self._CreateClientName_fmt_size = 1
        self.InvocationCreationTime = 0
        self.LastTransitionTime = 0
        self.LastMethodCall = ''
        self._LastMethodCall_fmt = '<s'
        self._LastMethodCall_fmt_size = 1
        self.LastMethodSessionId = NodeId()
        self.LastMethodInputArguments = []
        self.LastMethodOutputArguments = []
        self.LastMethodCallTime = 0
        self.LastMethodReturnStatus = StatusResult()
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(self.CreateSessionId.to_binary())
        tmp.append(struct.pack('<i', len(self.CreateClientName)))
        tmp.append(struct.pack('<{}s'.format(len(self.CreateClientName)), self.CreateClientName.encode()))
        tmp.append(self.InvocationCreationTime.to_binary())
        tmp.append(self.LastTransitionTime.to_binary())
        tmp.append(struct.pack('<i', len(self.LastMethodCall)))
        tmp.append(struct.pack('<{}s'.format(len(self.LastMethodCall)), self.LastMethodCall.encode()))
        tmp.append(self.LastMethodSessionId.to_binary())
        tmp.append(struct.pack('<i', len(self.LastMethodInputArguments)))
        for i in LastMethodInputArguments:
            tmp.append(self.LastMethodInputArguments.to_binary())
        tmp.append(struct.pack('<i', len(self.LastMethodOutputArguments)))
        for i in LastMethodOutputArguments:
            tmp.append(self.LastMethodOutputArguments.to_binary())
        tmp.append(self.LastMethodCallTime.to_binary())
        tmp.append(self.LastMethodReturnStatus.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            self.CreateSessionId = NodeId.from_binary(data)
            slength = struct.unpack('<i', data.red(1))
            self.CreateClientName = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.CreateClientName = struct.unpack(self._CreateClientName_fmt, data.read(self._CreateClientName_fmt_size))[0]
            self.InvocationCreationTime = DateTime.from_binary(data)
            self.LastTransitionTime = DateTime.from_binary(data)
            slength = struct.unpack('<i', data.red(1))
            self.LastMethodCall = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.LastMethodCall = struct.unpack(self._LastMethodCall_fmt, data.read(self._LastMethodCall_fmt_size))[0]
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
        self.TypeId = ExpandedNodeId()
        self.Message = ''
        self._Message_fmt = '<s'
        self._Message_fmt_size = 1
        self.UserName = ''
        self._UserName_fmt = '<s'
        self._UserName_fmt_size = 1
        self.AnnotationTime = 0
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack('<i', len(self.Message)))
        tmp.append(struct.pack('<{}s'.format(len(self.Message)), self.Message.encode()))
        tmp.append(struct.pack('<i', len(self.UserName)))
        tmp.append(struct.pack('<{}s'.format(len(self.UserName)), self.UserName.encode()))
        tmp.append(self.AnnotationTime.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
        @staticmethod
        def from_binary(self, data):
            self.TypeId = ExpandedNodeId.from_binary(data)
            slength = struct.unpack('<i', data.red(1))
            self.Message = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.Message = struct.unpack(self._Message_fmt, data.read(self._Message_fmt_size))[0]
            slength = struct.unpack('<i', data.red(1))
            self.UserName = struct.unpack('<{}s'.format(slength), data.read(slength))
            self.UserName = struct.unpack(self._UserName_fmt, data.read(self._UserName_fmt_size))[0]
            self.AnnotationTime = DateTime.from_binary(data)
            return data
