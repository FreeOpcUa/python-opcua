import os
from common import KeyValuePair, ErrorKeyValue
from opcua import uamethod, Server
try:
    from IPython import embed
except ImportError:
    import code

    def embed():
        vars = globals()
        vars.update(locals())
        shell = code.InteractiveConsole(vars)
        shell.interact()


@uamethod
def say_complex_hello(parent, complex_variable, complex_variable_list):
    # The uamethod decorator will take care of converting the data for us. We only work with python objects inside it
    # For it to work, you need to register your DataType like in common.py
    print("say_complex_hello called: {}, {}".format(complex_variable, complex_variable_list))
    complex_error = ErrorKeyValue("0", "foo", [KeyValuePair("key", "value"), KeyValuePair("hello", "world")])
    complex_error_list = ErrorKeyValue("1", "bar", [KeyValuePair("key", "value")])

    return complex_error, complex_error_list


class HellowerServer(object):
    def __init__(self, endpoint, name, model_filepath):
        self.server = Server()

        self.server.import_xml(model_filepath)

        # Those need to be done after importing the xml file or it will be overwritten
        self.server.set_endpoint(endpoint)
        self.server.set_server_name(name)

        objects = self.server.get_objects_node()
        hellower = objects.get_child("0:Hellower")

        say_hello_node = hellower.get_child("0:SayComplexHello")

        self.server.link_method(say_hello_node, say_complex_hello)

    def __enter__(self):
        self.server.start()
        return self.server

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.server.stop()


if __name__ == '__main__':
    script_dir = os.path.dirname(__file__)
    with HellowerServer(
            "opc.tcp://0.0.0.0:40840/freeopcua/server/",
            "FreeOpcUa Example Server",
            os.path.join(script_dir, "nodeset.xml")) as server:
        embed()
