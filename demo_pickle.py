#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO PRESERVE ONE Python Object
# to a pickle file using the pickle module
""" 
    DocString
"""
import pickle
import pprint
import gzip # Others tarfile, bz2, shutil

movies = { 'junyl': ['the godfather', 'la la land', 'whiplash'],
           'michael': ['the terminal', 'shrek 3', 'inception'],
           'damian': ['pirates caribbean', 'avengars', 'up'],
           'ninaad': ['interstellar', 'dark knight', 'cars 2']
}

# Open file handle for WRITING in BYTES mode
# with open(r"f:\labs\projects\Python_NW_DC_2026\movies.p", mode="wb") as fh_out:
with gzip.open(r"f:\labs\projects\Python_NW_DC_2026\movies.pgz", mode="wb") as fh_out:
    # pickle.dump(movies, fh_out, protocol=5) # Protocol (0=ASCII, 1-5=BINARY)
    pickle.dump(movies, fh_out, pickle.DEFAULT_PROTOCOL)  # Default=4
    # pickle.dump(movies, fh_out, pickle.HIGHEST_PROTOCOL)  # Default=5

# Open file handle for READING in BYTES mode
with gzip.open(r"f:\labs\projects\Python_NW_DC_2026\movies.pgz", mode="rb") as fh_in:
    films = pickle.load(fh_in)


pprint.pprint(movies)
print("-" * 60)
pprint.pprint(films)
