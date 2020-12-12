with open("5-input.txt") as fin:
    data = fin.read()

def get_id(boardingPass):
    # Get the row number first
    row = 0
    for i in range(7):
        if boardingPass[i] == "B":
            row += 1 << (6 - i)
    
    col = 0
    for i in range(3):
        if boardingPass[i + 7] == "R":
            col += 1 << (2 - i)

    return row * 8 + col


passes = data.split("\n")
maxID = 0
for p in passes:
    maxID = max(maxID, get_id(p))

print(maxID)