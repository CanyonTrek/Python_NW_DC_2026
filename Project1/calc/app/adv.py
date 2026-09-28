#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This module defines several ADVANCED functions for a calculator App
""" 
    Advanced Calculator functions including power, modules and sqrt
"""
import sys

def mod(x, z):
    """ Return Remainder of x divided by as a float """
    return float(x % z)

def power(x, z):
    """ Return x raised to the power of z as a float """
    return float(x ** z)

def sqrt(x):
    """ Return square root of x as a float """
    return float(x ** 0.5)

print("------------ ADVANCED CALC ------------")
print(f"100 % 30 = {mod(100, 30)}")
print(f"4 ** 3 = {power(4, 3)}")
print(f"\N{square root}100 = {sqrt(100)}")
print("----------------------------------------")

sys.exit(0)