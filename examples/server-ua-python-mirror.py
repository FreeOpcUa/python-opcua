import sys
sys.path.insert(0, "..")
import time


from opcua import ua, Server

# INFO: The concept in this example is that the software model is first built in OPC UA via XML. After that, matching
# python objects are created based on the UA address space design. Do not use this example to build a UA address space
# from the python design.

# The advantage of this is that the software can be designed in a tool like UA Modeler. Then with minimal setup, a
# python program will import the XML and mirror all the objects in the software design. After this mirroring is achieved
# the user can focus on programming in python knowing that all all data from UA clients will reach the python object,
# and all data that needs to be output to the server can be published from the python object.
#
# Be aware that subscription calls are asynchronous.


class SubHandler(object):
    """
    Subscription Handler. To receive events from server for a subscription.
    The handler forwards updates to it's referenced python object
    """

    def __init__(self, obj):
        self.obj = obj

    def datachange_notification(self, node, val, data):
        # print("Python: New data change event", node, val, data)

        _node_name = node.get_browse_name()
        setattr(self.obj, _node_name.Name, data.monitored_item.Value.Value.Value)


class UaObject(object):
    """
    Python object which mirrors an OPC UA object
    Child UA variables/properties are auto subscribed to to synchronize python with UA server
    Python can write to children via write method, which will trigger an update for UA clients
    """
    def __init__(self, opcua_server, ua_node):
        self.opcua_server = opcua_server
        self.nodes = {}
        self.b_name = ua_node.get_browse_name().Name

        # keep track of the children of this object (in case python needs to write, or get more info from UA server)
        for _child in ua_node.get_children():
            _child_name = _child.get_browse_name()
            self.nodes[_child_name.Name] = _child

        # find all children which can be subscribed to (python object is kept up to date via subscription)
        sub_children = ua_node.get_properties()
        sub_children.extend(ua_node.get_variables())

        # subscribe to properties/variables
        handler = SubHandler(self)
        sub = opcua_server.create_subscription(500, handler)
        handle = sub.subscribe_data_change(sub_children)

    def write(self, attr=None):
        # if a specific attr isn't passed to write, write all OPC UA children
        if attr is None:
            for k, node in self.nodes.items():
                node_class = node.get_node_class()
                if node_class == ua.NodeClass.Variable:
                    node.set_value(getattr(self, k))
        # only update a specific attr
        else:
            self.nodes[attr].set_value(getattr(self, attr))


class MyObj(UaObject):
    """
    Definition of OPC UA object which represents a object to be mirrored in python
    This class mirrors it's UA counterpart and semi-configures itself according to the UA model (generally from XML)
    """
    def __init__(self, opcua_server, ua_node):

        # properties and variables; must mirror UA model (based on browsename!)
        self.MyVariable = 0
        self.MyProperty = 0
        self.MyClientWrite = 0

        # init the UaObject super class to connect the python object to the UA object
        super().__init__(opcua_server, ua_node)

        # local values only for use inside python
        self.testval = 'python only'

        # If the object has other objects as children it is best to search by type and instantiate more
        # mirrored python classes so that your UA object tree matches your python object tree

        # ADD CUSTOM OBJECT INITIALIZATION BELOW
        # find children by type and instantiate them as sub-objects of this class
        # NOT PART OF THIS EXAMPLE


if __name__ == "__main__":

    # setup our server
    server = Server()
    server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")

    # setup our own namespace, not really necessary but should as spec
    uri = "http://examples.freeopcua.github.io"
    idx = server.register_namespace(uri)

    # get Objects node, this is where we should put our nodes
    objects = server.get_objects_node()

    # populating our address space; in most real use cases this should be imported from UA spec XML
    myobj = objects.add_object(idx, "MyObject")
    myvar = myobj.add_variable(idx, "MyVariable", 0.0)
    myprop = myobj.add_property(idx, "MyProperty", 0)
    mywritevar = myobj.add_variable(idx, "MyClientWrite", 0)
    mywritevar.set_writable()    # Set MyVariable to be writable by clients

    # starting!
    server.start()

    # after the UA server is started initialize the mirrored object
    my_python_obj = MyObj(server, myobj)
    
    try:
        while True:
            # from an OPC UA client write a value to this node to see it show up in the python object
            print('Python mirror of MyClientWrite is: ' + str(my_python_obj.MyClientWrite))

            # write a single attr to OPC UA
            my_python_obj.MyVariable = 12.3
            my_python_obj.MyProperty = 55  # this value will not be visible to clients because write is not called
            my_python_obj.write('MyVariable')

            time.sleep(3)

            # write all attr of the object to OPC UA
            my_python_obj.MyVariable = 98.1
            my_python_obj.MyProperty = 99
            my_python_obj.write()

            time.sleep(3)

            # write directly to the OPC UA node of the object
            dv = ua.DataValue(ua.Variant(5.5, ua.VariantType.Double))
            my_python_obj.nodes['MyVariable'].set_value(dv)
            dv = ua.DataValue(ua.Variant(4, ua.VariantType.UInt64))
            my_python_obj.nodes['MyVariable'].set_value(dv)

            time.sleep(3)

    finally:
        # close connection, remove subscriptions, etc
        server.stop()
