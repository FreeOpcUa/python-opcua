import unittest
import opcua.ua.uaerrors as uaerrors
from opcua.ua.uaerrors import UaStatusCodeError

class TestUaErrors(unittest.TestCase):
    status_code_bad_internal = 0x80020000
    status_code_unknown = "Definitely Not A Status Code"

    def setUp(self):
        self.direct = uaerrors.BadInternalError()
        self.indirect = UaStatusCodeError(self.status_code_bad_internal)
        self.unknown = UaStatusCodeError(self.status_code_unknown)

    def test_subclass_selection(self):
        self.assertIs(type(self.direct), uaerrors.BadInternalError)
        self.assertIs(type(self.indirect), uaerrors.BadInternalError)
        self.assertIs(type(self.unknown), UaStatusCodeError)

    def test_code(self):
        self.assertEqual(self.direct.code, self.status_code_bad_internal)
        self.assertEqual(self.indirect.code, self.status_code_bad_internal)
        self.assertEqual(self.unknown.code, self.status_code_unknown)

    def test_string_repr(self):
        self.assertIn("BadInternal", str(self.direct))
        self.assertIn("BadInternal", str(self.indirect))
