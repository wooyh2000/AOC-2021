file = open("command.txt", "r")
command = []
for line in file:
    commando = line.strip()
    command.append(commando)
horizontal = 0
depth = 0
for i in range(len(command)):
    command_number = [int(i) for i in command[i].split() if i.isdigit()]
    strings = [str(integer) for integer in command_number]
    a_string = "".join(strings)
    an_integer = int(a_string)
    if "forward" in command[i]:
        horizontal += an_integer
    elif "down" in command[i]:
        depth += an_integer
    elif "up" in command[i]:
        depth -= an_integer

total = depth * horizontal
print(total)
