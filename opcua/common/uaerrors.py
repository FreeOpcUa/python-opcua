"""
Define exceptions to be raised at various places in the stack
"""


class UaError(RuntimeError):
    pass


class UaStatusCodeError(UaError):
    pass


class UaStringParsingError(UaError):
    pass
