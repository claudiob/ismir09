require 'net/http'
require 'rexml/document'
require "#{File.dirname(__FILE__)}/lyricsfly_key"

url = "http://lyricsfly.com/api/api.php?a=Rihanna&t=Umbrella&i=#{$api_key}"
result = Net::HTTP.get_response(URI.parse(url))

response = REXML::Document.new(result.body).elements['//tx']
puts response.text
