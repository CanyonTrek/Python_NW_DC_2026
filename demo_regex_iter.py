#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO 
""" 
    DocString
"""
import re

df_data = r"c:\     498532348 341747480 156784968  69%  /mnt/c"

numbers = re.findall(r"\b\d+\b", df_data) # Returns a list
print(numbers)

for m in re.finditer(r"\b\d+\b", df_data):
    print(f" Sequence {m.group()} at {m.start()}-{m.end()}")
