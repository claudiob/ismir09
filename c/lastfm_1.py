#!/usr/bin/env python
import sys
from time import time
import pylast
from lastfm_key import lastfm_key

def recommend_artist(username):
    network = pylast.get_lastfm_network(api_key = lastfm_key)
    user = network.get_user(username)
    known_artists = get_known_artists(user, 1, int(time()))
    
    friends = user.get_friends()[:10]
    print "[%s has %d friends]" % (username, len(friends))

    now = int(time())
    sec_in_month = 604800*4
    prev_artists = get_friends_artists(friends, now-sec_in_month*2, now-sec_in_month)
    next_artists = get_friends_artists(friends, now-sec_in_month, now)
    
    prev_values = sum(prev_artists.values(), [])
    next_values = sum(next_artists.values(), [])
    both_artists = {}
    for artist in prev_values:
        both_artists[artist] = float(next_values.count(artist))/prev_values.count(artist) - 1
    
    hottest_artists = both_artists.keys()
    hottest_artists.sort(reverse = True, cmp = \
        lambda x,y: cmp(both_artists[x], both_artists[y]))
    print "[%d friends know %d artists]" % (len(friends), len(hottest_artists))
    
    recommended = [artist for artist in hottest_artists if artist not in known_artists][0]
    
    prev_listeners = [friend for friend, artists in prev_artists.items() if recommended in artists]
    next_listeners = list(set([friend for friend, artists in next_artists.items() if recommended in artists]) - set(prev_listeners))
    print "%s should listen to %s since" % (username, recommended)
    print "%s already listened to %s" % (prev_listeners, recommended)
    print "%s started listening to %s this month" % (next_listeners, recommended)


def get_known_artists(user, from_time='', to_time=''):
    charts = user.get_weekly_artist_charts(from_time, to_time)
    return [item.item for item in charts]


def get_friends_artists(friends, from_time, to_time):
    friends_artists  = {}
    for friend in friends:
        friends_artists[friend] = get_known_artists(friend, from_time, to_time)
    print "[Read list of friends' monthly artists]"  
    return friends_artists
    

if __name__ == "__main__":
    username = sys.argv[1]
    recommend_artist(username)


# To install pylast:
# $ wget http://pypi.python.org/packages/source/p/pylast/pylast-0.4.15.tar.gz
# $ tar xvf pylast-0.4.15.tar.gz
# $ cd pylast-0.4.15
# $ sudo python setup.py install
    