#Solution Part2 of Day7

# Time:
# 2.8ms

import time

file_path = "./input1"

rules={}

with open(file_path,"r") as f:
    rules_input = f.read().replace("bags","bag").replace(" ","").replace(".","").split("\n")

for r in rules_input:
    rule = r.split("contain")
    rules[rule[0]] = dict((bag[1:],int(bag[0])) for bag in rule[1].split(",") if bag[0] != "n" )

def getBags(rule):
    if not rule:
        return 1

    else:
        return sum([(getBags(rules[bag])*amount) for bag,amount in rule.items()])+1

t1 = time.time()

amount = getBags(rules["shinygoldbag"])-1

t2 = time.time()
print("time =", t2 - t1)

print(amount)

#prints: 27526