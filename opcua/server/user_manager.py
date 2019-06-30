
import logging
from enum import Enum
from struct import unpack_from

use_crypto = True
try:
    from opcua.crypto import uacrypto
except ImportError:
    logging.getLogger(__name__).warning("cryptography is not installed, use of crypto disabled")
    use_crypto = False


class UserManager(object):

    class User(Enum):
        """
        Define some default users.
        """
        Admin = 0
        Anonymous = 1
        User = 3

    def __init__(self, parent):
        self.logger = logging.getLogger(__name__)
        assert(hasattr(parent, 'private_key'))
        self._parent = parent
        self.user_manager = self.default_user_manager
        self.allow_remote_admin = True

    @property
    def private_key(self):
        return self._parent.private_key

    def default_user_manager(self, isession, userName, password):
        """
        Default user_manager, does nothing much but check for admin
        """
        if self.allow_remote_admin and userName in ("admin", "Admin"):
            isession.user = UserManager.User.Admin
        return True

    def set_user_manager(self, user_manager):
        """
        set up a function which that will check for authorize users. Input function takes username
        and password as paramters and returns True of user is allowed access, False otherwise.
        """
        self.user_manager = user_manager

    def check_user_token(self, isession, token):
        """
        unpack the username and password for the benefit of the user defined user manager
        """
        userName = token.UserName
        passwd = token.Password

        # decrypt password is we can
        if str(token.EncryptionAlgorithm) != "None":
            if use_crypto == False:
                return False;
            try:
                if token.EncryptionAlgorithm == "http://www.w3.org/2001/04/xmlenc#rsa-1_5":
                    raw_pw = uacrypto.decrypt_rsa15(self.private_key, passwd)
                elif token.EncryptionAlgorithm == "http://www.w3.org/2001/04/xmlenc#rsa-oaep":
                    raw_pw = uacrypto.decrypt_rsa_oaep(self.private_key, passwd)
                else:
                    self.logger.warning("Unknown password encoding '{0}'".format(token.EncryptionAlgorithm))
                    return False
                length = unpack_from('<I', raw_pw)[0] - len(isession.nonce)
                passwd = raw_pw[4:4 + length]
                passwd = passwd.decode('utf-8')
            except Exception as exp:
                self.logger.warning("Unable to decrypt password")
                return False
        else:
            try:
                passwd = passwd.decode('utf-8')
            except:
                self.logger.warning("Unable to decode password")

        # call user_manager
        return self.user_manager(isession, userName, passwd)
