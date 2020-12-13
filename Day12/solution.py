#Solution Part1 of Day12

import time

file_path = "./input1"

DirParseDict = {"E": (1,0),"S": (0,-1),"W": (-1,0),"N": (0,1)}

class Ship:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.xway = 0
        self.yway = 0
        self.directions = ("E","S","W","N")
        self.direction = 0

    def turn(self,turn,value):
        if turn == "R": self.direction += int(value/90)
        elif turn == "L": self.direction -= int(value/90)
        else: print("Wat se fak?")
        self.direction %= 4

    def doInstr(self,instr):
        if instr[0] == "F":
            instr[0] = self.directions[self.direction] 
        if instr[0] in DirParseDict:
            self.x += DirParseDict[instr[0]][0]*int(instr[1]) 
            self.y += DirParseDict[instr[0]][1]*int(instr[1]) 
        elif instr[0] in "LR":
            self.turn(instr[0],int(instr[1]) )



t1 = time.time()
with open(file_path,"r") as f:
    instructions = [[n[0],n[1:]] for n in f.read().split("\n")]

ship = Ship()
for instr in instructions:
    print(instr)
    ship.doInstr(instr)
    print(ship.x,ship.y)
    print()