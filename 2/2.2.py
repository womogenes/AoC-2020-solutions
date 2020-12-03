with open("2-input.txt") as fin:
    data = fin.read()
    
valid = 0
lines = data.split("\n")

def is_valid(line):
    x = line.split(" ")
    pos = [int(i) for i in x[0].split("-")]
    char = x[1][0]
    password = x[2]
    
    return (password[pos[0] - 1] == char) ^ (password[pos[1] - 1] == char)
    
for l in lines:
    valid += is_valid(l)
    
print(valid)

"""
EXCLUSIVE OR: XOR
   0  1
0  0  1
1  1  0
"""