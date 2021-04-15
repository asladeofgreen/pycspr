import os
import pathlib
import typing

import pytest

import pycspr



@pytest.fixture(scope="session")
def LIB() -> pycspr:
    """Returns pointer to configured library instance. 
    
    """
    # Initialise with default NCTL node 1 connection info.
    pycspr.initialise(pycspr.NodeConnectionInfo())

    return pycspr


@pytest.fixture(scope="session")
def hash_data(LIB) -> typing.Tuple[bytes, typing.Tuple]:
    """Returns set of test account key. 
    
    """    
    return b"al-kindi", (
        (
            LIB.crypto.HashAlgorithm.BLAKE2B, \
            LIB.crypto.HashEncoding.BYTES, \
            b"H\x1d{\x97\xb0\xb1!\xb0\xaf\xcf\x89\x1a\xa2#]\x0f\xf2\xf5\xf8r\xe9\xeb\xe0\xa7\xb6z\xf5\x86\xcd\x1cyR",
        ),
        (
            LIB.crypto.HashAlgorithm.BLAKE2B, \
            LIB.crypto.HashEncoding.HEX, \
            "481d7b97b0b121b0afcf891aa2235d0ff2f5f872e9ebe0a7b67af586cd1c7952"
        ),
    )


@pytest.fixture(scope="session")
def account_keys(LIB) -> typing.Tuple[pycspr.crypto.KeyAlgorithm, str, str]:
    """Returns set of test account key. 
    
    """    
    return (
        (
            LIB.crypto.KeyAlgorithm.ED25519, \
            "2fa788bfd72abbad5272e478e16dda3cf04f171f1368cca3a6517471475e42a1", \
            "1547c5d44c5a6d079093235329934fde9455b99f2a2bee769a625d0f1f006bbc"            
        ),
        (
            LIB.crypto.KeyAlgorithm.SECP256K1, \
            "0339a36013301597daef41fbe593a02cc513d0b55527ec2df1050e2e8ff49c85c2", \
            "95a90f4a251a8a66621704e0560a51786ce90559448e49bd21934c4aa4d91948"
        ),
    )


@pytest.fixture(scope="session")
def key_pair_specs(LIB) -> typing.Tuple[pycspr.crypto.KeyAlgorithm, str, str]:
    """Returns set of test account key. 
    
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
def key_pairs(LIB) -> typing.Tuple[pycspr.crypto.KeyAlgorithm, str, str]:
    """Returns set of test account key. 
    
    """
    return (
        (
            LIB.crypto.KeyAlgorithm.ED25519,
            LIB.crypto.KeyEncoding.BYTES,
            b'\x82/\x86\xc1\xea\x95F\xd3|l:E\x18w\xc8\xc1h\xfd\xca\xb5\x1be\xcc\xec\x14+\xa2zzkT\x8c',
            b'\xcdb\xf1\xc5\xcc\xa5\x1f\xa3\xc2_Lv\xa4m\xd5\xf6\xb0\x98\x8c\x95\xdan\xa85\xecDA\xd6\x8d\xce\xa3\x93',
        ),
        (
            LIB.crypto.KeyAlgorithm.ED25519,
            LIB.crypto.KeyEncoding.HEX,
            "822f86c1ea9546d37c6c3a451877c8c168fdcab51b65ccec142ba27a7a6b548c",
            "cd62f1c5cca51fa3c25f4c76a46dd5f6b0988c95da6ea835ec4441d68dcea393",
        ),
        (
            LIB.crypto.KeyAlgorithm.SECP256K1,
            LIB.crypto.KeyEncoding.BYTES,
            b'\xf6\xe4\x87\xb6\xd3\x86\xf1"\x1b\xd3\xb7\xc2\xa01\x91$\xbf\xf8\x0b"C\xd3\xda\xc3\x18\n\x11\x95\xce\xc2\x96\x85',
            b'\x02r\xdc\xc1\xd3\x84\xa6\xdd\xad\x06\xfd\xe1\xce\xb2\xf1\xfeRO\x84\xdd\xf5\xee;\xdb6\x82\xeb{\x92}\xe0\xe6\x82',
        ),
        (
            LIB.crypto.KeyAlgorithm.SECP256K1,
            LIB.crypto.KeyEncoding.HEX,
            "f6e487b6d386f1221bd3b7c2a0319124bff80b2243d3dac3180a1195cec29685",
            "0272dcc1d384a6ddad06fde1ceb2f1fe524f84ddf5ee3bdb3682eb7b927de0e682",
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
