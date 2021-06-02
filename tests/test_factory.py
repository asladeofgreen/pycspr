import datetime
import random



def test_create_cl_value(LIB):
    assert isinstance(
        LIB.factory.create_cl_value(LIB.types.CLType.STRING, "a-string-cl-value"),
        LIB.types.CLValue
        )


def test_create_deploy_named_arg(LIB, al_kindi):
    assert isinstance(
        LIB.factory.create_deploy_named_arg("a-string-arg", LIB.types.CLType.STRING, al_kindi),
        LIB.types.DeployNamedArg
        )



def test_create_deploy_approval_from_ed25519(LIB, account_info_ed25519, bytes_to_sign):
    assert isinstance(
        LIB.factory.create_deploy_approval(
            account_info_ed25519, 
            bytes_to_sign
            ), 
        LIB.types.DeployApproval
        )


def test_create_deploy_approval_from_secp256k1(LIB, account_info_secp256k1, bytes_to_sign):
    assert isinstance(
        LIB.factory.create_deploy_approval(
            account_info_secp256k1,
            bytes_to_sign
            ), 
        LIB.types.DeployApproval
        )


def test_create_deploy_header(LIB, account_info, chain_name):
    assert isinstance(
        LIB.factory.create_deploy_header(
            account=account_info.account_key,
            body_hash=None,
            chain_name=chain_name,
            dependencies=[],
            timestamp=datetime.datetime.utcnow(),
            ttl=30000,
        ), 
        LIB.types.DeployHeader
        )


def test_create_deploy_session_for_transfer(LIB):
    assert isinstance(
        LIB.factory.create_session_for_transfer(
            amount = 1e9,
            correlation_id = random.randint(0, 124),
            source_purse = None,
            target_account = bytes([]),
            ),
        LIB.types.DeployExecutable_Transfer
        )


def test_create_deploy_payment_for_transfer(LIB):
    assert isinstance(
        LIB.factory.create_payment_for_transfer(
            amount = 1e5,
        ),
        LIB.types.DeployExecutable_ModuleBytes
        )
