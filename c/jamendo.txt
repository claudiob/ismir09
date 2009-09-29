The first example is for people working on genre recognition systems. 

Say that you have developed an algorithm that is able to state whether a song is 'Rock' or not, based on any sort of content-based analysis.

What you would like to do is to evaluate the precision of this algorithm. The most common technique for this is to have a test-bed of songs of which you already know the genre, and to run your algorithm to test whether the genre is correctly identified by your algorithm or not.

To obtain valid statistical results, you need a very large data set of labelled songs. This is where Web mining can come to a help.

Several Web sites freely provide songs which have already been labelled and for which you can obtain an audio excerpt. Depending on the licensing of such songs, the excerpt can either be the complete audio or just a fraction, such as 30 seconds.

For this first example, we are going to employ the Web site Jamendo, which is an online collection of songs that are shared with non-restrictive conditions. This means that everyone can download any song for free and use them for research purpose. 

So what we will do is to compare the two ways of evaluating a genre recognition algorithm:
1) The "old" way, which requires you to collect by hand a set of audio files and label their genre
2) The "new" way, which uses Jamendo to automatically obtain a (large) set of audio files already genre-labelled

** The "old" way **

I have prepared a python script called genre_recognition_old.py that models the "old" way of evaluation, in which you collect a few files labelled as either 'Rock' or 'non Rock' and you run your genre recognition algorithm to see how it performs.

First of all, I have collected 4 files, two Rock songs and two non-Rock themes, and loaded them in shared folder. They can be accessed here:
http://www.iiia.csic.es/~claudio/ismir09/santana.mp3 (rock)
http://www.iiia.csic.es/~claudio/ismir09/pearljam.mp3 (rock)
http://www.iiia.csic.es/~claudio/ismir09/kennyg.mp3 (jazz)
http://www.iiia.csic.es/~claudio/ismir09/madonna.mp3 (pop)

The main() function adds these files into the array testSongs, specifying that the first two songs are Rock and the other two are not. Then runTest() is called.

The runTest() function call isRock() on each song to check whether that song is Rock or not. 
isRock() is the function that runs your genre recognition algorithm. It can use acoustic-based analysis, beat, tempo, this is not relevant.
It has to be seen as a sort of "black-box", that is given an audio file in input and returns True or False whether that song is Rock or not.
In the code, this is emulated by a very simple (and meaningless) algorithm, which reads the first KB of the audio file and returns that the song is Rock if any byte contains the value 'R'.

After running this process, the results are compared with the domain knowledge, counting how many times your genre recognition algorithm has correctly identified Rock songs. The precision is written to the output.

** The "new" way **

Using Jamendo as a source of music makes the process easier in that it does not require you to collect and label audio files. You can retrieve thousands of genre-labelled files directly from Jamendo and use them as a test-bed.

I have prepared a python script called genre_recognition_new.py that does exactly this: retrieves from Jamendo 20 songs labelled as 'Rock' and 20 songs labelled instead as 'Jazz'. Then it runs the genre recognition algorithm on this data set.

The main() function makes two similar calls to the Jamendo API using the urllib library. The first call opens the following URL:
http://jamendo.com/get2/stream/track/plain/?tag_idstr=rock&order=tag_weight_desc&n=20    
which returns a plain text list of the location of 20 audio files of songs labelled as Rock in the Jamendo database.
More information and documentation on this Jamendo API can be found at:
http://developer.jamendo.com/en/wiki/Musiclist2Api

The second call is similar, but retrieves 20 audio files of songs labelled as Jazz, rather than Rock.

The rest of the programme is equivalent to the "old" version: the genre recognition algorithm is run on each of these songs, counting how many times the genre "Rock" is correctly identified. The precision is written to the output.





