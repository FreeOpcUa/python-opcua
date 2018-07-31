#! /usr/bin/env python
import os
from urllib.request import build_opener

# https://opcfoundation.org/UA/schemas/OPC%20UA%20Schema%20Files%20Readme.xls

resources = [
    'https://opcfoundation.org/UA/schemas/1.04/Opc.Ua.Types.xsd',
    'https://opcfoundation.org/UA/schemas/1.04/Opc.Ua.Services.wsdl',
    'https://opcfoundation.org/UA/schemas/1.04/Opc.Ua.Endpoints.wsdl',
    'https://opcfoundation.org/UA/schemas/DI/1.0/Opc.Ua.Di.Types.xsd',
    'https://opcfoundation.org/UA/schemas/ADI/1.1/Opc.Ua.Adi.Types.xsd',

    'https://opcfoundation.org/UA/schemas/1.04/SecuredApplication.xsd',

    'https://opcfoundation.org/UA/schemas/1.04/UANodeSet.xsd',
    'https://opcfoundation.org/UA/schemas/1.04/UAVariant.xsd',
    'https://opcfoundation.org/UA/schemas/1.04/Opc.Ua.NodeSet2.xml',
    'https://opcfoundation.org/UA/schemas/1.04/Opc.Ua.NodeSet2.Part3.xml',
    'https://opcfoundation.org/UA/schemas/1.04/Opc.Ua.NodeSet2.Part4.xml',
    'https://opcfoundation.org/UA/schemas/1.04/Opc.Ua.NodeSet2.Part5.xml',
    'https://opcfoundation.org/UA/schemas/1.04/Opc.Ua.NodeSet2.Part8.xml',
    'https://opcfoundation.org/UA/schemas/1.04/Opc.Ua.NodeSet2.Part9.xml',
    'https://opcfoundation.org/UA/schemas/1.04/Opc.Ua.NodeSet2.Part10.xml',
    'https://opcfoundation.org/UA/schemas/1.04/Opc.Ua.NodeSet2.Part11.xml',
    'https://opcfoundation.org/UA/schemas/1.04/Opc.Ua.NodeSet2.Part13.xml',
    'https://opcfoundation.org/UA/schemas/DI/1.0/Opc.Ua.Di.NodeSet2.xml',
    'https://opcfoundation.org/UA/schemas/ADI/1.1/Opc.Ua.Adi.NodeSet2.xml',

    'https://opcfoundation.org/UA/schemas/1.04/OPCBinarySchema.xsd',
    'https://opcfoundation.org/UA/schemas/1.04/Opc.Ua.Types.bsd',
    'https://opcfoundation.org/UA/schemas/DI/1.0/Opc.Ua.Di.Types.bsd',
    'https://opcfoundation.org/UA/schemas/ADI/1.1/Opc.Ua.Adi.Types.bsd',

    'https://opcfoundation.org/UA/schemas/1.04/AttributeIds.csv',
    'https://opcfoundation.org/UA/schemas/1.04/StatusCode.csv',
    'https://opcfoundation.org/UA/schemas/1.04/NodeIds.csv',
]

opener = build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

for url in resources:
    f_name = os.path.basename(url)
    print('downloading', f_name, '... ', end='')
    try:
        open(f_name, 'wb+').write(opener.open(url).read())
        print('OK')
    except Exception as e:
        print(f'FAILED ({e!r})')
