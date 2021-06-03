import datetime
import random


def _assert_named_arg(FACTORY, TYPES, value, cl_type):
    arg_name = f"a-{cl_type.typeof.name.lower()}-arg"
    arg = FACTORY.deploy.create_named_arg(arg_name, cl_type, value)
    assert isinstance(arg, TYPES.DeployNamedArg)


def _assert_named_arg_option(FACTORY, TYPES, value, inner_cl_type):
    cl_type = FACTORY.cl_type.create_option(inner_cl_type)
    for value in [value, None]:
        _assert_named_arg(FACTORY, TYPES, value, cl_type)   


def test_create_named_arg_of_type_optional_bool(FACTORY, TYPES, a_boolean):
    inner_cl_type = FACTORY.cl_type.create_simple(TYPES.CLType.BOOL)
    _assert_named_arg_option(FACTORY, TYPES, a_boolean, inner_cl_type)


def test_create_named_arg_of_type_optional_byte_array(FACTORY, TYPES, a_bytearray):
    size = len(a_bytearray)
    inner_cl_type = FACTORY.cl_type.create_byte_array(size)
    _assert_named_arg_option(FACTORY, TYPES, a_bytearray, inner_cl_type)


def test_create_named_arg_of_type_optional_i32(FACTORY, TYPES, a_i32):
    inner_cl_type = FACTORY.cl_type.create_simple(TYPES.CLType.I32)
    _assert_named_arg_option(FACTORY, TYPES, a_i32, inner_cl_type)


def test_create_named_arg_of_type_optional_i64(FACTORY, TYPES, a_i64):
    inner_cl_type = FACTORY.cl_type.create_simple(TYPES.CLType.I64)
    _assert_named_arg_option(FACTORY, TYPES, a_i64, inner_cl_type)


def test_create_named_arg_of_type_optional_key(FACTORY, TYPES, a_key):
    inner_cl_type = FACTORY.cl_type.create_simple(TYPES.CLType.KEY)
    _assert_named_arg_option(FACTORY, TYPES, a_key, inner_cl_type)


def test_create_named_arg_of_type_optional_public_key(FACTORY, TYPES, a_public_key):
    inner_cl_type = FACTORY.cl_type.create_simple(TYPES.CLType.PUBLIC_KEY)
    _assert_named_arg_option(FACTORY, TYPES, a_public_key, inner_cl_type)


def test_create_named_arg_of_type_optional_string(FACTORY, TYPES, a_string):
    inner_cl_type = FACTORY.cl_type.create_simple(TYPES.CLType.STRING)
    _assert_named_arg_option(FACTORY, TYPES, a_string, inner_cl_type)


def test_create_named_arg_of_type_optional_u8(FACTORY, TYPES, a_u8):
    inner_cl_type = FACTORY.cl_type.create_simple(TYPES.CLType.U8)
    _assert_named_arg_option(FACTORY, TYPES, a_u8, inner_cl_type)


def test_create_named_arg_of_type_optional_u32(FACTORY, TYPES, a_u32):
    inner_cl_type = FACTORY.cl_type.create_simple(TYPES.CLType.U32)
    _assert_named_arg_option(FACTORY, TYPES, a_u32, inner_cl_type)


def test_create_named_arg_of_type_optional_u64(FACTORY, TYPES, a_u64):
    inner_cl_type = FACTORY.cl_type.create_simple(TYPES.CLType.U64)
    _assert_named_arg_option(FACTORY, TYPES, a_u64, inner_cl_type)


def test_create_named_arg_of_type_optional_u128(FACTORY, TYPES, a_u128):
    inner_cl_type = FACTORY.cl_type.create_simple(TYPES.CLType.U128)
    _assert_named_arg_option(FACTORY, TYPES, a_u128, inner_cl_type)


def test_create_named_arg_of_type_optional_u256(FACTORY, TYPES, a_u256):
    inner_cl_type = FACTORY.cl_type.create_simple(TYPES.CLType.U256)
    _assert_named_arg_option(FACTORY, TYPES, a_u256, inner_cl_type)


def test_create_named_arg_of_type_optional_unit(FACTORY, TYPES, a_unit):
    inner_cl_type = FACTORY.cl_type.create_simple(TYPES.CLType.UNIT)
    _assert_named_arg_option(FACTORY, TYPES, a_unit, inner_cl_type)


def test_create_named_arg_of_type_optional_uref(FACTORY, TYPES, a_uref):
    inner_cl_type = FACTORY.cl_type.create_simple(TYPES.CLType.UREF)
    _assert_named_arg_option(FACTORY, TYPES, a_uref, inner_cl_type)
