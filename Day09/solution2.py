#Solution Part2 of Day9
import time
import solution

file_path = "./input1"

#int(exec("solution.py").read())

#exec(open("solution.py").read())

#time 4ms with n = 1000
numbers = solution.numbers
invalidNumber = solution.invalidNumber

print("\nPart2: ")
t1 = time.time()

def findSublistAddingToSum(numbers,sum):
    prefixSum = {}
    sumSoFar = 0
    for index in range(len(numbers)):
        sumSoFar += numbers[index]

        if (sumSoFar - sum) in prefixSum:
            sublist_end_index = prefixSum[(sumSoFar - sum)]
            return numbers[sublist_end_index+1:index+1]

        prefixSum[sumSoFar]=index


sublist = findSublistAddingToSum(numbers,invalidNumber)

smallest = min(sublist)
largest = max(sublist)

t2 = time.time()

print(sublist)
print (smallest,"+",largest, "= ", smallest + largest)

print("\nPart2 time:",t2 - t1)

