#Solution of Day3
file_path = "./input1"

l = []
count = 0
x = 0
with open(file_path,"r") as f:
    for i in f:
        l.append(i[:-1])
        x %= len(l[-1])
        if l[-1][x] == "#":
            count += 1 #check field x mod len(i)-1
        x += 3

print(count)