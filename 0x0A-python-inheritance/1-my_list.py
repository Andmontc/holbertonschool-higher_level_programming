#!/usr/bin/python3
""" Creating a class"""


class MyList(list):
    """ Class Mylist inherit from list"""
    def print_sorted(self):
        """ function that print the sorted list """
        print(sorted(self))
