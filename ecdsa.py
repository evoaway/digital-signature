import hashlib
from hashlib import sha256

from fastecdsa.curve import P256

from util import *


def gen_private_key(curve=P256):
    return random_num(1, curve.q - 1)


def gen_public_key(private_key, curve=P256):
    return private_key * curve.G


def sign(message, private_key, curve=P256, hash_func=sha256):
    hash_digest = hash_func(message.encode()).digest()
    hash_num = number_from_byte_string(hash_digest)

    r, s = 0, 0
    while r == 0 or s == 0:
        k = random_num(1, curve.q - 1)
        R = curve.G * k
        r = R.x % curve.q
        s = (inv(k, curve.q) * (hash_num + private_key * r)) % curve.q
    return r, s


def verify(message, r, s, public_key, curve=P256, hash_func=sha256):
    hash_digest = hash_func(message.encode()).digest()
    hash_num = number_from_byte_string(hash_digest)

    if not 1 <= r <= curve.q - 1:
        return False
    if not 1 <= s <= curve.q - 1:
        return False

    c = inv(s, curve.q) % curve.q
    u1 = (hash_num * c) % curve.q
    u2 = (r * c) % curve.q
    X = u1 * curve.G + u2 * public_key
    v = X.x % curve.q
    if v == r:
        return True
    else:
        return False
