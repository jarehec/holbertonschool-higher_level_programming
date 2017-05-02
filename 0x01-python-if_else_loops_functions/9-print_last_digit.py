#!/usr/bin/python3
def print_last_digit(number):
    i = number
    if number < 0:
        i = number * -1
    print(i % 10, end='')
    return (i % 10)
