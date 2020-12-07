#Solution Part1 of Day5

# Time:
# 1.5ms

import time

file_path = "./input1"
l=[]     
count = 0

def parsebp(boardpass):
    parsed_bp = boardpass.translate(t_dict)
    return int(parsed_bp[:7], 2) * 8 + int(parsed_bp[7:], 2)

t1 = time.time()
t_dict = str.maketrans("FBLR","0101")

with open(file_path,"r") as f:
    boardpass_all = f.read().split("\n")

for boardpass in boardpass_all:
    l.append(parsebp(boardpass))

print(max(l))

t2 = time.time()

print("time =",t2 - t1)

#prints: 874