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

######### EXAMPLE #############################################################


artist = !ARGV[0].nil? ? ARGV[0] : "Nick Cave And The Bad Seeds"
title  = !ARGV[1].nil? ? ARGV[1] : "Where The Wild Roses Grow"
puts retrieve_lyrics(artist, title)
