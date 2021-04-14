import pytest

import tests.utils as tu



# Set of classes exposed by library.
_CLASSES = {
    "ConnectionInfo",
    }

# Set of constants exposed by library.
_CONSTANTS = {
    "CONNECTION",
    }

# Set of exceptions exposed by library.
_EXCEPTIONS = set()

# Set of functions exposed by library.
_FUNCS = {
    "get_account_balance",
    "get_account_hash",
    "get_account_info",
    "get_account_main_purse_uref",
    "get_auction_info",
    "get_block",
    "get_chain_state_root_hash",
    "get_era_info",
    "get_node_metrics",
    "get_node_peers",
    "get_node_status",
    "get_switch_block",
}


def yield_parameterizations():
    """Yields test parameterizations.

    """    
    for members, member_type in (
        (_CLASSES, 'class'),
        (_CONSTANTS, 'constant'),
        (_EXCEPTIONS, 'exception'),
        (_FUNCS, 'function'),
            ):
        for member in sorted(members):
            yield member_type, member


def test_library_version(LIB):
    """Test current version.

    """
    assert LIB.__version__ == "0.1.0"


@pytest.mark.parametrize("member_type, member", yield_parameterizations())
def test_library_exports(LIB, member_type, member):
    """Test set of exports exposed by library.

    """
    assertor = getattr(tu, 'assert_has_{}'.format(member_type))
    assertor(LIB, member)
