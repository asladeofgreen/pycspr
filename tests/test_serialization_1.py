def _assert_round_trip(LIB, typeof, values):
    """Performs round trip serialisation assertion.
    
    """
    for encoding in LIB.CLEncoding:
        for value in values:
            encoded = LIB.encode(typeof, value, encoding)
            decoded = LIB.decode(typeof, encoded, encoding)
            assert value == decoded


def test_bool(LIB):
    """Asserts domain type instance: boolean.
    
    """
    values = (False, True, 0, 1)

    _assert_round_trip(LIB, LIB.CLType.BOOL, values)


def test_i32(LIB):
    """Asserts domain type instance: i32.
    
    """
    values = (-(2 ** 31), 0, (2 ** 31) - 1)

    _assert_round_trip(LIB, LIB.CLType.I32, values)

#     (
#         (-100000, [96, 121, 254, 255]),
#         (100000, [160, 134, 1, 0]),
#         (0, [0, 0, 0, 0]),
#         (-1, [255, 255, 255, 255]),
#     )

def test_i64(LIB):
    """Asserts domain type instance: I64.
    
    """
    values = (-(2 ** 63), 0, (2 ** 63) - 1)

    _assert_round_trip(LIB, LIB.CLType.I64, values)


def test_string(LIB):
    """Asserts domain type instance: string.
    
    """
    values = ("test_测试", "")

    _assert_round_trip(LIB, LIB.CLType.STRING, values)


def test_u8(LIB):
    """Asserts domain type instance: u8.
    
    """
    values = (0, 255)

    _assert_round_trip(LIB, LIB.CLType.U8, values)


def test_u32(LIB):
    """Asserts domain type instance: u32.
    
    """
    values = (0, (2 ** 32) - 1)

    _assert_round_trip(LIB, LIB.CLType.U32, values)


def test_u64(LIB):
    """Asserts domain type instance: u64.
    
    """
    values = (0, (2 ** 64) - 1)

    _assert_round_trip(LIB, LIB.CLType.U64, values)


def test_u128(LIB):
    """Asserts domain type instance: u128.
    
    """
    values = (0, (2 ** 128) - 1)

    _assert_round_trip(LIB, LIB.CLType.U128, values)


def test_u256(LIB):
    """Asserts domain type instance: u256.
    
    """
    values = (0, (2 ** 256) - 1)

    _assert_round_trip(LIB, LIB.CLType.U256, values)


def test_u512(LIB):
    """Asserts domain type instance: u512.
    
    """
    values = (0, (2 ** 512) - 1)

    _assert_round_trip(LIB, LIB.CLType.U512, values)


def test_unit(LIB):
    """Asserts domain type instance: unit.
    
    """
    values = (None, )

    _assert_round_trip(LIB, LIB.CLType.UNIT, values)
