import pylast
from lastfm_key import lastfm_key

api = pylast.get_lastfm_network(lastfm_key)
friends = api.get_user("claudiob").get_friends()
print "Last.fm friends: %s" % friends