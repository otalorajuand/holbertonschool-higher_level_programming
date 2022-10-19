#!/usr/bin/python3
"""
Unittest for class Rectangle
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
import io
from contextlib import redirect_stdout


class TestRectangle(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_rectangle(self):

        r1 = Rectangle(1, 2)
        self.assertEqual(type(r1), Rectangle)

        r2 = Rectangle(1, 2, 3)
        self.assertEqual(type(r2), Rectangle)

    def test_id(self):

        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

        r4 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r4.id, 3)

    def test_area(self):
        r1 = Rectangle(3, 2)
        self.assertAlmostEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertAlmostEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertAlmostEqual(r3.area(), 56)
    
    def test_str(self):

        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertAlmostEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

        r2 = Rectangle(5, 5, 1)
        self.assertAlmostEqual(str(r2), "[Rectangle] (1) 1/0 - 5/5")

    def test_rectangle_throws_exception(self):
        with self.assertRaises(TypeError):
            Rectangle(10, "2")

        with self.assertRaises(TypeError):
            Rectangle("1", 2)

        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

        with self.assertRaises(ValueError):
            r = Rectangle(10, 2)
            r.width = -10

        with self.assertRaises(TypeError):
            r = Rectangle(10, 2)
            r.x = {}

        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

        with self.assertRaises(ValueError):
            Rectangle(1, -2)

        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

        with self.assertRaises(ValueError):
            Rectangle(10, 2, 3, -1)

        with self.assertRaises(ValueError):
            Rectangle(0, 2)

        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_display(self):
        r = Rectangle(2, 2)
        input_string = io.StringIO()
        res_str = "##\n##\n"
        with redirect_stdout(input_string):
            r.display()
        self.assertEqual(res_str, input_string.getvalue())
        
        r.x = 1
        res_str =  " ##\n ##\n"
        input_string = io.StringIO()
        with redirect_stdout(input_string):
            r.display()
        self.assertEqual(res_str, input_string.getvalue())

        r.y = 1
        res_str = "\n ##\n ##\n"
        input_string = io.StringIO()
        with redirect_stdout(input_string):
            r.display()
        self.assertEqual(res_str, input_string.getvalue())

    def test_to_dict(self):

        r = Rectangle(1, 1, 1, 1)
        res_dict = {"id": 1, "width": 1, "height": 1, "x": 1, "y": 1}
        self.assertEqual(r.to_dictionary(), res_dict)
