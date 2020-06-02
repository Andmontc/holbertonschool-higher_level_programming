#!/usr/bin/python3
""" Function that returns a list """

def lookup(obj):
    """ Return the list of available attributes
        and methods of an object
        Args: object """
    return(dir(obj))
