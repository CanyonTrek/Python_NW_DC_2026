#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO COPY and optionally FILTER a
# source collection to a destination collection (list/tuple/set/dict..)
""" 
    DocString
"""
students = ['lin', 'junyi', 'michael', 'zechen', 'yihong', 'dominic', 'laura',
            'andras', 'grace', 'isla', 'laura']

# Copy and Optionally filter source collection using..
# 1.Iterator FOR loop + source, condition (filtering), expression
wee_names = []
for name in students: # 1.Iterator loop plus source
    if len(name) <= 5: # 2.Optional condition (filtering)
        wee_names.append(name.upper()) # 3.Expression
print(f"1.Short names = {wee_names}")

# 2.Iterator FOR loop + source, user function (filtering), expression
def filter_names(name):
    """ Return True if parameter passes business logic """
    if len(name) <= 5:
        return True
    else:
        return False

wee_names = []
for name in students: # 1.Iterator loop plus source
    if filter_names(name): # 2.Optional condition (filtering)
        wee_names.append(name.upper()) # 3.Expression
print(f"2.Short names = {wee_names}")

# 3.Built-in filter() function + source, user function (filtering).
wee_names = list(filter(filter_names, students))
print(f"3.Short names = {wee_names}")

# 4.Built-in filter() function + source, lambda function (filtering).
wee_names = list(filter(lambda name:len(name) <= 5, students))
print(f"4.Short names = {wee_names}")

# 5.LIST COMPREHENSION for loop + source, optional if, expression.
wee_names = [ name.upper() for name in students if len(name) <= 5 ]
print(f"5.Short names = {wee_names}")

# 5.1 LIST COMPREHENSION for loop + source, optional if, expression.
wee_names = [ (name.upper(), len(name)) for name in students if len(name) <= 5 ]
print(f"5.1.Short names = {wee_names}")

# 5.2 DICTLIST COMPREHENSION for loop + source, optional if, expression.
# FREE FILTERING - all duplicates KEYS have been removed!
wee_names = { name.upper(): len(name) for name in students if len(name) <= 5 }
print(f"5.2.Short names = {wee_names}")

# 5.3 SET COMPREHENSION for loop + source, optional if, expression.
# FREE FILTERING - all duplicates VALUES have been removed!
wee_names = { name.upper() for name in students if len(name) <= 5 }
print(f"5.3.Short names = {wee_names}")