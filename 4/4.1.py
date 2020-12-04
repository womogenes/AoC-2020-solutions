import re

with open("4-input.txt") as fin:
    data = fin.read()
    
passports = data.split("\n\n")

fields = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    "cid"
]

def is_valid(passport):
    fCopy = set(fields)
    fList = re.split(" |\n", passport)
    print(repr(fList))
    for f in fList:
        key = f[:f.index(":")]
        fCopy.remove(key)
    
    if len(fCopy) == 1:
        return fCopy.pop() == "cid"
    
    return len(fCopy) == 0

total = 0
for p in passports:
    total += is_valid(p)

print(total)