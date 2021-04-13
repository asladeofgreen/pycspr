import requests as rest_client

import pycspr



# API endpoint to be invoked.
_API_ENDPOINT = "metrics"


def execute() -> dict:
    """Returns node peers information.

    :returns: Node peers information.

    """
    endpoint = f"{pycspr.CONNECTION.address_rest}/{_API_ENDPOINT}"
    response = rest_client.get(endpoint).content.decode("utf-8")
    
    return sorted([i.strip() for i in response.split("\n") if not i.startswith("#")])
