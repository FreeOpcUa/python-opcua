
IgnoredEnums = ["NodeIdType"]
IgnoredStructs = ["QualifiedName", "NodeId", "ExpandedNodeId", "FilterOperand", "Variant", "DataValue", "LocalizedText", "ExtensionObject", "XmlElement"]

class Primitives1(object):
    Int8 = 0
    SByte = 0
    Int16 = 0
    Int32 = 0
    Int64 = 0
    UInt8 = 0
    Char = 0
    Byte = 0
    UInt16 = 0
    UInt32 = 0
    UInt64 = 0
    Boolean = 0
    Double = 0
    Float = 0


class Primitives(Primitives1):
    Null = 0
    String = 0
    Bytes = 0
    ByteString = 0
    CharArray = 0
    DateTime = 0



class CodeGenerator(object):

    def __init__(self, model, output):
        self.model = model
        self.output_path = output
        self.indent = "    "
        self.iidx = 0  # indent index

    def run(self):
        print("Writting python protocol code to ", self.output_path)
        self.output_file = open(self.output_path, "w")
        self.make_header()
        for enum in self.model.enums:
            if enum.name not in IgnoredEnums:
                self.generate_enum_code(enum)
        for struct in self.model.structs:
            if struct.name in IgnoredStructs:
                continue
            if struct.name.endswith("Node") or struct.name.endswith("NodeId"):
                continue
            self.generate_struct_code(struct)

        self.iidx = 0
        self.write("")
        self.write("")
        self.write("ExtensionClasses = {")
        for struct in self.model.structs:
            if struct.name in IgnoredStructs:
                continue
            if struct.name.endswith("Node") or struct.name.endswith("NodeId"):
                continue
            if "ExtensionObject" in struct.parents:
                self.write("    ObjectIds.{0}_Encoding_DefaultBinary: {0},".format(struct.name))
        self.write("}")
        self.write("")
        with open('uaprotocol_auto_add.py') as f:
            for line in f:
                self.write(line.rstrip())

    def write(self, line):
        if line:
            line = self.indent * self.iidx + line
        self.output_file.write(line + "\n")

    def make_header(self):
        self.write("'''")
        self.write("Autogenerate code from xml spec")
        self.write("'''")
        self.write("")
        self.write("from datetime import datetime")
        self.write("from enum import Enum, IntEnum")
        self.write("")
        self.write("from opcua.common.utils import Buffer")
        self.write("from opcua.ua.uaerrors import UaError")
        self.write("from opcua.ua.uatypes import *")
        self.write("from opcua.ua import ua_binary as uabin")
        self.write("from opcua.ua.object_ids import ObjectIds")

    def generate_enum_code(self, enum):
        self.write("")
        self.write("")
        self.write("class {}(IntEnum):".format(enum.name))
        self.iidx = 1
        self.write("'''")
        if enum.doc:
            self.write(enum.doc)
            self.write("")
        for val in enum.values:
            self.write(":ivar {}:".format(val.name))
            self.write(":vartype {}: {}".format(val.name, val.value))
        self.write("'''")
        for val in enum.values:
            self.write("{} = {}".format(val.name, val.value))
        self.iidx = 0

    def generate_struct_code(self, obj):
        self.write("")
        self.write("")
        self.iidx = 0
        self.write("class {}(FrozenClass):".format(obj.name))
        self.iidx += 1
        self.write("'''")
        if obj.doc:
            self.write(obj.doc)
            self.write("")
        for field in obj.fields:
            self.write(":ivar {}:".format(field.name))
            self.write(":vartype {}: {}".format(field.name, field.uatype))
        self.write("'''")

        self.write("")
        self.write("ua_types = {")
        for field in obj.fields:
            self.write("    '{}': '{}',".format(field.name, field.uatype))
        self.write("           }")
        self.write("")

        self.write("def __init__(self, binary=None):")
        self.iidx += 1
        self.write("if binary is not None:")
        self.iidx += 1
        self.write("self._binary_init(binary)")
        self.write("self._freeze = True")
        self.write("return")
        self.iidx -= 1

        # hack extension object stuff
        extobj_hack = False
        if "BodyLength" in [f.name for f in obj.fields]:
            extobj_hack = True

        for field in obj.fields:
            if extobj_hack and field.name == "Encoding":
                self.write("self.Encoding = 1")
            elif field.uatype == obj.name:  # help!!! selv referencing class
                self.write("self.{} = None".format(field.name))
            elif not obj.name in ("ExtensionObject") and field.name == "TypeId":  # and ( obj.name.endswith("Request") or obj.name.endswith("Response")):
                self.write("self.TypeId = FourByteNodeId(ObjectIds.{}_Encoding_DefaultBinary)".format(obj.name))
            else:
                self.write("self.{} = {}".format(field.name, "[]" if field.length else self.get_default_value(field)))
        self.write("self._freeze = True")
        self.iidx = 1

        # serialize code
        self.write("")
        self.write("def to_binary(self):")
        self.iidx += 1

        # hack for self referencing classes
        # for field in obj.fields:
        # if field.uatype == obj.name: #help!!! selv referencing class
        #self.write("if self.{name} is None: self.{name} = {uatype}()".format(name=field.name, uatype=field.uatype))

        self.write("packet = []")
        if extobj_hack:
            self.write("body = []")
        #self.write("tmp = packet")
        for field in obj.fields:
            if field.switchfield:
                if field.switchvalue:
                    bit = obj.bits[field.switchfield]
                    #self.write("if self.{}: self.{} |= (value << {})".format(field.name, field.switchfield, field.switchvalue))
                    mask = '0b' + '0' * (8 - bit.length) + '1' * bit.length
                    self.write("others = self.{} & {}".format(bit.container, mask))
                    self.write("if self.{}: self.{} = ( {} | others )".format(field.name, bit.container, field.switchvalue))
                else:
                    bit = obj.bits[field.switchfield]
                    self.write("if self.{}: self.{} |= (1 << {})".format(field.name, bit.container, bit.idx))
        iidx = self.iidx
        listname = "packet"
        for idx, field in enumerate(obj.fields):
            # if field.name == "Body" and idx <= (len(obj.fields)-1):
            if field.name == "BodyLength":
                listname = "body"
                #self.write("tmp = packet")
                continue
            self.iidx = iidx
            switch = ""
            fname = "self." + field.name
            if field.switchfield:
                self.write("if self.{}: ".format(field.name))
                self.iidx += 1
            if field.length:
                self.write("{}.append(uabin.Primitives.Int32.pack(len(self.{})))".format(listname, field.name))
                self.write("for fieldname in self.{}:".format(field.name))
                fname = "fieldname"
                self.iidx += 1
            if field.is_native_type():
                self.write_pack_uatype(listname, fname, field.uatype)
            elif field.uatype in self.model.enum_list:
                enum = self.model.get_enum(field.uatype)
                self.write_pack_enum(listname, fname, enum)
            elif field.uatype in ("ExtensionObject"):
                self.write("{}.append(extensionobject_to_binary({}))".format(listname, fname))
            else:
                self.write("{}.append({}.to_binary())".format(listname, fname))
            if field.length:
                self.iidx -= 1
        self.iidx = 2
        if extobj_hack:
            self.write("body = b''.join(body)")
            self.write("packet.append(struct.pack('<i', len(body)))")
            self.write("packet.append(body)")
        self.write("return b''.join(packet)")
        self.write("")

        self.iidx = 1
        # deserialize
        self.write("@staticmethod")
        self.write("def from_binary(data):")
        self.iidx += 1
        self.write("return {}(data)".format(obj.name))
        self.iidx -= 1
        self.write("")

        self.write("def _binary_init(self, data):")
        self.iidx += 1
        iidx = self.iidx
        for idx, field in enumerate(obj.fields):
            self.iidx = iidx
            # if field.name == "Body" and idx <= (len(obj.fields)-1):
            #self.write("bodylength = struct.unpack('<i', data)[0]")
            # continue
            if field.switchfield:
                bit = obj.bits[field.switchfield]
                if field.switchvalue:
                    mask = '0b' + '0' * (8 - bit.length) + '1' * bit.length
                    self.write("val = self.{} & {}".format(bit.container, mask))
                    self.write("if val == {}:".format(bit.idx))
                else:
                    self.write("if self.{} & (1 << {}):".format(bit.container, bit.idx))
                self.iidx += 1
            if field.is_native_type():
                if field.length:
                    self.write("self.{} = uabin.Primitives.{}.unpack_array(data)".format(field.name, field.uatype))
                else:
                    self.write_unpack_uatype(field.name, field.uatype)
            elif field.uatype in self.model.enum_list:
                #uatype = self.model.get_enum(field.uatype).uatype
                #self.write_unpack_uatype(field.name, uatype)
                enum = self.model.get_enum(field.uatype)
                self.write_unpack_enum(field.name, enum)
            else:
                if field.uatype in ("ExtensionObject"):
                    frombinary = "extensionobject_from_binary(data)"
                else:
                    frombinary = "{}.from_binary(data)".format(field.uatype)
                if field.length:
                    self.write("length = uabin.Primitives.Int32.unpack(data)")
                    self.write("array = []")
                    self.write("if length != -1:")
                    self.iidx += 1
                    self.write("for _ in range(0, length):")
                    self.iidx += 1
                    self.write("array.append({})".format(frombinary))
                    self.iidx -= 2
                    self.write("self.{} = array".format(field.name))
                else:
                    self.write("self.{} = {}".format(field.name, frombinary))
            if field.switchfield:
                self.iidx -= 1
                self.write("else:")
                self.iidx += 1
                if extobj_hack and field.name == "Encoding":
                    self.write("self.Encoding = 1")
                elif field.uatype == obj.name:  # help!!! selv referencing class
                    self.write("self.{} = None".format(field.name))
                elif not obj.name in ("ExtensionObject") and field.name == "TypeId":  # and ( obj.name.endswith("Request") or obj.name.endswith("Response")):
                    self.write("self.TypeId = FourByteNodeId(ObjectIds.{}_Encoding_DefaultBinary)".format(obj.name))
                else:
                    self.write("self.{} = {}".format(field.name, "[]" if field.length else self.get_default_value(field)))
        if len(obj.fields) == 0:
            self.write("pass")

        self.iidx = 2

        #__str__
        self.iidx = 1
        self.write("")
        self.write("def __str__(self):")
        self.iidx += 1
        tmp = ["'{name}:' + str(self.{name})".format(name=f.name) for f in obj.fields]
        tmp = " + ', ' + \\\n               ".join(tmp)
        self.write("return '{}(' + {} + ')'".format(obj.name, tmp))
        self.iidx -= 1
        self.write("")
        self.write("__repr__ = __str__")

        self.iix = 0

    def write_unpack_enum(self, name, enum):
        self.write("self.{} = {}(uabin.Primitives.{}.unpack(data))".format(name, enum.name, enum.uatype))

    def get_size_from_uatype(self, uatype):
        if uatype in ("Int8", "UInt8", "Sbyte", "Byte", "Char", "Boolean"):
            return 1
        elif uatype in ("Int16", "UInt16"):
            return 2
        elif uatype in ("Int32", "UInt32", "Float"):
            return 4
        elif uatype in ("Int64", "UInt64", "Double"):
            return 8
        else:
            raise Exception("Cannot get size from type {}".format(uatype))

    def write_unpack_uatype(self, name, uatype):
        if hasattr(Primitives, uatype):
            self.write("self.{} = uabin.Primitives.{}.unpack(data)".format(name, uatype))
        else:
            self.write("self.{} = {}.from_binary(data))".format(name, uatype))

    def write_pack_enum(self, listname, name, enum):
        self.write("{}.append(uabin.Primitives.{}.pack({}.value))".format(listname, enum.uatype, name))

    def write_pack_uatype(self, listname, name, uatype):
        if hasattr(Primitives, uatype):
            self.write("{}.append(uabin.Primitives.{}.pack({}))".format(listname, uatype, name))
        else:
            self.write("{}.append({}.to_binary(}))".format(listname, name))
            return

    def get_default_value(self, field):
        if field.uatype in self.model.enum_list:
            enum = self.model.get_enum(field.uatype)
            return enum.name + "(0)"
        if field.uatype in ("String"):
            return None 
        elif field.uatype in ("ByteString", "CharArray", "Char"):
            return None 
        elif field.uatype in ("Boolean"):
            return "True"
        elif field.uatype in ("DateTime"):
            return "datetime.utcnow()"
        elif field.uatype in ("Int8", "Int16", "Int32", "Int64", "UInt8", "UInt16", "UInt32", "UInt64", "Double", "Float", "Byte"):
            return 0
        elif field.uatype in ("ExtensionObject"):
            return "None"
        else:
            return field.uatype + "()"

if __name__ == "__main__":
    import generate_model as gm
    xmlpath = "Opc.Ua.Types.bsd"
    protocolpath = "../opcua/ua/uaprotocol_auto.py"
    p = gm.Parser(xmlpath)
    model = p.parse()
    gm.add_basetype_members(model)
    gm.add_encoding_field(model)
    gm.remove_duplicates(model)
    gm.remove_vector_length(model)
    gm.split_requests(model)
    gm.fix_names(model)
    c = CodeGenerator(model, protocolpath)
    c.run()
