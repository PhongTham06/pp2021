from domains.Student import *
from domains.Course import *
from domains.Mark import *


def get_number_student(screen):
    screen.addstr("Enter the number of student: ")
    screen.refresh()
    number_student = int(screen.getstr().decode())
    screen.refresh()
    curses.napms(3000)
    screen.clear()
    screen.refresh()
    return number_student


def get_info_student(screen):
    number_student = get_number_student(screen)
    students = []
    for i in range(number_student):
        std = Student()
        std.input(screen)
        students += [std]
    return students


def get_number_courses(screen):
    screen.addstr("Enter the number of courses: ")
    screen.refresh()
    number_course = int(screen.getstr().decode())
    screen.refresh()
    curses.napms(3000)
    screen.clear()
    screen.refresh()
    return number_course


def get_info_course(screen):
    number_course = get_number_courses(screen)
    courses = []
    for i in range(number_course):
        cou = Course()
        cou.input(screen)
        courses += [cou]
        return courses


def create_mark(students, courses):
    marks = [[Mark(students[i], courses[j]) for i in range(len(students))] for j in range(len(courses))]
    return marks
