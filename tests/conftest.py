import os
import pathlib
import typing

import pytest

import pycspr
from pycspr.connection_info import ConnectionInfo



@pytest.fixture(scope="session")
def LIB() -> pycspr:
    """Returns pointer to configured library instance. 
    
    """
    # Initialise with default node connection info.
    pycspr.initialise(ConnectionInfo())

    return pycspr


@pytest.fixture(scope="session")
def account_keys(LIB) -> typing.Tuple[pycspr.crypto.KeyAlgorithm, str, str]:
    """Returns set of test accoutn key. 
    
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
    return LIB.get_chain_state_root_hash()


@pytest.fixture(scope="function")
def block_hash(LIB) -> str:
    """Returns hash of most recent block @ NCTL Node 1. 
    
    """
    return LIB.get_block()["hash"]