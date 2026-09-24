#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO SPLIT and REJOIN strings using
# the str.split() and str.join() methods.
""" 
    DocString
"""
# Sample line from /etc/passwd on Linux for the root user account
line = 'root:x:0:0:The Super User:/root:/bin/bash'

# I want to modify the str object! BUT str are IMMUTABLE!
fields = line.split(":") # Returns a LIST - which are MUTABLE!
fields[4] = "The Administrator"
fields[6] = "/bin/zsh"

line = ":".join(fields) # Returns a NEW str object
print("Modified line =", line)
