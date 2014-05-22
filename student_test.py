#!/usr/bin/env python3.4
import unittest
from student import Student
from course import Course

class TestSpec(unittest.TestCase):
    def setUp(self):
        self.s = Student()

    def test_getCourses(self):
        self.assertTrue(
            hasattr(self.s, "getCourses")
        )

    def test_getCourses_returns_empty_default(self):
        courses = self.s.getCourses()
        self.assertListEqual([], courses)

    def test_addCourse_requires_Course_instance(self):
        course = Course()
        self.s.addCourse(course)
        self.assertEquals([course], self.s.getCourses())
    #     with self.assertRaises(ValueError):
    #         self.s.addStudent('not an instance')
