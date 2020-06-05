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
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")
    for row in matrix:
        for number in row:
            if type(number) != int and type(number) != float:
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers/floats")
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not all(len(matrix[0]) == len(row) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    return [list(map(lambda n: round(n / div, 2), row)) for row in matrix]
