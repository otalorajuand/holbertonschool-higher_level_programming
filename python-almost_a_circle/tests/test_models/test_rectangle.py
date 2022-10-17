#!/usr/bin/python3
"""
Unittest for class Rectangle
"""
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_id(self):

        r1_id = Rectangle(10, 2)
        self.assertAlmostEqual(r1_id.id, 1)

        r2_id = Rectangle(2, 10)
        self.assertAlmostEqual(r2_id.id, 2)

        r3_id = Rectangle(10, 2, 0, 0, 12)
        self.assertAlmostEqual(r3_id.id, 12)

    def test_area(self):
        r1_area = Rectangle(3, 2)
        self.assertAlmostEqual(r1_area.area(), 6)

        r2_area = Rectangle(2, 10)
        self.assertAlmostEqual(r2_area.area(), 20)

        r3_area = Rectangle(8, 7, 0, 0, 12)
        self.assertAlmostEqual(r3_area.area(), 56)


    """
    def test_str(self):

        r1_str = Rectangle(4, 6, 2, 1, 12)
        self.assertAlmostEqual(str(r1_str), "[Rectangle] (12) 2/1 - 4/6")

        r2_str = Rectangle(5, 5, 1)
        self.assertAlmostEqual(str(r2_str), "[Rectangle] (1) 1/0 - 5/5")
    """


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
