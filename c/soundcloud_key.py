import scapi

# The following API keys are provided only for the ISMIR tutorial
# Substitute with your Soundcloud application keys, as returned by
# http://soundcloud.com/settings/applications/new
soundcloud_key = "ogLCAErlfuLqA8X1GDx8Kg"
soundcloud_secret = "4tQO1UnDxvSS6aRIA5V6PJ3tdFeb94CuVECgPzPI"

# The host and keys to authenticate application with Soundcloud
API_HOST = "api.soundcloud.com"
scapi.REQUEST_TOKEN_URL = "http://%s/oauth/request_token" % API_HOST
scapi.ACCESS_TOKEN_URL  = "http://%s/oauth/access_token"  % API_HOST
scapi.AUTHORIZATION_URL = "http://%s/oauth/authorize"     % API_HOST
