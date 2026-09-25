#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO match and substitute patterns using
# the re.sub() re.subn() functions
""" 
    DocString
"""
import re

# Sample line from /etc/passwd on Linux for the root user account
line = "root:x:0:0:The Super User:/root:/bin/ksh"  # Str are immutable!

line = re.sub(r"[Ss]uper [Uu]ser", r"Administrator", line) # Returns modified str
(line, num) = re.subn(r"ksh$", r"bash", line) # Returns TUPLE (modified str, changes)

print(f"Modified line = {line} with {num} changes")