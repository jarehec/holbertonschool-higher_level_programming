#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_digit = (number % -10)
else:
    last_digit = (number % 10)
if last_digit > 5:
    str = "greater than 5"
elif last_digit == 0:
    str = "0"
elif last_digit < 6:
    str = "less than 6 and not 0"
print("Last digit of {:d} is {:d} and is {:s}".format(number, last_digit, str))
