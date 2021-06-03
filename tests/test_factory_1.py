import datetime
import random



def test_create_named_arg_bool(FACTORY, TYPES, a_boolean):
    cl_type = FACTORY.cl_type.create_simple(TYPES.CLType.BOOL)
    _assert_arg(FACTORY, TYPES, a_boolean, cl_type)


def test_create_named_arg_byte_array(FACTORY, TYPES, a_bytearray):
    size = len(a_bytearray)
    cl_type = FACTORY.cl_type.create_byte_array(size)
    _assert_arg(FACTORY, TYPES, a_bytearray, cl_type)


def test_create_named_arg_i32(FACTORY, TYPES, a_i32):
    cl_type = FACTORY.cl_type.create_simple(TYPES.CLType.I32)
    _assert_arg(FACTORY, TYPES, a_i32, cl_type)


def test_create_named_arg_i64(FACTORY, TYPES, a_i64):
    cl_type = FACTORY.cl_type.create_simple(TYPES.CLType.I64)
    _assert_arg(FACTORY, TYPES, a_i64, cl_type)


def test_create_named_arg_key(FACTORY, TYPES, a_key):
    cl_type = FACTORY.cl_type.create_simple(TYPES.CLType.KEY)
    _assert_arg(FACTORY, TYPES, a_key, cl_type)


def test_create_named_arg_list(FACTORY, TYPES, a_list_of_integers):
    cl_type_inner = FACTORY.cl_type.create_simple(TYPES.CLType.U64)
    cl_type = FACTORY.cl_type.create_list(cl_type_inner)
    _assert_arg(FACTORY, TYPES, a_list_of_integers, cl_type)


def test_create_named_arg_map(FACTORY, TYPES, a_map_of_string_to_integer):
    cl_type_key = FACTORY.cl_type.create_simple(TYPES.CLType.STRING)
    cl_type_value = FACTORY.cl_type.create_simple(TYPES.CLType.U32)
    cl_type = FACTORY.cl_type.create_map(cl_type_key, cl_type_value)
    _assert_arg(FACTORY, TYPES, a_map_of_string_to_integer, cl_type)


def test_create_named_arg_public_key(FACTORY, TYPES, a_public_key):
    cl_type = FACTORY.cl_type.create_simple(TYPES.CLType.PUBLIC_KEY)
    _assert_arg(FACTORY, TYPES, a_public_key, cl_type)


def test_create_named_arg_string(FACTORY, TYPES, a_string):
    cl_type = FACTORY.cl_type.create_simple(TYPES.CLType.STRING)
    _assert_arg(FACTORY, TYPES, a_string, cl_type)


def test_create_named_arg_tuple_1(FACTORY, TYPES, a_string):
    value = (a_string, )
    cl_type_t0 = FACTORY.cl_type.create_simple(TYPES.CLType.STRING)
    cl_type = FACTORY.cl_type.create_tuple_1(cl_type_t0)
    _assert_arg(FACTORY, TYPES, a_string, cl_type)


def test_create_named_arg_tuple_2(FACTORY, TYPES, a_string, a_u256):
    value = (a_string, a_u256)
    cl_type_t0 = FACTORY.cl_type.create_simple(TYPES.CLType.STRING)
    cl_type_t1 = FACTORY.cl_type.create_simple(TYPES.CLType.U256)
    cl_type = FACTORY.cl_type.create_tuple_2(cl_type_t0, cl_type_t1)
    _assert_arg(FACTORY, TYPES, value, cl_type)


def test_create_named_arg_tuple_3(FACTORY, TYPES, a_string, a_u256, a_key):
    value = (a_string, a_u256, a_key)
    cl_type_t0 = FACTORY.cl_type.create_simple(TYPES.CLType.STRING)
    cl_type_t1 = FACTORY.cl_type.create_simple(TYPES.CLType.U256)
    cl_type_t2 = FACTORY.cl_type.create_simple(TYPES.CLType.KEY)
    cl_type = FACTORY.cl_type.create_tuple_3(cl_type_t0, cl_type_t1, cl_type_t2)
    _assert_arg(FACTORY, TYPES, value, cl_type)


def test_create_named_arg_u8(FACTORY, TYPES, a_u8):
    cl_type = FACTORY.cl_type.create_simple(TYPES.CLType.U8)    
    _assert_arg(FACTORY, TYPES, a_u8, cl_type)


def test_create_named_arg_u32(FACTORY, TYPES, a_u32):
    cl_type = FACTORY.cl_type.create_simple(TYPES.CLType.U32)    
    _assert_arg(FACTORY, TYPES, a_u32, cl_type)


def test_create_named_arg_u64(FACTORY, TYPES, a_u64):
    cl_type = FACTORY.cl_type.create_simple(TYPES.CLType.U64)    
    _assert_arg(FACTORY, TYPES, a_u64, cl_type)


def test_create_named_arg_u128(FACTORY, TYPES, a_u128):
    cl_type = FACTORY.cl_type.create_simple(TYPES.CLType.U128)    
    _assert_arg(FACTORY, TYPES, a_u128, cl_type)


def test_create_named_arg_u256(FACTORY, TYPES, a_u256):
    cl_type = FACTORY.cl_type.create_simple(TYPES.CLType.U256)    
    _assert_arg(FACTORY, TYPES, a_u256, cl_type)


def test_create_named_arg_unit(FACTORY, TYPES, a_unit):
    cl_type = FACTORY.cl_type.create_simple(TYPES.CLType.UNIT)    
    _assert_arg(FACTORY, TYPES, a_unit, cl_type)


def test_create_named_arg_uref(FACTORY, TYPES, a_uref):
    cl_type = FACTORY.cl_type.create_simple(TYPES.CLType.UREF)    
    _assert_arg(FACTORY, TYPES, a_uref, cl_type)


def _assert_arg(FACTORY, TYPES, value, cl_type):
    # Assert named arg can be instantiated.
    arg_name = f"a-{cl_type.typeof.name.lower()}-arg"
    arg = FACTORY.deploy.create_named_arg(arg_name, cl_type, value)
    assert isinstance(arg, TYPES.DeployNamedArg)

    # Assert optional named arg can be instantiated.
    cl_type = FACTORY.cl_type.create_option(cl_type)
    for value in [value, None]:
        arg = FACTORY.deploy.create_named_arg(f"{arg_name}-optional", cl_type, value)
        assert isinstance(arg, TYPES.DeployNamedArg)
