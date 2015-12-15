import sys
sys.path.insert(0, "..")
import logging

from opcua import Client
from opcua import uaprotocol as ua


class SubHandler(object):

    """
    Client to subscription. It will receive events from server
    """

    def data_change(self, handle, node, val, attr):
        print("Python: New data change event", handle, node, val, attr)

    def event(self, handle, event):
        print("Python: New event", handle, event)


if __name__ == "__main__":
    #from IPython import embed
    logging.basicConfig(level=logging.WARN)
    client = Client("opc.tcp://localhost:53530/OPCUA/SimulationServer/")
    #client = Client("opc.tcp://olivier:olivierpass@localhost:53530/OPCUA/SimulationServer/")
    try:
        client.connect()
        root = client.get_root_node()
        print("Root is", root)
        print("childs of root are: ", root.get_children())
        print("name of root is", root.get_browse_name())
        objects = client.get_objects_node()
        print("childs og objects are: ", objects.get_children())
        myfloat = client.get_node("ns=4;s=Float")
        mydouble = client.get_node("ns=4;s=Double")
        myint64 = client.get_node("ns=4;s=Int64")
        myuint64 = client.get_node("ns=4;s=UInt64")
        myint32 = client.get_node("ns=4;s=Int32")
        myuint32 = client.get_node("ns=4;s=UInt32")

        var = client.get_node(ua.NodeId("Random1", 5))
        print("var is: ", var)
        print("value of var is: ", var.get_value())
        var.set_value(ua.Variant([23], ua.VariantType.Double))
        print("setting float value")
        myfloat.set_value(ua.Variant(1.234, ua.VariantType.Float))
        print("reading float value: ", myfloat.get_value())

        handler = SubHandler()
        sub = client.create_subscription(500, handler)
        handle = sub.subscribe_data_change(var)

        device = objects.get_child(["2:MyObjects", "2:MyDevice"])
        method = device.get_child("2:MyMethod")
        result = device.call_method(method, ua.Variant("sin"), ua.Variant(180, ua.VariantType.Double))
        print("Mehtod result is: ", result)

        #embed()
        sub.unsubscribe(handle)
        sub.delete()
        #client.close_session()
    finally:
        client.disconnect()
