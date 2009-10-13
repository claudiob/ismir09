require 'net/http'
require 'rexml/document'
require "#{File.dirname(__FILE__)}/lyricsfly_key"
require "#{File.dirname(__FILE__)}/lastfm_key"

def get_lyrics(artist_and_title)
  artist,title = artist_and_title.collect{|arg| arg.gsub(/[^a-zA-Z0-9]/,'%25')}
  
  url = "http://lyricsfly.com/api/api.php?a=#{artist}&t=#{title}&i=#{$lyricsfly_key}"
  result = Net::HTTP.get_response(URI.parse(url))
  body = result.body.gsub(/[^\x20-\x7e]/,'')
  
  response = REXML::Document.new(body).elements['//tx']
  response.text.gsub("[br]", "") unless response.nil?
end

def get_artists_and_titles(genre)
  url =  "http://ws.audioscrobbler.com/2.0/?method=tag.gettoptracks"
  url += "&tag=#{genre}&api_key=#{$lastfm_key}"
  result = Net::HTTP.get_response(URI.parse(url))

  response = REXML::Document.new(result.body)
  response.elements.collect('//track') do |track| [
    track.elements['artist'].elements['name'].text, 
    track.elements['name'].text
  ] end unless response.nil?
end

ARGV.each do |genre|
  tracks = get_artists_and_titles(genre)
  lyrics = tracks.collect{|track| get_lyrics(track)}.compact 
  qmarks = lyrics.inject(0.0) {|qmarks, lyric| qmarks + lyric.count("?")}
  puts "#{genre} has in average %.2f question marks" % (qmarks/lyrics.length)
end

# Run as: ruby lyricsfly_3.rb country hip-hop