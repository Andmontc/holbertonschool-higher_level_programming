#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    x = len(sys.argv) - 1
    if x != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = sys.argv[1]
        b = sys.argv[3]
        if sys.argv[2] == '+':
            print("{} + {} = {}".format(a, b, add(int(a), int(b))))
        elif sys.argv[2] == '-':
            print("{} - {} = {}".format(a, b, sub(int(a), int(b))))
        elif sys.argv[2] == '*':
            print("{} * {} = {}".format(a, b, mul(int(a), int(b))))
        elif sys.argv[2] == '/':
            print("{} / {} = {}".format(a, b, div(int(a), int(b))))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        sys.exit(0)
