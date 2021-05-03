import numpy as np
from Input import *


def print_students(students, screen):
    for s in students:
        s.describe()
    screen.refresh()
    curses.napms(5000)
    screen.clear()
    screen.refresh()


def print_courses(courses, screen):
    for c in courses:
        c.describe()
    screen.refresh()
    curses.napms(5000)
    screen.clear()
    screen.refresh()


def marking_student(students, courses, marks, screen):
    for i in range(len(courses)):
        print(f"{i}, {courses[i].get_name()}")
    screen.addstr("Enter the order number of the chosen course:")
    num = int(screen.getstr().decode())
    mark_file = open("mark.txt", "a")
    for i in range(len(students)):
        marks[i][num].marking()
        mark_file.write(f"{marks[i][num].__str__}")
    screen.refresh()
    curses.napms(5000)
    screen.clear()
    screen.refresh()
    

def check_marked(marks):
    # check that all mark is filled
    for i in range(len(marks)):
        for j in range(len(marks[0])):
            if marks[i][j].get_mark == -1:
                return -1


def calculate_gpa(marks, students, courses, screen):
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
            total_mark += marks[i][j].get_mark * courses[j].get_credit
            total_credit += courses[j].get_credit
        rounded_gpa = math.floor((total_mark / total_credit) * 10) / 10
        students[i].set_gpa(rounded_gpa)


def sorted_student(students):
    gpas = np.array([])
    for i in range(len(students)):
        gpas += [students[i].get_gpa]
    sorted_gpa = np.argsort(gpas)
    return sorted_gpa


def print_sorted_student(students, screen):
    sorted_gpa = sorted_student(students)
    for i in range(len(students)):
        screen.addstr(f"{i+1}, {students[sorted_gpa[-i]].get_name}: {students[sorted_gpa[-i]].get_gpa}")
    screen.refresh()
    curses.napms(5000)
    screen.clear()
    screen.refresh()
