from opcua.ua import ObjectIds, ObjectIdNames
from opcua.ua.uaprotocol_auto import ExtensionClasses


def register_extension_object(object_factory):
    setattr(ObjectIds, "{}_Encoding_DefaultBinary".format(object_factory.__name__), object_factory.DEFAULT_BINARY)
    ObjectIdNames[object_factory.DEFAULT_BINARY] = object_factory.__name__
    ExtensionClasses[object_factory.DEFAULT_BINARY] = object_factory
