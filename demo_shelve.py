#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO PRESERVE ONE Python Object
# to a pickle file using the pickle module
"""
    DocString
"""
import shelve


movies = { 'junyl': ['the godfather', 'la la land', 'whiplash'],
           'michael': ['the terminal', 'shrek 3', 'inception'],
           'damian': ['pirates caribbean', 'avengars', 'up'],
           'ninaad': ['interstellar', 'dark knight', 'cars 2']
}

tv_series = {'junyl': ['friends', 'GOT'],
             'michael': ['the office us', 'the office uk'],
             'damian': ['invicible', 'breaking bad'],
             'ninaad': ['breaking bad', 'peaky blinders']
}

books = {'junyl': 'the intelligent investor book',
         'michael': 'python for dummies',
         'damian': 'diary of a wimpy kid',
         'ninaad': 'da vinci code'
}

with shelve.open(r"f:\labs\projects\Python_NW_DC_2026\media") as db:
    db['movies'] = movies
    db['tv_series'] = tv_series
    db['books'] = books

with shelve.open(r"f:\labs\projects\Python_NW_DC_2026\media") as db:
    print(f"Ninaad's favourite films are {db['movies']['ninaad']}")
    print(f"Damian's favourite tv_series is {db['tv_series']['damian'][0]}")
    print(f"Junyl's favourite book is {db['books']['junyl']}")