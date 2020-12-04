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
    for f in fList:
        key = f[:f.index(":")]
        value = f[f.index(":") + 1:]
        
        # LOTS OF CHECKS
        if key == "byr":
            if not 1920 <= int(value) <= 2002:
                return False
                
        elif key == "iyr":
            if not 2010 <= int(value) <= 2020:
                return False
                
        elif key == "eyr":
            if not 2020 <= int(value) <= 2030:
                return False
                
        elif key == "hgt":
            if not value[-2:] in ["in", "cm"]:
                return False
                
            if value[-2:] == "in":
                if not 59 <= int(value[:-2]) <= 76:
                    return False
                    
            else:
                if not 150 <= int(value[:-2]) <= 193:
                    return False
                    
        elif key == "hcl":
            if not re.fullmatch("#([0-9]|[a-f]){6}", value):
                return False
                
        elif key == "ecl":
            if not re.fullmatch("amb|blu|brn|gry|grn|hzl|oth", value):
                return False
                
        elif key == "pid":
            if not re.fullmatch("[0-9]{9}", value):
                return False
        
        fCopy.remove(key)
    
    if len(fCopy) == 1:
        return fCopy.pop() == "cid"
    
    return len(fCopy) == 0

total = 0
for p in passports:
    total += is_valid(p)

print(total)