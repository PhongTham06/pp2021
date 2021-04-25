from Output import *
from domains.Mark import *
import zipfile


file_name = "student.dat"
with zipfile.ZipFile(file_name, "r") as zip:
    zip.extractall()

screen = curses.initscr()
curses.noecho()
curses.cbreak()
curses.start_color()

students = get_info_student(screen)
courses = get_info_course(screen)
marks = create_mark(students, courses)


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
        print_sorted_student(students, screen)
    else:
        zip_file = zipfile.ZipFile("student.dat", "w", zipfile.ZIP_DEFLATED)
        zip_file.write("student.txt")
        zip_file.write("course.txt")
        zip_file.write("mark.txt")
        break
