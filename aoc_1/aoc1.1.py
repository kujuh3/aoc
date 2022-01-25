with open("input.txt") as file:
    lines = file.readlines()
    lines = [int(line.rstrip()) for line in lines]


z = 0
n = 0
i = 0

def window(list, x):
    for i in range(len(lines)-x+1):
        yield lines[i:i+x]

for s in window(lines, 3):
    i+=1
    #Ignore first iteration
    if i >= 2:
        if sum(s) > z:
            n+=1
        z = sum(s)

print(f"Total number of increases: {n}")