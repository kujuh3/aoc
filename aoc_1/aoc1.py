with open("input.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

z = 0

for i, x in enumerate(lines):
    if i == 0:
        pass
    else:
        pre = int(lines[i-1])
        if(int(x) > pre):
            z+=1

print(f"Total number of increases: {z}")