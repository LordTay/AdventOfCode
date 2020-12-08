#Solution Part1 of Day8

# Time:

import time
import copy

file_path = "./input1"

class State:
    def __init__(self, ip, acc, visited):
        self.ip = ip
        self.acc = acc
        self.visited = visited

#setup
with open(file_path,"r") as f:
    instructions = f.read().split("\n")

currState = State(0,0,[0] * len(instructions))
nextState = State(0,0,0)


acc = 0;
t1 = time.time()
ip = 0

#setup
with open(file_path,"r") as f:
    instructions = f.read().split("\n")

visited = [0] * len(instructions)

def flipInst(ip):
    global instructions
    if "nop" in instructions[ip]: 
        instructions[ip] = instructions[ip].replace("nop","jmp")
    else :
        instructions[ip] = instructions[ip].replace("jmp","nop")

def runInstr(rawinst):
    global currState, nextState
    inst = rawinst.split(" ")
    
    currState.ip, currState.acc= nextState.ip, nextState.acc
    currState.visited[currState.ip] = 1
    if inst[0] == "acc": 
        nextState.acc += int(inst[1])
        
    elif inst[0] == "jmp": 
        nextState.ip += int(inst[1])-1

def savePrevState():
    global currState, nextState, prevCurrState, prevNextState
    prevCurrState = State(currState.ip,currState.acc,copy.deepcopy(currState.visited))
    prevNextState = State(nextState.ip,nextState.acc,0)

def resetToPrev():
    global currState, nextState, prevCurrState, prevNextState
    currState.ip, currState.acc = prevCurrState.ip, prevCurrState.acc
    currState.visited = copy.deepcopy(prevCurrState.visited)
    nextState.ip, nextState.acc = prevNextState.ip, prevNextState.acc

trial = False
while nextState.ip < len(instructions):
    #run instructions till jmp or nop
    #save state at jmp or nop, flip the jmp or nop and continue until collision.
    #on collision reset state to saved state, flip jmp or nop and repeat
    
    while not currState.visited[nextState.ip]:
        if "acc" not in instructions[nextState.ip] and not trial:
            savePrevState()
            flipInst(nextState.ip)
            trial = True
        
        currState.ip = nextState.ip
        runInstr(instructions[currState.ip])
        nextState.ip += 1

        if currState.ip < 0:
            print("This shouldnt happen")
            exit()
        if nextState.ip >= len(instructions):
            print("Solution: ","acc =",currState.acc,", ip =", currState.ip)
            t2 = time.time()
            print("time: ", t2 - t1)
            exit()
        
    #collision
    if currState.visited[nextState.ip]:

        resetToPrev()
        flipInst(nextState.ip)

        currState.ip = nextState.ip
        runInstr(instructions[currState.ip])
        nextState.ip += 1 
        trial = False
        #break;

#scheis auf des kackbeispiel