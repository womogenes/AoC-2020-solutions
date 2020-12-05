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
ids = []
for p in passes:
    ids.append(get_id(p))

ids.sort()
minID = ids[0]
maxID = ids[-1]

for i in range(len(ids) - 1):
    if ids[i] + 1 != ids[i + 1]:
        print(ids[i] + 1)
        break