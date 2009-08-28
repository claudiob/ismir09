#!/usr/bin/env ruby
require 'net/http'
require 'rexml/document'

######### LYRICSFLY ###########################################################

LY_HOST = "lyricsfly.com"
LY_PATH = "/api/api.php"
LY_USER = "b14851dad4030d0e3-temporary.API.access"
# If LY_USER does not work, get a new one at http://lyricsfly.com/api/

def retrieve_lyrics(artist, title)
  # From http://lyricsfly.com/api/
  # If the character is not [A-Z a-z 0-9] or space, just substitute "%" for it
  artist = artist.gsub(/[^a-zA-Z0-9]/, '%25')
  title  = title.gsub(/[^a-zA-Z0-9]/, '%25')
  query_params = {:i => LY_USER, :a => artist, :t => title}
  query = query_params.collect{ |k, v| [k, v].join('=') }.join('&')

  # URI is something like http://lyricsfly.com/api/api.php?i=b14851dad4030d0e3-temporary.API.access&a=Nick%20Cave%20And%20The%20Bad%20Seeds&t=Where%20The%20Wild%20Roses%20Grow
  uri = URI::HTTP.build(:host => LY_HOST,  :path => LY_PATH, :query => query)
  result = Net::HTTP.get_response(uri)

  # From http://lyricsfly.com/api/
  # All API calls return an XML document
  # <tx> - lyrics text separated by [br] for line break
  response = REXML::Document.new(result.body)  
  unless response.elements['//tx'].nil?
    return response.elements['//tx'].text.gsub("[br]", "")
  end
end

######### LAST.FM #############################################################

LF_HOST    = "ws.audioscrobbler.com"
LF_PATH    = "/2.0/"
LF_API_KEY = "b25b959554ed76058ac220b7b2e0a026"
LF_METHOD  = "tag.gettoptracks"

def retrieve_songs_by_tag(tag)
  # From http://www.last.fm/api/show?service=276
  # tag.getTopTracks Get the top tracks tagged by this tag ordered by tag count
  query_params = {:api_key => LF_API_KEY, :method => LF_METHOD, :tag => tag}
  query = query_params.collect{ |k, v| [k, v].join('=') }.join('&')

  # URI is something like: http://ws.audioscrobbler.com/2.0/?method=tag.gettoptracks&tag=metal&api_key=b25b959554ed76058ac220b7b2e0a026
  uri = URI::HTTP.build(:host => LF_HOST,  :path => LF_PATH, :query => query)
  result = Net::HTTP.get_response(uri)

  # Response is in XML, as shown in http://www.last.fm/api/show?service=276
  response = REXML::Document.new(result.body)  
  tracks = response.elements.collect('//track') do |track| {
    :artist => track.elements['artist'].elements['name'].text,
    :title => track.elements['name'].text}
  end
  return tracks
end

######### MASHUP ##############################################################

STDOUT.sync = true; # to have print "." without char buffering
genres = ["country", "grunge", "metal", "hip-hop"]
# genres = ARGV.empty? ? genres : ARGV

genres.each do |genre|
  count = 0.0 
  tracks = retrieve_songs_by_tag(genre)
  tracks.each do |track|
#    puts "Parsing lyrics of #{track[:title]} by #{track[:artist]} (#{genre})"
    print "."
    lyrics = retrieve_lyrics(track[:artist], track[:title])
    count += lyrics.count("?") unless lyrics.nil?
  end
  avg = count/tracks.length 
  puts "\nSongs tagged as #{genre} have in average #{avg} question marks\n"
end

