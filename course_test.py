#!/usr/bin/env python3.4
import unittest
from course import Course
from lesson import Lesson

class TestSpec(unittest.TestCase):
    def setUp(self):
        self.s = Lesson()

    # def test_getLessons(self):
    #     self.assertTrue(
    #         hasattr(self.s, "getLessons")
    #     )

    # def test_addCourse_require_Course_instance(self):
    #     course = course()
    #     self.s.course(course)
    #     self.assertEquals(self.s.courses(), [course])
    #     with self.assertRaises(ValueError):
    #         self.s.course('not an instance')
