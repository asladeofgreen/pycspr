
def test_get_account_key(LIB, account_keys):
    for key_type, public_key, _ in account_keys:
        account_key = LIB.crypto.get_account_key(key_type, public_key)
        assert isinstance(account_key, str)
        assert len(account_key) == len(public_key) + 2


def test_get_account_hash(LIB, account_keys):
    for key_type, public_key, account_hash in account_keys:
        account_key = LIB.crypto.get_account_key(key_type, public_key)
        assert LIB.crypto.get_key_algo(account_key) == key_type
        assert LIB.crypto.get_account_hash(account_key) == account_hash
