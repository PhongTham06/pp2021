import subprocess

while True:
    command = input("shell_test>>>")
    if command == "exit":
        break
    else:
        if ">" in command:
            # not finished
            pass
            command_check = command.split(">")
        elif "<" in command:
            # not finished
            pass
            command_check = command.split("<")
            
        elif "|" in command:
            # not finished
            pass
            command_check = command.split("|")
        else:
            command_check = command.split()
            if len(command_check) == 1:
                subprocess.run(command)
            elif len(command_check) == 2:
                subprocess.run([command_check[0], command_check[1]])
