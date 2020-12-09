#Solution Part1 of Day9
import time

file_path = "./input1"

preambleLen = 25

t1 = time.time()
with open(file_path,"r") as f:
    numbers = [int(n) for n in f.read().split("\n")]

currNumbers = set()

for i in range(0,preambleLen):
    currNumbers.add(numbers[i])

for i in range(preambleLen,len(numbers)):
    target = numbers[i]
    if all([target-item not in currNumbers for item in currNumbers]):
        invalidNumber = target
        break
    currNumbers.add(target)  
    currNumbers.remove(numbers[i-preambleLen])


t2 = time.time()

print("Part1: ")

print(invalidNumber)
print("\nPart1 time:",t2 - t1)