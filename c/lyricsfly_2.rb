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

puts get_lyrics(ARGV)

# Run as: ruby lyricsfly_2.rb "John Lennon" Imagine
