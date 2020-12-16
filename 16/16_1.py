with open("16_input.txt") as fin:
    data = fin.read().split("\n")

# First get all the ranges
index = 0

ranges = []

# Common technique; loops while the value at index is non-empty
while data[index]:
    splitted = data[index][data[index].index(":") + 2:].split(" ")
    range1 = [int(i) for i in splitted[0].split("-")]
    range2 = [int(i) for i in splitted[2].split("-")]
    
    ranges.append([range1, range2])
    index += 1
    

# Skip to the lines that contain nearby tickets
while data[index] != "nearby tickets:":
    index += 1

index += 1

nearbyTickets = []
while index < len(data):
    ticket = [int(i) for i in data[index].split(",")]
    nearbyTickets.append(ticket)

    index += 1

def scanning_error_rate(ticket, ranges):
    errorRate = 0

    for value in ticket:
        exists = False
        for range1, range2 in ranges:
            if range1[0] <= value <= range1[1] or \
               range2[0] <= value <= range2[1]:
                exists = True
                break

        if not exists:
            errorRate += value

    return errorRate

totalErrorRate = 0
for ticket in nearbyTickets:
    totalErrorRate += scanning_error_rate(ticket, ranges)

print(totalErrorRate)