#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    ac = len(sys.argv) - 1
    s = "argument"
    if ac < 1:
        print("{:d} {:s}.".format(ac, s))
    else:
        if ac > 2:
            s += 's'
        print("{:d} {:s}:".format(ac, s))
    for av in range(1, ac + 1):
        print("{:d}: {:s}".format(av, sys.argv[av]))