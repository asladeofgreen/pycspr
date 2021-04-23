from pycspr.serialization.utils import ByteArray



# Length when encoded.
_ENCODED_LENGTH: int = 1


# Decodes input data.
decode = lambda v: bool(v[0])


# Encodes a domain type instance.
encode = lambda v: [int(v)]


# Returns length in bytes of encoded data.
get_encoded_length = lambda _: _ENCODED_LENGTH


# A predicate returning a flag indicating whether encoded data can be decoded.
is_decodeable = lambda encoded: isinstance(encoded, list) and \
                                len(encoded) == _ENCODED_LENGTH and \
                                encoded[0] in (0, 1)


# A predicate returning a flag indicating whether value can be encoded.
is_encodeable = lambda v: isinstance(v, bool)
