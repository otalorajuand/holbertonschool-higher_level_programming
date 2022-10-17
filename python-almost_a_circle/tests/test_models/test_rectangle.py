#!/usr/bin/python3
"""
Unittest for class Rectangle
"""
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_rectangle(self):

        r1 = Rectangle(10, 2)
        self.assertAlmostEqual(r1.id, 1)
        self.assertAlmostEqual(r1.area(), 20)

        r2 = Rectangle(2, 10)
        self.assertAlmostEqual(r2.id, 2)
        self.assertAlmostEqual(r2.area(), 20)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertAlmostEqual(r3.id, 12)
        self.assertAlmostEqual(r3.area(), 20)

    def test_rectangle_throws_exception(self):
        with self.assertRaises(TypeError):
            Rectangle(10, "2")

        with self.assertRaises(ValueError):
            r = Rectangle(10, 2)
            r.width = -10

        with self.assertRaises(TypeError):
            r = Rectangle(10, 2)
            r.x = {}

        with self.assertRaises(ValueError):
            Rectangle(10, 2, 3, -1)
