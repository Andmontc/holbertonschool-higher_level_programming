#!/usr/bin/python3
""" Return the number of lines"""


def number_of_lines(filename=""):
    """ function that return the number of lines """
    nlines = 0
    with open(filename) as f:
        for line in f:
            nlines += 1
    return nlines
