#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """test for finding the max integer
        in various situations
    """
    def test_mixed(self):
        """normal usage tests"""
        self.assertEqual(max_integer([0, 1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([5, 4, 3, 2, 1, 0]), 5)
        self.assertEqual(max_integer([4, 1, 3, 5, 0, 2]), 5)
        self.assertEqual(max_integer([-5, -4, -3, -2, -1, 0]), 0)

    def test_empty(self):
        """empty input"""
        self.assertRaises(TypeError, max_integer([]), None)

    def test_one(self):
        """one parameter input"""
        self.assertRaises(TypeError, max_integer([1]), 1)

    def test_float(self):
        """float input"""
        self.assertEqual(max_integer([1.33, 2.44, 1.25]), 2.44)

    def test_combined(self):
        """integer and str input"""
        self.assertRaises(TypeError, max_integer, [1, 2, 'Hello'])

    def test_str(self):
        """str input"""
        self.assertRaises(TypeError, max_integer(['hey']))

    def test_tuple(self):
        """tuple as input"""
        self.assertEqual(max_integer((10, 11, 12, 13)), 13)

    def test_negative_tuple(self):
        """tuple with negative integer input"""
        self.assertEqual(max_integer((-21, -22, -23, -24)), -21)

    def test_tg_numbers(self):
        """three digit integers input"""
        self.assertEqual(max_integer([212, 351, 787, 400, 599]), 787)


if __name__ == '__main__':
    unittest.main()
