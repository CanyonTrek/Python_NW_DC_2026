#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO open, and close and filehandle
# for RANDOM read and write using .seek() and .tell() methods
""" 
    DocString
"""

# Open file handle for READING in TEXT mode
with open(r"f:\labs\projects\Python_NW_DC_2026\movies.txt", mode="rt") as fh_in:
    fh_in.seek(90, 0) # Seek forwards 90 chars from SOF
    text = fh_in.read(30)
    print(f"Text at {fh_in.tell() - len(text)} = {text}")

    fh_in.seek(135, 0) # Seek forwards 135 chars from SOF
    text = fh_in.read(30)
    print(f"Text at {fh_in.tell() - len(text)} = {text}")

# Open file handle for READING in bytes mode
with open(r"f:\labs\projects\Python_NW_DC_2026\movies.txt", mode="rb") as fh_data:
    fh_data.seek(-90, 2) # Seek back 90 bytes from EOF
    text = fh_data.read(30)
    print(f"Text at {fh_data.tell() - len(text)} = {text}")

    fh_data.seek(-70, 1) # Seek back 70 bytes from current byte position
    text = fh_data.read(30)
    print(f"Text at {fh_data.tell() - len(text)} = {text}")