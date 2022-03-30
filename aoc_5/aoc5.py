import numpy as np

coordinates = []
#Introducing empty list, read from file, strip from line changes, arrows and
#set values into a list of lists. ['1x,1y','2x,2y']
with open("input.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    for i, y in enumerate(lines):
        coordinates.append([round(float(str(x).replace(",",".")),1) for x in y.split(' -> ')])

print(coordinates)

xmax = max(x for x in coordinates[0])
ymax = max([sublist[1] for sublist in coordinates])
print(f'Max X value: {xmax}  Max Y value: {ymax}')

x = np.linspace(1,xmax)
y = np.linspace(1, ymax)
xmax, ymax = np.meshgrid(x,y)

print(xmax,ymax)

board = []
