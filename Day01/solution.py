#Solution of Day1

target = 2020

file_path = "./input1"

l = []
s = set()
with open(file_path,"r") as f:
    for i in f:
        s.add(int(i))
        l.append(int(i))

for i in l:
    if (target-i) in s:
        print("a = ",i,", b = ",(target-i))
        print("solution = ", i*(target-i))
        break