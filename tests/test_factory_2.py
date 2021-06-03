import datetime
import random

# class CLType(enum.Enum):
#     """Enumeration over set of CL types.
    
#     """

#     KEY = 11
#     UREF = 12
#     PUBLIC_KEY = 22

#     OPTION = 13
#     LIST = 14
#     RESULT = 16
#     MAP = 17
#     TUPLE_1 = 18
#     TUPLE_2 = 19
#     TUPLE_3 = 20
#     ANY = 21


def test_create_named_arg_of_type_bool(FACTORY, TYPES, a_boolean_value):
    cl_type = FACTORY.cl_type.create_simple(TYPES.CLType.BOOL)
    arg = FACTORY.deploy.create_named_arg(
        "a-boolean-arg",
        cl_type,
        a_boolean_value
        )
    assert isinstance(arg, TYPES.DeployNamedArg)


def test_create_named_arg_of_type_byte_array(FACTORY, TYPES, a_bytearray_value):
    cl_type = FACTORY.cl_type.create_byte_array(len(a_bytearray_value))
    arg = FACTORY.deploy.create_named_arg(
        "a-byte-array-arg",
        cl_type,
        a_bytearray_value
        )
    assert isinstance(arg, TYPES.DeployNamedArg)


def test_create_named_arg_of_type_i32(LIB, FACTORY, TYPES, a_i32_value):
    cl_type = FACTORY.cl_type.create_simple(TYPES.CLType.I32)
    arg = FACTORY.deploy.create_named_arg(
        "a-i32-arg",
        cl_type,
        a_i32_value
        )
    assert isinstance(arg, TYPES.DeployNamedArg)


def test_create_named_arg_of_type_i64(LIB, FACTORY, TYPES, a_i64_value):
    cl_type = FACTORY.cl_type.create_simple(TYPES.CLType.I64)
    arg = FACTORY.deploy.create_named_arg(
        "a-i64-arg",
        cl_type,
        a_i64_value
        )
    assert isinstance(arg, TYPES.DeployNamedArg)


def test_create_named_arg_of_type_key(FACTORY, TYPES, a_key_value):
    cl_type = FACTORY.cl_type.create_simple(TYPES.CLType.KEY)
    arg = FACTORY.deploy.create_named_arg(
        "a-key-arg",
        cl_type,
        a_key_value
        )
    assert isinstance(arg, TYPES.DeployNamedArg)


def test_create_named_arg_of_type_public_key(FACTORY, TYPES, a_public_key_value):
    cl_type = FACTORY.cl_type.create_simple(TYPES.CLType.PUBLIC_KEY)
    arg = FACTORY.deploy.create_named_arg(
        "a-public-key-arg",
        cl_type,
        a_public_key_value
        )
    assert isinstance(arg, TYPES.DeployNamedArg)


def test_create_named_arg_of_type_string(FACTORY, TYPES, a_string_value):
    cl_type = FACTORY.cl_type.create_simple(TYPES.CLType.STRING)
    arg = FACTORY.deploy.create_named_arg(
        "a-string-arg",
        cl_type,
        a_string_value
        )
    assert isinstance(arg, TYPES.DeployNamedArg)


def test_create_named_arg_of_type_u8(FACTORY, TYPES, a_u8_value):
    cl_type = FACTORY.cl_type.create_simple(TYPES.CLType.U8)
    arg = FACTORY.deploy.create_named_arg(
        "a-u8-arg",
        cl_type,
        a_u8_value
        )
    assert isinstance(arg, TYPES.DeployNamedArg)


def test_create_named_arg_of_type_u32(FACTORY, TYPES, a_u32_value):
    cl_type = FACTORY.cl_type.create_simple(TYPES.CLType.U32)
    arg = FACTORY.deploy.create_named_arg(
        "a-u32-arg",
        cl_type,
        a_u32_value
        )
    assert isinstance(arg, TYPES.DeployNamedArg)


def test_create_named_arg_of_type_u64(FACTORY, TYPES, a_u64_value):
    cl_type = FACTORY.cl_type.create_simple(TYPES.CLType.U64)
    arg = FACTORY.deploy.create_named_arg(
        "a-u64-arg",
        cl_type,
        a_u64_value
        )
    assert isinstance(arg, TYPES.DeployNamedArg)


def test_create_named_arg_of_type_u128(FACTORY, TYPES, a_u128_value):
    cl_type = FACTORY.cl_type.create_simple(TYPES.CLType.U128)
    arg = FACTORY.deploy.create_named_arg(
        "a-u128-arg",
        cl_type,
        a_u128_value
        )
    assert isinstance(arg, TYPES.DeployNamedArg)


def test_create_named_arg_of_type_u256(FACTORY, TYPES, a_u256_value):
    cl_type = FACTORY.cl_type.create_simple(TYPES.CLType.U256)
    arg = FACTORY.deploy.create_named_arg(
        "a-u256-arg",
        cl_type,
        a_u256_value
        )
    assert isinstance(arg, TYPES.DeployNamedArg)


def test_create_named_arg_of_type_unit(FACTORY, TYPES, a_unit_value):
    cl_type = FACTORY.cl_type.create_simple(TYPES.CLType.UNIT)
    arg = FACTORY.deploy.create_named_arg(
        "a-unit-arg",
        cl_type,
        a_unit_value
        )
    assert isinstance(arg, TYPES.DeployNamedArg)


def test_create_named_arg_of_type_uref(FACTORY, TYPES, a_uref_value):
    cl_type = FACTORY.cl_type.create_simple(TYPES.CLType.UREF)
    arg = FACTORY.deploy.create_named_arg(
        "a-uref-arg",
        cl_type,
        a_uref_value
        )
    assert isinstance(arg, TYPES.DeployNamedArg)
