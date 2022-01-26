#Open file, read lines and strip from line changes
with open("input.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
#Variables for gamma and epsilon
gamma = ""
epsilon = ""
#Initial list for counting occurrences
counter = [0,0,0,0,0,0,0,0,0,0,0,0]

#Loop through lines
for i in lines:
    #Loop each binary, check value and adjust counter corresponding to index
    for x, z in enumerate(i):
        #Number stays positive for 1, negative for 0
        if int(z) == 1:
            counter[x] += 1
        else:
            counter[x] -= 1

#Gamma binary constructor
for i, y in enumerate(counter):
    if y > 0:
        gamma += "1"
    else:
        gamma += "0" 

#Epsilon binary constructor
for i, y in enumerate(counter):
    if y > 0:
        epsilon += "0"
    else:
        epsilon += "1" 

#Convert binaries to decimal and multiply
print(f"Power consumption is: {int(gamma, 2)*int(epsilon, 2)}")
