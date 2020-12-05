#Solution of Day5

import time as t
import builtins

def parsebp(boardpass):
    parsed_bp = boardpass.translate(t_dict)
    return int(parsed_bp[:7], 2) * 8 + int(parsed_bp[7:], 2)

def findMissing(seats):
    missingseats = set(range(0,max(seats))) - set(seats)
    return [seat for seat in range(0,max(seats)) if seat in missingseats 
                                                and seat+1 not in missingseats
                                                and seat-1 not in missingseats]

file_path = "./input1"
         
t_dict = str.maketrans("FBLR","0101")

t1 = t.time()

seats=[]
count = 0

with open(file_path,"r") as f:
    boardpass_all = f.read().split("\n")

for boardpass in boardpass_all:
    seats.append(parsebp(boardpass))

max_seatID = max(seats)
print(findMissing(seats))

print("time =",t.time() - t1)