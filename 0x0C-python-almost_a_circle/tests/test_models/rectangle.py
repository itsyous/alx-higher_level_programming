#!/usr/bin/python3
"""defines a test for Rectangle"""

import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestRectangle_method(unittest.TestCase):
    """testing instantiation for Rectangle"""

    def test_rectangle_base(self):
        self.assertIsInstance(Rectangle(19, 8), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(4)

    def test_Rect(self):
        rec1 = Rectangle(40, 2)
        rec2 = Rectangle(88, 46)
        self.asserEqual(rec1.id, rec2.id - 1)

    def test_three_arg(self):
        rec1 = Rectangle(8, 9, 10)
        rec2 = Rectangle(20, 35, 97)
        self.asserEqual(rec1.id, rec2.id - 1)

    def test_four_arg(self):
        rec1 = Rectangle(8, 9, 10, 88)
        rec2 = Rectangle(20, 35, 97, 33)
        self.asserEqual(rec1.id, rec2.id - 1)
