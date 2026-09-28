#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This is a ultra realistic game with Tanks
""" 
    GOT - Game of Tanks
"""
import sys
from GOT.app import tank

def main():
    # Create/Instantiate 3 new Tank objects
    laura_tank = tank.Tank('german', 'tiger')
    lin_tank = tank.Tank('german', 'tiger')
    andras_tank = tank.Tank('german', 'tiger')

    # And now the game begins..
    laura_tank.accel(63)
    lin_tank.accel(28)

    andras_tank.rotate_left(289)
    andras_tank.accel(31)
    andras_tank.shoot()

    # and success..
    laura_tank.take_damage(67)
    lin_tank.take_damage(29)

    # And now for some visuals...
    print(f"Health of Laura's tank is {laura_tank._health}") # POOR CODE

    # Example of Operator Overloading
    print(f"Health of Laura's and Lin's tanks = {laura_tank + lin_tank}")

    # Laura has received a HEALTH BOOST
    # laura_tank._health = 100 # POOR CODE
    # print(f"NEW health of Laura's tank is {laura_tank._health}") POOR CODE

    # Example of a GETTER and SETTER method
    laura_tank.set_health(101) # SETTER method GOOD
    print(f"NEW health of Laura's tank is {laura_tank.get_health()}") # GETTER method GOOD

    laura_tank.tank_health = 102 # property
    print(f"NEW health of Laura's tank is {laura_tank.tank_health}") # Special Property
    return None


if __name__ == "__main__":
    main()
    sys.exit(0)