import datetime
import enum
import typing



# Domain type: chain name.
ChainName = typing.NewType("Simple chain identifer", str)

# Domain type: output of a hashing function.
ContractHash = typing.NewType("32 byte array emitted by a hashing algorithm representing a static contract pointer", bytes)

# Domain type: representing a output of a hashing function.
ContractVersion = typing.NewType("U32 integer representing", int)

# Domain type: representing a public key derived from an ECC key pair.
PublicKey = typing.NewType("Either 32 or 33 bytes (compressed) depending upon ECC type", bytes)

# Domain type: representing a output of a hashing function.
Digest = typing.NewType("32 byte array emitted by a hashing algorithm", bytes)

# Domain type: representing a output of a hashing function.
Signature = typing.NewType("64 byte array emitted by an ECC algorithm", bytes)

# Domain type: representing a output of a hashing function.
Timestamp = typing.NewType("ISO compliant timestamp", datetime.datetime)

# Domain type: representing a output of a hashing function.
TimeDifference = typing.NewType("A temporal offset from now", datetime.time)


class CLType(enum.Enum):
    """Domain type: enumeration over set of low level CL types.
    
    """
    BOOL = 0
    I32 = 1
    I64 = 2
    U8 = 3
    U32 = 4
    U64 = 5
    U128 = 6
    U256 = 7
    U512 = 8
    UNIT = 9
    STRING = 10
    KEY = 11
    UREF = 12
    OPTION = 13
    LIST = 14
    BYTE_ARRAY = 15
    RESULT = 16
    MAP = 17
    TUPLE_1 = 18
    TUPLE_2 = 19
    TUPLE_3 = 20
    ANY = 21
    PUBLIC_KEY = 22


class CLValue():
    """Domain type: a value to be interpreted by node software.
    
    """
    def __init__(self):
        # Byte array representation of underlying data.
        self.bytes: bytes = None

        # Type information used by a deserializer.
        self.cl_type: CLType = None


class NamedArg():
    """Domain type: a named argument to be mapped to a contract function parameter.
    
    """
    def __init__(self):
        # Argument name mapped to an entry point parameter.
        self.name: str = None
        
        # Argument value. 
        self.value: CLValue = None


class DeployApproval():
    """Domain type: a digital signature approving process of a deploy.
    
    """
    def __init__(self):
        # The public key component to the signing key used to sign a deploy.
        self.signer: PublicKey = None

        # The digital signatutre signalling approval of deploy processing.
        self.signature: Signature = None


class DeployHeader():
    """Domain type: header information associated with a deploy.
    
    """
    def __init__(self):
        # Public key of account dispatching deploy to a node.
        self.account: PublicKey = None

        # Timestamp at point of deploy creation.
        self.timestamp: Timestamp = None

        # Time interval after which the deploy will no longer be considered for processing by a node.
        self.ttl: TimeDifference = None

        # Hash of deploy payload.
        self.body_hash: Digest = None

        # Set of deploys that must be executed prior to this one.
        self.dependencies = typing.List[Digest] = None

        # Name of target chain to which deploy will be dispatched.
        self.chain_name: ChainName = None


class DeployExecutable():
    """Domain type: vm executable information.
    
    """
    def __init__(self):
        # Set of arguments mapped to endpoint parameters.
        args: list[NamedArg] = []


class DeployExecutable_ModuleBytes(DeployExecutable):
    """Domain type: information required to execute an in-line wasm binary.
    
    """
    def __init__(self):
        # Raw wASM payload.
        self.module_bytes: bytes = bytes([])


class DeployExecutable_StoredContract(DeployExecutable):
    """Domain type: information required to execute an on-chain smart contract.
    
    """
    def __init__(self):
        # Name of a smart contract entry point to be executed. 
        self.entry_point: str = None


class DeployExecutable_StoredContractByHash(DeployExecutable_StoredContract):
    """Domain type: information required to execute an on-chain smart contract referenced by hash.
    
    """
    def __init__(self):
        # On-chain smart contract address. 
        self.hash: ContractHash = None


class DeployExecutable_StoredContractByHashVersioned(DeployExecutable_StoredContractByHash):
    """Domain type: information required to execute a versioned on-chain smart contract referenced by hash.
    
    """
    def __init__(self):
        # Smart contract version identifier.
        self.version: ContractVersion = None
    

class DeployExecutable_StoredContractByName(DeployExecutable_StoredContract):
    """Domain type: information required to execute an on-chain smart contract referenced by name.
    
    """
    def __init__(self):
        # On-chain smart contract name - only in scope when dispatch account = contract owner account. 
        self.name: str = None


class DeployExecutable_StoredContractByNameVersioned(DeployExecutable_StoredContractByName):
    """Domain type: information required to execute a versioned on-chain smart contract referenced by name.
    
    """
    def __init__(self):
        # Smart contract version identifier.
        self.version: ContractVersion = None


class DeployExecutable_Transfer(DeployExecutable):
    """Domain type: information required to execute a host-side balance transfer.
    
    """
    def __init__(self):
        pass


class Deploy(object):
    """Domain type: top level container encapsulating information required to interact with chain.
    
    """
    def __init__(self):
        self.approvals: typing.List[DeployApproval] = None
        self.hash: Digest = None
        self.header: DeployHeader = None
        self.payment: DeployExecutable = None
        self.session: DeployExecutable = None
