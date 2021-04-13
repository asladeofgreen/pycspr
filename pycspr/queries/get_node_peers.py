import jsonrpcclient as rpc_client

import pycspr



# Method upon client to be invoked.
_API_ENDPOINT = "info_get_peers"


def execute() -> dict:
    """Returns node peers information.

    :returns: Node peers information.

    """
    response = rpc_client.request(pycspr.CONNECTION.address_rpc, _API_ENDPOINT)

    return response.data.result
