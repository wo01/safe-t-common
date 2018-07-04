#!/usr/bin/python
import binascii

from ecdsa import SigningKey, VerifyingKey, SECP256k1

if __name__ == '__main__':
    sk = SigningKey.generate(curve=SECP256k1)
    vk = sk.get_verifying_key()

    fp = open('./key_ecdsa_SECP256k1.pem', 'w')
    fp.write(sk.to_pem())
    fp.close()

    fp2 = open('./key_ecdsa_SECP256k1.pub', 'w')
    fp2.write(binascii.hexlify(vk.to_string()))
    fp2.close()
