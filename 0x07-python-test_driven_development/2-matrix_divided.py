#!/usr/bin/python3
"""
This module defines the matrix_divided function
"""


def matrix_divided(matrix, div):
    """
    Function that divide all elemtens from a matrix
    Args:
        matrix (list): Matrix.
        div (int): divisor.
    Returns:
        list: new Matrix divided
    """

    new_matrix = []

    msg = "matrix must be a matrix (list of lists) of integers/floats"

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div is 0:
        raise ZeroDivisionError("division by zero")

    if type(matrix) is not list or matrix == []:
        raise TypeError(msg)
    else:
        longitude = len(matrix[0])

    for f_matrix in matrix:
        if any(type(x) not in [int, float] for x in f_matrix):
            raise TypeError(msg)

        if type(f_matrix) is not list or f_matrix == []:
            raise TypeError(msg)

        if len(f_matrix) is not longitude:
            raise TypeError("Each row of the matrix must have the same size")

        new_matrix.append(list(map(lambda x: round(x / div, 2), f_matrix)))

    return new_matrix
