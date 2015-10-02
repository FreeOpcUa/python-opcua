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


from opcua import ua, uamethod, Server, Event, ObjectIds, node


class SubHandler(object):

    """
    Subscription Handler. To receive events from server for a subscription
    """

    def data_change(self, handle, node, val, attr):
        print("Python: New data change event", handle, node, val, attr)

    def event(self, handle, event):
        print("Python: New event", handle, event)


# method to be exposed through server

def func(parent, variant):
    ret = False
    if variant.Value % 2 == 0:
        ret = True
    return [ua.Variant(ret, ua.VariantType.Boolean)]


# method to be exposed through server
# uses a decorator to automatically convert to and from variants

@uamethod
def multiply(parent, x, y):
    print("multiply method call with parameters: ", x, y)
    return x * y


if __name__ == "__main__":
    # optional: setup logging
    logging.basicConfig(level=logging.WARN)
    #logger = logging.getLogger("opcua.address_space")
    # logger.setLevel(logging.DEBUG)
    #logger = logging.getLogger("opcua.internal_server")
    # logger.setLevel(logging.DEBUG)
    #logger = logging.getLogger("opcua.binary_server_asyncio")
    # logger.setLevel(logging.DEBUG)
    #logger = logging.getLogger("opcua.uaprocessor")
    # logger.setLevel(logging.DEBUG)
    #logger = logging.getLogger("opcua.subscription_service")
    # logger.setLevel(logging.DEBUG)

    # now setup our server
    server = Server()
    #server.set_endpoint("opc.tcp://localhost:4841/freeopcua/server/")
    server.set_endpoint("opc.tcp://0.0.0.0:4841/freeopcua/server/")
    server.set_server_name("FreeOpcUa Example Server")

    # setup our own namespace
    uri = "http://examples.freeopcua.github.io"
    idx = server.register_namespace(uri)

    # get Objects node, this is where we should put our custom stuff
    objects = server.get_objects_node()

    # populating our address space
    myfolder = objects.add_folder(idx, "myEmptyFolder")
    myobj = objects.add_object(idx, "NewObject")
    myvar = myobj.add_variable(idx, "MyVariable", 6.7)
    myvar.set_writable()    # Set MyVariable to be writable by clients
    myarrayvar = myobj.add_variable(idx, "myarrayvar", [6.7, 7.9])
    myarrayvar = myobj.add_variable(idx, "myStronglytTypedVariable", ua.Variant([], ua.VariantType.UInt32))
    myprop = myobj.add_property(idx, "myproperty", "I am a property")
    mymethod = myobj.add_method(idx, "mymethod", func, [ua.VariantType.Int64], [ua.VariantType.Boolean])

    inargx = ua.Argument()
    inargx.Name = "x"
    inargx.DataType = node._guess_uatype(ua.Variant(None, ua.VariantType.Int64))
    inargx.ValueRank = -1
    inargx.ArrayDimensions = []
    inargx.Description = ua.LocalizedText("First number x")
    inargy = ua.Argument()
    inargy.Name = "y"
    inargy.DataType = node._guess_uatype(ua.Variant(None, ua.VariantType.Int64))
    inargy.ValueRank = -1
    inargy.ArrayDimensions = []
    inargy.Description = ua.LocalizedText("Second number y")
    outarg = ua.Argument()
    outarg.Name = "Result"
    outarg.DataType = node._guess_uatype(ua.Variant(None, ua.VariantType.Int64))
    outarg.ValueRank = -1
    outarg.ArrayDimensions = []
    outarg.Description = ua.LocalizedText("Multiplication result")

    multiply_node = myobj.add_method(idx, "multiply", multiply, [inargx, inargy], [outarg])

    # import some nodes from xml
    server.import_xml("custom_nodes.xml")

    # creating an event object
    # The event object automatically will have members for all events properties
    myevent = server.get_event_object(ObjectIds.BaseEventType)
    myevent.Message.Text = "This is my event"
    myevent.Severity = 300

    # starting!
    server.start()
    print("Available loggers are: ", logging.Logger.manager.loggerDict.keys())
    try:
        # enable following if you want to subscribe to nodes on server side
        #handler = SubHandler()
        #sub = server.create_subscription(500, handler)
        #handle = sub.subscribe_data_change(myvar)
        # trigger event, all subscribed clients wil receive it
        myevent.trigger()

        embed()
    finally:
        server.stop()
