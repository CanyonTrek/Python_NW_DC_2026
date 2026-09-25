#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO define a VARIADIC function
# which is a function that allows variable number of paremeters
"""
    DocString
"""
import re

# Example of a VARIADIC function that allows a variable
# number of parameters into a TUPLE
def search_pattern(pattern: str = r"^(.)(.).\2\1$", *files) -> int:
    lines = 0
    for file in files:
        fh_in = open(file, mode="rt")
        reobj = re.compile(pattern) # PRECOMPILE pattern ONLY ONCE!

        for line in fh_in:
            m = reobj.search(line) # Match precompiled pattern against str object
            if m:
                lines += 1
                print(f"Matched {m.group()} on {line.rstrip()} at {m.start()}-{m.end()}")
        fh_in.close()
    return lines


num_lines = search_pattern(r"^.{19}$", r"f:\labs\words", r"f:\labs\words2", r"f:\labs\words3")
print(f"Lines matched = {num_lines}")


