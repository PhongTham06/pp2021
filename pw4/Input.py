screen.addstr("Enter the number of student: ")
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
