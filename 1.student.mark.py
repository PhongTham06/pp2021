def get_number_student():
    number_student = int(input("Enter the number of students: "))
    return number_student

def get_info_student(number_student):
    student_name = []
    student_ID = []
    student_DoB = []
    for i in range (number_student):
        name = input(f"Enter the name of student {i+1}: ")
        student_name += [name]
        ID = input(f"Enter the ID of student {i+1}: ")
        student_ID += [ID]
        DoB = input(f"Enter the DoB of student {i+1}: ")
        student_DoB += [DoB]
    return student_name, student_ID, student_DoB

def print_info_student(student_name, student_ID, student_DoB):
    for i in range(len(student_name)):
        print(f"Student {i+1}. Name:{student_name[i]}. ID: {student_ID[i]}. DoB:{student_DoB[i]}")

def get_number_course():
    number_course = int(input("Enter the number of courses: "))
    return number_course

def get_info_course(number_course):
    course_name = []
    course_ID = []
    for i in range (number_course):
        name = input(f"Enter the name of course {i+1}: ")
        course_name += [name]
        ID = input(f"Enter the ID of course {i+1}: ")
        course_ID += [ID]
    return course_name, course_ID

def print_info_course(course_name, course_ID):
    for i in range(len(course_name)):
        print(f"Course {i+1}. Name:{course_name[i]}. ID: {course_ID[i]}")

def select_course(course_name):
    for i in range (len(course_name)):
        print(f"{i}, {course_name[i]}")
    no_course = int(input("Enter the number of the subject: "))
    return no_course

def create_mark_sheet(number_course, number_student):
    mark_sheet = [[0 for i in range(number_student)] for j in range(number_course)]
    return mark_sheet

def marking_course(course_name, student_name, mark_sheet):
    no_course = select_course(course_name)
    for i in range(len(mark_sheet[no_course])):
        mark = float(input(f"Enter the mark for student {i+1}, {student_name[i]}: "))
        mark_sheet[no_course][i] = mark

def print_mark(course_name, student_name, mark_sheet):
    no_course = select_course(course_name)
    print(f"Mark for the course {course_name[no_course]}")
    for i in range (len(mark_sheet[no_course])):
        print(f"Student {student_name[i]}: {mark_sheet[no_course][i]}")

number_student = get_number_student()
student_name, student_ID, student_DoB = get_info_student(number_student)
number_course = get_number_course()
course_name, course_ID = get_info_course(number_course)
mark_sheet = create_mark_sheet(number_course, number_student)
while True:
    a = int(input("What do you want to do ? Press 1 to list info student. Press 2 to list info course. Press 3 to marking. Press 4 to list mark. Press 0 to stop."))
    if a == 1:
        print_info_student(student_name, student_ID, student_DoB)
    elif a == 2:
        print_info_course(course_name, course_ID)
    elif a == 3:
        marking_course(course_name, student_name, mark_sheet)
    elif a == 4:
        print_mark(course_name, student_name, mark_sheet)
    else :
        break