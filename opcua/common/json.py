"""
JSON encoder / decoder for OPC UA objects
Not yet used anywhere, but could be useful in the future for sending data to
external system such as a web based app
"""

from json import JSONEncoder, JSONDecoder

from opcua import ua
from datetime import datetime

# FIXME this JSON utility is not finished, should implement encoding / decoding of useful UA types


class UaJSONEncoder(JSONEncoder):
    """
    JSON encoder utility which is extended to handle opc ua objects
    """
    def default(self, o):
        if isinstance(o, datetime):
            return {
                '__type__': 'datetime',
                'year': o.year,
                'month': o.month,
                'day': o.day,
                'hour': o.hour,
                'minute': o.minute,
                'second': o.second,
                'microsecond': o.microsecond
            }
        elif isinstance(o, ua.NodeId):
            return {
                '__type__': 'NodeId',
                'Identifier': o.Identifier,
                'NamespaceIndex': o.NamespaceIndex,
            }
        else:
            return JSONEncoder.default(self, o)


class UaJSONDecoder(JSONDecoder):
    """
    JSON decoder utility which is extended to handle opc ua objects
    """
    def __init__(self):
        JSONDecoder.__init__(self, object_hook=self.dict_to_object)

    def dict_to_object(self, d):
        if '__type__' not in d:
            return d

        type = d.pop('__type__')
        if type == 'datetime':
            return datetime(**d)
        elif type == 'NodeId':
            return ua.NodeId(**d)
        else:
            #  decoder subclass can't handle this object type; put it back in the dict so super throws TypeError
            d['__type__'] = type
            return d
