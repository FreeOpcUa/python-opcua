"""
High level method related functions
"""

from opcua import ua
from opcua.common import node


def call_method(parent, methodid, *args):
    """
    Call an OPC-UA method. methodid is browse name of child method or the
    nodeid of method as a NodeId object
    arguments are variants or python object convertible to variants.
    which may be of different types
    returns a list of values or a single value depending on the output of the method
    """
    result = call_method_full(parent, methodid, *args)

    if len(result.OutputArguments) == 0:
        return None
    elif len(result.OutputArguments) == 1:
        return result.OutputArguments[0]
    else:
        return result.OutputArguments


def call_method_full(parent, methodid, *args):
    """
    Call an OPC-UA method. methodid is browse name of child method or the
    nodeid of method as a NodeId object
    arguments are variants or python object convertible to variants.
    which may be of different types
    returns a CallMethodResult object with converted OutputArguments
    """
    if isinstance(methodid, (str, ua.uatypes.QualifiedName)):
        methodid = parent.get_child(methodid).nodeid
    elif isinstance(methodid, node.Node):
        methodid = methodid.nodeid

    result = _call_method(parent.server, parent.nodeid, methodid, to_variant(*args))
    result.OutputArguments = [var.Value for var in result.OutputArguments]
    return result


def _call_method(server, parentnodeid, methodid, arguments):
    request = ua.CallMethodRequest()
    request.ObjectId = parentnodeid
    request.MethodId = methodid
    request.InputArguments = arguments
    methodstocall = [request]
    results = server.call(methodstocall)
    res = results[0]
    res.StatusCode.check()
    return res


def uamethod(func):
    """
    Method decorator to automatically convert
    arguments and output to and from variants
    """
    def wrapper(parent, *args):
        if isinstance(parent, ua.NodeId):
            result = func(parent, *[arg.Value for arg in args])
        else:
            self = parent
            parent = args[0]
            args = args[1:]
            result = func(self, parent, *[arg.Value for arg in args])
        if result is None:
            return []
        elif isinstance(result, ua.CallMethodResult):
            result.OutputArguments = to_variant(*result.OutputArguments)
            return result
        elif isinstance(result, ua.StatusCode):
            return result
        elif isinstance(result, tuple):
            return to_variant(*result)
        else:
            return to_variant(result)
    return wrapper


def to_variant(*args):
    uaargs = []
    for arg in args:
        if not isinstance(arg, ua.Variant):
            arg = ua.Variant(arg)
        uaargs.append(arg)
    return uaargs
