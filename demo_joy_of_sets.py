#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO create a set, and grow, and shrink and
# combine sets using SET operators (Remember VENN Diagrams)
""" 
    DocString
"""
marvel_fans = {'donald', 'ninaad', 'michael', 'lin', 'laura', 'yihong'}
dc_fans = set() # Create an empty set.

# Grow a set..
dc_fans.add('donald')
dc_fans.add('dominic')
dc_fans.add('junyl')

# Shrink a set..
# dc_fans.pop() # Randomly remove an object
# comic_fans = dc_fans.copy() # Copy set
# comic_fans.clear() # Empty set

#  COMBINE sets using SET operator methods (Venn Diagrams)
print(f"Fans of Marvel or DC = {marvel_fans.union(dc_fans)}")
print(f"Fans of Marvel AND DC = {marvel_fans.intersection(dc_fans)}")
print(f"Fans of ONLY Marvel = {marvel_fans.difference(dc_fans)}")
print(f"Fans of EITHER ONLY Marvel OR DC = {marvel_fans.symmetric_difference(dc_fans)}")
print("-" * 60)
#  COMBINE sets using SET operators (Venn Diagrams)
print(f"Fans of Marvel or DC = {marvel_fans | dc_fans}")
print(f"Fans of Marvel AND DC = {marvel_fans & dc_fans}")
print(f"Fans of ONLY Marvel = {marvel_fans - dc_fans}")
print(f"Fans of EITHER ONLY Marvel OR DC = {marvel_fans ^ dc_fans}")




