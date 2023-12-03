# About
This is an [ECDSA](https://datatracker.ietf.org/doc/html/rfc6979) implementation that uses the [fastecdsa](https://github.com/AntonKueltz/fastecdsa) library for arbitrary elliptic curve arithmetic
# Installing additional libraries
You can use pip: `$ pip install fastecdsa` or clone the repo and use `$ python setup.py install`.
# Description
The Elliptic Curve Based Digital Signature Algorithm (ECDSA) implements a variant of the Digital Signature Algorithm (DSA) that uses elliptic curve based cryptography.
This implementation uses P256 as the default curve. The execution of the algorithm is based on 4 functions:
* `gen_private_key` - generates a private key depending on the elliptic curve
* `gen_public_key` - generates a public key depending on the private key and the curve
* `sign` - returns signature (r, s). By default, the SHA-256 hash function is used
* `verify` - returns signature verification result (true, false)
# Usage
An example of a signature using the `secp256k1` curve
```python
from fastecdsa import curve
from ecdsa import *

    priv_key = gen_private_key(curve.secp256k1)
    pub_key = gen_public_key(priv_key, curve.secp256k1)
    message = "Hello world, example text."
    r, s = sign(message, priv_key, curve.secp256k1)
    result = verify(message, r, s, pub_key, curve.secp256k1)
```
