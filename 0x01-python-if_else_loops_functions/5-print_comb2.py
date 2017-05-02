#!/usr/bin/python3
for i in range(99):
    if i < 10:
        print("0", end='')
    print("{:d}, ".format(i), end='')
print("{:d}".format(99))
