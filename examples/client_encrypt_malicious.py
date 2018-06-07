from opcua import Client
from opcua import ua
import time
import random
import logging
logging.basicConfig(level=logging.DEBUG)

if __name__ == '__main__':
    client = Client("opc.tcp://localhost:4841/freeopcua/server/")

    ## one can set different sets of key/cert for testing

    #client.load_private_key('key.pem')
    #client.load_client_certificate('cert.pem')
    client.load_private_key('private-key-example.pem')
    client.load_client_certificate('certificate-example.der')

    client.set_security_string("Basic256,SignAndEncrypt,cert.pem,key.pem")
    #client.set_security_string("Basic256,SignAndEncrypt,certificate-example.der,private-key-example.pem")

    ## this doesn't work because this cert.key pair is used for encryption of data
    #client.set_security_string("Basic256,SignAndEncrypt,cert.pem,private-key-example.pem")

    time.sleep(5)

    client.connect()
    print("connectedddd")

    var_temp = client.get_node("ns=2;i=12")
    var_vibration = client.get_node("ns=2;i=15")

    while True:
        var_temp.get_value()
        time.sleep(10)
    

