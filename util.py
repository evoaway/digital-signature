from binascii import hexlify
from random import SystemRandom


def random_num(min, max):
    return SystemRandom().randrange(min, max + 1)


def int_from_hex(hexadecimal):
    return int(hexadecimal, 16)


def to_string(string, encoding="utf-8"):
    return string.decode(encoding)


def safe_hex_from_binary(byteString):
    return to_string(hexlify(byteString))


def hex_from_byte_string(byteString):
    return safe_hex_from_binary(byteString)


def number_from_byte_string(byteString):
    return int_from_hex(hex_from_byte_string(byteString))


def inv(x, n):
    # Extended Euclidean Algorithm
    if x == 0:
        return 0

    lm = 1
    hm = 0
    low = x % n
    high = n

    while low > 1:
        r = high // low
        nm = hm - lm * r
        nw = high - low * r
        high = low
        hm = lm
        low = nw
        lm = nm

    return lm % n
