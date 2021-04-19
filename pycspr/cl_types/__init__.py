import typing

from pycspr.cl_types.codecs import CODECS
from pycspr.cl_types.enums import CLEncoding
from pycspr.cl_types.enums import CLType



def decode(encoded: typing.Union[bytes, str], encoding: CLEncoding = CLEncoding.BYTES) -> object:
    """Returns domain type instance decoded from a previously encoded instance.

    :param encoded: Previously encoded domain type instance.
    :param encoding: A supported domain type encoding.

    :returns: Domain type instance.

    """
    if not isinstance(encoded, (bytes, str)):
        raise ValueError(f"Unsupported CL domain type instance: {encoded}")
    if encoding not in CLEncoding:
        raise TypeError(f"Unsupported CL type encoding: {encoding}")

    encoded = encoded if encoding == CLEncoding.BYTES else bytes.fromhex(encoded)

    try:
        typeof = CLType(encoded[0])
    except:
        raise TypeError(f"Unsupported CL type tag: {encoded[0]}")

    if typeof not in CODECS:
        raise TypeError(f"Unsupported CL type: {typeof}")

    return CODECS[typeof].decode(encoded[1:])


def encode(typeof: CLType, value: object, encoding: CLEncoding = CLEncoding.BYTES) -> typing.Union[bytes, str]:
    """Returns an encoded domain type instance.

    :param typeof: Type of domain instance being encoded.
    :param value: Domain instance being encoded.
    :param encoding: A supported domain type encoding.

    :returns: Domain instance appropriately encoded.

    """
    if typeof not in CODECS:
        raise TypeError(f"Unsupported CL type: {typeof}")
    if encoding not in CLEncoding:
        raise TypeError(f"Unsupported CL type encoding: {encoding}")

    def _format(as_bytes):
        return as_bytes if encoding == CLEncoding.BYTES else as_bytes.hex()

    codec = CODECS[typeof]
    if not codec.is_encodeable(value):
        raise ValueError(f"Invalid CL value : {typeof} :: {value}")

    return _format(
        codec.TYPEOF.value.to_bytes(1, 'big') + \
        codec.encode(value)
        )
