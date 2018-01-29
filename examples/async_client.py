
import asyncio
import logging

from opcua.client.client import Client
from opcua import ua

logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger('opcua')
OBJECTS_AND_VARIABLES = ua.NodeClass.Object | ua.NodeClass.Variable


async def browse_nodes(node, level=0):
    node_class = await node.get_node_class()
    children = []
    for child in await node.get_children(nodeclassmask=OBJECTS_AND_VARIABLES):
        children.append(await browse_nodes(child, level=level + 1))
    return {
        'id': node.nodeid.to_string(),
        'name': (await node.get_display_name()).Text,
        'cls': node_class.value,
        'children': children,
        'type': (await node.get_data_type_as_variant_type()).value if node_class == ua.NodeClass.Variable else None,
    }


async def task(loop):
    try:
        client = Client(url='opc.tcp://commsvr.com:51234/UA/CAS_UA_Server')
        await client.connect()
        obj_node = client.get_objects_node()
        _logger.info('Objects Node: %r', obj_node)
        tree = await browse_nodes(obj_node)
        _logger.info('Tree: %r', tree)
    except Exception:
        _logger.exception('Task error')
    loop.stop()


def main():
    loop = asyncio.get_event_loop()
    loop.set_debug(True)
    loop.create_task(task(loop))
    try:
        loop.run_forever()
    except Exception:
        _logger.exception('Event loop error')
        loop.run_until_complete(loop.shutdown_asyncgens())
        loop.close()


if __name__ == '__main__':
    main()
