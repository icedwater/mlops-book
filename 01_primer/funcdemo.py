#! /usr/bin/env python

"""
Example code for functions.
Also a reminder that docstrings and type hints alone are not enough.
If type checking was strict, only the first one should be allowed.
"""

def add(a: int, b: int):
    """
    Take two arguments a and b and add them. Return the result.
    :param a:   int, first argument
    :param b:   int, second argument
    :return r:  int, sum of a and b
    """
    r = a + b
    return r

print(add(a=100, b=23))
print(add(a=1.4, b=.3))
print(add(a="hel", b="lo"))
    
