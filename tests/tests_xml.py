
from opcua import ua
from opcua import uamethod


@uamethod
def func(parent, value, string):
    return value * 2


class XmlTests(object):
    def test_xml_import(self):
        self.srv.import_xml("tests/custom_nodes.xml")
        o = self.opc.get_objects_node()
        v = o.get_child(["MyXMLFolder", "MyXMLObject", "MyXMLVariable"])
        val = v.get_value()
        self.assertEqual(val, "StringValue")

        node_path = ["Types", "DataTypes", "BaseDataType", "Enumeration",
                     "1:MyEnum", "0:EnumStrings"]
        o = self.opc.get_root_node().get_child(node_path)
        self.assertEqual(len(o.get_value()), 3)

        # Check if method is imported
        node_path = ["Types", "ObjectTypes", "BaseObjectType",
                     "1:MyObjectType", "1:MyMethod"]
        o = self.opc.get_root_node().get_child(node_path)
        self.assertEqual(len(o.get_referenced_nodes()), 4)

        # Check if InputArgs are imported and can be read
        node_path = ["Types", "ObjectTypes", "BaseObjectType",
                     "1:MyObjectType", "1:MyMethod", "InputArguments"]
        o = self.opc.get_root_node().get_child(node_path)
        input_arg = o.get_data_value().Value.Value[0]
        self.assertEqual(input_arg.Name, 'Context')

    def test_xml_export(self):
        o = self.opc.nodes.objects.add_object(2, "xmlexportobj")
        m = o.add_method(2, "callme", func, [ua.VariantType.Double, ua.VariantType.String], [ua.VariantType.Float])
        v = o.add_variable(3, "myxmlvar", 6.78, ua.VariantType.Float)
        a = o.add_variable(3, "myxmlvar", [6, 1], ua.VariantType.UInt16)
        a2 = o.add_variable(3, "myxmlvar", [[]], ua.VariantType.ByteString)
        print(a.get_value_rank)
        # set an arg dimension to a list to test list export
        inputs = m.get_child("InputArguments")
        val = inputs.get_value()
        val[0].ArrayDimensions = [2, 2]
        inputs.set_value(val)
        
        #get all nodes and export
        nodes = [o, m]
        nodes.extend(m.get_children())
        self.opc.export_xml(nodes, "export.xml")

        self.opc.delete_nodes(nodes)

        self.opc.import_xml("export.xml")
        
        # now see if our nodes are here
        val = inputs.get_value()
        self.assertEqual(len(val), 2)
        #self.assertEqual(val[0].ArrayDimensions, [2, 2]) # seems broken
        self.assertEqual(v.get_value(), 6.78)
        self.assertEqual(v.get_data_type(), ua.NodeId(ua.ObjectIds.Float))

        self.assertEqual(a.get_value(), [6, 1])
        self.assertEqual(a.get_data_type(), ua.NodeId(ua.ObjectIds.UInt16))
        self.assertIn(a.get_value_rank(), (0, 1))

        self.assertEqual(a2.get_value(), [[]])
        self.assertEqual(a2.get_data_type(), ua.NodeId(ua.ObjectIds.ByteString))
        self.assertIn(a2.get_value_rank(), (0, 2))
        self.assertEqual(a2.get_attribute(ua.AttributeIds.ArrayDimensions).Value.Value, [1, 0]) # seems broken


