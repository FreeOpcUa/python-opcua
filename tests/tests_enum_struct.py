from opcua import ua, Server
from opcua.ua import uatypes
from enum import IntEnum
from datetime import datetime

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


class StdMsgHeader(uatypes.FrozenClass):

    ua_types = [
        ('seq', 'UInt32'),
        ('stamp', 'DateTime'),
        ('frame_id', 'String'),
               ]

    def __init__(self):
        self.seq = 0
        self.stamp = datetime.now()
        self.frame_id = ''
        self._freeze = True

    def __str__(self):
        return 'StdMsgHeader(' + 'seq:' + str(self.seq) + ', ' + \
               'stamp:' + str(self.stamp) + ', ' +  \
               'frame_id:' + str(self.frame_id) + ')'

    __repr__ = __str__


def add_server_custom_enum_struct(server):
    # import some nodes from xml
    server.import_xml("/home/peiren/ros_test.xml")
    ns = server.get_namespace_index('http://ros.org/rosopcua')
    # uatypes.register_extension_object('StdMsgHeader', ua.NodeId(5001, ns), StdMsgHeader)
    return ns
    

if __name__ == '__main__':
    server = Server()
    server.set_endpoint('opc.tcp://127.0.0.1:48510')
    ns = add_server_custom_enum_struct(server)
    server.start()
    server.load_type_definitions()
    val = ua.StdMsgHeader()
    val.seq = 242
    val.frame_id = 'testtest'
    myvar = server.nodes.objects.add_variable(ua.NodeId(6009, ns), 'testnode',
                                              ua.Variant(None, ua.VariantType.Null),
                                              ua.NodeId(3002, ns))
    myvar.set_value(val)
    for desc in server.nodes.opc_binary.get_children_descriptions():
        if desc.BrowseName != ua.QualifiedName("Opc.Ua"):
            node = server.get_node(desc.NodeId)
            break
    xml = node.get_value()
    xml = xml.decode("utf-8")
    input('give a one')
    server.stop()
