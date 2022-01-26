#Open file, read lines and strip from line changes
with open("input.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
#Variables for depth and horizontal position
depth = 0
horizontal = 0

for i in lines:
    #Get direction and its value from string
    direction = i.split(' ',1)[0]
    value = int(i.split(' ',1)[1])

    print(depth, horizontal)

    #Ifs and elifs define what gets done based on string before space
    if direction == "forward":
        horizontal += value
    elif direction == "up":
        depth -= value
    elif direction == "down":
        depth += value

print(f"Final position: {horizontal*depth}")   