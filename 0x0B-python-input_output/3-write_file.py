#!/usr/bin/python3
""" write to a file """


def write_file(filename="", text=""):
    with open(filename, 'w') as f:
        return f.write(text)
