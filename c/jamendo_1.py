from urllib import urlopen
from isrock import isRock

query = "http://api.jamendo.com/get2/stream/track/plain/?n=50&tag_idstr=rock&order=random_desc"
result = urlopen(query).read()

songs = result.split()
rock = [isRock(song) for song in songs]

print "The ratio of rock songs is: %.2f" % (float(rock.count(True))/len(songs))

# Run as: python jamendo_1.py
