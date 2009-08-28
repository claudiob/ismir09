#!/usr/bin/env python
from pyechonest import track, artist, config, util, config

config.ECHO_NEST_API_KEY = "PCEGSUESZOVYQWRRP"

def main():
  major = track.upload('http://www.iiia.csic.es/~claudio/ismir09/major7.mp3')
  print "Mode: %s | Tempo: %sBPM" % (major.mode["value"], major.tempo["value"])

  minor = track.upload('http://www.iiia.csic.es/~claudio/ismir09/minor.mp3')
  print "Mode: %s | Tempo: %sBPM" % (minor.mode["value"], minor.tempo["value"])

# This example needs be completed.
# More audio files are required for statistical significance.
# Moreover some hypotheses have to be tested, for instance whether "sad" songs
# can be statistically associated with a minor mode or a slow tempo.
# Also, specify better that mode 0 = minor and 1 = major

if __name__ == '__main__':
	main()

