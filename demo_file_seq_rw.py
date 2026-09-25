#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO open, and close a file, for reading
# and writing. and appending in TEXT mode.
""" 
    DocString
"""

# Created a multi-dimensional dict of lists..
movies = { 'junyl': ['the godfather', 'la la land', 'whiplash'],
           'michael': ['the terminal', 'shrek 3', 'inception'],
           'damian': ['pirates caribbean', 'avengars', 'up'],
           'ninaad': ['interstellar', 'dark knight', 'cars 2']
}

# Open file handle for WRITING in Text mode
fh_out = open(r"f:\labs\projects\Python_NW_DC_2026\movies.txt", mode="wt")

# Iterate through the movies keys using for loop plus .keys()
for name in movies.keys():
    print(f"{name} {movies[name]}", end="\n")
    fh_out.write(f"{name} {movies[name]}\n")

# fh_out.flush() # Flush buffers
fh_out.close() # Flush buffers and close filehandle

print("-" * 60)

# Open file handle for READING in TEXT mode
fh_in = open(r"f:\labs\projects\Python_NW_DC_2026\movies.txt", mode="rt")

# text = fh_in.read() # Read ENTIRE file into str object. Be careful of HUGE files
# text = fh_in.read(30) # Read NEXT 30 chars into str.
# text = fh_in.readline() # Read NEXTLINE chars into str.
# lines = fh_in.readlines() # Read ENTIRE file into LIST object. Be careful of HUGE files.
# print(f"First line is {lines[0]}")
# print(f"Last line is {lines[-1]}")

# ITERATE through file handle one line at a time
# using ITERATOR for loop and filehandle (Iterable Object = next/iter)
# for line in open(r"f:\labs\projects\Python_NW_DC_2026\movies.txt", mode="rt"):
for line in fh_in:
    print(line, end="")

fh_in.close()
