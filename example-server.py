import time
import logging
from opcua import ua
from opcua.server import Server

from IPython import embed

class SubHandler(object):
    """
    Client to subscription. It will receive events from server
    """
    def data_change(self, handle, node, val, attr):
        print("Python: New data change event", handle, node, val, attr)

    def event(self, handle, event):
        print("Python: New event", handle, event)




if __name__ == "__main__":
    #optional setup logging
    logging.basicConfig(level=logging.WARN)
    #logger = logging.getLogger("opcua.address_space")
    #logger = logging.getLogger("opcua.internal_server")
    #logger.setLevel(logging.DEBUG)
    #logger = logging.getLogger("opcua.subscription_server")
    #logger.setLevel(logging.DEBUG)


    # now setup our server 
    server = Server()
    server.set_endpoint("opc.tcp://localhost:4841/freeopcua/server/")
    server.set_server_name("FreeOpcUa Example Server")

    # setup our own namespace
    uri = "http://examples.freeopcua.github.io"
    idx = server.register_namespace(uri)

    # get Objects node, this is where we should put our custom stuff
    objects = server.get_objects_node()

    # populating our address space
    myfolder = objects.add_folder(idx, "myfolder")
    myobj = objects.add_object(idx, "NewObject")
    myvar = myobj.add_variable(idx, "MyVariable", 6.7)
    myarrayvar = myobj.add_variable(idx, "myarrayvar", [6.7, 7.9])
    myprop = myobj.add_property(idx, "myproperty", "I am a property")
    
    # starting!
    server.start()
    print("Available loggers are: ", logging.Logger.manager.loggerDict.keys())
    try:
        handler = SubHandler()
        #enable following if you want to subscribe to nodes on server side
        #sub = server.create_subscription(500, handler)
        #handle = sub.subscribe_data_change(myvar)
        #time.sleep(0.1)
        #sub.unsubscribe(handle)
        #sub.delete()
        embed()
    finally:
        server.stop()

