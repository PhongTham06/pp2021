from Output import *
from domains.Mark import *

screen = curses.initscr()
curses.start_color()

students = get_info_student(screen)
courses = get_info_course(screen)
marks = create_mark(students, courses)

while True:
    screen.addstr(
        "What do you want to do ? Press 1 to print info student.\n "
        "Press 2 to print info course.\n "
        "Press 3 for marking.\n "
        "Press 4 to list mark.\n"
        "press 5 to print gpa (make sure that you mark all the student in every courses)\n"
        "Press 0 to exit")
    a = int(screen.getstr().decode())
    if a == 1:
        print_students(students, screen)
    elif a == 2:
        print_courses(courses, screen)
    elif a == 3:
        marking_student(students, courses, marks, screen)
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
    	calculate_gpa(marks, students, curses)
    	print_sorted_student(students, screen)
    else:
        break
