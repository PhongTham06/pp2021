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
    student_file = open("student.txt", "a")
    student_file.write("Student info:")
    for i in range(number_student):
        std = Student()
        std.input(screen)
        students += [std]
        student_file.write("Student info")
    student_file.close()
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
    course_file = open("course.txt", "a")
    course_file.write("Course info:")
    for i in range(number_course):
        cou = Course()
        cou.input(screen)
        courses += [cou]
        course_file.write("Student info")
    course_file.close()
    return courses


