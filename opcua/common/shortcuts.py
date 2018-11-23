from opcua.ua import ObjectIds
from opcua import Node


class Shortcuts(object):
    """
    This object contains Node objects to some commonly used nodes
    """
    def __init__(self, isession):
        self.root = Node(isession, ObjectIds.RootFolder)
        self.objects = Node(isession, ObjectIds.ObjectsFolder)
        self.isession = Node(isession, ObjectIds.Server)
        self.types = Node(isession, ObjectIds.TypesFolder)
        self.base_object_type = Node(isession, ObjectIds.BaseObjectType)
        self.base_data_type = Node(isession, ObjectIds.BaseDataType)
        self.base_event_type = Node(isession, ObjectIds.BaseEventType)
        self.base_variable_type = Node(isession, ObjectIds.BaseVariableType)
        self.folder_type = Node(isession, ObjectIds.FolderType)
        self.enum_data_type = Node(isession, ObjectIds.Enumeration)
        self.types = Node(isession, ObjectIds.TypesFolder)
        self.data_types = Node(isession, ObjectIds.DataTypesFolder)
        self.event_types = Node(isession, ObjectIds.EventTypesFolder)
        self.reference_types = Node(isession, ObjectIds.ReferenceTypesFolder)
        self.variable_types = Node(isession, ObjectIds.VariableTypesFolder)
        self.object_types = Node(isession, ObjectIds.ObjectTypesFolder)
        self.namespace_array = Node(isession, ObjectIds.Server_NamespaceArray)
        self.opc_binary = Node(isession, ObjectIds.OPCBinarySchema_TypeSystem)
        self.base_structure_type = Node(isession, ObjectIds.Structure)
