#!/usr/bin/python3

"""This module defines the print_square function"""


def print_square(size):
    """
    Function that print a square
    Args:
        size (int): Size of the square.
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    if size < 0:
        raise TypeError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
