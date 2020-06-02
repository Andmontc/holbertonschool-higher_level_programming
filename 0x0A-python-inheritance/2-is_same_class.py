#!/usr/bin/python3


def is_same_class(obj, a_class):
    """ function that compare the type of an object
        Args: obj = object
              a_class = instance
        Return: true if is instance, false if not """

    if (type(obj) == a_class):
        return True
    return False
