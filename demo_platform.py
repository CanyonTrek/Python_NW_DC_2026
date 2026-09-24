#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO CHECK which platform your script
# is running on..
""" 
    DocString
"""
import sys
import os

if sys.platform == "win32":
    home = os.environ["HOMEPATH"]
elif sys.platform == "linux":
    home = os.environ["HOME"]
else:
    print("Script is running on", sys.platform)

print("My home directory is", home)