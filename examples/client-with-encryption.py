import sys
sys.path.insert(0, "..")
import logging

from IPython import embed

from opcua import Client


if __name__ == "__main__":
    logging.basicConfig(level=logging.WARNING)
    client = Client("opc.tcp://localhost:4840/freeopcua/server/")
    #client = Client("opc.tcp://localhost:53530/OPCUA/SimulationServer/")
    client.set_security_string("Basic256Sha256,SignAndEncrypt,certificate-example.der,private-key-example.pem")
    client.application_uri = "urn:example.org:FreeOpcUa:python-opcua"
    client.secure_channel_timeout = 10000
    client.session_timeout = 10000
    try:
        client.connect()
        root = client.get_root_node()
        objects = client.get_objects_node()
        print("childs og objects are: ", objects.get_children())

        embed()
    finally:
        client.disconnect()
