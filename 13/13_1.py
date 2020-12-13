import math

with open("13_input.txt") as fin:
    data = fin.read().split("\n")

# Earliest timestamp we could leave at
earliest = int(data[0])

busIDs = data[1].split(",")
buses = []
for i in busIDs:
    if i.isnumeric():
        buses.append(int(i))

earliestLeave = 1 << 60
bestBus = -1
for b in buses:
    nextLeave = b * math.ceil(earliest / b)
    if nextLeave < earliestLeave:
        bestBus = b
        earliestLeave = nextLeave

toWait = earliestLeave - earliest
print(bestBus * toWait)