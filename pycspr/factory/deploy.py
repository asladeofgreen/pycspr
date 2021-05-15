from datetime import datetime
import typing

from pycspr import crypto
from pycspr.types.account import AccountKeyInfo
from pycspr.types.deploy import CLType, Digest
from pycspr.types.deploy import CLValue
from pycspr.types.deploy import Deploy
from pycspr.types.deploy import DeployApproval
from pycspr.types.deploy import DeployHeader
from pycspr.types.deploy import DeployExecutable_Transfer
from pycspr.types.deploy import NamedArg



def create_cl_value(value: object, cl_type: CLType) -> CLValue:
    return CLValue(
        bytes = bytes([]),
        cl_type = cl_type
    )


def create_named_arg(value: object, cl_type: CLType, name: str) -> NamedArg:
    return NamedArg(
        name = name,
        value = create_cl_value(value, cl_type)
    )


def create_deploy_for_a_transfer(
    amount: int,
    target_account: bytes,
    correlation_id: int,
    source_purse: str = None
    ) -> Deploy:
    return Deploy()

    return Deploy(
        approvals=[],
        hash=None,
        header=create_deploy_header(
            account = bytes([]),
            timestamp = datetime.utcnow(),
            ttl = 30000,
            body_hash = None,
            dependencies = [],
            chain_name = "casper-net-1",
        ),
        payment=None,
        session=DeployExecutable_Transfer(
            args=[
                create_named_arg(
                    "amount",
                    CLType.U512,
                    amount,
                    ),
                create_named_arg(
                    "target",
                    CLType.PUBLIC_KEY,
                    target_account,
                    ),
                create_named_arg(
                    "id",
                    CLType.U64,
                    correlation_id,
                    ),
            ]
        )
    )


def create_deploy_header(
    account: bytes,
    timestamp: datetime,
    ttl: int,
    body_hash: Digest,
    dependencies: typing.List[Digest],
    chain_name: str
    ) -> DeployHeader:
    return DeployHeader(
        account = account,
        timestamp = timestamp,
        ttl = ttl,
        body_hash = body_hash,
        dependencies = dependencies,
        chain_name = chain_name,
    )


def create_session_logic_for_transfer(amount: int, target_account: bytes, correlation_id: int, source_purse: str = None) -> DeployExecutable_Transfer:
    return DeployExecutable_Transfer(
        args=[
            create_named_arg(
                "amount",
                CLType.U512,
                amount,
                ),
            create_named_arg(
                "target",
                CLType.PUBLIC_KEY,
                target_account,
                ),
            create_named_arg(
                "id",
                CLType.U64,
                correlation_id,
                ),
        ]
        )


def create_deploy_approval(account_key_info: AccountKeyInfo, data: bytes) -> DeployApproval:
    return DeployApproval(
        signer=account_key_info.pbk, 
        signature=crypto.get_signature(account_key_info.pvk, data, algo=account_key_info.algo)
        )
