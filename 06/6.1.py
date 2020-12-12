with open("6-input.txt") as fin:
    data = fin.read()

def unique_questions(group):
    chars = set(group)
    if "\n" in chars:
        return len(chars) - 1

    return len(chars)

groups = data.split("\n\n")
total = 0
for g in groups:
    total += unique_questions(g)

print(total)