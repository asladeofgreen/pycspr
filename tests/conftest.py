import json
import os
import pathlib
import typing

import pytest

import pycspr


# Path to test assets.
_ASSETS = pathlib.Path(os.path.dirname(__file__)) / "assets"


def _get_asset(fname: str, parser: typing.Callable = None):
    """Returns contents of associated assets.
    
    """
    with open(_ASSETS / fname) as fhandle:
        return fhandle.read() if parser is None else parser(fhandle)


@pytest.fixture(scope="session")
def a_test_chain_id() -> str:
    """Returns name of a test chain. 
    
    """
    return "casper-net-1"


@pytest.fixture(scope="session")
def a_test_string() -> str:
    """Returns some bytes to use as input to upstream tests. 
    
    """
    return  _get_asset("fixture_for_unicode_test.txt")


@pytest.fixture(scope="session")
def a_test_bytearray() -> bytes:
    """Returns some bytes to use as input to upstream tests. 
    
    """
    return  _get_asset("fixture_for_unicode_test.txt").encode("utf-8")


@pytest.fixture(scope="session")
def fixtures_for_hash_tests() -> list:
    """Returns a set of fixtures for use as input to upstream hashing tests. 
    
    """
    return _get_asset("fixtures_for_hash_tests.json", json.load)["fixtures"]


@pytest.fixture(scope="session")
def fixtures_for_public_key_tests() -> list:
    """Returns a set of fixtures for use as input to upstream key tests. 
    
    """
    return _get_asset("fixtures_for_public_key_tests.json", json.load)["fixtures"]


@pytest.fixture(scope="session")
def fixtures_for_key_pair_tests() -> list:
    """Returns a set of fixtures for use as input to upstream key-pair tests. 
    
    """
    return _get_asset("fixtures_for_key_pair_tests.json", json.load)["fixtures"]


@pytest.fixture(scope="session")
def fixtures_for_signature_tests() -> list:
    """Returns a set of fixtures for use as input to upstream signature tests. 
    
    """
    return _get_asset("fixtures_for_signature_tests.json", json.load)["fixtures"]


@pytest.fixture(scope="session")
def LIB() -> pycspr:
    """Returns pointer to configured library instance. 
    
    """
    # Initialise with default NCTL node 1 connection info.
    pycspr.initialise(pycspr.NodeConnectionInfo(
        host="localhost",
        port_rest=50101,
        port_rpc=40101,
        port_sse=60101
    ))

    return pycspr


@pytest.fixture(scope="session")
def account_info_ed25519(LIB, fixtures_for_public_key_tests) -> pycspr.types.AccountKeyInfo:
    """Returns a test ED25519 account key. 
    
    """
    fixture = fixtures_for_public_key_tests[0]

    return LIB.types.AccountKeyInfo(
        pbk=bytes.fromhex(fixture["pbk"]),
        pvk=bytes.fromhex(fixture["address"]),
        algo=LIB.crypto.KeyAlgorithm[fixture["algo"]]
    )


@pytest.fixture(scope="session")
def account_info_secp256k1(LIB, fixtures_for_public_key_tests) -> pycspr.types.AccountKeyInfo:
    """Returns a test ED25519 account key. 
    
    """
    fixture = fixtures_for_public_key_tests[1]

    return LIB.types.AccountKeyInfo(
        pbk=bytes.fromhex(fixture["pbk"]),
        pvk=bytes.fromhex(fixture["address"]),
        algo=LIB.crypto.KeyAlgorithm[fixture["algo"]]
    )


@pytest.fixture(scope="session")
def account_info(LIB, account_info_ed25519) -> pycspr.types.AccountKeyInfo:
    """Returns a test account key. 
    
    """
    return account_info_ed25519


def _get_account_info_of_nctl_user(LIB, user_id: int) -> pycspr.types.AccountKeyInfo:
    """Returns account information related to NCTL user 1. 
    
    """
    path = pathlib.Path(os.getenv("NCTL"))
    path = path / "assets" / "net-1" / "users" / f"user-{user_id}" / "secret_key.pem"
    (pvk, pbk) = LIB.crypto.get_key_pair_from_pem_file(path)

    return LIB.types.AccountKeyInfo(
        pbk=pbk,
        pvk=pvk,
        algo=LIB.crypto.KeyAlgorithm.ED25519
    )


@pytest.fixture(scope="session")
def cp1(LIB) -> pycspr.types.AccountKeyInfo:
    """Returns a test account key. 
    
    """
    return _get_account_info_of_nctl_user(LIB, 1)


@pytest.fixture(scope="session")
def cp2(LIB) -> pycspr.types.AccountKeyInfo:
    """Returns a test account key. 
    
    """
    return _get_account_info_of_nctl_user(LIB, 2)


@pytest.fixture(scope="session")
def key_pair_specs(LIB) -> typing.Tuple[pycspr.crypto.KeyAlgorithm, str, str]:
    """Returns sets of specifications for key pair generation. 
    
    """
    return (
        (
            LIB.crypto.KeyAlgorithm.ED25519,
            LIB.crypto.KeyEncoding.BYTES,
            bytes,
            32,
            32,
        ),
        (
            LIB.crypto.KeyAlgorithm.ED25519,
            LIB.crypto.KeyEncoding.HEX,
            str,
            64,
            64,
        ),
        (
            LIB.crypto.KeyAlgorithm.SECP256K1,
            LIB.crypto.KeyEncoding.BYTES,
            bytes,
            32,
            33,
        ),
        (
            LIB.crypto.KeyAlgorithm.SECP256K1,
            LIB.crypto.KeyEncoding.HEX,
            str,
            64,
            66,
        ),
    )


@pytest.fixture(scope="session")
def account_key() -> str:
    """Returns a test NCTL account key. 
    
    """
    path = pathlib.Path(os.getenv("NCTL"))
    path = path / "assets" / "net-1" / "users" / "user-1" / "public_key_hex"

    with open(path) as fstream:
        return fstream.read()


@pytest.fixture(scope="function")
def account_main_purse_uref(LIB, account_key, state_root_hash) -> str:
    """Returns a test account main purse unforgeable reference. 
    
    """
    return LIB.get_account_main_purse_uref(account_key, state_root_hash)


@pytest.fixture(scope="function")
def state_root_hash(LIB) -> str:
    """Returns current state root hash @ NCTL Node 1. 
    
    """
    return LIB.get_state_root_hash()


@pytest.fixture(scope="function")
def block_hash(LIB) -> str:
    """Returns hash of most recent block @ NCTL Node 1. 
    
    """
    return LIB.get_block()["hash"]


@pytest.fixture(scope="session")
def switch_block(LIB) -> str:
    """Returns hash of most next switch. 
    
    """
    return LIB.get_switch_block()


@pytest.fixture(scope="session")
def switch_block_hash(switch_block) -> str:
    """Returns hash of most next switch. 
    
    """
    return switch_block["hash"]
