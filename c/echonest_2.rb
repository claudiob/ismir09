require 'net/http'
require 'rexml/document'
require "#{File.dirname(__FILE__)}/echonest_key"

def get_analysis(song, features = ["tempo", "mode", "key", "time_signature"])
  values = Hash.new

  url = "http://developer.echonest.com/api/upload"
  begin
    result = Net::HTTP.post_form(URI.parse(url), 
      {'api_key' => $echonest_key, 'version' => '3', 'url' => song})
  rescue Timeout::Error
    return values
  end
  song_id = REXML::Document.new(result.body).elements['//track'].attributes['id']

  features.each do |feature|
    url =  "http://developer.echonest.com/api/get_#{feature}"
    url += "?api_key=#{$echonest_key}&id=#{song_id}&version=3"
    begin
      result = Net::HTTP.get_response(URI.parse(url))
      body = REXML::Document.new(result.body)
      ready = body.elements["//code"].text.to_i != 11
      sleep(5) if not ready
    end while not ready
    tag = body.elements["//#{feature}"]
    values[feature] = tag.text.to_i unless tag.nil?
  end
  values
end

p get_analysis(ARGV[0])

# Run as: ruby echonest_2.rb http://ismir2009.benfields.net/m/120bpm.mp3
