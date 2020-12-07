#Solution Part1 of Day3

# Time:
# 0.3ms

import time

file_path = "./input1"

l = []
count = 0
x = 0

t1 = time.time()
with open(file_path,"r") as f:
    for i in f:
        l.append(i[:-1])
        x %= len(l[-1])
        if l[-1][x] == "#":
            count += 1 #check field x mod len(i)-1
        x += 3

t2 = time.time()
print("time =", t2 - t1)

print(count)

#prints: 250