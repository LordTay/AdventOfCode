#Solution of Day4
import re
import time

file_path = "./input1"
req_fields=["byr", "iyr", "eyr", "hgt" , "hcl", "ecl", "pid"]
                                                                # nine-digit number
t1 = time.time()
class Passport:
    def __init__(self, pw_data):
        self.pp ={}
        for field in [field.split(":") for field in pp_data.split(" ")]:
            self.pp[field[0]] = field[1]

    def isValid(self):
        req_field_allpresent = all(field in self.pp for field in req_fields) 
        return req_field_allpresent

l=[]
count = 0
with open(file_path,"r") as f:
    pp_data_all = [string.replace("\n"," ") for string in f.read().split("\n\n") ]

for pp_data in pp_data_all:
    l.append(Passport(pp_data))

for pp in l:   
    if pp.isValid(): count += 1
      
print(count)
print("time =",time.time() - t1) 