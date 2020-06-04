#!/usr/bin/python3
""" Class Student """


class Student:
    """ Class Student init """
    def __init__(self, first_name, last_name, age):
        """ init of the class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ dictionary from Student"""
        return self.__dict__
