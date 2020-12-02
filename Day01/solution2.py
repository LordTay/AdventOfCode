#Solution of Day1

target = 2020

file_path = "./input1"

try:
    f = open(file_path,"r")
except Exception as e:
    print("Exception: ",e)

l = []
d = {}

for i in f:
    l.append(int(i))

for i in l:
    for j in l:
        d[i+j] = i,j
        
l.sort()

for i in l:
    if (target-i) in d:
        print("a = ",i,", b = ",d[(target-i)][0],", c = ",d[(target-i)][1])
        print("solution = ", i*d[(target-i)][0]*d[(target-i)][1])
        break;