import balder
from balder.connections import HttpConnection
from tests.lib.features import HasLoginSystemFeature
from tests.setups import features as setup_features


class SetupWebBrowser(balder.Setup):
    """
    This setup will be used to test the web login page of the balderexample-loginserver project.
    """

    class Server(balder.Device):
        _ = HasLoginSystemFeature()
        login_webpage = setup_features.LoginWebpageFeature()
        internal_webpage = setup_features.InternalWebpageFeature()
        valid_user = setup_features.MyValidRegisteredUserFeature()

    @balder.connect(Server, HttpConnection)
    class Client(balder.Device):
        browser_manager = setup_features.BrowserSessionManagerFeature()
        credentials = setup_features.MyInsertCredentialsFeature()
        internal = setup_features.MyViewInternalPageFeature()
