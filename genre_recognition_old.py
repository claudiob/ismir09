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

# Example 1: before introducing Jamendo, using four manually labelled files.
def main():
    testSongs = []
    remoteFolder = "http://www.iiia.csic.es/~claudio/ismir09/"
    
    testSongs.append([remoteFolder + "santana.mp3",  True]) # is Rock
    testSongs.append([remoteFolder + "pearljam.mp3", True]) # is Rock
    testSongs.append([remoteFolder + "kennyg.mp3",  False]) # is not Rock
    testSongs.append([remoteFolder + "madonna.mp3", False]) # is not Rock

    return runTest(testSongs)

if __name__ == "__main__":
    main()
    