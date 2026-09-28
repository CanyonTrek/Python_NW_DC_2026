#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This module defines a class of Tank for a Game of Tanks
""" 
    Tank Class for a tank game
"""
from GOT.app import vehicle

class Tank(vehicle.Vehicle):
    # Two Components = Attributes/Data + Behaviour/Methods
    def __init__(self, country, model):
        vehicle.Vehicle.__init__(self, country, model)
        self._direction = 0
        self._location = {'x':0, 'y':0, 'z':0}
        self._shells = 20
        self._health = 100
        # No EXPLICIT return as method is called implicitly


    def rotate_left(self, degrees):
        self._direction -= degrees % 360
        return None

    def rotate_right(self, degrees):
        self._direction += degrees % 360
        return None

    def shoot(self):
        self._shells -= 1
        return None

    def take_damage(self, damage):
        self._health -= damage
        return None

    # And now for some SPECIAL methods..
    # Example of OPERATOR overloading
    def __add__(self, other):
        return self._health + other._health

    # Example of a GETTER and SETTER method
    def get_health(self):
        return self._health

    def set_health(self, new_health):
        self._health = new_health
        return None

    # WRAP ONE variable name interface to getter and setter
    # tank_health = property(get_health, set_health)

    # Alternatively we could DECORATE a function
    @property
    def tank_health(self):
        return self._health

    @tank_health.setter
    def tank_health(self, new_health):
        self._health = new_health
        return None