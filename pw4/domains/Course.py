class Course:
    def __init__(self):
        self.__name = ""
        self.__ID = ""
        self.__credit = 0

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__ID

    def get_credit(self):
        return self.__credit

    def input(self):
        screen.addstr("Enter name: ")
        self.__name = screen.getstr()
        screen.addstr("Enter ID: ")
        self.__ID = screen.getstr()
        screen.addstr("Enter number of credit: ")
        self.__credit = int(screen.getstr().decode())
        screen.refresh()
        curses.napms(3000)
        screen.clear()
        screen.refresh()

    def __str__(self):
        return f"Course name: {self.get_name()} Course ID: {self.get_id()} "

    def describe(self):
        screen.addstr(self.__str__())
