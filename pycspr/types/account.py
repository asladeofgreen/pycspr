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


    @property
    def account_key(self):
        """Returns on-chain account key.

        """ 
        return crypto.get_account_key(self.algo, self.pbk.hex())


    def get_signature(self, data: bytes) -> bytes:
        """Get signature over payload.
        
        """
        return crypto.get_signature(data, self.pvk, self.algo)
