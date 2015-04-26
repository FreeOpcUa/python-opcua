from opcua.attribute_ids import AttributeIds
from opcua.object_ids import ObjectIds
from opcua.status_code import StatusCodes
from opcua.uaprotocol_auto import *
from opcua.uaprotocol_hand import *


# FIXME: this is really crappy, should thing about a better implementation
# maybe never inherit extensionobject and parse only body....
def downcast_extobject(item):
    if item.TypeId.Identifier == 0:
        return item
    objectidname = ObjectIdsInv[item.TypeId.Identifier]
    classname = objectidname.split("_")[0]
    cmd = "{}.from_binary(utils.Buffer(item.to_binary()))".format(classname)
    return eval(cmd)
