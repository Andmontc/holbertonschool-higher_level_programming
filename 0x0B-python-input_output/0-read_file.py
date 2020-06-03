#!/usr/bin/python3
"""Read a txt file"""


def read_file(filename=""):
    """ function that reads a text file"""
    with open(filename) as f:
        print(f.read(), end="")
