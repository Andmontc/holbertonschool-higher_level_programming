#!/usr/bin/python3
""" Class Square """


class Square:
    """ Attributes of the class """
    def __init__(self, size=0):
        """init method
    size = size of the square, with try an exception """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ area:
        function that defines an area of a square """
        return(self.__size * self.__size)
