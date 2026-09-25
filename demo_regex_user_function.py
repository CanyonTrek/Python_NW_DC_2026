#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO define a useful and reusable
# user function to search for Regex Patterns
"""
    DocString
"""
import re

# Example of a USER function with optional parameters,
# and default values
def search_pattern(pattern: str = r"^(.)(.).\2\1$" ,file: str = r"f:\labs\words") -> None:
    fh_in = open(file, mode="rt")
    reobj = re.compile(pattern) # PRECOMPILE pattern ONLY ONCE!

    for line in fh_in:
        m = reobj.search(line) # Match precompiled pattern against str object
        if m:
            print(f"Matched {m.group()} on {line.rstrip()} at {m.start()}-{m.end()}")
    fh_in.close()
    return None


search_pattern(r"^.{19}$", r"f:\labs\words")

print(f"Annotations for search_pattern = {search_pattern.__annotations__}") # Fact finding