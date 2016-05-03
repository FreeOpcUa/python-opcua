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

    myevgen2 = server.get_event_generator(etype2, myobj)
    myevgen2.event.Severity = 123
    myevgen2.event.MyOtherProperty = ua.Variant(1.337)

    # Configure server to use sqlite as history database (default is a simple in memory dict)
    server.iserver.history_manager.set_storage(HistorySQLite(":memory:"))

    # starting!
    server.start()

    # enable history for this particular node, must be called after start since it uses subscription
    server.iserver.enable_history(myvar, period=None, count=100)

    # enable history for myobj events
    server.iserver.enable_event_history(myobj, period=None)

    try:
        count = 0
        while True:
            time.sleep(1)
            count += 0.1
            myvar.set_value(math.sin(count))
            myevgen.trigger(message="This is MyFirstEvent with MyNumericProperty and MyStringProperty.")
            myevgen2.trigger(message="This is MySecondEvent with MyOtherProperty.")
    finally:
        # close connection, remove subscriptions, etc
        server.stop()
