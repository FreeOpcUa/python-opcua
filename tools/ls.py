#!/usr/bin/env python
# lists references of OPC node

import os, sys, argparse, logging
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/..")
from opcua import ua, Client

FORMATS = ['display-name', 'browse-name', 'node-id']

def main(args, loglevel):
    logging.basicConfig(format="%(levelname)s: %(message)s", level=loglevel)

    i = -1
    if args.format in FORMATS:
        i = FORMATS.index(args.format)

    client = Client(args.address, timeout=10)
    try:
        client.connect()
        if args.node_id:
            root = client.get_node(ua.NodeId.from_string(args.node_id))
        else:
            root = client.get_root_node()
        for x in root.get_children_descriptions():
            data = [x.DisplayName.to_string(), x.BrowseName.to_string(), x.NodeId.to_string()]
            if i >= 0:
                print(data[i])
            else:
                print("\t".join(data))
    finally:
        client.disconnect()
    exit(0)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = "Performs OPC UA browse and prints result.")
    parser.add_argument("address",
        help = "URL of OPC UA server (for example, opc.tcp://example.org:4840)",
        metavar = "URL")
    parser.add_argument("node_id",
        help = "Fully-qualified node ID (for example, i=85). Default: root node",
        default='',
        nargs='?',
        metavar = "NODE")
    parser.add_argument(
        "-v",
        "--verbose",
        dest="logLevel",
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
        default='ERROR',
        help="Set the logging level")
    parser.add_argument(
        "-f",
        "--format",
        dest="format",
        choices=['full'] + FORMATS,
        default='full',
        help="Set the output format. Default: full")
    args = parser.parse_args()

    main(args, getattr(logging, args.logLevel))
