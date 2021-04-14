import jsonrpcclient as rpc_client

import pycspr
from pycspr.crypto import get_account_hash



# RPC method to be invoked.
_API_ENDPOINT = "chain_get_era_info_by_switch_block"


def execute(
    block_id: str = None,
    parse_response: bool = True,
    ) -> dict:
    """Returns current era information.

    :param block_id: Identifier of a finialised block.
    :param parse_response: Flag indicating whether to parse web-service response.

    :returns: Era information.

    """
    response = rpc_client.request(pycspr.CONNECTION.address_rpc, _API_ENDPOINT,
        block_identifier=block_id,
        )

    return response.data.result["era_summary"] if parse_response else response.data.result
