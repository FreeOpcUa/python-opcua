import inspect
import sys
import unittest
from datetime import datetime
from enum import EnumMeta

from opcua import ua
from opcua.common.structures import StructGenerator, Struct, EnumType
from opcua.ua.ua_binary import struct_to_binary, struct_from_binary


# An ExtensionObject that is decoded becomes a generated class of a custom name.
# The class below represents an example that includes OPC UA optional fields.
class ObjectWithOptionalFields(object):
    ua_switches = {
        'cavityId': ('BitEncoding0', 0),
        'description': ('BitEncoding0', 1),
        # This exists in xml but gets ignored because no matching switches.
        # 'Reserved1': ('ByteEncoding0', 2)
    }
    ua_types = [
        # The bits fields are not necessary because 'ua_switches' provides us with
        # the related bit we care about.
        # ('cavityIdSpecified', 'Bit'),
        # ('descriptionSpecified', 'Bit'),
        # ('Reserved1', 'Bit'),
        ('BitEncoding0', 'UInt32'),
        ('name', 'CharArray'),
        ('value', 'Double'),
        ('assignment', 'UInt32'),
        ('source', 'UInt32'),
        ('cavityId', 'UInt32'),
        ('id', 'CharArray'),
        ('description', 'CharArray'),
    ]

    def __str__(self):
        vals = [name + ": " + str(val) for name, val in self.__dict__.items()]
        return self.__class__.__name__ + "(" + ", ".join(vals) + ")"

    __repr__ = __str__

    def __init__(self):
        self.BitEncoding0 = 0x03
        self.name = 'SomeAmazingCycleParameter'
        self.value = 8
        self.assignment = 8
        self.source = 8
        self.cavityId = 5
        self.id = 'abcdefgh'
        self.description = 'BBA'


class CustomStructTestCase(unittest.TestCase):

    def setUp(self):
        self.identifier_count = 0

    def _generate_node_id(self):
        self.identifier_count += 1
        return f"ns=0;i={self.identifier_count}"

    @staticmethod
    def is_struct(obj):
        # TODO: putting this definition in the generated class would be better
        return hasattr(obj, 'ua_types')

    def assertCustomStructEqual(self, original, deserialized):
        if hasattr(original, 'ua_switches'):
            self.assertEqual(len(original.ua_switches), len(deserialized.ua_switches))
        self.assertEqual(len(original.ua_types), len(deserialized.ua_types))
        for field, _ in original.ua_types:
            field_obj = getattr(original, field)
            deserialized_obj = getattr(deserialized, field)
            if self.is_struct(field_obj):
                self.assertCustomStructEqual(field_obj, deserialized_obj)
            else:
                self.assertEqual(getattr(original, field), getattr(deserialized, field))

    def test_binary_struct_example(self):
        # Example test so that we can manually control the object that gets
        # generated and see how it gets serialized/deserialized
        original = ObjectWithOptionalFields()
        serialized = struct_to_binary(original)
        deserialized = struct_from_binary(ObjectWithOptionalFields, ua.utils.Buffer(serialized))
        self.assertEqual(len(original.ua_switches), len(deserialized.ua_switches))
        self.assertEqual(len(original.ua_types), len(deserialized.ua_types))
        for field, _ in original.ua_types:
            self.assertEqual(getattr(original, field), getattr(deserialized, field))

    def test_custom_struct_with_optional_fields(self):
        xmlpath = "custom_extension_with_optional_fields.xml"
        c = StructGenerator()
        c.make_model_from_file(xmlpath)
        for m in c.model:
            if type(m) in (Struct, EnumType):
                m.typeid = self._generate_node_id()
        c.save_to_file("custom_extension_with_optional_fields.py", register=True)
        import como_structures as s
        for name, obj in inspect.getmembers(sys.modules[s.__name__], predicate=inspect.isclass):
            if name.startswith('__') or obj in (datetime,) or isinstance(obj, EnumMeta):
                continue
            with self.subTest(name=name):
                original = obj()
                serialized = struct_to_binary(original)
                deserialized = struct_from_binary(obj, ua.utils.Buffer(serialized))
                self.assertCustomStructEqual(original, deserialized)
