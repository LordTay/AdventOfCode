#Solution Part2 of Day5

# Time:
# 1.5ms

import time

def parsebp(boardpass):
    parsed_bp = boardpass.translate(t_dict)
    return int(parsed_bp[:7], 2) * 8 + int(parsed_bp[7:], 2)

def findMissing(seats):
    missingseats = set(range(0,max(seats))) - set(seats)
    return [seat for seat in range(0,max(seats)) if seat in missingseats 
                                                and seat+1 not in missingseats
                                                and seat-1 not in missingseats]

file_path = "./input1"
seats=[]
count = 0

t1 = time.time()     
t_dict = str.maketrans("FBLR","0101")

with open(file_path,"r") as f:
    boardpass_all = f.read().split("\n")

for boardpass in boardpass_all:
    seats.append(parsebp(boardpass))

print(findMissing(seats)[0])

t2 = time.time()

print("time =",t2 - t1)

#prints: 594