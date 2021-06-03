import datetime
import random



# def test_create_cl_value(LIB):
#     assert isinstance(
#         LIB.factory.create_cl_value(LIB.types.CLType.STRING, "a-string-cl-value"),
#         LIB.types.CLValue
#         )


def test_create_named_arg(LIB, FACTORY, TYPES, a_string_value):
    arg = FACTORY.deploy.create_named_arg(
        "a-string-arg",
        TYPES.CLType.STRING,
        a_string_value
        )
    assert isinstance(arg, TYPES.DeployNamedArg)


# def test_create_deploy_approval_from_ed25519(LIB, account_info_ed25519, a_bytearray_value):
#     assert isinstance(
#         LIB.factory.create_deploy_approval(
#             account_info_ed25519, 
#             a_bytearray_value
#             ), 
#         LIB.types.DeployApproval
#         )


# def test_create_deploy_approval_from_secp256k1(LIB, account_info_secp256k1, a_bytearray_value):
#     assert isinstance(
#         LIB.factory.create_deploy_approval(
#             account_info_secp256k1,
#             a_bytearray_value
#             ), 
#         LIB.types.DeployApproval
#         )


# def test_create_deploy_header_1(LIB, account_info, a_test_chain_id):
#     assert isinstance(
#         LIB.factory.create_deploy_header(
#             account_key=account_info.account_key,
#             body_hash=None,
#             chain_name=a_test_chain_id,
#             dependencies=[],
#             timestamp=datetime.datetime.utcnow(),
#             ttl="1day",
#         ), 
#         LIB.types.DeployHeader
#         )


# def test_create_deploy_header_2(LIB, account_info, a_test_chain_id):
#     assert isinstance(
#         LIB.factory.create_deploy_header(
#             account_key=account_info.account_key,
#             body_hash=None,
#             chain_name=a_test_chain_id
#         ), 
#         LIB.types.DeployHeader
#         )


# def test_create_deploy_session_for_transfer(LIB):
#     assert isinstance(
#         LIB.factory.create_session_for_transfer(
#             amount = 1e9,
#             correlation_id = random.randint(0, 124),
#             target = bytes([]),
#             ),
#         LIB.types.DeployExecutable_Transfer
#         )


# def test_create_deploy_payment_for_transfer(LIB):
#     assert isinstance(
#         LIB.factory.create_payment_for_transfer(
#             amount = 1e5,
#         ),
#         LIB.types.DeployExecutable_ModuleBytes
#         )