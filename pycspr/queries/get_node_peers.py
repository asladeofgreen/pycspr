import jsonrpcclient as rpc_client

import pycspr



# Method upon client to be invoked.
_RPC_METHOD = "info_get_peers"


def execute() -> dict:
    """Returns node peers information.

    :returns: Node peers information.

    """
    response = rpc_client.request(pycspr.CONNECTION.address_rpc, _RPC_METHOD)

    return response.data.result
