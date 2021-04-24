import typing

from pycspr.serialization import byte_array
from pycspr.serialization import byte_stream
from pycspr.serialization import hex_string
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
    CLEncoding.BYTE_STREAM: byte_stream,
    CLEncoding.HEX: hex_string,
}


def decode(
    typeof: CLType,
    data: typing.Union[ByteArray, ByteStream, HexString],
    encoding: CLEncoding,
    ) -> object:
    """Returns domain type instance decoded from a previously encoded instance.

    :param typeof: Domain type to which data can be mapped, e.g. BOOL.
    :param data: Domain data appropriately encoded.
    :param encoding: A supported domain type encoding, e.g. BYTE_ARRAY.

    :returns: Domain type instance.

    """
    if encoding not in CODECS:
        raise DecoderError(encoding, "decoder unsupported")    

    return CODECS[encoding].decode(typeof, data)


def encode(
    typeof: CLType,
    value: object,
    encoding: CLEncoding,
    ) -> typing.Union[ByteArray, ByteStream, HexString]:
    """Returns an instance of a domain type encoded as a byte array.

    :param typeof: Domain type to which data can be mapped, e.g. BOOL.
    :param value: Domain type instance to be encoded.
    :param encoding: A supported domain type encoding, e.g. BYTE_ARRAY.

    :returns: Domain instance appropriately encoded.

    """
    if encoding not in CODECS:
        raise EncoderError(encoding, "encoder unsupported")    

    return CODECS[encoding].encode(typeof, value)
