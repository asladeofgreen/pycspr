from pycspr.serialization import byte_array
from pycspr.serialization.utils import ByteStream
from pycspr.serialization.utils import CLType
from pycspr.serialization.utils import DecoderError
from pycspr.serialization.utils import EncoderError



def decode(typeof: CLType, data: ByteStream) -> object:
    """Returns domain type instance decoded from a previously encoded instance.

    :param typeof: Domain type to which data can be mapped, e.g. BOOL.
    :param data: Domain data appropriately encoded.

    :returns: Domain type instance.

    """
    return byte_array.decode(typeof, [i for i in data])


def encode(typeof: CLType, value: object) -> ByteStream:
    """Returns an instance of a domain type encoded as a byte array.

    :param typeof: Domain type to which data can be mapped, e.g. BOOL.
    :param value: Domain type instance to be encoded.

    :returns: Domain instance appropriately encoded.

    """
    return bytes(byte_array.encode(typeof, value))
