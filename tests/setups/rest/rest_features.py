import balder
from ...lib.features import InsertCredentialsFeature, ViewInternalPageFeature, BasicAuthManager


# Server features
class UserApiFeature(balder.Feature):
    """
    This feature provides the api routes to access the user page
    """
    @property
    def url_users(self):
        return "http://localhost:8000/api/users"


# Client features
class MyInsertCredentialsFeature(InsertCredentialsFeature):
    """
    This feature allows inserting credentials into a login system
    """
    class Server(InsertCredentialsFeature.Server):
        pass

    basic_auth_manager = BasicAuthManager()
    username = None
    password = None

    def insert_username(self, username):
        """
        This method inserts the username into the element, the server vDevice provides

        :param username: the username that should be inserted
        """
        self.username = username

    def insert_password(self, password):
        """
        This method inserts the password into the element, the server vDevice provides

        :param password: the username that should be inserted
        """
        self.password = password

    def execute_login(self):
        """
        This method executed the login process

        :return: true if the login was successfully otherwise false
        """
        self.basic_auth_manager.set_credentials(self.username, self.password)
        return True

    def execute_logout(self):
        """
        This method executed the logout process

        :return: true if the logout was successfully otherwise false
        """
        self.basic_auth_manager.reset_credentials()
        return True


class MyViewInternalPageFeature(ViewInternalPageFeature):
    """
    This feature declares that the owner device is able to interact with the internal area provided by the vDevice.
    """
    class Server(ViewInternalPageFeature.Server):
        api = UserApiFeature()

    basic_auth_manager = BasicAuthManager()

    def check_internal_page_viewable(self):
        """
        This method check if it is currently possible to access the internal page, that should be only available after a
        successful login.

        :return: returns true if the page is available, otherwise false
        """
        response = self.basic_auth_manager.request_webpage(self.Server.api.url_users)
        return response.status_code == 200
