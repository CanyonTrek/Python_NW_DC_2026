#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO a SAFER way of opening
# and CLOSING a file handle using a context resource manager (with statement)
"""
    DocString
"""
import sys
# Created a multi-dimensional dict of lists..
movies = { 'junyl': ['the godfather', 'la la land', 'whiplash'],
           'michael': ['the terminal', 'shrek 3', 'inception'],
           'damian': ['pirates caribbean', 'avengars', 'up'],
           'ninaad': ['interstellar', 'dark knight', 'cars 2']
}

# Open file handle for WRITING in Text mode
with open(r"f:\labs\projects\Python_NW_DC_2026\movies.txt", mode="wt") as fh_out:
    for name in movies.keys():
        print(f"{name} {movies[name]}", end="\n", file=sys.stdout)
        print(f"{name} {movies[name]}", end="\n", file=fh_out)
        # fh_out.write(f"{name} {movies[name]}\n")
    # End of Block - filehandle is closed

print("-" * 60)

with open(r"f:\labs\projects\Python_NW_DC_2026\movies.txt", mode="rt") as fh_in:
    for line in fh_in:
        print(line, end="", file=sys.stdout)
    # End of Block - filehandle is closed EVEN if exception happens

