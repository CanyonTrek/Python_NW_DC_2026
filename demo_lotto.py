#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will generate 6 random
# lottery numbers
""" 
    DocString
"""
import random

lotto = [] # Create an empty list

while len(lotto) < 6:
    num = random.randint(1, 50)
    if num not in lotto:
        lotto.append(num)
    else:
        print("Duplicate number =", num)


print("Lottery numbers", lotto)
print("Done.")
