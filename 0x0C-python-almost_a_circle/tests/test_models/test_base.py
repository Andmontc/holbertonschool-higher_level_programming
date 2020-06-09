#!/usr/bin/python3
"""Unittest for Base class"""

import json
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseClass(unittest.TestCase):
    """This class is for testing the Base class"""

    @classmethod
    def setUpClass(cls):
        """Set up instances for all tests"""
        Base._Base__nb_objects = 0
        cls.b1 = Base()
        cls.b2 = Base(18)
        cls.b3 = Base(7)
        cls.b4 = Base()
        cls.b5 = Base()
        cls.b6 = Base("dam")
        cls.b7 = Base(17.8)
        cls.b8 = Base(None)
        cls.r1 = Rectangle(10, 7, 2, 8)

    def test_id_validation(self):
        """Test to check id's"""

        self.assertEqual(self.b1.id, 1)
		self.assertIsInstance(self.b1, Base)
        self.assertEqual(self.b2.id, 18)
		self.assertIsInstance(self.b2, Base)
        self.assertEqual(self.b3.id, 7)
		self.assertIsInstance(self.b3, Base)
        self.assertEqual(self.b4.id, 2)
		self.assertIsInstance(self.b4, Base)
        self.assertEqual(self.b5.id, 3)
		self.assertIsInstance(self.b5, Base)
        self.assertEqual(self.b6.id, "dam")
		self.assertIsInstance(self.b6, Base)
        self.assertEqual(self.b7.id, 17.8)
		self.assertIsInstance(self.b7, Base)
        self.assertEqual(self.b8.id, 4)
		self.assertIsInstance(self.b8, Base)

	def test_bool_id(self):
        self.assertEqual(True, Base(True).id)

    def test_list_id(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_tuple_id(self):
        self.assertEqual((1, 2), Base((1, 2)).id)

    def test_set_id(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_frozenset_id(self):
        self.assertEqual(frozenset({1, 2, 3}), Base(frozenset({1, 2, 3})).id)

    def test_range_id(self):
        self.assertEqual(range(5), Base(range(5)).id)

    def test_bytes_id(self):
        self.assertEqual(b'Python', Base(b'Python').id)

    def test_bytearray_id(self):
        self.assertEqual(bytearray(b'abcefg'), Base(bytearray(b'abcefg')).id)

    def test_memoryview_id(self):
        self.assertEqual(memoryview(b'abcefg'), Base(memoryview(b'abcefg')).id)

    def test_inf_id(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_NaN_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)
