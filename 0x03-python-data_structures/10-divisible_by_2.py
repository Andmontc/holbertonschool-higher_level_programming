#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return None
    mul = []
    for i in my_list:
        if i % 2 == 0:
            mul.append(True)
        else:
            mul.append(False)
    return mul
