from opcua.ua import ObjectIds
from opcua import Node


class Shortcuts(object):
    """
    This object contains Node objects to some commonly used nodes
    """
    def __init__(self, server):
        self.root = Node(server, ObjectIds.RootFolder)
        self.objects = Node(server, ObjectIds.ObjectsFolder)
        self.server = Node(server, ObjectIds.Server)
        self.types = Node(server, ObjectIds.TypesFolder)
        self.base_object_type = Node(server, ObjectIds.BaseObjectType)
        self.base_data_type = Node(server, ObjectIds.BaseDataType)
        self.base_event_type = Node(server, ObjectIds.BaseEventType)
        self.base_variable_type = Node(server, ObjectIds.BaseVariableType)
        self.folder_type = Node(server, ObjectIds.FolderType)
        self.enum_data_type = Node(server, ObjectIds.Enumeration)
        self.types = Node(server, 86)
        self.data_types = Node(server, 90)
        self.event_types = Node(server, 3048)
        self.reference_types = Node(server, 91)
        self.variable_types = Node(server, 89)
        self.object_types = Node(server, 88)
