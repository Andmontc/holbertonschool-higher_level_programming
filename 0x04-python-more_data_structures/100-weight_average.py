#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or my_list = []:
        return 0
    mul = 0
    div = 0
    for i in my_list:
        mul += (i[0] * i[1])
        div += i[1]
    return mul / div
