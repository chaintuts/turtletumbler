# This file contains code for calculating a password/PIN hash
#
# Author: Josh McIntyre
#
import enum
import hashlib

# This class contains code for constructing a password hash
class PWHash:

    # Class constants
    class HashAlgo(enum.Enum):
        SHA256 = "SHA-256"

    # Construct the hash object
    def __init__(self, password, algorithm=HashAlgo.SHA256):
        
        self.password = password
        self.password_hash = self.hash_password(self.password)

    # Generate the password hash
    def hash_password(self, password):

        hasher = self._get_hasher()
        hasher.update(password.encode())
        return hasher.hexdigest()

    # Construct the hasher
    def _get_hasher(self, algorithm=HashAlgo.SHA256):

        if algorithm == self.HashAlgo.SHA256:
            return hashlib.sha256()
