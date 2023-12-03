import unittest
from fastecdsa import curve

from ecdsa import *

class TestStringMethods(unittest.TestCase):
    def test_correct_verify(self):
        priv_key = gen_private_key()
        pub_key = gen_public_key(priv_key)
        message = "Hello world, example text."
        r, s = sign(message, priv_key)
        self.assertTrue(verify(message, r, s, pub_key))

    def test_correct_verify_secp256k1(self):
        priv_key = gen_private_key(curve.secp256k1)
        pub_key = gen_public_key(priv_key, curve.secp256k1)
        message = "Hello world, example text."
        r, s = sign(message, priv_key, curve.secp256k1)
        self.assertTrue(verify(message, r, s, pub_key, curve.secp256k1))

    def test_incorrect_message(self):
        priv_key = gen_private_key()
        pub_key = gen_public_key(priv_key)
        message = "Hello world, example text."
        r, s = sign(message, priv_key)
        message = "Hello world, new data."
        self.assertFalse(verify(message, r, s, pub_key))

    def test_incorrect_key(self):
        priv_key_1 = gen_private_key()
        priv_key_2 = gen_private_key()
        pub_key = gen_public_key(priv_key_2)
        message = "Hello world, example text."
        r, s = sign(message, priv_key_1)
        self.assertFalse(verify(message, r, s, pub_key))

if __name__ == '__main__':
    unittest.main()