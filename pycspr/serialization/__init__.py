import typing

from pycspr.serialization import byte_array
from pycspr.serialization.utils import ByteArray
from pycspr.serialization.utils import ByteStream
from pycspr.serialization.utils import CLEncoding
from pycspr.serialization.utils import CLType
from pycspr.serialization.utils import DecoderError
from pycspr.serialization.utils import EncoderError
from pycspr.serialization.utils import HexString



# Map: CL encoding <-> codec.
CODECS = {
    CLEncoding.BYTE_ARRAY: byte_array,
}


def decode(
    data,
    typeof: CLType,
    encoding: CLEncoding,
    ) -> object:
    """Returns domain type instance decoded from a previously encoded instance.

    :param data: Domain data appropriately encoded.
    :param typeof: Domain type to which data can be mapped, e.g. BOOL.
    :param encoding: A supported domain type encoding, e.g. BYTE_ARRAY.

    :returns: Domain type instance.

    """
    if encoding not in CODECS or typeof not in CODECS[encoding].CODECS:
        raise DecoderError(encoding, "decoder unsupported")    

    return CODECS[encoding].CODECS[typeof].decode(data)


def encode(
    value: object,
    typeof: CLType,
    encoding: CLEncoding,
    ):
    """Returns an instance of a domain type encoded as a byte array.

    :param value: Domain type instance to be encoded.
    :param typeof: Domain type to which data can be mapped, e.g. BOOL.
    :param encoding: A supported domain type encoding, e.g. BYTE_ARRAY.

    :returns: Domain instance appropriately encoded.

    """
    if encoding not in CODECS:
        raise EncoderError(encoding, "encoder unsupported")    
    if typeof not in CODECS[encoding].CODECS:
        raise EncoderError(typeof, "type encoder unsupported")    

    return CODECS[encoding].CODECS[typeof].encode(value)
