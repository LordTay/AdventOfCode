#Solution of Day2

file_path = "./input1"

try:
    f = open(file_path,"r")
except Exception as e:
    print("Exception: ",e)

class Password:
    def __init__(self, password, letter, amount):
        self.password = password
        self.letter = letter
        self.amount = amount
    def isValid(self):
        return (self.password[self.amount[0]-1]==self.letter) != (self.password[self.amount[1]-1]==self.letter)

l = []

string = ""
for i in f:
    string = i
    pw = string[string.index(":")+2:-1]
    letter = string[string.index(":")-1]
    amount = string[:string.index(":")-2].split("-")

    l.append(Password(pw,letter,(int(amount[0]),int(amount[1]))))
n_valid_passwords = 0

for p in l:
    if p.isValid(): 
        n_valid_passwords+=1

print(n_valid_passwords)