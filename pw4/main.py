import curses
import math
import numpy as np


screen = curses.initscr()
curses.noecho()
curses.cbreak()
curses.start_color()


while True:
    screen.addstr(
        "What do you want to do ? Press 1 to print info student. "
        "Press 2 to print info course. "
        "Press 3 for marking. "
        "Press 4 to list mark."
        "press 5 to print gpa (make sure that you mark all the student in every courses)"
        "Press 0 to exit")
    a = int(screen.getstr().decode())
    if a == 1:
        print_student(students)
    elif a == 2:
        print_courses(courses)
    elif a == 3:
        marking_student(students, courses)
    elif a == 4:
        for i in range(len(courses)):
            print(f"{i}, {courses[i].get_name()}")
        screen.addstr("Enter the order number of the chosen course:")
        num = int(screen.getstr().decode())
        for i in range(len(students)):
            marks[i][num].describe()
        screen.refresh()
        curses.napms(5000)
        screen.clear()
        screen.refresh()
    elif a == 5:
        print_sorted_student(students)
    else:
        break
