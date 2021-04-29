import base64
import typing

import ecdsa

from pycspr.crypto.enums import KeyEncoding



# Curve of interest.
CURVE = ecdsa.SECP256k1

# Use uncompressed public keys.
UNCOMPRESSED = "uncompressed"


def get_key_pair() -> typing.Tuple[bytes, bytes]:
    """Returns an SECP256K1 key pair, each key is a 32 byte array.

    :returns : 2 member tuple: (private key, public key)
    
    """    
    return _get_key_pair_from_sk(ecdsa.SigningKey.generate(curve=CURVE))


def get_key_pair_from_pvk_b64(pvk_b64: str):
    """Returns an SECP256K1 key pair derived from a previously base 64 private key.

    :param pvk_b64: Base64 encoded private key.

    :returns : 2 member tuple: (private key, public key)
    
    """
    return get_key_pair_from_pvk_bytes(base64.b64decode(pvk_b64))


def get_key_pair_from_pvk_bytes(pvk: bytes) -> typing.Tuple[bytes, bytes]:
    """Returns an ED25519 key pair derived from a byte array representation of a private key.

    :param pvk: 32 byte array representing a private key.

    :returns : 2 member tuple: (private key, public key)
    
    """
    sk = ecdsa.SigningKey.from_string(pvk, curve=CURVE)

    return _get_key_pair_from_sk(sk)


def get_key_pair_from_pvk_hex_string(pvk_hex: str) -> typing.Tuple[bytes, bytes]:
    """Returns an ED25519 key pair derived from a previously base 64 private key.

    :param pvk_b64: Base64 encoded private key.

    :returns : 2 member tuple: (private key, public key)
    
    """
    return get_key_pair_from_pvk_bytes(bytes.fromhex(pvk_hex))


def get_key_pair_from_pvk_pem_file(fpath: str) -> typing.Tuple[bytes, bytes]:
    """Returns an SECP256K1 key pair derived from a previously persisted PEM file.

    :param fpath: PEM file path.

    :returns : 2 member tuple: (private key, public key)
    
    """
    with open(fpath, "rb") as f:
        return _get_key_pair_from_sk(ecdsa.SigningKey.from_pem(f.read()))


def get_key_pair_from_seed(seed: bytes) -> typing.Tuple[bytes, bytes]:
    """Returns an ED25519 key pair derived from a seed.

    :param seed: A seed used as input to deterministic key pair generation.

    :returns : 2 member tuple: (private key, public key)
    
    """
    sk = ecdsa.SigningKey.from_string(seed, curve=CURVE)

    return _get_key_pair_from_sk(sk)


def get_pvk_pem_from_bytes(pvk: bytes) -> bytes:
    """Returns SECP256K1 private key (pem) from bytes.
    
    """
    sk = ecdsa.SigningKey.from_string(pvk, curve=CURVE)

    return sk.to_pem()


def _get_key_pair_from_sk(sk: ecdsa.SigningKey) -> typing.Tuple[bytes, bytes]:
    """Returns key pair from a signing key.
    
    """
    return sk.to_string(), \
           sk.verifying_key.to_string("compressed")
