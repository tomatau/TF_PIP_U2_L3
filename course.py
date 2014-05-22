#!/usr/bin/env python3.4
from lesson import Lesson

class Course(object):
    """Course to be managed"""
    def __init__(self):
        self._lessons = []

    def getLessons(self):
        return self._lessons

    def addLesson(self, lesson):
        if not isinstance(lesson, Lesson):
            raise ValueError('addLesson requires Lesson instance') 
        self._lessons.append(lesson)


#   add course to student
#       set a session time and recurring dates 
#   add project to student
#   add notes to student