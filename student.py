#!/usr/bin/env python3.4
from course import Course

class Student(object):
    """Student to be managed"""
    def __init__(self):
        self._courses = []

    def addCourse(self, course):
        if not isinstance(course, Course):
            raise ValueError('addCourse requires Course instance') 
        self._courses.append(course)

    def getCourses(self):
        return self._courses

#   add course to student
#       set a session time and recurring dates 
#   add project to student
#   add notes to student