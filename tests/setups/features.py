"""
This general module provides all setup feature classes.
"""
import balder
from ..lib.features import InsertCredentialsFeature, ViewInternalPageFeature, BrowserSessionManagerFeature, \
    ValidRegisteredUserFeature


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


class LoginWebpageFeature(balder.Feature):
    """
    This feature provides all specific data for the login page of the login front-end webpage.
    """
    @property
    def url(self):
        """
        :return: returns the url to the login page
        """
        return "http://localhost:8000/accounts/login"

    @property
    def dom_name_login_form(self):
        """
        :return: returns the HTML DOM name of the login form
        """
        return "login"

    @property
    def dom_name_username_field(self):
        """
        :return: returns the HTML DOM name of the username field
        """
        return "username"

    @property
    def dom_name_password_field(self):
        """
        :return: returns the HTML DOM name of the password field
        """
        return "password"


class InternalWebpageFeature(balder.Feature):
    """
    This feature provides all specific data of the internal front-end webpage.
    """
    @property
    def url(self):
        """
        :return: returns the url to the internal webpage
        """
        return "http://localhost:8000"

    @property
    def title(self):
        """
        :return: returns the title of the page to verify if we have access to the internal page
        """
        return "Internal"

    @property
    def url_logout(self):
        """
        :return: returns the url to execute the logout process
        """
        return "http://localhost:8000/accounts/logout"


# Client Features

class MyInsertCredentialsFeature(InsertCredentialsFeature):
    """
    This feature allows inserting credentials into a login system
    """
    class Server(InsertCredentialsFeature.Server):
        """the vDevice we need to communicate with -> the vDevice needs the login and internal webpage DOM references"""
        login_webpage = LoginWebpageFeature()
        internal_webpage = InternalWebpageFeature()

    browser_manager = BrowserSessionManagerFeature()
    setup_done = False

    def do_setup_if_necessary(self):
        """
        This method opens the browser and opens the page - will be executed only on the first time
        """
        if not self.setup_done:
            self.browser_manager.create_browser_if_necessary()
            self.browser_manager.open_page(self.Server.login_webpage.url)
            self.setup_done = True

    def insert_username(self, username):
        """
        This method inserts the username into the DOM-element, the server vDevice provides

        :param username: the username that should be inserted
        """
        self.do_setup_if_necessary()
        # now insert the username
        self.browser_manager.browser.select_form(name=self.Server.login_webpage.dom_name_login_form)
        self.browser_manager.browser[self.Server.login_webpage.dom_name_username_field] = username

    def insert_password(self, password):
        """
        This method inserts the password into the DOM-element, the server vDevice provides

        :param password: the username that should be inserted
        """
        self.do_setup_if_necessary()
        # now insert the password
        self.browser_manager.browser.select_form(name=self.Server.login_webpage.dom_name_login_form)
        self.browser_manager.browser[self.Server.login_webpage.dom_name_password_field] = password

    def execute_login(self):
        """
        This method executed the login process

        :return: true if the login was successfully otherwise false
        """
        response = self.browser_manager.browser.submit()
        return response.wrapped.code == 200

    def execute_logout(self):
        """
        This method executed the logout process

        :return: true if the logout was successfully otherwise false
        """
        response = self.browser_manager.open_page(self.Server.internal_webpage.url_logout)
        return response.wrapped.code == 200


class MyViewInternalPageFeature(ViewInternalPageFeature):
    """
    This feature declares that the owner device is able to interact with the internal area provided by the vDevice.
    """
    class Server(ViewInternalPageFeature.Server):
        """our vDevice we want to communicate with -> vDevice needs the internal page references"""
        internal_webpage = InternalWebpageFeature()

    browser_manager = BrowserSessionManagerFeature()

    def check_internal_page_viewable(self):
        """
        This method check if it is currently possible to access the internal page, that should be only available after a
        successful login.

        :return: returns true if the page is available, otherwise false
        """
        self.browser_manager.create_browser_if_necessary()
        self.browser_manager.open_page(self.Server.internal_webpage.url)
        if self.browser_manager.browser.title() != self.Server.internal_webpage.title:
            # redirect to another webpage -> not able to read the internal webpage
            return False
        return True
