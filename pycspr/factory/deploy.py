from datetime import datetime
import typing

from pycspr import crypto
from pycspr.types.account import AccountKeyInfo
from pycspr.types.deploy import CLType, DeployExecutable_ModuleBytes, Digest
from pycspr.types.deploy import CLValue
from pycspr.types.deploy import Deploy
from pycspr.types.deploy import DeployApproval
from pycspr.types.deploy import DeployHeader
from pycspr.types.deploy import DeployExecutable_Transfer
from pycspr.types.deploy import DeployNamedArg



def create_cl_value(cl_type: CLType, value: object) -> CLValue:
    """Returns an arbitrary value encoded for interpretation by a node.
    
    """
    # TODO: map value to bytes
    return CLValue(
        bytes = bytes([]),
        cl_type = cl_type
    )


def create_deploy_named_arg(
    value: object, 
    cl_type: CLType, 
    name: str
    ) -> DeployNamedArg:
    """Returns a named argument associated with deploy execution information (session|payment).
    
    """
    return DeployNamedArg(
        name = name,
        value = create_cl_value(cl_type, value)
    )


def create_deploy_header(
    account: bytes,
    timestamp: datetime,
    ttl: int,
    body_hash: Digest,
    dependencies: typing.List[Digest],
    chain_name: str
    ) -> DeployHeader:
    """Returns header information associated with a deploy.
    
    """
    return DeployHeader(
        account=account,
        timestamp=timestamp,
        ttl=ttl,
        body_hash=body_hash,
        dependencies=dependencies,
        chain_name=chain_name,
    )


def create_payment_for_transfer(amount: int) -> DeployExecutable_ModuleBytes:
    """Returns payment execution info for a native transfer.
    
    """
    return DeployExecutable_ModuleBytes(
        args=[
            create_deploy_named_arg(
                "amount",
                CLType.U512,
                amount,
                ),
        ],
        module_bytes=bytes([])
        )


def create_session_for_transfer(
    amount: int, 
    target_account: bytes, 
    correlation_id: int, 
    source_purse: str = None
    ) -> DeployExecutable_Transfer:
    """Returns session execution info for a native transfer.
    
    """
    return DeployExecutable_Transfer(
        args=[
            create_deploy_named_arg(
                "amount",
                CLType.U512,
                amount,
                ),
            create_deploy_named_arg(
                "target",
                CLType.PUBLIC_KEY,
                target_account,
                ),
            create_deploy_named_arg(
                "id",
                CLType.U64,
                correlation_id,
                ),
        ]
        )


def create_deploy_approval(
    account_key_info: AccountKeyInfo, 
    data: bytes
    ) -> DeployApproval:
    """Returns an approval authorizing a node to process a deploy.
    
    """
    return DeployApproval(
        signer=account_key_info.pbk, 
        signature=crypto.get_signature(account_key_info.pvk, data, algo=account_key_info.algo)
        )
