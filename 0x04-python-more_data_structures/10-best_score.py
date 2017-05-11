#!/usr/bin/python3
def best_score(my_dict):
    if my_dict is not None and len(my_dict) > 0:
        big = 0
        for key, val in my_dict.items():
            if val >= big:
                big = val
                b_val = key
        return b_val
