import balder
from balder.connections import HttpConnection
from tests.lib.features import HasLoginSystemFeature
from tests.setups import setup_features
from tests.setups.rest import rest_features


class SetupRestBasicAuth(balder.Setup):
    """
    This setup will be used to test the rest interface. For this the setup uses the BasicAuthentication method.
    """

    class Server(balder.Device):
        _ = HasLoginSystemFeature()
        api_route = rest_features.UserApiFeature()
        valid_user = setup_features.MyValidRegisteredUserFeature()

    @balder.connect(Server, HttpConnection)
    class Client(balder.Device):
        basicauth_manager = rest_features.BasicAuthManager()
        credentials = rest_features.MyInsertCredentialsFeature()
        internal = rest_features.MyViewInternalPageFeature()
