import sys
sys.path.insert(0, "..")
import time
import random

from opcua import Server
from opcua.common.sqlite3_backend import SQLite3Backend
from opcua.server.address_space_sqlite import StandardAddressSpaceSQLite, AddressSpaceSQLite

ITEMS = ('Pump', 'Motor', 'Fan', 'Gearbox', 'Filter', 'Building', 'Ventilation')

if __name__ == "__main__":

    print('\nStart and stop this server multiple times and\n'
          'verify that address space is persisted in SQL.\n'
          'Values written from any opc-ua client into the\n'
          'server are also stored.\n')

    with SQLite3Backend(sqlFile='my_address_space.py', readonly=False) as backend, \
         StandardAddressSpaceSQLite() as stdAspace, \
         AddressSpaceSQLite(backend=backend, cache=stdAspace) as myAspace:

        # setup our server
        server = Server(aspace=myAspace)
        server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")
    
        # setup our own namespace, not really necessary but should as spec
        uri = "http://examples.freeopcua.github.io"
        idx = server.register_namespace(uri)
    
        # get Objects node, this is where we should put our nodes
        objects = server.get_objects_node()
    
        # populating our address space
        myobj = objects.add_object(idx, "{:s}-{:d}".format(random.choice(ITEMS), random.randint(1,100)))
        myvar = myobj.add_variable(idx, "MyVariable", 42)
        myvar.set_writable()    # Set MyVariable to be writable by clients
    
        # starting!
        server.start()
        
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            pass
        finally:
            #close connection, remove subcsriptions, etc
            server.stop()
