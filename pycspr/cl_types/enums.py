import enum



class CLType(enum.Enum):
    """Enumeration over set of supported CL types.
    
    """
    # --------------------------------
    # Primitive types.
    # --------------------------------
    BOOL = 0
    I32 = 1
    I64 = 2
    U8 = 3
    U32 = 4
    U64 = 5
    U128 = 6
    U256 = 7
    U512 = 8

    # --------------------------------
    # String + variants.
    # --------------------------------
    UNIT = 9
    STRING = 10
    KEY = 11
    UREF = 12
    PUBLIC_KEY = 22
    ACCOUNT_HASH = 23 # ???

    # --------------------------------
    # Complex.
    # --------------------------------
    OPTION = 13
    LIST = 14
    BYTE_ARRAY = 15
    RESULT = 16
    MAP = 17
    TUPLE_1 = 18
    TUPLE_2 = 19
    TUPLE_3 = 20
    ANY = 21


class CLEncoding(enum.Enum):
    """Enumeration over set of supported value encodings.
    
    """
    BYTES = enum.auto()
    HEX = enum.auto()
