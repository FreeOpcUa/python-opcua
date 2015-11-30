from Crypto.Util.asn1 import DerSequence
from ssl import PEM_cert_to_DER_cert
from ssl import DER_cert_to_PEM_cert
import base64
import hashlib

import OpenSSL

from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Hash 
from Crypto import Random

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS) 
unpad = lambda s: s[:-ord(s[len(s) - 1:])]

def encrypt(key, raw):
    #key = hashlib.sha256(key.encode()).digest()
    key = key.exportKey(format="DER")
    raw = pad(raw)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(raw)) 

def decrypt(key, enc):
    enc = base64.b64decode(enc)
    iv = enc[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(enc[16:]))

def encrypt256(privkey, data):
    if not type(privkey) is RSA._RSAobj:
        privkey = RSA.importKey(privkey)
    cipher = PKCS1_OAEP.new(privkey, Hash.SHA256)
    ciphertext = cipher.encrypt(data)
    return ciphertext


def pubkey_from_dercert(der):
    cert = DerSequence()
    cert.decode(der)
    tbsCertificate = DerSequence()
    tbsCertificate.decode(cert[0])
    subjectPublicKeyInfo = tbsCertificate[6]

    # Initialize RSA key
    rsa_key = RSA.importKey(subjectPublicKeyInfo)
    return rsa_key


def sign(key, data):
    rng = Random.new().read()
    RSAkey = RSA.generate(384, rng)   # This will take a while...
    hash = hash.MD5.new(plaintext).digest()
    signature = RSAkey.sign(hash, rng)
    signature   # Print what an RSA sig looks like--you don't really care.
    RSAkey.verify(hash, signature)     # This sig will check out
    RSAkey.verify(hash[:-1], signature)# This sig will fail
     


if __name__ == "__main__":
    # Convert from PEM to DER
    pem = open("../examples/server_cert.pem").read()
    der = PEM_cert_to_DER_cert(pem)
    rsa_pubkey = pubkey_from_dercert(der)
    priv_pem = open("../examples/mykey.pem").read()
    rsa_privkey = RSA.importKey(priv_pem)
    #lines = pem.replace(" ",'').split()
    #der = a2b_base64(''.join(lines[1:-1]))
    cert = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, pem)

    
    # Extract subjectPublicKeyInfo field from X.509 certificate (see RFC3280)
    #cert = DerSequence()
    #cert.decode(der)
    #tbsCertificate = DerSequence()
    #tbsCertificate.decode(cert[0])
    #subjectPublicKeyInfo = tbsCertificate[6]

    # Initialize RSA key
    #rsa_key = RSA.importKey(subjectPublicKeyInfo)
    print("Pub Key", rsa_pubkey)
    print("Priv Key", rsa_privkey)
    msg = encrypt256(rsa_privkey, b"this is my message")
    print("Encrypted data: ", msg)
    from IPython import embed
    embed()
