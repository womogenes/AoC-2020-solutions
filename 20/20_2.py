import collections
from pprint import pprint
import copy

with open("20_input.txt") as fin:
    data = fin.read().split("\n")

# Get the tiles
tiles = {}
line = 0

tile = []
while line < len(data):
    tile = []
    tileID = int(data[line][data[line].index(" ") + 1:-1])
    for _ in range(10):
        line += 1
        tile.append(data[line])

    tiles[tileID] = tile

    line += 2

# Get borders
borders = {}
for tileID in tiles:
    tile = tiles[tileID]
    border0 = tile[0]
    border2 = tile[-1][::-1]
    border1 = "".join([row[-1] for row in tile])
    border3 = "".join([row[0] for row in tile][::-1])

    borders[tileID] = [border0, border1, border2, border3]

# Place the tiles!
grid = collections.defaultdict(lambda: None)
tile0 = list(tiles.keys())[0]

# Rotation/flipped
rotations = { tile0: 1 }
flipped = { tile0: True }

stack = [(tile0, (0, 0))]
grid[(0, 0)] = tile0

used = {tile0}

# Rotation utility function
def rotate(l, n):
    return l[n:] + l[:n]

def dCoords(direction):
    if direction == 0:
        return 0, 1
    if direction == 1:
        return 1, 0
    if direction == 2:
        return 0, -1
    if direction == 3:
        return -1, 0

while len(stack) > 0:
    tileID, coords = stack.pop()

    # Search in all 4 directions
    for direction in range(4):
        border = borders[tileID][direction]

        #print(tileID, border, "DIRECTION:", direction)

        found = False
        for other in borders:
            if other in used:
                continue
            
            if border in borders[other] or border[::-1] in borders[other]:
                if border in borders[other]:
                    flipped[other] = False
                    borders[other] = [b[::-1] for b in borders[other][::-1]]
                    #print("FLIPPED!", other)

                elif border[::-1] in borders[other]:
                    flipped[other] = True
                    #print("NORMAL!", other)

                otherSide = borders[other].index(border[::-1])
                found = True

                # Must match 4 - direction
                drot = (otherSide - (direction + 2) % 4) % 4
                rotations[other] = (drot + 1) % 4
                borders[other] = rotate(borders[other], drot)

                #print(direction)
                #print(borders[other])
                #print(border)
                assert borders[other][(direction + 2) % 4] == border[::-1]

                coordsChange = dCoords(direction)
                newCoords = coords[0] + coordsChange[0], coords[1] + coordsChange[1]
                
                if newCoords in grid:
                    break

                #print(newCoords)

                grid[newCoords] = other
                stack.append((other, newCoords))
                used.add(other)


            if found:
                break


    #print(tileID)

for coords in grid:
    pass
    #print(coords, grid[coords])

for tileID in tiles:
    found = False
    for coords in grid:
        if tileID == grid[coords]:
            found = True
            break

    if not found:
        print(tileID)

# Now I'm just defining functions everywhere :(
def print_grid(grid):
    to_print = "\n".join(["".join(i) for i in grid])
    print(to_print.replace(".", " ").replace("#", "."))

# Utility function for rotating/flipping a grid
def transform(grid, rotation, flipped):
    size = len(grid) - 1
    assert len(grid) == len(grid[0])
    if flipped:
        # Account for some weirdness in flipping
        rotation = (rotation + 1) % 4
        grid = [line[::-1] for line in grid]

    else:
        rotation = (rotation + 2) % 4

    newGrid = [[char for char in line] for line in grid].copy()
    if rotation == 1:
        for row in range(size + 1):
            for col in range(size + 1):
                newGrid[row][col] = grid[size - col][row]

    elif rotation == 2:
        for row in range(size):
            for col in range(size + 1):
                newGrid[row][col] = grid[size - row][size - col]

    elif rotation == 3:
        for row in range(size + 1):
            for col in range(size + 1):
                newGrid[row][col] = grid[col][size - row]

    return newGrid

def remove_border(grid):
    return [line[1:-1] for line in grid[1:-1]]

for tileID in tiles:
    tiles[tileID] = remove_border(transform(tiles[tileID], rotations[tileID], flipped[tileID]))

minx = 100000
miny = 100000
maxx = -100000
maxy = -100000

for x, y in grid:
    minx = min(minx, x)
    maxx = max(maxx, x)
    miny = min(miny, y)
    maxy = max(maxy, y)

print(minx, maxx)
print(miny, maxy)

true_image = []
for row in range(8 * miny, 8 * (maxy + 1)):
    this_row = []
    for col in range(minx, maxx + 1):
        tileID = grid[(col, row // 8)]
        this_row += tiles[tileID][row % 8]

    """
        print("".join(tiles[tileID][row % 8]), end=" ")

    print()
    if row % 8 == 7:
        print()

    """
    true_image.append(this_row)

# Find sea monsters
monster = """
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
"""[1:-1].split("\n")
monster_height = len(monster)
monster_width = len(monster[0])

def find_monsters(image):
    height = len(image)
    width = len(image[0])

    modified_image = copy.deepcopy(image)
    has_monsters = False

    for row in range(height - monster_height):
        for col in range(width - monster_width):
            found = True
            for i in range(monster_height):
                for j in range(monster_width):
                    if (monster[i][j] == "#") and (image[row + i][col + j] != "#"):
                        found = False
                        break

            if found:
                has_monsters = True
                for i in range(monster_height):
                    for j in range(monster_width):
                        if monster[i][j] == "#":
                            assert image[row + i][col + j] == "#"
                            modified_image[row + i][col + j] = "O"


    return has_monsters, modified_image


for rot in range(4):
    for flip in [False, True]:
        transformed_image = transform(true_image, rot, flip)
        has_monsters, monsters_image = find_monsters(transformed_image)
        
        if has_monsters:
            print_grid(transformed_image)
            print("\n" * 3)
            print_grid(monsters_image)
            ans = 0
            for i in monsters_image:
                for j in i:
                    ans += j == "#"
            print(ans)