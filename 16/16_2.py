with open("16_input.txt") as fin:
    data = fin.read().split("\n")

# First get all the fieldRanges
index = 0

fieldRanges = []

# Common technique; loops while the value at index is non-empty
while data[index]:
    splitted = data[index][data[index].index(":") + 2:].split(" ")
    range1 = [int(i) for i in splitted[0].split("-")]
    range2 = [int(i) for i in splitted[2].split("-")]
    
    fieldRanges.append([range1, range2])
    index += 1


allTickets = []

# Get to our own ticket
index += 2
ourTicket = [int(i) for i in data[index].split(",")]
allTickets.append(ourTicket)

while data[index] != "nearby tickets:":
    index += 1

index += 1

while index < len(data):
    ticket = [int(i) for i in data[index].split(",")]
    allTickets.append(ticket)

    index += 1

def scanning_error_rate(ticket, fieldRanges):
    errorRate = 0

    for value in ticket:
        exists = False
        for range1, range2 in fieldRanges:
            if range1[0] <= value <= range1[1] or \
               range2[0] <= value <= range2[1]:
                exists = True
                break

        if not exists:
            errorRate += value

    return errorRate

index = 0
while index < len(allTickets):
    if scanning_error_rate(allTickets[index], fieldRanges) > 0:
        # Invalid ticket!
        allTickets.pop(index)

    else:
        index += 1


# This list stores possible fieldRanges for each field, based on every nearby ticket
possiblefieldRanges = []

for fieldIndex in range(len(allTickets[0])): # 20 is the number of fields
    # Figure out WHICH FIELDS work for the ith position on each ticket
    fieldsThatWork = []

    for j in range(len(fieldRanges)):
        range1, range2 = fieldRanges[j]
        #print(j, range1, range2)
        fits = True

        for ticket in allTickets:
            #print(ticket[fieldIndex])
            if not (range1[0] <= ticket[fieldIndex] <= range1[1] or \
                    range2[0] <= ticket[fieldIndex] <= range2[1]):
                fits = False
                break

        if fits:
            fieldsThatWork.append(j)

    possiblefieldRanges.append(fieldsThatWork)

for pfr in possiblefieldRanges:
    print(pfr)


# Time for process of elimination!
finalRange = [-1] * 20

for i in range(len(finalRange)):
    # Find the ticket position that only has one possibility
    for position in range(len(allTickets[0])):
        if len(possiblefieldRanges[position]) == 1 and finalRange[position] == -1:
            break

    takenField = possiblefieldRanges[position][0]
    finalRange[position] = takenField

    # Remove this from all other positions' possibilities
    for other in range(len(possiblefieldRanges)):
        if other == position:
            continue

        if takenField in possiblefieldRanges[other]:
            possiblefieldRanges[other].remove(takenField)

print(finalRange)

prod = 1

# I'M ASSUMING THESE ARE THE FIRST SIX
for i in range(len(finalRange)):
    if finalRange[i] < 6:
        prod *= ourTicket[i]

print(prod)