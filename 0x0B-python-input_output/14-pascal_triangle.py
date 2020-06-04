#!/usr/bin/python3
""" pascal triangle """


def pascal_triangle(n):
    """ function that prints a pascal triangle"""
    empty = []
    if n <= 0:
        return empty
    pascaltri = [[1]]
    for i in range(1, n):
        tmp = [1]
        for j in range(1, i):
            tmp.append(pascaltri[i - 1][j - 1] + pascaltri[i - 1][j])
        tmp.append(1)
        pascaltri.append(tmp)
    return pascaltri
