#!/usr/bin/python3
""" class module for square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Square inherited from Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor for square """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ getter size as width """
        return self.width

    @size.setter
    def size(self, size):
        """ setter for sizes of the square """
        self.width = size
        self.height = size

    def __str__(self):
        """ override str method """
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """ update with args and kwargs"""
        if args:
            count = 0
            for arg in args:
                if count == 0:
                    self.id = arg
                elif count == 1:
                    self.size = arg
                elif count == 2:
                    self.x = arg
                elif count == 3:
                    self.y = arg
                count += 1
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """ Dictionary representation of Square """
        ndicts = {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
        return ndicts
