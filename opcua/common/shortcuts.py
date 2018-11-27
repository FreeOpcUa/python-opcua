from opcua.ua import ObjectIds
from opcua import Node


class Shortcuts(object):
    """
    This object contains Node objects to some commonly used nodes
    """
    def __init__(self, session_server):
        self.root = Node(session_server, ObjectIds.RootFolder)
        self.objects = Node(session_server, ObjectIds.ObjectsFolder)
        self.session_server = Node(session_server, ObjectIds.Server)
        self.types = Node(session_server, ObjectIds.TypesFolder)
        self.base_object_type = Node(session_server, ObjectIds.BaseObjectType)
        self.base_data_type = Node(session_server, ObjectIds.BaseDataType)
        self.base_event_type = Node(session_server, ObjectIds.BaseEventType)
        self.base_variable_type = Node(session_server, ObjectIds.BaseVariableType)
        self.folder_type = Node(session_server, ObjectIds.FolderType)
        self.enum_data_type = Node(session_server, ObjectIds.Enumeration)
        self.types = Node(session_server, ObjectIds.TypesFolder)
        self.data_types = Node(session_server, ObjectIds.DataTypesFolder)
        self.event_types = Node(session_server, ObjectIds.EventTypesFolder)
        self.reference_types = Node(session_server, ObjectIds.ReferenceTypesFolder)
        self.variable_types = Node(session_server, ObjectIds.VariableTypesFolder)
        self.object_types = Node(session_server, ObjectIds.ObjectTypesFolder)
        self.namespace_array = Node(session_server, ObjectIds.Server_NamespaceArray)
        self.opc_binary = Node(session_server, ObjectIds.OPCBinarySchema_TypeSystem)
        self.base_structure_type = Node(session_server, ObjectIds.Structure)
