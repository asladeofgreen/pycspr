import jsonrpcclient as rpc_client

import pycspr
from pycspr.crypto import get_account_hash



# RPC method to be invoked.
_RPC_METHOD = "state_get_item"


def execute(
    account_key: str,
    state_root_hash=None,
    ) -> str:
    """Queries account information at a certain state root hash.

    :param account_key: Key of an on-chain account.
    :param state_root_hash: A node's root state hash at some point in chain time.

    :returns: Account information in JSON format.

    """
    account_hash = get_account_hash(account_key)

    response = rpc_client.request(pycspr.CONNECTION.address_rpc, _RPC_METHOD,
        key=f"account-hash-{account_hash}",
        state_root_hash=state_root_hash,
        path=[]
        )

    assert "api_version" in response.data.result
    assert "merkle_proof" in response.data.result
    assert "stored_value" in response.data.result
    assert "Account" in response.data.result["stored_value"]

    return response.data.result["stored_value"]["Account"]
