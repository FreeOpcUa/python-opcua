def extensionobject_from_binary(data):
    """
    Convert binary-coded ExtensionObject to a Python object.
    Returns an object, or None if TypeId is zero
    """
    TypeId = NodeId.from_binary(data)
    Encoding = ord(data.read(1))
    if Encoding & (1 << 0):
        Body = unpack_bytes(data)
    if TypeId.Identifier == 0:
        return None
    klass = ExtensionClasses[TypeId.Identifier]
    return klass.from_binary(Buffer(Body))

def extensionobject_to_binary(obj):
    """
    Convert Python object to binary-coded ExtensionObject.
    If obj is None, convert to empty ExtensionObject (TypeId = 0, no Body).
    Returns a binary string
    """
    TypeId = NodeId()
    Encoding = 0
    Body = None
    if obj is not None:
        TypeId = FourByteNodeId(getattr(ObjectIds, "{}_Encoding_DefaultBinary".format(obj.__class__.__name__)))
        Encoding |= (1 << 0)
        Body = obj.to_binary()
    packet = []
    packet.append(TypeId.to_binary())
    packet.append(uatype_UInt8.pack(Encoding))
    if Body:
        packet.append(pack_bytes(Body))
    return b''.join(packet)
