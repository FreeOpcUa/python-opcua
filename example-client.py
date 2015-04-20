import logging
import time

try:
    from IPython import embed
except ImportError:
    import code
    def embed():
        vars = globals()
        vars.update(locals())
        shell = code.InteractiveConsole(vars)
        shell.interact()


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
    logging.basicConfig(level=logging.WARN)
    #logger = logging.getLogger("KeepAlive")
    #logger.setLevel(logging.DEBUG)
    client = Client("opc.tcp://localhost:4841/freeopcua/server/")
    try:
        client.connect()
        root = client.get_root_node()
        print(root)
        print(root.get_children())
        print(root.get_browse_name())
        #var = client.get_node(ua.NodeId(1002, 2))
        #print(var)
        #print(var.get_value())
        #var.set_value(ua.Variant([23], ua.VariantType.Int64))
        state = root.get_child(["0:Objects", "0:Server"])
        print(state)
        myvar = root.get_child(["0:Objects", "2:NewObject", "2:MyVariable"])
        obj = root.get_child(["0:Objects", "2:NewObject"])
        print("yvar is: ", myvar)
        handler = SubHandler()
        sub = client.create_subscription(500, handler)
        handle = sub.subscribe_data_change(myvar)
        time.sleep(0.1)
        sub.subscribe_events()
        #sub.unsubscribe(handle)
        #sub.delete()
        
        #calling a method on server
        res = obj.call_method("2:multiply", 3, "klk")
        print("method result is: ", res)

        embed()
    finally:
        client.disconnect()
