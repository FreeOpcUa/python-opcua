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
    print("say_complex_hello called: {}, {}".format(complex_variable, complex_variable_list))
    complex_error = ErrorKeyValue("0", "foo", [KeyValuePair("key", "value"), KeyValuePair("hello", "world")])
    complex_error_list = ErrorKeyValue("1", "bar", [KeyValuePair("key", "value")])

    return complex_error, complex_error_list


class HellowerServer(object):
    def __init__(self, endpoint, name, model_filepath):
        self.server = Server()

        self.server.import_xml(model_filepath)

        self.server.set_endpoint(endpoint)
        self.server.set_server_name(name)

        objects = self.server.get_objects_node()
        serial_manager = objects.get_child("0:Hellower")

        for child in serial_manager.get_children():
            print(dir(child))
            print("Got a child: {}".format(child.get_browse_name()))
        get_serial_node = serial_manager.get_child("0:SayComplexHello")

        self.server.link_method(get_serial_node, say_complex_hello)

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
