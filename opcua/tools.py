import logging
import sys
import argparse
from datetime import datetime
from enum import Enum
import math
import time

try:
    from IPython import embed
except ImportError:
    import code

    def embed():
        code.interact(local=dict(globals(), **locals())) 

from opcua import ua
from opcua import Client
from opcua import Server
from opcua import Node
from opcua import uamethod


def add_minimum_args(parser):
    parser.add_argument("-u",
                        "--url",
                        help="URL of OPC UA server (for example: opc.tcp://example.org:4840)",
                        default='opc.tcp://localhost:4841',
                        metavar="URL")
    parser.add_argument("-v",
                        "--verbose",
                        dest="loglevel",
                        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
                        default='WARNING',
                        help="Set log level")
    parser.add_argument("--timeout",
                        dest="timeout",
                        type=int,
                        default=1,
                        help="Set socket timeout (NOT the diverse UA timeouts)")


def add_common_args(parser):
    add_minimum_args(parser)
    parser.add_argument("-n",
                        "--nodeid",
                        help="Fully-qualified node ID (for example: i=85). Default: root node",
                        default='i=84',
                        metavar="NODE")
    parser.add_argument("-p",
                        "--path",
                        help="Comma separated browse path to the node starting at NODE (for example: 3:Mybject,3:MyVariable)",
                        default='',
                        metavar="BROWSEPATH")
    parser.add_argument("-i",
                        "--namespace",
                        help="Default namespace",
                        type=int,
                        default=0,
                        metavar="NAMESPACE")


def parse_args(parser, requirenodeid=False):
    args = parser.parse_args()
    logging.basicConfig(format="%(levelname)s: %(message)s", level=getattr(logging, args.loglevel))
    if args.url and '://' not in args.url:
        logging.info("Adding default scheme %s to URL %s", ua.OPC_TCP_SCHEME, args.url)
        args.url = ua.OPC_TCP_SCHEME + '://' + args.url
    # check that a nodeid has been given explicitly, a bit hackish...
    if requirenodeid and args.nodeid == "i=84" and args.path == "":
        parser.print_usage()
        print("{}: error: A NodeId or BrowsePath is required".format(parser.prog))
        sys.exit(1)
    return args


def get_node(client, args):
    node = client.get_node(args.nodeid)
    if args.path:
        node = node.get_child(args.path.split(","))
    return node


def uaread():
    parser = argparse.ArgumentParser(description="Read attribute of a node, per default reads value of a node")
    add_common_args(parser)
    parser.add_argument("-a",
                        "--attribute",
                        dest="attribute",
                        type=int,
                        default=ua.AttributeIds.Value,
                        help="Set attribute to read")
    parser.add_argument("-t",
                        "--datatype",
                        dest="datatype",
                        default="python",
                        choices=['python', 'variant', 'datavalue'],
                        help="Data type to return")

    args = parse_args(parser, requirenodeid=True)

    client = Client(args.url, timeout=args.timeout)
    client.connect()
    try:
        node = get_node(client, args)
        attr = node.get_attribute(args.attribute)
        if args.datatype == "python":
            print(attr.Value.Value)
        elif args.datatype == "variant":
            print(attr.Value)
        else:
            print(attr)
    finally:
        client.disconnect()
    sys.exit(0)
    print(args)


def _args_to_array(val, array):
    if array == "guess":
        if "," in val:
            array = "true"
    if array == "true":
        val = val.split(",")
    return val


def _arg_to_bool(val):
    if val in ("true", "True"):
        return True
    else:
        return False


def _arg_to_variant(val, array, ptype, varianttype=None):
    val = _args_to_array(val, array)
    if isinstance(val, list):
        val = [ptype(i) for i in val]
    else:
        val = ptype(val)
    if varianttype:
        return ua.Variant(val, varianttype)
    else:
        return ua.Variant(val)


def _val_to_variant(val, args):
    array = args.array
    if args.datatype == "guess":
        if val in ("true", "True", "false", "False"):
            return _arg_to_variant(val, array, _arg_to_bool)
        # FIXME: guess bool value
        try:
            return _arg_to_variant(val, array, int)
        except ValueError:
            try:
                return _arg_to_variant(val, array, float)
            except ValueError:
                return _arg_to_variant(val, array, str)
    elif args.datatype == "bool":
        if val in ("1", "True", "true"):
            return ua.Variant(True, ua.VariantType.Boolean)
        else:
            return ua.Variant(False, ua.VariantType.Boolean)
    elif args.datatype == "sbyte":
        return _arg_to_variant(val, array, int, ua.VariantType.SByte)
    elif args.datatype == "byte":
        return _arg_to_variant(val, array, int, ua.VariantType.Byte)
    #elif args.datatype == "uint8":
        #return _arg_to_variant(val, array, int, ua.VariantType.Byte)
    elif args.datatype == "uint16":
        return _arg_to_variant(val, array, int, ua.VariantType.UInt16)
    elif args.datatype == "uint32":
        return _arg_to_variant(val, array, int, ua.VariantType.UInt32)
    elif args.datatype == "uint64":
        return _arg_to_variant(val, array, int, ua.VariantType.UInt64)
    #elif args.datatype == "int8":
        #return ua.Variant(int(val), ua.VariantType.Int8)
    elif args.datatype == "int16":
        return _arg_to_variant(val, array, int, ua.VariantType.Int16)
    elif args.datatype == "int32":
        return _arg_to_variant(val, array, int, ua.VariantType.Int32)
    elif args.datatype == "int64":
        return _arg_to_variant(val, array, int, ua.VariantType.Int64)
    elif args.datatype == "float":
        return _arg_to_variant(val, array, float, ua.VariantType.Float)
    elif args.datatype == "double":
        return _arg_to_variant(val, array, float, ua.VariantType.Double)
    elif args.datatype == "string":
        return _arg_to_variant(val, array, str, ua.VariantType.String)
    elif args.datatype == "datetime":
        raise NotImplementedError
    elif args.datatype == "Guid":
        return _arg_to_variant(val, array, bytes, ua.VariantType.Guid)
    elif args.datatype == "ByteString":
        return _arg_to_variant(val, array, bytes, ua.VariantType.ByteString)
    elif args.datatype == "xml":
        return _arg_to_variant(val, array, str, ua.VariantType.XmlElement)
    elif args.datatype == "nodeid":
        return _arg_to_variant(val, array, ua.NodeId.from_string, ua.VariantType.NodeId)
    elif args.datatype == "expandednodeid":
        return _arg_to_variant(val, array, ua.ExpandedNodeId.from_string, ua.VariantType.ExpandedNodeId)
    elif args.datatype == "statuscode":
        return _arg_to_variant(val, array, int, ua.VariantType.StatusCode)
    elif args.datatype in ("qualifiedname", "browsename"):
        return _arg_to_variant(val, array, ua.QualifiedName.from_string, ua.VariantType.QualifiedName)
    elif args.datatype == "LocalizedText":
        return _arg_to_variant(val, array, ua.LocalizedText, ua.VariantTypeLocalizedText)


def uawrite():
    parser = argparse.ArgumentParser(description="Write attribute of a node, per default write value of node")
    add_common_args(parser)
    parser.add_argument("-a",
                        "--attribute",
                        dest="attribute",
                        type=int,
                        default=ua.AttributeIds.Value,
                        help="Set attribute to read")
    parser.add_argument("-l",
                        "--list",
                        "--array",
                        dest="array",
                        default="guess",
                        choices=["guess", "true", "false"],
                        help="Value is an array")
    parser.add_argument("-t",
                        "--datatype",
                        dest="datatype",
                        default="guess",
                        choices=["guess", 'byte', 'sbyte', 'nodeid', 'expandednodeid', 'qualifiedname', 'browsename', 'string', 'float', 'double', 'int16', 'int32', "int64", 'uint16', 'uint32', 'uint64', "bool", "string", 'datetime', 'bytestring', 'xmlelement', 'statuscode', 'localizedtext'],  
                        help="Data type to return")
    parser.add_argument("value",
                        help="Value to be written",
                        metavar="VALUE")
    args = parse_args(parser, requirenodeid=True)

    client = Client(args.url, timeout=args.timeout)
    client.connect()
    try:
        node = get_node(client, args)
        val = _val_to_variant(args.value, args)
        node.set_attribute(args.attribute, ua.DataValue(val))
    finally:
        client.disconnect()
    sys.exit(0)
    print(args)


def uals():
    parser = argparse.ArgumentParser(description="Browse OPC-UA node and print result")
    add_common_args(parser)
    parser.add_argument("-l",
                        dest="long_format",
                        const=3,
                        nargs="?",
                        type=int,
                        help="use a long listing format")
    parser.add_argument("-d",
                        "--depth",
                        default=1,
                        type=int,
                        help="Browse depth")

    args = parse_args(parser)
    if args.long_format is None:
        args.long_format = 1

    client = Client(args.url, timeout=args.timeout)
    client.connect()
    try:
        node = get_node(client, args)
        print("Browsing node {} at {}\n".format(node, args.url))
        if args.long_format == 0:
            _lsprint_0(node, args.depth - 1)
        elif args.long_format == 1:
            _lsprint_1(node, args.depth - 1)
        else:
            _lsprint_long(node, args.depth - 1)
    finally:
        client.disconnect()
    sys.exit(0)
    print(args)


def _lsprint_0(node, depth, indent=""):
    if not indent:
        print("{:30} {:25}".format("DisplayName", "NodeId"))
        print("")
    for desc in node.get_children_descriptions():
        print("{}{:30} {:25}".format(indent, desc.DisplayName.to_string(), desc.NodeId.to_string()))
        if depth:
            _lsprint_0(Node(node.server, desc.NodeId), depth - 1, indent + "  ")


def _lsprint_1(node, depth, indent=""):
    if not indent:
        print("{:30} {:25} {:25} {:25}".format("DisplayName", "NodeId", "BrowseName", "Value"))
        print("")

    for desc in node.get_children_descriptions():
        if desc.NodeClass == ua.NodeClass.Variable:
            val = Node(node.server, desc.NodeId).get_value()
            print("{}{:30} {!s:25} {!s:25}, {!s:3}".format(indent, desc.DisplayName.to_string(), desc.NodeId.to_string(), desc.BrowseName.to_string(), val))
        else:
            print("{}{:30} {!s:25} {!s:25}".format(indent, desc.DisplayName.to_string(), desc.NodeId.to_string(), desc.BrowseName.to_string()))
        if depth:
            _lsprint_1(Node(node.server, desc.NodeId), depth - 1, indent + "  ")


def _lsprint_long(pnode, depth, indent=""):
    if not indent:
        print("{:30} {:25} {:25} {:10} {:30} {:25}".format("DisplayName", "NodeId", "BrowseName", "DataType", "Timestamp", "Value"))
        print("")
    for node in pnode.get_children():
        attrs = node.get_attributes([ua.AttributeIds.DisplayName, 
                                     ua.AttributeIds.BrowseName,
                                     ua.AttributeIds.NodeClass,
                                     ua.AttributeIds.WriteMask,
                                     ua.AttributeIds.UserWriteMask,
                                     ua.AttributeIds.DataType,
                                     ua.AttributeIds.Value])
        name, bname, nclass, mask, umask, dtype, val = [attr.Value.Value for attr in attrs]
        update = attrs[-1].ServerTimestamp
        if nclass == ua.NodeClass.Variable:
            print("{}{:30} {:25} {:25} {:10} {!s:30} {!s:25}".format(indent, name.to_string(), node.nodeid.to_string(), bname.to_string(), dtype.to_string(), update, val))
        else:
            print("{}{:30} {:25} {:25}".format(indent, name.to_string(), bname.to_string(), node.nodeid.to_string()))
        if depth:
            _lsprint_long(node, depth - 1, indent + "  ")


class SubHandler(object):

    def data_change(self, handle, node, val, attr):
        print("New data change event", handle, node, val, attr)

    def event(self, handle, event):
        print("New event", handle, event)


def uasubscribe():
    parser = argparse.ArgumentParser(description="Subscribe to a node and print results")
    add_common_args(parser)
    parser.add_argument("-t",
                        "--eventtype",
                        dest="eventtype",
                        default="datachange",
                        choices=['datachange', 'event'],
                        help="Event type to subscribe to")

    args = parse_args(parser, requirenodeid=True)

    client = Client(args.url, timeout=args.timeout)
    client.connect()
    try:
        node = get_node(client, args)
        handler = SubHandler()
        sub = client.create_subscription(500, handler)
        if args.eventtype == "datachange":
            sub.subscribe_data_change(node)
        else:
            sub.subscribe_events(node)
        embed()
    finally:
        client.disconnect()
    sys.exit(0)
    print(args)


# converts numeric value to its enum name.
def enum_to_string(klass, value):
    if isinstance(value, Enum):
        return value.name
    # if value is not a subtype of Enum, try to find a constant
    # with this value in this class
    for k, v in vars(klass).items():
        if not k.startswith('__') and v == value:
            return k
    return 'Unknown {} ({})'.format(klass.__name__, value)


def application_to_strings(app):
    result = []
    result.append(('Application URI', app.ApplicationUri))
    optionals = [
        ('Product URI', app.ProductUri),
        ('Application Name', app.ApplicationName.to_string()),
        ('Application Type', enum_to_string(ua.ApplicationType, app.ApplicationType)),
        ('Gateway Server URI', app.GatewayServerUri),
        ('Discovery Profile URI', app.DiscoveryProfileUri),
    ]
    for (n, v) in optionals:
        if v:
            result.append((n, v))
    for url in app.DiscoveryUrls:
        result.append(('Discovery URL', url))
    return result  # ['{}: {}'.format(n, v) for (n, v) in result]


def endpoint_to_strings(ep):
    result = [('Endpoint URL', ep.EndpointUrl)]
    result += application_to_strings(ep.Server)
    result += [
        ('Server Certificate', len(ep.ServerCertificate)),
        ('Security Mode', enum_to_string(ua.MessageSecurityMode, ep.SecurityMode)),
        ('Security Policy URI', ep.SecurityPolicyUri)]
    for tok in ep.UserIdentityTokens:
        result += [
            ('User policy', tok.PolicyId),
            ('  Token type', enum_to_string(ua.UserTokenType, tok.TokenType))]
        if tok.IssuedTokenType or tok.IssuerEndpointUrl:
            result += [
                ('  Issued Token type', tok.IssuedTokenType),
                ('  Issuer Endpoint URL', tok.IssuerEndpointUrl)]
        if tok.SecurityPolicyUri:
            result.append(('  Security Policy URI', tok.SecurityPolicyUri))
    result += [
        ('Transport Profile URI', ep.TransportProfileUri),
        ('Security Level', ep.SecurityLevel)]
    return result


def uaclient():
    parser = argparse.ArgumentParser(description="Connect to server and start python shell. root and objects nodes are available. Node specificed in command line is available as mynode variable")
    add_common_args(parser)
    parser.add_argument("-c",
                        "--certificate",
                        help="set client certificate")
    parser.add_argument("-k",
                        "--private_key",
                        help="set client private key")
    args = parse_args(parser)

    client = Client(args.url, timeout=args.timeout)
    client.connect()
    if args.certificate:
        client.load_certificate(args.certificate)
    if args.private_key:
        client.load_certificate(args.private_key)
    try:
        root = client.get_root_node()
        objects = client.get_objects_node()
        mynode = get_node(client, args)
        embed()
    finally:
        client.disconnect()
    sys.exit(0)


def uaserver():
    parser = argparse.ArgumentParser(description="Run an example OPC-UA server. By importing xml definition and using uawrite command line, it is even possible to expose real data using this server")
    # we setup a server, this is a bit different from other tool so we do not reuse common arguments
    parser.add_argument("-u",
                        "--url",
                        help="URL of OPC UA server, default is opc.tcp://0.0.0.0:4841",
                        default='opc.tcp://0.0.0.0:4841',
                        metavar="URL")
    parser.add_argument("-v",
                        "--verbose",
                        dest="loglevel",
                        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
                        default='WARNING',
                        help="Set log level")
    parser.add_argument("-x",
                        "--xml",
                        metavar="XML_FILE",
                        help="Populate address space with nodes defined in XML")
    parser.add_argument("-p",
                        "--populate",
                        action="store_false",
                        help="Populate address space with some sample nodes")
    parser.add_argument("-c",
                        "--disable-clock",
                        action="store_true",
                        help="Disable clock, to avoid seeing many write if debugging an application")
    parser.add_argument("-s",
                        "--shell",
                        action="store_true",
                        help="Start python shell instead of randomly changing node values")
    args = parser.parse_args()
    logging.basicConfig(format="%(levelname)s: %(message)s", level=getattr(logging, args.loglevel))

    server = Server()
    server.set_endpoint(args.url)
    server.disable_clock(args.disable_clock)
    server.set_server_name("FreeOpcUa Example Server")
    if args.xml:
        server.import_xml(args.xml)
    if args.populate:
        @uamethod
        def multiply(parent, x, y):
            print("multiply method call with parameters: ", x, y)
            return x * y

        uri = "http://examples.freeopcua.github.io"
        idx = server.register_namespace(uri)
        objects = server.get_objects_node()
        myobj = objects.add_object(idx, "MyObject")
        mywritablevar = myobj.add_variable(idx, "MyWritableVariable", 6.7)
        mywritablevar.set_writable()    # Set MyVariable to be writable by clients
        myvar = myobj.add_variable(idx, "MyVariable", 6.7)
        myarrayvar = myobj.add_variable(idx, "MyVarArray", [6.7, 7.9])
        myprop = myobj.add_property(idx, "MyProperty", "I am a property")
        mymethod = myobj.add_method(idx, "MyMethod", multiply, [ua.VariantType.Double, ua.VariantType.Int64], [ua.VariantType.Double])

    server.start()
    try:
        if args.shell:
            embed()
        else:
            count = 0
            while True:
                time.sleep(1)
                myvar.set_value(math.sin(count / 10))
                myarrayvar.set_value([math.sin(count / 10), math.sin(count / 100)])
                count += 1
    finally:
        server.stop()
    sys.exit(0)


def uadiscover():
    parser = argparse.ArgumentParser(description="Performs OPC UA discovery and prints information on servers and endpoints.")
    add_minimum_args(parser)
    parser.add_argument("-n",
                        "--network",
                        action="store_true",
                        help="Also send a FindServersOnNetwork request to server")
    #parser.add_argument("-s",
                        #"--servers",
                        #action="store_false",
                        #help="send a FindServers request to server")
    #parser.add_argument("-e",
                        #"--endpoints",
                        #action="store_false",
                        #help="send a GetEndpoints request to server")
    args = parse_args(parser)
    
    client = Client(args.url, timeout=args.timeout)

    if args.network:
        print("Performing discovery at {}\n".format(args.url))
        for i, server in enumerate(client.find_all_servers_on_network(), start=1):
            print('Server {}:'.format(i))
            #for (n, v) in application_to_strings(server):
                #print('  {}: {}'.format(n, v))
            print('')

    print("Performing discovery at {}\n".format(args.url))
    for i, server in enumerate(client.find_all_servers(), start=1):
        print('Server {}:'.format(i))
        for (n, v) in application_to_strings(server):
            print('  {}: {}'.format(n, v))
        print('')

    for i, ep in enumerate(client.get_server_endpoints(), start=1):
        print('Endpoint {}:'.format(i))
        for (n, v) in endpoint_to_strings(ep):
            print('  {}: {}'.format(n, v))
        print('')

    sys.exit(0)


def print_history(o):
    if isinstance(o, ua.HistoryData):
        print("{:30} {:10} {}".format('Source timestamp', 'Status', 'Value'))
        for d in o.DataValues:
            print("{:30} {:10} {}".format(str(d.SourceTimestamp), d.StatusCode.name, d.Value))


def str_to_datetime(s):
    if not s:
        return datetime.utcnow()
    # try different datetime formats
    for fmt in ["%Y-%m-%d", "%Y-%m-%d %H:%M", "%Y-%m-%d %H:%M:%S"]:
        try:
            return datetime.strptime(s, fmt)
        except ValueError:
            pass


def uahistoryread():
    parser = argparse.ArgumentParser(description="Read history of a node")
    add_common_args(parser)
    parser.add_argument("--starttime",
                        default="",
                        help="Start time, formatted as YYYY-MM-DD [HH:MM[:SS]]. Default: current time")
    parser.add_argument("--endtime",
                        default="",
                        help="End time, formatted as YYYY-MM-DD [HH:MM[:SS]]. Default: current time")

    args = parse_args(parser, requirenodeid=True)

    client = Client(args.url, timeout=args.timeout)
    client.connect()
    try:
        node = get_node(client, args)
        starttime = str_to_datetime(args.starttime)
        endtime = str_to_datetime(args.endtime)
        print("Reading raw history of node {} at {}; start at {}, end at {}\n".format(node, args.url, starttime, endtime))
        print_history(node.read_raw_history(starttime, endtime))
    finally:
        client.disconnect()
    sys.exit(0)
