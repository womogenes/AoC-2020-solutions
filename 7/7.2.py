from pprint import pprint

with open("7-input.txt") as fin:
    data = fin.read()

tree = {}

rule = "clear tomato bags contain 4 dotted magenta bags, 1 dull chartreuse bag, 2 dim aqua bags, 1 dull brown bag."

def add_parents(rule):
    split = rule.split(" ")
    parent = " ".join(split[:split.index("contain") - 1])

    if not parent in tree:
        tree[parent] = set()

    childList = " ".join(split[split.index("contain") + 1:]).split(", ")
    for cString in childList:
        if cString == "no other bags.":
            continue

        parts = cString.split(" ")
        amount = int(parts[0])
        bagName = " ".join(parts[1:-1])
        tree[parent].add((amount, bagName))


rules = data.split("\n")
for r in rules:
    add_parents(r)

answer = 0
dfs = [(1, "shiny gold")]
seen = set()

while len(dfs) > 0:
    amount, color = dfs.pop()
    answer += amount

    #seen.add(pop)
    
    if color in tree:
        children = tree[color]
        for n, child in children:
            dfs.append((n * amount, child))


print(answer - 1)