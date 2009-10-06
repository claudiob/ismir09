#!/usr/bin/env python
import sys
from time import time
import pylast
from lastfm_key import lastfm_key

def recommend_artist(username):
    # 1. Look for already known artists
    network = pylast.get_lastfm_network(api_key = lastfm_key)
    user = network.get_user(username)
    known_artists = get_known_artists(user)
    
    # 2. Retrieve list of friends
    friends = user.get_friends()[:15]
    print "[Analysing %d friends of %s]" % (username, len(friends))

    # 3. Look for artists listened by friends one month ago or this month
    now = int(time())
    sec_in_month = 60*60*24*30
    
    old_data = {} 
    new_data = {}
    for friend in friends:
        old_data[friend] = get_known_artists(friend, now-sec_in_month*2, now-sec_in_month)
        new_data[friend] = get_known_artists(friend, now-sec_in_month, now)

    # 4. Identify artists unknown to user and check if they have become popular
    old_artists = sum(old_data.values(), [])
    new_artists = sum(new_data.values(), [])
    unknown_artists = list(set(old_artists) & set(new_artists) - set(known_artists))
    unknown_data = {}
    for artist in unknown_artists:
        unknown_data[artist] = float(new_artists.count(artist))/old_artists.count(artist)
    
    # 5. Sort unknown artists based on how more popular they have become 
    unknown_artists.sort(reverse = True, cmp = lambda x,y: cmp(unknown_data[x], unknown_data[y]))

    # 6. Recommend the first most trendy artists unknown to the user
    print "%s should listen to:" % username
    for recommend in unknown_artists[:3]:
        old_listeners = [friend for friend, artists in old_data.items() if recommend in artists]
        new_listeners = list(set([friend for friend, artists in new_data.items() if recommend in artists]) - set(old_listeners))
        print "%s, already known by %s and recently discovered by %s." % (recommend, old_listeners, new_listeners)


def get_known_artists(user, from_time=1, to_time=int(time())):
    charts = user.get_weekly_artist_charts(from_time, to_time)
    return [item.item for item in charts]


if __name__ == "__main__":
    username = sys.argv[1]
    recommend_artist(username)

    