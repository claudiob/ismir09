require 'net/http'
require 'rexml/document'

def get_analysis(track, features = ["tempo", "mode", "key", "time_signature"])
  api_key = "PCEGSUESZOVYQWRRP"
  values = Hash.new

  url = "http://developer.echonest.com/api/upload"
  begin
    result = Net::HTTP.post_form(URI.parse(url), {'api_key' => api_key, 
      'version' => '3', 'url' => track})
  rescue Timeout::Error
    return values
  end
  track_id = REXML::Document.new(result.body).elements['//track'].attributes['id']

  features.each do |feature|
    url =  "http://developer.echonest.com/api/get_#{feature}"
    url += "?api_key=#{api_key}&id=#{track_id}&version=3"
    begin
      result = Net::HTTP.get_response(URI.parse(url))
      body = REXML::Document.new(result.body)
      ready = body.elements["//code"].text.to_i != 11
      sleep(10) if not ready
    end while not ready
    tag = body.elements["//#{feature}"]
    values[feature] = tag.text.to_i unless tag.nil?
  end
  values
end

p get_analysis(ARGV[0])

# Run as: ruby echonest_2.rb http://ismir2009.benfields.net/m/120bpm.mp3
