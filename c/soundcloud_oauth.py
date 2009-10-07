import scapi

# The host and keys to authenticate application with Soundcloud 
from soundcloud_key import soundcloud_key, soundcloud_secret
# Note: the authentication returns the following tokens:
soundcloud_token = "nvFKBw83bTfDjIFPiRCxGw"
soundcloud_token_secret = "BNGdRSiimWgxrfPDmWkHza1roy77EwQ1mvT8JoeE"

API_HOST = "api.soundcloud.com"
scapi.REQUEST_TOKEN_URL = "http://%s/oauth/request_token" % API_HOST
scapi.ACCESS_TOKEN_URL  = "http://%s/oauth/access_token"  % API_HOST
scapi.AUTHORIZATION_URL = "http://%s/oauth/authorize"     % API_HOST

def init_scope():
    return scapi.Scope(scapi.ApiConnector(API_HOST, authenticator = \
        scapi.authentication.OAuthAuthenticator(soundcloud_key, \
        soundcloud_secret, soundcloud_token, soundcloud_token_secret)))
