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

    if inst[0] == "acc": nextState.acc += int(inst[1])
    elif inst[0] == "jmp": nextState.ip += int(inst[1])-1

def savePrevState():
    global currState, nextState, prevState
    prevState = State(nextState.ip,nextState.acc,copy.deepcopy(currState.visited))
    print("saving state:","acc =",currState.acc,", ip =", currState.ip)

def resetToPrev():
    global currState, nextState, prevState
    currState.ip, currState.acc = prevState.ip, prevState.acc
    currState.visited = copy.deepcopy(prevState.visited)
    nextState.ip, nextState.acc = currState.ip, currState.acc

trial = False
trialcount = 0
while nextState.ip < len(instructions):
    #run instructions till jmp or nop
    #save state at jmp or nop, flip the jmp or nop and continue until collision.
    #on collision reset state to saved state, flip jmp or nop and repeat
    while not currState.visited[nextState.ip]:

        if "acc" not in instructions[nextState.ip] and not trial:
            
            if ("nop" in instructions[nextState.ip] and 
            0 < int(instructions[nextState.ip].split(" ")[1])+nextState.ip < len(instructions)):
                trialcount+=1
                print("trial,",trialcount)
                savePrevState()
                flipInst(nextState.ip)
                trial = True


        #print("acc =",currState.acc,", ip =", currState.ip)
        print("acc =",nextState.acc,", ip =", nextState.ip)
        print("visited:",currState.visited[nextState.ip])
        currState.ip = nextState.ip
        runInstr(instructions[currState.ip])
        nextState.ip += 1

        if nextState.ip >= len(instructions):
            print("Solution: ","acc =",currState.acc,", ip =", currState.ip)
            break

    if currState.visited[nextState.ip]:
        print("reset")
        print("acc =",nextState.acc,", ip =", nextState.ip)
        print("visited:",currState.visited[nextState.ip])
        
        resetToPrev()
        runInstr(instructions[currState.ip])
        nextState.ip += 1 
        trial = False
        #break;
       


        
print("Collision: acc =",currState.acc,", ip =", currState.ip)
print("Collision: nacc =",nextState.acc,", nip =", nextState.ip)


#collision at ip
savePrevState()
collision = True
collision_inst = instructions[collisionState.ip]


i = 0
while nextState.ip < len(instructions):
    instructions[collisionState.ip] = "nop"
    resetToCol()
    print(instructions[collisionState.ip])
    
    while nextState.ip < len(instructions) and not currState.visited[nextState.ip]:
        print("acc =",currState.acc,", ip =", currState.ip)
        currState.ip = nextState.ip
        runInstr(instructions[currState.ip])
        nextState.ip += 1 
    #print("acc =",currState.acc,", ip =", currState.ip)
    #print()
    i+=1
    if i > 500:
        break

