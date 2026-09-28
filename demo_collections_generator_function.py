#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO GENERATE a collection in a more
# memory efficient way be yielding one value at a time.
""" 
    DocString
"""

def get_numbers():
    """ Return an ENTIRE collection of numbers """
    numbers = []
    for x in range(0, 10):
        numbers.append(x)
    return numbers

def generate_numbers():
    """ Generator Function - Yields one value at a time """
    for z in range(0, 10):
        yield z

# for z in get_numbers():
for z in generate_numbers():
    print(z)

print("-" * 60)

# Alternatively, we could use a while loop and the built-in next() function
gen = generate_numbers()
while True:
    num = next(gen, -1)
    if num != -1:
        print(num)
    else:
        break


print("-" * 60)
# Alternatively we could manually get the next yielded values..
gen = generate_numbers()
num1 = next(gen)
num2 = next(gen)
num3 = next(gen)
print(f"Yielded values: ", num1, num2, num3)