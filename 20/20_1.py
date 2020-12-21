import collections

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

    if tileID == 1427:
        print(borders[tileID])


# Place the tiles!
grid = collections.defaultdict(lambda: None)
tile0 = list(tiles.keys())[0]

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
                    borders[other] = [b[::-1] for b in borders[other][::-1]]
                    #print("FLIPPED!", other)

                elif border[::-1] in borders[other]:
                    pass
                    #print("NORMAL!", other)

                otherSide = borders[other].index(border[::-1])
                found = True

                # Must match 4 - direction
                borders[other] = rotate(borders[other], (otherSide - (direction + 2) % 4) % 4)

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


minx = 100000
miny = 100000
maxx = -100000
maxy = -100000

for x, y in grid:
    minx = min(minx, x)
    maxx = max(maxx, x)
    miny = min(miny, y)
    maxy = max(maxy, y)

#print(dict(grid))

prod = 1
for x in minx, maxx:
    for y in miny, maxy:
        tileID = grid[(x, y)]
        #print(tileID)
        prod *= tileID

print(prod)