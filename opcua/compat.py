""" Module with Python 2/3 compatibility functions. """

def with_metaclass(Meta, *bases):
    """ Allows to specify metaclasses in Python 2 and 3 compatible ways.
        Might not allow 
    """
    return Meta("Meta", bases, {})
