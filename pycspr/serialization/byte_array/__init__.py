from pycspr.serialization.byte_array import cl_bool
from pycspr.serialization.byte_array import cl_i32
from pycspr.serialization.byte_array import cl_i64
from pycspr.serialization.byte_array import cl_string
from pycspr.serialization.byte_array import cl_u8
from pycspr.serialization.byte_array import cl_u32
from pycspr.serialization.byte_array import cl_u64
from pycspr.serialization.byte_array import cl_u128
from pycspr.serialization.byte_array import cl_u256
from pycspr.serialization.byte_array import cl_u512
from pycspr.serialization.byte_array import cl_unit
from pycspr.serialization.utils import ByteArray
from pycspr.serialization.utils import CLType
from pycspr.serialization.utils import DecoderError
from pycspr.serialization.utils import EncoderError


# Map: CL type <-> codec.
CODECS = {
    CLType.BOOL: cl_bool,
    CLType.I32: cl_i32,
    CLType.I64: cl_i64,    
    CLType.STRING: cl_string,
    CLType.U8: cl_u8,
    CLType.U32: cl_u32,
    CLType.U64: cl_u64,
    CLType.U128: cl_u128,
    CLType.U256: cl_u256,
    CLType.U512: cl_u512,
    CLType.UNIT: cl_unit,
}


def decode(typeof: CLType, data: ByteArray) -> object:
    """Returns domain type instance decoded from a previously encoded instance.

    :param typeof: Domain type to which data can be mapped, e.g. BOOL.
    :param data: Domain data appropriately encoded.

    :returns: Domain type instance.

    """
    if typeof not in CODECS:
        raise DecoderError(encoding, "decoder unsupported")    

    return CODECS[typeof].decode(data)


def encode(typeof: CLType, value: object) -> ByteArray:
    """Returns an instance of a domain type encoded as a byte array.

    :param typeof: Domain type to which data can be mapped, e.g. BOOL.
    :param value: Domain type instance to be encoded.

    :returns: Domain instance appropriately encoded.

    """
    if typeof not in CODECS:
        raise EncoderError(typeof, "type encoder unsupported")    

    return CODECS[typeof].encode(value)
