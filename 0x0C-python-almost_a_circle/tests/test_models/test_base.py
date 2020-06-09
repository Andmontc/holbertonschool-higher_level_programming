#!/usr/bin/python3
"""Unittest for Base class"""

import json
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import pep8


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

class TestBasepep8(unittest.TestCase):
    """Validate pep8"""

    def test_pep8(self):
        """test for base file and test_base file pep8"""
        style = pep8.StyleGuide(quiet=True)
        base = "models/base.py"
        test_base = "tests/test_models/test_base.py"
        result = style.check_files([base, test_base])
        self.assertEqual(result.total_errors, 2)

class TestDocs(unittest.TestCase):
    """test docstrings for base and test_base files"""

    def test_module(self):
        """check module docstrings"""
        self.assertTrue(len(Base.__doc__) > 0)

    def test_class(self):
        """check class docstrings"""
        self.assertTrue(len(Base.__doc__) > 0)

    def test_method(self):
        """check method docstrings"""
        for func in dir(Base):
            self.assertTrue(len(func.__doc__) > 0)

if __name__ == "__main__":
    unittest.main()
