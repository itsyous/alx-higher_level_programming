#!/usr/bin/python3
"""defines unittest for base.py"""


import unittest
from models.Base import Base

class TestBase(unittest.TestCase):
    """testing instantiation for Base class"""
    def test_inst(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_no_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_one_id(self):
        self.assertEqual(7, Base(7).id)

    def test_public_id(self):
        b1 = Base()
        b1.id = 20
        self.assertEqual(20, b1.id)

    def test_nb_inst_private(self):
        with self assertRaises(AttributError):
            print(Base(20).__nb_instances)

    def test_str_id(self):
        self.assertEqual("Python", Base("Python").id)

    def test_float_id(self):
        self.assertEqual(2.5, Base(2.5).id)

    def test_bool_id(self):
        self.assertEqual(True, Base(True).id)

    def test_list_id(self):
        self.assertEqual([6, 7, 8], Base([6, 7, 8]).id)
