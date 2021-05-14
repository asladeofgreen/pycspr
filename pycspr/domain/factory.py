import typing

from pycspr.domain.types import CLType
from pycspr.domain.types import CLValue
from pycspr.domain.types import Deploy
from pycspr.domain.types import DeployHeader
from pycspr.domain.types import DeployExecutable_Transfer
from pycspr.domain.types import NamedArg



def create_cl_value(value: object, cl_type: CLType) -> CLValue:
    instance = CLValue()
    instance.bytes = bytes([])
    instance.cl_type = cl_type

    return instance


def create_named_arg(value: object, cl_type: CLType, name: str) -> NamedArg:
    instance = NamedArg()
    instance.name = name
    instance.value = create_cl_value(value, cl_type)

    return instance


def create_deploy_for_a_transfer(
    amount: int,
    target: bytes,
    correlation_id: int,
    source_purse: str = None
) -> Deploy:
    return Deploy(
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
                    target,
                    ),
                create_named_arg(
                    "id",
                    CLType.U64,
                    correlation_id,
                    ),
            ]
        )
    )


def create_deploy_header() -> DeployHeader:
    return DeployHeader()
