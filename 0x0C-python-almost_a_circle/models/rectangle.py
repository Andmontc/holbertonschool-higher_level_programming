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
        return self.__x

    @property
    def y(self):
        """ get data (getter)"""
        return self.__y

    @width.setter
    def width(self,width):
        """ change the data (width setter) """
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        """ change the data ( height setter) """
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @x.setter
    def x(self, x):
        """ change the data (x setter) """
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be > 0")
        self.__x = x

    @y.setter
    def y(self, y):
        """ change the data (y setter) """
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be > 0")
        self.__y = y

    def area(self):
        """ area of the rectangle """
        return self.__width * self.__height
    