#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO format your strings using
# str concatenation, escape chars, str methods and f-strings!
""" 
    DocString
"""
# Dict of planets and their distance to the sun in Gigametres.
planets = {'Mercury': 57.91,
           'Venus': 108.2,
           'Earth': 149.597870,
           'Mars': 227.94
}

# ITERATE through the planets dict and display planet info
# using an ITERATOR for loop plus..
# ..str concatenation and escape chars. MEH!
for planet in planets.keys():
    print("\t\t" + planet + ": \t" + str(planets[planet]) + " Gm")

print("-" * 60)
# ..str concatenation and str justification methods. OK!
for planet in planets.keys():
    print(planet.rjust(12) + ": " + str(planets[planet]).rjust(12, '.') + " Gm")

print("-" * 60)
# ..str.format method. GOOD!
for planet in planets.keys():
    print("{0:>12s}: {1:.>12.3f} Gm".format(planet, planets[planet]))

print("-" * 60)
# ..f-strings (Python 3.5). BEST!
for planet in planets.keys():
    print(f"{planet:>12s}: {planets[planet]:.>12.3f} Gm")



