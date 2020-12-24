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

        print(chars, end=" ")
        changes = dirs[chars]

        x += changes[0]
        y += changes[1]

    return x, y


black = set()
for line in data:
    coords = get_coords(line)
    if coords in black:
        black.remove(coords)
    else:
        black.add(coords)

print(len(black))