#!/usr/bin/python3
"""
Unittest for class Square
"""
import unittest
from models.base import Base
from models.square import Square
import io
from contextlib import redirect_stdout
import os


class TestsSquare(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_square(self):

        s1 = Square(1)
        self.assertEqual(type(s1), Square)

        s2 = Square(1, 2)
        self.assertEqual(type(s2), Square)

        s3 = Square(1, 2, 3)
        self.assertEqual(type(s3), Square)

    def test_id(self):

        s1 = Square(2)
        self.assertEqual(s1.id, 1)

        s2 = Square(10)
        self.assertEqual(s2.id, 2)

        s3 = Square(10, 2, 0, 12)
        self.assertEqual(s3.id, 12)

        s4 = Square(1, 2, 4)
        self.assertEqual(s4.id, 3)

    def test_area(self):
        s1 = Square(3)
        self.assertEqual(s1.area(), 9)

        s2 = Square(2, 10)
        self.assertEqual(s2.area(), 4)

        s3 = Square(8, 0, 0, 12)
        self.assertEqual(s3.area(), 64)

    def test_square_throws_exception(self):
        with self.assertRaises(TypeError):
            Square("1")

        with self.assertRaises(TypeError):
            Square(1, "2")

        with self.assertRaises(TypeError):
            Square(1, 2, "3")

        with self.assertRaises(ValueError):
            Square(-1)

        with self.assertRaises(ValueError):
            Square(1, -2)

        with self.assertRaises(ValueError):
            Square(1, 2, -3)

        with self.assertRaises(ValueError):
            Square(0)

    def test_str(self):

        s1 = Square(6, 2, 1, 12)
        self.assertEqual(str(s1), "[Square] (12) 2/1 - 6")

        s2 = Square(5, 5, 1)
        self.assertEqual(str(s2), "[Square] (1) 5/1 - 5")

    def test_to_dict(self):

        s = Square(1, 1, 1, 1)
        res_dict = {"id": 1, "size": 1, "x": 1, "y": 1}
        self.assertEqual(s.to_dictionary(), res_dict)

    def test_update(self):

        s = Square(1, 1, 1, 1)
        s.update(x = 3, y = 3)
        res_dict = {"id": 1, "size": 1, "x": 3, "y": 3}
        self.assertEqual(s.to_dictionary(), res_dict)

    def test_create(self):

        s1 = Square(3, 5, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(s1.to_dictionary(), s2.to_dictionary())

    def test_save_to_file(self):

        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            reading = file.read()
        self.assertEqual(reading, "[]")

        os.remove("Square.json")

        Square.save_to_file([])
        with open("Square.json", "r") as file:
            reading = file.read()
        self.assertEqual(reading, "[]")

        s1 = Square(10, 7, 2, 8)
        s2 = Square(2, 4, 3)
        Square.save_to_file([s1, s2])

        with open("Square.json", "r") as file:
            reading = file.read()

        res_list  = '[{"id": 8, "size": 10, "x": 7, "y": 2},' \
                    ' {"id": 1, "size": 2, "x": 4, "y": 3}]'
        self.assertEqual(reading, res_list) 

    def test_load_from_file(self):

        os.remove('Square.json')

        list_squares_output = Square.load_from_file()
        self.assertEqual(list_squares_output, [])

        r1 = Square(2, 4, 3)
        list_squares_input = [r1]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        res_dict = {'id': 1, 'size': 2, 'x': 4, 'y': 3}
        self.assertEqual(list_squares_output[0].to_dictionary(), res_dict)

