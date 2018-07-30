# encoding: utf-8
from concurrent.futures import Future, TimeoutError
import pytest
from datetime import datetime
from datetime import timedelta
import math
from contextlib import contextmanager

from opcua import ua
from opcua import Node
from opcua import uamethod
from opcua import instantiate
from opcua import copy_node
from opcua.common import ua_utils
from opcua.common.methods import call_method_full


async def add_server_methods(srv):
    @uamethod
    def func(parent, value):
        return value * 2

    o = srv.get_objects_node()
    await o.add_method(
        ua.NodeId("ServerMethod", 2), ua.QualifiedName('ServerMethod', 2),
        func, [ua.VariantType.Int64], [ua.VariantType.Int64]
    )

    @uamethod
    def func2(parent, methodname, value):
        if methodname == "panic":
            return ua.StatusCode(ua.StatusCodes.BadOutOfMemory)
        if methodname != "sin":
            res = ua.CallMethodResult()
            res.StatusCode = ua.StatusCode(ua.StatusCodes.BadInvalidArgument)
            res.InputArgumentResults = [ua.StatusCode(ua.StatusCodes.BadNotSupported), ua.StatusCode()]
            return res
        return math.sin(value)

    o = srv.get_objects_node()
    await o.add_method(
        ua.NodeId("ServerMethodArray", 2), ua.QualifiedName('ServerMethodArray', 2), func2,
        [ua.VariantType.String, ua.VariantType.Int64], [ua.VariantType.Int64]
    )

    @uamethod
    def func3(parent, mylist):
        return [i * 2 for i in mylist]

    o = srv.get_objects_node()
    await o.add_method(
        ua.NodeId("ServerMethodArray2", 2), ua.QualifiedName('ServerMethodArray2', 2), func3,
        [ua.VariantType.Int64], [ua.VariantType.Int64]
    )

    @uamethod
    def func4(parent):
        return None

    base_otype = srv.get_node(ua.ObjectIds.BaseObjectType)
    custom_otype = await base_otype.add_object_type(2, 'ObjectWithMethodsType')
    await custom_otype.add_method(2, 'ServerMethodDefault', func4)
    await (await custom_otype.add_method(2, 'ServerMethodMandatory', func4)).set_modelling_rule(True)
    await (await custom_otype.add_method(2, 'ServerMethodOptional', func4)).set_modelling_rule(False)
    await (await custom_otype.add_method(2, 'ServerMethodNone', func4)).set_modelling_rule(None)
    await o.add_object(2, 'ObjectWithMethods', custom_otype)

    @uamethod
    def func5(parent):
        return 1, 2, 3

    o = srv.get_objects_node()
    await o.add_method(ua.NodeId("ServerMethodTuple", 2), ua.QualifiedName('ServerMethodTuple', 2), func5, [],
                       [ua.VariantType.Int64, ua.VariantType.Int64, ua.VariantType.Int64])



"""
Tests that will be run twice. Once on server side and once on
client side since we have been carefull to have the exact
same api on server and client side
"""


async def test_find_servers(opc):
    servers = await opc.find_servers()
    # FIXME : finish

async def test_add_node_bad_args(opc):
    obj = opc.get_objects_node()

    with pytest.raises(TypeError):
        fold = await obj.add_folder(1.2, "kk")

    with pytest.raises(TypeError):
        fold = await obj.add_folder(ua.UaError, "khjh")

    with pytest.raises(ua.UaError):
        fold = await obj.add_folder("kjk", 1.2)

    with pytest.raises(TypeError):
        fold = await obj.add_folder("i=0;s='oooo'", 1.2)

    with pytest.raises(ua.UaError):
        fold = await obj.add_folder("i=0;s='oooo'", "tt:oioi")

async def test_delete_nodes(opc):
    obj = opc.get_objects_node()
    fold = await obj.add_folder(2, "FolderToDelete")
    var = await fold.add_variable(2, "VarToDelete", 9.1)
    childs = await fold.get_children()
    assert var in childs
    await opc.delete_nodes([var])
    with pytest.raises(ua.UaStatusCodeError):
        await var.set_value(7.8)
    with pytest.raises(ua.UaStatusCodeError):
        await obj.get_child(["2:FolderToDelete", "2:VarToDelete"])
    childs = await fold.get_children()
    assert var not in  childs

async def test_delete_nodes_recursive(opc):
    obj = opc.get_objects_node()
    fold = await obj.add_folder(2, "FolderToDeleteR")
    var = await fold.add_variable(2, "VarToDeleteR", 9.1)
    await opc.delete_nodes([fold, var])
    with pytest.raises(ua.UaStatusCodeError):
        await var.set_value(7.8)
    with pytest.raises(ua.UaStatusCodeError):
        await obj.get_child(["2:FolderToDelete", "2:VarToDelete"])

async def test_delete_nodes_recursive2(opc):
    obj = opc.get_objects_node()
    fold = await obj.add_folder(2, "FolderToDeleteRoot")
    nfold = fold
    mynodes = []
    for i in range(7):
        nfold = await fold.add_folder(2, "FolderToDeleteRoot")
        var = await fold.add_variable(2, "VarToDeleteR", 9.1)
        var = await fold.add_property(2, "ProToDeleteR", 9.1)
        prop = await fold.add_property(2, "ProToDeleteR", 9.1)
        o = await fold.add_object(3, "ObjToDeleteR")
        mynodes.append(nfold)
        mynodes.append(var)
        mynodes.append(prop)
        mynodes.append(o)
    await opc.delete_nodes([fold], recursive=True)
    for node in mynodes:
        with pytest.raises(ua.UaStatusCodeError):
            await node.get_browse_name()

def test_delete_references(opc):
    newtype = opc.get_node(ua.ObjectIds.HierarchicalReferences).add_reference_type(0, "HasSuperSecretVariable")

    obj = opc.get_objects_node()
    fold = obj.add_folder(2, "FolderToRef")
    var = fold.add_variable(2, "VarToRef", 42)

    fold.add_reference(var, newtype)

    assert [fold] == var.get_referenced_nodes(newtype)
    assert [var] == fold.get_referenced_nodes(newtype)

    fold.delete_reference(var, newtype)

    assert [] == var.get_referenced_nodes(newtype)
    assert [] == fold.get_referenced_nodes(newtype)

    fold.add_reference(var, newtype, bidirectional=False)

    assert [] == var.get_referenced_nodes(newtype)
    assert [var] == fold.get_referenced_nodes(newtype)

    fold.delete_reference(var, newtype)

    assert [] == var.get_referenced_nodes(newtype)
    assert [] == fold.get_referenced_nodes(newtype)

    var.add_reference(fold, newtype, forward=False, bidirectional=False)

    assert [fold] == var.get_referenced_nodes(newtype)
    assert [] == fold.get_referenced_nodes(newtype)

    with pytest.raises(ua.UaStatusCodeError):
        fold.delete_reference(var, newtype)

    assert [fold] == var.get_referenced_nodes(newtype)
    assert [] == fold.get_referenced_nodes(newtype)

    with pytest.raises(ua.UaStatusCodeError):
        var.delete_reference(fold, newtype)

    assert [fold] == var.get_referenced_nodes(newtype)
    assert [] == fold.get_referenced_nodes(newtype)

    var.delete_reference(fold, newtype, forward=False)

    assert [] == var.get_referenced_nodes(newtype)
    assert [] == fold.get_referenced_nodes(newtype)

    # clean-up
    opc.delete_nodes([fold, newtype], recursive=True)

def test_server_node(opc):
    node = opc.get_server_node()
    assert ua.QualifiedName('Server', 0) == node.get_browse_name()

def test_root(opc):
    root = opc.get_root_node()
    assert ua.QualifiedName('Root', 0) == root.get_browse_name()
    assert ua.LocalizedText('Root') == root.get_display_name()
    nid = ua.NodeId(84, 0)
    assert nid == root.nodeid

def test_objects(opc):
    objects = opc.get_objects_node()
    assert ua.QualifiedName('Objects', 0) == objects.get_browse_name()
    nid = ua.NodeId(85, 0)
    assert nid == objects.nodeid

def test_browse(opc):
    objects = opc.get_objects_node()
    obj = objects.add_object(4, "browsetest")
    folder = obj.add_folder(4, "folder")
    prop = obj.add_property(4, "property", 1)
    prop2 = obj.add_property(4, "property2", 2)
    var = obj.add_variable(4, "variable", 3)
    obj2 = obj.add_object(4, "obj")
    alle = obj.get_children()
    assert prop in alle
    assert prop2 in alle
    assert var in alle
    assert folder in alle
    assert obj not in alle
    props = obj.get_children(refs=ua.ObjectIds.HasProperty)
    assert prop in props
    assert prop2 in props
    assert var not in props
    assert folder not in props
    assert obj2 not in props
    all_vars = obj.get_children(nodeclassmask=ua.NodeClass.Variable)
    assert prop in all_vars
    assert var in all_vars
    assert folder not in props
    assert obj2 not in props
    all_objs = obj.get_children(nodeclassmask=ua.NodeClass.Object)
    assert folder in all_objs
    assert obj2 in all_objs
    assert var not in all_objs

def test_browse_references(opc):
    objects = opc.get_objects_node()
    folder = objects.add_folder(4, "folder")

    childs = objects.get_referenced_nodes(refs=ua.ObjectIds.Organizes, direction=ua.BrowseDirection.Forward,
                                          includesubtypes=False)
    assert folder in childs

    childs = objects.get_referenced_nodes(refs=ua.ObjectIds.Organizes, direction=ua.BrowseDirection.Both,
                                          includesubtypes=False)
    assert folder in childs

    childs = objects.get_referenced_nodes(refs=ua.ObjectIds.Organizes, direction=ua.BrowseDirection.Inverse,
                                          includesubtypes=False)
    assert folder not in childs

    parents = folder.get_referenced_nodes(refs=ua.ObjectIds.Organizes, direction=ua.BrowseDirection.Inverse,
                                          includesubtypes=False)
    assert objects in parents

    parents = folder.get_referenced_nodes(refs=ua.ObjectIds.HierarchicalReferences,
                                          direction=ua.BrowseDirection.Inverse, includesubtypes=False)
    assert objects in parents

    parent = folder.get_parent()
    assert parent == objects

def test_browsename_with_spaces(opc):
    o = opc.get_objects_node()
    v = o.add_variable(3, 'BNVariable with spaces and %&+?/', 1.3)
    v2 = o.get_child("3:BNVariable with spaces and %&+?/")
    assert v == v2

def test_non_existing_path(opc):
    root = opc.get_root_node()
    with pytest.raises(ua.UaStatusCodeError):
        server_time_node = root.get_child(['0:Objects', '0:Server', '0:nonexistingnode'])

def test_bad_attribute(opc):
    root = opc.get_root_node()
    with pytest.raises(ua.UaStatusCodeError):
        root.set_value(99)

def test_get_node_by_nodeid(opc):
    root = opc.get_root_node()
    server_time_node = root.get_child(['0:Objects', '0:Server', '0:ServerStatus', '0:CurrentTime'])
    correct = opc.get_node(ua.NodeId(ua.ObjectIds.Server_ServerStatus_CurrentTime))
    assert server_time_node == correct

def test_datetime_read(opc):
    time_node = opc.get_node(ua.NodeId(ua.ObjectIds.Server_ServerStatus_CurrentTime))
    dt = time_node.get_value()
    utcnow = datetime.utcnow()
    delta = utcnow - dt
    assert delta < timedelta(seconds=1)

def test_datetime_write(opc):
    time_node = opc.get_node(ua.NodeId(ua.ObjectIds.Server_ServerStatus_CurrentTime))
    now = datetime.utcnow()
    objects = opc.get_objects_node()
    v1 = objects.add_variable(4, "test_datetime", now)
    tid = v1.get_value()
    assert now == tid

def test_variant_array_dim(opc):
    objects = opc.get_objects_node()
    l = [[[1.0, 1.0, 1.0, 1.0], [2.0, 2.0, 2.0, 2.0], [3.0, 3.0, 3.0, 3.0]],
         [[5.0, 5.0, 5.0, 5.0], [7.0, 8.0, 9.0, 01.0], [1.0, 1.0, 1.0, 1.0]]]
    v = objects.add_variable(3, 'variableWithDims', l)

    v.set_array_dimensions([0, 0, 0])
    dim = v.get_array_dimensions()
    assert [0, 0, 0] == dim

    v.set_value_rank(0)
    rank = v.get_value_rank()
    assert 0 == rank

    v2 = v.get_value()
    assert l == v2
    dv = v.get_data_value()
    assert [2, 3, 4] == dv.Value.Dimensions

    l = [[[], [], []], [[], [], []]]
    variant = ua.Variant(l, ua.VariantType.UInt32)
    v = objects.add_variable(3, 'variableWithDimsEmpty', variant)
    v2 = v.get_value()
    assert l == v2
    dv = v.get_data_value()
    assert [2, 3, 0] == dv.Value.Dimensions

def test_add_numeric_variable(opc):
    objects = opc.get_objects_node()
    v = objects.add_variable('ns=3;i=888;', '3:numericnodefromstring', 99)
    nid = ua.NodeId(888, 3)
    qn = ua.QualifiedName('numericnodefromstring', 3)
    assert nid == v.nodeid
    assert qn == v.get_browse_name()

def test_add_string_variable(opc):
    objects = opc.get_objects_node()
    v = objects.add_variable('ns=3;s=stringid;', '3:stringnodefromstring', [68])
    nid = ua.NodeId('stringid', 3)
    qn = ua.QualifiedName('stringnodefromstring', 3)
    assert nid == v.nodeid
    assert qn == v.get_browse_name()

def test_utf8(opc):
    objects = opc.get_objects_node()
    utf_string = "æøå@%&"
    bn = ua.QualifiedName(utf_string, 3)
    nid = ua.NodeId("æølå", 3)
    val = "æøå"
    v = objects.add_variable(nid, bn, val)
    assert nid == v.nodeid
    val2 = v.get_value()
    assert val == val2
    bn2 = v.get_browse_name()
    assert bn == bn2

def test_null_variable(opc):
    objects = opc.get_objects_node()
    var = objects.add_variable(3, 'nullstring', "a string")
    var.set_value(None)
    val = var.get_value()
    assert val is None
    var.set_value("")
    val = var.get_value()
    assert val is not None
    assert "" == val

def test_variable_data_type(opc):
    objects = opc.get_objects_node()
    var = objects.add_variable(3, 'stringfordatatype', "a string")
    val = var.get_data_type_as_variant_type()
    assert ua.VariantType.String == val
    var = objects.add_variable(3, 'stringarrayfordatatype', ["a", "b"])
    val = var.get_data_type_as_variant_type()
    assert ua.VariantType.String == val

def test_add_string_array_variable(opc):
    objects = opc.get_objects_node()
    v = objects.add_variable('ns=3;s=stringarrayid;', '9:stringarray', ['l', 'b'])
    nid = ua.NodeId('stringarrayid', 3)
    qn = ua.QualifiedName('stringarray', 9)
    assert nid == v.nodeid
    assert qn == v.get_browse_name()
    val = v.get_value()
    assert ['l', 'b'] == val

def test_add_numeric_node(opc):
    objects = opc.get_objects_node()
    nid = ua.NodeId(9999, 3)
    qn = ua.QualifiedName('AddNodeVar1', 3)
    v1 = objects.add_variable(nid, qn, 0)
    assert nid == v1.nodeid
    assert qn == v1.get_browse_name()

def test_add_string_node(opc):
    objects = opc.get_objects_node()
    qn = ua.QualifiedName('AddNodeVar2', 3)
    nid = ua.NodeId('AddNodeVar2Id', 3)
    v2 = objects.add_variable(nid, qn, 0)
    assert nid == v2.nodeid
    assert qn == v2.get_browse_name()

def test_add_find_node_(opc):
    objects = opc.get_objects_node()
    o = objects.add_object('ns=2;i=101;', '2:AddFindObject')
    o2 = objects.get_child('2:AddFindObject')
    assert o == o2

def test_node_path(opc):
    objects = opc.get_objects_node()
    o = objects.add_object('ns=2;i=105;', '2:NodePathObject')
    root = opc.get_root_node()
    o2 = root.get_child(['0:Objects', '2:NodePathObject'])
    assert o == o2

def test_add_read_node(opc):
    objects = opc.get_objects_node()
    o = objects.add_object('ns=2;i=102;', '2:AddReadObject')
    nid = ua.NodeId(102, 2)
    assert nid == o.nodeid
    qn = ua.QualifiedName('AddReadObject', 2)
    assert qn == o.get_browse_name()

def test_simple_value(opc):
    o = opc.get_objects_node()
    v = o.add_variable(3, 'VariableTestValue', 4.32)
    val = v.get_value()
    assert 4.32 == val

def test_add_exception(opc):
    objects = opc.get_objects_node()
    o = objects.add_object('ns=2;i=103;', '2:AddReadObject')
    with pytest.raises(ua.UaStatusCodeError):
        o2 = objects.add_object('ns=2;i=103;', '2:AddReadObject')

def test_negative_value(opc):
    o = opc.get_objects_node()
    v = o.add_variable(3, 'VariableNegativeValue', 4)
    v.set_value(-4.54)
    val = v.get_value()
    assert -4.54 == val

def test_read_server_state(opc):
    statenode = opc.get_node(ua.NodeId(ua.ObjectIds.Server_ServerStatus_State))
    state = statenode.get_value()
    assert 0 == state

def test_bad_node(opc):
    bad = opc.get_node(ua.NodeId(999, 999))
    with pytest.raises(ua.UaStatusCodeError):
        bad.get_browse_name()
    with pytest.raises(ua.UaStatusCodeError):
        bad.set_value(89)
    with pytest.raises(ua.UaStatusCodeError):
        bad.add_object(0, "0:myobj")
    with pytest.raises(ua.UaStatusCodeError):
        bad.get_child("0:myobj")

def test_value(opc):
    o = opc.get_objects_node()
    var = ua.Variant(1.98, ua.VariantType.Double)
    v = o.add_variable(3, 'VariableValue', var)
    val = v.get_value()
    assert 1.98 ==  val

    dvar = ua.DataValue(var)
    dv = v.get_data_value()
    assert ua.DataValue == type(dv)
    assert dvar.Value == dv.Value
    assert dvar.Value == var

def test_set_value(opc):
    o = opc.get_objects_node()
    var = ua.Variant(1.98, ua.VariantType.Double)
    dvar = ua.DataValue(var)
    v = o.add_variable(3, 'VariableValue', var)
    v.set_value(var.Value)
    v1 = v.get_value()
    assert v1 == var.Value
    v.set_value(var)
    v2 = v.get_value()
    assert v2 == var.Value
    v.set_data_value(dvar)
    v3 = v.get_data_value()
    assert v3.Value == dvar.Value

def test_array_value(opc):
    o = opc.get_objects_node()
    v = o.add_variable(3, 'VariableArrayValue', [1, 2, 3])
    val = v.get_value()
    assert [1, 2, 3] == val

def test_bool_variable(opc):
    o = opc.get_objects_node()
    v = o.add_variable(3, 'BoolVariable', True)
    dt = v.get_data_type_as_variant_type()
    assert ua.VariantType.Boolean == dt
    val = v.get_value()
    assert val is True
    v.set_value(False)
    val = v.get_value()
    assert val is False

def test_array_size_one_value(opc):
    o = opc.get_objects_node()
    v = o.add_variable(3, 'VariableArrayValue', [1, 2, 3])
    v.set_value([1])
    val = v.get_value()
    assert [1] == val

def test_use_namespace(opc):
    idx = opc.get_namespace_index("urn:freeopcua:python:server")
    assert 1 == idx
    root = opc.get_root_node()
    myvar = root.add_variable(idx, 'var_in_custom_namespace', [5])
    myid = myvar.nodeid
    assert idx == myid.NamespaceIndex

def test_method(opc):
    o = opc.get_objects_node()
    m = o.get_child("2:ServerMethod")
    result = o.call_method("2:ServerMethod", 2.1)
    assert 4.2 == result
    with pytest.raises(ua.UaStatusCodeError):
        # FIXME: we should raise a more precise exception
        result = o.call_method("2:ServerMethod", 2.1, 89, 9)
    with pytest.raises(ua.UaStatusCodeError):
        result = o.call_method(ua.NodeId(999), 2.1)  # non existing method

def test_method_array(opc):
    o = opc.get_objects_node()
    m = o.get_child("2:ServerMethodArray")
    result = o.call_method(m, "sin", ua.Variant(math.pi))
    assert result < 0.01
    with pytest.raises(ua.UaStatusCodeError) as cm:
        result = o.call_method(m, "cos", ua.Variant(math.pi))
    assert ua.StatusCodes.BadInvalidArgument == cm.exception.code
    with pytest.raises(ua.UaStatusCodeError) as cm:
        result = o.call_method(m, "panic", ua.Variant(math.pi))
    assert ua.StatusCodes.BadOutOfMemory == cm.exception.code

def test_method_array2(opc):
    o = opc.get_objects_node()
    m = o.get_child("2:ServerMethodArray2")
    result = o.call_method(m, [1.1, 3.4, 9])
    assert [2.2, 6.8, 18] == result
    result = call_method_full(o, m, [1.1, 3.4, 9])
    assert [[2.2, 6.8, 18]] == result.OutputArguments

def test_method_tuple(opc):
    o = opc.get_objects_node()
    m = o.get_child("2:ServerMethodTuple")
    result = o.call_method(m)
    assert [1, 2, 3] == result
    result = call_method_full(o, m)
    assert [1, 2, 3] == result.OutputArguments

def test_method_none(opc):
    # this test calls the function linked to the type's method..
    o = opc.get_node(ua.ObjectIds.BaseObjectType).get_child("2:ObjectWithMethodsType")
    m = o.get_child("2:ServerMethodDefault")
    result = o.call_method(m)
    assert result is None
    result = call_method_full(o, m)
    assert [] == result.OutputArguments

def test_add_nodes(opc):
    objects = opc.get_objects_node()
    f = objects.add_folder(3, 'MyFolder')
    child = objects.get_child("3:MyFolder")
    assert child == f
    o = f.add_object(3, 'MyObject')
    child = f.get_child("3:MyObject")
    assert child == o
    v = f.add_variable(3, 'MyVariable', 6)
    child = f.get_child("3:MyVariable")
    assert child == v
    p = f.add_property(3, 'MyProperty', 10)
    child = f.get_child("3:MyProperty")
    assert child == p
    childs = f.get_children()
    assert o in childs
    assert v in childs
    assert p in childs

def test_modelling_rules(opc):
    obj = opc.nodes.base_object_type.add_object_type(2, 'MyFooObjectType')
    v = obj.add_variable(2, "myvar", 1.1)
    v.set_modelling_rule(True)
    p = obj.add_property(2, "myvar", 1.1)
    p.set_modelling_rule(False)

    refs = obj.get_referenced_nodes(refs=ua.ObjectIds.HasModellingRule)
    assert 0 == len(refs)

    refs = v.get_referenced_nodes(refs=ua.ObjectIds.HasModellingRule)
    assert opc.get_node(ua.ObjectIds.ModellingRule_Mandatory) == refs[0]

    refs = p.get_referenced_nodes(refs=ua.ObjectIds.HasModellingRule)
    assert opc.get_node(ua.ObjectIds.ModellingRule_Optional) == refs[0]

    p.set_modelling_rule(None)
    refs = p.get_referenced_nodes(refs=ua.ObjectIds.HasModellingRule)
    assert 0 == len(refs)

def test_incl_subtypes(opc):
    base_type = opc.get_root_node().get_child(["0:Types", "0:ObjectTypes", "0:BaseObjectType"])
    descs = base_type.get_children_descriptions(includesubtypes=True)
    assert len(descs) > 10
    descs = base_type.get_children_descriptions(includesubtypes=False)
    assert 0 == len(descs)

def test_add_node_with_type(opc):
    objects = opc.get_objects_node()
    f = objects.add_folder(3, 'MyFolder_TypeTest')

    o = f.add_object(3, 'MyObject1', ua.ObjectIds.BaseObjectType)
    assert ua.ObjectIds.BaseObjectType == o.get_type_definition().Identifier

    o = f.add_object(3, 'MyObject2', ua.NodeId(ua.ObjectIds.BaseObjectType, 0))
    assert ua.ObjectIds.BaseObjectType == o.get_type_definition().Identifier

    base_otype = opc.get_node(ua.ObjectIds.BaseObjectType)
    custom_otype = base_otype.add_object_type(2, 'MyFooObjectType')

    o = f.add_object(3, 'MyObject3', custom_otype.nodeid)
    assert custom_otype.nodeid.Identifier == o.get_type_definition().Identifier

    references = o.get_references(refs=ua.ObjectIds.HasTypeDefinition, direction=ua.BrowseDirection.Forward)
    assert 1 == len(references)
    assert custom_otype.nodeid == references[0].NodeId

def test_references_for_added_nodes(opc):
    objects = opc.get_objects_node()
    o = objects.add_object(3, 'MyObject')
    nodes = objects.get_referenced_nodes(refs=ua.ObjectIds.Organizes, direction=ua.BrowseDirection.Forward,
                                         includesubtypes=False)
    assert o in nodes
    nodes = o.get_referenced_nodes(refs=ua.ObjectIds.Organizes, direction=ua.BrowseDirection.Inverse,
                                   includesubtypes=False)
    assert objects in nodes
    assert objects == o.get_parent()
    assert ua.ObjectIds.BaseObjectType == o.get_type_definition().Identifier
    assert [] == o.get_references(ua.ObjectIds.HasModellingRule)

    o2 = o.add_object(3, 'MySecondObject')
    nodes = o.get_referenced_nodes(refs=ua.ObjectIds.HasComponent, direction=ua.BrowseDirection.Forward,
                                   includesubtypes=False)
    assert o2 in nodes
    nodes = o2.get_referenced_nodes(refs=ua.ObjectIds.HasComponent, direction=ua.BrowseDirection.Inverse,
                                    includesubtypes=False)
    assert o in nodes
    assert o == o2.get_parent()
    assert ua.ObjectIds.BaseObjectType == o2.get_type_definition().Identifier
    assert [] == o2.get_references(ua.ObjectIds.HasModellingRule)

    v = o.add_variable(3, 'MyVariable', 6)
    nodes = o.get_referenced_nodes(refs=ua.ObjectIds.HasComponent, direction=ua.BrowseDirection.Forward,
                                   includesubtypes=False)
    assert v in nodes
    nodes = v.get_referenced_nodes(refs=ua.ObjectIds.HasComponent, direction=ua.BrowseDirection.Inverse,
                                   includesubtypes=False)
    assert o in nodes
    assert o == v.get_parent()
    assert ua.ObjectIds.BaseDataVariableType == v.get_type_definition().Identifier
    assert [] == v.get_references(ua.ObjectIds.HasModellingRule)

    p = o.add_property(3, 'MyProperty', 2)
    nodes = o.get_referenced_nodes(refs=ua.ObjectIds.HasProperty, direction=ua.BrowseDirection.Forward,
                                   includesubtypes=False)
    assert p in nodes
    nodes = p.get_referenced_nodes(refs=ua.ObjectIds.HasProperty, direction=ua.BrowseDirection.Inverse,
                                   includesubtypes=False)
    assert o in nodes
    assert 0 == p.get_parent()
    assert ua.ObjectIds.PropertyType == p.get_type_definition().Identifier
    assert [] == p.get_references(ua.ObjectIds.HasModellingRule)

    m = objects.get_child("2:ServerMethod")
    assert [] == m.get_references(ua.ObjectIds.HasModellingRule)

def test_path_string(opc):
    o = opc.nodes.objects.add_folder(1, "titif").add_object(3, "opath")
    path = o.get_path(as_string=True)
    assert ["0:Root", "0:Objects", "1:titif", "3:opath"] == path
    path = o.get_path(2, as_string=True)
    assert ["1:titif", "3:opath"] == path

def test_path(opc):
    of = opc.nodes.objects.add_folder(1, "titif")
    op = of.add_object(3, "opath")
    path = op.get_path()
    assert [opc.nodes.root, opc.nodes.objects, of, op] == path
    path = op.get_path(2)
    assert [of, op] == path
    target = opc.get_node("i=13387")
    path = target.get_path()
    assert [opc.nodes.root, opc.nodes.types, opc.nodes.object_types, opc.nodes.base_object_type,
         opc.nodes.folder_type, opc.get_node(ua.ObjectIds.FileDirectoryType), target] == path

def test_get_endpoints(opc):
    endpoints = opc.get_endpoints()
    assert len(endpoints) > 0
    assert endpoints[0].EndpointUrl.startswith("opc.tcp://")

def test_copy_node(opc):
    dev_t = opc.nodes.base_data_type.add_object_type(0, "MyDevice")
    v_t = dev_t.add_variable(0, "sensor", 1.0)
    p_t = dev_t.add_property(0, "sensor_id", "0340")
    ctrl_t = dev_t.add_object(0, "controller")
    prop_t = ctrl_t.add_property(0, "state", "Running")
    # Create device sutype
    devd_t = dev_t.add_object_type(0, "MyDeviceDervived")
    v_t = devd_t.add_variable(0, "childparam", 1.0)
    p_t = devd_t.add_property(0, "sensorx_id", "0340")

    nodes = copy_node(opc.nodes.objects, dev_t)
    mydevice = nodes[0]

    assert ua.NodeClass.ObjectType == mydevice.get_node_class()
    assert 4 == len(mydevice.get_children())
    obj = mydevice.get_child(["0:controller"])
    prop = mydevice.get_child(["0:controller", "0:state"])
    assert ua.ObjectIds.PropertyType == prop.get_type_definition().Identifier
    assert "Running" == prop.get_value()
    assert prop.nodeid != prop_t.nodeid

def test_instantiate_1(opc):
    # Create device type
    dev_t = opc.nodes.base_object_type.add_object_type(0, "MyDevice")
    v_t = dev_t.add_variable(0, "sensor", 1.0)
    v_t.set_modelling_rule(True)
    p_t = dev_t.add_property(0, "sensor_id", "0340")
    p_t.set_modelling_rule(True)
    ctrl_t = dev_t.add_object(0, "controller")
    ctrl_t.set_modelling_rule(True)
    v_opt_t = dev_t.add_variable(0, "vendor", 1.0)
    v_opt_t.set_modelling_rule(False)
    v_none_t = dev_t.add_variable(0, "model", 1.0)
    v_none_t.set_modelling_rule(None)
    prop_t = ctrl_t.add_property(0, "state", "Running")
    prop_t.set_modelling_rule(True)

    # Create device sutype
    devd_t = dev_t.add_object_type(0, "MyDeviceDervived")
    v_t = devd_t.add_variable(0, "childparam", 1.0)
    v_t.set_modelling_rule(True)
    p_t = devd_t.add_property(0, "sensorx_id", "0340")
    p_t.set_modelling_rule(True)

    # instanciate device
    nodes = instantiate(opc.nodes.objects, dev_t, bname="2:Device0001")
    mydevice = nodes[0]

    assert ua.NodeClass.Object == mydevice.get_node_class()
    assert dev_t.nodeid == mydevice.get_type_definition()
    obj = mydevice.get_child(["0:controller"])
    prop = mydevice.get_child(["0:controller", "0:state"])
    with pytest.raises(ua.UaError):
        mydevice.get_child(["0:controller", "0:vendor"])
    with pytest.raises(ua.UaError):
        mydevice.get_child(["0:controller", "0:model"])

    assert ua.ObjectIds.PropertyType == prop.get_type_definition().Identifier
    assert "Running" == prop.get_value()
    assert prop.nodeid != prop_t.nodeid

    # instanciate device subtype
    nodes = instantiate(opc.nodes.objects, devd_t, bname="2:Device0002")
    mydevicederived = nodes[0]
    prop1 = mydevicederived.get_child(["0:sensorx_id"])
    var1 = mydevicederived.get_child(["0:childparam"])
    var_parent = mydevicederived.get_child(["0:sensor"])
    prop_parent = mydevicederived.get_child(["0:sensor_id"])

def test_instantiate_string_nodeid(opc):
    # Create device type
    dev_t = opc.nodes.base_object_type.add_object_type(0, "MyDevice2")
    v_t = dev_t.add_variable(0, "sensor", 1.0)
    v_t.set_modelling_rule(True)
    p_t = dev_t.add_property(0, "sensor_id", "0340")
    p_t.set_modelling_rule(True)
    ctrl_t = dev_t.add_object(0, "controller")
    ctrl_t.set_modelling_rule(True)
    prop_t = ctrl_t.add_property(0, "state", "Running")
    prop_t.set_modelling_rule(True)

    # instanciate device
    nodes = instantiate(opc.nodes.objects, dev_t, nodeid=ua.NodeId("InstDevice", 2, ua.NodeIdType.String),
                        bname="2:InstDevice")
    mydevice = nodes[0]

    assert ua.NodeClass.Object == mydevice.get_node_class()
    assert dev_t.nodeid == mydevice.get_type_definition()
    obj = mydevice.get_child(["0:controller"])
    obj_nodeid_ident = obj.nodeid.Identifier
    prop = mydevice.get_child(["0:controller", "0:state"])
    assert "InstDevice.controller" == obj_nodeid_ident
    assert ua.ObjectIds.PropertyType == prop.get_type_definition().Identifier
    assert "Running" == prop.get_value()
    assert prop.nodeid != prop_t.nodeid

def test_variable_with_datatype(opc):
    v1 = opc.nodes.objects.add_variable(3, 'VariableEnumType1', ua.ApplicationType.ClientAndServer,
                                             datatype=ua.NodeId(ua.ObjectIds.ApplicationType))
    tp1 = v1.get_data_type()
    assert tp1 == ua.NodeId(ua.ObjectIds.ApplicationType)

    v2 = opc.nodes.objects.add_variable(3, 'VariableEnumType2', ua.ApplicationType.ClientAndServer,
                                             datatype=ua.NodeId(ua.ObjectIds.ApplicationType))
    tp2 = v2.get_data_type()
    assert tp2 == ua.NodeId(ua.ObjectIds.ApplicationType)

def test_enum(opc):
    # create enum type
    enums = opc.get_root_node().get_child(["0:Types", "0:DataTypes", "0:BaseDataType", "0:Enumeration"])
    myenum_type = enums.add_data_type(0, "MyEnum")
    es = myenum_type.add_variable(0, "EnumStrings",
                                  [ua.LocalizedText("String0"), ua.LocalizedText("String1"),
                                   ua.LocalizedText("String2")],
                                  ua.VariantType.LocalizedText)
    # es.set_value_rank(1)
    # instantiate
    o = opc.get_objects_node()
    myvar = o.add_variable(2, "MyEnumVar", ua.LocalizedText("String1"), datatype=myenum_type.nodeid)
    # myvar.set_writable(True)
    # tests
    assert myenum_type.nodeid == myvar.get_data_type()
    myvar.set_value(ua.LocalizedText("String2"))

def test_supertypes(opc):
    nint32 = opc.get_node(ua.ObjectIds.Int32)
    node = ua_utils.get_node_supertype(nint32)
    assert opc.get_node(ua.ObjectIds.Integer) == node

    nodes = ua_utils.get_node_supertypes(nint32)
    assert opc.get_node(ua.ObjectIds.Number) == nodes[1]
    assert opc.get_node(ua.ObjectIds.Integer) == nodes[0]

    # test custom
    dtype = nint32.add_data_type(0, "MyCustomDataType")
    node = ua_utils.get_node_supertype(dtype)
    assert nint32 == node

    dtype2 = dtype.add_data_type(0, "MyCustomDataType2")
    node = ua_utils.get_node_supertype(dtype2)
    assert dtype == node

def test_base_data_type(opc):
    nint32 = opc.get_node(ua.ObjectIds.Int32)
    dtype = nint32.add_data_type(0, "MyCustomDataType")
    dtype2 = dtype.add_data_type(0, "MyCustomDataType2")
    assert nint32 == ua_utils.get_base_data_type(dtype)
    assert nint32 == ua_utils.get_base_data_type(dtype2)

    ext = opc.nodes.objects.add_variable(0, "MyExtensionObject", ua.Argument())
    d = ext.get_data_type()
    d = opc.get_node(d)
    assert opc.get_node(ua.ObjectIds.Structure) == ua_utils.get_base_data_type(d)
    assert ua.VariantType.ExtensionObject == ua_utils.data_type_to_variant_type(d)

def test_data_type_to_variant_type(opc):
    test_data = {
        ua.ObjectIds.Boolean: ua.VariantType.Boolean,
        ua.ObjectIds.Byte: ua.VariantType.Byte,
        ua.ObjectIds.String: ua.VariantType.String,
        ua.ObjectIds.Int32: ua.VariantType.Int32,
        ua.ObjectIds.UInt32: ua.VariantType.UInt32,
        ua.ObjectIds.NodeId: ua.VariantType.NodeId,
        ua.ObjectIds.LocalizedText: ua.VariantType.LocalizedText,
        ua.ObjectIds.Structure: ua.VariantType.ExtensionObject,
        ua.ObjectIds.EnumValueType: ua.VariantType.ExtensionObject,
        ua.ObjectIds.Enumeration: ua.VariantType.Int32,  # enumeration
        ua.ObjectIds.AttributeWriteMask: ua.VariantType.UInt32,
        ua.ObjectIds.AxisScaleEnumeration: ua.VariantType.Int32  # enumeration
    }
    for dt, vdt in test_data.items():
        assert vdt == ua_utils.data_type_to_variant_type(opc.get_node(ua.NodeId(dt)))
