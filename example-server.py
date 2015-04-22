import time
import logging

try:
    from IPython import embed
except ImportError:
    import code
    def embed():
        vars = globals()
        vars.update(locals())
        shell = code.InteractiveConsole(vars)
        shell.interact()


from opcua import ua, uamethod, Server, Event, ObjectIds


class SubHandler(object):
    """
    Client to subscription. It will receive events from server
    """
    def data_change(self, handle, node, val, attr):
        print("Python: New data change event", handle, node, val, attr)

    def event(self, handle, event):
        print("Python: New event", handle, event)

#method to be exposed through server
def func(parent, variant):
    return [variant.Value * 2]

#method to be exposed through server
# uses a decorator to automatically convert to and from variants
@uamethod
def multiply(parent, x, y):
    print("multiply method call with parameters: ", x, y)
    return x*y


if __name__ == "__main__":
    #optional setup logging
    logging.basicConfig(level=logging.WARN)
    #logger = logging.getLogger("opcua.address_space")
    #logger = logging.getLogger("opcua.internal_server")
    #logger.setLevel(logging.DEBUG)
    #logger = logging.getLogger("opcua.subscription_server")
    #logger.setLevel(logging.DEBUG)


    # now setup our server 
    server = Server()
    server.set_endpoint("opc.tcp://localhost:4841/freeopcua/server/")
    server.set_server_name("FreeOpcUa Example Server")

    # setup our own namespace
    uri = "http://examples.freeopcua.github.io"
    idx = server.register_namespace(uri)

    # get Objects node, this is where we should put our custom stuff
    objects = server.get_objects_node()

    # populating our address space
    myfolder = objects.add_folder(idx, "myfolder")
    myobj = objects.add_object(idx, "NewObject")
    myvar = myobj.add_variable(idx, "MyVariable", 6.7)
    myarrayvar = myobj.add_variable(idx, "myarrayvar", [6.7, 7.9])
    myprop = myobj.add_property(idx, "myproperty", "I am a property")
    mymethod = myobj.add_method(idx, "mymethod", func, [ua.VariantType.Int64], [ua.VariantType.Boolean])
    multiply_node = myobj.add_method(idx, "multiply", multiply, [ua.VariantType.Int64, ua.VariantType.Int64], [ua.VariantType.Int64])

    # creating an event object
    # The event object automatically will have members for all events properties
    myevent = server.get_event_object(ObjectIds.BaseEventType)
    myevent.Message.Text = "This is my event"
    myevent.Severity = 300
    
    # starting!
    server.start()
    print("Available loggers are: ", logging.Logger.manager.loggerDict.keys())
    try:
        handler = SubHandler()
        #enable following if you want to subscribe to nodes on server side
        sub = server.create_subscription(500, handler)
        handle = sub.subscribe_data_change(myvar)
        # trigger event, all subscribed clients wil receive it
        myevent.trigger()

        embed()
    finally:
        server.stop()

