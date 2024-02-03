from django.contrib.auth import get_user_model

from PPM.models import *

user_class = get_user_model()


class AccessRequest:
    # package, package_version, user, token_pass, token_user, action
    def __init__(self, package: Packages,
                 user: user_class, token_pass: str, token_user: str, action,ip_address:str):

        self.package = package
        self.user = user
        self.token_pass = token_pass
        self.token_user = token_user
        self.action = action
        self.ip_address = ip_address


