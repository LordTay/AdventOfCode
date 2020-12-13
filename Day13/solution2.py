#Solution of Day13
import time

s=set()

def readInput():
    
    with open("input1","r") as f:
        f.readline()
        return [n for n in f.read().split(",")]


t1 = time.time()
l = readInput()
busses=[]
for i in range(len(l)):
    if l[i]!="x": busses.append((l[i],i))


print(busses)
