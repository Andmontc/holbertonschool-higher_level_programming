#!/usr/bin/python3
""" append to a file """


def append_write(filename="", text=""):
    """ function that append a string """
    with open(filename, 'a') as f:
        return f.write(text)
