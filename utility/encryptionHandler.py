#pip3 install cryptography

import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from abc import ABC

class encryption(ABC):

    @staticmethod
    def encryptString(string):
        print("encryptPassword()")
        key = encryption.generateKey()
        token = encryption.encrypt(string, key)
        strtoken = token.decode("ascii")
        strkey = key.decode("ascii")
        return strtoken, strkey

    @staticmethod
    def generateKey():
        passKey = b"yourPassKey"
        salt = os.urandom(16)
        kdf = PBKDF2HMAC(
                    algorithm=hashes.SHA256(),
                    length=32,
                    salt=salt,
                    iterations=100000,
                    backend=default_backend()
                    )
        key = base64.urlsafe_b64encode(kdf.derive(passKey))
        return key

    @staticmethod
    def encrypt(string, key):
        FernetObj = Fernet(key)
        token = FernetObj.encrypt(bytes(string, encoding='utf8'))
        return token

    @staticmethod
    def decryptString(string, key):
        FernetObj = Fernet(key)
        token = FernetObj.decrypt(bytes(string, encoding='utf8'))
        return token




    # def encrypt(self, string):
    #     passKey = "PK@951753"
    #     salt = os.urandom(16)
    #     kdf = PBKDF2HMAC(
    #                 algorithm=hashes.SHA256(),
    #                 length=32,
    #                 salt=salt,
    #                 iterations=100000,
    #                 backend=default_backend()
    #                 )

    #     key = base64.urlsafe_b64encode(kdf.derive(passKey))
    #     FernetObj = Fernet(key)
    #     token = FernetObj.encrypt(string)
    #     return token, salt


