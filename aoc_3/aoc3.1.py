import numpy as np

#Open file, read lines and strip from line changes
with open("input.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

i = 0
#Why the fuck wont this work?
while i < 12:
    c = 0
    for e in lines:
        if int(e[i]) == 1:
            c += 1
        elif int(e[i]) == 0:
            c -= 1
    if c > 0:
        c = 1
    else:
        c = 0

    for e in lines:
        if int(e[i]) != c:
            print(e[i])
            lines.remove(e)  

    i += 1

print(lines)