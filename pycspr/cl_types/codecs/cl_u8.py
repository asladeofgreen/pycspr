from pycspr.cl_types.enums import CLType
from pycspr.cl_types import exceptions



# CL type.
TYPEOF = CLType.U8

# Length when encoded.
_ENCODED_LENGTH: int = 1

# Dimension constraint.
_MIN_SIZE = 0
_MAX_SIZE = (2 ** 8) - 1


def decode(encoded: bytes) -> int:
    """Returns previously encoded domain type instance.
    
    :param encoded: Previously encoded domain type instance.

    :returns: Decoded domain type instance.

    """
    if not is_decodeable(encoded):
        raise exceptions.DecodingError(TYPEOF, encoded)

    return int.from_bytes(encoded, 'big')


def encode(value: int) -> bytes:
    """Returns an encoded domain type instance.
    
    :param value: Domain type instance.

    :returns: Encoded domain type instance.

    """
    if not is_encodeable(value):
        raise exceptions.EncodingError(TYPEOF, value)

    return value.to_bytes(get_encoded_length(value), 'big')


def get_encoded_length(_: int) -> int:
    """Returns expected length of encoded domain type instance.
    
    """
    return _ENCODED_LENGTH


def is_decodeable(encoded: bytes):
    """A predicate returning a flag indicating whether encoded byte array can be decoded.
    
    :param encoded: Previously encoded domain type instance.

    :returns: A flag indicating whether encoded byte array can be decoded.

    """
    return isinstance(encoded, bytes) and \
           len(encoded) == _ENCODED_LENGTH and \
           _MIN_SIZE <= encoded[0] <= _MAX_SIZE 


def is_encodeable(value: int):
    """A predicate returning a flag indicating whether a domain type instance can be encoded.
    
    :param value: Domain type instance.

    :returns: A flag indicating whether domain type instance can be encoded.

    """
    return isinstance(value, int) and \
           _MIN_SIZE <= value <= _MAX_SIZE
