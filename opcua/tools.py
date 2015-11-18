import logging
import sys
import argparse
from opcua import ua, Client
import code
from enum import Enum

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


def add_common_args(parser):
    add_minimum_args(parser)
    parser.add_argument("-n",
                        "--nodeid",
                        help="Fully-qualified node ID (for example: i=85). Default: root node",
                        default='i=84',
                        metavar="NODE")
    parser.add_argument("-p",
                        "--path",
                        help="Comma separated browse path to the node starting at nodeid (for example: 3:Mybject,3:MyVariable)",
                        default='',
                        metavar="BROWSEPATH")
    parser.add_argument("-i",
                        "--namespace",
                        help="Default namespace",
                        type=int,
                        default=0,
                        metavar="NAMESPACE")


def get_node(client, args):
    node = client.get_node(args.nodeid)
    if args.path:
        node = node.get_child(args.path.split(","))


def uaread():
    parser = argparse.ArgumentParser(description="Read attribute of a node, per default reads value of a node")
    add_common_args(parser)
    parser.add_argument("-a",
                        "--attribute",
                        dest="attribute",
                        type=int,
                        #default="VALUE",
                        #choices=['VALUE', 'NODEID', 'BROWSENAME', 'ERROR', 'CRITICAL'],
                        default=ua.AttributeIds.Value,
                        help="Set attribute to read")
    parser.add_argument("-t",
                        "--datatype",
                        dest="datatype",
                        default="python",
                        choices=['python', 'variant', 'datavalue'],
                        help="Data type to return")

    args = parser.parse_args()
    if args.nodeid == "i=84" and args.path == "" and args.attribute == ua.AttributeIds.Value:
        parser.print_usage()
        print("uaread: error: A NodeId or BrowsePath is required")
        sys.exit(1)
    logging.basicConfig(format="%(levelname)s: %(message)s", level=getattr(logging, args.loglevel))

    client = Client(args.url)
    client.connect()
    try:
        node = client.get_node(args.nodeid)
        if args.path:
            node = node.get_child(args.path.split(","))
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


def uawrite():
    parser = argparse.ArgumentParser(description="Write attribute of a node, per default write value of node")
    add_common_args(parser)
    parser.add_argument("-a",
                        "--attribute",
                        dest="attribute",
                        type=int,
                        #default="VALUE",
                        #choices=['VALUE', 'NODEID', 'BROWSENAME', 'ERROR', 'CRITICAL'],
                        default=ua.AttributeIds.Value,
                        help="Set attribute to read")
    parser.add_argument("-t",
                        "--datatype",
                        dest="datatype",
                        default="guess",
                        choices=["guess", 'nodeid', 'qualifiedname', 'browsename', 'string', 'double', 'int32', "int64", "bool"],  # FIXME: to be finished
                        help="Data type to return")
    parser.add_argument("value",
                        help="Value to be written",
                        metavar="VALUE")
    args = parser.parse_args()
    if args.nodeid == "i=84" and args.path == "" and args.attribute == ua.AttributeIds.Value:
        parser.print_usage()
        print("uaread: error: A NodeId or BrowsePath is required")
        sys.exit(1)
    logging.basicConfig(format="%(levelname)s: %(message)s", level=getattr(logging, args.loglevel))

    client = Client(args.url)
    client.connect()
    try:
        node = client.get_node(args.nodeid)
        if args.path:
            node = node.get_child(args.path.split(","))
        val = args.value
        if args.datatype == "guess":
            try:
                val = int(val)
            except ValueError:
                try:
                    val = float(val)
                except ValueError:
                    pass
        elif args.datatype == "nodeid":
            val = ua.Variant(ua.NodeId.from_string(val))
        elif args.datatype in ("qualifiedname", "browsename"):
            val = ua.Variant(ua.QualifiedName.from_string(val))
        #elif args.datatype == "uint8":
            #val = ua.Variant(int(val), ua.VariantType.UInt8)
        elif args.datatype == "uint16":
            val = ua.Variant(int(val), ua.VariantType.UInt16)
        elif args.datatype == "uint32":
            val = ua.Variant(int(val), ua.VariantType.UInt32)
        elif args.datatype == "uint64":
            val = ua.Variant(int(val), ua.VariantType.UInt64)
        #elif args.datatype == "int8":
            #val = ua.Variant(int(val), ua.VariantType.Int8)
        elif args.datatype == "int16":
            val = ua.Variant(int(val), ua.VariantType.Int16)
        elif args.datatype == "int32":
            val = ua.Variant(int(val), ua.VariantType.Int32)
        elif args.datatype == "int64":
            val = ua.Variant(int(val), ua.VariantType.Int64)
        elif args.datatype == "double":
            val = ua.Variant(float(val), ua.VariantType.Double)
        elif args.datatype == "float":
            val = ua.Variant(float(val), ua.VariantType.Float)
        elif args.datatype == "bool":
            if val in ("1", "True", "true"):
                val = ua.Variant(True, ua.VariantType.Boolean)
            else:
                val = ua.Variant(False, ua.VariantType.Boolean)
        elif args.datatype == "string":
            val = ua.Variant(val, ua.VariantType.String)
        node.set_attribute(args.attribute, ua.DataValue(val))
    finally:
        client.disconnect()
    sys.exit(0)
    print(args)


def uals():
    parser = argparse.ArgumentParser(description="Browse OPC-UA node and print result")
    add_common_args(parser)
    #parser.add_argument("-l",
                        #dest="long_format",
                        #default=ua.AttributeIds.Value,
                        #help="use a long listing format")
    parser.add_argument("-d",
                        "--depth",
                        default=1,
                        type=int,
                        help="Browse depth")

    args = parser.parse_args()
    logging.basicConfig(format="%(levelname)s: %(message)s", level=getattr(logging, args.loglevel))

    client = Client(args.url)
    client.connect()
    try:
        node = client.get_node(args.nodeid)
        if args.path:
            node = node.get_child(args.path.split(","))
        print("Browsing node {} at {}\n".format(node, args.url))
        _lsprint(client, node.nodeid, args.depth - 1)

    finally:
        client.disconnect()
    sys.exit(0)
    print(args)


def _lsprint(client, nodeid, depth, indent=""):
    indent += "    "
    pnode = client.get_node(nodeid)
    for desc in pnode.get_children_descriptions():
        print("{} {}, {}, {}".format(indent, desc.DisplayName.to_string(), desc.BrowseName.to_string(), desc.NodeId.to_string()))
        if depth:
            _lsprint(client, desc.NodeId, depth - 1, indent)


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

    args = parser.parse_args()
    if args.nodeid == "i=84" and args.path == "":
        parser.print_usage()
        print("uaread: error: The NodeId or BrowsePath of a variable is required")
        sys.exit(1)
    logging.basicConfig(format="%(levelname)s: %(message)s", level=getattr(logging, args.loglevel))

    client = Client(args.url)
    client.connect()
    try:
        node = client.get_node(args.nodeid)
        if args.path:
            node = node.get_child(args.path.split(","))
        handler = SubHandler()
        sub = client.create_subscription(500, handler)
        if args.eventtype == "datachange":
            sub.subscribe_data_change(node)
        else:
            sub.subscribe_events(node)
        vars = globals()
        vars.update(locals())
        shell = code.InteractiveConsole(vars)
        shell.interact()
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
                ('  Issued Token type', tok.IssuedTokenType)
                ('  Issuer Endpoint URL', tok.IssuerEndpointUrl)]
        if tok.SecurityPolicyUri:
            result.append(('  Security Policy URI', tok.SecurityPolicyUri))
    result += [
        ('Transport Profile URI', ep.TransportProfileUri),
        ('Security Level', ep.SecurityLevel)]
    return result


def uadiscover():
    parser = argparse.ArgumentParser(description="Performs OPC UA discovery and prints information on servers and endpoints.")
    add_minimum_args(parser)
    args = parser.parse_args()
    logging.basicConfig(format="%(levelname)s: %(message)s", level=getattr(logging, args.loglevel))

    client = Client(args.url)
    for i, server in enumerate(client.find_all_servers(), start=1):
        print('Server {}:'.format(i))
        for (n, v) in application_to_strings(server):
            print('  {}: {}'.format(n, v))
        print('')

    client = Client(args.url)
    for i, ep in enumerate(client.get_server_endpoints()):
        print('Endpoint {}:'.format(i))
        for (n, v) in endpoint_to_strings(ep):
            print('  {}: {}'.format(n, v))
        print('')

    sys.exit(0)


