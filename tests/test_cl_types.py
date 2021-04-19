def _assert_round_trip(LIB, typeof, value):
    for encoding in LIB.CLEncoding:
        encoded = LIB.encode(typeof, value, encoding)
        decoded = LIB.decode(encoded, encoding)
        assert value == decoded


def test_cl_type_bool(LIB):
    """Asserts domain type instance: boolean.
    
    """
    for value in (False, True):
        _assert_round_trip(LIB, LIB.CLType.BOOL, value)


def test_cl_type_u8(LIB):
    """Asserts domain type instance: u8.
    
    """
    for value in (0, 1, 255):
        _assert_round_trip(LIB, LIB.CLType.U8, value)


def test_cl_type_u32(LIB):
    """Asserts domain type instance: u32.
    
    """
    for value in (0, 1, 4294967295):
        _assert_round_trip(LIB, LIB.CLType.U32, value)
