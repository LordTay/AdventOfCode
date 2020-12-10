#Solution Part1 of Day10
import time

file_path = "./input1"

t1 = time.time()
with open(file_path,"r") as f:
    numbers = [int(n) for n in f.read().split("\n")]

numbers.sort()
count={1:0,2:0,3:0}

print(numbers)
for i in range(1,len(numbers)):
    count[numbers[i]-numbers[i-1]]+=1

print((count[1]+1)*(count[3]+1))

t2=time.time()

print("time",t2 - t1)