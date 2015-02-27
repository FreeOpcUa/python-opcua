#temporary hack
from IPython import embed
import sys
sys.path.append("../../schemas/")

import struct

import  generate_protocol as gp

IgnoredEnums = ["NodeIdType"]
IgnoredStructs = ["NodeId", "ExpandedNodeId", "FilterOperand"]

class CodeGenerator(object):
    def __init__(self, model, output):
        self.model = model
        self.output_path = output
        self.indent = "    "
        self.iidx = 0 #indent index

    def run(self):
        print("Writting python protocol code to ", self.output_path)
        self.output_file = open(self.output_path, "w")
        self.make_header()
        for enum in self.model.enums:
            if not enum.name in IgnoredEnums:
                self.generate_enum_code(enum)
        for struct in self.model.structs:
            if not struct.name in IgnoredStructs:
                self.generate_struct_code(struct)

    def write(self, *args):
        args = list(args)
        args.insert(0, self.indent * self.iidx)
        line = " ".join(args) 
        self.output_file.write(line[1:] + "\n")

    def make_header(self):
        self.write("'''")
        self.write("Autogenerate code from xml spec")
        self.write("'''")
        self.write("")
        self.write("import struct")
        self.write("")
        self.write("from .uatypes import *")
        self.write("from .object_ids import ObjectIds")
        self.write("")
        self.write("")

    def generate_enum_code(self, enum):
        self.write("")
        self.write("class {}(object):".format(enum.name))
        self.iidx = 1
        for val in enum.values:
            self.write("{} = {}".format(val.name, val.value))
        self.iidx = 0

    def generate_struct_code(self, obj):
        self.write("")
        self.iidx = 0
        self.write("class {}(object):".format(obj.name))
        self.iidx += 1
        self.write("def __init__(self):")
        self.iidx += 1
        for field in obj.fields:
            if field.uatype == obj.name: #help!!! selv referencing class
                self.write("self.{} = None".format(field.name))
            elif field.name == "TypeId" and ( obj.name.endswith("Request") or obj.name.endswith("Response")):
                #self.write("nodeid = NodeId()")
                #self.write("fourbyte = FourByteNodeId()")
                #self.write("fourbyte.NamespaceIndex = 0")
                #self.write("fourbyte.Identifier = ObjectIds.{}".format(obj.name +"_Encoding_DefaultBinary"))
                #self.write("nodeid.FourByte = fourbyte")

                self.write("self.TypeId = NodeId(0, ObjectIds.{}, NodeIdType.FourByte)".format(obj.name +"_Encoding_DefaultBinary"))
                #self.write("self.{} = nodeid".format(field.name))
            else:
                self.write("self.{} = {}".format(field.name, "[]" if field.length else self.get_default_value(field)))
            #if field.name == "RequestHeader":
                #self.write("self.RequestHeader.TypeId = NodeId(0, ObjectIds.{}, NodeIdType.FourByte)".format(obj.name +"_Encoding_DefaultBinary"))
        self.iidx = 1

        #serialize code
        self.write("")
        self.write("def to_binary(self):")
        self.iidx += 1

        #hack for self referencing classes
        for field in obj.fields:
            if field.uatype == obj.name: #help!!! selv referencing class
                self.write("if self.{name} is None: self.{name} = {uatype}()".format(name=field.name, uatype=field.uatype))

        self.write("packet = []")
        #if obj.is_extension_object():
            #self.write("body = []")
        #self.write("tmp = packet")
        for field in obj.fields:
            if field.switchfield:
                if field.switchvalue:
                    bit = obj.bits[field.switchfield]
                    #self.write("if self.{}: self.{} |= (value << {})".format(field.name, field.switchfield, field.switchvalue))
                    mask = '0b' + '0' *(8-bit.length) + '1' * bit.length
                    self.write("others = self.{} & {}".format(bit.container, mask))
                    self.write("if self.{}: self.{} = ( {} | others )".format(field.name, bit.container, field.switchvalue))
                else:
                    bit = obj.bits[field.switchfield]
                    self.write("if self.{}: self.{} |= (1 << {})".format(field.name, bit.container, bit.idx))
        iidx = self.iidx
        for idx, field in enumerate(obj.fields):
            #if field.name == "Body" and idx <= (len(obj.fields)-1):
                #self.write("tmp = packet")
                #continue
            self.iidx = iidx
            switch = ""
            fname = "self." + field.name
            if field.switchfield:
                self.write("if self.{}: ".format(field.name))
                self.iidx += 1
            if field.length:
                self.write("packet.append(struct.pack('<i', len(self.{})))".format(field.name))
                self.write("for fieldname in self.{}:".format(field.name))
                fname = "fieldname"
                self.iidx += 1
            if field.uatype in ("CharArray", "ByteString"):
                self.write("packet.append(pack_bytes({name}))".format(name=fname))
            elif field.uatype == "String":
                #self.write("packet.append(struct.pack('<i', len({})))".format(fname))
                #self.write("packet.append(struct.pack('<{{}}s'.format(len({name})), {name}.encode()))".format(name=fname))
                self.write("packet.append(pack_string({name}))".format(name=fname))
            elif field.is_native_type() or field.uatype in self.model.enum_list:
                self.write("fmt = '<{}'".format(self.to_fmt(field)))
                self.write("packet.append(struct.pack(fmt, {name}))".format(name=fname))
            else:
                self.write("packet.append({}.to_binary())".format(fname))
            if field.length:
                self.iidx -= 1
        self.iidx = 2
        #if obj.is_extension_object():
            #self.write("body = b''.join(tmp)")
            #self.write("packet.append(struct.pack('<i', len(body)))")
            #self.write("packet.append(body)")
        self.write("return b''.join(packet)")
        self.write("")

        self.iidx = 1
        #deserialize
        self.write("@staticmethod")
        self.write("def from_binary(data):")
        self.iidx += 1 
        iidx = self.iidx
        self.write("obj = {}()".format(obj.name))
        for idx, field in enumerate(obj.fields):
            self.iidx = iidx
            #if field.name == "Body" and idx <= (len(obj.fields)-1):
                #self.write("bodylength = struct.unpack('<i', data.read(4))[0]")
                #continue
            if field.switchfield:
                bit = obj.bits[field.switchfield]
                if field.switchvalue:
                    mask = '0b' + '0' *(8-bit.length) + '1' * bit.length
                    self.write("val = obj.{} & {}".format(bit.container, mask))
                    self.write("if val == {}:".format(bit.idx))
                    #self.write("if self.{} & (1 << {}):".format(field.switchfield, field.switchvalue))
                else:
                    self.write("if obj.{} & (1 << {}):".format(bit.container, bit.idx))
                self.iidx += 1
            if field.length:
                self.write("length = struct.unpack('<i', data.read(4))[0]")
                self.write("if length != -1:")
                self.iidx += 1
                self.write("for i in range(0, length):")
                self.iidx += 1
            if field.uatype in ("CharArray", "ByteString"):
                self.write("obj.{name} = unpack_bytes(data)".format(name=field.name))
            elif field.uatype == "String":
                self.write("obj.{name} = unpack_string(data)".format(name=field.name))
            elif field.is_native_type() or field.uatype in self.model.enum_list:
                fmt =  self.to_fmt(field)
                self.write("fmt = '<{}'".format(fmt))
                self.write("fmt_size = {}".format(struct.calcsize(fmt)))
                self.write("obj.{name} = struct.unpack(fmt, data.read(fmt_size))[0]".format(name=field.name))
            else:
                self.write("obj.{} = {}.from_binary(data)".format(field.name, field.uatype))
        self.iidx = 2
        self.write("return obj")
        
        #__str__
        self.iidx = 1
        self.write("")
        self.write("def __str__(self):")
        self.iidx += 1
        #ObjectName(fieldnam:fieldvalue, fieldname:fieldvalue)
        #'ObjectName(fiel)dname:' + fieldvalye + ',fieldname:' ))+ value + ',fieldname:' + value + ')'
        tmp = ["'{name}:' + str(self.{name})".format(name=f.name ) for f in obj.fields]
        tmp = " + ', '  + \\\n             ".join(tmp)
        self.write("return '{}(' + {} + ')'".format(obj.name, tmp))
        self.iidx -= 1
        self.write("")
        self.write("__repr__ = __str__")







        self.iix = 0

    
    def get_default_value(self, field):
        if field.uatype in self.model.enum_list:
            return 0
        if field.uatype in ("String"):
            return "''"
        elif field.uatype in ("ByteString", "CharArray", "Char"):
            return "b''"
        elif field.uatype in ("Int8", "Int16", "Int32", "Int64", "UInt8", "UInt16", "UInt32", "UInt64", "Boolean", "Double", "Float", "Byte"):
            return 0
        else:
            return field.uatype + "()"

    def to_fmt(self, obj):
        if obj.uatype == "String":
            return "s"
        elif obj.uatype == "CharArray":
            return "s"
        elif obj.uatype == "Char":
            return "s"
        elif obj.uatype == "SByte":
            return "B"
        elif obj.uatype == "Int8":
            return "b"
        elif obj.uatype == "Int16":
            return "h"
        elif obj.uatype == "Int32":
            return "i"
        elif obj.uatype == "Int64":
            return "q"
        elif obj.uatype == "UInt8":
            return "B"
        elif obj.uatype == "UInt16":
            return "H"
        elif obj.uatype == "UInt32":
            return "I"
        elif obj.uatype == "UInt64":
            return "Q"
        elif obj.uatype == "DateTime":
            return "d"
        elif obj.uatype == "Boolean":
            return "?"
        elif obj.uatype == "Double":
            return "d"
        elif obj.uatype == "Float":
            return "f"
        elif obj.uatype == "Byte":
            return "B"
        elif obj.uatype in ("6", "8"):
            return "B"
        elif obj.uatype == "32": 
            return "I"
        else:
            field = self.model.get_enum(obj.uatype)
            return self.to_fmt(field)
            #print("Error unknown uatype: ", obj.uatype)




def fix_names(model):
    for s in model.enums:
        for f in s.values:
            if f.name == "None":
                f.name = "None_"


if __name__ == "__main__":
    xmlpath = "Opc.Ua.Types.bsd"
    protocolpath = "../opcua/uaprotocol_auto.py"
    p = gp.Parser(xmlpath)
    model = p.parse()
    #gp.reorder_extobjects(model)
    gp.add_basetype_members(model)
    gp.add_encoding_field(model)
    gp.remove_duplicates(model)
    gp.remove_vector_length(model)
    gp.remove_body_length(model)
    gp.split_requests(model)
    fix_names(model)
    c = CodeGenerator(model, protocolpath)
    c.run()


