#!/usr/bin/python3
""" module for subclass Rectangle """
from models.base import Base


class Rectangle(Base):
    """ class that represent a rectangle inherited from Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ constructor """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
@property
def width(self):
    """ get data (getter)"""
    return self.__width
@property
def height(self):
    """ get data (getter)"""
    return self.__height
@property
def x(self):
    """ get data (getter)"""
    return self.x
@property
def y(self):
    """ get data (getter)"""
    return self.__y
