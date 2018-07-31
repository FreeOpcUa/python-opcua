import pytest
from opcua import Client
from opcua import Server
from .test_common import add_server_methods

port_num1 = 48510
port_num = 48540


def pytest_generate_tests(metafunc):
    if 'opc' in metafunc.fixturenames:
        metafunc.parametrize('opc', ['client', 'server'], indirect=True)


@pytest.fixture()
async def opc(request):
    if request.param == 'client':
        srv = Server()
        await srv.init()
        srv.set_endpoint(f'opc.tcp://127.0.0.1:{port_num}')
        await add_server_methods(srv)
        await srv.start()
        # start client
        # long timeout since travis (automated testing) can be really slow
        clt = Client(f'opc.tcp://admin@127.0.0.1:{port_num}', timeout=10)
        await clt.connect()
        yield clt
        await clt.disconnect()
        await srv.stop()
    elif request.param == 'server':
        # start our own server
        # start our own server
        srv = Server()
        await srv.init()
        srv.set_endpoint(f'opc.tcp://127.0.0.1:{port_num}')
        await add_server_methods(srv)
        await srv.start()
        yield srv
        # stop the server
        await srv.stop()
    else:
        raise ValueError("invalid internal test config")
