import dataclasses
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


@dataclasses.dataclass
class CLValue():
    """Domain type: a value to be interpreted by node software.
    
    """
    # Byte array representation of underlying data.
    bytes: bytes

    # Type information used by a deserializer.
    cl_type: CLType


@dataclasses.dataclass
class NamedArg():
    """Domain type: a named argument to be mapped to a contract function parameter.
    
    """
    # Argument name mapped to an entry point parameter.
    name: str
    
    # Argument value. 
    value: CLValue


@dataclasses.dataclass
class DeployApproval:
    """A digital signature approving deploy processing.
    
    """
    # The public key component to the signing key used to sign a deploy.
    signer: PublicKey

    # The digital signatutre signalling approval of deploy processing.
    signature: Signature


@dataclasses.dataclass
class DeployExecutable():
    """Encapsulates vm executable information.
    
    """
    # Set of arguments mapped to endpoint parameters.
    args: typing.List[NamedArg]


@dataclasses.dataclass
class DeployExecutable_ModuleBytes(DeployExecutable):
    """Encapsulates information required to execute an in-line wasm binary.
    
    """
    # Raw wASM payload.
    module_bytes: bytes


@dataclasses.dataclass
class DeployExecutable_StoredContract(DeployExecutable):
    """Encapsulates information required to execute an on-chain smart contract.
    
    """
    # Name of a smart contract entry point to be executed. 
    entry_point: str


@dataclasses.dataclass
class DeployExecutable_StoredContractByHash(DeployExecutable_StoredContract):
    """Encapsulates information required to execute an on-chain smart contract referenced by hash.
    
    """
    # On-chain smart contract address. 
    hash: ContractHash


@dataclasses.dataclass
class DeployExecutable_StoredContractByHashVersioned(DeployExecutable_StoredContractByHash):
    """Encapsulates information required to execute a versioned on-chain smart contract referenced by hash.
    
    """
    # Smart contract version identifier.
    version: ContractVersion
    

@dataclasses.dataclass
class DeployExecutable_StoredContractByName(DeployExecutable_StoredContract):
    """Encapsulates information required to execute an on-chain smart contract referenced by name.
    
    """
    # On-chain smart contract name - only in scope when dispatch account = contract owner account. 
    name: str


@dataclasses.dataclass
class DeployExecutable_StoredContractByNameVersioned(DeployExecutable_StoredContractByName):
    """Encapsulates information required to execute a versioned on-chain smart contract referenced by name.
    
    """
    # Smart contract version identifier.
    version: ContractVersion


@dataclasses.dataclass
class DeployExecutable_Transfer(DeployExecutable):
    """Encapsulates information required to execute a host-side balance transfer.
    
    """
    pass


@dataclasses.dataclass
class DeployHeader():
    """Encapsulates header information associated with a deploy.
    
    """
    # Public key of account dispatching deploy to a node.
    account: PublicKey

    # Timestamp at point of deploy creation.
    timestamp: Timestamp

    # Time interval after which the deploy will no longer be considered for processing by a node.
    ttl: TimeDifference

    # Hash of deploy payload.
    body_hash: Digest

    # Set of deploys that must be executed prior to this one.
    dependencies: typing.List[Digest]

    # Name of target chain to which deploy will be dispatched.
    chain_name: ChainName


@dataclasses.dataclass
class Deploy():
    """Top level container encapsulating information required to interact with chain.
    
    """
    # Set of signatures approving this deploy for execution.
    approvals: typing.List[DeployApproval]

    # Unique identifier.
    hash: Digest

    # Header information encapsulating various information impacting deploy processing.
    header: DeployHeader

    # Executable information passed to chain's VM for taking payment required to process session logic.
    payment: DeployExecutable

    # Executable information passed to chain's VM.
    session: DeployExecutable
