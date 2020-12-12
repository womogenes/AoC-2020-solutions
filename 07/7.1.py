from pprint import pprint

with open("7-input.txt") as fin:
    data = fin.read()

tree = {}

rule = "clear tomato bags contain 4 dotted magenta bags, 1 dull chartreuse bag, 2 dim aqua bags, 1 dull brown bag."

def add_parents(rule):
    split = rule.split(" ")
    parent = " ".join(split[:split.index("contain") - 1])

    childList = " ".join(split[split.index("contain") + 1:]).split(", ")
    for cString in childList:
        if cString == "no other bags.":
            continue

        parts = cString.split(" ")
        bagName = " ".join(parts[1:-1])
        if bagName not in tree:
            tree[bagName] = set()
        tree[bagName].add(parent)

rules = data.split("\n")
for r in rules:
    add_parents(r)

answer = []
dfs = ["shiny gold"]
seen = set()

while len(dfs) > 0:
    pop = dfs.pop()
    if pop in seen:
        continue

    seen.add(pop)
    if pop in tree:
        parents = tree[pop]
        for p in parents:
            dfs.append(p)

    else:
        answer.append(pop)


print(len(seen) - 1)