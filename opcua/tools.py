import logging
import sys
import argparse
from datetime import datetime, timedelta
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
                        default='opc.tcp://localhost:4840',
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


def add_common_args(parser, default_node='i=84', require_node=False):
    add_minimum_args(parser)
    parser.add_argument("-n",
                        "--nodeid",
                        help="Fully-qualified node ID (for example: i=85). Default: root node",
                        default=default_node,
                        required=require_node,
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
    parser.add_argument("--security",
                        help="Security settings, for example: Basic256,SignAndEncrypt,cert.der,pk.pem[,server_cert.der]. Default: None",
                        default='')


def _require_nodeid(parser, args):
    # check that a nodeid has been given explicitly, a bit hackish...
    if args.nodeid == "i=84" and args.path == "":
        parser.print_usage()
        print("{0}: error: A NodeId or BrowsePath is required".format(parser.prog))
        sys.exit(1)


def parse_args(parser, requirenodeid=False):
    args = parser.parse_args()
    logging.basicConfig(format="%(levelname)s: %(message)s", level=getattr(logging, args.loglevel))
    if args.url and '://' not in args.url:
        logging.info("Adding default scheme %s to URL %s", ua.OPC_TCP_SCHEME, args.url)
        args.url = ua.OPC_TCP_SCHEME + '://' + args.url
    if requirenodeid:
        _require_nodeid(parser, args)
    return args


def get_node(client, args):
    node = client.get_node(args.nodeid)
    if args.path:
        path = args.path.split(",")
        if node.nodeid == ua.NodeId(84, 0) and path[0] == "0:Root":
            # let user specify root if not node given
            path = path[1:]
        node = node.get_child(path)
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
    client.set_security_string(args.security)
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
    return val in ("true", "True")


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
        return _arg_to_variant(val, array, ua.LocalizedText, ua.VariantType.LocalizedText)


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
    client.set_security_string(args.security)
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
    client.set_security_string(args.security)
    client.connect()
    try:
        node = get_node(client, args)
        print("Browsing node {0} at {1}\n".format(node, args.url))
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
        print("{0:30} {1:25}".format("DisplayName", "NodeId"))
        print("")
    for desc in node.get_children_descriptions():
        print("{0}{1:30} {2:25}".format(indent, desc.DisplayName.to_string(), desc.NodeId.to_string()))
        if depth:
            _lsprint_0(Node(node.server, desc.NodeId), depth - 1, indent + "  ")


def _lsprint_1(node, depth, indent=""):
    if not indent:
        print("{0:30} {1:25} {2:25} {3:25}".format("DisplayName", "NodeId", "BrowseName", "Value"))
        print("")

    for desc in node.get_children_descriptions():
        if desc.NodeClass == ua.NodeClass.Variable:
            val = Node(node.server, desc.NodeId).get_value()
            print("{0}{1:30} {2!s:25} {3!s:25}, {4!s:3}".format(indent, desc.DisplayName.to_string(), desc.NodeId.to_string(), desc.BrowseName.to_string(), val))
        else:
            print("{0}{1:30} {2!s:25} {3!s:25}".format(indent, desc.DisplayName.to_string(), desc.NodeId.to_string(), desc.BrowseName.to_string()))
        if depth:
            _lsprint_1(Node(node.server, desc.NodeId), depth - 1, indent + "  ")


def _lsprint_long(pnode, depth, indent=""):
    if not indent:
        print("{0:30} {1:25} {2:25} {3:10} {4:30} {5:25}".format("DisplayName", "NodeId", "BrowseName", "DataType", "Timestamp", "Value"))
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
            print("{0}{1:30} {2:25} {3:25} {4:10} {5!s:30} {6!s:25}".format(indent, name.to_string(), node.nodeid.to_string(), bname.to_string(), dtype.to_string(), update, val))
        else:
            print("{0}{1:30} {2:25} {3:25}".format(indent, name.to_string(), bname.to_string(), node.nodeid.to_string()))
        if depth:
            _lsprint_long(node, depth - 1, indent + "  ")


class SubHandler(object):

    def datachange_notification(self, node, val, data):
        print("New data change event", node, val, data)

    def event_notification(self, event):
        print("New event", event)


def uasubscribe():
    parser = argparse.ArgumentParser(description="Subscribe to a node and print results")
    add_common_args(parser)
    parser.add_argument("-t",
                        "--eventtype",
                        dest="eventtype",
                        default="datachange",
                        choices=['datachange', 'event'],
                        help="Event type to subscribe to")

    args = parse_args(parser, requirenodeid=False)
    if args.eventtype == "datachange":
        _require_nodeid(parser, args)
    else:
        # FIXME: this is broken, someone may have written i=84 on purpose
        if args.nodeid == "i=84" and args.path == "":
            args.nodeid = "i=2253"

    client = Client(args.url, timeout=args.timeout)
    client.set_security_string(args.security)
    client.connect()
    try:
        node = get_node(client, args)
        handler = SubHandler()
        sub = client.create_subscription(500, handler)
        if args.eventtype == "datachange":
            sub.subscribe_data_change(node)
        else:
            sub.subscribe_events(node)
        print("Type Ctr-C to exit")
        while True:
            time.sleep(1)
    finally:
        client.disconnect()
    sys.exit(0)
    print(args)


def application_to_strings(app):
    result = []
    result.append(('Application URI', app.ApplicationUri))
    optionals = [
        ('Product URI', app.ProductUri),
        ('Application Name', app.ApplicationName.to_string()),
        ('Application Type', str(app.ApplicationType)),
        ('Gateway Server URI', app.GatewayServerUri),
        ('Discovery Profile URI', app.DiscoveryProfileUri),
    ]
    for (n, v) in optionals:
        if v:
            result.append((n, v))
    for url in app.DiscoveryUrls:
        result.append(('Discovery URL', url))
    return result  # ['{}: {}'.format(n, v) for (n, v) in result]


def cert_to_string(der):
    if not der:
        return '[no certificate]'
    try:
        from opcua.crypto import uacrypto
    except ImportError:
        return "{0} bytes".format(len(der))
    cert = uacrypto.x509_from_der(der)
    return uacrypto.x509_to_string(cert)


def endpoint_to_strings(ep):
    result = [('Endpoint URL', ep.EndpointUrl)]
    result += application_to_strings(ep.Server)
    result += [
        ('Server Certificate', cert_to_string(ep.ServerCertificate)),
        ('Security Mode', str(ep.SecurityMode)),
        ('Security Policy URI', ep.SecurityPolicyUri)]
    for tok in ep.UserIdentityTokens:
        result += [
            ('User policy', tok.PolicyId),
            ('  Token type', str(tok.TokenType))]
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
    client.set_security_string(args.security)
    if args.certificate:
        client.load_client_certificate(args.certificate)
    if args.private_key:
        client.load_private_key(args.private_key)
    client.connect()
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
                        help="URL of OPC UA server, default is opc.tcp://0.0.0.0:4840",
                        default='opc.tcp://0.0.0.0:4840',
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
                        action="store_true",
                        help="Populate address space with some sample nodes")
    parser.add_argument("-c",
                        "--disable-clock",
                        action="store_true",
                        help="Disable clock, to avoid seeing many write if debugging an application")
    parser.add_argument("-s",
                        "--shell",
                        action="store_true",
                        help="Start python shell instead of randomly changing node values")
    parser.add_argument("--certificate",
                        help="set server certificate")
    parser.add_argument("--private_key",
                        help="set server private key")
    args = parser.parse_args()
    logging.basicConfig(format="%(levelname)s: %(message)s", level=getattr(logging, args.loglevel))

    server = Server()
    server.set_endpoint(args.url)
    if args.certificate:
        server.load_certificate(args.certificate)
    if args.private_key:
        server.load_private_key(args.private_key)
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
        elif args.populate:
            count = 0
            while True:
                time.sleep(1)
                myvar.set_value(math.sin(count / 10))
                myarrayvar.set_value([math.sin(count / 10), math.sin(count / 100)])
                count += 1
        else:
            while True:
                time.sleep(1)
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
        print("Performing discovery at {0}\n".format(args.url))
        for i, server in enumerate(client.connect_and_find_servers_on_network(), start=1):
            print('Server {0}:'.format(i))
            #for (n, v) in application_to_strings(server):
                #print('  {}: {}'.format(n, v))
            print('')

    print("Performing discovery at {0}\n".format(args.url))
    for i, server in enumerate(client.connect_and_find_servers(), start=1):
        print('Server {0}:'.format(i))
        for (n, v) in application_to_strings(server):
            print('  {0}: {1}'.format(n, v))
        print('')

    for i, ep in enumerate(client.connect_and_get_server_endpoints(), start=1):
        print('Endpoint {0}:'.format(i))
        for (n, v) in endpoint_to_strings(ep):
            print('  {0}: {1}'.format(n, v))
        print('')

    sys.exit(0)


def print_history(o):
    print("{0:30} {1:10} {2}".format('Source timestamp', 'Status', 'Value'))
    for d in o:
        print("{0:30} {1:10} {2}".format(str(d.SourceTimestamp), d.StatusCode.name, d.Value.Value))


def str_to_datetime(s, default=None):
    if not s:
        if default is not None:
            return default
        return datetime.utcnow()
    # FIXME: try different datetime formats
    for fmt in ["%Y-%m-%d", "%Y-%m-%d %H:%M", "%Y-%m-%d %H:%M:%S"]:
        try:
            return datetime.strptime(s, fmt)
        except ValueError:
            pass


def uahistoryread():
    parser = argparse.ArgumentParser(description="Read history of a node")
    add_common_args(parser)
    parser.add_argument("--starttime",
                        default=None,
                        help="Start time, formatted as YYYY-MM-DD [HH:MM[:SS]]. Default: current time - one day")
    parser.add_argument("--endtime",
                        default=None,
                        help="End time, formatted as YYYY-MM-DD [HH:MM[:SS]]. Default: current time")
    parser.add_argument("-e",
                        "--events",
                        action="store_true",
                        help="Read event history instead of data change history")
    parser.add_argument("-l",
                        "--limit",
                        type=int,
                        default=10,
                        help="Maximum number of notfication to return")

    args = parse_args(parser, requirenodeid=True)

    client = Client(args.url, timeout=args.timeout)
    client.set_security_string(args.security)
    client.connect()
    try:
        node = get_node(client, args)
        starttime = str_to_datetime(args.starttime, datetime.utcnow() - timedelta(days=1))
        endtime = str_to_datetime(args.endtime, datetime.utcnow())
        print("Reading raw history of node {0} at {1}; start at {2}, end at {3}\n".format(node, args.url, starttime, endtime))
        if args.events:
            evs = node.read_event_history(starttime, endtime, numvalues=args.limit)
            for ev in evs:
                print(ev)
        else:
            print_history(node.read_raw_history(starttime, endtime, numvalues=args.limit))
    finally:
        client.disconnect()
    sys.exit(0)


def uacall():
    parser = argparse.ArgumentParser(description="Call method of a node")
    add_common_args(parser)
    parser.add_argument("-m",
                        "--method",
                        dest="method",
                        type=int,
                        default=None,
                        help="Set method to call. If not given then (single) method of the selected node is used.")
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
                        help="Value to use for call to method, if any",
                        nargs="?",
                        metavar="VALUE")

    args = parse_args(parser, requirenodeid=True)

    client = Client(args.url, timeout=args.timeout)
    client.set_security_string(args.security)
    client.connect()
    try:
        node = get_node(client, args)
        # val must be a tuple in order to enable method calls without arguments
        if ( args.value is None ):
            val = () #empty tuple
        else:
            val = (_val_to_variant(args.value, args),) # tuple with one element

        # determine method to call: Either explicitly given or automatically select the method of the selected node.
        methods = node.get_methods()
        method_id = None
        #print( "methods=%s" % (methods) )

        if ( args.method is None ):
            if ( len( methods ) == 0 ):
                raise ValueError( "No methods in selected node and no method given" )
            elif ( len( methods ) == 1 ):
                method_id = methods[0]
            else:
                raise ValueError( "Selected node has {0:d} methods but no method given. Provide one of {1!s}".format(*(methods)) )
        else:
            for m in methods:
                if ( m.nodeid.Identifier == args.method ):
                    method_id = m.nodeid
                    break

        if ( method_id is None):
            # last resort:
            method_id = ua.NodeId( identifier=args.method )#, namespaceidx=? )#, nodeidtype=?): )

        #print( "method_id=%s\nval=%s" % (method_id,val) )

        result_variants = node.call_method( method_id, *val )
        print( "resulting result_variants={0!s}".format(result_variants) )
    finally:
        client.disconnect()
    sys.exit(0)
    print(args)


def uageneratestructs():
    parser = argparse.ArgumentParser(description="Generate a Python module from the xml structure definition (.bsd)")
    add_common_args(parser, require_node=True)
    parser.add_argument("-o",
                        "--output",
                        dest="output_path",
                        required=True,
                        type=str,
                        default=None,
                        help="The python file to be generated.",
                        )
    args = parse_args(parser, requirenodeid=True)

    client = Client(args.url, timeout=args.timeout)
    client.set_security_string(args.security)
    client.connect()
    try:
        node = get_node(client, args)
        generators, _ = client.load_type_definitions([node])
        generators[0].save_to_file(args.output_path, True)
    finally:
        client.disconnect()
    sys.exit(0)
