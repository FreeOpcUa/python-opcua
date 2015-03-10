import logging

from opcua import Client
from opcua import uaprotocol as ua

class SubHandler(object):
    """
    Client to subcsription. It will receive events from server
    """
    def data_change(self, handle, node, val, attr):
        print("Python: New data change event", handle, node, val, attr)

    def event(self, handle, event):
        print("Python: New event", handle, event)



if __name__ == "__main__": 
    from IPython import embed
    logging.basicConfig(level=logging.DEBUG)
    client = Client("opc.tcp://localhost:4841/freeopcua/server/")
    try:
        client.connect()
        root = client.get_root_node()
        print(root)
        print(root.get_children())
        print(root.get_name())
        var = client.get_node(ua.NodeId(1002, 2))
        print(var)
        print(var.get_value())
        var.set_value(ua.Variant([23], ua.VariantType.Int64))
        myvar = root.get_child(["0:Objects", "2:NewObject", "2:MyVariable"])
        print("yvar is: ", myvar)
        handler = SubHandler()
        sub = client.create_subscription(500, handler)
        sub.subscribe_data_change(myvar)
        embed()
        client.close_session()
    finally:
        client.disconnect()
