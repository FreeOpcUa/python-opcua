import logging

from opcua import Client


if __name__ == "__main__": 
    from IPython import embed
    logging.basicConfig(level=logging.DEBUG)
    client = Client("opc.tcp://localhost:4841/freeopcua/server/")
    try:
        client.connect()
        client.send_hello()
        client.open_secure_channel()
        endpoints = client.get_endpoints()
        client.close_secure_channel()
        client.connect()
        client.send_hello()
        client.open_secure_channel()
        client.create_session()
        client.activate_session()
        root = client.get_root_node()
        print(root)
        childs = root.get_children()
        print(childs)
        bname = root.get_name()
        print(bname)
        embed()
        client.close_session()
    finally:
        client.disconnect()
