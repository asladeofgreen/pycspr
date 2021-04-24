from pycspr.serialization import byte_stream
from pycspr.serialization.utils import HexString
from pycspr.serialization.utils import CLType
from pycspr.serialization.utils import DecoderError
from pycspr.serialization.utils import EncoderError



def decode(typeof: CLType, data: HexString) -> object:
    """Returns domain type instance decoded from a previously encoded instance.

    :param typeof: Domain type to which data can be mapped, e.g. BOOL.
    :param data: Domain data appropriately encoded.

    :returns: Domain type instance.

    """
    return byte_stream.decode(typeof, bytes.fromhex(data))


def encode(typeof: CLType, value: object) -> HexString:
    """Returns an instance of a domain type encoded as a byte array.

    :param typeof: Domain type to which data can be mapped, e.g. BOOL.
    :param value: Domain type instance to be encoded.

    :returns: Domain instance appropriately encoded.

    """
    return byte_stream.encode(typeof, value).hex()
