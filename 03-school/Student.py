

class Student:
    def __init__(self, sid, lname, fname):
        self.id = sid
        self.fname = fname
        self.lname = lname
        self.courses = []

    def __str__(self):
        return self.id + ". " + self.fname + " " + self.lname

    def enrol(self, course):
        self.courses.append(course)