"""
This general module provides all setup-shared feature classes.
"""
from ..lib.features import ValidRegisteredUserFeature


# Server Features
class MyValidRegisteredUserFeature(ValidRegisteredUserFeature):
    """
    This feature provides the user credentials for our balderexample-loginserver. The user is valid for all access
    strategies.
    """
    def get_valid_user(self):
        """
        This method returns a valid (user, password) pair - valid means that the user is known and could work with
        the server.

        :return: a tuple with a valid user and a valid password
        """
        return "guest", "guest12345"
