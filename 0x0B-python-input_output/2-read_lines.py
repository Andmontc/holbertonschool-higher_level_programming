#!/usr/bin/python3
""" read a line or all the lines """


def read_lines(filename="", nb_lines=0):
    """ function that reads a line or all the lines in a file """
    nlines = 0
    with open(filename) as f:
        if nb_lines <= 0:
            print(f.read(), end="")
        lines = 1
        for line in f:
            print(line, end="")
            if nb_lines == lines:
                return
            else:
                lines += 1
