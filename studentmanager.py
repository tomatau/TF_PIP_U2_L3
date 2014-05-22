#!/usr/bin/env python3.4
from student import Student

class StudentManager():
    """Manage mentor students"""
    def __init__(self):
        self.students = []

    def addStudent(self, student):
        if not isinstance(student, Student):
            raise ValueError('addStudent requires Student instance') 
        self.students.append(student)

    def getStudents(self):
        return self.students

# add student (should be a student)
#   add course to student
#       set a session time and recurring dates 
#   add project to student
#   add notes to student
#   
# get next session


'''
nextsession

calendar
    days
        sessions

invoiceGenerator

students
    student
        name *
        background
        expectations
        location
        preferred timezone
        notes
        courses
            course
                first session datetime *
                last session datetime *

            sessions *
                session *
                    start datetime *
                    end datetime *
                    notes

            projects *
                project *
                    name
                    revision
                        url
                        localPath
                        notes

'''