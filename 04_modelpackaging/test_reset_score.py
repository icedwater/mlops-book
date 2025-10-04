#! /usr/bin/env python
"""
Example for pytest with above students
"""

import pytest

class Student:
    def __init__(self, name, score=0):
        self.name = name
        self.score = score

    def reset_score(self):
        self.score = 0

class Group:
    def __init__(self, *students):
        self.students = students
        self._reset_all_scores()

    def _reset_all_scores(self):
        for student in self.students:
            student.reset_score()

@pytest.fixture
def testgroup():
    return [Student(name="Amy", score=20), Student(name="Bob", score=25), Student(name="Cal", score=15)]

def test_reset_group(testgroup):
    example = Group(*testgroup)
    assert all(s.score == 0 for s in example.students)
