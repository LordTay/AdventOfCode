#Solution Part1 of Day11

import time
import copy

def readInput():
    with open("input1","r") as f:
        return [list(n) for n in f.read().split("\n")]

currSeats = readInput()
nextSeats = copy.deepcopy(currSeats)

def getAdjSeatsOccupied(seats,y,x):
    count = 0
    for r in [-1, 0, 1]:
        for c in [-1, 0, 1]:
            if r == c == 0: continue
            if 0 <= y+r < len(seats) and 0 <= x+c < len(seats[0]):
                if seats[y+r][x+c] == "#": count += 1

    return count

def getNextSeats(seats):
    changes = 0
    t1 = time.time()
    for row in range(len(seats)):
        for col in range(len(seats[0])):
            adjOccupied = getAdjSeatsOccupied(seats,row,col)
            if seats[row][col] == "L":
                if adjOccupied == 0:
                    nextSeats[row][col] = "#"
                    changes = True
                else: nextSeats[row][col] = "L" 
            elif seats[row][col] == "#":
                if adjOccupied >= 4:
                    nextSeats[row][col] = "L"
                    changes = True
                else: nextSeats[row][col] = "#" 
    print("time:",time.time()-t1)
    return changes


while getNextSeats(currSeats):
    nextSeats, currSeats = currSeats, nextSeats
        

count = 0
for s in currSeats:
    for c in s:
        if c == "#":
            count += 1

print (count)