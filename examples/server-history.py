import sys
sys.path.insert(0, "..")
import time
import math


from opcua import ua, Server
from opcua.server.history_sql import HistorySQLite


if __name__ == "__main__":

    # setup our server
    server = Server()
    server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")

    # setup our own namespace, not really necessary but should as spec
    uri = "http://examples.freeopcua.github.io"
    idx = server.register_namespace(uri)

    # get Objects node, this is where we should put our custom stuff
    objects = server.get_objects_node()

    # populating our address space
    myobj = objects.add_object(idx, "MyObject")
    myvar = myobj.add_variable(idx, "MyVariable", ua.Variant(0, ua.VariantType.Double))
    myvar.set_writable()    # Set MyVariable to be writable by clients

    # creating an event object
    # The event object automatically will have members for all events properties
    myevent = server.get_event_object(ua.ObjectIds.BaseEventType)
    myevent.Message.Text = "This is my event"
    myevent.Severity = 300

    server_obj = server.get_node(myevent.SourceNode)

    # Configure server to use sqlite as history database (default is a simple in memory dict)
    server.iserver.history_manager.set_storage(HistorySQLite("history.db"))

    # starting!
    server.start()

    # enable history for this particular node, must be called after start since it uses subscription
    server.iserver.enable_history(myvar, period=None, count=100)

    # enable history for server events
    server.iserver.enable_event_history(server_obj, period=None)

    try:
        count = 0
        while True:
            time.sleep(1)
            count += 0.1
            myvar.set_value(math.sin(count))
            myevent.trigger()
    finally:
        #close connection, remove subcsriptions, etc
        server.stop()
