import webbrowser
import scapi

# The host and keys to authenticate application with Soundcloud 
from soundcloud_key import soundcloud_key, soundcloud_secret
API_HOST = "api.soundcloud.com"
scapi.REQUEST_TOKEN_URL = "http://%s/oauth/request_token" % API_HOST
scapi.ACCESS_TOKEN_URL  = "http://%s/oauth/access_token"  % API_HOST
scapi.AUTHORIZATION_URL = "http://%s/oauth/authorize"     % API_HOST

def init_scope():
    # The first authenticator to get a request-token
    authenticator = scapi.authentication.OAuthAuthenticator(soundcloud_key, \
        soundcloud_secret, None, None)

    # The first connector to create and sign the requests
    connector = scapi.ApiConnector(host=API_HOST, authenticator=authenticator)
    token, secret = connector.fetch_request_token()

    # Grant authorization for the request-token via browser confirmation
    authorization_url = connector.get_request_token_authorization_url(token)
    webbrowser.open(authorization_url)
    oauth_verifier = raw_input("Enter verifier code as seen in the browser: ")

    # The second authenticator with the temp token/secret to get access-token
    authenticator = scapi.authentication.OAuthAuthenticator(soundcloud_key, \
        soundcloud_secret, token, secret)

    # The second connector with the new authenticator
    connector = scapi.ApiConnector(API_HOST, authenticator=authenticator)
    token, secret = connector.fetch_access_token(oauth_verifier)

    # The final authenticator with all four parameters OAuth requires
    authenticator = scapi.authentication.OAuthAuthenticator(soundcloud_key, \
        soundcloud_secret, token, secret)

    # The final connector returned in the root to query for resources
    connector = scapi.ApiConnector(API_HOST, authenticator=authenticator)
    root = scapi.Scope(connector)

    print "Authenticated as %s" % root.me().username
    return root