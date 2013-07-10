#!/usr/bin/python

import os

from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA

from util_sign import canonicalize


def main():
    # sign
    message = {
        'key1': ['value1', 'value3'],
        'key2': {'some': 'value2', 'thing': 'value4'}
    }

    print(canonicalize(message))

    key = RSA.importKey(open(os.path.join('..', 'res', 'private.pem')).read())
    h = SHA.new(canonicalize(message))
    signer = PKCS1_v1_5.new(key)
    signature = signer.sign(h)

    # veify
    message = {
        'key2': {'some': 'value2', 'thing': 'value4'},
        'key1': ['value1', 'value3']
    }
    key = RSA.importKey(open(os.path.join('..', 'res', 'public.pem')).read())
    h = SHA.new(canonicalize(message))
    verifier = PKCS1_v1_5.new(key)
    if verifier.verify(h, signature):
        print "The signature is authentic."
    else:
        print "The signature is not authentic."

if __name__ == "__main__":
    main()
