from pycspr.cl_types.enums import CLType
from pycspr.cl_types import exceptions



# CL type.
TYPEOF = CLType.BOOL

# Length when encoded.
_ENCODED_LENGTH: int = 1


def decode(encoded: bytes) -> bool:
    """Returns previously encoded domain type instance.
    
    :param encoded: Previously encoded domain type instance.

    :returns: Decoded domain type instance.

    """
    if not is_decodeable(encoded):
        raise exceptions.DecodingError(TYPEOF, encoded)

    return bool(encoded[0])


def encode(value: bool) -> bytes:
    """Returns an encoded domain type instance.
    
    :param value: Domain type instance.

    :returns: Encoded domain type instance.

    """
    if not is_encodeable(value):
        raise exceptions.EncodingError(TYPEOF, value)

    return int(value).to_bytes(get_encoded_length(value), 'big')


def get_encoded_length(_: bool) -> int:
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
           encoded[0] in (0, 1) 


def is_encodeable(value: bool):
    """A predicate returning a flag indicating whether a domain type instance can be encoded.
    
    :param value: Domain type instance.

    :returns: A flag indicating whether domain type instance can be encoded.

    """
    return isinstance(value, bool)
