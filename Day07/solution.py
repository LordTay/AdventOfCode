#Solution Part of Day7

# Time:
# checking everthing:
#   92ms
# only skiping bags if a previous bag is already a valid option:
#   20ms
# dynamic programming:
#   3.6ms

import time


file_path = "./input1"

rules={}
checkDictDP= {}

def checkDict(rule):
    if not rule:
        return False

    if "shinygoldbag" in rule:
        return True

    else: 
        for bag in rule.keys():
            if bag not in checkDictDP :
                checkDictDP[bag] = checkDict(rules[bag])
            if checkDictDP[bag]:
                return True
                
t1 = time.time()
#reading
with open(file_path,"r") as f:
    rules_input = f.read().replace("bags","bag").replace(" ","").replace(".","").split("\n")
#write in a dict of dicts
for r in rules_input:
    rule = r.split("contain")
    rules[rule[0]] = dict((bag[1:],int(bag[0])) for bag in rule[1].split(",") if bag[0] != "n" )

count = 0
for bag,value in rules.items():
    if checkDict(value): count+=1

t2 = time.time()

print(count)

print("time =", t2 - t1)  

#prints: 378