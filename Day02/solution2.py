#Solution Part2 of Day2

# Time:
# 4.5ms

import time

file_path = "./input1"
l = []

class Password:
    def __init__(self, password, letter, amount):
        self.password = password
        self.letter = letter
        self.amount = amount
    def isValid(self):
        return (self.password[self.amount[0]-1]==self.letter) != (self.password[self.amount[1]-1]==self.letter)


t1 = time.time()
with open(file_path,"r") as f:
    for i in f:
        string = i
        pw, letter, amount = string[string.index(":")+2:-1], string[string.index(":")-1], string[:string.index(":")-2].split("-")

        l.append(Password(pw,letter,(int(amount[0]),int(amount[1]))))

n_valid_passwords = 0
for p in l:
    if p.isValid(): 
        n_valid_passwords+=1

t2 = time.time()
print("time =", t2 - t1)

print(n_valid_passwords)

#Output: 388