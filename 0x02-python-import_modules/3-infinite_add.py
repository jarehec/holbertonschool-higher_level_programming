#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    ac = len(sys.argv) - 1
    i = 0
    for av in range(1, ac + 1):
        i = int(sys.argv[av]) + i
    print(i)
