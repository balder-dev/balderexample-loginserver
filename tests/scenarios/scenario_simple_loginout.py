import balder
import balder.connections as conn
from ..lib.features import HasLoginSystemFeature, ValidRegisteredUserFeature, InsertCredentialsFeature, ViewInternalPageFeature


class ScenarioSimpleLoginOut(balder.Scenario):
    """
    This scenario is a simple "login - check if it has access to the internal area - logout" scenario. It consists of
    two devices, a server device which provides the login area and a client device that should be able to execute a
    log-in into the area, the server provides.
    """

    class ServerDevice(balder.Device):
        _autonomous = HasLoginSystemFeature()
        user_credential = ValidRegisteredUserFeature()

    @balder.connect(ServerDevice, conn.HttpConnection)
    class ClientDevice(balder.Device):
        login_out = InsertCredentialsFeature(Server="ServerDevice")
        internal_page = ViewInternalPageFeature(Server="ServerDevice")

    def test_valid_login_logout(self):
        """
        This testcase will execute the following procedure:

        * check that we have no access to the internal page
        * insert a valid username
        * insert a valid password
        * press submit
        * check that we have access to the internal page
        * logout
        * check that we have no access to the internal page
        """
        # secure that we are not logged in
        assert not self.ClientDevice.internal_page.check_internal_page_viewable(), \
            "can access internal data before user is logged in"

        # get example user with a valid username and password
        username, password = self.ServerDevice.user_credential.get_valid_user()

        # insert the user data and execute the login command
        self.ClientDevice.login_out.insert_username(username)
        self.ClientDevice.login_out.insert_password(password)
        assert self.ClientDevice.login_out.execute_login(),\
            "login does not work"

        # check that the internal page is viewable
        assert self.ClientDevice.internal_page.check_internal_page_viewable(), \
            "can not access internal data after login"

        # now log out user
        assert self.ClientDevice.login_out.execute_logout(), \
            "logout does not work"

        # check that we can not access the internal page after user is logged out
        assert not self.ClientDevice.internal_page.check_internal_page_viewable(), \
            "can access internal data after user was logged out"
