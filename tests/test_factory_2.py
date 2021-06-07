import datetime
import random



def test_create_deploy_approval_from_ed25519(FACTORY, TYPES, vectors_1, account_info_ed25519):
    vector = vectors_1.get_vector(TYPES.CLType.BYTE_ARRAY)
    value = bytes.fromhex(vector["value"])
    approval = FACTORY.deploy.create_approval(account_info_ed25519, value)
    assert isinstance(approval, TYPES.DeployApproval)


def test_create_deploy_approval_from_secp256k1(FACTORY, TYPES, vectors_1, account_info_secp256k1):
    vector = vectors_1.get_vector(TYPES.CLType.BYTE_ARRAY)
    value = bytes.fromhex(vector["value"])
    approval = FACTORY.deploy.create_approval(account_info_secp256k1, value)
    assert isinstance(approval, TYPES.DeployApproval)


def test_create_deploy_header_1(FACTORY, TYPES, account_info, a_test_chain_id):
    assert isinstance(
        FACTORY.deploy.create_header(
            account_key_info=account_info,
            body_hash=None,
            chain_name=a_test_chain_id,
            dependencies=[],
            timestamp=datetime.datetime.utcnow(),
            ttl="1day",
        ), 
        TYPES.DeployHeader
        )


def test_create_deploy_header_2(FACTORY, TYPES, account_info, a_test_chain_id):
    assert isinstance(
        FACTORY.deploy.create_header(
            account_key_info=account_info,
            body_hash=None,
            chain_name=a_test_chain_id
        ), 
        TYPES.DeployHeader
        )


def test_create_deploy_session_for_transfer(FACTORY, TYPES):
    assert isinstance(
        FACTORY.deploy.create_session_for_transfer(
            amount = 1e9,
            correlation_id = random.randint(0, 124),
            target = bytes([]),
            ),
        TYPES.DeployExecutable_Transfer
        )


# def test_create_deploy_payment_for_transfer(LIB):
#     assert isinstance(
#         LIB.factory.create_payment_for_transfer(
#             amount = 1e5,
#         ),
#         LIB.types.DeployExecutable_ModuleBytes
#         )
