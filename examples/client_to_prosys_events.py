import sys
sys.path.insert(0, "..")
import logging

from opcua import Client
from opcua import ua
from IPython import embed


class SubHandler(object):

    """
    Subscription Handler. To receive events from server for a subscription
    """

    def datachange_notification(self, node, val, data):
        print("Python: New data change event", node, val)

    def event_notification(self, event):
        print("Python: New event", event.EventType)




if __name__ == "__main__":
    #from IPython import embed
    logging.basicConfig(level=logging.WARN)
    client = Client("opc.tcp://localhost:53530/OPCUA/SimulationServer/")
    #client = Client("opc.tcp://olivier:olivierpass@localhost:53530/OPCUA/SimulationServer/")
    try:
        client.connect()
        root = client.get_root_node()
        print("Root is", root)

        handler = SubHandler()
        sub = client.create_subscription(500, handler)
        handle = sub.subscribe_events(evtype=2788)
        # refresh server condition to force generation of events
        cond = root.get_child(["0:Types", "0:EventTypes", "0:BaseEventType", "0:ConditionType"])
        cond.call_method("0:ConditionRefresh", ua.Variant(sub.subscription_id, ua.VariantType.UInt32))

        embed()
    finally:
        client.disconnect()
