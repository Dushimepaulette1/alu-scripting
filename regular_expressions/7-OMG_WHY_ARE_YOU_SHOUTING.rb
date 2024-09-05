#!/usr/bin/env ruby

# Regular expression to match only capital letters
input = ARGV[0]
matches = input.scan(/[A-Z]/).join
puts matches
