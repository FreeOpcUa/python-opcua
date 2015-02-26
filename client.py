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
    params.ClientProtocolVersion = 255
    params.RequestType = ua.SecurityTokenRequestType.Issue
    params.SecurityMode = ua.MessageSecurityMode.None_
    params.RequestedLifetime = 300000
    params.ClientNonce = ua.ByteString('\x00')
    client.open_secure_channel(params)
    embed()
    #binclient.stop()
