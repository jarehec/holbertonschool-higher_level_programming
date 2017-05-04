#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    ac = len(sys.argv) - 1
    s = "argument"
    if ac < 1:
        s += '.'
    elif ac == 1:
        s += ':'
    elif ac > 1:
            s += 's:'
    print("{:d} {:s}".format(ac, s))
    for av in range(1, ac + 1):
        print("{:d}: {:s}".format(av, sys.argv[av]))
