from opcua.common.methods import to_variant
from opcua.ua import ua_binary as uabin
from opcua.ua.uatypes import Variant
from opcua.ua.uautils import register_extension_object


class KeyValuePair(object):
    # The DEFAULT_BINARY is the NodeId of the custom type
    DEFAULT_BINARY = 20001

    def __init__(self, key, value, namespace_id=0):
        self.key = key
        self.value = value
        self.NamespaceIndex = namespace_id

    def __repr__(self):
        return "KeyValuePair(key={}, value={})".format(self.key, self.value)

    def to_binary(self):
        # We need to define to_binary. It will be used when serializing the object
        packet = []
        packet.append(uabin.Primitives.UInt16.pack(self.NamespaceIndex))
        packet.append(uabin.Primitives.String.pack(self.key))
        packet.append(uabin.Primitives.String.pack(self.value))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        # This is how we deserialize the object
        namespace_index = uabin.Primitives.UInt16.unpack(data)
        key = uabin.Primitives.String.unpack(data)
        value = uabin.Primitives.String.unpack(data)
        return KeyValuePair(key, value, namespace_index)


class ErrorKeyValue(object):
    DEFAULT_BINARY = 20002

    def __init__(self, code, description, extensions, namespace_id=0):
        self.code = code
        self.description = description
        self.extensions = extensions
        self.NamespaceIndex = namespace_id

    def __repr__(self):
        return "ErrorKeyValue(code='{}', description='{}', extensions={})".format(
            self.code, self.description, self.extensions)

    def to_binary(self):
        packet = []
        packet.append(uabin.Primitives.UInt16.pack(self.NamespaceIndex))
        packet.append(uabin.Primitives.String.pack(self.code))
        packet.append(uabin.Primitives.String.pack(self.description))

        # When we want to serialize a list, we need to transform the objects to a Variant and then manually call
        # to_binary() to serialize them
        for i in to_variant(self.extensions):
            packet.append(i.to_binary())

        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        namespace_index = uabin.Primitives.UInt16.unpack(data)
        code = uabin.Primitives.String.unpack(data)
        description = uabin.Primitives.String.unpack(data)

        # When descerialising, you'll get a Variant object back. This is how get the object's value back
        extensions = Variant.from_binary(data)
        extensions = [ext for ext in extensions.Value]
        return ErrorKeyValue(code, description, extensions, namespace_index)

# For each custom type defined, we need to register it so the script know how to serialize / deserialise them
register_extension_object(KeyValuePair)
register_extension_object(ErrorKeyValue)
