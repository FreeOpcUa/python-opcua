import sys
sys.path.insert(0, "..")
import time


from opcua import ua, Server


if __name__ == "__main__":

    # setup our server
    server = Server()
    server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")

    # setup our own namespace, not really necessary but should as spec
    uri = "http://examples.freeopcua.github.io"
    idx = server.register_namespace(uri)

    # Import customobject type
    server.import_xml('customobject.xml')

    # get Objects node, this is where we should put our custom stuff
    objects = server.get_objects_node()


    # get nodeid of custom object type by :
    # 1) Use node ID
    # 2) Or Full path
    # 3) Or As child from parent
    nodeid_a = ua.NodeId.from_string('ns=1;i=1002')
    nodeid_b = server.get_root_node().get_child(["0:Types", "0:ObjectTypes", "0:BaseObjectType", "1:MyObjectType"]).nodeid
    nodeid_c = server.get_node(ua.ObjectIds.BaseObjectType).get_child(["1:MyObjectType"]).nodeid


    myobject_type_nodeid = nodeid_a

    # populating our address space
    myobj = objects.add_object(idx, "MyObject",)
    myobj = objects.add_object(idx, "MyCustomObject", myobject_type_nodeid)

    # starting!
    server.start()

    try:
        while True:
            time.sleep(1)
    finally:
        # close connection, remove subcsriptions, etc
        server.stop()
