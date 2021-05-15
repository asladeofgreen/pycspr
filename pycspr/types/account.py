import dataclasses

from pycspr import crypto



@dataclasses.dataclass
class AccountKeyInfo:
    """Encapsulates information associated with an external account.
    
    """
    # Private key as bytes - sensitive material !
    pvk: bytes

    # Public key as bytes.
    pbk: bytes

    # Algorithm used to generate ECC key pair.
    algo: crypto.KeyAlgorithm = crypto.KeyAlgorithm.ED25519


    def get_signature(self, data: bytes) -> bytes:
        """Get signature over payload.
        
        """
        return crypto.get_signature(self.pvk, data, self.algo)
