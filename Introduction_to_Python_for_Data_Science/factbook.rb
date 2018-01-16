#!/usr/bin/env ruby
require 'factbook'

Factbook.codes.each do |code|
  pp code
end

page = Factbook::Page.new( 'br' )
File.open( 'br.json', 'w') do |f|
  f.write page.to_json
end
