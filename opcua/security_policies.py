# -*- coding: utf-8 -*-

from opcua.uaprotocol import SecurityPolicy, MessageSecurityMode, CryptographyNone
try:
    from cryptography import x509, exceptions
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives.asymmetric import padding
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
    from cryptography.hazmat.primitives import hashes,serialization,hmac
    cryptography_available = True
except ImportError:
    cryptography_available = False


def require_cryptography(obj):
    if not cryptography_available:
        raise Exception("Can't use {}, cryptography module is not installed".format(obj.__class__.__name__))


class Cryptography(CryptographyNone):
    """
    Security policy: Sign or SignAndEncrypt
    """
    def __init__(self, mode=MessageSecurityMode.Sign):
        self.Signer = None
        self.Verifier = None
        self.Encryptor = None
        self.Decryptor = None
        assert(mode in (MessageSecurityMode.Sign, MessageSecurityMode.SignAndEncrypt))
        self.is_encrypted = (mode == MessageSecurityMode.SignAndEncrypt)

    def plain_block_size(self):
        """
        Size of plain text block for block cipher.
        """
        if self.is_encrypted:
            return self.Encryptor.plain_block_size()
        return 1

    def encrypted_block_size(self):
        """
        Size of encrypted text block for block cipher.
        """
        if self.is_encrypted:
            return self.Encryptor.encrypted_block_size()
        return 1

    def padding(self, size):
        """
        Create padding for a block of given size.
        plain_size = size + len(padding) + signature_size()
        plain_size = N * plain_block_size()
        """
        if not self.is_encrypted:
            return b''
        rem = (size + self.signature_size() + 1) % self.Encryptor.plain_block_size()
        if rem != 0:
            rem = self.Encryptor.plain_block_size() - rem
        return bytes(bytearray([rem])) * (rem + 1)

    def min_padding_size(self):
        if self.is_encrypted:
            return 1
        return 0

    def signature_size(self):
        return self.Signer.signature_size()

    def signature(self, data):
        return self.Signer.signature(data)

    def vsignature_size(self):
        return self.Verifier.signature_size()

    def verify(self, data, sig):
        self.Verifier.verify(data, sig)

    def encrypt(self, data):
        if self.is_encrypted:
            assert(len(data) % self.Encryptor.plain_block_size() == 0)
            return self.Encryptor.encrypt(data)
        return data

    def decrypt(self, data):
        if self.is_encrypted:
            #assert(len(data) % self.Decryptor.encrypted_block_size() == 0)
            return self.Decryptor.decrypt(data)
        return data

    def remove_padding(self, data):
        if self.is_encrypted:
            pad_size = bytearray(data[-1:])[0] + 1
            return data[:-pad_size]
        return data


class SignerRsa:
    def __init__(self, client_pk):
        require_cryptography(self)
        self.client_pk = serialization.load_pem_private_key(client_pk, None, default_backend())
        self.key_size = self.client_pk.key_size // 8

    def signature_size(self):
        assert(len(self.signature(b'')) == self.key_size)
        return self.key_size

    def signature(self, data):
        s = self.client_pk.signer(padding.PKCS1v15(), hashes.SHA1())
        s.update(data)
        return s.finalize()

class VerifierRsa:
    def __init__(self, server_cert):
        require_cryptography(self)
        self.server_cert = x509.load_der_x509_certificate(server_cert, default_backend())
        self.key_size = self.server_cert.public_key().key_size // 8

    def signature_size(self):
        return self.key_size

    def verify(self, data, signature):
        verifier = self.server_cert.public_key().verifier(signature, padding.PKCS1v15(), hashes.SHA1())
        verifier.update(data)
        verifier.verify()


class EncryptorRsa:
    def __init__(self, server_cert, padding, padding_size):
        require_cryptography(self)
        self.server_cert = x509.load_der_x509_certificate(server_cert, default_backend())
        self.key_size = self.server_cert.public_key().key_size // 8
        self.padding = padding
        self.padding_size = padding_size

    def plain_block_size(self):
        return self.key_size - self.padding_size

    def encrypted_block_size(self):
        return self.key_size

    def encrypt(self, data):
        e = b''
        for i in range(0, len(data), self.plain_block_size()):
            e += self.server_cert.public_key().encrypt(data[i:i+self.plain_block_size()], self.padding)
        return e

class DecryptorRsa:
    def __init__(self, client_pk, padding, padding_size):
        require_cryptography(self)
        self.client_pk = serialization.load_pem_private_key(client_pk, None, default_backend())
        self.key_size = self.client_pk.key_size // 8
        self.padding = padding
        self.padding_size = padding_size

    def plain_block_size(self):
        return self.key_size - self.padding_size

    def encrypted_block_size(self):
        return self.key_size

    def decrypt(self, data):
        d = b''
        for i in range(0, len(data), self.encrypted_block_size()):
            d += self.client_pk.decrypt(data[i:i+self.encrypted_block_size()], self.padding)
        return d


class SignerAesCbc:
    def __init__(self, key):
        require_cryptography(self)
        self.key = key

    def signature_size(self):
        return hashes.SHA1.digest_size

    def signature(self, data):
        h = hmac.HMAC(self.key, hashes.SHA1(), backend=default_backend())
        h.update(data)
        return h.finalize()


class VerifierAesCbc:
    def __init__(self, key):
        require_cryptography(self)
        self.key = key

    def signature_size(self):
        return hashes.SHA1.digest_size

    def verify(self, data, signature):
        h = hmac.HMAC(self.key, hashes.SHA1(), backend=default_backend())
        h.update(data)
        expected = h.finalize()
        if signature != expected:
            raise exceptions.InvalidSignature


class EncryptorAesCbc:
    def __init__(self, key, iv):
        require_cryptography(self)
        self.cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

    def plain_block_size(self):
        return self.cipher.algorithm.key_size // 8

    def encrypted_block_size(self):
        return self.cipher.algorithm.key_size // 8

    def encrypt(self, data):
        encryptor = self.cipher.encryptor()
        return encryptor.update(data) + encryptor.finalize()


class DecryptorAesCbc:
    def __init__(self, key, iv):
        require_cryptography(self)
        self.cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

    def plain_block_size(self):
        return self.cipher.algorithm.key_size // 8

    def encrypted_block_size(self):
        return self.cipher.algorithm.key_size // 8

    def decrypt(self, data):
        decryptor = self.cipher.decryptor()
        return decryptor.update(data) + decryptor.finalize()


def hash_hmac(a, b):
    h = hmac.HMAC(a, hashes.SHA1(), backend=default_backend())
    h.update(b)
    return h.finalize()

def p_sha1(key, body, sizes=()):
    size = 0
    for s in sizes:
        size += s
    result = b''
    accum = body
    while len(result) < size:
        accum = hash_hmac(key, accum)
        result += hash_hmac(key, accum + body)
    parts = []
    for s in sizes:
        parts.append(result[:s])
        result = result[s:]
    return tuple(parts)


class SecurityPolicyBasic128Rsa15(SecurityPolicy):
    """
    Security Basic 128Rsa15
    A suite of algorithms that uses RSA15 as Key-Wrap-algorithm and 128-Bit for encryption algorithms.
    -> SymmetricSignatureAlgorithm – HmacSha1 – (http://www.w3.org/2000/09/xmldsig#hmac-sha1).
    -> SymmetricEncryptionAlgorithm – Aes128 – (http://www.w3.org/2001/04/xmlenc#aes128-cbc).
    -> AsymmetricSignatureAlgorithm – RsaSha1 – (http://www.w3.org/2000/09/xmldsig#rsa-sha1).
    -> AsymmetricKeyWrapAlgorithm – KwRsa15 – (http://www.w3.org/2001/04/xmlenc#rsa-1_5).
    -> AsymmetricEncryptionAlgorithm – Rsa15 – (http://www.w3.org/2001/04/xmlenc#rsa-1_5).
    -> KeyDerivationAlgorithm – PSha1 – (http://docs.oasis-open.org/ws-sx/ws-secureconversation/200512/dk/p_sha1).
    -> DerivedSignatureKeyLength – 128 (16 bytes)
    -> MinAsymmetricKeyLength – 1024 (128 bytes)
    -> MaxAsymmetricKeyLength – 2048 (256 bytes)
    -> CertificateSignatureAlgorithm – Sha1

    If a certificate or any certificate in the chain is not signed with a hash that is Sha1 or stronger then the certificate shall be rejected.
    """
    URI = "http://opcfoundation.org/UA/SecurityPolicy#Basic128Rsa15"
    signature_key_size = 16
    symmetric_key_size = 16

    def __init__(self, server_cert, client_cert, client_pk, mode=MessageSecurityMode.SignAndEncrypt):
        require_cryptography(self)
        self.asymmetric_cryptography = Cryptography(MessageSecurityMode.SignAndEncrypt)
        self.asymmetric_cryptography.Signer = SignerRsa(client_pk)
        self.asymmetric_cryptography.Verifier = VerifierRsa(server_cert)
        self.asymmetric_cryptography.Encryptor = EncryptorRsa(server_cert, padding.PKCS1v15(), 11)
        self.asymmetric_cryptography.Decryptor = DecryptorRsa(client_pk, padding.PKCS1v15(), 11)
        self.symmetric_cryptography = Cryptography(mode)
        self.Mode = mode
        self.server_certificate = server_cert
        self.client_certificate = client_cert

    def make_symmetric_key(self, n1, n2):
        (sigkey, key, iv) = p_sha1(n2, n1, (self.signature_key_size, self.symmetric_key_size, 16))
        self.symmetric_cryptography.Signer = SignerAesCbc(sigkey)
        self.symmetric_cryptography.Encryptor = EncryptorAesCbc(key, iv)
        (sigkey2, key2, iv2) = p_sha1(n1, n2, (self.signature_key_size, self.symmetric_key_size, 16))
        self.symmetric_cryptography.Verifier = VerifierAesCbc(sigkey2)
        self.symmetric_cryptography.Decryptor = DecryptorAesCbc(key2, iv2)


def oaep():
    return padding.OAEP(padding.MGF1(hashes.SHA1()), hashes.SHA1(), None)


class SecurityPolicyBasic256(SecurityPolicy):
    """
    Security Basic 256
    A suite of algorithms that are for 256-Bit encryption, algorithms include:
    -> SymmetricSignatureAlgorithm – HmacSha1 – (http://www.w3.org/2000/09/xmldsig#hmac-sha1).
    -> SymmetricEncryptionAlgorithm – Aes256 – (http://www.w3.org/2001/04/xmlenc#aes256-cbc).
    -> AsymmetricSignatureAlgorithm – RsaSha1 – (http://www.w3.org/2000/09/xmldsig#rsa-sha1).
    -> AsymmetricKeyWrapAlgorithm – KwRsaOaep – (http://www.w3.org/2001/04/xmlenc#rsa-oaep-mgf1p).
    -> AsymmetricEncryptionAlgorithm – RsaOaep – (http://www.w3.org/2001/04/xmlenc#rsa-oaep).
    -> KeyDerivationAlgorithm – PSha1 – (http://docs.oasis-open.org/ws-sx/ws-secureconversation/200512/dk/p_sha1).
    -> DerivedSignatureKeyLength – 192 (24 bytes)
    -> MinAsymmetricKeyLength – 1024 (128 bytes)
    -> MaxAsymmetricKeyLength – 2048 (256 bytes)
    -> CertificateSignatureAlgorithm – Sha1

    If a certificate or any certificate in the chain is not signed with a hash that is Sha1 or stronger then the certificate shall be rejected.
    """
    URI = "http://opcfoundation.org/UA/SecurityPolicy#Basic256"
    signature_key_size = 24
    symmetric_key_size = 32

    def __init__(self, server_cert, client_cert, client_pk, mode=MessageSecurityMode.SignAndEncrypt):
        require_cryptography(self)
        self.asymmetric_cryptography = Cryptography(MessageSecurityMode.SignAndEncrypt)
        self.asymmetric_cryptography.Signer = SignerRsa(client_pk)
        self.asymmetric_cryptography.Verifier = VerifierRsa(server_cert)
        self.asymmetric_cryptography.Encryptor = EncryptorRsa(server_cert, oaep(), 42)
        self.asymmetric_cryptography.Decryptor = DecryptorRsa(client_pk, oaep(), 42)
        self.symmetric_cryptography = Cryptography(mode)
        self.Mode = mode
        self.server_certificate = server_cert
        self.client_certificate = client_cert

    def make_symmetric_key(self, n1, n2):
        (sigkey, key, iv) = p_sha1(n2, n1, (self.signature_key_size, self.symmetric_key_size, 16))
        self.symmetric_cryptography.Signer = SignerAesCbc(sigkey)
        self.symmetric_cryptography.Encryptor = EncryptorAesCbc(key, iv)
        (sigkey2, key2, iv2) = p_sha1(n1, n2, (self.signature_key_size, self.symmetric_key_size, 16))
        self.symmetric_cryptography.Verifier = VerifierAesCbc(sigkey2)
        self.symmetric_cryptography.Decryptor = DecryptorAesCbc(key2, iv2)
