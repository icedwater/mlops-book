#! /usr/bin/env python

"""
Demonstrate student data save/load using pickle.
"""

import pickle
from data import students

with open("students.data", "wb") as s_write:
    pickle.dump(students, s_write)

with open("students.data", "rb") as s_read:
    students_from_file = pickle.load(s_read)

print(students == students_from_file)
