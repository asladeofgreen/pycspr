import dataclasses



@dataclasses.dataclass
class ConnectionInfo:
    """Encpasulates information required to connect to a node.
    
    """
    # Host address.
    host: str = "localhost"

    # Number of exposed REST port.
    port_rest: int = 50101

    # Number of exposed RPC port.
    port_rpc: int = 40101
    
    # Number of exposed SSE port.
    port_sse: int = 60101

    @property
    def address_rest(self):
        """A node's REST server base address."""
        return f"http://{self.host}:{self.port_rest}"

    @property
    def address_rpc(self):
        """A node's RPC server base address."""
        return f"http://{self.host}:{self.port_rpc}/rpc"

    @property
    def address_sse(self):
        """A node's SSE server base address."""
        return f"http://{self.host}:{self.port_sse}"
