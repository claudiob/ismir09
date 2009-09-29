require 'net/http'
require 'rexml/document'

def get_lyrics(artist_and_title)
  api_key = "91cbb76afd4f18217-temporary.API.access"
  artist,title = artist_and_title.collect{|arg| arg.gsub(/[^a-zA-Z0-9]/,'%25')}
  
  url = "http://lyricsfly.com/api/api.php?a=#{artist}&t=#{title}&i=#{api_key}"
  result = Net::HTTP.get_response(URI.parse(url))
  
  response = REXML::Document.new(result.body).elements['//tx']
  response.text.gsub("[br]", "") unless response.nil?
end

def get_artists_and_titles(genre)
  api_key = "7d7fa519b0e7b34a3905eb921bfad20d"
  
  url =  "http://ws.audioscrobbler.com/2.0/?method=tag.gettoptracks"
  url += "&tag=#{genre}&api_key=#{api_key}"
  result = Net::HTTP.get_response(URI.parse(url))

  response = REXML::Document.new(result.body)
  response.elements.collect('//track') do |track|
    [track.elements['artist'].elements['name'].text, track.elements['name'].text]
  end unless response.nil?
end

ARGV.each do |genre|
  tracks = get_artists_and_titles(genre)
  lyrics = tracks.collect{|track| get_lyrics(track)}.compact 
  qmarks = lyrics.inject(0.0) {|qmarks, lyric| qmarks + lyric.count("?")}
  puts "#{genre} has in average %.2f question marks" % (qmarks/lyrics.length)
end

# Run as: ruby lyricsfly_3.rb country hip-hop