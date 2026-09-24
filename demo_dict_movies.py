#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO create, and grow, and shrink
# a dict (Unordered collection with Unique keys).
# Note - from Py 3.6 dict are in INSERTION ORDER.
""" 
    DocString
"""
import pprint
# Created a multi-dimensional dict of lists..
movies = { 'junyl': ['the godfather', 'la la land', 'whiplash'],
           'michael': ['the terminal', 'shrek 3', 'inception'],
           'damian': ['pirates caribbean', 'avengars', 'up'],
           'ninaad': ['interstellar', 'dark knight', 'cars 2']
}
# Grow a dict..
movies['lin'] = ['gattaca', 'she', 'the grand budapest']

# Shrink a dict..
movies.pop('michael') # Remove KEY+VALUE from dict
# movies.popitem() # Removed LAST INSERTED key+value

# Access the dict..
pprint.pprint(movies)
print("-" * 60)
print(f"Damian's favourite list of films is {movies['damian']}")
print(f"Damian's favourite list of films is {movies.get('damian')}")
print(f"Ninaad's favourite film is {movies['ninaad'][0]}")
print("-" * 60)

# An alternative way of accessing dict keys and values is to
# ITERATE through them using an ITERATOR for loop plus..
for name in movies.keys(): # Returns next key
    print(f"{name} loves the films {movies[name]}")

print("-" * 60)
for films in movies.values(): # Returns next value
    print(f"Recommended films: {films}")

print("-" * 60)
for (name, films) in movies.items(): # Returns key+value
    print(f"{name}'s favourite film is {films[0]}")