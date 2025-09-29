#! /usr/bin/env python

"""
Example class script
"""

class Multiply:
    def mul(self):
        """
        multiply two numbers and return the result
        :param num1: float, first operand
        :param num2: float, second operand
        :return result: float, result of multiplying the two
        """
        result = self.num1 * self.num2
        return result


    def __init__(self, num1: float, num2: float):
        """
        Initialise an instance of the class with values for num1 and num2.
        :param num1: float, to be used as first operand in mul
        :param num2: float, to be used as second operand in mul
        """
        self.num1 = num1
        self.num2 = num2

a = Multiply(3.5, 4.2)
print(f"{a.mul():.6}")
