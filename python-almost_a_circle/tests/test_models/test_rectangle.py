#!/usr/bin/python3
"""
Unittest for class Rectangle
"""
import unittest
from models.rectangle import Rectangle

class TestBase(unittest.TestCase):
    def test_rectangle(self):

        r1 = Rectangle(10, 2)
        self.assertAlmostEqual(r1.id, 1)

        r2 = Rectangle(2, 10)
        self.assertAlmostEqual(r2.id, 2)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertAlmostEqual(r3.id, 12)
