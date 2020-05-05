#!/usr/bin/python3
def no_c(my_string):
    if my_string is None:
        return None
    copia = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            copia += i
    return copia
