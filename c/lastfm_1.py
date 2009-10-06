#!/usr/bin/env python
import sys
from time import time
import pylast
from lastfm_key import lastfm_key

def recommend_artist(username):
    network = pylast.get_lastfm_network(api_key = lastfm_key)
    user = network.get_user(username)
    known = get_known_artists(user, 1, int(time()))
    
    friends = user.get_friends()[:50]
    print "[%s has %d friends]" % (username, len(friends))
    hottest = get_hottest_artists(friends)
    
    recommended = [artist for artist in hottest if artist not in known][:3]
    print "%s should listen to %s" % (username, recommended)


def get_known_artists(user, from_time='', to_time=''):
    charts = user.get_weekly_artist_charts(from_time, to_time)
    return [item.item for item in charts]


def get_hottest_artists(friends):
    now = int(time())
    sec_in_week = 604800
    prev_artists = get_friends_artists(friends, now-sec_in_week*2, now-sec_in_week)
    next_artists = get_friends_artists(friends, now-sec_in_week, now)
    
    both_artists = {}
    for artist, count in prev_artists.items():
        if next_artists.has_key(artist):
            both_artists[artist] = float(next_artists[artist])/count-1
    
    sorted_artists = both_artists.keys()
    sorted_artists.sort(reverse = True, cmp = \
        lambda x,y: cmp(both_artists[x], both_artists[y]))
    print "[%d friends know %d artists]" % (len(friends), len(sorted_artists))
    return sorted_artists


def get_friends_artists(friends, from_time, to_time):
    known_artists = [get_known_artists(friend, from_time, to_time) for friend in friends]
    known_artists = sum(known_artists, []) # flatten
    friends_artists  = {}
    for i in set(known_artists):
        friends_artists[i] = known_artists.count(i)
    print "[Read list of friends' weekly artists]"  
    return friends_artists
    

if __name__ == "__main__":
    username = sys.argv[1]
    recommend_artist(username)


# To install pylast:
# $ wget http://pypi.python.org/packages/source/p/pylast/pylast-0.4.15.tar.gz
# $ tar xvf pylast-0.4.15.tar.gz
# $ cd pylast-0.4.15
# $ sudo python setup.py install
    