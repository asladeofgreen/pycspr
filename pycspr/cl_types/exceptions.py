from pycspr.cl_types.enums import CLType



class DecodingError(ValueError):
    """Raised whenever domain type instance decoding fails.

    """
    def __init__(self, typeof: CLType, encoded: bytes):
        """Object constructor.

        """
        msg = f"Non-decodeable CL value: {typeof} :: {encoded}"
        super(DecodingError, self).__init__(msg)


class EncodingError(ValueError):
    """Raised whenever domain type instance encoding fails.

    """
    def __init__(self, typeof: CLType, value: object):
        """Object constructor.

        """
        msg = f"Non-encodeable CL value: {typeof} :: {value}"
        super(EncodingError, self).__init__(msg)
