#!/usr/bin/python3
""" write to a file """


def write_file(filename="", text=""):
    """ function that write into a file """
    with open(filename, 'w') as f:
        return f.write(text)
