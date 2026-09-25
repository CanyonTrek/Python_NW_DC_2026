#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO define and name a USER FUNCTION,
# call it with optional parameters and optional return value.
""" 
    DocString
"""
# Example of a user function with optional
# parameter passing and default values.
# Enforce named parameters using *,
# And using Annotations (embedded comment)
def say_hello(greeting: str = "ciao", recipient: str = "amici") -> None:
    message = f"{greeting} {recipient}"
    print(message)
    return None

say_hello("hello", "my friends") # Positional parameters
say_hello(greeting="hola", recipient="mis amigos") # Named parameter passing
say_hello(recipient="ni ore mi", greeting="bawo") # Named parameters (different order)
say_hello("privet", recipient="moi druk") # Mixed parameters (positional->named)
say_hello("bonjour", "mes amis")
say_hello("ciao")
say_hello()


