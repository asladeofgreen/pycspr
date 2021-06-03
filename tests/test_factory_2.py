import datetime
import random

# class CLType(enum.Enum):
#     """Enumeration over set of CL types.
    
#     """

#     OPTION = 13
#     LIST = 14
#     RESULT = 16
#     MAP = 17
#     TUPLE_1 = 18
#     TUPLE_2 = 19
#     TUPLE_3 = 20
#     ANY = 21


def test_create_named_arg_of_type_bool(FACTORY, TYPES, a_boolean):
    _assert_named_arg_simple(FACTORY, TYPES, a_boolean, TYPES.CLType.BOOL)


def test_create_named_arg_of_type_byte_array(FACTORY, TYPES, a_bytearray):
    size = len(a_bytearray)
    cl_type = FACTORY.cl_type.create_byte_array(size)
    _assert_named_arg(FACTORY, TYPES, a_bytearray, cl_type)


def test_create_named_arg_of_type_i32(LIB, FACTORY, TYPES, a_i32):
    _assert_named_arg_simple(FACTORY, TYPES, a_i32, TYPES.CLType.I32)


def test_create_named_arg_of_type_i64(LIB, FACTORY, TYPES, a_i64):
    _assert_named_arg_simple(FACTORY, TYPES, a_i64, TYPES.CLType.I64)


def test_create_named_arg_of_type_key(FACTORY, TYPES, a_key_value):
    _assert_named_arg_simple(FACTORY, TYPES, a_key_value, TYPES.CLType.KEY)


def test_create_named_arg_of_type_public_key(FACTORY, TYPES, a_public_key_value):
    _assert_named_arg_simple(FACTORY, TYPES, a_public_key_value, TYPES.CLType.PUBLIC_KEY)


def test_create_named_arg_of_type_string(FACTORY, TYPES, a_string_value):
    _assert_named_arg_simple(FACTORY, TYPES, a_string_value, TYPES.CLType.STRING)


def test_create_named_arg_of_type_u8(FACTORY, TYPES, a_u8_value):
    _assert_named_arg_simple(FACTORY, TYPES, a_u8_value, TYPES.CLType.U8)


def test_create_named_arg_of_type_u32(FACTORY, TYPES, a_u32_value):
    _assert_named_arg_simple(FACTORY, TYPES, a_u32_value, TYPES.CLType.U32)


def test_create_named_arg_of_type_u64(FACTORY, TYPES, a_u64_value):
    _assert_named_arg_simple(FACTORY, TYPES, a_u64_value, TYPES.CLType.U64)


def test_create_named_arg_of_type_u128(FACTORY, TYPES, a_u128_value):
    _assert_named_arg_simple(FACTORY, TYPES, a_u128_value, TYPES.CLType.U128)


def test_create_named_arg_of_type_u256(FACTORY, TYPES, a_u256_value):
    _assert_named_arg_simple(FACTORY, TYPES, a_u256_value, TYPES.CLType.U256)


def test_create_named_arg_of_type_unit(FACTORY, TYPES, a_unit_value):
    _assert_named_arg_simple(FACTORY, TYPES, a_unit_value, TYPES.CLType.UNIT)


def test_create_named_arg_of_type_uref(FACTORY, TYPES, a_uref_value):
    _assert_named_arg_simple(FACTORY, TYPES, a_uref_value, TYPES.CLType.UREF)


def _assert_named_arg(FACTORY, TYPES, value, cl_type):
    arg_name = f"a-{cl_type.typeof.name.lower()}-arg"
    arg = FACTORY.deploy.create_named_arg(arg_name, cl_type, value)
    assert isinstance(arg, TYPES.DeployNamedArg)


def _assert_named_arg_simple(FACTORY, TYPES, value, cl_typeof):
    cl_type = FACTORY.cl_type.create_simple(cl_typeof)
    _assert_named_arg(FACTORY, TYPES, value, cl_type)
