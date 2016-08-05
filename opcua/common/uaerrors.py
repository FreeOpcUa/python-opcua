"""
Define exceptions to be raised at various places in the stack
"""

class UaError(RuntimeError):
    pass


class UaStatusCodeError(UaError):
    """
    This exception is raised when a bad status code is encountered.

    It exposes the status code number in the `code' property, so the
    user can distinguish between the different status codes and maybe
    handle some of them.

    The list of status error codes can be found in opcua.ua.status_codes.
    """
    def __init__(self, code):
        """
        :param code: The code of the exception. (Should be a number.)
        """
        UaError.__init__(self, code)

    def __str__(self):
        # import here to avoid circular import problems
        import opcua.ua.status_codes as status_codes

        return "{1}({0})".format(*status_codes.get_name_and_doc(self.code))

    @property
    def code(self):
        """
        The code of the status error.
        """
        return self.args[0]

class UaStringParsingError(UaError):
    pass
