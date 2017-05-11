#!/usr/bin/python3
def multiply_by_2(my_dict):
    new_dict = {}
    for key, val in my_dict.items():
        temp = {key: val * 2}
        new_dict.update(temp)
    return new_dict
