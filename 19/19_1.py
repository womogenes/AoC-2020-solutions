import re
from functools import lru_cache
from pprint import pprint

with open("19_input.txt") as fin:
    data = fin.read().split("\n")

# Variable to keep track of rules
rules = {}

# Get all the rules
line = 0
while data[line] != "":
    number = int(data[line][:data[line].index(":")])
    rule = data[line][data[line].index(":") + 2:]
    rules[number] = rule
    line += 1

# Variable to keep track of regexes
regexes = {}

@lru_cache(None)
def to_regex(rule):
    # Converts "rule" to regex

    if "|" in rule:
        part1 = [int(i) for i in rule[:rule.index("|") - 1].split(" ")]
        part2 = [int(i) for i in rule[rule.index("|") + 2:].split(" ")]

        regex1 = "(" + ")(".join([get_regex(i) for i in part1]) + ")"
        regex2 = "(" + ")(".join([get_regex(i) for i in part2]) + ")"

        ans =  f"({regex1})|({regex2})"

    elif '"' in rule:
        ans =  rule[1]

    else:
        parts = [int(i) for i in rule.split(" ")]
        ans = "(" + ")(".join([get_regex(i) for i in parts]) + ")"

    return ans

def get_regex(number):
    # Gets regex based on id
    if number in regexes:
        return regexes[number]
    
    ans = to_regex(rules[number])
    regexes[number] = ans
    return ans


# Verify!
count = 0
line += 1
regex0 = get_regex(0)

pprint(regexes)

#print(regex0)

while line < len(data):
    matches = bool(re.fullmatch(regex0, data[line]))
    count += matches
    line += 1

print(count)