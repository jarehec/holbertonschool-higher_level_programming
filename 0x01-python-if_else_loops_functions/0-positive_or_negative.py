#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    str = "positive"
elif number < 0:
    str = "negative"
elif number == 0:
    str = "zero"
print("{:d} is {:s}".format(number, str))
