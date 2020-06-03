#!/usr/bin/python3
"""Class Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """subclass from rectangle"""
    def __init__(self, size):
        """ fuction init"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
