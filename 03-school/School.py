import csv
from Course import Course


class School:
    def __init__(self):
        self.courses = []
        self.students = []

    def load_courses(self):
        with open('courses.csv') as file:
            reader = csv.DictReader(file, delimiter=',')
            for row in reader:
                course = Course(row['SIS ID'], row['Section Name'])
                self.courses.append(course)

    def load_students(self):
        pass

    def load_enrollments(self):
        # read the enrolments file
        # for each row get the student's id
        # find the student
        # get the course's id
        # find the course
        # enrol the student to the course
        pass

    def print_student(self):
        # ask user for a student's id
        # print student's name
        # print student's courses
        pass

    def print_course(self):
        # ask user for a course's id
        # print course's title
        # print course's students
        pass

    def print_courses(self):
        for course in self.courses:
            print(course)


if __name__ == '__main__':
    school = School()
    school.load_courses()
    school.print_courses()

