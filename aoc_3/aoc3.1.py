import numpy as np

#Open file, read lines and strip from line changes
with open("input.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

i = 0
#Why the fuck wont this work?
#For each character in string, while loop
while i < 12:
    #Reset current iterations most common value
    c = 0
    #For each line, count binary occurrences based on index
    for e in lines:
        if int(e[i]) == 1:
            c += 1
        elif int(e[i]) == 0:
            c -= 1
    #Positive = 1, negative = 0
    if c > 0:
        c = 1
    else:
        c = 0
    #Loop through lines again and if corresponding character at index isn't equal to most common value, remove it.
    for e in lines:
        if int(e[i]) != c:
            print(e[i])
            lines.remove(e)  

    i += 1

print(lines)
