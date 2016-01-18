Pure Python OPC-UA / IEC 62541 Client and Server Python 2, 3 and pypy .
http://freeopcua.github.io/, https://github.com/FreeOpcUa/python-opcua

[![Build Status](https://travis-ci.org/FreeOpcUa/python-opcua.svg?branch=master)](https://travis-ci.org/FreeOpcUa/python-opcua)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/FreeOpcUa/python-opcua/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/FreeOpcUa/python-opcua/?branch=master)
[![Code Coverage](https://scrutinizer-ci.com/g/FreeOpcUa/python-opcua/badges/coverage.png?b=master)](https://scrutinizer-ci.com/g/FreeOpcUa/python-opcua/?branch=master)

OPC-UA implementation is quasi complete and has been tested against many different OPC-UA stacks. API offers both a low level interface to send and receive all UA defined structures and high level classes allowing to write a server or a client in a few lines. It is easy to mix high level objects and low level UA calls in one application.

Most code is autogenerated from xml specification using same code as the one that is used for freeopcua C++ client and server, thus adding missing functionnality to client and server shoud be trivial.

Using Python > 3.4 the only dependency is cryptography. If using python 2.7 or pypy < 3 you need to install enum34, trollius(asyncio), and futures(concurrent.futures), with pip for example. 

coveryage.py reports a test coverage of over 90% of code, most of non-tested code is autogenerate code that is not used yet.

Some documentation is available at http://python-opcua.readthedocs.org/en/latest/

A simple GUI client is available: https://github.com/FreeOpcUa/opcua-client-gui

Examples: https://github.com/FreeOpcUa/python-opcua/tree/master/examples

Minimal client example: https://github.com/FreeOpcUa/python-opcua/tree/master/examples/minimal-client.py
Minimal server example: https://github.com/FreeOpcUa/python-opcua/tree/master/examples/minimal-server.py

A set of command line tools also available: https://github.com/FreeOpcUa/python-opcua/tree/master/tools
* uadiscover (find_servers, get_endpoints and find_servers_on_network calls)
* uals (list children of a node)
* uahistoryread
* uaread (read attribute of a node)
* uawrite (write attribute of a node)
* uasubscribe (subscribe to a node and print datachange events)
* uaclient (connect to server and start python shell)
* uaserver (starts a demo OPC-UA server)

    tools/uaserver --populate --certificate cert.pem --private_key pk.pem


Client: what works:
* connection to server, opening channel, session
* browsing and reading attributes value
* gettings nodes by path and nodeids
* creating subscriptions
* subscribing to items for data change
* subscribing to events
* adding nodes
* method call
* user and password
* history read
* login with certificate
* communication encryption

Tested servers: freeopcua C++, freeopcua Python, prosys, kepware, beckoff

Client: what is not implemented yet 
* localized text feature
* removing nodes 
* adding some missing modify methods


Server: what works:
* creating channel and sessions
* read/set attributes and browse
* gettings nodes by path and nodeids
* autogenerate addres space from spec
* adding nodes to address space
* datachange events
* events
* methods
* basic user implementation (one existing user called admin, which can be disabled, all others are read only)
* encryption
* certificate handling

Tested clients: freeopcua C++, freeopcua Python, uaexpert, prosys, quickopc

Server: what is not implemented
* localized text feature
* better securty model with users and password
* removing nodes 
* adding some missing modify methods
* views


# Development

Code follows PEP8 apart for line lengths and autogenerate class and enums that keep camel case from XML definition.

All code is under opcua directory

- ua contains all UA structures from specification
- common contains high level objects and methods used both in server and client
- client contains client specific code
- server contains server specific code
- utils contains some utilities not really related to OPC-UA
- tools contains command lines tools

## Running tests:

python tests.py

## Coverage

coverage run tests.py  
coverage html  
firefox htmlcov/index.html  

