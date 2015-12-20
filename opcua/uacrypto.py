import os

from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


def load_certificate(path):
    _, ext = os.path.splitext(path)
    with open(path, "br") as f:
        if ext == ".pem":
            return x509.load_pem_x509_certificate(f.read(), default_backend())
        else:
            return x509.load_der_x509_certificate(f.read(), default_backend())


def x509_from_der(data):
    if not data:
        return None
    return x509.load_der_x509_certificate(data, default_backend())


def load_private_key(path):
    with open(path, "br") as f:
        return serialization.load_pem_private_key(f.read(), password=None, backend=default_backend())


def der_from_x509(certificate):
    if certificate is None:
        return b""
    return certificate.public_bytes(serialization.Encoding.DER)


def sign_sha1(private_key, data):
    signer = private_key.signer(
        padding.PKCS1v15(),
        hashes.SHA1()
    )
    signer.update(data)
    return signer.finalize()


def encrypt_basic256(public_key, data):
    ciphertext = public_key.encrypt(
        data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None)
    )
    return ciphertext


if __name__ == "__main__":
    # Convert from PEM to DER
    cert = load_certificate("../examples/server_cert.pem")
    #rsa_pubkey = pubkey_from_dercert(der)
    rsa_privkey = load_private_key("../examples/mykey.pem")
    
    from IPython import embed
    embed()
