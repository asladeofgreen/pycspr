import jsonrpcclient as rpc_client

import pycspr
from pycspr.crypto import get_account_hash



# RPC method to be invoked.
_RPC_METHOD = "chain_get_block"


def execute(
    block_id: str = None,
    ) -> dict:
    """Returns on-chain block information.

    :param block_id: Identifier of a finialised block.

    :returns: On-chain block information.

    """
    response = rpc_client.request(pycspr.CONNECTION.address_rpc, _RPC_METHOD,
        block_identifier=block_id,
        )

    return response.data.result["block"]
