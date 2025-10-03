#! /usr/bin/env python

"""
Demonstrate student data save/load using joblib.
"""

import joblib
from data import students

joblib.dump(students, "stu_data")               # stores student data into a file called stu_data
students_from_file = joblib.load("stu_data")    # loads the contents of stu_data back into an object

print(students == students_from_file)
