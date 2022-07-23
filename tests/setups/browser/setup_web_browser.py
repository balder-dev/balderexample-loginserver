import balder
from balder.connections import HttpConnection
from tests.lib.features import HasLoginSystemFeature
from tests.setups import setup_features
from tests.setups.browser import browser_features


class SetupWebBrowser(balder.Setup):
    """
    This setup will be used to test the web login page of the balderexample-loginserver project.
    """

    class Server(balder.Device):
        _ = HasLoginSystemFeature()
        login_webpage = browser_features.LoginWebpageFeature()
        internal_webpage = browser_features.InternalWebpageFeature()
        valid_user = setup_features.MyValidRegisteredUserFeature()

    @balder.connect(Server, HttpConnection)
    class Client(balder.Device):
        browser_manager = browser_features.BrowserSessionManagerFeature()
        credentials = browser_features.MyInsertCredentialsFeature()
        internal = browser_features.MyViewInternalPageFeature()
