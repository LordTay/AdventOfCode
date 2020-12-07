#Solution Part1 of Day6

# Time:
# 2.5ms

import time

file_path = "./input1"
    
l=[]

t1 = time.time()
with open(file_path,"r") as f:
    groups = [group.replace("\n","") for group in f.read().split("\n\n")]

for group in groups:
        l.append(set([c for c in group]))

print(sum(len(group) for group in l))

t2 = time.time()

print("time =", t2 - t1)

#prints 6532
