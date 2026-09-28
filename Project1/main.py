#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This is a calculator APP
""" 
    Calculator APP with basic and advanced functions
"""
import sys
# from calc.app import basic # SAFER - import into their OWN namespace :-)
# from calc.app.basic import * # Import ALL identifiers into __main__ namespace
from calc.app.basic import add, mul, div
from calc.app import adv

def main():
    menu = """
            Menu Options
            ------------
            1.Display Basic Calc examples
            2.Display Advanced Calc examples
            q=quit
    """
    while True:
        print(menu)
        option = input("Enter (1-2,q=quit): ")
        match option:
            case "1":
                print(f"20 + 19 + 18 = {add(20, 19, 18)}")
                print(f"20 * 19 * 18 = {mul(20, 19, 18)}")
                print(f"20 / 19 = {div(20, 19)}")
            case "2":
                print(f"200 % 19 = {adv.mod(200, 19)}")
                print(f"20 ** 3 = {adv.power(20, 3)}")
                print(f"\N{square root}335 = {adv.sqrt(335)}")
            case "q":
                break
            case _:
                print("Invalid option")
    return None


# Namespace Trick
if __name__ == "__main__":
    # Execute ONLY if ran directly as a program
    # Ignore if imported as a module
    main()
    sys.exit(0) # Exit and return exit code (0=success, 1-255=error)









