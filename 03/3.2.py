with open("3-input.txt") as fin:
    data = fin.read()
    
tmap = data.split("\n")

width = len(tmap[0])
height = len(tmap)

def count_trees(yslope, xslope):
    pos = [0, 0]
    trees = 0

    while pos[0] < height:
        trees += tmap[pos[0]][pos[1]] == "#"
        pos[1] = (pos[1] + xslope) % width
        pos[0] += yslope
    
    return trees
        
slopes = [
    (1, 1),
    (1, 3),
    (1, 5),
    (1, 7),
    (2, 1)
]

prod = 1
for yslope, xslope in slopes:
    prod *= count_trees(yslope, xslope)
    
print(prod)