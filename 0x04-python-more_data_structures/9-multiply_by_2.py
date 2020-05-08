#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dictmul = {x: a_dictionary[x]*2 for x in a_dictionary}
    return dictmul
