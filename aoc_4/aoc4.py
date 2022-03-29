#Non object-oriented approach, no numpy, just figuring out
from itertools import cycle, islice, chain

#Open file and read only first row to numbers
with open("input.txt") as file:
    numbers_str = file.readline()
    numbers = [int(x) for x in numbers_str.split(',')]

#Looks ugly but works
#Open file again, skip first line. Strip of line changes and weird empty characters
#Then loop through each object in list, separate values to new objects and once again filter weird empty strings. Result will be a list of lists containing each rows numbers.
with open("input.txt") as file:
    lines = file.readlines()[1:]
    boards = [line.strip('\n') for line in lines]
    boards = [line for line in boards if line]
    for i, y in enumerate(boards):
        boards[i] = y.split(' ')
        boards[i] = [int(x) for x in boards[i] if x != '']

# |---Wasn't a good idea, generators aint for this one--| 
# Constructing a sliding list of all boards, each cycle containing a 5x5 board
# def boardconstructor(board, size):
#    boardcycle = cycle(board)
#
#    while True:
#        yield list(islice(boardcycle, size))

def calculateamount(number, amount):
    return number*amount
#BEHOLD
def bingocheck(numbers1, boards):
    updatedboards = boards

    #For each number in call list we go through every list in list and each element in each list
    for index, i in enumerate(numbers1):
        #Inner and outer ranges for list slices and row coordinates as a list
        for outerindex, x in enumerate(boards):
            inner = 0
            outer = 5
            col = [0,5,10,15,20]
            counter = 0
            #For each iterated list we'll go through the 5x5 board row by row, column by column
            while counter < 5:
                checkrow = x[inner:outer]
                checkcolumn = x[col[0]],x[col[1]],x[col[2]],x[col[3]],x[col[4]]
                #If checks for column and row, get answer by calling function and return that value
                if all(l=="X" for l in checkcolumn):
                    amount = 0
                    print(f'Matched list:{x} Called number:{i}')
                    for j in x:
                        if j != "X":
                            amount+=j
                    #-1 from index since it's one ahead when the call ends
                    return calculateamount(numbers1[index-1], amount)
                if all(l=="X" for l in checkrow):
                    amount = 0
                    print(f'Matched list:\n{x} \nCalled number:{i}')
                    for j in x:
                        if j != "X":
                            amount+=j
                    return calculateamount(numbers1[index-1], amount)
                inner+=5
                outer+=5
                col = [x+1 for x in col]
                counter+=1
            #Simply go through each element and if match, change value to X
            for innerindex, y in enumerate(x):
                if y == "X":
                    pass
                elif y == i:
                    updatedboards[outerindex][innerindex] = "X"


#Longest list comprehension I've usen so far
#Use chain and islice to divide numbers of each board to a list of their own
boards = [list(chain.from_iterable(islice(boards,i,i+5))) for i in range(0,len(boards),5)]

Firstwinner = bingocheck(numbers, boards)

print(f'First winning board: {Firstwinner}')
