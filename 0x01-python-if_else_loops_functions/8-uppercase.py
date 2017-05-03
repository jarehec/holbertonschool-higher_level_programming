#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) > 96:
            print("{:s}".format(chr(ord(c) - 32)), end='')
        else:
            print("{:s}".format(chr(ord(c))), end='')
    print("")
