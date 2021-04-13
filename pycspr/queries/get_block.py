import jsonrpcclient as rpc_client

import pycspr
from pycspr.crypto import get_account_hash



# RPC method to be invoked.
_API_ENDPOINT = "chain_get_block"


def execute(
    block_id: str = None,
    parse_response: bool = True,
    ) -> dict:
    """Returns on-chain block information.

    :param block_id: Identifier of a finialised block.
    :param parse_response: Flag indicating whether to parse web-service response.

    :returns: On-chain block information.

    """
    response = rpc_client.request(pycspr.CONNECTION.address_rpc, _API_ENDPOINT,
        block_identifier=block_id,
        )

    return response.data.result["block"] if parse_response else response.data.result
