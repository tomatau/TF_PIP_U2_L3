#!/usr/bin/env python3.4
import unittest
from student import Student

class TestSpec(unittest.TestCase):
    def setUp(self):
        self.m = Student()

    def testAddStudentShouldRequireStudents(self):
        student = Student()
        self.m.addStudent(student)
        self.assertEquals(self.m.getStudents(), [student])
        with self.assertRaises(ValueError):
            self.m.addStudent('not an instance')
