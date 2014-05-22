#!/usr/bin/env python3.4
import unittest
from lesson import Lesson

class TestSpec(unittest.TestCase):
    def setUp(self):
        self.l = Lesson()

    # def test_getLessons_returns_empty_default(self):
    #     lessons = self.l.getLessons()
    #     self.assertListEqual(lessons, [])

    # def test_addLesson_requires_Lesson_instance(self):
    #     lesson = Lesson()
    #     self.l.addLesson(lesson)
    #     self.assertEquals([lesson], self.l.getLessons())
    #     with self.assertRaises(ValueError):
    #         self.l.addLesson('not an instance')