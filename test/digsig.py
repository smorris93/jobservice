#!/usr/bin/python

import os

from collections import OrderedDict

from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA


def main():
    # sign
    message = str(OrderedDict({'key1': 'value1', 'key2': 'value2'}))
    print(message)
    key = RSA.importKey(open(os.path.join('..', 'res', 'private.pem')).read())
    h = SHA.new(message)
    signer = PKCS1_v1_5.new(key)
    signature = signer.sign(h)

    # veify
    key = RSA.importKey(open(os.path.join('..', 'res', 'public.pem')).read())
    h = SHA.new(message)
    verifier = PKCS1_v1_5.new(key)
    if verifier.verify(h, signature):
        print "The signature is authentic."
    else:
        print "The signature is not authentic."

if __name__ == "__main__":
    main()
