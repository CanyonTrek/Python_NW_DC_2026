#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO ITERATE through files/dirs in the
# file system one item at a time using the glob module
""" 
    DocString
"""
import sys
import os
import glob
home = ""

if sys.platform == "win32":
    home = os.environ["HOMEDRIVE"] + os.environ["HOMEPATH"]
elif sys.platform == "linux":
    home = os.environ["HOME"]

files = glob.glob(os.path.join(home, "*")) # Return list of files/dirs
print(files)

# ITERATE through the files/dirs using an ITERATOR for loop
for file in glob.iglob(os.path.join(home, "*")):
    print(file)


try:
    sys.exit(66) # Explicit EXIT with return code (0=success, 1-255=error)
    # sys.exit("Goodbye") # Explicit EXIT and send EXPR to STDERR (in RED) and code 1
except SystemExit:
    print("Exiting program")
    sys.exit(0)