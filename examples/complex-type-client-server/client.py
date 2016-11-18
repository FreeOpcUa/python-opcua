from opcua import Client
from common import KeyValuePair


class HelloClient(object):
    def __init__(self, endpoint):
        self.client = Client(endpoint)

    def __enter__(self):
        self.client.connect()
        return self.client

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.disconnect()


if __name__ == '__main__':
    with HelloClient("opc.tcp://localhost:40840/freeopcua/server/") as client:
        root = client.get_root_node()
        for obj in root.get_children():
            print(obj.get_browse_name())

        objects = root.get_child("0:Objects")
        for obj in objects.get_children():
            print(obj.get_browse_name())
        serial_manager = objects.get_child("0:Hellower")
        complex_error, complex_error_list = serial_manager.call_method(
                "0:SayComplexHello",
                KeyValuePair("foo", "bar"),
                [KeyValuePair("toto", "tata"), KeyValuePair("Hello", "World")],
            )

        print(complex_error, complex_error_list)
