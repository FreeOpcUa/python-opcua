
import asyncio
from opcua import ua, Server


async def task(loop):
    # setup our server
    server = Server()
    server.set_endpoint('opc.tcp://0.0.0.0:4840/freeopcua/server/')

    # setup our own namespace, not really necessary but should as spec
    uri = 'http://examples.freeopcua.github.io'
    idx = await server.register_namespace(uri)

    # get Objects node, this is where we should put our nodes
    objects = server.get_objects_node()

    # populating our address space
    myobj = objects.add_object(idx, 'MyObject')
    myvar = myobj.add_variable(idx, 'MyVariable', 6.7)
    myvar.set_writable()  # Set MyVariable to be writable by clients

    # starting!
    await server.start()

    try:
        count = 0
        while True:
            await asyncio.sleep(1)
            count += 0.1
            myvar.set_value(count)
    finally:
        # close connection, remove subcsriptions, etc
        server.stop()


def main():
    loop = asyncio.get_event_loop()
    loop.set_debug(True)
    loop.run_until_complete(task(loop))
    loop.close()


if __name__ == '__main__':
    main()
