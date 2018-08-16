from opcua import ua
from opcua.ua import uatypes
from enum import IntEnum

class ExampleEnum(IntEnum):
    EnumVal1 = 0
    EnumVal2 = 1
    EnumVal3 = 2

import opcua.ua
setattr(opcua.ua, 'ExampleEnum', ExampleEnum)

class ExampleStruct(uatypes.FrozenClass):

    ua_types = [
        ('IntVal1', 'Int16'),
        ('EnumVal', 'ExampleEnum'),
               ]

    def __init__(self):
        self.IntVal1 = 0
        self.EnumVal = ExampleEnum(0)
        self._freeze = True

    def __str__(self):
        return 'ExampleStruct(' + 'IntVal1:' + str(self.IntVal1) + ', ' + \
               'EnumVal:' + str(self.EnumVal) + ')'

    __repr__ = __str__

def add_server_custom_enum_struct(server):
    # import some nodes from xml
    server.import_xml("tests/enum_struct_test_nodes.xml")
    ns = server.get_namespace_index('http://yourorganisation.org/struct_enum_example/')
    uatypes.register_extension_object('ExampleStruct', ua.NodeId(5001, ns), ExampleStruct)
    val = ua.ExampleStruct()
    val.IntVal1 = 242
    val.EnumVal = ua.ExampleEnum.EnumVal2
    myvar = server.get_node(ua.NodeId(6009, ns))
    myvar.set_value(val)
