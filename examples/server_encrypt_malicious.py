import sys
sys.path.insert(0, "..")
from datetime import datetime
from opcua import ua, uamethod, Server

import logging
import ipdb
logging.basicConfig(level=logging.DEBUG)
import time

try:
    from IPython import embed
except ImportError:
    import code

    def embed():
        vars = globals()
        vars.update(locals())
        shell = code.InteractiveConsole(vars)
        shell.interact()

# server definition
server = Server()

server.set_endpoint("opc.tcp://localhost:4841/freeopcua/server/")
server.set_server_name("Test Turbo Server")

server.set_security_policy([ua.SecurityPolicyType.Basic256_SignAndEncrypt])
'''
server.set_security_policy([
                ua.SecurityPolicyType.NoSecurity,
                ua.SecurityPolicyType.Basic128Rsa15_SignAndEncrypt,
                ua.SecurityPolicyType.Basic128Rsa15_Sign,
                ua.SecurityPolicyType.Basic256_SignAndEncrypt,
                ua.SecurityPolicyType.Basic256_Sign])
'''
server.set_security_IDs(["Basic256"])

server.load_certificate("certificate-example.der")
server.load_private_key("private-key-example.pem")
#server.load_private_key("key.pem")

uri = "iab_namespace"
idx = server.register_namespace(uri)

##########################################################################
server.import_xml("XMLSchemas/xml_opc_schema_test1.xml")
##########################################################################
# modeler can also set variables to writable
#v1 = server.get_node("i=20004") 
#v1.set_writable()

v1 = server.get_node("ns=2;i=12") 
v2 = server.get_node("ns=2;i=15") 

if __name__ == "__main__":

    server.start()

    # TODO why can't set variables to writable before running the server????
    server.historize_node_data_change(v1)
    server.historize_node_data_change(v2)

    
    # in case we decide to use good old loop instead of interativeshell
    try:
        while True:
            time.sleep(10)
            v1.set_value(1111111)
    finally:
        server.stop()



