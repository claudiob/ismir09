The second example is for people working with lyrics. 

Say that you would like to improve your MIR algorithm taking into account the lyrics of the songs that you analyse.
In this case, you need to obtain lyrics, and Web mining can come to a help.

Previous work have dealt with lyrics retrieval from the web, but the majority used Google as a source of knowledge (Geleijnse 2006, Knees 2005, Kleedorfer 2008). This has two main problems. Firstly, Google does not have the concept of lyrics, so you need to use keywords and hope that what is returned is actually lyrics. Secondly, what is returned are web pages containing lyrics, that you have to clean up removing everything additional on the page.

A better solution is to employ a lyrics-based Web site that offers an API to programmatically retrieve lyrics. For this example, we are going to employ the Web site LyricsFly. 

LyricsFly has an API that accepts in input a user ID, artist name and song title and returns the lyrics of that song in an XML format.
For instance, to obtain the lyrics for the song "Where the wild roses grow" by Nick Cave And The Bad Seeds, you need to access the following URL:

http://lyricsfly.com/api/api.php?i=b14851dad4030d0e3-temporary.API.access&a=Nick Cave And The Bad Seeds&t=Where The Wild Roses Grow

The query has indeed three parameters: user ID, artist name, song title.
One thing about the user ID: you have to request one to LyricsFly, the one in this example is a temporary one, that you have to substitute with a new one, just read the API documentation page on LyricsFly site.

*A simple example*

I have prepared a ruby script called lyrics_retrieval.rb that retrieves the lyrics for one song from LyricsFly. If called with no parameters, the command:

$ ruby lyrics_retrieval.rb

retrieves the lyrics for "Where The Wild Roses Grow" by Nick Cave and The Bad Seeds. To change song, just specify artist and title as the parameters in the command line, for instance the command:

$ ruby lyrics_retrieval.rb "Frank Sinatra" "Strangers in the night"

retrieves the lyrics for "Strangers in the night" by Frank Sinatra.

The programme works as follows:
* First parameters are converted into a format valid to be written in a URL
* Then an HTTP request is made to obtain the lyrics from LyricsFly
* Then the XML file returned is parsed to read only the lyrics
* Finally, if lyrics are found, they are printed to the output

*A mash-up example*

Now that we know how to automatically retrieve lyrics, let's see how this can be useful.

We can use this to check on the paper Mayer 2008 "Rhyme and Style Features for Musical Genre Classification by Song Lyrics" which stated that Hip-Hop and Metal songs have a lot more question marks in the lyrics than Country and Grunge songs.

First we need a list of songs labelled with these four genres.
We saw in the first experiment how this can be done using Jamendo.
Here we employ the same approach, but with a different Web site: Last.fm.
This is because Last.fm contains more famous songs than Jamendo, and probably LyricsFly will hold the lyrics for these songs.

I have prepared a ruby script called lyrics_retrieval_mashup.rb that includes the previous code to retrieve lyrics from LyricsFly, together with new code to retrieve genre-labelled songs from Last.fm.

The function retrieve_songs_by_tag() gets a Last.fm tag in input (which can be a genre) and returns the list of top tracks belonging to that tag.

The rest of the programme takes a series of genres (Metal, Hip-Hop, Country, Grunge by default) and for each of them retrieves a set of tracks from Last.fm. Then the lyrics of each track are retrieved from LyricsFly and the number of question marks is counted. 
Finally, the average number of "?" for each genre is printed.

The result confirms the research done by Mayer et al.:
# Songs tagged as country have in average 0.26 question marks
# Songs tagged as grunge have in average 0.26 question marks
# Songs tagged as metal have in average 0.66 question marks
# Songs tagged as hip-hop have in average 1.42 question marks


