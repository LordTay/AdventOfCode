#Solution of Day13
import time

s=set()

def readInput():
    
    with open("input1","r") as f:
        dep = int(f.readline())
        return dep, [int(n) for n in f.read().replace(",x","").split(",")]


t1 = time.time()
departure, l = readInput()
 



for d in l:
    print(d,departure/d,(departure)%d,d-(departure)%d)
t2= time.time()

print(l)



for i in range(departure-3,departure+20):
    print(i,":",end="")

    for d in l:
        if i%d == 0 :print(" D   ",end="")
        else :print(" .   ",end="")
    if(i==departure):print('\033[1m'+"moin"+'\033[0m',end="")
    print("")
print("Time:",t2-t1)
