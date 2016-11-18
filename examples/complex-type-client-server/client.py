from opcua import Client
from common import KeyValuePair


class HelloClient(object):
    def __init__(self, endpoint):
        self._client = Client(endpoint)

        # We cannot set them properly as we are still not connected to the server
        self._root = None
        self._objects = None
        self._hellower = None

    def __enter__(self):
        # __enter__ and __exit__ are called when getting the object with the with keyword. See context manager
        # documentation for more information
        self._client.connect()

        # As soon as we are connected to the server, we set the variables
        self._root = self._client.get_root_node()
        self._objects = self._client.get_objects_node()
        self._hellower = self._objects.get_child("0:Hellower")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._client.disconnect()

    def say_hello(self, complex_variable, complex_variable_list):
        """Adapt the method call so it is used like a normal python method"""
        return self._hellower.call_method(
            "0:SayComplexHello",
            complex_variable,
            complex_variable_list
        )


if __name__ == '__main__':
    with HelloClient("opc.tcp://localhost:40840/freeopcua/server/") as hello_client:
        complex_error, complex_error_list = hello_client.say_hello(
                KeyValuePair("foo", "bar"),
                [KeyValuePair("toto", "tata"), KeyValuePair("Hello", "World")],
            )

        print(complex_error, complex_error_list)
