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
      sleep(5) if not ready
    end while not ready
    tag = body.elements["//#{feature}"]
    values[feature] = tag.text.to_i unless tag.nil?
  end
  values
end

def get_tracks(mood)
  url =  "http://api.jamendo.com/get2/stream/track/xml/?"
  url += "tag_idstr=#{mood}&n=5&order=random_desc"
  result = Net::HTTP.get_response(URI.parse(url))

  response = REXML::Document.new(result.body)
  response.elements.collect('//track') do |track|
    track.text
  end unless response.nil?
end

ARGV.each do |mood|
  tracks = get_tracks(mood)
  modes = tracks.collect{|track| get_analysis(track, ["mode"])["mode"]}.compact
  major = (modes - [0]).length/modes.length.to_f
  puts "#{mood} songs are %.2f major" % major + ", %.2f minor" % (1-major)
end

# Run as: ruby echonest_3.rb sad happy
