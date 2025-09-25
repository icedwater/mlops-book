#! /usr/bin/env python

"""
Example for pass - skips multiples of 3
"""

num = 10

while num <= 100:
    if (num % 3 == 0):
        pass
    else:
        print(num)
    num = num + 10
