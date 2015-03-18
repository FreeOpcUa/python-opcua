import time
import logging
from opcua import ua
from opcua.server import Server

from IPython import embed


if __name__ == "__main__":
    logging.basicConfig(level=logging.WARN)
    #logger = logging.getLogger("opcua.address_space")
    logger = logging.getLogger("opcua.internal_server")
    logger.setLevel(logging.DEBUG)
    server = Server()
    server.set_endpoint("opc.tcp://localhost:4841/freeopcua/server/")
    server.set_server_name("FreeOpcUa Example Server")
    server.start()
    print("Available loggers are: ", logging.Logger.manager.loggerDict.keys())
    try:
        root = server.get_root_node()
        root.add_folder(2, "myfolder")
        embed()
    finally:
        server.stop()

