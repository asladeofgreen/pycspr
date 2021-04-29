import base64
import pathlib
import secrets



def test_get_hash(LIB, hash_data):
    data, fixtures = hash_data
    for algo, encoding, digest_expected in fixtures:
        digest = LIB.crypto.get_hash(data, 32, algo, encoding)
        assert digest == digest_expected


def test_get_account_key(LIB, account_keys):
    for key_algo, public_key, _ in account_keys:
        account_key = LIB.crypto.get_account_key(key_algo, public_key)
        assert isinstance(account_key, str)
        assert len(account_key) == len(public_key) + 2


def test_get_account_key_algo(LIB, account_keys):
    for key_algo, public_key, _ in account_keys:
        account_key = LIB.crypto.get_account_key(key_algo, public_key)
        assert LIB.crypto.get_account_key_algo(account_key) == key_algo


def test_get_account_hash(LIB, account_keys):
    for key_algo, public_key, account_hash in account_keys:
        account_key = LIB.crypto.get_account_key(key_algo, public_key)
        assert LIB.crypto.get_account_hash(account_key) == account_hash


def test_get_key_pair(LIB, key_pair_specs):
    for key_algo, key_encoding, typeof, pvk_length, pbk_length in key_pair_specs:
        pvk, pbk = LIB.crypto.get_key_pair(key_algo, key_encoding)
        assert isinstance(pvk, typeof) and len(pvk) == pvk_length
        assert isinstance(pbk, typeof) and len(pbk) == pbk_length
        

def test_get_key_pair_from_base64(LIB, key_pair_specs):
    for key_algo, key_encoding, _, _, _ in key_pair_specs:
        pvk, pbk = LIB.crypto.get_key_pair(key_algo, key_encoding)
        pvk_b64 = base64.b64encode(pvk) if key_encoding == LIB.crypto.KeyEncoding.BYTES else \
                  base64.b64encode(bytes.fromhex(pvk))
        assert (pvk, pbk) == LIB.crypto.get_key_pair_from_base64(pvk_b64, key_algo, key_encoding)


def test_get_key_pair_from_bytes(LIB, key_pair_specs):
    for key_algo, key_encoding, _, _, _ in key_pair_specs:
        pvk, pbk = LIB.crypto.get_key_pair(key_algo, key_encoding)
        pvk = bytes.fromhex(pvk) if key_encoding == LIB.crypto.KeyEncoding.HEX else pvk
        pvk_pem = LIB.crypto.get_pvk_pem_from_bytes(pvk, key_algo)
        assert isinstance(pvk_pem, bytes)


def test_get_key_pair_from_pem_file(LIB, key_pair_specs):
    for key_algo, key_encoding, _, _, _ in key_pair_specs:
        pvk, pbk = LIB.crypto.get_key_pair(key_algo, key_encoding)
        if key_encoding == LIB.crypto.KeyEncoding.HEX:
            path_to_pvk_pem_file = LIB.crypto.get_pvk_pem_file_from_bytes(bytes.fromhex(pvk), key_algo)
        else:
            path_to_pvk_pem_file = LIB.crypto.get_pvk_pem_file_from_bytes(pvk, key_algo)
        assert pathlib.Path(path_to_pvk_pem_file).is_file()
        assert (pvk, pbk) == LIB.crypto.get_key_pair_from_pem_file(path_to_pvk_pem_file, key_algo, key_encoding)


def test_get_key_pair_from_seed(LIB, key_pair_specs):
    """Asserts that key pairs can be generated from a seed.
    
    """
    for key_algo, key_encoding, typeof, pvk_length, pbk_length in key_pair_specs:
        seed = secrets.token_bytes(32)
        pvk, pbk = LIB.crypto.get_key_pair_from_bytes(seed, key_algo, key_encoding)
        assert isinstance(pvk, typeof) and len(pvk) == pvk_length
        assert isinstance(pbk, typeof) and len(pbk) == pbk_length


def test_get_signature(LIB, signature_data):
    data, key_info, fixtures = signature_data
    pvk_hex, algo = key_info
    pvk = bytes.fromhex(pvk_hex)
    for encoding, expected in fixtures:
        assert LIB.crypto.get_signature(pvk, data, algo, encoding) == expected
