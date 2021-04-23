from pycspr.serialization.byte_array import cl_bool
from pycspr.serialization.byte_array import cl_i32
from pycspr.serialization.byte_array import cl_i64
from pycspr.serialization.byte_array import cl_u8
from pycspr.serialization.byte_array import cl_u32
from pycspr.serialization.byte_array import cl_u64
from pycspr.serialization.byte_array import cl_u128
from pycspr.serialization.byte_array import cl_u256
from pycspr.serialization.byte_array import cl_u512
from pycspr.serialization.utils import CLType



# Map: CL type <-> codec.
CODECS = {
    CLType.BOOL: cl_bool,
    CLType.I32: cl_i32,
    CLType.I64: cl_i64,    
    CLType.U8: cl_u8,
    CLType.U32: cl_u32,
    CLType.U64: cl_u64,
    CLType.U128: cl_u128,
    CLType.U256: cl_u256,
    CLType.U512: cl_u512,
}
