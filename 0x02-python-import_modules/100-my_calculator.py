#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    ops = [add, sub, mul, div]
    a, operator, b = int(sys.argv[1]), sys.argv[2], int(sys.argv[3])
    if operator == '+':
        i = 0
    elif operator == '-':
        i = 1
    elif operator == '*':
        i = 2
    elif operator == '/':
        i = 3
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{:d} {:s} {:d} = {:d}".format(a, operator, b, ops[i](a, b)))
