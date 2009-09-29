require 'net/http'
require 'rexml/document'

api_key = "PCEGSUESZOVYQWRRP"
url = "http://developer.echonest.com/api/upload"
result = Net::HTTP.post_form(URI.parse(url), {'api_key' => api_key, 
  'version' => '3', 'url' => 'http://ismir2009.benfields.net/m/120bpm.mp3'})

song_id = REXML::Document.new(result.body).elements['//track'].attributes['id']

url =  "http://developer.echonest.com/api/get_tempo"
url += "?api_key=#{api_key}&id=#{song_id}&version=3"
result = Net::HTTP.get_response(URI.parse(url))

tempo = REXML::Document.new(result.body).elements['//tempo'].text
puts tempo