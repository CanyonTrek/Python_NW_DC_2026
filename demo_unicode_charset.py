#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will display the ENTIRE Unicode charset (0->65535)
""" 
    DocString
"""

for pos in range(0, 65536):
    try:
        print(chr(pos), end=" ")
        if pos % 16 == 0:
            print()
    except UnicodeEncodeError:
        print(" ")
