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
        screen.addstr(f"Enter mark for student {self.__student.get_name()} "
                      f"in course {self.__course.get_name()}: ")
        raw_mark = int(screen.getstr().decode())
        self.__mark = math.floor(raw_mark*10)/10
        screen.refresh()
        curses.napms(1000)
        screen.clear()
        screen.refresh()

    def __str__(self):
        return f"Mark for student {self.__student.get_name()} " \
               f"in course {self.__course.get_name()} is {self.__mark}"

    def describe(self):
        screen.addstr(self.__str__())
