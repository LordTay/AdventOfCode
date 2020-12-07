#Solution Part2 of Day1

# Time:
# 0.25ms

import time

file_path = "./input1"
target = 2020

l = []
d = {}

t1 = time.time()
with open(file_path,"r") as f:
    for i in f:
        l.append(int(i))

for i in l:
    for j in l:
        d[i+j] = i,j

for i in l:
    if (target-i) in d:
        print("a = ",i,", b = ",d[(target-i)][0],", c = ",d[(target-i)][1])
        print("solution = ", i*d[(target-i)][0]*d[(target-i)][1])
        break;

t2 = time.time()
print("time =", t2 - t1)

'''Output:
a =  74 , b =  894 , c =  1052
solution =  69596112
'''