from opcua import ua, Server
from opcua.crypto import uacrypto

import time

import sys
sys.path.insert(0, "..")


def simple_certificate_manager(isession, certificate, signature):
    """
    Simple certificate manager that only allows clients that are authorized.
    To simplify this example, we use the same certificate on the both side.
    """
    server_certificate = uacrypto.der_from_x509(uacrypto.load_certificate('certificate-example.der'))
    trusted_certificate = uacrypto.load_certificate('certificate-example.der')

    if uacrypto.der_from_x509(trusted_certificate) == certificate:
        data = server_certificate + isession.nonce
        try:
            uacrypto.verify_sha256(trusted_certificate, data, signature)
            return True
        except:
            return False

    return False


if __name__ == "__main__":

    # setup our server
    server = Server()
    server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")

    # setup our own namespace, not really necessary but should as spec
    uri = "http://examples.freeopcua.github.io"
    idx = server.register_namespace(uri)

    # load server certificate and private key. This enables endpoints
    # with signing and encryption.
    server.load_certificate("certificate-example.der")
    server.load_private_key("private-key-example.pem")

    server.certificate_manager.set_certificate_manager(simple_certificate_manager)

    # starting
    server.start()

    try:
        while True:
            time.sleep(5)
    finally:
        server.stop()
