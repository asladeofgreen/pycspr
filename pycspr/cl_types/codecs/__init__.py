from pycspr.cl_types.codecs import cl_bool
from pycspr.cl_types.codecs import cl_u8
from pycspr.cl_types.codecs import cl_u32
from pycspr.cl_types.enums import CLType



# Map: CL type <-> codec.
CODECS = {
    v.TYPEOF: v for v in [
        cl_bool,
        cl_u8,
        cl_u32,
    ]
}
