#!/usr/bin/env python
import sys
from urllib import urlopen
from time import sleep

def isRock(song):
    # Substitute with your code (blur)
    try:
        excerpt = urlopen(song).read(512)
    except IOError:
        sleep(2)
        excerpt = urlopen(song).read(512)
    isRock = excerpt.find('7') > 0
    return isRock

if __name__ == "__main__":
    print isRock(sys.argv[1])
    