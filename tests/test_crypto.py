import base64
import pathlib
import secrets



def test_get_hash(LIB, hash_data):
    """Asserts that data can be hashed.
    
    """
    data, fixtures = hash_data
    for algo, encoding, digest_expected in fixtures:
        digest = LIB.crypto.get_hash(data, 32, algo, encoding)
        assert digest == digest_expected


def test_get_account_key(LIB, account_keys):
    """Asserts that account keys can be mapped from an ECC public key.
    
    """
    for key_algo, public_key, _ in account_keys:
        account_key = LIB.crypto.get_account_key(key_algo, public_key)
        assert isinstance(account_key, str)
        assert len(account_key) == len(public_key) + 2


def test_get_account_hash(LIB, account_keys):
    """Asserts that account hashes can be mapped from an account key.
    
    """
    for key_algo, public_key, account_hash in account_keys:
        account_key = LIB.crypto.get_account_key(key_algo, public_key)
        assert LIB.crypto.get_account_hash(account_key) == account_hash


def test_get_account_key_algo(LIB, account_keys):
    """Asserts that ECC key algo can be derived from an account key.
    
    """
    for key_algo, public_key, _ in account_keys:
        account_key = LIB.crypto.get_account_key(key_algo, public_key)
        assert LIB.crypto.get_account_key_algo(account_key) == key_algo


def test_get_key_pair_01(LIB, key_pair_specs):
    """Asserts that generated key pairs are encoded correctly.
    
    """
    for key_algo, key_encoding, typeof, pvk_length, pbk_length in key_pair_specs:
        pvk, pbk = LIB.crypto.get_key_pair(key_algo, key_encoding)
        assert isinstance(pvk, typeof) and len(pvk) == pvk_length
        assert isinstance(pbk, typeof) and len(pbk) == pbk_length
        

def test_get_key_pair_02(LIB, key_pair_specs):
    """Asserts that key pairs can be decoded from base64.
    
    """
    for key_algo, key_encoding, _, _, _ in key_pair_specs:
        pvk, pbk = LIB.crypto.get_key_pair(key_algo, key_encoding)

        pvk_b64 = base64.b64encode(pvk) if key_encoding == LIB.crypto.KeyEncoding.BYTES else \
                  base64.b64encode(bytes.fromhex(pvk))

        pvk_1, pbk_1 = LIB.crypto.get_key_pair_from_pvk_b64(pvk_b64, key_algo, key_encoding)
        assert pvk == pvk_1 and pbk == pbk_1


def test_get_key_pair_03(LIB, key_pair_specs):
    """Asserts that key pairs can be decoded from bytes.
    
    """
    for key_algo, key_encoding, _, _, _ in key_pair_specs:
        pvk, pbk = LIB.crypto.get_key_pair(key_algo, key_encoding)
        pvk = bytes.fromhex(pvk) if key_encoding == LIB.crypto.KeyEncoding.HEX else pvk
        pvk_pem = LIB.crypto.get_pvk_pem_from_bytes(pvk, key_algo)
        assert isinstance(pvk_pem, bytes)


def test_get_key_pair_04(LIB, key_pair_specs):
    """Asserts that key pairs can be written/read to/from pem files.
    
    """
    for key_algo, key_encoding, _, _, _ in key_pair_specs:
        pvk, pbk = LIB.crypto.get_key_pair(key_algo, key_encoding)

        if key_encoding == LIB.crypto.KeyEncoding.HEX:
            path_to_pvk_pem_file = LIB.crypto.get_pvk_pem_file_from_bytes(bytes.fromhex(pvk), key_algo)
        else:
            path_to_pvk_pem_file = LIB.crypto.get_pvk_pem_file_from_bytes(pvk, key_algo)
        assert pathlib.Path(path_to_pvk_pem_file).is_file()

        pvk_1, pbk_1 = LIB.crypto.get_key_pair_from_pvk_pem_file(path_to_pvk_pem_file, key_algo, key_encoding)
        assert pvk == pvk_1 and pbk == pbk_1


def test_get_key_pair_05(LIB, key_pair_specs):
    """Asserts that key pairs can be generated from a seed.
    
    """
    for key_algo, key_encoding, typeof, pvk_length, pbk_length in key_pair_specs:
        seed = secrets.token_bytes(32)
        pvk, pbk = LIB.crypto.get_key_pair_from_seed(seed, key_algo, key_encoding)
        assert isinstance(pvk, typeof) and len(pvk) == pvk_length
        assert isinstance(pbk, typeof) and len(pbk) == pbk_length
