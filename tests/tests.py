import unittest
import logging
import sys
sys.path.insert(0, "..")
sys.path.insert(0, ".")



from tests_cmd_lines import TestCmdLines
from tests_server import TestServer
from tests_client import TestClient
from tests_unit import Unit
from tests_crypto_connect import TestCryptoConnect


if __name__ == '__main__':
    logging.basicConfig(level=logging.WARNING)

    unittest.main(verbosity=3)
