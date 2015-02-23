import logging

from opcua import uaprotocol as ua
from opcua import binary_client 



if __name__ == "__main__": 
    from IPython import embed
    logging.basicConfig(level=logging.DEBUG)
    client = binary_client.BinaryClient()
    client.connect()
    #client.start()
    ack = client.send_hello("opc.tcp://localhost:4841/freeopcua/server/")
    params = ua.OpenSecureChannelParameters()
    client.open_secure_channel(params)
    embed()
    #binclient.stop()
