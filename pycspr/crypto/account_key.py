from pycspr.crypto.enums import KeyAlgorithm



# Map: key algorithm to key prefix.
_KEY_ALGO_PREFIX = {
    KeyAlgorithm.ED25519: "01",
    KeyAlgorithm.SECP256K1: "02",
}


def get_account_key(key_algo: KeyAlgorithm, public_key: str) -> str:
    """Returns an on-chain account identifier.

    :param key_algo: Algorithm used to generate public key.
    :param public_key: Hexadecimal representation of an ECC verifying key.

    :returns: An on-chain account identifier.

    """ 
    try:
        _KEY_ALGO_PREFIX[key_algo]
    except KeyError:
        raise KeyError(f"Unsupported key type: {key_algo}")

    if key_algo == KeyAlgorithm.ED25519 and len(public_key) != 64:
        raise ValueError(f"ED25519 public key (hex) should be 64 characters in length.")
    elif key_algo == KeyAlgorithm.SECP256K1 and len(public_key) != 66:
        raise ValueError(f"SECP256K1 public key (hex) should be 66 characters in length.")

    return f"{_KEY_ALGO_PREFIX[key_algo]}{public_key}"


def get_account_key_algo(account_key: str) -> KeyAlgorithm:
    """Returns algorithm of an account key.

    :param account_key: An account key from which an algorithm can be derived.

    :returns: A supported key algorithm.

    """
    if account_key.startswith("01"):
        return KeyAlgorithm.ED25519
    if account_key.startswith("02"):
        return KeyAlgorithm.SECP256K1

    raise ValueError("Unsupported account key type.")
