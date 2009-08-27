#!/usr/bin/env python
from urllib import urlopen

def isRock(remotePath):
    print "Testing song: %s" % remotePath.rsplit("/",1)[-1]
    song = urlopen(remotePath)
    # The rest of this function is a blackbox
    # Substitute with your genre recognition code
    return song.read(1024).find('R') > 0

def runTest(testSongs):
    results = [isRock(song[0]) == song[1] for song in testSongs]

    positive = results.count(True) 
    negative = results.count(False)
    precision = 1.0*positive/(positive + negative)

    print "Precision rate: %.0f%% " % (precision*100)
    return precision

# Example 2: using Jamendo, retrieving 20 rock and 20 jazz songs.
def main():
    testSongs = []
    basicUrl  = "http://jamendo.com/get2/stream/track/plain/?tag_idstr=%s"
    basicUrl += "&order=tag_weight_desc&n=20"    

    rockSongs = urlopen(basicUrl % "rock").read().split()
    jazzSongs = urlopen(basicUrl % "jazz").read().split()
    testSongs.extend([[song, True]  for song in rockSongs])
    testSongs.extend([[song, False] for song in jazzSongs])

    return runTest(testSongs)
            
if __name__ == "__main__":
    main()
    
