#!/usr/bin/env ruby

# Checking if one argument is passed
if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME} <string>"
  exit 1
end

# Getting the input string
input = ARGV[0]

# Useing a regular expression to find all the matches  of 'School'
matches = input.scan(/hbt*n/)

# Printing the matches combined
puts matches.join
