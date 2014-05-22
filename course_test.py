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

    def test_addLesson_requires_Lesson_instance(self):
        lesson = Lesson()
        self.c.addLesson(lesson)
        self.assertEquals([lesson], self.c.getLessons())
        with self.assertRaises(ValueError):
            self.c.addLesson('not an instance')