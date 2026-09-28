#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO 
""" 
    Example of using a TEST RUNNER
"""
from Project1.calc.app import basic
import unittest

class TestBasic(unittest.TestCase):
    def test_add(self):
        self.assertEqual(basic.add(4, 3, 2, 1), 10.0, "Should be 10.0")
        return None

    def test_mul(self):
        self.assertEqual(basic.mul(4, 3, 2), 24.0, "Should be 24.0")
        return None

    def test_div(self):
        self.assertEqual(basic.div(4, 3), 1.333, "Should be 1.333")
        return None

if __name__ == "__main__":
    unittest.main()