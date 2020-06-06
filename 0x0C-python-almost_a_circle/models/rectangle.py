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
    def width(self, width):
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

    def display(self):
        """ print the rectangle in stdout"""
        for i in range(self.__y):
            print("")
        for h in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.width)

    def __str__(self):
        """ override str """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.__x, self.__y, self.__width,
                self.__height)

    def update(self, *args, **kwargs):
        """ update with args and kwargs"""
        if args:
            count = 0
            for arg in args:
                if count == 0:
                    self.id = arg
                elif count == 1:
                    self.__width = arg
                elif count == 2:
                    self.__height = arg
                elif count == 3:
                    self.__x = arg
                elif count == 4:
                    self.__y = arg
                count += 1
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)
