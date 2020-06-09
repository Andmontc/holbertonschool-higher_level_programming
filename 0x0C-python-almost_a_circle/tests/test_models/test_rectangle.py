#!/usr/bin/python3
"""Unit testing rectangle"""

import unittest
from unittest.mock import patch
from io import StringIO
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """This class is for testing the Square class"""

    def setUp(self):
        """Set up method"""
        Base._Base__nb_objects = 0

    def test_id(self):
        """Test to check id's"""

        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_validate_attr(self):
        """Tests to validate error messages of attr"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1 = Rectangle(10, "2")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(10, 2)
            r.width = -10
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(10, 2)
            r.x = {}
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 3, -1)

    def test_area(self):
        """Test to check area function"""

        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_display(self):
        """Test display method"""

        r1 = Rectangle(2, 2)
        expected_output = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1.display()
            self.assertEqual(fake_out.getvalue(), expected_output)
        r1 = Rectangle(1, 1)
        expected_output = "#\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1.display()
            self.assertEqual(fake_out.getvalue(), expected_output)
        r1 = Rectangle(4, 6)
        expected_output = "####\n####\n####\n####\n####\n####\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1.display()
            self.assertEqual(fake_out.getvalue(), expected_output)
        r1 = Rectangle(2, 3, 2, 2)
        expected_output = "\n\n  ##\n  ##\n  ##\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_str(self):
        """Test str method"""

        r1 = Rectangle(4, 6, 2, 1, 12)
        expected_output = "[Rectangle] (12) 2/1 - 4/6\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r1)
            self.assertEqual(fake_out.getvalue(), expected_output)
        r2 = Rectangle(3, 7, 11, 13)
        expected_output = "[Rectangle] (1) 11/13 - 3/7\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r2)
            self.assertEqual(fake_out.getvalue(), expected_output)
        r3 = Rectangle(3, 5, 7)
        expected_output = "[Rectangle] (2) 7/0 - 3/5\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r3)
            self.assertEqual(fake_out.getvalue(), expected_output)
        r4 = Rectangle(3, 5)
        expected_output = "[Rectangle] (3) 0/0 - 3/5\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r4)
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_update(self):
        """Test update method"""

        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(r1.id, 89)

        r1.update(89, 2)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)

        r1.update(89, 2, 3)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)

        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)

        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)

        r1.update(id=1)
        self.assertEqual(r1.id, 1)

        r1.update(width=2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 2)

        r1.update(height=3)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)

        r1.update(x=5)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 5)

        r1.update(y=7)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 5)
        self.assertEqual(r1.y, 7)

        r1.update(2, 4, 6, 8, 10, id=3, width=5, height=7, x=9, y=11)
        self.assertEqual(r1.id, 2)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.height, 6)
        self.assertEqual(r1.x, 8)
        self.assertEqual(r1.y, 10)

    def test_to_dictionary(self):
        """Test to_dictionary method"""

        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        dictionary = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(r1_dictionary, dictionary)
        self.assertEqual(type(r1_dictionary), dict)

        r2 = Rectangle(3, 5, 7)
        r2_dictionary = r2.to_dictionary()
        dictionary = {'x': 7, 'y': 0, 'id': 2, 'height': 5, 'width': 3}
        self.assertEqual(r2_dictionary, dictionary)
        self.assertEqual(type(r2_dictionary), dict)

        r3 = Rectangle(7, 11)
        r3_dictionary = r3.to_dictionary()
        dictionary = {'x': 0, 'y': 0, 'id': 3, 'height': 11, 'width': 7}
        self.assertEqual(r3_dictionary, dictionary)
        self.assertEqual(type(r3_dictionary), dict)


if __name__ == "__main__":
    unittest.main()
