"""
Usefull method and classes not belonging anywhere and depending on opcua library
"""

from dateutil import parser
from datetime import datetime
from enum import Enum

from opcua import ua


def val_to_string(val):
    """
    convert a python object or python-opcua object to a string
    which should be easy to understand for human
    easy to modify, and not too hard to parse back ....not easy
    meant for UI or command lines

    """
    if isinstance(val, (list, tuple)):
        res = []
        for v in val:
            res.append(val_to_string(v))
        return "[" + ", ".join(res) + "]"

    if isinstance(val, (ua.NodeId)):
        val = val.to_string()
    elif isinstance(val, (ua.QualifiedName, ua.LocalizedText)):
        val = val.to_string()
    elif isinstance(val, Enum):
        val = val.name
    elif isinstance(val, ua.DataValue):
        val = variant_to_string(val.Value)
    elif isinstance(val, str):
        pass
    elif isinstance(val, bytes):
        val = str(val)
    elif isinstance(val, datetime):
        val = val.isoformat()
    else:
        val = str(val)
    return val


def variant_to_string(var):
    """
    convert a variant to a string which should be easy to understand for human
    easy to modify, and not too hard to parse back ....not easy
    meant for UI or command lines
    """
    return val_to_string(var.Value)


def string_to_val(string, vtype):
    """
    Convert back a string to a python or python-opcua object 
    """
    string = string.strip()
    if string.startswith("["):
        string = string[1:-1]
        var = []
        for s in string.split(","):
            s = s.strip()
            val = string_to_val(s, vtype)
            var.append(val)
        return var

    if vtype == ua.VariantType.Boolean:
        val = bool(string)
    elif 4 <= vtype.value < 9:
        val = int(string)
    elif vtype in (ua.VariantType.Float, ua.VariantType.Double):
        val = float(string)
    elif vtype == ua.VariantType.String:
        val = string
    elif vtype == ua.VariantType.NodeId:
        val = ua.NodeId.from_string(string)
    elif vtype == ua.VariantType.DateTime:
        val = parser.parse(string)
    else:
        raise NotImplementedError
    return val


def string_to_variant(string, vtype):
    """
    convert back a string to an ua.Variant
    """
    return ua.Variant(string_to_val(string, vtype), vtype)


