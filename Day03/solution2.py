#Solution of Day3

file_path = "./input2"

l = []
count = [0,0,0,0,0]
x = 0

with open(file_path,"r") as f:
    for i in f:
        l.append(i[:-1])

n =  len(l[0])-1
xstep = [1,3,5,7,1]
ystep = [1,1,1,1,2]

for j in range(0,len(xstep)):
    x = 0
    for i in range(0,len(l),ystep[j]):
        err = i
        if l[i][x] == "#":
            count[j] += 1
        x = (x + xstep[j]) % n

print(count)

result=1
for m in count:
    result *= m

print(result)