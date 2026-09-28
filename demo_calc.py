#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will emulate a basic calculator
""" 
    DocString
"""

def add(x, z):
    """ Return SUM of x and z as a float """
    return float(x + z)

print(f"4 + 3 = {add(4, 3)}")
print(f"4 + 3 = {(lambda x, z:float(x + z))(4, 3)}")