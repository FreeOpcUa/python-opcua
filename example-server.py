import time
import logging
from opcua import ua
from opcua.server import Server

from IPython import embed


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    server = Server()
    server.set_endpoint("opc.tcp://localhost:4841/freeopcua/server/")
    server.set_server_name("FreeOpcUa Example Server")
    server.start()
    try:
        embed()
    finally:
        server.stop()

