import sys
sys.path.insert(0, "..")
import time
from collections import OrderedDict

from opcua import ua, Server, instantiate
from opcua.common.xmlexporter import XmlExporter


if __name__ == "__main__":

    # setup our server
    server = Server()
    server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")

    # setup our own namespace, not really necessary but should as spec
    uri = "http://examples.freeopcua.github.io"
    idx = server.register_namespace(uri)

    # get Objects node, this is where we should put our nodes
    objects = server.get_objects_node()

    # populating our address space
    myobj = objects.add_object(idx, "MyObject")
    myvar = myobj.add_variable(idx, "MyVariable", 6.7)
    myvar.set_writable()    # Set MyVariable to be writable by clients

    dev = server.nodes.base_object_type.add_object_type(0, "MyDevice")
    dev.add_variable(0, "sensor1", 1.0)

    mydevice = instantiate(server.nodes.objects, dev, bname="2:Device0001")

    node_list = [dev, mydevice, myobj, myvar]

    # starting!
    server.start()

    node_set_attributes = OrderedDict()
    node_set_attributes['xmlns:xsi'] = '"http://www.w3.org/2001/XMLSchema-instance"'
    node_set_attributes['xmlns:uax'] = 'http://opcfoundation.org/UA/2008/02/Types.xsd'
    node_set_attributes['xmlns:s1'] = 'http://yourorganisation.org/dataobject/Types.xsd'
    node_set_attributes['xmlns:xsd'] = 'http://www.w3.org/2001/XMLSchema'
    node_set_attributes['xmlns'] = 'http://opcfoundation.org/UA/2011/03/UANodeSet.xsd'

    exporter = XmlExporter(server, node_set_attributes)
    exporter.build_etree(node_list)
    exporter.write_xml('ua-export.xml')

    server.stop()
