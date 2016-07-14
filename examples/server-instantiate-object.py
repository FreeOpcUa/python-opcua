import sys
sys.path.insert(0, "..")
import time
from IPython import embed


from opcua import ua, Server, instantiate


if __name__ == "__main__":

    # setup our server
    server = Server()
    server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")

    # setup our own namespace, not really necessary but should as spec
    uri = "http://examples.freeopcua.github.io"
    idx = server.register_namespace(uri)


    # create our custom object type
    base_type = server.get_root_node().get_child(["0:Types", "0:ObjectTypes", "0:BaseObjectType"])
    dev = base_type.add_object_type(0, "MyDevice")
    dev.add_variable(0, "sensor", 1.0)
    dev.add_property(0, "sensor_id", "0340")
    ctrl = dev.add_object(0, "controller")
    ctrl.add_property(0, "state", "Running")


    # get Objects node, this is where we should put our custom stuff
    objects = server.get_objects_node()

    # instantiate our new object type

    mydevice = instantiate(objects, dev, bname="2:Device0001")



    # starting!
    server.start()

    try:
        embed()
    finally:
        # close connection, remove subcsriptions, etc
        server.stop()
