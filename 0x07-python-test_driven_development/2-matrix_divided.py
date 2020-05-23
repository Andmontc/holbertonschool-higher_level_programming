#!/usr/bin/python3
"""
This module defines the matrix_divided function
"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.
    Args:
        matrix (list): A list of lists of ints or floats.
        div (int/float): The divisor.
    Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.
    Returns:
        A new matrix representing the result of the division.
    """
    err1 = "matrix must be a matrix (list of lists) of integers/floats"
    err2 = "Each row of the matrix must have the same size"
    err3 = "div must be a number"

    if not matrix:
        raise TypeError(err1)
    if matrix == [[]] or matrix == []:
        raise TypeError(err1)

    count = len(matrix[0])

    for lists in matrix:
        comp = len(lists)
        for ele in lists:

            if not isinstance(ele, (int, float)):
                raise TypeError(err1)
        if comp != count:
            raise TypeError(err2)

    if not isinstance(div, (int, float)):
        raise TypeError(err3)

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new = [[round(i/div, 2) for i in row] for row in matrix]

    return new
