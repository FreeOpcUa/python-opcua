
from opcua import ua
from opcua import uamethod
from opcua.ua import uaerrors


@uamethod
def func(parent, value, string):
    return value * 2


class XmlTests(object):
    srv = None
    opc = None  # just to remove pylint warnings
    assertEqual = dir

    def test_xml_import(self):
        self.srv.import_xml("tests/custom_nodes.xml")
        o = self.opc.get_objects_node()
        v = o.get_child(["1:MyXMLFolder", "1:MyXMLObject", "1:MyXMLVariable"])
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

    def test_xml_import_additional_ns(self):
        self.srv.register_namespace('http://placeholder.toincrease.nsindex')  # if not already shift the new namespaces

        # "tests/custom_nodes.xml" isn't created with namespaces in mind, provide new test file
        self.srv.import_xml("tests/custom_nodesns.xml")  # the ns=1 in to file now should be mapped to ns=2

        ns = self.srv.get_namespace_index("http://examples.freeopcua.github.io/")
        o = self.opc.get_objects_node()

        o2 = o.get_child(["%d:MyBaseObject" % ns])

        self.assertIsNotNone(o2)

        v1 = o.get_child(["%d:MyBaseObject" % ns, "%d:MyVar" % ns])
        self.assertIsNotNone(v1)

        r1 = o2.get_references(refs=ua.ObjectIds.HasComponent)[0]
        self.assertEqual(r1.NodeId.NamespaceIndex, ns)

        r3 = v1.get_references(refs=ua.ObjectIds.HasComponent)[0]
        self.assertEqual(r3.NodeId.NamespaceIndex, ns)

    def test_xml_method(self):
        self.opc.register_namespace("tititi")
        self.opc.register_namespace("whatthefuck")
        o = self.opc.nodes.objects.add_object(2, "xmlexportmethod")
        m = o.add_method(2, "callme", func, [ua.VariantType.Double, ua.VariantType.String], [ua.VariantType.Float])
        # set an arg dimension to a list to test list export
        inputs = m.get_child("InputArguments")
        val = inputs.get_value()
        val[0].ArrayDimensions = [2, 2]
        desc = b"My nce description"
        val[0].Description = ua.LocalizedText(desc)
        inputs.set_value(val)

        # get all nodes and export
        nodes = [o, m]
        nodes.extend(m.get_children())
        self.opc.export_xml(nodes, "export.xml")

        self.opc.delete_nodes(nodes)
        self.opc.import_xml("export.xml")

        # now see if our nodes are here
        val = inputs.get_value()
        self.assertEqual(len(val), 2)

        self.assertEqual(val[0].ArrayDimensions, [2, 2])
        self.assertEqual(val[0].Description.Text, desc)

    def test_xml_vars(self):
        self.opc.register_namespace("tititi")
        self.opc.register_namespace("whatthefuck")
        o = self.opc.nodes.objects.add_object(2, "xmlexportobj")
        v = o.add_variable(3, "myxmlvar", 6.78, ua.VariantType.Float)
        a = o.add_variable(3, "myxmlvar-array", [6, 1], ua.VariantType.UInt16)
        a2 = o.add_variable(3, "myxmlvar-2dim", [[1, 2], [3,4]], ua.VariantType.UInt32)
        a3 = o.add_variable(3, "myxmlvar-2dim", [[]], ua.VariantType.ByteString)

        nodes = [o, v, a, a2, a3]
        self.opc.export_xml(nodes, "export-vars.xml")
        self.opc.delete_nodes(nodes)
        self.opc.import_xml("export-vars.xml")

        self.assertEqual(v.get_value(), 6.78)
        self.assertEqual(v.get_data_type(), ua.NodeId(ua.ObjectIds.Float))
        
        self.assertEqual(a.get_data_type(), ua.NodeId(ua.ObjectIds.UInt16))
        self.assertIn(a.get_value_rank(), (0, 1))
        self.assertEqual(a.get_value(), [6, 1])

        self.assertEqual(a2.get_value(), [[1, 2],[3, 4]])
        self.assertEqual(a2.get_data_type(), ua.NodeId(ua.ObjectIds.UInt32))
        self.assertIn(a2.get_value_rank(), (0, 2))
        self.assertEqual(a2.get_attribute(ua.AttributeIds.ArrayDimensions).Value.Value, [2, 2])
        #self.assertEqual(a3.get_value(), [[]])  # would require special code ...
        self.assertEqual(a3.get_data_type(), ua.NodeId(ua.ObjectIds.ByteString))
        self.assertIn(a3.get_value_rank(), (0, 2))
        self.assertEqual(a3.get_attribute(ua.AttributeIds.ArrayDimensions).Value.Value, [1, 0])

    def test_xml_ext_obj(self):
        arg = ua.Argument()
        arg.DataType = ua.NodeId(ua.ObjectIds.Float)
        arg.Description = ua.LocalizedText(b"This is a nice description")
        arg.ArrayDimensions = [1, 2, 3]
        arg.Name = "MyArg"

        v = self.opc.nodes.objects.add_variable(2, "xmlexportobj2", arg)

        nodes = [v]
        self.opc.export_xml(nodes, "export.xml")
        self.opc.delete_nodes(nodes)
        self.opc.import_xml("export.xml")

        arg2 = v.get_value()

        self.assertEqual(arg.Name, arg2.Name)
        self.assertEqual(arg.ArrayDimensions, arg2.ArrayDimensions)
        self.assertEqual(arg.Description, arg2.Description)
        self.assertEqual(arg.DataType, arg2.DataType)


    def test_xml_ns(self):
        ns_array = self.opc.get_namespace_array()
        if len(ns_array) < 3:
            self.opc.register_namespace("dummy_ns")
        print("ARRAY", self.opc.get_namespace_array())

        ref_ns = self.opc.register_namespace("ref_namespace")
        new_ns = self.opc.register_namespace("my_new_namespace")
        bname_ns = self.opc.register_namespace("bname_namespace")

        o = self.opc.nodes.objects.add_object(0, "xmlns0")
        o50 = self.opc.nodes.objects.add_object(50, "xmlns20")
        o200 = self.opc.nodes.objects.add_object(200, "xmlns200")
        onew = self.opc.nodes.objects.add_object(new_ns, "xmlns_new")
        vnew = onew.add_variable(new_ns, "xmlns_new_var", 9.99)
        o_no_export = self.opc.nodes.objects.add_object(ref_ns, "xmlns_parent")
        v_no_parent = o_no_export.add_variable(new_ns, "xmlns_new_var_no_parent", 9.99)
        o_bname = onew.add_object("ns={};i=4000".format(new_ns), "{}:BNAME".format(bname_ns))

        nodes = [o, o50, o200, onew, vnew, v_no_parent, o_bname]
        print("CREATED", nodes, o_no_export)
        self.opc.export_xml(nodes, "export-ns.xml")
        # delete node and change index og new_ns before re-importing
        self.opc.delete_nodes(nodes)
        ns_node = self.opc.get_node(ua.NodeId(ua.ObjectIds.Server_NamespaceArray))
        nss = ns_node.get_value()
        nss.remove("my_new_namespace")
        #nss.remove("ref_namespace")
        nss.remove("bname_namespace")
        ns_node.set_value(nss)
        new_ns = self.opc.register_namespace("my_new_namespace_offsett")
        new_ns = self.opc.register_namespace("my_new_namespace")

        new_nodes = self.opc.import_xml("export-ns.xml")
        print("NEW NODES", new_nodes)

        for i in [o, o50, o200]:
            print(i)
            i.get_browse_name()
        with self.assertRaises(uaerrors.BadNodeIdUnknown):
            onew.get_browse_name()
        
        # since my_new_namesspace2 is referenced byt a node it should have been reimported
        nss = self.opc.get_namespace_array()
        self.assertIn("bname_namespace", nss)
        # get index of namespaces after import
        new_ns = self.opc.register_namespace("my_new_namespace")
        bname_ns = self.opc.register_namespace("bname_namespace")
        print("ARRAY 2", self.opc.get_namespace_array())
        
        print("NEW NS", new_ns, onew)
        onew.nodeid.NamespaceIndex = new_ns
        print("OENE", onew)
        onew.get_browse_name()
        vnew2 = onew.get_children()[0]
        self.assertEqual(new_ns, vnew2.nodeid.NamespaceIndex)
