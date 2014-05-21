#!/usr/bin/env python3.4
import unittest
from studentmanager import StudentManager
from student import Student

class TestSpec(unittest.TestCase):
    def setUp(self):
        self.m = StudentManager()

    def testStudentManagerGetStudents(self):
        self.assertTrue(
            hasattr(self.m, "getStudents")
        )

    def test_studentManager_getStudents_returns_empty_default(self):
        students = self.m.getStudents()
        self.assertListEqual([], students)

    def test_addStudent_require_Student_instance(self):
        student = Student()
        self.m.addStudent(student)
        self.assertEquals(self.m.getStudents(), [student])
        with self.assertRaises(ValueError):
            self.m.addStudent('not an instance')