with open("3-input.txt") as fin:
    data = fin.read()
    
tmap = data.split("\n")

width = len(tmap[0])
height = len(tmap)

pos = [0, 0]
trees = 0

while pos[0] < height:
    trees += tmap[pos[0]][pos[1]] == "#"
    pos[1] = (pos[1] + 3) % width
    pos[0] += 1
        
print(trees)