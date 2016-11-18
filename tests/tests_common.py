# encoding: utf-8
from datetime import datetime
from datetime import timedelta
import math

from opcua import ua
from opcua import uamethod
from opcua import instantiate
from opcua import copy_node
from opcua.ua.uautils import register_extension_object

from opcua.ua import ua_binary as uabin
from opcua.common import ua_utils


def add_server_methods(srv):
    @uamethod
    def func(parent, value):
        return value * 2

    o = srv.get_objects_node()
    v = o.add_method(ua.NodeId("ServerMethod", 2), ua.QualifiedName('ServerMethod', 2), func, [ua.VariantType.Int64], [ua.VariantType.Int64])

    @uamethod
    def func2(parent, methodname, value):
        return math.sin(value)

    o = srv.get_objects_node()
    v = o.add_method(ua.NodeId("ServerMethodArray", 2), ua.QualifiedName('ServerMethodArray', 2), func2, [ua.VariantType.String, ua.VariantType.Int64], [ua.VariantType.Int64])

    @uamethod
    def func3(parent, mylist):
        return [i * 2 for i in mylist]

    o = srv.get_objects_node()
    v = o.add_method(ua.NodeId("ServerMethodArray2", 2), ua.QualifiedName('ServerMethodArray2', 2), func3, [ua.VariantType.Int64], [ua.VariantType.Int64])


class CommonTests(object):

    '''
    Tests that will be run twice. Once on server side and once on
    client side since we have been carefull to have the exact
    same api on server and client side
    '''
    # jyst to avoid editor warnings
    opc = None
    assertEqual = lambda x, y: True
    assertIn = lambda x, y: True

    def test_find_servers(self):
        servers = self.opc.find_servers()
        # FIXME : finish

    def test_add_node_bad_args(self):
        obj = self.opc.get_objects_node()

        with self.assertRaises(TypeError):
            fold = obj.add_folder(1.2, "kk")

        with self.assertRaises(TypeError):
            fold = obj.add_folder(ua.UaError, "khjh")

        with self.assertRaises(ua.UaError):
            fold = obj.add_folder("kjk", 1.2)

        with self.assertRaises(TypeError):
            fold = obj.add_folder("i=0;s='oooo'", 1.2)

        with self.assertRaises(ua.UaError):
            fold = obj.add_folder("i=0;s='oooo'", "tt:oioi")

    def test_delete_nodes(self):
        obj = self.opc.get_objects_node()
        fold = obj.add_folder(2, "FolderToDelete")
        var = fold.add_variable(2, "VarToDelete", 9.1)
        childs = fold.get_children()
        self.assertIn(var, childs)
        self.opc.delete_nodes([var])
        with self.assertRaises(ua.UaStatusCodeError):
            var.set_value(7.8)
        with self.assertRaises(ua.UaStatusCodeError):
            obj.get_child(["2:FolderToDelete", "2:VarToDelete"])
        childs = fold.get_children()
        self.assertNotIn(var, childs)

    def test_delete_nodes_recursive(self):
        obj = self.opc.get_objects_node()
        fold = obj.add_folder(2, "FolderToDeleteR")
        var = fold.add_variable(2, "VarToDeleteR", 9.1)
        self.opc.delete_nodes([fold, var])
        with self.assertRaises(ua.UaStatusCodeError):
            var.set_value(7.8)
        with self.assertRaises(ua.UaStatusCodeError):
            obj.get_child(["2:FolderToDelete", "2:VarToDelete"])

    def test_delete_nodes_recursive2(self):
        obj = self.opc.get_objects_node()
        fold = obj.add_folder(2, "FolderToDeleteRoot")
        nfold = fold
        mynodes = []
        for i in range(7):
            nfold = fold.add_folder(2, "FolderToDeleteRoot")
            var = fold.add_variable(2, "VarToDeleteR", 9.1)
            var = fold.add_property(2, "ProToDeleteR", 9.1)
            prop = fold.add_property(2, "ProToDeleteR", 9.1)
            o = fold.add_object(3, "ObjToDeleteR")
            mynodes.append(nfold)
            mynodes.append(var)
            mynodes.append(prop)
            mynodes.append(o)
        self.opc.delete_nodes([fold], recursive=True)
        for node in mynodes:
            with self.assertRaises(ua.UaStatusCodeError):
                node.get_browse_name()

    def test_server_node(self):
        node = self.opc.get_server_node()
        self.assertEqual(ua.QualifiedName('Server', 0), node.get_browse_name())

    def test_root(self):
        root = self.opc.get_root_node()
        self.assertEqual(ua.QualifiedName('Root', 0), root.get_browse_name())
        self.assertEqual(ua.LocalizedText('Root'), root.get_display_name())
        nid = ua.NodeId(84, 0)
        self.assertEqual(nid, root.nodeid)

    def test_objects(self):
        objects = self.opc.get_objects_node()
        self.assertEqual(ua.QualifiedName('Objects', 0), objects.get_browse_name())
        nid = ua.NodeId(85, 0)
        self.assertEqual(nid, objects.nodeid)

    def test_browse(self):
        objects = self.opc.get_objects_node()
        obj = objects.add_object(4, "browsetest")
        folder = obj.add_folder(4, "folder")
        prop = obj.add_property(4, "property", 1)
        prop2 = obj.add_property(4, "property2", 2)
        var = obj.add_variable(4, "variable", 3)
        obj2 = obj.add_object(4, "obj")
        alle = obj.get_children()
        self.assertTrue(prop in alle)
        self.assertTrue(prop2 in alle)
        self.assertTrue(var in alle)
        self.assertTrue(folder in alle)
        self.assertFalse(obj in alle)
        props = obj.get_children(refs=ua.ObjectIds.HasProperty)
        self.assertTrue(prop in props)
        self.assertTrue(prop2 in props)
        self.assertFalse(var in props)
        self.assertFalse(folder in props)
        self.assertFalse(obj2 in props)
        all_vars = obj.get_children(nodeclassmask=ua.NodeClass.Variable)
        self.assertTrue(prop in all_vars)
        self.assertTrue(var in all_vars)
        self.assertFalse(folder in props)
        self.assertFalse(obj2 in props)
        all_objs = obj.get_children(nodeclassmask=ua.NodeClass.Object)
        self.assertTrue(folder in all_objs)
        self.assertTrue(obj2 in all_objs)
        self.assertFalse(var in all_objs)

    def test_browse_references(self):
        objects = self.opc.get_objects_node()
        folder = objects.add_folder(4, "folder")

        childs = objects.get_referenced_nodes(refs=ua.ObjectIds.Organizes, direction=ua.BrowseDirection.Forward, includesubtypes=False)
        self.assertTrue(folder in childs)

        childs = objects.get_referenced_nodes(refs=ua.ObjectIds.Organizes, direction=ua.BrowseDirection.Both, includesubtypes=False)
        self.assertTrue(folder in childs)

        childs = objects.get_referenced_nodes(refs=ua.ObjectIds.Organizes, direction=ua.BrowseDirection.Inverse, includesubtypes=False)
        self.assertFalse(folder in childs)

        parents = folder.get_referenced_nodes(refs=ua.ObjectIds.Organizes, direction=ua.BrowseDirection.Inverse, includesubtypes=False)
        self.assertTrue(objects in parents)

        parents = folder.get_referenced_nodes(refs=ua.ObjectIds.HierarchicalReferences, direction=ua.BrowseDirection.Inverse, includesubtypes=False)
        self.assertTrue(objects in parents)

        parent = folder.get_parent()
        self.assertEqual(parent, objects)

    def test_browsename_with_spaces(self):
        o = self.opc.get_objects_node()
        v = o.add_variable(3, 'BNVariable with spaces and %&+?/', 1.3)
        v2 = o.get_child("3:BNVariable with spaces and %&+?/")
        self.assertEqual(v, v2)

    def test_non_existing_path(self):
        root = self.opc.get_root_node()
        with self.assertRaises(ua.UaStatusCodeError):
            server_time_node = root.get_child(['0:Objects', '0:Server', '0:nonexistingnode'])

    def test_bad_attribute(self):
        root = self.opc.get_root_node()
        with self.assertRaises(ua.UaStatusCodeError):
            root.set_value(99)

    def test_get_node_by_nodeid(self):
        root = self.opc.get_root_node()
        server_time_node = root.get_child(['0:Objects', '0:Server', '0:ServerStatus', '0:CurrentTime'])
        correct = self.opc.get_node(ua.NodeId(ua.ObjectIds.Server_ServerStatus_CurrentTime))
        self.assertEqual(server_time_node, correct)

    def test_datetime_read(self):
        time_node = self.opc.get_node(ua.NodeId(ua.ObjectIds.Server_ServerStatus_CurrentTime))
        dt = time_node.get_value()
        utcnow = datetime.utcnow()
        delta = utcnow - dt
        self.assertTrue(delta < timedelta(seconds=1))

    def test_datetime_write(self):
        time_node = self.opc.get_node(ua.NodeId(ua.ObjectIds.Server_ServerStatus_CurrentTime))
        now = datetime.utcnow()
        objects = self.opc.get_objects_node()
        v1 = objects.add_variable(4, "test_datetime", now)
        tid = v1.get_value()
        self.assertEqual(now, tid)

    def test_variant_array_dim(self):
        objects = self.opc.get_objects_node()
        l = [[[1.0, 1.0, 1.0, 1.0], [2.0, 2.0, 2.0, 2.0], [3.0, 3.0, 3.0, 3.0]],[[5.0, 5.0, 5.0, 5.0], [7.0, 8.0, 9.0, 01.0], [1.0, 1.0, 1.0, 1.0]]]
        v = objects.add_variable(3, 'variableWithDims', l)

        v.set_array_dimensions([0, 0, 0])
        dim = v.get_array_dimensions()
        self.assertEqual(dim, [0, 0, 0])

        v.set_value_rank(0)
        rank = v.get_value_rank()
        self.assertEqual(rank, 0)

        v2 = v.get_value()
        self.assertEqual(v2, l)
        dv = v.get_data_value()
        self.assertEqual(dv.Value.Dimensions, [2,3,4])

        l = [[[], [], []], [[], [], []]]
        variant = ua.Variant(l, ua.VariantType.UInt32)
        v = objects.add_variable(3, 'variableWithDimsEmpty', variant)
        v2 = v.get_value()
        self.assertEqual(v2, l)
        dv = v.get_data_value()
        self.assertEqual(dv.Value.Dimensions, [2,3,0])

    def test_add_numeric_variable(self):
        objects = self.opc.get_objects_node()
        v = objects.add_variable('ns=3;i=888;', '3:numericnodefromstring', 99)
        nid = ua.NodeId(888, 3)
        qn = ua.QualifiedName('numericnodefromstring', 3)
        self.assertEqual(nid, v.nodeid)
        self.assertEqual(qn, v.get_browse_name())

    def test_add_string_variable(self):
        objects = self.opc.get_objects_node()
        v = objects.add_variable('ns=3;s=stringid;', '3:stringnodefromstring', [68])
        nid = ua.NodeId('stringid', 3)
        qn = ua.QualifiedName('stringnodefromstring', 3)
        self.assertEqual(nid, v.nodeid)
        self.assertEqual(qn, v.get_browse_name())

    def test_utf8(self):
        objects = self.opc.get_objects_node()
        utf_string = "æøå@%&"
        bn = ua.QualifiedName(utf_string, 3)
        nid = ua.NodeId("æølå", 3)
        val = "æøå"
        v = objects.add_variable(nid, bn, val)
        self.assertEqual(nid, v.nodeid)
        val2 = v.get_value()
        self.assertEqual(val, val2)
        bn2 = v.get_browse_name()
        self.assertEqual(bn, bn2)

    def test_null_variable(self):
        objects = self.opc.get_objects_node()
        var = objects.add_variable(3, 'nullstring', "a string")
        var.set_value(None)
        val = var.get_value()
        self.assertEqual(val, None)
        var.set_value("")
        val = var.get_value()
        self.assertNotEqual(val, None)
        self.assertEqual(val, "")

    def test_variable_data_type(self):
        objects = self.opc.get_objects_node()
        var = objects.add_variable(3, 'stringfordatatype', "a string")
        val = var.get_data_type_as_variant_type()
        self.assertEqual(val, ua.VariantType.String)
        var = objects.add_variable(3, 'stringarrayfordatatype', ["a", "b"])
        val = var.get_data_type_as_variant_type()
        self.assertEqual(val, ua.VariantType.String)

    def test_add_string_array_variable(self):
        objects = self.opc.get_objects_node()
        v = objects.add_variable('ns=3;s=stringarrayid;', '9:stringarray', ['l', 'b'])
        nid = ua.NodeId('stringarrayid', 3)
        qn = ua.QualifiedName('stringarray', 9)
        self.assertEqual(nid, v.nodeid)
        self.assertEqual(qn, v.get_browse_name())
        val = v.get_value()
        self.assertEqual(['l', 'b'], val)

    def test_add_numeric_node(self):
        objects = self.opc.get_objects_node()
        nid = ua.NodeId(9999, 3)
        qn = ua.QualifiedName('AddNodeVar1', 3)
        v1 = objects.add_variable(nid, qn, 0)
        self.assertEqual(nid, v1.nodeid)
        self.assertEqual(qn, v1.get_browse_name())

    def test_add_string_node(self):
        objects = self.opc.get_objects_node()
        qn = ua.QualifiedName('AddNodeVar2', 3)
        nid = ua.NodeId('AddNodeVar2Id', 3)
        v2 = objects.add_variable(nid, qn, 0)
        self.assertEqual(nid, v2.nodeid)
        self.assertEqual(qn, v2.get_browse_name())

    def test_add_find_node_(self):
        objects = self.opc.get_objects_node()
        o = objects.add_object('ns=2;i=101;', '2:AddFindObject')
        o2 = objects.get_child('2:AddFindObject')
        self.assertEqual(o, o2)

    def test_node_path(self):
        objects = self.opc.get_objects_node()
        o = objects.add_object('ns=2;i=105;', '2:NodePathObject')
        root = self.opc.get_root_node()
        o2 = root.get_child(['0:Objects', '2:NodePathObject'])
        self.assertEqual(o, o2)

    def test_add_read_node(self):
        objects = self.opc.get_objects_node()
        o = objects.add_object('ns=2;i=102;', '2:AddReadObject')
        nid = ua.NodeId(102, 2)
        self.assertEqual(o.nodeid, nid)
        qn = ua.QualifiedName('AddReadObject', 2)
        self.assertEqual(o.get_browse_name(), qn)

    def test_simple_value(self):
        o = self.opc.get_objects_node()
        v = o.add_variable(3, 'VariableTestValue', 4.32)
        val = v.get_value()
        self.assertEqual(4.32, val)

    def test_add_exception(self):
        objects = self.opc.get_objects_node()
        o = objects.add_object('ns=2;i=103;', '2:AddReadObject')
        with self.assertRaises(ua.UaStatusCodeError):
            o2 = objects.add_object('ns=2;i=103;', '2:AddReadObject')

    def test_negative_value(self):
        o = self.opc.get_objects_node()
        v = o.add_variable(3, 'VariableNegativeValue', 4)
        v.set_value(-4.54)
        val = v.get_value()
        self.assertEqual(-4.54, val)

    def test_read_server_state(self):
        statenode = self.opc.get_node(ua.NodeId(ua.ObjectIds.Server_ServerStatus_State))
        state = statenode.get_value()
        self.assertEqual(state, 0)

    def test_bad_node(self):
        bad = self.opc.get_node(ua.NodeId(999, 999))
        with self.assertRaises(ua.UaStatusCodeError):
            bad.get_browse_name()
        with self.assertRaises(ua.UaStatusCodeError):
            bad.set_value(89)
        with self.assertRaises(ua.UaStatusCodeError):
            bad.add_object(0, "0:myobj")
        with self.assertRaises(ua.UaStatusCodeError):
            bad.get_child("0:myobj")

    def test_value(self):
        o = self.opc.get_objects_node()
        var = ua.Variant(1.98, ua.VariantType.Double)
        v = o.add_variable(3, 'VariableValue', var)
        val = v.get_value()
        self.assertEqual(1.98, val)

        dvar = ua.DataValue(var)
        dv = v.get_data_value()
        self.assertEqual(ua.DataValue, type(dv))
        self.assertEqual(dvar.Value, dv.Value)
        self.assertEqual(dvar.Value, var)

    def test_set_value(self):
        o = self.opc.get_objects_node()
        var = ua.Variant(1.98, ua.VariantType.Double)
        dvar = ua.DataValue(var)
        v = o.add_variable(3, 'VariableValue', var)
        v.set_value(var.Value)
        v1 = v.get_value()
        self.assertEqual(v1, var.Value)
        v.set_value(var)
        v2 = v.get_value()
        self.assertEqual(v2, var.Value)
        v.set_data_value(dvar)
        v3 = v.get_data_value()
        self.assertEqual(v3.Value, dvar.Value)

    def test_array_value(self):
        o = self.opc.get_objects_node()
        v = o.add_variable(3, 'VariableArrayValue', [1, 2, 3])
        val = v.get_value()
        self.assertEqual([1, 2, 3], val)

    def test_bool_variable(self):
        o = self.opc.get_objects_node()
        v = o.add_variable(3, 'BoolVariable', True)
        dt = v.get_data_type_as_variant_type()
        self.assertEqual(dt, ua.VariantType.Boolean)
        val = v.get_value()
        self.assertEqual(True, val)
        v.set_value(False)
        val = v.get_value()
        self.assertEqual(False, val)

    def test_array_size_one_value(self):
        o = self.opc.get_objects_node()
        v = o.add_variable(3, 'VariableArrayValue', [1, 2, 3])
        v.set_value([1])
        val = v.get_value()
        self.assertEqual([1], val)

    def test_use_namespace(self):
        idx = self.opc.get_namespace_index("urn:freeopcua:python:server")
        self.assertEqual(idx, 1)
        root = self.opc.get_root_node()
        myvar = root.add_variable(idx, 'var_in_custom_namespace', [5])
        myid = myvar.nodeid
        self.assertEqual(idx, myid.NamespaceIndex)

    def test_method(self):
        o = self.opc.get_objects_node()
        m = o.get_child("2:ServerMethod")
        result = o.call_method("2:ServerMethod", 2.1)
        self.assertEqual(result, 4.2)
        with self.assertRaises(ua.UaStatusCodeError):
            # FIXME: we should raise a more precise exception
            result = o.call_method("2:ServerMethod", 2.1, 89, 9)
        with self.assertRaises(ua.UaStatusCodeError):
            result = o.call_method(ua.NodeId(999), 2.1)  # non existing method

    def test_method_array(self):
        o = self.opc.get_objects_node()
        m = o.get_child("2:ServerMethodArray")
        result = o.call_method(m, "sin", ua.Variant(math.pi))
        self.assertTrue(result < 0.01)

    def test_method_array2(self):
        o = self.opc.get_objects_node()
        m = o.get_child("2:ServerMethodArray2")
        result = o.call_method(m, [1.1, 3.4, 9])
        self.assertEqual(result, [2.2, 6.8, 18])

    def test_add_nodes(self):
        objects = self.opc.get_objects_node()
        f = objects.add_folder(3, 'MyFolder')
        child = objects.get_child("3:MyFolder")
        self.assertEqual(child, f)
        o = f.add_object(3, 'MyObject')
        child = f.get_child("3:MyObject")
        self.assertEqual(child, o)
        v = f.add_variable(3, 'MyVariable', 6)
        child = f.get_child("3:MyVariable")
        self.assertEqual(child, v)
        p = f.add_property(3, 'MyProperty', 10)
        child = f.get_child("3:MyProperty")
        self.assertEqual(child, p)
        childs = f.get_children()
        self.assertTrue(o in childs)
        self.assertTrue(v in childs)
        self.assertTrue(p in childs)

    def test_incl_subtypes(self):
        base_type = self.opc.get_root_node().get_child(["0:Types", "0:ObjectTypes", "0:BaseObjectType"])
        descs = base_type.get_children_descriptions(includesubtypes=True)
        self.assertTrue(len(descs) > 10)
        descs = base_type.get_children_descriptions(includesubtypes=False)
        self.assertEqual(len(descs), 0)

    def test_add_node_with_type(self):
        objects = self.opc.get_objects_node()
        f = objects.add_folder(3, 'MyFolder_TypeTest')

        o = f.add_object(3, 'MyObject1', ua.ObjectIds.BaseObjectType)
        self.assertEqual(o.get_type_definition().Identifier, ua.ObjectIds.BaseObjectType)

        o = f.add_object(3, 'MyObject2', ua.NodeId(ua.ObjectIds.BaseObjectType, 0))
        self.assertEqual(o.get_type_definition().Identifier, ua.ObjectIds.BaseObjectType)

        base_otype= self.opc.get_node(ua.ObjectIds.BaseObjectType)
        custom_otype = base_otype.add_object_type(2, 'MyFooObjectType')

        o = f.add_object(3, 'MyObject3', custom_otype.nodeid)
        self.assertEqual(o.get_type_definition().Identifier, custom_otype.nodeid.Identifier)

        references = o.get_references(refs=ua.ObjectIds.HasTypeDefinition, direction=ua.BrowseDirection.Forward)
        self.assertEqual(len(references), 1)
        self.assertEqual(references[0].NodeId, custom_otype.nodeid)

    def test_references_for_added_nodes(self):
        objects = self.opc.get_objects_node()
        o = objects.add_object(3, 'MyObject')
        nodes = objects.get_referenced_nodes(refs=ua.ObjectIds.Organizes, direction=ua.BrowseDirection.Forward, includesubtypes=False)
        self.assertTrue(o in nodes)
        nodes = o.get_referenced_nodes(refs=ua.ObjectIds.Organizes, direction=ua.BrowseDirection.Inverse, includesubtypes=False)
        self.assertTrue(objects in nodes)
        self.assertEqual(o.get_parent(), objects)
        self.assertEqual(o.get_type_definition().Identifier, ua.ObjectIds.BaseObjectType)

        o2 = o.add_object(3, 'MySecondObject')
        nodes = o.get_referenced_nodes(refs=ua.ObjectIds.HasComponent, direction=ua.BrowseDirection.Forward, includesubtypes=False)
        self.assertTrue(o2 in nodes)
        nodes = o2.get_referenced_nodes(refs=ua.ObjectIds.HasComponent, direction=ua.BrowseDirection.Inverse, includesubtypes=False)
        self.assertTrue(o in nodes)
        self.assertEqual(o2.get_parent(), o)
        self.assertEqual(o2.get_type_definition().Identifier, ua.ObjectIds.BaseObjectType)

        v = o.add_variable(3, 'MyVariable', 6)
        nodes = o.get_referenced_nodes(refs=ua.ObjectIds.HasComponent, direction=ua.BrowseDirection.Forward, includesubtypes=False)
        self.assertTrue(v in nodes)
        nodes = v.get_referenced_nodes(refs=ua.ObjectIds.HasComponent, direction=ua.BrowseDirection.Inverse, includesubtypes=False)
        self.assertTrue(o in nodes)
        self.assertEqual(v.get_parent(), o)
        self.assertEqual(v.get_type_definition().Identifier, ua.ObjectIds.BaseDataVariableType)

        p = o.add_property(3, 'MyProperty', 2)
        nodes = o.get_referenced_nodes(refs=ua.ObjectIds.HasProperty, direction=ua.BrowseDirection.Forward, includesubtypes=False)
        self.assertTrue(p in nodes)
        nodes = p.get_referenced_nodes(refs=ua.ObjectIds.HasProperty, direction=ua.BrowseDirection.Inverse, includesubtypes=False)
        self.assertTrue(o in nodes)
        self.assertEqual(p.get_parent(), o)
        self.assertEqual(p.get_type_definition().Identifier, ua.ObjectIds.PropertyType)

    def test_path_string(self):
        o = self.opc.nodes.objects.add_folder(1, "titif").add_object(3, "opath")
        path = o.get_path_as_string()
        self.assertEqual(["0:Root", "0:Objects", "1:titif", "3:opath"], path)
        path = o.get_path_as_string(2)
        self.assertEqual(["1:titif", "3:opath"], path)
        path = self.opc.get_node("i=13387").get_path_as_string()
        # FIXME this is wrong in our server! BaseObjectType is missing an inverse reference to its parent! seems xml definition is wrong
        self.assertEqual(['0:BaseObjectType', '0:FolderType', '0:FileDirectoryType', '0:CreateDirectory'], path)

    def test_path(self):
        of = self.opc.nodes.objects.add_folder(1, "titif")
        op = of.add_object(3, "opath")
        path = op.get_path()
        self.assertEqual([self.opc.nodes.root, self.opc.nodes.objects, of, op], path)
        path = op.get_path(2)
        self.assertEqual([of, op], path)
        target = self.opc.get_node("i=13387")
        path = target.get_path()
        # FIXME this is wrong in our server! BaseObjectType is missing an inverse reference to its parent! seems xml definition is wrong
        self.assertEqual([self.opc.nodes.base_object_type, self.opc.nodes.folder_type, self.opc.get_node(ua.ObjectIds.FileDirectoryType), target], path)

    def test_get_endpoints(self):
        endpoints = self.opc.get_endpoints()
        self.assertTrue(len(endpoints) > 0)
        self.assertTrue(endpoints[0].EndpointUrl.startswith("opc.tcp://"))

    def test_copy_node(self):
        dev_t = self.opc.nodes.base_data_type.add_object_type(0, "MyDevice")
        v_t = dev_t.add_variable(0, "sensor", 1.0)
        p_t = dev_t.add_property(0, "sensor_id", "0340")
        ctrl_t = dev_t.add_object(0, "controller")
        prop_t = ctrl_t.add_property(0, "state", "Running")
        # Create device sutype
        devd_t = dev_t.add_object_type(0, "MyDeviceDervived")
        v_t = devd_t.add_variable(0, "childparam", 1.0)
        p_t = devd_t.add_property(0, "sensorx_id", "0340")
        

        nodes = copy_node(self.opc.nodes.objects, dev_t)
        mydevice = nodes[0]

        self.assertEqual(mydevice.get_node_class(), ua.NodeClass.ObjectType)
        self.assertEqual(len(mydevice.get_children()), 4)
        obj = mydevice.get_child(["0:controller"])
        prop = mydevice.get_child(["0:controller", "0:state"])
        self.assertEqual(prop.get_type_definition().Identifier, ua.ObjectIds.PropertyType)
        self.assertEqual(prop.get_value(), "Running")
        self.assertNotEqual(prop.nodeid, prop_t.nodeid)

    def test_instantiate_1(self):
        # Create device type
        dev_t = self.opc.nodes.base_object_type.add_object_type(0, "MyDevice")
        v_t = dev_t.add_variable(0, "sensor", 1.0)
        p_t = dev_t.add_property(0, "sensor_id", "0340")
        ctrl_t = dev_t.add_object(0, "controller")
        prop_t = ctrl_t.add_property(0, "state", "Running")

        # Create device sutype
        devd_t = dev_t.add_object_type(0, "MyDeviceDervived")
        v_t = devd_t.add_variable(0, "childparam", 1.0)
        p_t = devd_t.add_property(0, "sensorx_id", "0340")
        
        # instanciate device
        nodes = instantiate(self.opc.nodes.objects, dev_t, bname="2:Device0001")
        mydevice = nodes[0]

        self.assertEqual(mydevice.get_node_class(), ua.NodeClass.Object)
        self.assertEqual(mydevice.get_type_definition(), dev_t.nodeid)
        obj = mydevice.get_child(["0:controller"])
        prop = mydevice.get_child(["0:controller", "0:state"])
        self.assertEqual(prop.get_type_definition().Identifier, ua.ObjectIds.PropertyType)
        self.assertEqual(prop.get_value(), "Running")
        self.assertNotEqual(prop.nodeid, prop_t.nodeid)
        
        # instanciate device subtype
        nodes = instantiate(self.opc.nodes.objects, devd_t, bname="2:Device0002")
        mydevicederived = nodes[0] 
        prop1 = mydevicederived.get_child(["0:sensorx_id"])
        var1 = mydevicederived.get_child(["0:childparam"])
        var_parent = mydevicederived.get_child(["0:sensor"])
        prop_parent = mydevicederived.get_child(["0:sensor_id"])

    def test_instantiate_string_nodeid(self):
        # Create device type
        dev_t = self.opc.nodes.base_object_type.add_object_type(0, "MyDevice2")
        v_t = dev_t.add_variable(0, "sensor", 1.0)
        p_t = dev_t.add_property(0, "sensor_id", "0340")
        ctrl_t = dev_t.add_object(0, "controller")
        prop_t = ctrl_t.add_property(0, "state", "Running")

        # instanciate device
        nodes = instantiate(self.opc.nodes.objects, dev_t, nodeid=ua.NodeId("InstDevice", 2, ua.NodeIdType.String), bname="2:InstDevice")
        mydevice = nodes[0]

        self.assertEqual(mydevice.get_node_class(), ua.NodeClass.Object)
        self.assertEqual(mydevice.get_type_definition(), dev_t.nodeid)
        obj = mydevice.get_child(["0:controller"])
        obj_nodeid_ident = obj.nodeid.Identifier
        prop = mydevice.get_child(["0:controller", "0:state"])
        self.assertEqual(obj_nodeid_ident, "InstDevice.controller")
        self.assertEqual(prop.get_type_definition().Identifier, ua.ObjectIds.PropertyType)
        self.assertEqual(prop.get_value(), "Running")
        self.assertNotEqual(prop.nodeid, prop_t.nodeid)

    def test_variable_with_datatype(self):
        v1 = self.opc.nodes.objects.add_variable(3, 'VariableEnumType1', ua.ApplicationType.ClientAndServer, datatype=ua.NodeId(ua.ObjectIds.ApplicationType))
        tp1 = v1.get_data_type()
        self.assertEqual(ua.NodeId(ua.ObjectIds.ApplicationType), tp1)

        v2 = self.opc.nodes.objects.add_variable(3, 'VariableEnumType2', ua.ApplicationType.ClientAndServer, datatype=ua.NodeId(ua.ObjectIds.ApplicationType) )
        tp2 = v2.get_data_type()
        self.assertEqual( ua.NodeId(ua.ObjectIds.ApplicationType), tp2)

    def test_enum(self):
        # create enum type
        enums = self.opc.get_root_node().get_child(["0:Types", "0:DataTypes", "0:BaseDataType", "0:Enumeration"])
        myenum_type = enums.add_data_type(0, "MyEnum")
        es = myenum_type.add_variable(0, "EnumStrings", [ua.LocalizedText("String0"), ua.LocalizedText("String1"), ua.LocalizedText("String2")], ua.VariantType.LocalizedText) 
        #es.set_value_rank(1)
        # instantiate
        o = self.opc.get_objects_node()
        myvar = o.add_variable(2, "MyEnumVar", ua.LocalizedText("String1"), datatype=myenum_type.nodeid)
        #myvar.set_writable(True)
        # tests
        self.assertEqual(myvar.get_data_type(), myenum_type.nodeid)
        myvar.set_value(ua.LocalizedText("String2"))

    def test_supertypes(self):
        nint32 = self.opc.get_node(ua.ObjectIds.Int32)
        node = ua_utils.get_node_supertype(nint32)
        self.assertEqual(node, self.opc.get_node(ua.ObjectIds.Integer))

        nodes = ua_utils.get_node_supertypes(nint32)
        self.assertEqual(nodes[1], self.opc.get_node(ua.ObjectIds.Number))
        self.assertEqual(nodes[0], self.opc.get_node(ua.ObjectIds.Integer))

        # test custom
        dtype = nint32.add_data_type(0, "MyCustomDataType")
        node = ua_utils.get_node_supertype(dtype)
        self.assertEqual(node, nint32)

        dtype2 = dtype.add_data_type(0, "MyCustomDataType2")
        node = ua_utils.get_node_supertype(dtype2)
        self.assertEqual(node, dtype)

    def test_base_data_type(self):
        nint32 = self.opc.get_node(ua.ObjectIds.Int32)
        dtype = nint32.add_data_type(0, "MyCustomDataType")
        dtype2 = dtype.add_data_type(0, "MyCustomDataType2")
        self.assertEqual(ua_utils.get_base_data_type(dtype), nint32)
        self.assertEqual(ua_utils.get_base_data_type(dtype2), nint32)

        ext = self.opc.nodes.objects.add_variable(0, "MyExtensionObject", ua.Argument())
        d = ext.get_data_type()
        d = self.opc.get_node(d)
        self.assertEqual(ua_utils.get_base_data_type(d), self.opc.get_node(ua.ObjectIds.Structure))
        self.assertEqual(ua_utils.data_type_to_variant_type(d), ua.VariantType.ExtensionObject)

    def test_ua_method_unique(self):
        def unique_response(parent):
            return 42

        decorated_unique_response = uamethod(unique_response)
        response = decorated_unique_response(ua.NodeId("ServerMethod", 2))

        self.assertEqual(len(response), 1)
        self.assertEqual(type(response[0]), ua.Variant)

    def test_ua_method_multiple(self):
        def unique_response(parent):
            return 42, 49

        decorated_unique_response = uamethod(unique_response)
        response = decorated_unique_response(ua.NodeId("ServerMethod", 2))

        self.assertEqual(len(response), 2)
        self.assertEqual(type(response[0]), ua.Variant)

    def test_ua_method_complex(self):
        register_extension_object(KeyValuePair)

        def unique_response(parent):
            return KeyValuePair("Key", "Value")

        decorated_unique_response = uamethod(unique_response)
        response = decorated_unique_response(ua.NodeId("ServerMethod", 2))

        self.assertEqual(len(response), 1)
        self.assertEqual(type(response[0]), ua.Variant)

    def test_ua_method_complex_multiple(self):
        register_extension_object(KeyValuePair)

        def unique_response(parent):
            return [KeyValuePair("Key", "Value"),
                    KeyValuePair("Hello", "World")]

        decorated_unique_response = uamethod(unique_response)
        response = decorated_unique_response(ua.NodeId("ServerMethod", 2))

        self.assertEqual(len(response), 2)
        self.assertEqual(type(response[0]), ua.Variant)

    # TODO: Fix the test
    # def test_decode_custom_object(self):
    #     register_extension_object(KeyValuePair)
    #
    #     def unique_response(parent):
    #         return KeyValuePair("Key", "Value")
    #
    #     decorated_unique_response = uamethod(unique_response)
    #     response = decorated_unique_response(ua.NodeId("ServerMethod", 2))
    #
    #     self.assertEqual(len(response), 1)
    #     self.assertEqual(type(response[0]), ua.Variant)
    #
    #     key_value = uabin.unpack_uatype_array(response[0].VariantType, io.BytesIO(response[0].to_binary()))
    #     self.assertEqual(key_value.key, "Key")
    #     self.assertEqual(key_value.value, "Value")


class KeyValuePair(object):
    DEFAULT_BINARY = 20001

    def __init__(self, key, value, namespace_id=0):
        self.key = key
        self.value = value
        self.NamespaceIndex = namespace_id

    def to_binary(self):
        packet = []
        packet.append(uabin.Primitives.UInt16.pack(self.NamespaceIndex))
        packet.append(uabin.Primitives.String.pack(self.key))
        packet.append(uabin.Primitives.String.pack(self.value))
        return b''.join(packet)

    @staticmethod
    def from_binary(data):
        namespace_index = uabin.Primitives.UInt16.unpack(data)
        key = uabin.Primitives.String.unpack(data)
        value = uabin.Primitives.String.unpack(data)
        return KeyValuePair(key, value, namespace_index)
