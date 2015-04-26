
import os.path

import opcua

from opcua.standard_address_space_part3 import create_standard_address_space_Part3
from opcua.standard_address_space_part4 import create_standard_address_space_Part4
from opcua.standard_address_space_part5 import create_standard_address_space_Part5
from opcua.standard_address_space_part8 import create_standard_address_space_Part8
from opcua.standard_address_space_part9 import create_standard_address_space_Part9
from opcua.standard_address_space_part10 import create_standard_address_space_Part10
from opcua.standard_address_space_part11 import create_standard_address_space_Part11
from opcua.standard_address_space_part13 import create_standard_address_space_Part13


def fill_address_space(aspace):
    create_standard_address_space_Part3(aspace)
    create_standard_address_space_Part4(aspace)
    create_standard_address_space_Part5(aspace)
    create_standard_address_space_Part8(aspace)
    create_standard_address_space_Part9(aspace)
    create_standard_address_space_Part10(aspace)
    create_standard_address_space_Part11(aspace)
    create_standard_address_space_Part13(aspace)

def fill_address_space_from_disk(aspace):
    dirname = os.path.dirname(opcua.__file__)
    path = os.path.join(dirname, "binary_address_space.pickle")
    aspace.load(path)


