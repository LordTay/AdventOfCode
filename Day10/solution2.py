#Solution Part1 of Day10
import time

file_path = "./input1"

t1 = time.time()
with open(file_path,"r") as f:
    numbers = [int(n) for n in f.read().split("\n")]
t1 = time.time()
dp = {}

def dpHeader(numbers,index):
    if index in dp:
        return dp[index]
    dp[index] = getWays(numbers,index)
    return dp[index]

def getWays(numbers,index):
    if index >= len(numbers)-1: 
        #print("1")
        return 1
    #if index >= 15: return 1    
    ret = [dpHeader(numbers,i) for i in range(index+1,index+4) if i<len(numbers) and numbers[i]-numbers[index]<=3]
    return sum(ret)
            #print(numbers[i],"from ", numbers[index])
            
numbers.append(0)

numbers.sort()

t2=time.time()

print(getWays(numbers,0))

print("time",t2 - t1)