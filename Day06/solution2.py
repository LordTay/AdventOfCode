#Solution Part2 of Day6

# Time:
# 2.5ms

import time

file_path = "./input1"

l=[]

t1 = time.time()
with open(file_path,"r") as f:
    groups = [group.split("\n") for group in f.read().split("\n\n")]

for group in groups:
    intersect = set(group[0]).intersection(*group)
    if intersect:
        l.append(intersect)

t2 = time.time()
print(sum(len(group) for group in l))

print("time =", t2 - t1)  

#prints 3427
