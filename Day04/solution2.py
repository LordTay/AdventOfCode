#Solution Part2 of Day4

# Time:
# 5.5ms

import re
import time

file_path = "./input1"
req_fields=["byr", "iyr", "eyr", "hgt" , "hcl", "ecl", "pid"]
l=[]
count = 0

regex_fields={  "byr" : "(19[2-9][0-9]|200[0-2])$",                                 # 1920 - 2002
                "iyr" : "(201[0-9]|2020)$",                                         # 2010 - 2020
                "eyr" : "(202[0-9]|2030)$",                                         # 2020 - 2030
                "hgt" : "((1[5-8][0-9]|19[0-3])[c][m])|(59|6[0-9]|7[0-6])[i][n]$",  # 150 - 193cm or 59 - 76 inch
                "hcl" : "#[0-f]{6}",                                                # #xxxxxx  x - hex digit lower case
                "ecl" : "amb|blu|brn|gry|grn|hzl|oth$",                             # one of amb blu brn gry grn hzl oth
                "pid" : "[0-9]{9}$",                                                # nine-digit number
                "cid" : ".*"}                                                       # anything

class Passport:
    def __init__(self, pw_data):
        self.pp ={}
        for field in [field.split(":") for field in pp_data.split(" ")]:
            self.pp[field[0]] = field[1]

    def isValid(self):
        req_field_allpresent = all(field in self.pp for field in req_fields) 
        req_field_allvalid = all(re.match(regex_fields[f_key],f_value) for f_key,f_value in self.pp.items())
        return req_field_allpresent & req_field_allvalid

t1 = time.time()
with open(file_path,"r") as f:
    pp_data_all = [string.replace("\n"," ") for string in f.read().split("\n\n") ]

for pp_data in pp_data_all:
    l.append(Passport(pp_data))

for pp in l:   
    if pp.isValid(): count += 1

t2 = time.time()
print("time =",t2 - t1) 

print(count)

#prints:101