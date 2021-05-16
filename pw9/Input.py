from domains.Student import *
from domains.Course import *
from domains.Mark import *
import tkinter as tk


def get_number_student(window):
    frame = tk.Frame(window).pack()
    number_student = tk.IntVar()
    tk.Label(frame, text="Number of student").grid(column=0, row=0, sticky=tk.EW, padx=3, pady=3)
    tk.Entry(frame, textvariable = number_student).grid(column=0, row=1, sticky=tk.EW, padx=3, pady=3)
    tk.Button(frame, text="OK", command=frame.destroy)
    return number_student


def get_info_student(window):
    number_student = get_number_student(window)
    students = []
    student_file = open("student.txt", "a")
    student_file.write("Student info:")
    frame = tk.Frame(window).pack()
    for i in range(number_student):
        tk.Label(frame, text="Number of student").grid(column=0, row=0, sticky=tk.EW, padx=3, pady=3)
        tk.Entry(frame, textvariable=number_student).grid(column=0, row=1, sticky=tk.EW, padx=3, pady=3)
        tk.Label(frame, text="Number of student").grid(column=0, row=0, sticky=tk.EW, padx=3, pady=3)
        tk.Entry(frame, textvariable=number_student).grid(column=0, row=1, sticky=tk.EW, padx=3, pady=3)
        tk.Label(frame, text="Number of student").grid(column=0, row=0, sticky=tk.EW, padx=3, pady=3)
        tk.Entry(frame, textvariable=number_student).grid(column=0, row=1, sticky=tk.EW, padx=3, pady=3)
        tk.Button(frame, text="OK", command=frame.destroy)
    student_file.close()
    return students


def get_number_courses(window):
    frame = tk.Frame(window).pack()
    number_course = tk.IntVar()
    tk.Label(frame, text="Number of student").grid(column=0, row=0, sticky=tk.EW, padx=3, pady=3)
    tk.Entry(frame, textvariable=number_course).grid(column=0, row=1, sticky=tk.EW, padx=3, pady=3)
    tk.Button(frame, text="OK", command=frame.destroy)
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


