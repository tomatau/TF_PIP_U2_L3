#!/usr/bin/env python3.4
import unittest
from course import Course
from lesson import Lesson

class TestSpec(unittest.TestCase):
    def setUp(self):
        self.c = Course()

    def test_getLessons_returns_empty_default(self):
        lessons = self.c.getLessons()
        self.assertListEqual(lessons, [])

    # def test_addCourse_requires_Course_instance(self):
    #     course = Course()
    #     self.c.addCourse(course)
    #     self.assertEquals([course], self.c.getLessons())
    #     with self.assertRaises(ValueError):
    #         self.c.addCourse('not an instance')