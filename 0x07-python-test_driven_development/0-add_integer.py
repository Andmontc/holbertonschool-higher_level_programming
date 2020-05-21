#!/usr/bin/python3
"""
    module add
    sums numbers
    return add
"""


def add_integer(a, b=98):
    """
    Function that adds numbers
     a (int or float) first number, b (int or float) second number """

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")

    return (a + b)
