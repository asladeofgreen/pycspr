import jsonrpcclient as rpc_client

import pycspr



# Method upon client to be invoked.
_RPC_METHOD = "info_get_status"


def execute() -> dict:
    """Returns node status information.

    :returns: Node status information.

    """
    response = rpc_client.request(pycspr.CONNECTION.address_rpc, _RPC_METHOD)

    return response.data.result
