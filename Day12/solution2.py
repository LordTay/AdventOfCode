#Solution Part2 of Day12

import time
import numpy as np

directionDict = {"E": np.array([[1],[0]]),"S": np.array([[0],[-1]]),"W": np.array([[-1],[0]]),"N": np.array([[0],[1]])}

rightRotation = np.matrix([[ 0, 1],
                          [ -1, 0]])

def readInput():
    with open("input1","r") as f:
        return [[n[0],n[1:]] for n in f.read().split("\n")]

class Ship:

    def __init__(self):
        self.shipPos = np.array([[0],[0]])
        self.wayPos = np.array([[10],[1]])

    def turn(self,turn,value):
        if turn == "L": value = (-value+360)
        self.wayPos = np.linalg.matrix_power(rightRotation, int(value/90)) * self.wayPos

    def doInstr(self,instr,value):
        
        if instr == "F":
            self.shipPos +=  self.wayPos * value

        elif instr in directionDict:
            self.wayPos += directionDict[instr] * value

        elif instr in "LR":
            self.turn(instr,value) 

t1 = time.time()
instructions = readInput()

ship = Ship()
for instr in instructions:
    ship.doInstr(instr[0],int(instr[1]))

t2 = time.time()
print("Manhattan distance: ",sum(abs(ship.shipPos)))

print("time: ", t2 - t1)