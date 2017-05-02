#!/usr/bin/python3
for i in range(9):
        first = i
        while first < 10:
            if i == first:
                first += 1
                continue
            if i < 8:
                print("{:d}{:d}, ".format(i, first), end='')
            else:
                print("{:d}{:d}".format(i, first))
            first += 1
