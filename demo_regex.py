#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO match text using str testing
# and Regex Pattern matching and the re module
""" 
    DocString
"""
import re

# Open file handle for READING in TEXT mode
fh_in = open(r"f:\labs\words", mode="rt")

# Iterate through the file handle using an iterator for loop
for line in fh_in:
    # Example of str testing
    # if (line.startswith("Y") and line.rstrip("\n").endswith("n") and "town" in line):
    # m = re.search(r"^the", line) # Match lines starting with 'the'
    # m = re.search(r"ing$", line)  # Match lines ending with 'ing'
    # m = re.search(r"^ring$", line)  # Match lines only containing with 'ring'
    # m = re.search(r"^.ing$", line)  # Match lines of 4 char ending with 'ing'
    # m = re.search(r"^...................$", line)  # Match lines of exactly 19 chars
    # m = re.search(r"^.{19}$", line)  # Match lines of exactly 19 chars
    # m = re.search(r"^[adrp]ing$", line)  # Match lines of 4 char ending with 'ing'
    # m = re.search(r"^[A-Z]", line)  # Match lines starting with a CAPITAL
    # m = re.search(r"[0-9][0-9][0-9]", line)  # Match lines with 3 consecutive digits
    # m = re.search(r"[aeiou][aeiou][aeiou]", line)  # Match lines with 3 consecutive vowels
    # m = re.search(r"[aeiou]{5,}", line)  # Match lines at least 5 consecutive vowels
    # m = re.search(r"\.", line)  # Match lines with a DOT
    # m = re.search(r"[.]", line)  # Match lines with a DOT
    # m = re.search(r"^[A-Z].*[A-Z]$", line)  # Match lines start/end with a CAPITAL
    # m = re.search(r"^[A-Z].{4}[A-Z]$", line)  # Match lines of 6 chars start/end with a CAPITAL
    # m = re.search(r"rhubarb|gooseberry|pineapple", line)  # Match lines with ONE of these patterns
    m = re.search(r"^(.)(.).\2\1$", line)  # Match lines of 5 char palindromes
    # m = re.search(r"^([A-Z]).*\1$", line)  # Match lines start/end SAME CAPITAL
    # m = re.match(r"([A-Z]).*\1$", line)  # match() auto matches LINES starting with
    # m = re.fullmatch(r"^([A-Z]).*\1\n$", line)  # Match ENTIRE text incl hidden chars
    if m:
        print(f"Matched {m.group()} on {line.rstrip()} at {m.start()}-{m.end()}, "
              f"Groupings = {m.groups()}, Group 1 = {m.group(1)}")

fh_in.close()