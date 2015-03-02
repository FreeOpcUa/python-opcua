#temporary hack
from IPython import embed

import struct

import  generate_model as gm

IgnoredEnums = ["NodeIdType"]
IgnoredStructs = ["QualifiedName", "NodeId", "ExpandedNodeId", "FilterOperand", "Variant"]

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
            if struct.name in IgnoredStructs:
                continue
            if struct.name.endswith("Node") or struct.name.endswith("NodeId"):
                continue
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
        self.write("'''")
        self.write(enum.doc)
        self.write("'''")
        for val in enum.values:
            self.write("{} = {}".format(val.name, val.value))
        self.iidx = 0

    def generate_struct_code(self, obj):
        self.write("")
        self.iidx = 0
        self.write("class {}(object):".format(obj.name))
        self.iidx += 1
        self.write("'''")
        self.write(obj.doc)
        self.write("'''")
        self.write("def __init__(self):")
        self.iidx += 1

        #hack extension object stuff
        extobj_hack = False 
        if "BodyLength" in [f.name for f in obj.fields]:
            extobj_hack = True

        for field in obj.fields:
            if extobj_hack and field.name == "Encoding":
                self.write("self.Encoding = 1")
            elif field.uatype == obj.name: #help!!! selv referencing class
                self.write("self.{} = None".format(field.name))
            elif not obj.name in ("ExtensionObject") and field.name == "TypeId" :# and ( obj.name.endswith("Request") or obj.name.endswith("Response")):
                self.write("self.TypeId = FourByteNodeId(ObjectIds.{}_Encoding_DefaultBinary)".format(obj.name))
            else:
                self.write("self.{} = {}".format(field.name, "[]" if field.length else self.get_default_value(field)))
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
        if extobj_hack:
            self.write("body = []")
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
        listname = "packet"
        for idx, field in enumerate(obj.fields):
            #if field.name == "Body" and idx <= (len(obj.fields)-1):
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
                self.write("{}.append(struct.pack('<i', len(self.{})))".format(listname, field.name))
                self.write("for fieldname in self.{}:".format(field.name))
                fname = "fieldname"
                self.iidx += 1
            if field.is_native_type():
                self.write("{}.append(pack_uatype('{}', {}))".format(listname, field.uatype, fname))
            elif field.uatype in self.model.enum_list:
                uatype = self.model.get_enum(field.uatype).uatype
                self.write("{}.append(pack_uatype('{}', {}))".format(listname, uatype, fname))
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
                else:
                    self.write("if obj.{} & (1 << {}):".format(bit.container, bit.idx))
                self.iidx += 1
            array = False
            if field.is_native_type():
                if field.length:
                    self.write("obj.{} = unpack_uatype_array('{}', data)".format(field.name, field.uatype))
                else:
                    self.write("obj.{} = unpack_uatype('{}', data)".format(field.name, field.uatype))
            elif field.uatype in self.model.enum_list:
                uatype = self.model.get_enum(field.uatype).uatype
                self.write("obj.{} = unpack_uatype('{}', data)".format(field.name, uatype))
            else:
                if field.length:
                    self.write("length = struct.unpack('<i', data.read(4))[0]")
                    self.write("if length != -1:")
                    self.iidx += 1
                    self.write("for i in range(0, length):")
                    self.iidx += 1
                    self.write("obj.{}.append({}.from_binary(data))".format(field.name, field.uatype))
                else:
                    self.write("obj.{} = {}.from_binary(data)".format(field.name, field.uatype))

        self.iidx = 2
        self.write("return obj")
        
        #__str__
        self.iidx = 1
        self.write("")
        self.write("def __str__(self):")
        self.iidx += 1
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
        elif field.uatype in ("Boolean"):
            return "True"
        elif field.uatype in ("Int8", "Int16", "Int32", "Int64", "UInt8", "UInt16", "UInt32", "UInt64", "Double", "Float", "Byte"):
            return 0
        else:
            return field.uatype + "()"



def fix_names(model):
    for s in model.enums:
        for f in s.values:
            if f.name == "None":
                f.name = "None_"


if __name__ == "__main__":
    xmlpath = "Opc.Ua.Types.bsd"
    protocolpath = "../opcua/uaprotocol_auto.py"
    p = gm.Parser(xmlpath)
    model = p.parse()
    gm.add_basetype_members(model)
    gm.add_encoding_field(model)
    gm.remove_duplicates(model)
    gm.remove_vector_length(model)
    gm.split_requests(model)
    fix_names(model)
    c = CodeGenerator(model, protocolpath)
    c.run()


