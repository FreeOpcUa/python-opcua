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

    client = Client(args.url, timeout=args.timeout)
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
                        #default="VALUE",
                        #choices=['VALUE', 'NODEID', 'BROWSENAME', 'ERROR', 'CRITICAL'],
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
    args = parser.parse_args()
    if args.nodeid == "i=84" and args.path == "" and args.attribute == ua.AttributeIds.Value:
        parser.print_usage()
        print("uaread: error: A NodeId or BrowsePath is required")
        sys.exit(1)
    logging.basicConfig(format="%(levelname)s: %(message)s", level=getattr(logging, args.loglevel))

    client = Client(args.url, timeout=args.timeout)
    client.connect()
    try:
        node = client.get_node(args.nodeid)
        if args.path:
            node = node.get_child(args.path.split(","))
        val = _val_to_variant(args.value, args)
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

    client = Client(args.url, timeout=args.timeout)
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

    client = Client(args.url, timeout=args.timeout)
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
        glbs = globals()
        glbs.update(locals())
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
                ('  Issued Token type', tok.IssuedTokenType),
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

    client = Client(args.url, timeout=args.timeout)
    print("Performing discovery at {}\n".format(args.url))
    for i, server in enumerate(client.find_all_servers(), start=1):
        print('Server {}:'.format(i))
        for (n, v) in application_to_strings(server):
            print('  {}: {}'.format(n, v))
        print('')

    client = Client(args.url, timeout=args.timeout)
    for i, ep in enumerate(client.get_server_endpoints(), start=1):
        print('Endpoint {}:'.format(i))
        for (n, v) in endpoint_to_strings(ep):
            print('  {}: {}'.format(n, v))
        print('')

    sys.exit(0)


