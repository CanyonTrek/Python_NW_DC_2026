#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO ITERATE through values in a
# SEQUENCE (str/tuple/list/dict keys/set) using an ITERATOR for loop.
""" 
    DocString
"""
#               0                 1                2               3
heroes = ['billy connolly', 'didier drogba', 'steven morrisey', 'andras']

# ITERATE through heroes one object at a time using
# an ITERATOR for loop.
for name in heroes:
    print(name, end="\n")

# ITERATE through heroes one object at a time and MODIFY the objects
# using an ITERATOR for loop.
idx = 0
for name in heroes:
    print(name.upper(), end="\n")
    heroes[idx] = name.upper()
    idx += 1
print("Heroes =", heroes)

# ITERATE through heroes one object at a time and MODIFY the objects
# using an ITERATOR for loop and built-in function enumerate().
for (idx, name) in enumerate(heroes):
    print(name.title(), end="\n")
    heroes[idx] = name.title()
print("Heroes =", heroes)