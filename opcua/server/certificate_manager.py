import logging


class CertificateManager(object):

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.certificate_manager = self.default_certificate_manager

    def default_certificate_manager(self, isession, certificate, signature):
        """
        Default certificate_manager, does nothing.
        """
        self.logger.warning("There is no certificate manager. You have to set one to manage the client identity.")
        return True

    def set_certificate_manager(self, certificate_manager):
        """
        set up a function which will check for the authorize client certificate. Input function takes certificate
        and signature as parameters and returns True of client is allowed access, False otherwise.
        """
        self.certificate_manager = certificate_manager

    def check_certificate_token(self, isession, client_params):
        """
        call the certificate manager
        """
        return self.certificate_manager(isession, client_params.UserIdentityToken.CertificateData,
                                        client_params.UserTokenSignature.Signature)
