#!/usr/bin/python3
"""
Unittest for class Base
"""
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_id_base(self):

        b1 = Base()
        self.assertAlmostEqual(b1.id, 1)

        b2 = Base()
        self.assertAlmostEqual(b2.id, 2)

        b3 = Base()
        self.assertAlmostEqual(b3.id, 3)

        b4 = Base(12)
        self.assertAlmostEqual(b4.id, 12)

        b5 = Base()
        self.assertAlmostEqual(b5.id, 4)


if __name__ == '__main__':
    unittest.main()
