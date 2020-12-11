with open("11-input.txt") as fin:
    data = fin.read()

# Function to iterate to next state
def next_state(layout):
    rows = len(layout)
    cols = len(layout[0])

    # Variable to determine if state changes
    modified = False

    newLayout = [[None for i in range(cols)] for j in range(rows)]

    for r in range(rows):
        for c in range(cols):
            # Analyzing seat in position (r, c)
            if layout[r][c] == ".":
                newLayout[r][c] = "."
                
            else:
                occupiedAround = 0
                for dr in range(-1, 2):
                    for dc in range(-1, 2):
                        if dr == dc == 0: continue

                        # Surrounding seat at (rr, cc)
                        rr = r
                        cc = c
                        while True:
                            rr += dr
                            cc += dc
                            if (not 0 <= rr < rows) or (not 0 <= cc < cols): break

                            if layout[rr][cc] != ".":
                                occupiedAround += layout[rr][cc] == "#"
                                break

                if layout[r][c] == "L" and occupiedAround == 0:
                    modified = True
                    newLayout[r][c] = "#"

                elif layout[r][c] == "#" and occupiedAround >= 5:
                    modified = True
                    newLayout[r][c] = "L"

                else:
                    newLayout[r][c] = layout[r][c]

    return newLayout, modified

def count_occupied(layout):
    count = 0
    for i in layout:
        for j in i:
            count += j == "#"

    return count

layout = data.split("\n")
modified = True

while modified:
    layout, modified = next_state(layout)
    #print("\n" * 2)
    #print("\n".join(["".join(x) for x in layout]))

print(count_occupied(layout))