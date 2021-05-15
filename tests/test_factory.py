import random


def test_api(LIB):
    assert LIB.factory.create_cl_value is not None
    assert LIB.factory.create_deploy_for_a_transfer is not None
    assert LIB.factory.create_deploy_header is not None
    assert LIB.factory.create_named_arg is not None


def test_create_cl_value(LIB):
    assert isinstance(
        LIB.factory.create_cl_value("a-string-cl-value", LIB.types.CLType.STRING),
        LIB.types.CLValue
        )


def test_create_named_arg(LIB, al_kindi):
    assert isinstance(
        LIB.factory.create_named_arg("a-string-arg", LIB.types.CLType.STRING, al_kindi),
        LIB.types.NamedArg
        )


def test_create_deploy_for_a_transfer(LIB):
    assert isinstance(
        LIB.factory.create_deploy_for_a_transfer(
        amount = 1e9,
        correlation_id = random.randint(0, 124),
        source_purse = None,
        target_account = bytes([]),
        ),
        LIB.types.Deploy
        )


def test_create_deploy_approval_from_ed25519(LIB, account_key_ed25519, bytes_to_sign):
    assert isinstance(
        LIB.factory.create_deploy_approval(account_key_ed25519, bytes_to_sign), 
        LIB.types.DeployApproval
        )


def test_create_deploy_approval_from_secp256k1(LIB, account_key_secp256k1, bytes_to_sign):
    assert isinstance(
        LIB.factory.create_deploy_approval(account_key_secp256k1, bytes_to_sign), 
        LIB.types.DeployApproval
        )
