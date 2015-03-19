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
        objects = server.get_objects_node()
        myfolder = objects.add_folder(2, "myfolder")
        myvar = myfolder.add_variable(2, "myvar", 6.7)
        myobj = myfolder.add_object(2, "myobj")
        myarrayvar = myobj.add_variable(2, "myarrayvar", [6.7, 7.9])
        myprop = myobj.add_property(2, "myproperty", "I am a property")
        embed()
    finally:
        server.stop()

