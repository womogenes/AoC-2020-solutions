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

    newState = [[["." for _ in range(maxx + 1)] for _ in range(maxy + 1)] for _ in range(maxz + 1)]

    for x in range(minx, maxx + 1):
        for y in range(miny, maxy + 1):
            for z in range(minz, maxz + 1):
                neighbors = 0

                # Find all 26 surrounding cubes
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        for dz in range(-1, 2):
                            xx = x + dx
                            yy = y + dy
                            zz = z + dz

                            if not (minx <= xx <= maxx and miny <= yy <= maxy and minz <= zz <= maxz):
                                continue

                            if dx == 0 and dy == 0 and dz == 0:
                                continue
                            
                            neighbors += state[zz][yy][xx] == "#"

                if state[z][y][x] == "#" and (not neighbors in [2, 3]):
                    newState[z][y][x] = "."

                elif state[z][y][x] == "." and neighbors == 3:
                    newState[z][y][x] = "#"

                else:
                    newState[z][y][x] = state[z][y][x]

    return newState

# Usually hard-coded stuff is bad but it works here
n = len(data.split("\n"))
size = 50

def print_state(state):
    for layer in state:
        if count_active(layer) > 0:
            print("\n".join([" ".join(row) for row in layer]))
            print()

def count_active(layer):
    count = 0
    for i in layer:
        for j in i:
            count += j != "."

    return count

inputState = data.split("\n")
state = [[["." for i in range(size)] for j in range(size)] for k in range(size)]

# Fill in our grid
for y in range(size // 2, size // 2 + n):
    for x in range(size // 2, size // 2 + n):
        state[size // 2][y][x] = inputState[y - size // 2][x - size // 2]

print_state(state)
count = 0
for i in range(6):
    state = next_state(state).copy()

    print(f"Finished iteration {i + 1}")
    #print_state(state)
    #print()

count = 0
for layer in state:
    count += count_active(layer)

print(count)