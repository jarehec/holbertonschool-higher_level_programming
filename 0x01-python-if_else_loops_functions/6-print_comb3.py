#!/usr/bin/python3
for i in range(9):
        first = i
        while first < 9:
            if i == first:
                first += 1
                continue
            print("{:d}{:d}, ".format(i, first), end='')
            first += 1
print("89")
