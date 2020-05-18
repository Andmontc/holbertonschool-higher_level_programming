#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    j = 0
    for i in my_list[:x]:
        try:
            print("{:d}".format(i), end="")
            j += 1
        except (TypeError, ValueError):
            continue
    print(" ")
    return j
