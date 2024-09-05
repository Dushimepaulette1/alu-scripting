#!/usr/bin/env ruby

# The regular expression to extract sender, receiver, and flags
log_entry = ARGV[0]

# Match the necessary parts using capture groups
if log_entry.match(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/)
  sender = $1
  receiver = $2
  flags = $3
  puts "#{sender},#{receiver},#{flags}"
end
