import sys
sys.path.insert(0, "..")
import time
import logging


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
    myvar.set_writable()  # Set MyVariable to be writable by clients

    # Creating a custom event: Approach 1
    # The custom event object automatically will have members from its parent (BaseEventType)
    etype = server.create_custom_event_type(2, 'MyFirstEvent', ua.ObjectIds.BaseEventType,
                                            [('MyNumericProperty', ua.VariantType.Float),
                                             ('MyStringProperty', ua.VariantType.String)])
    # create second event
    etype2 = server.create_custom_event_type(2, 'MySecondEvent', ua.ObjectIds.BaseEventType,
                                             [('MyOtherProperty', ua.VariantType.Float)])

    myevgen = server.get_event_generator(etype, myobj)
    myevgen.event.Severity = 500
    myevgen.event.MyStringProperty = ua.Variant("hello world")
    myevgen.event.MyNumericProperty = ua.Variant(-456)

    myevgen2 = server.get_event_generator(etype2, myobj)
    myevgen2.event.Severity = 123
    myevgen2.event.MyOtherProperty = ua.Variant(1.337)

    serverevgen = server.get_event_generator()
    serverevgen.event.Severity = 111

    # Configure server to use sqlite as history database (default is a simple in memory dict)
    server.iserver.history_manager.set_storage(HistorySQLite("my_event_history.sql"))

    # starting!
    server.start()

    # enable history for myobj events
    server.iserver.enable_history_event(myobj, period=None)

    # enable history for server events
    server_node = server.get_node(ua.ObjectIds.Server)
    server.iserver.enable_history_event(server_node, period=None)

    try:
        count = 0
        while True:
            time.sleep(1)
            count += 0.1
            myevgen.trigger(message="This is MyFirstEvent " + str(count))
            myevgen2.trigger(message="This is MySecondEvent " + str(count))
            serverevgen.trigger(message="Server Event Message")

            res = server_node.read_event_history(None, None, 0)

    finally:
        # close connection, remove subscriptions, etc
        server.stop()
