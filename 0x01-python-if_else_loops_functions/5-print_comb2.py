#!/usr/bin/python3
for i in range(99):
#    if i < 10:
 #       print("0", end='')
    if i < 100:
        print("{:d}".format(i).zfill(2) + ", ", end='')
print("{:d}".format(99))
