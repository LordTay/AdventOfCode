#Solution Part1 of Day8

# Time:

import time


file_path = "./input1"
acc = 0;
t1 = time.time()
ip = 0

#setup
with open(file_path,"r") as f:
    instructions = f.read().split("\n")

visited = [0] * len(instructions)


def runInstr(rawinst):
    global ip,acc,visited
    inst = rawinst.split(" ")
    visited[ip] = 1
    if inst[0] == "acc": acc += int(inst[1])
    elif inst[0] == "jmp": ip += int(inst[1])-1

while(not visited[ip]):
    runInstr(instructions[ip])
    ip += 1
print("acc =",acc,", ip =", ip)