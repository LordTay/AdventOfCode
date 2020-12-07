#Solution Part1 of Day1

# Time:
# 0.25ms

import time

target = 2020

file_path = "./input1"
l = []
s = set()

t1 = time.time()
with open(file_path,"r") as f:
    for i in f:
        s.add(int(i))
        l.append(int(i))

for i in l:
    if (target-i) in s:
        print("a = ",i,", b = ",(target-i))
        print("solution = ", i*(target-i))
        break

t2 = time.time()
print("time =", t2 - t1)

'''Output:
a =  75 , b =  1945
solution =  145875
'''