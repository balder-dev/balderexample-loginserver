import balder
import mechanize


# SERVER FEATURES

class HasLoginSystemFeature(balder.Feature):
    """
    This is an autonomous feature that shows that the device has a login system.
    """
    pass


class ValidRegisteredUserFeature(balder.Feature):
    """
    This feature provides data, that is known from the device that manages user credentials.
    """
    def get_valid_user(self):
        """
        This method returns a valid (user, password) pair - valid means that the user is known and could work with
        the server.

        :return: a tuple with a valid user and a valid password
        """
        raise NotImplementedError("this method has to be implemented on setup level")


# CLIENT FEATURES

class InsertCredentialsFeature(balder.Feature):
    """
    This feature allows inserting credentials into a login system
    """
    class Server(balder.VDevice):
        """a vDevice that should describe the server (needed later on)"""
        _ = HasLoginSystemFeature()

    def insert_username(self, username):
        """
        This method inserts the username into the login-element, that the server vDevice provides

        :param username: the username that should be inserted
        """
        raise NotImplementedError("this method has to be implemented on setup level")

    def insert_password(self, password):
        """
        This method inserts the password into the login-element, that the server vDevice provides

        :param password: the password that should be inserted
        """
        raise NotImplementedError("this method has to be implemented on setup level")

    def execute_login(self):
        """
        This method executes the login process

        :return: true if the login was successfully otherwise false
        """
        raise NotImplementedError("this method has to be implemented on setup level")

    def execute_logout(self):
        """
        This method executes the logout process

        :return: true if the logout was successfully otherwise false
        """
        raise NotImplementedError("this method has to be implemented on setup level")


class ViewInternalPageFeature(balder.Feature):
    """
    This feature declares that the owner device is able to interact with the internal area provided by the vDevice.
    """
    class Server(balder.VDevice):
        """a vDevice that should describe the server (needed later on)"""
        _ = HasLoginSystemFeature()

    def check_internal_page_viewable(self):
        """
        This method check if it is currently possible to access the internal page, that should be only available after a
        successful login.

        :return: returns true if the page is available, otherwise false
        """
        raise NotImplementedError("this method has to be implemented on setup level")


class BrowserSessionManagerFeature(balder.Feature):
    """
    This feature provides an interface to interact with a browser session of the `mechanize` python package.
    """
    browser = None

    def create_browser_if_necessary(self):
        """
        This method creates a new browser session for this object
        """
        if self.browser is None:
            self.browser = mechanize.Browser()

    def open_page(self, open_page_url=None):
        """
        This method opens a webpage if the given webpage is currently not open

        :param open_page_url: the url that should be opened
        """
        return self.browser.open(open_page_url)
