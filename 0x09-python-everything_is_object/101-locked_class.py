#!/usr/bin/python3
""" Define a lockedclass """


class LockedClass:
    """ prevent all instance but first_name """

    __slots__ = ["first_name"]
