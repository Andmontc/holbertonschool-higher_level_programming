#!/usr/bin/python3
""" Class MagicClass """
import math


class MagicClass(self):
    """ Class for circle"""
    def __init__(self, radius=0):
        """ init MagicClass"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """ function area"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """ function circumference"""
        return (self.__radius * 2) * math.pi
