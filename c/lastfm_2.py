#!/usr/bin/env python
import sys
from time import time
import pylast
from lastfm_key import lastfm_key

def trends_for(username):
    api = pylast.get_lastfm_network(lastfm_key)
    user = api.get_user(username)    
    known_artists = get_known_artists(user)
    friends = user.get_friends()
    print "Looking for trends among %s's %d friends" % (username, len(friends))
    trends = get_trends(friends)
    
    for artist in trends.keys():
        if artist in known_artists or trends[artist][1] == []:
            del trends[artist]
    trendy_artists = trends.keys()
    trendy_artists.sort(key = lambda a: \
        len(trends[a][0]) / float(len(trends[a][1]) + len(trends[a][0])))
    print "Trendy artists for %s:" % username
    for artist in trendy_artists[:3]:
        print "%s, already known by %s, recently discovered by %s" % \
            (artist, trends[artist][0], trends[artist][1])        

def get_known_artists(user, when='always'):
    now = int(time())
    one_period = 60*60*24*30 # one month in seconds
    periods = {'always': (1, now), 
               'this_period': (now - one_period, now), 
               'last_period': (now - one_period*2, now - one_period)}
    charts = user.get_weekly_artist_charts(*periods[when])
    return [item.item for item in charts]

def get_trends(friends):
    trends = {} 
    for friend in friends:
        for artist in get_known_artists(friend, 'last_period'):
            last_friends = trends.get(artist, [[]])[0]
            trends[artist] = last_friends + [friend], []
        for artist in get_known_artists(friend, 'this_period'):
            if trends.has_key(artist) and friend not in trends[artist][0]:
                trends[artist][1].append(friend)
    return trends

if __name__ == "__main__":
    username = sys.argv[1]
    trends_for(username)