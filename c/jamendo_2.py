#!/usr/bin/env python
import sys
from urllib import urlopen
from isrock import isRock

def evaluate(n, genre):
    query = "http://api.jamendo.com/get2/stream/track/plain/?"
    query += "tag_idstr=%s&n=%d&order=random_desc" % (genre, n)
    result = urlopen(query).read()
    songs = result.split()
    rock = [isRock(song) for song in songs]
    ratio = float(rock.count(True))/len(songs)
    print "%s) The ratio of rock songs is: %.2f" % (genre, ratio)

if __name__ == "__main__":
    n = int(sys.argv[1])
    genres = sys.argv[2:]
    [evaluate(n, genre) for genre in genres]

# Run as: python jamendo_2.py 30 rock jazz country blues
