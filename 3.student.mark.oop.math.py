import curses
import math
import numpy as np


class Student:
    def __init__(self):
        self.__name = ""
        self.__ID = ""
        self.__DoB = ""
        self.__gpa = -1

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__ID

    def get_dob(self):
        return self.__DoB

    def get_gpa(self):
        return self.__gpa

    def set_gpa(self, g):
        self.__gpa = g

    def input(self):
        screen.addstr("Enter name: ")
        self.__name = screen.getstr()
        screen.addstr("Enter ID: ")
        self.__ID = screen.getstr()
        screen.addstr("Enter DoB: ")
        self.__DoB = screen.getstr()
        screen.refresh()
        curses.napms(3000)
        screen.clear()
        screen.refresh()

    def __str__(self):
        return f"Student name: {self.get_name()} Student ID: {self.get_id()} Student DoB: {self.get_dob()} "

    def describe(self):
        screen.addstr(self.__str__())
        screen.refresh()
        curses.napms(2000)
        screen.clear()
        screen.refresh()


class Course:
    def __init__(self):
        self.__name = ""
        self.__ID = ""
        self.__credit = 0

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__ID

    def get_credit(self):
        return self.__credit

    def input(self):
        screen.addstr("Enter name: ")
        self.__name = screen.getstr()
        screen.addstr("Enter ID: ")
        self.__ID = screen.getstr()
        screen.addstr("Enter number of credit: ")
        self.__credit = int(screen.getstr().decode())
        screen.refresh()
        curses.napms(3000)
        screen.clear()
        screen.refresh()

    def __str__(self):
        return f"Course name: {self.get_name()} Course ID: {self.get_id()} "

    def describe(self):
        screen.addstr(self.__str__())


class Mark:
    def __init__(self, student, course, mark=-1):
        self.__student = student
        self.__course = course
        self.__mark = mark

    def get_student(self):
        return self.__student

    def get_course(self):
        return self.__course

    def get_mark(self):
        return self.__mark

    def marking(self):
        screen.addstr(f"Enter mark for student {self.__student.get_name()} "
                      f"in course {self.__course.get_name()}: ")
        raw_mark = int(screen.getstr().decode())
        self.__mark = round_down(raw_mark)
        screen.refresh()
        curses.napms(1000)
        screen.clear()
        screen.refresh()

    def __str__(self):
        return f"Mark for student {self.__student.get_name()} " \
               f"in course {self.__course.get_name()} is {self.__mark}"

    def describe(self):
        screen.addstr(self.__str__())


def round_down(point):
    return math.floor(point*10)/10


screen = curses.initscr()
# curses.noecho()
# curses.cbreak()
curses.start_color()

screen.addstr("Enter the number of student: ")
screen.refresh()
number_student = int(screen.getstr().decode())
students = []
screen.refresh()
curses.napms(3000)
screen.clear()
screen.refresh()

for i in range(number_student):
    std = Student()
    std.input()
    students += [std]

screen.addstr("Enter the number of courses: ")
screen.refresh()
number_course = int(screen.getstr().decode())
courses = []
screen.refresh()
curses.napms(3000)
screen.clear()
screen.refresh()

for i in range(number_course):
    cou = Course()
    cou.input()
    courses += [cou]

marks = [[Mark(students[i], courses[j]) for i in range(number_student)] for j in range(number_course)]


def check_marked(marks):
    # check that all mark is filled
    for i in range(len(marks)):
        for j in range(len(marks[0])):
            if marks[i][j].get_mark == -1:
                return -1


def calculate_gpa(marks, students, courses):
    # calculate the gpa for all student
    if (check_marked(marks)) == -1:
        screen.addstr("There is a student/courses haven't marked", curses.A_BOLD)
        screen.refresh()
        curses.napms(2000)
        screen.clear()
        screen.refresh()
        return -1
    for i in range(len(students)):
        total_mark = 0
        total_credit = 0
        for j in range(len(courses)):
            total_mark += marks[i][j].get_mark*courses[j].get_credit
            total_credit += courses[j].get_credit
        rounded_gpa = round_down((total_mark/total_credit))
        students[i].set_credit(rounded_gpa)


def sorted_student(students):
    gpas = np.array([])
    for i in range(len(students)):
        gpas += [students[i].get_gpa]
    sorted_gpa = np.argsort(gpas)
    return sorted_gpa


def print_sorted_student(students):
    sorted_gpa = sorted_student(students)
    for i in range (len(students)):
        screen.addstr(f"{i+1}, {students[sorted_gpa[-i]].get_name}: {students[sorted_gpa[-i]].get_gpa}")
    screen.refresh()
    curses.napms(5000)
    screen.clear()
    screen.refresh()

while True:
    screen.addstr(
        "What do you want to do ? Press 1 to print info student.\n "
        "Press 2 to print info course.\n "
        "Press 3 for marking.\n "
        "Press 4 to list mark.\n"
        "press 5 to print gpa (make sure that you mark all the student in every courses)\n"
        "Press 0 to exit\n")
    screen.refresh()
    a = int(screen.getstr().decode())
    if a == 1:
        for s in students:
            s.describe()
        screen.refresh()
        curses.napms(5000)
        screen.clear()
        screen.refresh()
    elif a == 2:
        for c in courses:
            c.describe()
        screen.refresh()
        curses.napms(5000)
        screen.clear()
        screen.refresh()
    elif a == 3:
        for i in range(len(courses)):
            print(f"{i}, {courses[i].get_name()}")
        screen.addstr("Enter the order number of the chosen course:")
        screen.refresh()
        num = int(screen.getstr().decode())
        for i in range(len(students)):
            marks[i][num].marking()
        screen.refresh()
        curses.napms(5000)
        screen.clear()
        screen.refresh()
    elif a == 4:
        for i in range(len(courses)):
            print(f"{i}, {courses[i].get_name()}")
        screen.addstr("Enter the order number of the chosen course:")
        screen.refresh()
        num = int(screen.getstr().decode())
        for i in range(len(students)):
            marks[i][num].describe()
        screen.refresh()
        curses.napms(5000)
        screen.clear()
        screen.refresh()
    elif a == 5:
        calculate_gpa(marks, students, courses)
        print_sorted_student(students)
    else:
        break
