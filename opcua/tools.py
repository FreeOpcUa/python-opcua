import logging
import os
import sys
import argparse
from opcua import ua, Client


def add_common_args(parser):
    parser.add_argument("-u",
                        "--url",
                        help="URL of OPC UA server (for example: opc.tcp://example.org:4840)",
                        default='opc.tcp://localhost:4841',
                        metavar="URL")
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

    parser.add_argument("-v",
                        "--verbose",
                        dest="loglevel",
                        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
                        default='WARNING',
                        help="Set log level")


def get_node(client, args):
    node = client.get_node(args.nodeid)
    if args.path:
        node = node.get_child(args.path.split(","))


def uaread():
    parser = argparse.ArgumentParser(description="Read attribute of a node")
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
    if args.nodeid == "i=84" and args.attribute == ua.AttributeIds.Value:
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



