import logging

from opcua import Client


if __name__ == "__main__": 
    from IPython import embed
    logging.basicConfig(level=logging.DEBUG)
    client = Client("opc.tcp://localhost:4841/freeopcua/server/")
    try:
        client.connect()
        client.open_secure_channel()
        embed()
    finally:
        client.disconnect()
