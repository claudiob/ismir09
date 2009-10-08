import scapi
from soundcloud_key import soundcloud_key, soundcloud_secret, API_HOST

def init_scope():
    soundcloud_token = "nvFKBw83bTfDjIFPiRCxGw" # Already retrieved
    soundcloud_token_secret = "BNGdRSiimWgxrfPDmWkHza1roy77EwQ1mvT8JoeE"
    return scapi.Scope(scapi.ApiConnector(API_HOST, authenticator = \
        scapi.authentication.OAuthAuthenticator(soundcloud_key, \
        soundcloud_secret, soundcloud_token, soundcloud_token_secret)))

root = init_scope()
user = root.users("bfields")
print "%s is following:" % user.username
for friend in user.followings():
    print "- %s [%s]" % (friend["username"], friend["permalink_url"])
