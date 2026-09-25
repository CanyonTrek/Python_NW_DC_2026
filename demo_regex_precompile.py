#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO match text using str testing
# and Regex Pattern matching and the re module
"""
    DocString
"""
import re

fh_in = open(r"f:\labs\words", mode="rt")

reobj = re.compile(r"^(.)(.).\2\1$") # PRECOMPILE pattern ONLY ONCE!

for line in fh_in:
    # m = re.search(r"^(.)(.).\2\1$", line)  # Match lines of 5 char palindromes
    m = reobj.search(line) # Match precompiled pattern against str object
    if m:
        print(f"Matched {m.group()} on {line.rstrip()} at {m.start()}-{m.end()}")

fh_in.close()