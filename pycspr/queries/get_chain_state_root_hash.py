import jsonrpcclient as rpc_client

import pycspr



# Method upon client to be invoked.
_RPC_METHOD = "chain_get_state_root_hash"


def execute(
    block_id: str = None,
    ) -> str:
    """Returns an on-chain state root hash at specified block.

    :param block_id: Identifier of a finialised block.

    :returns: State root hash at specified block.

    """
    response = rpc_client.request(pycspr.CONNECTION.address_rpc, _RPC_METHOD,
        block_identifier=block_id,
        )

    assert "api_version" in response.data.result
    assert "state_root_hash" in response.data.result

    return response.data.result["state_root_hash"]
