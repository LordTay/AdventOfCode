#Solution of Day6
import time as t

file_path = "./input1"

t1 = t.time()

with open(file_path,"r") as f:
    groups = [group.replace("\n","") for group in f.read().split("\n\n")]
    
l=[]
for group in groups:
        l.append(set([c for c in group]))

print(sum(len(group) for group in l))

print("time =",t.time() - t1)  