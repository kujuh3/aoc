#Open file, read lines and strip from line changes
with open("input.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

#Initial variable for increases
z = 0

#For loop including element value and index
for i, x in enumerate(lines):
    #Ignore first iteration
    if i == 0:
        pass
    #Get preceding value, compare to current and increase counter
    else:
        pre = int(lines[i-1])
        if(int(x) > pre):
            z+=1

print(f"Total number of increases: {z}")