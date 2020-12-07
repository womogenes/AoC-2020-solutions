import string

with open("6-input.txt") as fin:
    data = fin.read()

def all_questions(group):
    people = group.split("\n")
    count = 0
    for char in string.ascii_lowercase:
        presentInAll = True
        for p in people:
            if char not in p:
                presentInAll = False
                break
    
        count += presentInAll

    return count


groups = data.split("\n\n")
total = 0
for g in groups:
    total += all_questions(g)

print(total)