import unittest
import logging
import sys
sys.path.insert(0, "..")
sys.path.insert(0, ".")
try:
    from opcua.crypto import uacrypto
    CRYPTOGRAPHY_AVAILABLE = True
except ImportError:
    print("WARNING: CRYPTO NOT AVAILABLE, CRYPTO TESTS DISABLED!!")
    CRYPTOGRAPHY_AVAILABLE = False




from tests_cmd_lines import TestCmdLines
from tests_server import TestServer, TestServerCaching
from tests_client import TestClient
from tests_unit import TestUnit
from tests_history import TestHistory, TestHistorySQL, TestHistoryLimits, TestHistorySQLLimits
from tests_history import TestHistorySQL
if CRYPTOGRAPHY_AVAILABLE:
    from tests_crypto_connect import TestCryptoConnect


if __name__ == '__main__':
    logging.basicConfig(level=logging.WARNING)
    #l = logging.getLogger("opcua.server.internal_subscription")
    #l.setLevel(logging.DEBUG)
    #l = logging.getLogger("opcua.server.internal_server")
    #l.setLevel(logging.DEBUG)

    unittest.main(verbosity=3)
