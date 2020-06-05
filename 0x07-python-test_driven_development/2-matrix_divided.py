#!/usr/bin/python3
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
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    for column in matrix:
        if len(column) is not len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        if isinstance(len(column), (int, float)):
            tmp_list = list(map(lambda row: round(row / div, 2), column))
            new_matrix.append(tmp_list)
        else:
            raise TypeError(msg)

    return new_matrix
