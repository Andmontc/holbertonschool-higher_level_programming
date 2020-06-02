#!/usr/bin/python3
"""Class BaseGeometry"""


class BaseGeometry:
    """Class BaseGeometry"""
    def area(self):
        """ Exception area not defined """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates values
            Args: name and value
            Raises: Errors"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
