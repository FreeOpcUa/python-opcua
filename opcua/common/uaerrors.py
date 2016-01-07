"""
Define exceptions to be raised at various places in the stack
"""


class UAError(RuntimeError):
    pass


class UAStatusCodeError(UAError):
    pass


class UAStringParsingError(UAError):
    pass
