#!/usr/bin/python3
import sys
if __name__ == "__main__":
    x = len(sys.argv)
    suma = 0
    for n in range(1, x):
        suma += int(sys.argv[n])
    print("{}".format(suma))
