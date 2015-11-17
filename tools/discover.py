#!/usr/bin/env python
# Prints OPC UA servers and endpoints for URL

import os, sys, argparse, logging
from enum import Enum
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/..")
from opcua import ua, Client

# converts numeric value to its enum name.
def enum_to_string(klass, value):
    if isinstance(value, Enum):
        return value.name
    # if value is not a subtype of Enum, try to find a constant
    # with this value in this class
    for k,v in vars(klass).items():
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
    return result # ['{}: {}'.format(n, v) for (n, v) in result]

def endpoint_to_strings(ep):
    result = [('Endpoint URL', ep.EndpointUrl)]
    result += application_to_strings(ep.Server)
    result += [
        ('Server Certificate', len(ep.ServerCertificate)),
        ('Security Mode', enum_to_string(ua.MessageSecurityMode, ep.SecurityMode)),
        ('Security Policy URI', ep.SecurityPolicyUri) ]
    for tok in ep.UserIdentityTokens:
        result += [
            ('User policy', tok.PolicyId),
            ('  Token type', enum_to_string(ua.UserTokenType, tok.TokenType)) ]
        if tok.IssuedTokenType or tok.IssuerEndpointUrl:
            result += [
                ('  Issued Token type', tok.IssuedTokenType)
                ('  Issuer Endpoint URL', tok.IssuerEndpointUrl) ]
        if tok.SecurityPolicyUri:
            result.append(('  Security Policy URI', tok.SecurityPolicyUri))
    result += [
        ('Transport Profile URI', ep.TransportProfileUri),
        ('Security Level', ep.SecurityLevel)]
    return result

def main(args, loglevel):
    logging.basicConfig(format="%(levelname)s: %(message)s", level=loglevel)

    client = Client(args.address, timeout=10)
    for i, server in enumerate(client.find_all_servers(), start=1):
        print('Server {}:'.format(i))
        for (n, v) in application_to_strings(server):
            print('  {}: {}'.format(n, v))
        print('')

    client = Client(args.address, timeout=10)
    for i, ep in enumerate(client.get_server_endpoints()):
        print('Endpoint {}:'.format(i))
        for (n, v) in endpoint_to_strings(ep):
            print('  {}: {}'.format(n, v))
        print('')

    exit(0)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description = "Performs OPC UA discovery and prints information on servers and endpoints.")
    parser.add_argument("address",
        help = "URL of OPC UA server (for example, opc.tcp://example.org:4840)",
        metavar = "URL")
    parser.add_argument(
        "-v",
        "--verbose",
        dest="logLevel",
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
        default='ERROR',
        help="Set the logging level")
    args = parser.parse_args()

    main(args, getattr(logging, args.logLevel))
