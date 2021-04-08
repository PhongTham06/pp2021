class Student:
    def __init__(self):
        self.__name = ""
        self.__ID = ""
        self.__DoB = ""

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__ID

    def get_dob(self):
        return self.__DoB

    def input(self):
        self.__name = input(f"Enter name: ")
        self.__ID = input(f"Enter ID: ")
        self.__DoB = input(f"Enter DoB: ")

    def __str__(self):
        return f"Student name: {self.get_name()} Student ID: {self.get_id()} Student DoB: {self.get_dob()} "

    def describe(self):
        print(self.__str__())


class Course:
    def __init__(self):
        self.__name = ""
        self.__ID = ""

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__ID

    def input(self):
        self.__name = input(f"Enter name: ")
        self.__ID = input(f"Enter ID: ")

    def __str__(self):
        return f"Course name: {self.get_name()} Course ID: {self.get_id()} "

    def describe(self):
        print(self.__str__())


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
        self.__mark = int(input(f"Enter mark for student {self.__student.get_name()} "
                                f"in course {self.__course.get_name()}: "))

    def __str__(self):
        return f"Mark for student {self.__student.get_name()} " \
               f"in course {self.__course.get_name()} is {self.__mark}"

    def describe(self):
        print(self.__str__())


number_student = int(input("Enter the number of students: "))
students = []

for i in range(number_student):
    std = Student()
    std.input()
    students += [std]

number_course = int(input("Enter the number of courses: "))
courses = []

for i in range(number_course):
    cou = Course()
    cou.input()
    courses += [cou]

marks = [[Mark(students[i], courses[j]) for i in range(number_student)] for j in range(number_course)]

while True:
    a = int(input(
        "What do you want to do ? Press 1 to print info student. "
        "Press 2 to print info course. "
        "Press 3 for marking. "
        "Press 4 to list mark."
        "Press 0 to exit"))
    if a == 1:
        for s in students:
            s.describe()
    elif a == 2:
        for c in courses:
            c.describe()
    elif a == 3:
        for i in range(len(courses)):
            print(f"{i}, {courses[i].get_name()}")
        num = int(input("Enter the order number of the chosen course:"))
        for i in range(len(students)):
            marks[i][num].marking()
    elif a == 4:
        for i in range(len(courses)):
            print(f"{i}, {courses[i].get_name()}")
        num = int(input("Enter the order number of the chosen course:"))
        for i in range(len(students)):
            marks[i][num].describe()
    else:
        break
