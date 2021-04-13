import jsonrpcclient as rpc_client

import pycspr
from pycspr.crypto import get_account_hash



# RPC method to be invoked.
_RPC_METHOD = "state_get_balance"


def execute(
    purse_uref: str,
    state_root_hash: str = None,
    ) -> int:
    """Queries account balance at a certain state root hash.

    :param purse_uref: URef of a purse associated with an on-chain account.
    :param state_root_hash: A node's root state hash at some point in chain time.

    :returns: Account balance if on-chain account is found.

    """
    response = rpc_client.request(pycspr.CONNECTION.address_rpc, _RPC_METHOD,
        purse_uref=purse_uref,
        state_root_hash=state_root_hash,
        )

    # assert "api_version" in response.data.result
    # assert "merkle_proof" in response.data.result
    # assert "stored_value" in response.data.result
    # assert "Account" in response.data.result["stored_value"]

    return int(response.data.result["balance_value"])
