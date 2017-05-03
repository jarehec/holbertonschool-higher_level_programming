#!/usr/bin/python3
alpha = 122
while alpha > 96:
    al = alpha
    if alpha % 2 != 0:
        al -= 32
    print("{:s}".format(chr(al)), end='')
    alpha -= 1
