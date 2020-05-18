#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    j = 0
    for i in my_list[:x]:
        try:
            j += 1
            print("{:d}".format(i), end="")
        except (TypeError, ValueError):
            pass
    print()
    return j
