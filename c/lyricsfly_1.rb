require 'net/http'
require 'rexml/document'

api_key = "91cbb76afd4f18217-temporary.API.access"
url = "http://lyricsfly.com/api/api.php?a=Rihanna&t=Umbrella&i=#{api_key}"
result = Net::HTTP.get_response(URI.parse(url))

response = REXML::Document.new(result.body).elements['//tx']
puts response.text
