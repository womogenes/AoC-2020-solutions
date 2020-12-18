with open("17_input.txt") as fin:
    data = fin.read()

def next_state(state):
    # Return the next state given the current state
    # State is represented by a big enough 3-dimensional matrix

    minz = 0
    maxz = len(state) - 1
    
    miny = 0
    maxy = len(state[0]) - 1

    minx = 0
    maxx = len(state[0][0]) - 1

    minw = 0
    maxw = len(state[0][0][0]) - 1

    newState = [[[["." for _ in range(maxx + 1)] for _ in range(maxy + 1)] for _ in range(maxz + 1)] for _ in range(maxw + 1)]

    for w in range(minw, maxw + 1):
        for x in range(minx, maxx + 1):
            for y in range(miny, maxy + 1):
                for z in range(minz, maxz + 1):
                        neighbors = 0

                        # Find all 26 surrounding cubes
                        for dw in range(-1, 2):
                            for dx in range(-1, 2):
                                for dy in range(-1, 2):
                                    for dz in range(-1, 2):
                                        xx = x + dx
                                        yy = y + dy
                                        zz = z + dz
                                        ww = w + dw

                                        if not (minx <= xx <= maxx and miny <= yy <= maxy and minz <= zz <= maxz and minw <= ww <= maxw):
                                            continue

                                        if dx == 0 and dy == 0 and dz == 0 and dw == 0:
                                            continue
                                        
                                        neighbors += state[ww][zz][yy][xx] == "#"

                        if state[w][z][y][x] == "#" and (not neighbors in [2, 3]):
                            newState[w][z][y][x] = "."

                        elif state[w][z][y][x] == "." and neighbors == 3:
                            newState[w][z][y][x] = "#"

                        else:
                            newState[w][z][y][x] = state[w][z][y][x]

    return newState

# Usually hard-coded stuff is bad but it works here
n = len(data.split("\n"))
size = 20

inputState = data.split("\n")
state = [[[["." for i in range(size)] for j in range(size)] for k in range(size)] for l in range(size)]

# Fill in our grid
for y in range(size // 2, size // 2 + n):
    for x in range(size // 2, size // 2 + n):
        state[size // 2][size // 2][y][x] = inputState[y - size // 2][x - size // 2]

count = 0
for i in range(6):
    state = next_state(state).copy()
    print(f"Finished iteration {i + 1}")


count = 0
for cube in state:
    for layer in cube:
        for row in layer:
            for hypercube in row:
                count += hypercube != "."

print(count)