"""
JSON encoder / decoder for OPC UA objects
This can be useful for serializing data for external system such as a cloud service or a web app
"""

from json import JSONEncoder, JSONDecoder

from opcua import ua
from opcua import Node
from opcua.common.subscription import DataChangeNotif
from opcua.common.events import Event
from datetime import datetime

# FIXME this JSON utility is not finished, should implement encoding / decoding of useful UA types
# FIXME this class should be improved to use JSON schemas to better serialize UA objects


class UaJSONEncoder(JSONEncoder):
    """
    JSON encoder utility which is extended to handle opc ua objects
    note that JSON pair order may not match the python object attribute order
    """
    def default(self, o, sort_keys=True):
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
                'Identifier': str(o.Identifier),
                'NamespaceIndex': str(o.NamespaceIndex),
                'NamespaceUri': o.NamespaceUri,
                'NodeIdType': o.NodeIdType.name,

            }
        elif isinstance(o, Node):
            return {
                '__type__': 'Node',
                'NodeId': str(o.nodeid),
                'BrowseName': o.get_browse_name().Name,
                'DisplayName': o.get_display_name().Text.decode(encoding='UTF-8'),
            }
        elif isinstance(o, ua.DataValue):
            return {
                '__type__': 'DataValue',
                'ServerTimestamp': o.ServerTimestamp.isoformat(' '),
                'SourceTimestamp': o.SourceTimestamp.isoformat(' '),
                'StatusCode': o.StatusCode.name,
                'VariantType': o.Value.VariantType.name,
                'Value': str(o.Value.Value),
            }
        elif isinstance(o, DataChangeNotif):
            return {
                '__type__': 'DataChangeNotif',
                'Node': str(o.subscription_data.node.nodeid),
                'DisplayName': o.subscription_data.node.get_display_name().Text.decode(encoding='UTF-8'),
                'ServerTimestamp': o.monitored_item.Value.ServerTimestamp.isoformat(' '),
                'SourceTimestamp': o.monitored_item.Value.SourceTimestamp.isoformat(' '),
                'StatusCode': o.monitored_item.Value.StatusCode.name,
                'VariantType': o.monitored_item.Value.Value.VariantType.name,
                'Value': str(o.monitored_item.Value.Value.Value),
            }
        elif isinstance(o, Event):
            return {
                '__type__': 'Event',
                'SourceNode': str(o.SourceNode),
                'EventId': o.EventId,
                'EventType': str(o.EventType),
                'LocalTime': o.LocalTime.isoformat(' '),
                'ReceiveTime': o.ReceiveTime.isoformat(' '),
                'Time': o.Time.isoformat(' '),
                'Severity': str(o.Severity),
                'Message': o.Message.Text.decode(encoding='UTF-8'),
            }
        else:
            return JSONEncoder.default(self, o)


class UaJSONDecoder(JSONDecoder):
    """
    JSON decoder utility which is extended to handle opc ua objects
    Limited functionality; user must check what kind of object was decoded externally
    """
    def __init__(self):
        JSONDecoder.__init__(self, object_hook=self.dict_to_object)

    def dict_to_object(self, d):
        if '__type__' not in d:
            return d

        o_type = d.pop('__type__')
        if o_type == 'datetime':
            return datetime(**d)
        elif o_type == 'NodeId':
            node_id_type = d.pop('NodeIdType')

            if node_id_type == 'Numeric':
                identifier = int(d.pop('Identifier'))
            elif node_id_type == 'String':
                identifier = d.pop('Identifier')
            elif node_id_type == 'ByteString':
                identifier = bytes(d.pop('Identifier'))
            else:
                raise ValueError("NodeId object missing NodeIdType attribute")

            return ua.NodeId(identifier, int(d.pop('NamespaceIndex')))
        elif o_type == 'Node':
            raise TypeError("Node should not be decoded because it requires a reference to the server")
        elif o_type == 'DataValue':
            variant_type = d.pop('VariantType')
            if variant_type in ("Int8", "UInt8", "Int16", "UInt16", "Int32", "UInt32", "Int64", "UInt64"):
                dv = ua.DataValue(ua.Variant(int(d.pop('Value'))))
            elif variant_type in ("Float", "Double"):
                dv = ua.DataValue(ua.Variant(float(d.pop('Value'))))
            elif variant_type in ("Boolean"):
                dv = ua.DataValue(ua.Variant(bool(d.pop('Value'))))
            elif variant_type in ("ByteString", "String"):
                dv = ua.DataValue(ua.Variant(d.pop('Value')))
            else:
                raise TypeError("DataValue did not have a supported variant type")
            return dv
        elif o_type == 'DataChangeNotif':
            raise TypeError("DataChangeNotif should not be decoded")
        elif o_type == 'Event':
            raise TypeError("Event should not be decoded")
        else:
            #  decoder subclass can't handle this object type; put it back in the dict so super throws TypeError
            d['__type__'] = o_type
            return d
