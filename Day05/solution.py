#Solution of Day5

import time as t
import builtins

def parsebp(boardpass):
    parsed_bp = boardpass.translate(t_dict)
    return int(parsed_bp[:7], 2) * 8 + int(parsed_bp[7:], 2)


file_path = "./input1"
         
t_dict = str.maketrans("FBLR","0101")

t1 = t.time()
   
l=[]
count = 0

with open(file_path,"r") as f:
    boardpass_all = f.read().split("\n")

for boardpass in boardpass_all:
    l.append(parsebp(boardpass))

print(max(l))

print("time =",t.time() - t1)  