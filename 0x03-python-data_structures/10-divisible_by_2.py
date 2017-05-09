#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    stat = []
    for i in my_list:
        if i % 2 == 0:
            stat.append(True)
        elif i % 2 != 0:
            stat.append(False)
    return stat
