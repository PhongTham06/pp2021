import os

while True:
    command = input("shell_test>>>")
    if command == "exit":
        break
    else:
        os.system(command)
