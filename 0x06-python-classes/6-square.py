#!/usr/bin/python3
""" Class Square """


class Square:
    """ Attributes of the class """
    def __init__(self, size=0, position=(0, 0)):
        """init method
        size = size of the square"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """ get the data """
        return self.__size

    @property
    def position(self):
        """ get position data """
        return self.__position

    @size.setter
    def size(self, value):
        """change the data"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """ set/change the position value """
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ area:
        function that defines an area of a square """
        return(self.__size * self.__size)

    def my_print(self):
        """ function that print the square """
        if self.__size == 0:
            print("")

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
