#!/usr/bin/python3
import sys
if __name__ == "__main__":
    x = len(sys.argv)
    if(x == 0 or x == 1):
        print("0 arguments.")
    elif x == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(x - 1))
    for args in range(x - 1):
        print("{}: {}".format(args + 1, sys.argv[args + 1]))
