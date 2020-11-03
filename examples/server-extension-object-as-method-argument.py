from opcua import Server, ua, uamethod

@uamethod
def callback(parent, in_extobj):

    out_extobj = ua.uaprotocol_auto.AxisInformation() # get new instanace of AxisInformation
    out_extobj.EngineeringUnits = in_extobj.EngineeringUnits
    out_extobj.EURange.Low = in_extobj.EURange.Low
    out_extobj.EURange.High = in_extobj.EURange.High
    out_extobj.Title = in_extobj.Title
    out_extobj.AxisScaleType = in_extobj.AxisScaleType
    out_extobj.AxisSteps = in_extobj.AxisSteps

    axis_info.set_value(out_extobj) #write values to variable
    
    return [
        out_extobj
    ]

server = Server()
server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")
server.set_security_policy([ua.SecurityPolicyType.NoSecurity])

obj = server.get_objects_node()
idx = server.register_namespace("http://examples.freeopcua.github.io")

server.load_type_definitions()

inarg_extobj = ua.Argument()
inarg_extobj.Name = "In"
inarg_extobj.DataType = ua.NodeId(12079, 0)
inarg_extobj.ValueRank = -1
inarg_extobj.ArrayDimensions = []
inarg_extobj.Description = ua.LocalizedText("Wanted AxisInformation")

outarg_extobj = ua.Argument()
outarg_extobj.Name = "Out"
outarg_extobj.DataType = ua.NodeId(12079, 0)
outarg_extobj.ValueRank = -1
outarg_extobj.ArrayDimensions = []
outarg_extobj.Description = ua.LocalizedText("Actual AxisInformation")

method_parent = obj.add_object(idx, "Methods")
method_node = method_parent.add_method(
    idx, 
    "SetAxisInformation", 
    callback, 
    [
        inarg_extobj
    ], 
    [
        outarg_extobj
    ]
)

#add a variable of type AxisInformation
axis_info = obj.add_variable(idx, "AxisInformation", ua.uaprotocol_auto.AxisInformation(), varianttype=ua.VariantType.ExtensionObject)

if  __name__ == "__main__":
    server.start()