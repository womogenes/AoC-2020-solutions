with open("24_input.txt") as fin:
    data = fin.read().split("\n")

dirs = {
    "e": (1, 0),
    "w": (-1, 0),
    "ne": (1, -1),
    "nw": (0, -1),
    "se": (0, 1),
    "sw": (-1, 1)
}

def get_coords(line):
    index = 0
    x, y = 0, 0
    while index < len(line):
        if index < len(line) - 1 and line[index:index + 2] in dirs:
            chars = line[index:index + 2]
            index += 2

        elif line[index] in dirs:
            chars = line[index]
            index += 1

        #print(chars, end=" ")
        changes = dirs[chars]

        x += changes[0]
        y += changes[1]

    return x, y

def count_neighbors(coords):
    total = 0
    for neighbor_coords in get_neighbors(coords):
        if neighbor_coords in black:
            total += 1

    return total

def get_neighbors(coords):
    # Return a list of neighboring coords
    result = []
    for direction in dirs:
        changes = dirs[direction]
        neighbor_coords = (coords[0] + changes[0], coords[1] + changes[1])
        result.append(neighbor_coords)

    return result

def iterate():
    stack = set()
    visited = set()
    new_black = black.copy()

    for tile in black:
        stack.add(tile)
        stack.update(get_neighbors(tile))

    while len(stack) > 0:
        coords = stack.pop()
        if coords in visited:
            continue
    
        visited.add(coords)
        
        neighbor_count = count_neighbors(coords)
        if coords in black and (neighbor_count == 0 or neighbor_count > 2):
            new_black.remove(coords)

        elif coords not in black and (neighbor_count == 2):
            new_black.add(coords)

    return new_black


# Do the initial flips
black = set()
for line in data:
    coords = get_coords(line)
    if coords in black:
        black.remove(coords)
    else:
        black.add(coords)


for _ in range(100):
    black = iterate()

print(len(black))