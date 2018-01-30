import pytest

from opcua import Client
from opcua import Server
from opcua import ua

from .tests_subscriptions import SubscriptionTests
from .tests_common import CommonTests, add_server_methods
from .tests_xml import XmlTests

port_num1 = 48510


@pytest.yield_fixture()
async def admin_client():
    # start admin client
    # long timeout since travis (automated testing) can be really slow
    clt = Client(f'opc.tcp://admin@127.0.0.1:{port_num1}', timeout=10)
    await clt.connect()
    yield clt
    await clt.disconnect()


@pytest.yield_fixture()
async def client():
    # start anonymous client
    ro_clt = Client(f'opc.tcp://127.0.0.1:{port_num1}')
    await ro_clt.connect()
    yield ro_clt
    await ro_clt.disconnect()


@pytest.yield_fixture()
async def server():
    # start our own server
    srv = Server()
    srv.set_endpoint(f'opc.tcp://127.0.0.1:{port_num1}')
    await add_server_methods(srv)
    await srv.start()
    yield srv
    # stop the server
    await srv.stop()


@pytest.mark.asyncio
async def test_service_fault(server, admin_client):
    request = ua.ReadRequest()
    request.TypeId = ua.FourByteNodeId(999)  # bad type!
    with pytest.raises(ua.UaStatusCodeError):
        await admin_client.uaclient.protocol.send_request(request)


@pytest.mark.asyncio
async def test_objects_anonymous(server, client):
    objects = client.get_objects_node()
    with pytest.raises(ua.UaStatusCodeError):
        objects.set_attribute(ua.AttributeIds.WriteMask, ua.DataValue(999))
    with pytest.raises(ua.UaStatusCodeError):
        f = objects.add_folder(3, 'MyFolder')


@pytest.mark.asyncio
async def test_folder_anonymous(server, client):
    objects = client.get_objects_node()
    f = objects.add_folder(3, 'MyFolderRO')
    f_ro = client.get_node(f.nodeid)
    assert f == f_ro
    with pytest.raises(ua.UaStatusCodeError):
        f2 = f_ro.add_folder(3, 'MyFolder2')


@pytest.mark.asyncio
async def test_variable_anonymous(server, admin_client, client):
    objects = admin_client.get_objects_node()
    v = objects.add_variable(3, 'MyROVariable', 6)
    v.set_value(4)  # this should work
    v_ro = client.get_node(v.nodeid)
    with pytest.raises(ua.UaStatusCodeError):
        v_ro.set_value(2)
    assert await v_ro.get_value() == 4
    v.set_writable(True)
    v_ro.set_value(2)  # now it should work
    assert await v_ro.get_value() == 2
    v.set_writable(False)
    with pytest.raises(ua.UaStatusCodeError):
        v_ro.set_value(9)
    assert await v_ro.get_value() == 2


@pytest.mark.asyncio
async def test_context_manager(server):
    """Context manager calls connect() and disconnect()"""
    state = [0]

    def increment_state(*args, **kwargs):
        state[0] += 1

    # create client and replace instance methods with dummy methods
    client = Client('opc.tcp://dummy_address:10000')
    client.connect = increment_state.__get__(client)
    client.disconnect = increment_state.__get__(client)

    assert state[0] == 0
    with client:
        # test if client connected
        assert state[0] == 1
    # test if client disconnected
    assert state[0] == 2


@pytest.mark.asyncio
async def test_enumstrings_getvalue(server, client):
    """
    The real exception is server side, but is detected by using a client.
    All due the server trace is also visible on the console.
    The client only 'sees' an TimeoutError
    """
    nenumstrings = client.get_node(ua.ObjectIds.AxisScaleEnumeration_EnumStrings)
    value = ua.Variant(nenumstrings.get_value())
