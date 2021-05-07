import curses


class Student:
    def __init__(self):
        self.__name = ""
        self.__ID = ""
        self.__DoB = ""
        self.__gpa = -1

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__ID

    def get_dob(self):
        return self.__DoB

    def get_gpa(self):
        return self.__gpa

    def set_gpa(self, g):
        self.__gpa = g

    def input(self, screen):
        screen.addstr("Enter name: ")
        self.__name = screen.getstr()
        screen.addstr("Enter ID: ")
        self.__ID = screen.getstr()
        screen.addstr("Enter DoB: ")
        self.__DoB = screen.getstr()
        screen.refresh()
        curses.napms(3000)
        screen.clear()
        screen.refresh()

    def __str__(self):
        return f"Student name: {self.get_name()} Student ID: {self.get_id()} Student DoB: {self.get_dob()} "

    def describe(self, screen):
        screen.addstr(self.__str__())
        screen.refresh()
        curses.napms(2000)
        screen.clear()
        screen.refresh()
