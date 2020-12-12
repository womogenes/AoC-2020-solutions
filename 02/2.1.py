with open("2-input.txt") as fin:
    data = fin.read()
    
valid = 0
lines = data.split("\n")

def is_valid(line):
    x = line.split(" ")
    amounts = [int(i) for i in x[0].split("-")]
    char = x[1][0]
    password = x[2]
    
    count = 0
    for i in password:
        count += i == char
        
    return amounts[0] <= count <= amounts[1]
    
for l in lines:
    valid += is_valid(l)
    
print(valid)